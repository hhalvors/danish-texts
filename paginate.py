#!/usr/bin/env python3
"""paginate.py — put recoverable printed-page markers into a transcription.

Most transcriptions carry no record of where the original's pages fell, so a
search hit in them cannot be cited and a reader of the PDF cannot find the
passage in the original. This puts the pagination into the document, as the
marginal [N] that Møller's volumes already use.

    ./paginate.py status                     # the work queue, worst first
    ./paginate.py convert nielsen/religionsphilosophie   # comments -> visible
    ./paginate.py probe hoeffding/menneskelige-tanke     # writes nothing
    ./paginate.py apply hoeffding/menneskelige-tanke
    ./paginate.py verify hoeffding/menneskelige-tanke

Two routes, and choosing the wrong one loses work:

  convert  for a book whose pages are already recorded as comments. Those were
           established at the image by a person; this makes them visible and
           recomputes nothing. \opage, because a person set them.
  probe /  for a book with no usable pagination. This derives it by aligning
  apply    against the scan. \apage, because a machine set them.

Always probe before apply: probe writes nothing and prints what apply would do.

HOW IT WORKS

1. The offset between scan page and printed page is *measured*, not assumed.
   Printed folios are read out of the scan's own running heads, kept only when
   neighbouring pages agree, and forced monotonic. It cannot be derived from
   the alignment itself — every offset appears to match, because each scan
   page's text occurs somewhere in the transcription whatever number we give
   it — so a book whose folios cannot be read gets no automatic offset and
   must be given one with --offset.

2. Both texts are reduced to a bare lowercase letter-stream. Hyphenation, line
   breaks, letterspacing, LaTeX markup and punctuation all differ between the
   OCR and the transcription; the sequence of letters does not.

3. For each printed page, several anchors are taken from its scan text — from
   a few starting lines, since a running head may not appear in the
   transcription, and from further in, since any one window may sit on an OCR
   error — and the first that lands in the stream fixes that page's position.

4. Markers go in at the nearest paragraph boundary. A paragraph straddling a
   page break therefore carries the page it begins on, which is the same
   convention SKS entries follow, so a citation can be one page early for
   material at a long paragraph's end. Say so when it matters.

WHAT IT WILL NOT DO

It will not silently overwrite. apply keeps a .bak, marks every inserted line
[auto] so a later run can replace them and a reader can tell them from
hand-made ones, and never touches a line that is not a comment. Verify the
result, then commit it yourself.
"""

import argparse, os, re, subprocess, sys, glob, time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
TEXTS = os.environ.get("DANISH_TEXTS") or os.path.join(HERE, "texts")
BIB = os.path.expanduser(os.environ.get("BIBLIOTEK") or "~/bibliotek")
# \apage, not \opage: both render as a marginal [N] and both are read by the
# search index, but the edition should record which page numbers were read at
# the image and which were placed by machine alignment. Promote an \apage to
# \opage when you have checked it against the page.
# \apage, not \opage: both render as a marginal [N] and both are read by the
# search index, but an edition should record which page numbers were read at
# the image and which were placed by machine alignment against the scan.
# Promote an \apage to \opage once you have checked it against the page.
MARK = "\\apage{%d}"
MARK_OPAGE = "\\opage{%d}"
# Three comment conventions record printed pages in this corpus:
#   % ---- printed p.110 (PDF 35) ----   (21 books)
#   % --- p. 110 ---                     (26 books)
#   % p. 110                             (3 books)
# Each alternative below demands that the page number be the whole content of
# the line -- fenced by dashes on BOTH sides, or followed by the (PDF n) of the
# printed form, or by nothing at all. That is what separates a marker from the
# far commoner annotations that merely mention a page: "% p. 110 bears ONE
# footnote", "% p.174 --- THE LONGEST SPACED RUN", "% printed p. 121. Verified
# at 300 dpi." A one-sided dash is prose, not pagination.
MARK_COMMENT = re.compile(
    r"^%+[ \t]*(?:"
    r"-{2,}[ \t]*p\.?[ \t]*(\d+)[ \t]*-{2,}[ \t]*$"
    r"|-*[ \t]*printed[ \t]+p\.?[ \t]*(\d+)"
    r"(?=[ \t]*(?:\([Pp][Dd][Ff][ \t]*\d+\)|-{2,}|$))"
    r"|p\.?[ \t]*(\d+)[ \t]*$"
    r")",
    re.I | re.M)


def mark_page(m):
    """The page number from a MARK_COMMENT match, whichever form matched."""
    return int(next(g for g in m.groups() if g is not None))


MARK_INLINE = re.compile(r"\\[oa]page\{(\d+)\}")
AUTO_INLINE = re.compile(r"\\apage\{(\d+)\}")
PREAMBLE = (
    "\\usepackage{marginnote}\n"
    "\\newcommand{\\opage}[1]{\\marginnote{\\footnotesize\\textit{[#1]}}}\n"
    "\\newcommand{\\apage}[1]{\\marginnote{\\footnotesize\\textit{[#1]}}}\n")


# A transcription's preamble comments discuss the document's own structure, so
# "\\begin{document}" appears inside a % comment in three books before the real
# one. str.partition finds the comment, which silently made the preamble's tail
# part of the body -- splitting the comment line and un-commenting its
# remainder. Split only on an occurrence that no % precedes on its line.
BEGIN_DOC = re.compile(r"^(?:[^%\n]|\\%)*\\begin\{document\}", re.M)


def split_document(src):
    """(preamble, body) split at the real \\begin{document}, or ("", src)."""
    m = BEGIN_DOC.search(src)
    if not m:
        return "", src
    cut = src.index(r"\begin{document}", m.start())
    return src[:cut], src[cut + len(r"\begin{document}"):]


def page_marks(body):
    """Every printed-page mark in the file, in either form, with its position."""
    out = [(m.start(), mark_page(m)) for m in MARK_COMMENT.finditer(body)]
    out += [(m.start(), int(m.group(1))) for m in MARK_INLINE.finditer(body)]
    return sorted(out)


# ----------------------------------------------------------------- the texts

def book_dir(slug):
    d = os.path.join(TEXTS, slug)
    if not os.path.isdir(d):
        sys.exit(f"No such book: {slug}")
    return d


def find_scan(d, given=None):
    """The scan this transcription was made from."""
    if given:
        p = os.path.expanduser(given)
        return p if os.path.exists(p) else sys.exit(f"No scan at {p}")
    local = os.path.join(d, "scan.pdf")
    if os.path.exists(local):
        return local
    # Where it came from is recorded in prose, in RESUME-NOTES.md or in the
    # comment header of the transcription itself, e.g.
    #   Scan: ~/bibliotek/Høffding, Harald/den-menneskelige-tanke.pdf
    blob = ""
    # Read the whole notes file, not a prefix of it: the source is as often
    # recorded at the end (in a "Scan:" line added later) as in the header.
    for name in ("RESUME-NOTES.md", "transcription.tex"):
        f = os.path.join(d, name)
        if os.path.exists(f):
            blob += open(f, encoding="utf-8", errors="replace").read()
    for m in re.finditer(r"~?/?(?:Users/[^/]+/)?bibliotek/(.+?\.pdf)", blob):
        cand = os.path.join(BIB, m.group(1).strip())
        if os.path.exists(cand):
            return cand
    return None


def letters_map(body):
    """Letter-stream of the body, plus stream-index -> byte-offset map."""
    buf, pos, i = [], [], 0
    while i < len(body):
        c = body[i]
        if c == "\\":                       # skip over a LaTeX command name
            j = i + 1
            while j < len(body) and body[j].isalpha():
                j += 1
            i = j if j > i + 1 else i + 1
            continue
        if c.isalnum():
            buf.append(c.lower())
            pos.append(i)
        i += 1
    return "".join(buf), pos


def norm(s):
    s = re.sub(r"\\[a-zA-Z]+\s*", " ", s)
    return re.sub(r"[^0-9A-Za-zÀ-ɏÆØÅæøå]", "", s).lower()


# ------------------------------------------------------------ reading the scan

def pdf_pages(path):
    r = subprocess.run(["pdftotext", "-q", path, "-"],
                       capture_output=True, text=True, timeout=900)
    if not r.stdout:
        return []
    pp = r.stdout.split("\f")
    if pp and not pp[-1].strip():
        pp.pop()
    return pp


BARE = re.compile(r"^(\d{1,4})$")
EDGE = re.compile(r"^(\d{1,4})\b|\b(\d{1,4})$")


def folio_candidates(page):
    lines = [l.strip() for l in page.splitlines() if l.strip()]
    if not lines:
        return []
    edges = [lines[0], lines[-1]] + ([lines[1], lines[-2]] if len(lines) > 2 else [])
    out = []
    for c in edges:
        m = BARE.match(c)
        if m and 1 <= int(m.group(1)) <= 3000:
            out.append(int(m.group(1)))
    for c in (lines[0], lines[-1]):
        if len(c) <= 80:
            for m in EDGE.finditer(c):
                v = int(m.group(1) or m.group(2))
                if 1 <= v <= 3000:
                    out.append(v)
    seen, uniq = set(), []
    for v in out:
        if v not in seen:
            seen.add(v); uniq.append(v)
    return uniq[:4]


def measure_offset(pages):
    """scan page - printed page, read off the scan's own running heads.

    A number recurring on many pages is furniture, not a folio; a folio is
    kept only if a page within six agrees with it arithmetically; and the
    survivors must rise together, since pagination does and footnote numbering
    does not. A handful of agreeing pages is enough, and unanimity is the
    signal to trust.
    """
    cands = {i: folio_candidates(t) for i, t in enumerate(pages, 1)}
    counts = Counter(v for vs in cands.values() for v in vs)
    bad = {v for v, k in counts.items() if k > 4}
    cands = {p: [v for v in vs if v not in bad] for p, vs in cands.items()}
    keep = {}
    for p, vs in cands.items():
        for f in vs:
            if any(f + (q - p) in cands.get(q, ()) for q in
                   range(p - 6, p + 7) if q != p):
                keep[p] = f
                break
    if not keep:
        return None, 0, {}
    import bisect
    items = sorted(keep.items())
    tails, ti, prev = [], [], [None] * len(items)
    for i, (_, f) in enumerate(items):
        j = bisect.bisect_left(tails, f)
        if j:
            prev[i] = ti[j - 1]
        if j == len(tails):
            tails.append(f); ti.append(i)
        else:
            tails[j], ti[j] = f, i
    chain, k = [], ti[-1]
    while k is not None:
        chain.append(k); k = prev[k]
    keep = dict(items[i] for i in chain)
    offs = Counter(p - f for p, f in keep.items())
    off, n = offs.most_common(1)[0]
    return off, n, keep


# -------------------------------------------------------------- the alignment

def anchors(txt, width=55):
    lines = [l for l in txt.splitlines() if l.strip()]
    out, seen = [], set()
    # Skip up to five opening lines: a page may carry a folio, a running head,
    # a stray scan artefact and a rule before its text begins, none of which
    # are in the transcription.
    for skip in range(6):
        s = norm(" ".join(lines[skip:]))
        for start in (0, 150, 400, 800):
            if len(s) >= start + width:
                a = s[start:start + width]
                if a not in seen:
                    seen.add(a); out.append((a, start))
    return out


def align(body, pages, offset, first, last, width=55):
    stream, pmap = letters_map(body)
    found, cursor, missed = {}, 0, []
    for p in range(first, last + 1):
        idx = p + offset - 1
        if not (0 <= idx < len(pages)):
            missed.append(p); continue
        hit = -1
        for a, st in anchors(pages[idx], width):
            k = stream.find(a, cursor)
            if k == -1:
                k = stream.find(a)
            if k != -1:
                hit = max(0, k - st); break
        if hit == -1:
            missed.append(p); continue
        found[p] = pmap[min(hit, len(pmap) - 1)]
        cursor = max(cursor, hit)
    return found, missed


# ------------------------------------------------------------------- commands

def load(slug, scan_arg):
    d = book_dir(slug)
    tex = os.path.join(d, "transcription.tex")
    if not os.path.exists(tex):
        sys.exit(f"No transcription.tex in {slug}")
    src = open(tex, encoding="utf-8", errors="replace").read()
    head, body = split_document(src)
    # Drop any previous run's markers before aligning, so a rerun replaces its
    # own work rather than compounding it, and so offsets stay valid.
    body = AUTO_INLINE.sub("", body)
    scan = find_scan(d, scan_arg)
    if not scan:
        sys.exit(f"No scan found for {slug}. Put it at {d}/scan.pdf, name it in "
                 f"RESUME-NOTES.md, or pass --scan PATH.")
    return d, tex, src, head, body, scan


def do_probe(args, apply_=False):
    d, tex, src, head, body, scan = load(args.slug, args.scan)
    print(f"{args.slug}\n  scan: {scan}")
    pages = pdf_pages(scan)
    if not pages:
        sys.exit("  the scan has no text layer; OCR it first (ocrmypdf) and retry.")
    off, agree, folios = measure_offset(pages)
    if args.offset is not None:
        off, agree = args.offset, -1
        print(f"  offset: {off} (given)")
    elif off is None:
        sys.exit("  could not read any printed folio off the scan. Establish the "
                 "offset by eye and pass --offset N.")
    else:
        spread = Counter(p - f for p, f in folios.items())
        print(f"  offset: {off}  (measured from {agree} folios"
              f"{', unanimous' if len(spread) == 1 else f', {len(spread)} values seen — CHECK'})")
    first = args.first or 1
    last = args.last or (len(pages) - off)
    width = getattr(args, "width", None) or 55
    found, missed = align(body, pages, off, first, last, width)
    # The scan usually has back matter, so the tail of the range is not part of
    # the book; trim a trailing run of misses rather than reporting it as loss.
    while missed and found and missed[-1] > max(found):
        last = missed.pop() - 1
    total = last - first + 1
    print(f"  pages {first}-{last}: matched {len(found)}/{total}"
          f"  ({100*len(found)//max(total,1)}%), {len(missed)} missed")
    ks = sorted(found)
    if not ks:
        sys.exit("  nothing aligned — wrong scan, or wrong offset.")
    mono = all(found[a] <= found[b] for a, b in zip(ks, ks[1:]))
    if not mono:
        found, dropped = longest_rising(found)
        share = len(dropped) / max(1, len(dropped) + len(found))
        print(f"  {len(dropped)} anchor(s) landed out of order and were "
              f"dropped: {dropped[:10]}{' …' if len(dropped) > 10 else ''}")
        if share > 0.10:
            print(f"  REFUSING: {share:.0%} of the anchors contradict each "
                  f"other, so this is not a stray match or two — the "
                  f"alignment itself is wrong.")
            return
        ks = sorted(found)
    gaps = sorted(found[b] - found[a] for a, b in zip(ks, ks[1:]))
    print(f"  usable pages: {len(found)}   chars/page: median "
          f"{gaps[len(gaps)//2] if gaps else 0}")
    if missed[:12]:
        print(f"  missed pages: {missed[:12]}{' …' if len(missed) > 12 else ''}")
    hand = {p for _, p in page_marks(body)} - set(AUTO_INLINE.findall(body))
    hand = {int(p) for p in hand}
    if hand:
        print(f"  NOTE: {len(hand)} pages are already marked by hand.")
        if getattr(args, "fill", False):
            print(f"  --fill: leaving those alone, placing only the "
                  f"{len(set(found) - hand)} the transcriber never marked.")
        else:
            print("  apply adds [auto] markers around them, so the page is "
                  "marked twice. Pass --fill to place only the gaps.")
    if not apply_:
        print("  (probe only — nothing written. Run apply to write.)")
        return
    write(tex, src, head, body, found,
          keep=hand if getattr(args, "fill", False) else ())


def longest_rising(found):
    """The largest subset of pages whose positions rise, and the rest.

    A handful of anchors in a long book can land in the wrong place -- a stock
    phrase, a running head repeated in the text, a passage the author quotes
    from himself. Refusing the whole book for two bad anchors out of 173 throws
    away a good alignment, but keeping them puts a page marker earlier in the
    text than the page before it, which is worse than no marker at all. So keep
    the longest rising run and drop what contradicts it -- the same longest-
    increasing-subsequence argument measure_offset uses on folios, and for the
    same reason: pagination rises, and whatever does not rise is not pagination.
    """
    import bisect
    ks = sorted(found)
    tails, ti, prev = [], [], [None] * len(ks)
    for i, k in enumerate(ks):
        j = bisect.bisect_right(tails, found[k])
        if j:
            prev[i] = ti[j - 1]
        if j == len(tails):
            tails.append(found[k]); ti.append(i)
        else:
            tails[j], ti[j] = found[k], i
    chain, i = [], (ti[-1] if ti else None)
    while i is not None:
        chain.append(ks[i]); i = prev[i]
    keep = set(chain)
    return {k: v for k, v in found.items() if k in keep}, sorted(set(ks) - keep)


def safe_spots(body):
    """Positions where a marker may be dropped: ordinary running text.

    Not inside braces, so it cannot land in \emph{...} or a footnote and change
    what is emphasised; not inside math; not after a % , where it would vanish
    with the rest of the commented line.

    Word boundaries are preferred but not required. A page break often falls
    inside a word — Den menneskelige Tanke turns from p.29 to p.30 in the
    middle of "indenfor", the original hyphenating it as "inden-/for" — and
    refusing to mark there loses the page altogether. \opage is a marginal
    note and sets no text, so "inden\opage{30}for" still reads "indenfor".
    """
    safe = bytearray(len(body))
    depth, math, comment, i = 0, False, False, 0
    while i < len(body):
        c = body[i]
        if comment:
            if c == "\n":
                comment = False
            i += 1; continue
        if c == "\\":
            # Skip the whole command name. Skipping a fixed two characters left
            # the rest of it looking like ordinary text, and a marker dropped
            # into \addcontentsline split it into \addcontentslin + e{...},
            # which LaTeX only survives because nonstopmode carries on past an
            # undefined control sequence — silently losing the entry.
            j = i + 1
            while j < len(body) and body[j].isalpha():
                j += 1
            i = j if j > i + 1 else i + 2
            continue
        if c == "%":
            comment = True; i += 1; continue
        if c == "$":
            math = not math; i += 1; continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth = max(0, depth - 1)
        elif depth == 0 and not math:
            safe[i] = 2 if c.isspace() else 1
        i += 1
    return safe


def nearest_safe(safe, off, reach=400, snap=12):
    """The closest safe spot to off.

    A word boundary within `snap` characters is preferred, since that is where
    a marker reads best; beyond that the exact position wins, because the page
    really does turn there.
    """
    for d in range(snap):
        if off - d >= 0 and safe[off - d] == 2:
            return off - d
        if off + d < len(safe) and safe[off + d] == 2:
            return off + d
    for d in range(reach):
        if off - d >= 0 and safe[off - d]:
            return off - d
        if off + d < len(safe) and safe[off + d]:
            return off + d
    return None


BLANK_RUN = re.compile(r"\n[ \t]*\n")


def snap_out_of_break(body, spot):
    """Move a spot that falls inside a blank-line run to the new paragraph.

    A marker is inserted AT `spot`, so a spot landing on the second newline of a
    "\n\n" pair writes the marker between the two newlines and the blank line is
    gone -- two paragraphs silently become one. Nothing downstream can see it:
    braces balance, check.py is happy, the page markers verify, and the document
    compiles. It destroyed 64 paragraph breaks across 13 books in September 2026
    before anyone noticed, and 39 more in Den menneskelige Tanke.

    Where a page really does turn at a paragraph boundary, the marker belongs at
    the head of the NEW paragraph, so the break is preserved and the marginal
    number sits beside the first line of the page. Returns (spot, at_paragraph).
    """
    a = b = spot
    while a > 0 and body[a-1] in " \t\n":
        a -= 1
    while b < len(body) and body[b] in " \t\n":
        b += 1
    if BLANK_RUN.search(body[a:b]):
        return b, True
    return spot, False


def ensure_preamble(head):
    """The macros this writes must exist, or the document will not build."""
    add = ""
    if "\\newcommand{\\apage}" not in head:
        if "\\newcommand{\\opage}" in head:
            add = ("\\newcommand{\\apage}[1]"
                   "{\\marginnote{\\footnotesize\\textit{[#1]}}}\n")
        else:
            add = PREAMBLE
    if not add:
        return head, False
    if "\\usepackage{marginnote}" in head:
        add = add.replace("\\usepackage{marginnote}\n", "")
    tag = "\n% ---- original-page markers (paginate.py) ----\n"
    return head.rstrip() + "\n" + tag + add, True


def write(tex, src, head, body, found, keep=()):
    """Place an \\apage for each aligned page, skipping any page in `keep`.

    `keep` is the merge case: a book whose transcriber marked some of the page
    turns by hand and not the rest. Nielsen's Grundideernes Logik is the one
    here -- 425 of its 456 pages carry a `% p. N` comment placed at the turn by
    someone reading the page, and the rest were never written down. Those 425
    are better evidence than the alignment, in position as well as number, so
    convert makes them \\opage and this fills only the gaps.
    """
    safe = safe_spots(body)
    placed, skipped, last = [], 0, -1
    for page, off in sorted(found.items()):
        if page in keep:
            continue
        spot = nearest_safe(safe, min(off, len(body) - 1))
        if spot is None or spot <= last:
            skipped += 1
            continue
        spot, at_para = snap_out_of_break(body, spot)
        if spot <= last:
            skipped += 1
            continue
        placed.append((spot, page, at_para))
        last = spot
    out, cut = [], 0
    for spot, page, at_para in placed:
        out.append(body[cut:spot])
        out.append((MARK % page + " ") if at_para else (" " + MARK % page))
        cut = spot
    out.append(body[cut:])
    newbody = "".join(out)

    head, added = ensure_preamble(head)
    # Named to match the repo's own ignore rule, texts/**/*.bak.*
    bak = f"{tex}.bak.{time.strftime('%Y%m%d-%H%M%S')}"
    open(bak, "w", encoding="utf-8").write(src)
    whole = (head + r"\begin{document}" + newbody) if head else newbody
    open(tex, "w", encoding="utf-8").write(whole)
    print(f"  wrote {len(placed)} \\apage markers"
          + (f", skipped {skipped} with no safe spot" if skipped else ""))
    if added:
        print("  added the \\opage/\\apage definitions to the preamble")
    print(f"  backup: {os.path.basename(bak)}")
    print("  next: verify, rebuild the index, check the PDF builds, then commit.")


def do_convert(args):
    """Make an existing comment-form pagination visible, without recomputing it.

    Nine books carry good page numbers as comments: Nielsen's Religionsphilosophie
    has 537 of them, with a verified offset and a misbound leaf in the KB scan
    documented by hand. Those numbers are better evidence than any alignment,
    so this does not touch them — it leaves every comment where it is, for the
    PDF-page numbers and the notes they carry, and adds an \opage marker at the
    head of the paragraph each one introduces.

    \opage, not \apage: these were established at the image by a person.
    """
    d = book_dir(args.slug)
    tex = os.path.join(d, "transcription.tex")
    src = open(tex, encoding="utf-8", errors="replace").read()
    head, body = split_document(src)
    if not head:
        sys.exit("  no \\begin{document}; convert expects a full document.")
    have = {p for _, p in page_marks(body)}
    inline = {int(m.group(1)) for m in MARK_INLINE.finditer(body)}
    todo = [(m.end(), mark_page(m)) for m in MARK_COMMENT.finditer(body)
            if mark_page(m) not in inline]
    if not todo:
        print(f"{args.slug}: nothing to convert "
              f"({len(inline)} markers already visible).")
        return
    print(f"{args.slug}: {len(todo)} comment marks to make visible, "
          f"{len(inline)} already visible")
    out, cut, placed = [], 0, 0
    for end, page in todo:
        # The comment runs to end of line; the marker goes at the start of the
        # text that follows it, so the margin note sits beside its own page.
        nl = body.find("\n", end)
        if nl == -1 or nl < cut:
            continue
        j = nl
        while j < len(body) and body[j] in "\n \t":
            j += 1
        if j <= cut:
            continue
        out.append(body[cut:j])
        out.append(MARK_OPAGE % page)
        out.append(" ")
        cut, placed = j, placed + 1
    out.append(body[cut:])
    newbody = "".join(out)
    head, added = ensure_preamble(head)
    # Named to match the repo's own ignore rule, texts/**/*.bak.*
    bak = f"{tex}.bak.{time.strftime('%Y%m%d-%H%M%S')}"
    open(bak, "w", encoding="utf-8").write(src)
    open(tex, "w", encoding="utf-8").write(head + r"\begin{document}" + newbody)
    print(f"  placed {placed} \opage markers; every comment left in place")
    if added:
        print(r"  added the \opage/\apage definitions to the preamble")
    print(f"  backup: {os.path.basename(bak)}")
    print("  next: verify, build the PDF, rebuild the index, then commit.")


def do_audit(args):
    """Collate a paginated transcription against its scan, page by page.

    Once a book is marked, every page is a bounded stretch of text with a known
    counterpart in the scan, and the two can be compared. The scan's OCR is
    chopped into 40-letter windows and each is looked for in the transcription
    between that page's markers. This is not a spell-check: it finds places
    where the transcription and the original actually diverge.

    Expect a few misses on every page. A footnote is printed at the foot of the
    page but sits inline in the LaTeX, so the letter-streams differ around it,
    and the OCR itself is imperfect. Pages in the nineties are normal. It is
    the outliers that repay reading, and they do repay it: this found "deri
    finder man" for the printed "deri finder han", and a line of Den
    menneskelige Tanke p.133 where the transcriber's eye had skipped from
    "historiske Emner" to the "Totaliteter" of the following line.
    """
    d = book_dir(args.slug)
    tex = os.path.join(d, "transcription.tex")
    body = open(tex, encoding="utf-8", errors="replace").read()
    body = split_document(body)[1]
    scan = find_scan(d, args.scan)
    if not scan:
        sys.exit(f"  no scan for {args.slug}; audit needs one.")
    pages = pdf_pages(scan)
    if not pages:
        sys.exit("  the scan has no text layer.")
    marks = [(m.start(), int(m.group(1)), m.end()) for m in MARK_INLINE.finditer(body)]
    if len(marks) < 2:
        sys.exit("  this book is not marked yet; run probe/apply or convert first.")
    off = args.offset
    if off is None:
        off, n, _ = measure_offset(pages)
        if off is None:
            sys.exit("  could not measure the offset; pass --offset N.")
    scored = []
    for (st, pg, en), (nx, _, _) in zip(marks, marks[1:]):
        idx = pg + off - 1
        if not (0 <= idx < len(pages)):
            continue
        got = norm(body[en:nx])
        want = norm(pages[idx])
        if len(want) < 120:
            continue
        # Trigrams, not long windows. A scan's text layer may misread a common
        # letter everywhere — the Nielsen scans render "være" as "vcrre" and
        # "Følelse" as "Folelse" — and a 40-character window dies on a single
        # bad character, so whole good pages scored 20%. A trigram loses only
        # its own neighbourhood, so the score tracks real divergence rather
        # than the scan's spelling of æ and ø.
        A = {want[i:i+3] for i in range(len(want) - 2)}
        B = {got[i:i+3] for i in range(len(got) - 2)}
        hits = len(A & B)
        scored.append((hits / len(A), pg, hits, len(A)))
    if not scored:
        sys.exit("  nothing comparable.")
    scored.sort()
    med = scored[len(scored) // 2][0]
    print(f"{args.slug}: {len(scored)} pages collated against the scan "
          f"(offset {off})")
    print(f"  median coverage {100*med:.0f}%  —  a page well below that is "
          f"worth reading against the image\n")
    print(f"  {'page':>6}{'coverage':>10}   trigrams")
    for frac, pg, hits, tot in scored[:args.worst]:
        flag = "   <= look at this one" if frac < med - 0.12 else ""
        print(f"  {pg:>6}{100*frac:>9.0f}%   {hits}/{tot}{flag}")
    low = [p for f, p, *_ in scored if f < med - 0.12]
    if low:
        print(f"\n  {len(low)} page(s) more than 12 points below the median: "
              f"{low[:14]}")
        print("  pdftoppm -f <scan page> -l <scan page> -r 150 -png scan.pdf /tmp/pg")


def do_locate(args):
    """Which printed pages of a collected volume this transcription occupies.

    Several texts here are a single essay inside a big PDF -- Hoeffding's
    "Forholdet mellem Tro og Viden" is twenty-odd pages of a 263-page Mindre
    Arbejder, and Moeller's "En dansk Students Eventyr" sits deep in volume I
    of the Efterladte Skrifter. probe defaults to pages 1..len(scan)-offset,
    which for those is mostly other people's text, so it reports a few per cent
    matched and looks like a failed alignment when nothing is wrong.

    This measures the range instead of guessing it: it looks for the opening
    and closing of the transcription in the scan's own pages, and converts the
    scan pages it finds them on into printed pages with the measured offset.
    Pass the result to probe as --first/--last.
    """
    d, tex, src, head, body, scan = load(args.slug, getattr(args, "scan", None))
    pages = pdf_pages(scan)
    if not pages:
        sys.exit("  the scan has no text layer; OCR it first (ocrmypdf).")
    off, agree, _ = measure_offset(pages)
    if args.offset is not None:
        off, agree = args.offset, -1
    if off is None:
        sys.exit("  could not measure the offset; pass --offset N.")
    stream, _ = letters_map(body)
    if len(stream) < 400:
        sys.exit("  transcription too short to locate.")
    norms = [norm(t) for t in pages]

    def page_of(probe):
        hits = [i for i, t in enumerate(norms, 1) if probe in t]
        return hits

    # Probe right across the text, not just at its two ends. The ends are the
    # worst place to look: letters_map keeps environment names, so the first
    # few hundred characters of a stream are \begin{center}, \maketitle and
    # title-page apparatus that is not in the scan at all, and the last few
    # hundred are the closing environments. Sampling throughout also survives a
    # page the OCR mangled -- one bad probe costs nothing when there are eighty.
    hits = []
    step = max(60, (len(stream) - 60) // 80)
    for k in range(0, len(stream) - 60, step):
        for pg in page_of(stream[k:k + 60]):
            hits.append((k, pg))
    if not hits:
        sys.exit("  could not find this text in that scan -- likely the wrong "
                 "scan. Check it with find_source.py.")
    lo, hi = min(p for _, p in hits), max(p for _, p in hits)
    print(f"  {len({k for k, _ in hits})} of {len(range(0, len(stream) - 60, step))}"
          f" probes placed")
    # A negative or zero printed page is arithmetically impossible, so it is
    # proof the offset is wrong rather than a range worth reporting. This is
    # the cheapest check there is on a weakly-measured offset: two folios
    # agreeing by chance survive measure_offset but not this.
    if lo - off < 1:
        print(f"{args.slug}")
        print(f"  scan: {scan}")
        print(f"  found on scan pages {lo}-{hi} of {len(pages)}, but offset "
              f"{off} puts that at printed page {lo - off}.")
        sys.exit("  REFUSING: the offset is wrong. Read a folio off the scan "
                 "by eye and pass --offset N.")
    print(f"{args.slug}")
    print(f"  scan: {scan}")
    print(f"  offset: {off}" + (f"  (measured from {agree} folios)"
                                if agree >= 0 else "  (given)"))
    print(f"  found on scan pages {lo}-{hi} of {len(pages)}")
    print(f"  printed pages {lo - off}-{hi - off}")
    print(f"  next: ./paginate.py probe {args.slug} "
          f"--first {lo - off} --last {hi - off}")


def do_verify(args):
    d = book_dir(args.slug)
    tex = os.path.join(d, "transcription.tex")
    whole = open(tex, encoding="utf-8", errors="replace").read()
    # Only the body. The comment header discusses page numbers in prose
    # ("printed p.1 = PDF 14"), and reading those as markers puts a spurious
    # page at the top of the sequence and fails an otherwise sound file.
    body = split_document(whole)[1]
    marks = page_marks(body)
    if not marks:
        sys.exit("  no page markers in this file.")
    # A converted book carries each page twice — once as the comment that
    # records it and once as the marker that shows it — so collapse a run of
    # the same page before judging the sequence.
    pages = [p for i, (_, p) in enumerate(marks)
             if i == 0 or p != marks[i - 1][1]]
    visible = len(MARK_INLINE.findall(body))
    comment = len(MARK_COMMENT.findall(body))
    mono = all(a < b for a, b in zip(pages, pages[1:]))
    gaps = [b - a for a, b in zip(pages, pages[1:]) if b - a != 1]
    print(f"{args.slug}: {len(pages)} distinct page marks, "
          f"pp. {pages[0]}-{pages[-1]}  ({visible} visible, {comment} as comments)")
    print(f"  strictly increasing: {mono}")
    print(f"  non-consecutive steps: {len(gaps)}"
          + (f"  {sorted(set(gaps))[:8]}" if gaps else ""))
    body_chars = len(body)
    seen, uniq = set(), []
    for pos, pg in marks:
        if pg not in seen:
            seen.add(pg); uniq.append(pos)
    spacing = [b - a for a, b in zip(uniq, uniq[1:])]
    if spacing:
        spacing.sort()
        print(f"  chars between markers: min {spacing[0]}, median "
              f"{spacing[len(spacing)//2]}, max {spacing[-1]}")
        if spacing[-1] > 6 * max(spacing[len(spacing)//2], 1):
            print("  one gap is far larger than the rest — check that stretch by eye.")
    if not mono:
        print("  FAIL: page numbers are not increasing. Restore the .bak.")


def do_status(args):
    """The work queue, read from the transcriptions themselves.

    Deliberately independent of the search index: this has to work in a fresh
    checkout, before anything is built.
    """
    rows = []
    for tex in sorted(glob.glob(os.path.join(TEXTS, "*", "*", "transcription.tex"))):
        d = os.path.dirname(tex)
        slug = f"{os.path.basename(os.path.dirname(d))}/{os.path.basename(d)}"
        body = open(tex, encoding="utf-8", errors="replace").read()
        body = split_document(body)[1]
        paras = sum(1 for b in re.split(r"\n\s*\n", body)
                    if len(b.strip()) > 80)
        pages = len({p for _, p in page_marks(body)})
        ratio = paras / pages if pages else None
        state = "ok" if pages and ratio <= 8 else ("thin" if pages else "none")
        if state == "ok" and not args.all:
            continue
        rows.append((state, paras, pages, slug, "scan" if find_scan(d) else "no scan"))
    rows.sort(key=lambda r: -r[1])
    print(f"{'state':<6}{'paras':>6}{'pages':>7}  {'book':<44}source")
    for st, n, dp, slug, src in rows:
        print(f"{st:<6}{n:>6}{dp:>7}  {slug:<44}{src}")
    done = sum(1 for r in rows if r[0] == "ok")
    print(f"\n{len(rows) - done} books need work, biggest first — they carry the "
          f"most uncitable text.\n"
          f"{sum(1 for r in rows if r[4] == 'scan')} of them have a scan findable now.")


def main():
    p = argparse.ArgumentParser(description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    st = sub.add_parser("status", help="the work queue")
    st.add_argument("--all", action="store_true", help="include finished books")
    st.set_defaults(func=do_status)
    for name, fn, helptext in (("probe", lambda a: do_probe(a, False),
                                "measure and report; writes nothing"),
                               ("apply", lambda a: do_probe(a, True),
                                "insert the markers")):
        q = sub.add_parser(name, help=helptext)
        q.add_argument("slug", help="e.g. hoeffding/menneskelige-tanke")
        q.add_argument("--scan", help="path to the scan, if not found automatically")
        q.add_argument("--offset", type=int, help="scan page minus printed page")
        q.add_argument("--first", type=int); q.add_argument("--last", type=int)
        q.add_argument("--width", type=int, metavar="N",
                       help="anchor length in letters (default 55). Shorten to "
                            "~30 for a Fraktur scan whose OCR is too garbled "
                            "for a long anchor to survive")
        q.add_argument("--fill", action="store_true",
                       help="place markers only where the transcriber left "
                            "none, keeping hand-made ones")
        q.set_defaults(func=fn)
    cv = sub.add_parser("convert",
                        help="make existing comment-form page marks visible")
    cv.add_argument("slug")
    cv.set_defaults(func=do_convert)

    au = sub.add_parser("audit",
                        help="collate a marked transcription against its scan")
    au.add_argument("slug")
    au.add_argument("--scan"); au.add_argument("--offset", type=int)
    au.add_argument("--worst", type=int, default=12)
    au.set_defaults(func=do_audit)

    lo = sub.add_parser("locate",
                        help="which printed pages an excerpt occupies in its volume")
    lo.add_argument("slug"); lo.add_argument("--scan")
    lo.add_argument("--offset", type=int)
    lo.set_defaults(func=do_locate)
    v = sub.add_parser("verify", help="check the markers in a file")
    v.add_argument("slug")
    v.set_defaults(func=do_verify)
    a = p.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
