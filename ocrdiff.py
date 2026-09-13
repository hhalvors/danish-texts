#!/usr/bin/env python3
"""ocrdiff.py -- catch transcription errors by diffing our words against the scan's.

WHY THIS EXISTS

For a book whose scan has a usable text layer, the method deliberately does not
eyeball the words page by page: the OCR carries the words, the image carries
structure and emphasis. That is the right division of labour and it is what
makes antiqua books cheap. But it leaves the words themselves unchecked by
anything, because an agent handed a page of OCR does not copy it -- it reads it
and writes it out again, and the difference is invisible to every structural
check we run.

Collating Den menneskelige Tanke in 2026 measured the cost: ~0.9 errors per
page, and of the errors found WITHOUT using the OCR, two-thirds were readings
the scan's own text layer had already got right. The words were not lost by the
OCR. They were lost between the OCR and the file. Nothing in the batch loop
compared the two, so nothing could see it.

This compares them. It is text-only, needs no images, and costs nothing.

TWO MODES

  Per batch, before splicing -- this is the one that matters:
      python3 ocrdiff.py --frag .parts/pp45-57.texfrag --scan scan.pdf --offset 2

  Over a whole marked book, to audit work already done:
      python3 ocrdiff.py hoeffding/menneskelige-tanke
      python3 ocrdiff.py hoeffding/menneskelige-tanke --first 340 --last 392

KNOW THIS BEFORE YOU TRUST A RESULT: IT DEPENDS ENTIRELY ON THE SCAN

This tool compares two *sequences* of words, so it is only as good as the
reading order of the scan's text layer. On a clean layer -- ABBYY over the 1910
antiqua of Den menneskelige Tanke -- roughly 85% of its candidates were real
transcription errors, and it found some 200 of them. On the older Google and
HathiTrust scans of the 19th-century books it is near useless: a sample of 27
candidates drawn from three of them (Brøchner's Philosophiens Udvikling and
Spinoza, Nielsen's Natur og Aand) was read at the page and **not one was a real
error**. All 27 were the text layer emitting words out of their printed order
around hyphenated line breaks, running heads, footnote markers and formulas.

`pdftotext -layout` cuts that noise by about two thirds and is worth trying, but
it does not rescue the method.

`--ocr PATH` takes an EXTERNAL witness -- a tesseract reading you build yourself
-- for the four books whose scan carries no usable layer. Measured against the
embedded layer on a planted-fault test (pp. 100-104 of *Den menneskelige Tanke*,
one dropped `ikke` and one stripped adverbial `-t`): both modes catch both
faults, but the external mode returns 13 candidates where the embedded returns
3. The reason is structural and worth knowing. The frequency floors below screen
OCR garbage by asking whether a word occurs elsewhere in the book, and an
external witness is only the batch's own pages, so there is no frequency signal
to screen with; the floors drop to 1 and everything is shown. That is the right
failure direction -- a noisy check a reader must adjudicate beats a quiet one --
but it means an external-witness batch costs perhaps three times the
adjudication of an embedded one. Budget for it; do not economise by skipping it.

So: before believing a ranking or a count from this tool on a book you have not
used it on before, **draw a handful of its candidates and read them at the
page.** If the first half-dozen are all OCR, the rest will be too, and the
number it reports measures the scan rather than the transcription. A random
ten-page collation against the images is the instrument that always works; this
one is a cheap pre-filter for the books whose scans happen to support it.

WHAT IT REPORTS, AND WHAT IT DOES NOT

Only divergences with three exactly matching words on BOTH sides, so a garbled
neighbourhood cannot manufacture one; a "missing" word must be one the book uses
elsewhere, so OCR debris is out; both readings of a substitution must be real
words of the book. Words the OCR split across a line break are rejoined first.

Whole-book mode additionally drops any substitution pattern seen more than twice
-- that is the scan's own habit (del/det, liden/tiden, slaa/staa), not an error.
BEWARE: a real error that recurs is suppressed by that filter, which is exactly
what the adverbial -t class does. Run whole-book mode over ~50-page ranges as
well as whole. Batch mode does no frequency filtering at all; with twelve pages
there is nothing to average over, and a handful of false positives per batch is
the cheapest review there is.

The output is a candidate list, not a verdict. Read each at the image before
changing anything. On the one book this has been run against, roughly 85% were
real and the rest were OCR after all.
"""
import argparse, collections, difflib, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import paginate as pg

PAGE_MARK = re.compile(r"\\[oa]page\{(\d+)\}|^%\s*-*\s*p\.?\s*(\d+)\s*-*\s*$", re.M)


def words(s, latex=False):
    if latex:
        s = re.sub(r"%.*", "", s)                      # drop comments
        s = re.sub(r"\\footnote\s*", "", s)
        s = re.sub(r"\\[a-zA-Z]+\*?\s*", " ", s)
        s = s.replace("{", " ").replace("}", " ")
    s = s.replace("\u00ad", "")
    s = re.sub(r"-\s*\n\s*", "", s)                    # rejoin OCR line-break splits
    s = re.sub(r"[^0-9A-Za-zÀ-ɏÆØÅæøå]+", " ", s)
    return [w.lower() for w in s.split() if w]


# Letter pairs these scans actually confuse, from the repo's own OCR: r/b in
# "bum" for "rum", l/i in "bievne" for "blevne", f/e in "eorstaaelse". A pair
# differing by exactly one such substitution is almost always the scan's fault.
CONFUSIONS = [set(p) for p in ("rb", "li", "l1", "i1", "fe", "ec", "eo", "nu",
                               "vy", "cg", "hb", "sg", "tf", "ao")]


def looks_like_ocr(s, t):
    if len(s) != len(t) or " " in s or " " in t:
        return False
    diff = [(a, b) for a, b in zip(s, t) if a != b]
    return len(diff) == 1 and set(diff[0]) in CONFUSIONS


def label(kind, s, t):
    """Name the class where we recognise it. These are the ones that have
    actually happened, and naming them is most of the reader's work.

    Nothing is filtered on this basis -- a label is a hint, and a wrong hint
    that suppressed a real reading would defeat the whole point of the check."""
    if kind == "DITTO":
        return "scan repeats itself — probably OCR, not a loss"
    if kind == "MISSING":
        return "dropped word" if len(s.split()) == 1 else "dropped words"
    if s == t + "t":
        return "adverbial -t dropped"          # egentligt, stadigt, navnligt...
    if looks_like_ocr(s, t):
        return "likely OCR"
    if len(s) > 3 and len(t) > 3 and s[:3] == t[:3]:
        return "form modernised?"              # Regelen/Reglen, stansede/standsede
    return ""


def collect(spans, pages, off, vocab, pad=1, floor=None):
    """Compare each page's transcription span with the scan.

    The scan side is a WINDOW of pages (N-pad .. N+pad), not page N alone. A
    page marker often sits a few words off the true turn -- it snaps to a word
    boundary, and an aligner-placed one can match past a footnote; eleven of Den
    menneskelige Tanke's 392 markers were late by a sentence or more. A span
    compared against its single page is then misaligned at both ends and the
    anchors fail there. Widening the scan side costs almost nothing: the surplus
    at each end aligns out as one long unmatched block, which the anchor guard
    and the four-word ceiling both reject anyway. Measured on that book it
    changed the whole-book candidate count by one.
    """
    # The frequency floors below screen OCR garbage by asking "does this word
    # occur elsewhere in the book?". That question needs a book-sized
    # vocabulary. With an EXTERNAL witness the vocabulary is only the batch's
    # own pages, the counts never reach 3 or 4, and the check goes silent --
    # the same cold-start failure that once made --frag useless on batch 2.
    # With no frequency signal, show the candidate and let the reader settle it.
    d_floor, r_floor = (4, 3) if floor is None else (floor, floor)
    raw = []
    for p, text in spans:
        idx = p + off - 1
        if not (0 <= idx < len(pages)):
            continue
        lo, hi = max(0, idx - pad), min(len(pages), idx + pad + 1)
        T, S = words(text, latex=True), words(" ".join(pages[lo:hi]))
        if len(S) < 40:
            continue
        sm = difflib.SequenceMatcher(None, S, T, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                continue
            if i1 < 3 or j1 < 3 or i2 > len(S) - 3 or j2 > len(T) - 3:
                continue
            if S[i1-3:i1] != T[j1-3:j1] or S[i2:i2+3] != T[j2:j2+3]:
                continue
            s, t = " ".join(S[i1:i2]), " ".join(T[j1:j2])
            before, after = " ".join(T[max(0, j1-6):j1]), " ".join(T[j2:j2+6])
            if tag == "delete" and 0 < i2 - i1 <= 4:
                if all(vocab[w] >= d_floor for w in S[i1:i2]):
                    # A scan's text layer sometimes re-reads a phrase it has just
                    # read -- line or column dittography. It looks exactly like a
                    # dropped phrase, and on one book it accounted for most of the
                    # candidates. If the "missing" words simply repeat what stands
                    # next to them in OUR text, say so rather than crying wolf.
                    n = i2 - i1
                    run = S[i1:i2]
                    near = T[max(0, j1-10):j1] + T[j2:j2+10]
                    dit = any(near[x:x+n] == run for x in range(len(near) - n + 1))
                    raw.append((p, "DITTO" if dit else "MISSING", s, t,
                                f"{before} \u27ea scan has: {s} \u27eb {after}"))
            elif tag == "replace" and i2 - i1 <= 2 and j2 - j1 <= 2:
                if s.replace(" ", "") == t.replace(" ", ""):
                    continue
                if not all(vocab[w] >= r_floor for w in S[i1:i2]):
                    continue
                if not all(vocab[w] >= 1 for w in T[j1:j2]):
                    continue
                if difflib.SequenceMatcher(None, s, t).ratio() < 0.5:
                    continue
                raw.append((p, "DIFFERS", s, t,
                            f"{before} \u27ea tex: {t}  |  scan: {s} \u27eb {after}"))
    return raw


def report(out, header, footer):
    print(header + "\n")
    for p, kind, s, t, ctx in out:
        tag = label(kind, s, t)
        tag = f"  [{tag}]" if tag else ""
        print(f"p.{p:>4} {kind:<8} {ctx}{tag}")
    print("\n" + footer)


def spans_from_marks(text, marks):
    """[(page, text-belonging-to-that-page)] from marker positions."""
    out = []
    for (st, p, en), (nx, _, _) in zip(marks, marks[1:]):
        out.append((p, text[en:nx]))
    return out


def do_frag(a):
    frag = open(a.frag, encoding="utf-8", errors="replace").read()
    d = os.path.dirname(os.path.abspath(a.frag))
    if os.path.basename(d) == ".parts":
        d = os.path.dirname(d)
    marks = [(m.start(), int(m.group(1) or m.group(2)), m.end())
             for m in PAGE_MARK.finditer(frag)]
    if len(marks) < 2:
        sys.exit("  fewer than two page markers in the fragment; nothing to bound.")

    if a.ocr:
        # An EXTERNAL witness, for a book whose scan carries no usable embedded
        # layer. The point of the second reading is not that it is accurate --
        # tesseract over Fraktur is not -- but that it is INDEPENDENT of the
        # agent that wrote the fragment. A word present in both was copied; a
        # word in neither is the witness's problem; a word in one only is
        # exactly what this tool exists to surface.
        raw_ocr = open(a.ocr, encoding="utf-8", errors="replace").read()
        # Join words the compositor broke across a line. Without this the
        # three-word anchors on either side of a divergence fail wherever a
        # hyphenated word falls in the context, and the check goes quiet in
        # exactly the places it is needed. Measured on a planted-fault test,
        # this is the difference between catching two of three planted faults
        # and catching one.
        raw_ocr = re.sub(r"(\w)[-\u00ad]\s*\n\s*(\w)", r"\1\2", raw_ocr)
        chunks = raw_ocr.split("\f")
        chunks = [c for c in chunks if c.strip()]
        nums = [p for _, p, _ in marks]
        if len(chunks) != len(nums):
            sys.exit(f"  the witness has {len(chunks)} page(s) but the fragment marks "
                     f"{len(nums)} (pp. {nums[0]}\u2013{nums[-1]}). They must correspond "
                     "one to one, in order; re-render the witness for exactly this range.")
        pages = [""] * (max(nums) + 2)
        for n_, c in zip(nums, chunks):
            pages[n_] = c
        off = 1                      # collect() reads pages[p + off - 1]
        witness = f"external ({os.path.basename(a.ocr)})"
    else:
        scan = pg.find_scan(d, a.scan)
        if not scan:
            sys.exit("  no scan found; pass --scan PATH, or --ocr PATH for a book\n"
                     "  whose scan has no usable embedded layer. SCANS.tsv at\n"
                     "  the repo root says which case this book is.")
        pages = pg.pdf_pages(scan)
        if not pages:
            sys.exit("  the scan has no usable text layer. This check still applies:\n"
                     "  build a tesseract witness for this batch's pages and pass it with\n"
                     "  --ocr PATH. See TRANSCRIPTION-PLAYBOOK.md \u00a73 step 4.")
        off = a.offset
        if off is None:
            off, n, _ = pg.measure_offset(pages)
            if off is None:
                sys.exit("  could not measure the offset; pass --offset N "
                         "(your book's pagemap knows it).")
        witness = "embedded layer"
    # Vocabulary -- "is this a real word of this book?" -- comes from the SCAN,
    # not from the transcription so far. On batch 2 of a book transcription.tex
    # is nearly empty, the counts never reach the thresholds below, and the
    # check silently reports nothing precisely when it is most needed. The scan
    # is complete from the first batch. Its OCR garbage is mostly unique, so the
    # frequency thresholds still screen it out.
    vocab = collections.Counter(words(" ".join(pages)))
    vocab += collections.Counter(words(frag, latex=True))
    tex = os.path.join(d, "transcription.tex")
    if os.path.exists(tex):
        vocab += collections.Counter(
            words(open(tex, encoding="utf-8", errors="replace").read(), latex=True))
    spans = spans_from_marks(frag, marks)
    # the last marked page has no following marker; bound it with end-of-fragment
    spans.append((marks[-1][1], frag[marks[-1][2]:]))
    out = sorted(collect(spans, pages, off, vocab,
                         floor=1 if a.ocr else None))
    pp = f"pp. {marks[0][1]}\u2013{marks[-1][1]}"
    report(out,
           f"{os.path.basename(a.frag)}: {pp}, offset {off} \u2014 "
           f"{len(out)} divergence(s) from the {witness}",
           "  Settle every one of these at the image before the fragment is spliced.\n"
           "  Some will be OCR error; the ones that are not are transcription error,\n"
           "  and they are the class no other check in the loop can see.")
    return 1 if out else 0


def do_book(a):
    d = pg.book_dir(a.slug)
    body = open(os.path.join(d, "transcription.tex"), encoding="utf-8",
                errors="replace").read()
    body = body.partition(r"\begin{document}")[2] or body
    scan = pg.find_scan(d, a.scan)
    if not scan:
        sys.exit(f"  no scan for {a.slug}; ocrdiff needs one.")
    pages = pg.pdf_pages(scan)
    if not pages:
        sys.exit("  the scan has no text layer.")
    marks = [(m.start(), int(m.group(1)), m.end())
             for m in pg.MARK_INLINE.finditer(body)]
    if len(marks) < 2:
        sys.exit("  this book is not marked yet; run paginate.py first.")
    off = a.offset
    if off is None:
        off, n, _ = pg.measure_offset(pages)
        if off is None:
            sys.exit("  could not measure the offset; pass --offset N.")
    vocab = collections.Counter(words(body, latex=True))
    spans = [(p, t) for p, t in spans_from_marks(body, marks)
             if a.first <= p <= a.last]
    raw = collect(spans, pages, off, vocab)
    seen = collections.Counter((k, s, t) for _, k, s, t, _ in raw)
    out = sorted(r for r in raw if seen[(r[1], r[2], r[3])] <= 2)
    report(out,
           f"{a.slug}: {len(raw)} anchored divergences -> {len(out)} candidates "
           f"after removing repeated OCR patterns (offset {off})",
           "  Read these at the image before changing anything:\n"
           "  pdftoppm -f <printed + offset> -l <same> -r 300 -png scan.pdf /tmp/pg\n"
           "  Then run again over narrower --first/--last ranges: the pattern filter\n"
           "  hides real errors that recur, which is what the -t class does.")
    return 0


def main():
    ap = argparse.ArgumentParser(
        description="Diff a transcription's words against the scan's text layer.")
    ap.add_argument("slug", nargs="?", help="book slug, for whole-book mode")
    ap.add_argument("--frag", help="a .texfrag to check before splicing")
    ap.add_argument("--scan")
    ap.add_argument("--ocr", help="an external witness for a book whose scan has no\nusable embedded layer: one text file holding this batch's pages in order,\nseparated by form feeds (what `tesseract` and `pdftotext` both emit).")
    ap.add_argument("--offset", type=int)
    ap.add_argument("--first", type=int, default=0)
    ap.add_argument("--last", type=int, default=10**6)
    a = ap.parse_args()
    if a.frag:
        sys.exit(do_frag(a))
    if not a.slug:
        ap.error("give a book slug, or --frag for a single batch")
    sys.exit(do_book(a))


if __name__ == "__main__":
    main()
