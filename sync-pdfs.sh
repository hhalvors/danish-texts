#!/usr/bin/env bash
# sync-pdfs.sh
# Copy compiled PDFs from phi423 readings into the danish-texts repo,
# compile any tex files that don't yet have PDFs, then commit everything.

set -e

REPO="$HOME/danish-texts"
PHI423="$HOME/hhalvors.github.io/courses/phi423_s2026/readings"

echo "==> Copying PDFs from phi423 readings..."

cp "$PHI423/nielsen-darwin/transcription.pdf"     "$REPO/texts/nielsen/darwinismen/"
cp "$PHI423/nielsen-darwin/translation.pdf"       "$REPO/texts/nielsen/darwinismen/"

cp "$PHI423/nielsen-propaedeutik/transcription.pdf" "$REPO/texts/nielsen/propaedeutik-darwin/"
cp "$PHI423/nielsen-propaedeutik/translation.pdf"   "$REPO/texts/nielsen/propaedeutik-darwin/"

cp "$PHI423/hoffding-darwin/transcription.pdf"    "$REPO/texts/hoeffding/darwinismen/"
cp "$PHI423/hoffding-darwin/translation.pdf"      "$REPO/texts/hoeffding/darwinismen/"

cp "$PHI423/hoffding-realisme/transcription.pdf"  "$REPO/texts/hoeffding/realisme/"
cp "$PHI423/hoffding-realisme/translation.pdf"    "$REPO/texts/hoeffding/realisme/"

echo "==> Compiling Brøchner PDFs..."
cd "$REPO/texts/brochner/problemet-tro-viden"
pdflatex -interaction=nonstopmode transcription.tex
pdflatex -interaction=nonstopmode translation.tex

echo "==> Compiling Nielsen Om det oprindelige Forhold PDFs..."
cd "$REPO/texts/nielsen/om-oprindelige-forhold"
pdflatex -interaction=nonstopmode transcription.tex
pdflatex -interaction=nonstopmode translation.tex

echo "==> Compiling Nielsen Theologiens Naturbegreb PDFs..."
cd "$REPO/texts/nielsen/theologiens-naturbegreb"
pdflatex -interaction=nonstopmode transcription.tex
pdflatex -interaction=nonstopmode translation.tex

echo "==> Committing to git..."
cd "$REPO"
git add texts/
git commit -m "Add/refresh PDFs for all complete texts"
git push

echo "==> Done."
