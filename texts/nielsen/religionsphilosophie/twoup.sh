#!/bin/bash
# usage: twoup.sh <printed_first> <printed_second>
set -e
D="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$D/.render"

# PDF page for a printed page in the KB scan.
#
# The KB scan (14,-225 8°) is NOT uniformly printed+13: a leaf bearing printed
# pp. 274-275 was scanned TWO LEAVES EARLY, so pp. 260-273 are pushed back by 2.
# Verified by reading the folio numbers off PDF 268-301. The Bodleian copy is
# correctly ordered, so this is a defect of the KB scan, not of the edition.
#
#   printed  <= 259  ->  PDF = printed + 13
#   printed 260-273  ->  PDF = printed + 15
#   printed 274-275  ->  PDF = printed -  1
#   printed  >= 276  ->  PDF = printed + 13
kbpage() {
  local p=$1
  if   [ "$p" -le 259 ]; then echo $(( p + 13 ))
  elif [ "$p" -le 273 ]; then echo $(( p + 15 ))
  elif [ "$p" -le 275 ]; then echo $(( p -  1 ))
  else                        echo $(( p + 13 ))
  fi
}
A=$(kbpage $1); B=$(kbpage $2)
pdftoppm -f $A -l $A -r 160 -gray -png "$D/scan.pdf" /tmp/pa
pdftoppm -f $B -l $B -r 160 -gray -png "$D/scan.pdf" /tmp/pb
montage /tmp/pa-*.png /tmp/pb-*.png -tile 2x1 -geometry +4+0 -background white "$D/.render/p$1-$2.png"
convert "$D/.render/p$1-$2.png" -resize 2000x2000\> -quality 92 "$D/.render/p$1-$2.png"
rm -f /tmp/pa-*.png /tmp/pb-*.png
identify "$D/.render/p$1-$2.png"
