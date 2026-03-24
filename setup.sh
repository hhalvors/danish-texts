#!/bin/bash
# Run this once from ~/danish-texts/ to initialize the git repo
# and connect it to GitHub.
#
# Prerequisites:
#   1. Create a new repo at https://github.com/new
#      Name: danish-texts
#      Visibility: Public
#      Do NOT initialize with README (we already have one)
#   2. Run this script

set -e
cd "$(dirname "$0")"

git init
git add .
git commit -m "Initial commit: Nielsen Religionsphilosophie Indledning §§1-2"
git branch -M main
git remote add origin git@github.com:hhalvors/danish-texts.git
git push -u origin main

echo ""
echo "Done. Now enable GitHub Pages in the repo settings:"
echo "  Settings → Pages → Source: Deploy from branch → main / (root)"
echo "  The site will appear at: https://hhalvors.github.io/danish-texts/"
