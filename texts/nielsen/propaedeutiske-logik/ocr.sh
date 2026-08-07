#!/bin/bash
# usage: ocr.sh <printed_first> [n_pages]     (default n = 12)
#
# Fraktur OCR for a whole batch in one call, with this book's systematic
# confusions corrected mechanically. The OCR carries the WORDS; the page image
# only has to carry structure (§ heads, Anm. paragraphs, rules) and emphasis.
#
# This scan reads WELL under the Fraktur model — better than Evangelietroen.
# A second, independent witness is free here: the PDF's own ABBYY layer,
#   pdftotext -f P -l P -layout "$SCAN" -
# which fails differently (it loses æ/ø, reads I as J). Where the two agree the
# reading is safe; where they differ, look at the image.
#
# NOTE the scan is 105 MB and pdftoppm seeks slowly: budget ~6 s per page, so a
# 12-page batch is ~2 minutes. Run this in its own call with timeout >= 240000.
set -e
D="$(cd "$(dirname "$0")" && pwd)"
SCAN="$(python3 "$D/pagemap.py" --scan)"
export TESSDATA_PREFIX="${TESSDATA_PREFIX:-/tmp/tessdata}"
FIRST=$1; N=${2:-12}
T="$(mktemp -d)"
trap 'rm -rf "$T"' EXIT

for p in $(seq "$FIRST" $(( FIRST + N - 1 ))); do
  P=$(python3 "$D/pagemap.py" "$p")
  # -singlefile + a unique dir: never glob /tmp for the render (see playbook §6)
  pdftoppm -f "$P" -l "$P" -r 300 -png -singlefile "$SCAN" "$T/page"
  echo "===== printed p.$p (PDF $P) ====="
  tesseract "$T/page.png" stdout -l Fraktur --psm 6 2>/dev/null \
    | sed -e 's/ſ/s/g' \
          -e 's/œæ/æ/g'           -e 's/æœ/æ/g'      -e 's/œ/æ/g' \
          -e 's/ﬀ/ff/g'           -e 's/ﬁ/fi/g'      -e 's/ﬂ/fl/g' \
          -e 's/\bJnd/Ind/g'      -e 's/\bJmpres/Impres/g' \
          -e 's/\bJdee/Idee/g'    -e 's/\bJdea/Idea/g' \
          -e 's/\bJntet\b/Intet/g' -e 's/\bJagttag/Iagttag/g' \
          -e 's/\bJmagination/Imagination/g' -e 's/\bJronie/Ironie/g' \
          -e 's/\bffal\b/skal/g'  -e 's/\bfal\b/skal/g' \
          -e 's/\bffulde\b/skulde/g' \
          -e 's/\biffe\b/ikke/g'  -e 's/\bife\b/ikke/g' \
          -e 's/\bfunne\b/kunne/g' -e 's/\bfan\b/kan/g'  -e 's/\bfun\b/kun/g' \
          -e 's/\bnof\b/nok/g'    -e 's/\bfif\b/fik/g' \
          -e 's/\bselo\b/selv/g'  -e 's/\bfelo\b/selv/g' \
          -e 's/\bDie\b/Øie/g'    -e 's/\bDiet\b/Øiet/g' \
          -e "s/[´\`’ˆ¨]//g" \
    | tr -s ' '
done

cat <<'NOTE'

--- still to fix by hand (not safely mechanisable) ---
  NB the J->I rule is a WHITELIST on purpose. A blanket 's/\bJ\([a-zæøå]\)/I\1/'
  destroys this book's commonest technical term: Jeg / Jeget / Jegets / Ikke=Jeg,
  and also Jord, Jordbund, Ja, Jo. Do not "improve" it into a general rule.
  f/k confusion inside words the sed table does not list (Adſfillelſe->Adskillelse)
  v read as o inside words (ſelo->selv, objectio->objectiv, bles->blev)
  ll read as ﬅ/ff in the abbreviations  o. s. f.  and  o. s. v.
  dropped ø  (gjore->gjøre, horer->hører, Sporgsmaal->Spørgsmaal)
  B/V confusion (BVillede->Billede), 0<->o, 9<->y
  gutter/edge noise: --psm 6 picks up the facing leaf's black edge as stray
    '|', 'l', 'i', ':' at the right margin. Ignore those columns.
  ALL letterspacing: run  python3 spacing.py <pages>
  STRUCTURE: § heads, Anm. paragraphs (smaller type), rules -- image only.
NOTE
