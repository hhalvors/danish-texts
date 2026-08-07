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

op, cl = body.count("„"), body.count("“")
print(f"quotes: „={op} “={cl}  balance={op-cl}   (expect 0 unless a defect is logged)")

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
    (r"\bJ(?!eg\b|eg[a-zæøå]|ord|a\b|o\b|ordan|fr\b|acobi)[a-zæøå]{2,}",
     "Fraktur I read as J (Jdee, Jndhold, ...)", body, 0),
    (r'"', "straight double quote — this book uses „ and “", body, 0),
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
