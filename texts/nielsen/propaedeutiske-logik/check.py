#!/usr/bin/env python3
"""
check.py [transcription.tex]

Automated invariants, so that verifying a batch does not mean re-reading the
file. Run it after every splice: it reports on what the last batch wrote.

Page-marker convention for this book:  % --- p. N ---  on its own line, at the
point where printed page N BEGINS. Every page in a batch needs one.

Book-specific extras over the Evangelietroen version:
  * body is printed pp. 1-283
  * the text is a numbered textbook whose §§ run CONTINUOUSLY 1..21 across both
    Parts -- they do not restart in the Anden Deel. So a repeated \\parag number
    is an error, and check.py says so.
  * structure goes in through the preamble macros \\deel, \\capitel, \\parag and
    \\anm. Hand-rolled \\begin{center} display heads are reported as suspect,
    because they render inconsistently and check.py cannot count them.
"""
import re, sys, os

BODY_LAST = 283

PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "transcription.tex")
src = open(PATH, encoding="utf-8").read()

pages = [int(m) for m in re.findall(r"^%\s*---\s*p\.\s*(\d+)\s*---", src, re.M)]
body = re.sub(r"(?m)^\s*%.*$", "", src)          # ignore comments for counting

print(f"file: {os.path.basename(PATH)}  ({len(src)/1024:.0f} KB)")

if pages:
    lo, hi = min(pages), max(pages)
    missing = sorted(set(range(lo, hi + 1)) - set(pages))
    dupes = sorted({p for p in pages if pages.count(p) > 1})
    print(f"pages: {lo}..{hi}  n={len(pages)}  "
          f"gaps={missing if missing else 'none'}  "
          f"dupes={dupes if dupes else 'none'}")
    print(f"progress: {hi}/{BODY_LAST} = {hi/BODY_LAST*100:.1f}%   "
          f"next page to transcribe: {hi+1}")
else:
    print("pages: no  % --- p. N ---  markers yet")
    print(f"progress: 0/{BODY_LAST} = 0.0%   next page to transcribe: 1")

print(f"braces balanced: {body.count('{') == body.count('}')}"
      f"  ({body.count('{')} open / {body.count('}')} close)")
print(f"$ even: {body.count('$') % 2 == 0}")
print(f"markers remaining (text to be added): {src.count('text to be added')}")

print(f"structure: \\division={body.count(chr(92)+'division{')} "
      f"\\deel={body.count(chr(92)+'deel{')} "
      f"\\capitel={body.count(chr(92)+'capitel{')} "
      f"\\capitelsp={body.count(chr(92)+'capitelsp{')} "
      f"\\anm={body.count(chr(92)+'anm{')}")

secs = [int(m) for m in re.findall(r"\\parag\{(\d+)\}", body)]
dup = sorted({s for s in secs if secs.count(s) > 1})
if secs:
    holes = sorted(set(range(min(secs), max(secs) + 1)) - set(secs))
    print(f"§ heads: {secs}")
    print(f"  §§ run continuously 1..21 across both Parts (they do NOT restart). "
          f"missing in range={holes if holes else 'none'}  "
          f"repeated={dup if dup else 'none'}")
else:
    print("§ heads: none yet")

print(f"footnotes: {body.count(chr(92)+'footnote')} | "
      f"emph: {body.count(chr(92)+'emph')} | "
      f"textit: {body.count(chr(92)+'textit')} | "
      f"sic: {body.count(chr(92)+'sic')}")

# ---------------------------------------------------------------------------
# QUOTE BALANCE against the LOGGED DEFECTS, not against zero.
#
# This book's printer left unmatched quotation marks, which are transcribed as
# printed. So the raw balance is not supposed to be zero, and — worse — the
# defects can CANCEL: after p.86 the raw balance returned to 0 not because the
# quotes are sound but because a missing opener at p.29 and a missing closer at
# p.86 happened to offset. A bare "balance=0" would have read as all-clear.
#
# So: list every logged defect with its page and its effect, and compare the raw
# balance to the sum. Add a line here whenever a new one is found and logged.
QUOTE_DEFECTS = [
    (29,  -1, "Sibbern quotation CLOSES with “ and has no opening „ anywhere"),
    (86,  +1, "quotation opened „Hvis A er et … at p.85's foot never closes"),
    (111, +4, "TWO quotations („Ansich„ and „…Mediationens Strøm„) each CLOSE with "
              "the low „ instead of “ — verified at 8x, marks on the baseline where "
              "p.112's vide?“ sets the pair at ascender height. +2 each."),
    (124, +1, "„Logische Untersuchungen, 1ster Band Pag. 46=55) never closes its „"),
    (142, -1, "Hegel quotation CLOSES with “ after Aeußeres but was never opened — "
              "clean word-space paper between the colon and So, verified twice"),
    (195, -1, "Wissen quotation CLOSES with “ (…sinnliches Wissen“.) and was never "
              "opened — clean paper between the comma and 'ist'; ABBYY agrees"),
    (223, +1, "„Ideens fuldkomne Selvmeddelelse i sine naturlige Producter … never "
              "closes its „ (both witnesses agree)"),
]

# A quotation may legitimately be OPEN at the transcription frontier: p.180 opens a
# Schelling quotation that closes on p.181. That is a page split, not a defect, and it
# must not be logged as one — it disappears when the next batch is spliced. List any
# such span here with the page whose splice closes it, and REMOVE the row then.
OPEN_AT_FRONTIER = [
    # (181, +1, ...) removed: pp.181- are spliced, so that span now closes in-file.
    # NB the Bacon span open across p.240/241 is a PARENTHESIS and an italic run, not a
    # quotation: it involves no „ or “ and so has NO effect on this balance. Recorded in
    # RESUME-NOTES instead. Do not add non-quote spans here.
]

op, cl = body.count("„"), body.count("“")
raw = op - cl
pages_done = max(pages) if pages else 0
expected = sum(d for pg, d, _ in QUOTE_DEFECTS if pg <= pages_done)
pending = [(pg, d, w) for pg, d, w in OPEN_AT_FRONTIER if pg > pages_done]
expected += sum(d for _, d, _ in pending)
status = "MATCHES the logged defects" if raw == expected else "*** DOES NOT MATCH ***"
print(f"quotes: „={op} “={cl}  raw balance={raw:+d}")
print(f"  expected {expected:+d} from {sum(1 for pg,_,_ in QUOTE_DEFECTS if pg<=pages_done)} "
      f"logged defect(s) -> {status}")
for pg, d, why in QUOTE_DEFECTS:
    if pg <= pages_done:
        print(f"    p.{pg}: {d:+d}  {why}")
for pg, d, why in pending:
    print(f"    OPEN AT FRONTIER {d:+d}  {why}")
if raw == expected and expected == 0 and QUOTE_DEFECTS:
    print("  NB raw zero here is defects CANCELLING, not quotes being sound.")

# The Indhold reproduction in the front matter legitimately uses centre blocks
# (it is a facsimile of the printed contents, not a structural head), so the
# hand-rolled-head test runs only over \mainmatter.
main = body.split(r"\mainmatter", 1)[-1]

OFFSET_MAIN = body.index(r"\mainmatter") if r"\mainmatter" in body else 0

bad = []
CHECKS = [
    (r"\bo:", "id-est mark typed as plain 'o:' — should be ɔ:", body, 0),
    (r"ﬀ|ﬁ|ﬂ|ſ|œ", "raw OCR ligature/long-s left in the text", body, 0),
    (r"\biffe\b|\bife\b|\bfan\b|\bfunne\b|\bfun\b|\bffal\b|\bselo\b",
     "uncorrected Fraktur OCR error", body, 0),
    # Fraktur I misread as J. But Jeg/Jeget/Jegets is this book's commonest
    # technical term; Jord/Ja/Jo/Jordan are ordinary words; Jfr is the standard
    # "jævnfør" abbreviation; and Jacobi is F. H. Jacobi. All correct as J.
    # "Just" (= netop) is an ordinary Danish adverb and is printed with J; both
    # OCR witnesses agree on it at p.53. "Jern"/"Jernet" (p.209) and "Jesuitismens" (p.238) likewise.
    (r"\bJ(?!eg\b|eg[a-zæøå]|ord|a\b|o\b|ordan|fr\b|acobi|ust\b|ern|esuit)[a-zæøå]{2,}",
     "Fraktur I read as J (Jdee, Jndhold, ...)", body, 0),
    # A straight " used as a quotation mark. Not preceded by a backslash: \" is
    # the umlaut accent command (\"a for ä in "Qvidit\"at", printed p. 32), and
    # is legitimate.
    (r'(?<!\\)"', "straight double quote — this book uses „ and “", body, 0),
    (r"\\footnote", "this book has NO footnotes — check the image again", body, 0),
    (r"(?m)^\\begin\{center\}(?!\\rule).*\{\\(?:bf|Large|large)",
     "hand-rolled display head — use \\deel / \\capitel / \\parag instead",
     main, OFFSET_MAIN),
]
for pat, why, where, off in CHECKS:
    for m in re.finditer(pat, where):
        line = body[:off + m.start()].count(chr(10)) + 1
        bad.append(f"  line {line}: {why} -> {m.group()!r}")
bad.sort(key=lambda s: int(s.split()[1].rstrip(":")))
print(f"suspect readings: {len(bad)}")
for b in bad[:15]:
    print(b)
if len(bad) > 15:
    print(f"  ... and {len(bad)-15} more")
