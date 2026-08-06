#!/bin/bash
# usage: ocr.sh <printed_first> [n_pages]     (default n = 12)
#
# Fraktur OCR for a whole batch in one call. The sed table below is copied
# verbatim from evangelietroen-theologien's ocr.sh as a starting point — it has
# NOT yet been tuned against this book's own scan, so expect more hand-fixes
# in the first few batches until the confusions specific to this scan are
# known and added here.
#
# The embedded (PyPDF2/KB) text layer in this PDF is a garbled OCR — do not
# use it as a witness (see pagemap.py's docstring for examples: "Msthetisk"
# for "Æsthetisk", "Sporgsmaal" for "Spørgsmaal"). The scan itself looks like
# a clean, crisp Fraktur print (similar condition to evangelietroen), so the
# Fraktur tesseract model run fresh here should do much better than that
# layer — confirm this on the first batch before trusting the pipeline.
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

--- still to fix by hand (not safely mechanisable, and this table is UNTUNED
    for this scan — inherited from evangelietroen-theologien) ---
  f/k confusion inside words the sed table does not list (fan->kan, beflageligt->beklageligt)
  dropped ø  (gjore->gjøre, horer->hører, sergeligt->sørgeligt)
  Fraktur long-s runs, 0<->o, 9<->y  (udtr9ffelig -> udtrykkelig)
  ALL letterspacing: run  python3 spacing.py <pages>
  Watch for NEW confusions specific to this scan and add them here as found.
NOTE
