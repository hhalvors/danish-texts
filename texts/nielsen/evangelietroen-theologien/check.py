#!/usr/bin/env python3
"""
check.py [transcription.tex]

Automated invariants, so that verifying a batch does not mean re-reading the
file. Run it at the START of every batch (batch.sh does this for you): it
reports on what the previous sitting wrote.

Page-marker convention for this book:  % --- p. N ---  on its own line, at the
point where printed page N BEGINS. check.py uses these to find gaps and to
report progress, so put one in for every page.
"""
import re, sys, os

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
    print(f"progress: {hi}/174 = {hi/174*100:.1f}%   next page to transcribe: {hi+1}")
else:
    print("pages: no arabic  % --- p. N ---  markers yet "
          "(the Forord's roman ones are ignored)")
    print("progress: 0/174 = 0.0%   next page to transcribe: 1")

print(f"braces balanced: {body.count('{') == body.count('}')}"
      f"  ({body.count('{')} open / {body.count('}')} close)")
print(f"$ even: {body.count('$') % 2 == 0}")
print(f"markers remaining (text to be added): {src.count('text to be added')}")
print(f"footnotes: {body.count(chr(92)+'footnote')} | "
      f"emph: {body.count(chr(92)+'emph')} | "
      f"textit: {body.count(chr(92)+'textit')} | "
      f"sic: {body.count(chr(92)+'sic')}")

op, cl = body.count("„"), body.count("“")
print(f"quotes: „={op} “={cl}  balance={op-cl}   (expect 0 unless a defect is logged)")

bad = []
for pat, why in [(r"[^-]---[^-]", None),
                 (r"\bo:", "id-est mark typed as plain 'o:' — should be ɔ:"),
                 (r"ﬀ|ﬁ|ﬂ|ſ", "raw OCR ligature/long-s left in the text"),
                 (r"\biffe\b|\bife\b|\bsulde\b|\bfan\b", "uncorrected Fraktur OCR error")]:
    if why:
        for m in re.finditer(pat, body):
            bad.append(f"  line {body[:m.start()].count(chr(10))+1}: {why} -> {m.group()!r}")
print(f"suspect readings: {len(bad)}")
for b in bad[:15]:
    print(b)
