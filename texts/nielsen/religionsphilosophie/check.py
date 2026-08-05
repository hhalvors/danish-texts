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
# and ONE closer is never opened:
#   5. the Hase quotation of pp.349-350 („Verbum divinum ... til Evangeliet“)
#   8. the Grundtvig quotation resumed on p.500 after an ellipsis with no opener
#      („Det Samme gjælder om Konst-Ordet ... lader sig døbe paa“)
# and TWO more unmatched openers:
#   6. the Strauss/Hegel quotation on p.376 („Modsætningen mellem Substans og
#      Subject ...), which runs on into Nielsen's own voice unclosed.
#   7. the Ideekjærlighed quotation on p.416 („den forvandler sig til lutter
#      Indhold.), likewise never closed.
# All confirmed by collation against the Bodleian copy.
#
# !! The "dropped openers" list below will NOT catch #5 or #8. A stray “ only
# registers there if the running balance is already 0; here each merely cancels
# one of the standing unmatched openers. The running total is therefore
#     9 never-closed openers - 2 never-opened closers (p.350, p.500) = 7.
#      (7th = the p.524 footnote opener „Naar Du derimod…; 8th and 9th are both
#       on p.527 — the Greek „Ἔδοξε … and „Da besluttede Apostlene …)
# THE BODY IS COMPLETE (pp.1-537), so 7 is now the FINAL figure, not a running
# one: any deviation from it means something has been edited by mistake.
# ANY entry in the neg list beyond the single expected one is a real error.
# A batch that ends mid-quotation reads one higher; check the last transcribed
# page before treating that as a bug.
STANDING = 7
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
print(f"quote balance: {bal} (standing expectation {STANDING}; "
      f"higher = quote open at the cut)")
print("dropped openers at lines:", neg or "none", "(expect exactly one)")

done = len(m)
print(f"progress: {done}/537 = {done/537*100:.1f}%")
