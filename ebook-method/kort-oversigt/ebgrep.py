#!/usr/bin/env python3
"""ebook-method/kort-oversigt/ebgrep.py WORD... -- show each word in the e-book (with context) and in the transcription
(with line numbers), to compare a doubtful reading across the two texts.  Read-only."""
import os, re, sys, zipfile, html
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
BOOK = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt')
z = zipfile.ZipFile(os.path.join(BOOK, 'Kort_oversigt_over_den_nyere_filosofis_historie.epub'))
EB = re.sub(r'\s+', ' ', ' '.join(html.unescape(re.sub('<[^>]+>', ' ', z.read(n).decode('utf-8'))) for n in sorted(z.namelist()) if n.endswith('.xhtml')))
TX = open(os.path.join(BOOK, 'transcription.tex'), encoding='utf-8').read().split('\n')
for w in sys.argv[1:]:
    ms = list(re.finditer(re.escape(w), EB))[:3]
    print(f'== {w}: e-book {len(ms)}: ' + ' || '.join(EB[max(0, m.start() - 40):m.end() + 30] for m in ms))
    for i, l in enumerate(TX, 1):
        if w in l and not l.lstrip().startswith('%'): print(f'   tex {i}: {l[:140]}')
