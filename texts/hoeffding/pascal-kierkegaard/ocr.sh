#!/bin/bash
# usage: ocr.sh <printed_first> [n_pages]     (default n = 9)
#
# French antiqua OCR for a whole batch in one call.
#
# This text is NOT Fraktur — it is clean 1923 roman type in a well-printed
# Paris journal, so tesseract's French model reads it very well and the OCR
# carries the WORDS. The page image only has to carry structure (paragraphing,
# footnotes, the section numerals), italics, and the non-French quotations.
#
# The Internet Archive item already ships a tesseract 5.3 `-l fra` text layer
# (Revue_de_métaphysique_et_de_morale_-_30,_2_djvu.txt). Treat that as a SECOND
# WITNESS: it fails differently from a fresh local run, so where the two agree
# the reading is safe and where they differ, look at the image.
#
# Watch for, because tesseract-fra mangles them and they matter here:
#   - Danish in the Kierkegaard quotations: æ ø å, and 1923-era aa
#   - Greek, if Høffding quotes any
#   - accented French: é è ê à ù û ï — especially è/é confusion
#   - guillemets « » read as < < or K K
#   - the long dash — read as - or _
set -e
D="$(cd "$(dirname "$0")" && pwd)"
SCAN="$(python3 "$D/pagemap.py" --scan)"
FIRST=$1; N=${2:-9}

# The sandbox tesseract ships only `eng` + `osd` — no `fra`. Fall back rather
# than die, but say so loudly: the English model drops French accents wholesale
# (é è ê à ù û ï all come back bare) and mangles guillemets. With `-l eng` the
# OCR is a POSITIONING aid only; the reading of every accented word has to come
# off the image.
LANG=fra
tesseract --list-langs 2>/dev/null | grep -qx fra || {
  LANG=eng
  echo "!!! tesseract has no 'fra' model — falling back to -l eng." >&2
  echo "!!! Accents and guillemets in the output below are NOT trustworthy." >&2
}
TMP="$(mktemp -d)"                 # never render inside the repo
trap 'rm -rf "$TMP"' EXIT

for p in $(seq "$FIRST" $(( FIRST + N - 1 ))); do
  P=$(python3 "$D/pagemap.py" "$p")
  pdftoppm -f "$P" -l "$P" -r 300 -png -singlefile "$SCAN" "$TMP/pg" >/dev/null 2>&1
  echo "===== printed p.$p (PDF $P) ====="
  tesseract "$TMP/pg.png" stdout -l "$LANG" --psm 6 2>/dev/null \
    | sed -e 's/ﬁ/fi/g' -e 's/ﬂ/fl/g' -e 's/ﬀ/ff/g' -e 's/ſ/s/g' \
          -e 's/«\s*/« /g' -e 's/\s*»/ »/g' \
    | tr -s ' '
done

cat <<'NOTE'

--- still to fix by hand (not safely mechanisable) ---
  Danish words inside quotations (tesseract -l fra has no æ ø å)
  è/é and à/a confusion; circumflexes dropped
  italics are INVISIBLE to OCR — read them off the image, every time
  footnote rules and marks; small-caps in the running heads
NOTE
