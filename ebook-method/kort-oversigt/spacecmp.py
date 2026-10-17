#!/usr/bin/env python3
"""ebook-method/kort-oversigt/spacecmp.py -- LETTERSPACING measured on the page images (betingelserne-villie's
spacedsheets.py measure: the white columns inside a tesseract word box per letter gap, as a fraction of the box height),
set against the transcription's \\emph (from the e-book, emarks.py) page by page (2026-10-14).
    python3 ebook-method/kort-oversigt/spacecmp.py [TH]   -> .parts/spacecmp.tsv (page, word, score, in-emph, box)
and prints the score distribution of words inside and outside \\emph, and the disagreements at the threshold."""
import os, re, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE)); sys.path.insert(0, HERE)
import pagemap as C
BOOK = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt'); OUT = os.path.join(BOOK, '.render')
TH = float(sys.argv[1]) if len(sys.argv) > 1 else 0.105
Lr = re.compile(r'[A-Za-zÀ-ÖØ-öø-ÿ]'); K = lambda s: re.sub(r'[^a-zæøåäöüéèàò]', '', s.lower())
TEX = open(os.path.join(BOOK, 'transcription.tex'), encoding='utf-8').read()
PG = dict(re.findall(r'% --- p\. (\d+) ---\n(.*?)(?=% --- p\. \w+ ---|\\end\{document\})', TEX, re.S))
rows = []
for p in C.PAGES:
    em = set(); t = PG.get(str(p), '')
    for m in re.finditer(r'\\emph\{([^{}]*)\}', t): em.update(K(w) for w in m.group(1).split())
    allw = {K(w) for w in re.sub(r'\\[a-zA-Z]+|[{}]', ' ', t).split()}
    im = Image.open(os.path.join(OUT, f'kort-oversigt-p{p}-300.png')).convert('L')
    for r in open(os.path.join(BOOK, '.parts', 'collate', 'ocr', f'p{p}.tsv'), encoding='utf-8').read().splitlines()[1:]:
        r = r.split('\t')
        if len(r) != 12 or r[0] != '5' or not re.fullmatch(r'\W*[A-Za-zÀ-ÖØ-öø-ÿ]{3,}\W*', r[11].strip()): continue
        x, y, ww, hh = map(int, r[6:10]); n = len(Lr.findall(r[11]))
        if n < 5: continue
        c = im.crop((x, y, x + ww, y + hh)); px = c.load()
        ink = [sum(1 for j in range(c.height) if px[i, j] < 150) for i in range(c.width)]
        runs, r0 = [], None
        for i, v in enumerate(ink + [1]):
            if v == 0 and r0 is None: r0 = i
            if v and r0 is not None: runs.append(i - r0); r0 = None
        s = sum(runs[1:-1]) / max(1, n - 1) / hh if len(runs) > 2 else 0
        rows.append((p, r[11], round(s, 3), K(r[11]) in em, f'{x},{y},{ww},{hh}'))
open(os.path.join(BOOK, '.parts', 'spacecmp.tsv'), 'w', encoding='utf-8').write('\n'.join('\t'.join(map(str, r)) for r in rows) + '\n')
import statistics as S
a = sorted(r[2] for r in rows if r[3]); b = sorted(r[2] for r in rows if not r[3])
q = lambda v: [v[int(len(v) * f)] for f in (0.05, 0.25, 0.5, 0.75, 0.95)] if v else []
print('in \\emph:', len(a), q(a)); print('outside:', len(b), q(b), 'over TH:', sum(x >= TH for x in b))
print('emph words under TH:', [(r[0], r[1], r[2]) for r in rows if r[3] and r[2] < TH][:40])
print('non-emph over TH:', [(r[0], r[1], r[2]) for r in rows if not r[3] and r[2] >= TH][:60])
