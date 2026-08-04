#!/usr/bin/env python3
"""Structural check for transcription.tex. No LaTeX compile -- see RESUME-NOTES.md
for why the sandbox must never write transcription.pdf."""
import re, sys

path = sys.argv[1] if len(sys.argv) > 1 else "transcription.tex"
raw = open(path, encoding="utf-8").read()
# strip comments so % sic: / % ERRATUM notes don't pollute the counts
body = "\n".join(re.sub(r"(?<!\\)%.*$", "", l) for l in raw.split("\n"))


def kb(p):
    """PDF page for a printed page in the KB scan (misbound leaf at 260-275)."""
    if p <= 259:
        return p + 13
    if p <= 273:
        return p + 15
    if p <= 275:
        return p - 1
    return p + 13


print("braces balanced:", body.count("{") == body.count("}"))
print("$ even:", body.count("$") % 2 == 0)

m = [(int(a), int(b)) for a, b in
     re.findall(r"---- printed p\.(\d+) \(PDF (\d+)\) ----", raw)]
gaps = [p for i, (p, _) in enumerate(m) if p != i + 1]
bad = [(p, pdf, kb(p)) for p, pdf in m if pdf != kb(p)]
print(f"pages: {m[0][0]}..{m[-1][0]}  n={len(m)}  gaps={gaps or 'none'}")
print("offsets correct:", not bad, bad[:5] if bad else "")

print("footnotes:", body.count("\\footnote{"),
      "| sic:", raw.count("% sic:"),
      "| errata applied:", raw.count("% ERRATUM"))
print("partheads:", body.count("\\parthead{"),
      "| lettersubs:", body.count("\\lettersub{"),
      "| greekruns:", body.count("\\greekrun{"),
      "| parmarks:", body.count("\\parmark{"))

# Running balance of Danish quotes. FOUR openers are never closed BY THE PRINTER:
#   1. one early dropped opener (p.71 footnote / p.72)
#   2. the Strauss quotation of pp.280-282
#   3. the Bethesda quotation on p.294 („end mere søgte ... Gud lig;)
#   4. the Martensen quotation in the p.294 footnote („De tre første Evangelier)
# so the standing expected balance is 4. A batch that ends mid-quotation reads
# higher; check the last transcribed page before treating that as a bug.
bal, neg = 0, []
for i, line in enumerate(body.split("\n"), 1):
    for ch in line:
        if ch == "„":
            bal += 1
        elif ch == "“":
            bal -= 1
            if bal < 0:
                neg.append(i)
                bal = 0
print(f"quote balance: {bal} (standing expectation 4; higher = quote open at the cut)")
print("dropped openers at lines:", neg or "none", "(expect exactly one)")

done = len(m)
print(f"progress: {done}/537 = {done/537*100:.1f}%")
