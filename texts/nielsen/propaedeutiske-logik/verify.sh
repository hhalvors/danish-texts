#!/bin/bash
# usage: bash verify.sh
#
# Portable compile test for the sandbox, where libertinus/libertinust1math/
# textalpha/babel-danish are not installed and `make` therefore fails on every
# file in the repo, this one included.
#
# WHY THIS FILE EXISTS. The first version of this recipe was a hand-typed sed
# chain that ALSO rewrote "ɔ:" to "o:" and stripped textalpha. It reported
# 0 errors on a file that could not build on the user's machine at all: the raw
# ɔ (U+0254) was a fatal error under the real preamble, and two more defects
# (duplicate PDF page destinations, and \quad inside \addcontentsline) were
# warnings the recipe never looked at. A test that edits away the thing under
# test is worse than no test. So:
#
#   * The ONLY substitutions are the four packages the sandbox lacks, plus
#     Greek -> placeholder, which textalpha would otherwise render. Nothing else
#     in the source is touched. In particular ɔ: is NOT substituted -- it is
#     handled by \DeclareUnicodeCharacter{0254} in the real preamble, and if that
#     ever regresses this test must fail.
#   * Warnings that are silent killers on the real build are checked explicitly
#     and reported as failures: hyperref "Token not allowed in a PDF string"
#     (a \quad or other non-text token inside \addcontentsline), and pdfTeX
#     "destination with the same identifier" (duplicate page.N labels).
#
# Exit status 0 means clean. Anything else, read the report.
set -u
D="$(cd "$(dirname "$0")" && pwd)"
W=$(mktemp -d); trap 'rm -rf "$W"' EXIT

python3 - "$D/transcription.tex" "$W/t.tex" <<'PY'
import re, sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
s = s.replace(r"\usepackage{libertinus}",       r"\usepackage{lmodern}")
s = s.replace(r"\usepackage{libertinust1math}", "")
s = s.replace(r"\usepackage{textalpha}",        "")
s = s.replace(r"\usepackage[danish]{babel}",    r"\usepackage{babel}")
# textalpha is what renders the polytonic Greek; without it every Greek glyph is
# an error, so map the RANGE to a placeholder. Never delete Greek from the source.
s = re.sub(r'[Ͱ-Ͽἀ-῿]+', '[Gr]', s)
open(dst, "w", encoding="utf-8").write(s)
PY

cd "$W"
for i in 1 2 3; do pdflatex -interaction=nonstopmode t.tex >l.txt 2>&1; done

fail=0
report () { # name, count
  if [ "$2" -eq 0 ]; then printf '  ok    %-42s %s\n' "$1" "$2"
  else printf '  FAIL  %-42s %s\n' "$1" "$2"; fail=1; fi
}

echo "--- $(basename "$D") compile report ---"

# STATIC LINT FOR GREEK, run on the ORIGINAL source, not the substituted copy.
#
# The sandbox cannot compile Greek at all: textalpha/greek-fontenc is not
# installed here, tlmgr cannot install it (local TeX Live 2021 vs a 2026 remote),
# and the compile test therefore has to map the Greek range to a placeholder.
# That means an unusable Greek character sails through every check above and
# then kills the user's build. It has already done so once, with ϑ.
#
# So: lint the source for the Greek *variant/symbol* codepoints that LGR text
# mode rejects. The repo's standing convention (see
# texts/nielsen/religionsphilosophie/transcription.tex) is that these are fount
# variants, not distinct letters, and are normalised to their base letter.
greeklint=$(python3 - "$D/transcription.tex" <<'PY'
import sys, unicodedata
bad = {"ϑ":"θ", "ϰ":"κ", "ϕ":"φ", "ϖ":"π", "ϱ":"ρ", "ϐ":"β", "ϵ":"ε", "ϲ":"σ"}
src = open(sys.argv[1], encoding="utf-8").read()
hits = 0
for n, line in enumerate(src.split("\n"), 1):
    if line.lstrip().startswith("%"):
        continue                      # a comment may discuss the variant form
    for ch, repl in bad.items():
        if ch in line:
            hits += line.count(ch)
            print(f"    line {n}: {ch} U+{ord(ch):04X} "
                  f"{unicodedata.name(ch)} -> normalise to {repl}", file=sys.stderr)
print(hits)
PY
) || true
greekbad=$(printf '%s' "$greeklint" | tail -1)
report "Greek variant glyphs (LGR-fatal)" "${greekbad:-0}"
report "errors (^!)"                    "$(grep -ac '^!' l.txt)"
report "missing characters"             "$(grep -ac 'Missing character' l.txt)"
report "undefined control sequences"    "$(grep -ac 'Undefined control sequence' l.txt)"
report "hyperref: token not allowed"    "$(grep -ac 'Token not allowed in a PDF string' l.txt)"
report "pdfTeX: duplicate destinations" "$(grep -ac 'destination with the same identifier' l.txt)"
report "undefined references"           "$(grep -ac 'LaTeX Warning: Reference' l.txt)"
# Overfull boxes are informational only: the sandbox substitutes lmodern for
# libertinus, so the line breaking here is not the line breaking the real build
# gets. Reported, never a failure.
printf '  info  %-42s %s\n' "overfull hboxes (lmodern, not real)" \
       "$(grep -ac 'Overfull \\hbox' l.txt)"

if [ "$(grep -ac '^!' l.txt)" -ne 0 ]; then
  echo "--- first errors ---"; grep -A3 '^!' l.txt | head -30
fi
grep -o 'Output written.*' l.txt || echo "  NO PDF PRODUCED"
echo "--- log kept at $W/l.txt for this shell only ---"
exit $fail
