#!/usr/bin/env python3
"""ebook-method/kort-oversigt/lsheets.py -- BLIND crop sheets for the LETTERSPACING of the Noter (2026-10-14).
In this book only the Noter (pp. 148-157) letterspace: the names of the authors cited (spacecmp.py: letter-gap score
0.10-0.25 against 0.02-0.08 for ordinary words; the text pages show no spaced words).  Every Noter line holding a word
that scores >= 0.095 (5+ letters) or >= 0.12 (3-4 letters) is cropped whole; the reader writes the line with every
spaced run in <sp>..</sp> (READER-BRIEF.md, l-sheets); reads.py turns the runs into spaced.tsv (applied as \\emph by
draft.py --post).  Two controls per sheet: whole text-page lines (no spacing there; a reader who marks one is guessing).
    python3 ebook-method/kort-oversigt/lsheets.py      -> .render/kort-oversigt-l1-NN.png, .parts/reads/sheets-l1.tsv, controls-l1.tsv"""
import os, re, sys, random
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
BOOK = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt'); OUT = os.path.join(BOOK, '.render'); RD = os.path.join(BOOK, '.parts', 'reads')
try: font = ImageFont.truetype('DejaVuSans.ttf', 20)
except OSError: font = ImageFont.load_default()
Lr = re.compile(r'[A-Za-zÀ-ÖØ-öø-ÿ]')
def score(im, x, y, w, h, n):
    c = im.crop((x, y, x + w, y + h)); px = c.load()
    ink = [sum(1 for j in range(c.height) if px[i, j] < 150) for i in range(c.width)]
    runs, r0 = [], None
    for i, v in enumerate(ink + [1]):
        if v == 0 and r0 is None: r0 = i
        if v and r0 is not None: runs.append(i - r0); r0 = None
    return sum(runs[1:-1]) / max(1, n - 1) / h if len(runs) > 2 else 0
def words(p):
    out = []
    for r in open(os.path.join(BOOK, '.parts', 'collate', 'ocr', f'p{p}.tsv'), encoding='utf-8').read().splitlines()[1:]:
        r = r.split('\t')
        if len(r) == 12 and r[0] == '5' and r[11].strip(): out.append((r[11], tuple(map(int, r[6:10])), (r[2], r[3], r[4])))
    return out
items = []
for p in range(148, 158):
    im = Image.open(os.path.join(OUT, f'kort-oversigt-p{p}-300.png')).convert('L'); ws = words(p); lines = {}
    for w, (x, y, ww, hh), ln in ws:
        n = len(Lr.findall(w))
        if n < 3 or not re.fullmatch(r'\W*[A-Za-zÀ-ÖØ-öø-ÿ-]{3,}\W*', w): continue
        s = score(im, x, y, ww, hh, n)
        if (n >= 5 and s >= 0.095) or (n < 5 and s >= 0.12): lines.setdefault(ln, []).append((w, x, y, ww, hh))
    for ln, hits in lines.items():
        lw = [b for w, b, l2 in ws if l2 == ln]
        y0 = min(b[1] for b in lw); y1 = max(b[1] + b[3] for b in lw)
        items.append(('check', p, y0, y1, ' '.join(h[0] for h in hits)))
rng = random.Random(20261014); pool = []
for p in rng.sample(range(2, 147), 12):
    ws = words(p); lns = {}
    for w, b, ln in ws: lns.setdefault(ln, []).append(b)
    for ln in rng.sample(sorted(lns), min(2, len(lns))):
        bs = lns[ln]
        if len(bs) >= 6: pool.append(('control', p, min(b[1] for b in bs), max(b[1] + b[3] for b in bs), 'roman'))
PER = 10; groups = [items[k:k + PER] for k in range(0, len(items), PER)]; idx, ctl = [], []
for g_n, g in enumerate(groups, 1):
    g = list(g) + [pool.pop(), pool.pop()]; rng.shuffle(g); crops = []
    for pos, (kind, p, y0, y1, key) in enumerate(g, 1):
        im = Image.open(os.path.join(OUT, f'kort-oversigt-p{p}-300.png')).convert('RGB'); h = y1 - y0
        ox = int(im.width * 0.05); cr = im.crop((ox, max(0, y0 - int(0.5 * h)), im.width - ox, y1 + int(0.5 * h)))
        cid = f'l1-{g_n:02d}-{pos:02d}'
        lab = Image.new('RGB', (cr.width, 28), 'white'); ImageDraw.Draw(lab).text((4, 3), f'{cid}   p. {p}', fill=(0, 0, 0), font=font)
        b = Image.new('RGB', (cr.width, cr.height + 28), 'white'); b.paste(lab, (0, 0)); b.paste(cr, (0, 28)); crops.append(b)
        (ctl if kind == 'control' else idx).append(f'kort-oversigt-l1-{g_n:02d}.png\t{cid}\t{p}\t{key}')
    sh = Image.new('RGB', (max(x.width for x in crops), sum(x.height + 8 for x in crops)), (170, 170, 170)); y = 0
    for x in crops: sh.paste(x, (0, y)); y += x.height + 8
    sh.save(os.path.join(OUT, f'kort-oversigt-l1-{g_n:02d}.png'))
open(os.path.join(RD, 'sheets-l1.tsv'), 'w', encoding='utf-8').write('\n'.join(idx) + '\n')
open(os.path.join(RD, 'controls-l1.tsv'), 'w', encoding='utf-8').write('\n'.join(ctl) + '\n')
print(len(items), 'Noter lines +', len(ctl), 'controls on', len(groups), 'sheets')
