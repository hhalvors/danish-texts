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
#
# Authentication: uses HTTPS. When prompted for a password, use a
# GitHub personal access token (not your account password):
#   github.com → Settings → Developer settings → Personal access tokens
#   → Tokens (classic) → Generate new token → tick "repo" → copy token

set -e
cd "$(dirname "$0")"

git init
git add .
git commit -m "Initial commit: Nielsen Religionsphilosophie Indledning §§1-2"
git branch -M main
git remote add origin https://github.com/hhalvors/danish-texts.git
git push -u origin main

echo ""
echo "Done. Now enable GitHub Pages in the repo settings:"
echo "  Settings → Pages → Source: Deploy from branch → main / (root)"
echo "  The site will appear at: https://hhalvors.github.io/danish-texts/"
