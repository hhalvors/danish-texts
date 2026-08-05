#!/bin/bash
# usage: ocr.sh <printed_first> [n_pages]     (default n = 12)
#
# Fraktur OCR for a whole batch in one call, with this book's closed set of
# systematic Fraktur confusions corrected mechanically. The remaining errors are
# few enough to fix while writing; the point is that the OCR carries the WORDS,
# so the page image only has to carry structure and emphasis.
#
# Unlike the Religionsphilosophie scan (Antiqua, scrambled reading order), the
# Fraktur model reads this book cleanly — that is why this book gets an OCR-first
# pipeline and that one did not.
set -e
D="$(cd "$(dirname "$0")" && pwd)"
SCAN="$(python3 "$D/pagemap.py" --scan)"
export TESSDATA_PREFIX="${TESSDATA_PREFIX:-/tmp/tessdata}"
FIRST=$1; N=${2:-12}

for p in $(seq $FIRST $(( FIRST + N - 1 ))); do
  P=$(python3 "$D/pagemap.py" $p)
  pdftoppm -f $P -l $P -r 300 -png "$SCAN" /tmp/ocr >/dev/null 2>&1
  echo "===== printed p.$p (PDF $P) ====="
  tesseract /tmp/ocr-*.png stdout -l Fraktur --psm 6 2>/dev/null \
    | sed -e 's/ſ/s/g' \
          -e 's/œ/æ/g' \
          -e 's/\biffe\b/ikke/g'   -e 's/\bife\b/ikke/g' \
          -e 's/ﬀal/skal/g'        -e 's/\\kal/skal/g' \
          -e 's/\bsulde\b/skulde/g' -e 's/ﬀulde/skulde/g' \
          -e 's/\bfritisfe\b/kritiske/g' \
          -e 's/\bnof\b/nok/g'     -e 's/\bNofk\b/Nok/g' \
          -e 's/\bfif\b/fik/g' \
          -e 's/\bselo\b/selv/g' \
          -e 's/\bJronie\b/Ironie/g' \
          -e 's/\bJndsigelser\b/Indsigelser/g' \
          -e 's/\bJagttager\b/Iagttager/g' \
          -e "s/[´\`’ˆ¨]//g" \
    | tr -s ' '
  rm -f /tmp/ocr-*.png
done

cat <<'NOTE'

--- still to fix by hand (not safely mechanisable) ---
  f/k confusion inside words the sed table does not list (fan->kan, beflageligt->beklageligt)
  dropped ø  (gjore->gjøre, horer->hører, sergeligt->sørgeligt)
  Fraktur long-s runs, 0<->o, 9<->y  (udtr9ffelig -> udtrykkelig)
  ALL letterspacing: run  python3 spacing.py <pages>
NOTE
