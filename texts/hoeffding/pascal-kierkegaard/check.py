#!/usr/bin/env python3
"""
check.py [transcription.tex]

Automated invariants, so that verifying a batch does not mean re-reading the
file in the main conversation. Run it after every splice.

Page-marker convention:  % --- p. N ---  on its own line, at the point where
printed page N BEGINS. check.py uses these to find gaps and report progress,
so put one in for every page.

French text, so the quotation-mark check counts « » rather than the Danish
„ “. Balance should be 0 unless a printer's defect is logged at the site with
a % comment — see the editorial stance in ../../../CLAUDE.md.
"""
import re, sys, os

FIRST, LAST = 221, 246
N_PAGES = LAST - FIRST + 1

PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "transcription.tex")
src = open(PATH, encoding="utf-8").read()

pages = [int(m) for m in re.findall(r"^%\s*---\s*p\.\s*(\d+)\s*---", src, re.M)]
body = re.sub(r"(?m)^\s*%.*$", "", src)          # ignore comments for counting

print(f"file: {os.path.basename(PATH)}  ({len(src)/1024:.0f} KB)")

if pages:
    lo, hi = min(pages), max(pages)
    missing = sorted(set(range(FIRST, hi + 1)) - set(pages))
    dupes = sorted({p for p in pages if pages.count(p) > 1})
    stray = sorted(p for p in set(pages) if not FIRST <= p <= LAST)
    print(f"pages: {lo}..{hi}  n={len(pages)}  "
          f"gaps={missing if missing else 'none'}  "
          f"dupes={dupes if dupes else 'none'}  "
          f"out-of-range={stray if stray else 'none'}")
    done = hi - FIRST + 1
    print(f"progress: {done}/{N_PAGES} = {done/N_PAGES*100:.1f}%   "
          f"next page to transcribe: {hi + 1 if hi < LAST else '— done —'}")
else:
    print("pages: no  % --- p. N ---  markers yet")
    print(f"progress: 0/{N_PAGES} = 0.0%   next page to transcribe: {FIRST}")

print(f"braces balanced: {body.count('{') == body.count('}')}"
      f"  ({body.count('{')} open / {body.count('}')} close)")
print(f"$ even: {body.count('$') % 2 == 0}")
print(f"markers remaining (text to be added): {src.count('text to be added')}")
print(f"footnotes: {body.count(chr(92)+'footnote')} | "
      f"emph: {body.count(chr(92)+'emph')} | "
      f"textit: {body.count(chr(92)+'textit')} | "
      f"foreignlang: {body.count(chr(92)+'foreignlanguage')}")

op, cl = body.count("«"), body.count("»")
print(f"guillemets: «={op} »={cl}  balance={op-cl}   (expect 0 unless a defect is logged)")

bad = []
checks = [
    (r'"', "straight ASCII quote — the journal sets « » (or “ ” inside a quotation)"),
    (r"ﬀ|ﬁ|ﬂ|ſ", "raw OCR ligature/long-s left in the text"),
    (r"(?<![-!])--(?!-)", "en-dash typed as -- ; the journal's dash is em, i.e. ---"),
    (r"\baa\b|\bAa\b", "Danish 'aa' left loose — check it is inside a Danish quotation"),
    # NB: in French a space BELONGS before ; : ! ? and inside « », so only a
    # space before a comma or a full stop is an artefact worth flagging.
    (r"[a-zà-ÿ]\s+[,.](\s|$)", "space before a comma/full stop (OCR artefact)"),
    # A stray glyph left by marginal dirt: preceded by a space ON THE SAME LINE
    # (so [^\S\n], not \s — otherwise a lone closing brace on its own line, as
    # in the preamble's \hypersetup block, matches across the newline).
    (r"(?m)\w[^\S\n]+[^\w\s.,;:!?«»'()\[\]{}\\-]$",
     "stray single glyph at end of line (marginal dirt)"),
    (r"<<|>>", "guillemets read by OCR as << / >>"),
]
for pat, why in checks:
    for m in re.finditer(pat, body):
        bad.append(f"  line {body[:m.start()].count(chr(10))+1}: {why} -> {m.group()!r}")
print(f"suspect readings: {len(bad)}")
for b in bad[:20]:
    print(b)
if len(bad) > 20:
    print(f"  ... and {len(bad)-20} more")
