#!/bin/sh
# ebook-method/kort-oversigt/rebuild.sh -- rebuild texts/hoeffding/kort-oversigt/transcription.tex from the
# scan (NB's ALTO layer), the tesseract cache, and the decisions and patches in this folder.  Run from the repo root:
#   sh ebook-method/kort-oversigt/rebuild.sh
# (1) draft from NB's layer + patches.PATCHES + the headings (HEADS); (2) collate against tesseract and apply
# decisions.tsv with the italics (ONCE per fresh draft: a second --apply on the applied text is wrong); (3) POST:
# patches.POST, postfix.tsv, spaced.tsv.  Logs go to files, never through a pipe (a pipe hides a failing step's status).
set -e
D=ebook-method/kort-oversigt; L=/tmp/kort-rebuild-$$
mkdir -p $L
python3 $D/draft.py --emit --force > $L/1-draft.log; grep -v '^  p\. ' $L/1-draft.log | tail -3
python3 ebook-method/collate/check.py kort-oversigt --italics --apply > $L/2-check.log; grep -v '^[CI][0-9]' $L/2-check.log | tail -6
python3 $D/draft.py --post > $L/3-post.log; cat $L/3-post.log
echo "logs: $L"
