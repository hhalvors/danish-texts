#!/bin/bash
# batch.sh <first_printed> [n_pages]      (default n = 12)
#
# ONE call per batch. It (a) verifies what the previous sitting wrote, (b) OCRs
# the next twelve pages, (c) reports detected letterspacing for them, and
# (d) renders six two-up images.
#
# Then: read the six PNGs, and write all twelve pages in ONE Edit.
# Next turn: bash batch.sh <first+12>  — which verifies what you just wrote.
#
# The cost of this job is context replay, not transcription. Twelve pages per
# turn, one edit per batch, fresh conversation per sitting.
set -e
D="$(cd "$(dirname "$0")" && pwd)"
FIRST=$1; N=${2:-12}
LAST=$(( FIRST + N - 1 ))

# tesseract models do not persist between sessions
if [ ! -f /tmp/tessdata/Fraktur.traineddata ]; then
  echo "=== fetching Fraktur model (once per session) ==="
  mkdir -p /tmp/tessdata
  wget -q https://github.com/tesseract-ocr/tessdata_best/raw/main/script/Fraktur.traineddata \
       -O /tmp/tessdata/Fraktur.traineddata
  cp -r /usr/share/tesseract-ocr/4.00/tessdata/configs /tmp/tessdata/ 2>/dev/null || true
fi
export TESSDATA_PREFIX=/tmp/tessdata

echo "=== 1. verification of transcription.tex as it stands ==="
python3 "$D/check.py" "$D/transcription.tex"

echo
echo "=== 2. Fraktur OCR, printed pp. $FIRST-$LAST ==="
bash "$D/ocr.sh" $FIRST $N

echo
echo "=== 3. letterspacing candidates (Sperrsatz -> \\emph{}) ==="
python3 "$D/spacing.py" $(seq $FIRST $LAST)

echo
echo "=== 4. two-up renders ==="
p=$FIRST
while [ $p -le $LAST ]; do
  bash "$D/twoup.sh" $p $(( p + 1 )) >/dev/null 2>&1 || true
  echo "  .render/p$p-$(( p + 1 )).png"
  p=$(( p + 2 ))
done
echo
echo "Now: read those PNGs, then ONE Edit for all $N pages."
