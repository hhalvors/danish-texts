#!/bin/bash
# batch.sh <first_printed> [n_pages]      (default n = 12)
#
# Renders a whole batch as consecutive two-up spreads IN ONE CALL, and prints the
# verification report for what is already in transcription.tex. Written to keep the
# number of tool round-trips per batch at ~1: the cost of this job is dominated by
# context replay, not by the transcribing itself, so do 12 pages per turn, not 2.
#
# Typical use:
#     bash batch.sh 287         -> check report + .render/p287-288.png … p297-298.png
# then read the six PNGs, write all twelve pages in ONE edit, and call
#     bash batch.sh 299         -> checks what you just wrote AND renders the next.
set -e
D="$(cd "$(dirname "$0")" && pwd)"
FIRST=$1
N=${2:-12}

echo "=== verification of transcription.tex as it stands ==="
python3 "$D/check.py" "$D/transcription.tex"

echo
echo "=== rendering printed pp. $FIRST-$(( FIRST + N - 1 )) ==="
p=$FIRST
while [ $p -lt $(( FIRST + N )) ]; do
  bash "$D/twoup.sh" $p $(( p + 1 )) >/dev/null
  echo "  .render/p$p-$(( p + 1 )).png"
  p=$(( p + 2 ))
done
