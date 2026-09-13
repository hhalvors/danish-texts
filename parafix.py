#!/usr/bin/env python3
"""parafix.py -- find and repair paragraph breaks destroyed by pagination.

THE BUG (fixed in paginate.py 2026-09-12; the damage outlives the fix)

`paginate.py apply` inserts its marker AT the nearest safe whitespace. Where a
page turn fell at a paragraph boundary the chosen spot could be the SECOND
newline of the "\\n\\n" pair, so the marker was written between the two newlines
and the blank line vanished -- two paragraphs silently became one.

Nothing downstream could see it. Braces balance, quotes balance, check.py is
happy, `paginate.py verify` passes, not a letter changes, and the document
compiles without a murmur. It destroyed 39 paragraph breaks in Den menneskelige
Tanke and 65 more across fourteen other books before anyone noticed, and it was
noticed only because a reader collating against the page images kept reporting
paragraph starts the transcription did not have.

HOW THIS COMPARES -- AND WHY IT IS EXACT

`apply` writes a `.bak` beside every file it touches, and that backup is the
pre-pagination state. Pagination changes no letters, so the two letter streams
must be identical; a paragraph boundary is then just an index into that stream,
and the before/after sets of indices can be compared outright.

That matters. Earlier attempts matched paragraphs by a fixed-length key taken
from a fixed window of CHARACTERS, and got it wrong twice: inserting a marker
shifts what falls inside the window, so the same paragraph yields a different
key before and after and reads as damaged when nothing is wrong. One version
reported 4,569 losses where the true number was 65. If you change this file,
keep the comparison in the letter stream, where markup cannot move anything.

    python3 parafix.py check                  # every paginated book
    python3 parafix.py check nielsen/videnskabslaere
    python3 parafix.py repair --all
    python3 parafix.py check                  # must print 0

A repair moves whitespace only: it writes its own .bak.parafix-* first, and
afterwards `check` must report zero and the book must still compile.

THE TRAP IN THE REPAIR ITSELF

A paragraph's first letter may sit inside a command argument -- `\\emph{Stumpf}
vil...`, `\\subsection*{c. Erindrings-...}`. Insert the blank line at the letter
and you split the argument across it, which no text-only check sees and only
the compiler catches. The insertion point is therefore walked back out of any
enclosing `\\command{`, and out of any page marker, before anything is written.
"""
import re, os, sys, glob, shutil, time, bisect, argparse

MARKER_ANY = re.compile(r"\\[oa]page\{\d+\}")
MARKER_END = re.compile(r"(\\[oa]page\{\d+\})\s*$")
CMD_OPEN   = re.compile(r"\\[a-zA-Z]+\*?\{\s*$")
PREAMBLE   = re.compile(r"%\s*-+ original-page markers \(paginate\.py\) -+\s*\n"
                        r"\\usepackage\{marginnote\}\s*\n\\newcommand\{\\opage\}[^\n]*\n"
                        r"\\newcommand\{\\apage\}[^\n]*\n")


def baseline_for(d):
    """The .bak `apply` wrote: the oldest one still carrying no page markers."""
    baks = sorted(glob.glob(os.path.join(d, "transcription.tex.bak.20*")))
    clean = [b for b in baks
             if not MARKER_ANY.search(open(b, encoding="utf-8", errors="replace").read())]
    return clean[0] if clean else None


def letter_map(body):
    """(letter stream, stream index -> char offset). Comments, command names and
    page markers contribute nothing, so the stream is identical before and after
    pagination."""
    buf, pos, i = [], [], 0
    while i < len(body):
        m = MARKER_ANY.match(body, i)
        if m: i = m.end(); continue
        c = body[i]
        if c == "%":
            j = body.find("\n", i); i = j if j != -1 else len(body); continue
        if c == "\\":
            j = i + 1
            while j < len(body) and body[j].isalpha(): j += 1
            i = j if j > i + 1 else i + 1; continue
        if c.isalnum(): buf.append(c.lower()); pos.append(i)
        i += 1
    return "".join(buf), pos


def analyse(txt, strip_preamble=False):
    body = txt.partition(r"\begin{document}")[2] or txt
    if strip_preamble: body = PREAMBLE.sub("", body)
    stream, pmap = letter_map(body)
    starts = []
    for m in re.finditer(r"\n[ \t]*\n", body):
        k = bisect.bisect_left(pmap, m.end())
        if k < len(pmap): starts.append(k)
    return body, stream, pmap, sorted(set(starts))


def compare(d):
    """(lost, spurious, body, pmap) or None / 'letters differ'."""
    bk = baseline_for(d)
    tex = os.path.join(d, "transcription.tex")
    if not bk or not os.path.exists(tex): return None
    _, sp, _, ip = analyse(open(bk, encoding="utf-8", errors="replace").read())
    cur = open(tex, encoding="utf-8", errors="replace").read()
    for strip in (False, True):
        body, sc, pmap, ic = analyse(cur, strip)
        if sc == sp:
            return ([i for i in ip if i not in set(ic)],
                    [i for i in ic if i not in set(ip)], body, pmap)
    return "letters differ"


def repair(d):
    r = compare(d)
    if r is None or r == "letters differ": return 0
    lost, _, _, _ = r
    if not lost: return 0
    tex = os.path.join(d, "transcription.tex")
    src = open(tex, encoding="utf-8", errors="replace").read()
    head, sep, body = src.partition(r"\begin{document}")
    fixed = 0
    while True:
        r = compare(d) if fixed == 0 else None
        break
    # re-derive after each insertion, since offsets move
    for _ in range(len(lost)):
        r = compare(d)
        if r is None or r == "letters differ": break
        lost_now, _, body_now, pmap_now = r
        if not lost_now: break
        i = lost_now[0]
        src = open(tex, encoding="utf-8", errors="replace").read()
        head, sep, body = src.partition(r"\begin{document}")
        off = pmap_now[i]
        start, j, marker = off, off, ""
        while True:
            k = j
            while j > 0 and body[j-1] in " \t\n": j -= 1
            m = MARKER_END.search(body[:j])
            if m and not marker: marker = m.group(1); j = m.start(); continue
            c = CMD_OPEN.search(body[:j])
            if c: j = c.start(); start = j; continue
            if j == k: break
        body = body[:j] + "\n\n" + (marker + " " if marker else "") + body[start:]
        if fixed == 0:
            shutil.copy2(tex, f"{tex}.bak.parafix-{time.strftime('%Y%m%d-%H%M%S')}")
        open(tex, "w", encoding="utf-8").write(head + sep + body)
        fixed += 1
    return fixed


def books(slugs):
    if slugs: return [os.path.join("texts", s) for s in slugs]
    return [os.path.dirname(t) for t in sorted(glob.glob("texts/*/*/transcription.tex"))]


def main():
    ap = argparse.ArgumentParser(description="find and repair paragraph breaks lost to pagination")
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check");  c.add_argument("slugs", nargs="*")
    r = sub.add_parser("repair"); r.add_argument("slugs", nargs="*"); r.add_argument("--all", action="store_true")
    a = ap.parse_args()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if a.cmd == "check":
        exact = tot = 0; odd = []
        for d in books(a.slugs):
            r = compare(d)
            if r is None: continue
            if r == "letters differ":
                odd.append((d, "letters differ from the backup — edited since pagination;"
                               " compare by hand")); continue
            lost, spurious, _, _ = r
            if not lost and not spurious: exact += 1; continue
            tot += len(lost)
            print(f"  {len(lost):>4} lost, {len(spurious)} spurious   {d.replace('texts/','')}")
        print(f"\n{exact} book(s) match the pre-pagination paragraph structure exactly; "
              f"{tot} break(s) lost")
        for d, why in odd: print(f"  note: {d.replace('texts/','')}: {why}")
        sys.exit(1 if tot else 0)
    if not a.slugs and not a.all: ap.error("give a slug, or --all")
    tot = 0
    for d in books(a.slugs):
        n = repair(d)
        if n: tot += n; print(f"  {d.replace('texts/',''):<44} restored {n}")
    print(f"\ntotal restored: {tot}\n  now run: python3 parafix.py check")


if __name__ == "__main__":
    main()
