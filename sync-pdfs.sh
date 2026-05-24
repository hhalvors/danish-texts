#!/usr/bin/env bash
# sync-pdfs.sh
#
# Push compiled PDFs from danish-texts (the single source of truth)
# out to phi423/readings and any other consumers.
#
# Workflow:
#   1. Edit .tex sources in danish-texts/texts/
#   2. Run 'make' (or 'make -j4') to rebuild PDFs
#   3. Run this script to push PDFs to course directories

set -e

DANISH="$HOME/danish-texts"
PHI423="$HOME/hhalvors.github.io/courses/phi423_s2026/readings"

echo "==> Pushing PDFs from danish-texts to phi423..."

cp "$DANISH/texts/hoeffding/darwinismen/transcription.pdf"    "$PHI423/hoffding-darwin/"
cp "$DANISH/texts/hoeffding/darwinismen/translation.pdf"      "$PHI423/hoffding-darwin/"

cp "$DANISH/texts/hoeffding/realisme/transcription.pdf"       "$PHI423/hoffding-realisme/"
cp "$DANISH/texts/hoeffding/realisme/translation.pdf"         "$PHI423/hoffding-realisme/"

cp "$DANISH/texts/nielsen/darwinismen/transcription.pdf"      "$PHI423/nielsen-darwin/"
cp "$DANISH/texts/nielsen/darwinismen/translation.pdf"        "$PHI423/nielsen-darwin/"

cp "$DANISH/texts/nielsen/propaedeutik-darwin/transcription.pdf" "$PHI423/nielsen-propaedeutik/"
cp "$DANISH/texts/nielsen/propaedeutik-darwin/translation.pdf"   "$PHI423/nielsen-propaedeutik/"

echo "==> Committing danish-texts..."
cd "$DANISH"
git add texts/
git commit -m "Rebuild PDFs" || echo "(nothing to commit)"
git push

echo "==> Done."
