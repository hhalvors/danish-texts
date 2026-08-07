#!/usr/bin/env python3
"""
build_frag.py <first_printed> <last_printed>  ->  .parts/pp<F>-<L>.texfrag

Builds the mechanical skeleton of a batch fragment straight from tesseract,
WITHOUT the text passing through a language model. The OCR carries the words;
a human (or an agent working from the page images) then adds what OCR cannot
see — italics, section heads, footnote placement — with small targeted edits.

Why this exists
---------------
TRANSCRIPTION-PLAYBOOK.md §2 says the OCR should carry the words and the image
only the structure. For a Fraktur book that meant a `sed` table of systematic
confusions. For this French journal it means something a bit more careful,
because `--psm 6` throws away the indentation that marks paragraph starts. So
we ask tesseract for TSV instead of plain text and recover the structure from
the geometry:

  - a LINE is a (block, par, line) group of words;
  - the BODY LEFT MARGIN is the modal left-x over all body lines;
  - a line whose left-x sits more than INDENT_FRAC of an em beyond that margin
    is a PARAGRAPH START;
  - a line whose glyph height is well under the body median is FOOTNOTE-sized;
  - the RUNNING HEAD is the topmost line, matched against the two forms this
    journal actually sets (verso: "<n> REVUE DE MÉTAPHYSIQUE ET DE MORALE.";
    recto: "H. HÖFFDING. — PASCAL ET KIERKEGAARD. <n>").

Everything the script cannot decide is left as an explicit `% TODO` comment
rather than guessed at, so nothing silently enters the transcription unchecked.

Requires TESSDATA_PREFIX to point at a directory holding fra.traineddata.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import pagemap  # noqa: E402

DPI = 300
# Left-edge jitter from page skew and OCR is about +/-20 px at 300 dpi, while a
# real paragraph indent is ~50-60 px. So the threshold has to clear the jitter:
# 0.7 * median line height (~49 px) ~= 34 px sits comfortably between the two.
INDENT_FRAC = 0.55             # of the median line HEIGHT, not character width
FOOTNOTE_HEIGHT_RATIO = 0.82   # line height below this * median => small type
FOOTNOTE_ZONE = 0.72           # ...and only if it sits below this fraction of
                               #    the page's text block. Both must hold: the
                               #    running head is small AND at the top, and we
                               #    do not want it mistaken for a footnote.

HEAD_VERSO = re.compile(r"^\s*\d{1,4}\s+REVUE\s+DE\s+M[EÉ]TAP", re.I)
HEAD_RECTO = re.compile(r"^\s*H\.?\s*H[ÖO]FFDING", re.I)
SIGNATURE = re.compile(r"^\s*Rev\.?\s*M[ée]ta\.?\s*[—-]", re.I)


def tsv_for(pdfpage: int, scan: str, tmp: Path) -> str:
    png = tmp / f"pg{pdfpage}"
    subprocess.run(
        ["pdftoppm", "-f", str(pdfpage), "-l", str(pdfpage), "-r", str(DPI),
         "-png", "-singlefile", scan, str(png)],
        check=True, capture_output=True)
    out = subprocess.run(
        ["tesseract", f"{png}.png", "stdout", "-l", "fra", "--psm", "6", "tsv"],
        check=True, capture_output=True, text=True)
    return out.stdout


def lines_from_tsv(tsv: str):
    """-> [(left, top, height, text, [low_conf_words])] in reading order."""
    groups = defaultdict(list)
    for row in tsv.splitlines()[1:]:
        f = row.split("\t")
        if len(f) < 12 or not f[11].strip():
            continue
        key = (int(f[2]), int(f[3]), int(f[4]))      # block, par, line
        groups[key].append({
            "left": int(f[6]), "top": int(f[7]),
            "h": int(f[9]), "conf": float(f[10]), "text": f[11],
        })
    out = []
    for key in sorted(groups, key=lambda k: min(w["top"] for w in groups[k])):
        ws = sorted(groups[key], key=lambda w: w["left"])
        text = " ".join(w["text"] for w in ws)
        low = [w["text"] for w in ws if 0 <= w["conf"] < 70]
        out.append((min(w["left"] for w in ws),
                    min(w["top"] for w in ws),
                    sorted(w["h"] for w in ws)[len(ws) // 2],
                    text, low))
    return out


def median(xs):
    xs = sorted(xs)
    return xs[len(xs) // 2] if xs else 0


def build_page(printed: int, scan: str, tmp: Path):
    lines = lines_from_tsv(tsv_for(pagemap.pdfpage(printed), scan, tmp))
    if not lines:
        return [f"% --- p. {printed} ---", f"% TODO p.{printed}: OCR returned nothing."]

    out = [f"% --- p. {printed} ---"]
    notes = []

    # Every printed page of this article except p. 221 carries a running head,
    # and it is always the topmost line. Drop it positionally rather than by
    # regex: marginal specks routinely glue a stray "[", "{" or "C" onto the
    # front of the line and defeat an anchored pattern. But assert that what we
    # dropped really does look like a head, and say so loudly if it does not —
    # silently swallowing a line of text would be a corruption.
    HEADISH = re.compile(r"REVUE|FFDING|KIER[RK]EGAARD|M[EÉ]TAP", re.I)
    dropped = 0
    while lines and dropped < 3:
        text = lines[0][3]
        if HEADISH.search(text):
            lines = lines[1:]
            dropped += 1
            break                               # the head itself; stop here
        if len(text.strip()) <= 3 and not re.search(r"\w{2}", text):
            # a marginal speck above the head ("#", "[", "C") — discard and
            # keep looking, otherwise it displaces the head-drop and the head
            # leaks into the body text.
            lines = lines[1:]
            dropped += 1
            continue
        notes.append(f"% TODO p.{printed}: no running head found at the top of this "
                     f"page; nothing was dropped. Topmost line: {text.strip()!r}")
        break
    if not lines:
        return out + notes

    body_h = median([h for _, _, h, _, _ in lines])
    margin = median([l for l, _, _, _, _ in lines])   # median, not modal:
    # the modal left is unstable (top count was only 4 of 39 lines on p. 230),
    # whereas indented lines are always a small minority, so the median sits on
    # the body margin.
    tops = [t for _, t, _, _, _ in lines]
    lo, hi = min(tops), max(tops)
    span = max(hi - lo, 1)

    for left, top, h, text, low in lines:
        if SIGNATURE.match(text):
            notes.append(f"% printer's signature line at foot of p.{printed}: {text.strip()}")
            continue
        if h < body_h * FOOTNOTE_HEIGHT_RATIO and (top - lo) / span > FOOTNOTE_ZONE:
            notes.append(f"% FOOTNOTE-sized line on p.{printed} (place with \\footnote{{}}): {text.strip()}")
            continue
        if left > margin + INDENT_FRAC * body_h and out[-1] != "":
            out.append("")                      # paragraph break
        if low:
            notes.append(f"% low-confidence on p.{printed}: {', '.join(low)}")
        out.append(text)

    return out + ([""] + notes if notes else [])


def dehyphenate(lines):
    """Join words broken across a line end. Leaves an em-dash line end alone."""
    out = []
    for line in lines:
        if out and out[-1].endswith("-") and not out[-1].endswith("--") and line and line[0].islower():
            out[-1] = out[-1][:-1] + line.split(" ", 1)[0]
            rest = line.split(" ", 1)[1] if " " in line else ""
            if rest:
                out.append(rest)
        else:
            out.append(line)
    return out


def main():
    first, last = int(sys.argv[1]), int(sys.argv[2])
    scan = pagemap.scan_path()
    if not os.environ.get("TESSDATA_PREFIX"):
        raise SystemExit("set TESSDATA_PREFIX to a directory containing fra.traineddata")
    tmp = Path(tempfile.mkdtemp())              # never render inside the repo
    try:
        body = []
        for p in range(first, last + 1):
            body += build_page(p, scan, tmp) + [""]
        body = dehyphenate(body)
        dest = HERE / ".parts" / f"pp{first}-{last}.texfrag"
        dest.parent.mkdir(exist_ok=True)
        header = [
            f"% Mechanical OCR skeleton for pp. {first}--{last}, built by build_frag.py.",
            "% Words from tesseract -l fra; structure from TSV geometry.",
            "% STILL TO DO BY EYE, against the page images:",
            "%   italics (OCR cannot see them), section heads, footnote placement,",
            "%   guillemet spacing, printer's defects.",
            "",
        ]
        dest.write_text("\n".join(header + body) + "\n", encoding="utf-8")
        print(f"wrote {dest.relative_to(HERE)}  ({len(body)} lines)")
        print("now verify by eye, then: python3 splice.py && python3 check.py")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
