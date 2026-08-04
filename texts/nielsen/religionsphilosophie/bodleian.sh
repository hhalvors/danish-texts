#!/bin/bash
# bodleian.sh <printed_first> [printed_second]
#
# Renders a page (or facing pair) from the SECOND WITNESS: the Google Books scan
# of the Bodleian copy of Religionsphilosophie (1869), for collation wherever the
# KB scan (scan.pdf, shelfmark 14,-225 8°) is damaged or unclear.
#
#   KB   scan.pdf     : PDF = printed + 13
#   Bod. bodleian.pdf : PDF = printed + 14   <-- note: NOT the same
#
# The Bodleian PDF has NO usable OCR text layer (only the Google front matter),
# so collation there is necessarily visual.
#
# The scan must sit NEXT TO THIS SCRIPT as bodleian.pdf (gitignored), the same
# way scan.pdf does. It used to be read straight out of ~/bibliotek, but the
# render sandbox only mounts the repo, so the old path resolved to nothing and
# collation silently became impossible. Keep the local copy. To refresh it:
#
#   cp ~/bibliotek/"Nielsen, Rasmus"/religion-1869.pdf \
#      texts/nielsen/religionsphilosophie/bodleian.pdf
set -e
D="$(cd "$(dirname "$0")" && pwd)"
B="$D/bodleian.pdf"
[ -f "$B" ] || { echo "Bodleian scan not found at: $B
Copy it in with:
  cp ~/bibliotek/\"Nielsen, Rasmus\"/religion-1869.pdf \\
     \"$D/bodleian.pdf\"" >&2; exit 1; }
mkdir -p "$D/.render"
OFF=14
A=$(( $1 + OFF ))
pdftoppm -f $A -l $A -r 170 -gray -png "$B" /tmp/bodA
if [ -n "$2" ]; then
  C=$(( $2 + OFF ))
  pdftoppm -f $C -l $C -r 170 -gray -png "$B" /tmp/bodB
  montage /tmp/bodA-*.png /tmp/bodB-*.png -tile 2x1 -geometry +4+0 -background white \
    "$D/.render/bod_p$1-$2.png"
  OUT="$D/.render/bod_p$1-$2.png"
else
  cp /tmp/bodA-*.png "$D/.render/bod_p$1.png"
  OUT="$D/.render/bod_p$1.png"
fi
convert "$OUT" -resize 2000x2000\> -quality 92 "$OUT"
rm -f /tmp/bodA-*.png /tmp/bodB-*.png
identify "$OUT"
