#!/bin/bash
# usage: twoup.sh <printed_first> <printed_second>
set -e
D="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$D/.render"
OFF=13
A=$(( $1 + OFF )); B=$(( $2 + OFF ))
pdftoppm -f $A -l $A -r 160 -gray -png "$D/scan.pdf" /tmp/pa
pdftoppm -f $B -l $B -r 160 -gray -png "$D/scan.pdf" /tmp/pb
montage /tmp/pa-*.png /tmp/pb-*.png -tile 2x1 -geometry +4+0 -background white "$D/.render/p$1-$2.png"
convert "$D/.render/p$1-$2.png" -resize 2000x2000\> -quality 92 "$D/.render/p$1-$2.png"
rm -f /tmp/pa-*.png /tmp/pb-*.png
identify "$D/.render/p$1-$2.png"
