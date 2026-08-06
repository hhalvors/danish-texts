#!/bin/bash
# usage: twoup.sh <printed_first> <printed_second>
# Renders two printed pages side by side as ONE image.
#
# 130 dpi is deliberate and lower than the Religionsphilosophie harness used.
# There, the image was the only witness. Here the Fraktur OCR carries the words
# and spacing.py carries the emphasis, so the image only has to answer
# structural questions — paragraph breaks, footnotes, section rules, headings —
# plus the occasional doubtful reading. Zoom with crop.sh when you actually doubt.
set -e
D="$(cd "$(dirname "$0")" && pwd)"
SCAN="$(python3 "$D/pagemap.py" --scan)"
mkdir -p "$D/.render"

A=$(python3 "$D/pagemap.py" $1); B=$(python3 "$D/pagemap.py" $2)
pdftoppm -f $A -l $A -r 130 -gray -png "$SCAN" /tmp/pa
pdftoppm -f $B -l $B -r 130 -gray -png "$SCAN" /tmp/pb
montage /tmp/pa-*.png /tmp/pb-*.png -tile 2x1 -geometry +4+0 -background white "$D/.render/p$1-$2.png"
convert "$D/.render/p$1-$2.png" -resize 1800x1800\> -quality 90 "$D/.render/p$1-$2.png"
rm -f /tmp/pa-*.png /tmp/pb-*.png
identify -format "%f %wx%h %b\n" "$D/.render/p$1-$2.png"
