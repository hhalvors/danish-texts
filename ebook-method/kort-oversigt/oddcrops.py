#!/usr/bin/env python3
"""oddcrops.py (2026-10-17) -- the translators' odd spots as LINE crops from the 400-dpi page images (the line holding a
phrase, found on tesseract's lines, plus the line above and below), 12 to a sheet, read in the main session.
    python3 ebook-method/kort-oversigt/oddcrops.py SPOTS.tsv TAG   (SPOTS: page<TAB>phrase)  -> .render/kort-oversigt-TAG-NN.png"""
import os, re, sys, unicodedata
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import pagemap as C
B = C.BOOKDIR; OUT = os.path.join(B, '.render')
try: font = ImageFont.truetype('DejaVuSans.ttf', 22)
except OSError: font = ImageFont.load_default()
fold = lambda s: re.sub(r'[^a-z]', '', ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn').replace('ø', 'o').replace('æ', 'ae'))
def lines(p):
    L = {}
    for l in open(os.path.join(B, '.parts', 'collate', 'ocr', f'p{p}.tsv'), encoding='utf-8'):
        r = l.rstrip('\n').split('\t')
        if len(r) >= 12 and r[0] == '5' and r[11].strip():
            x, y, w, h = map(int, r[6:10]); L.setdefault(tuple(r[2:5]), []).append((r[11], y, y + h))
    return sorted(([' '.join(w[0] for w in ws), min(w[1] for w in ws), max(w[2] for w in ws)] for ws in L.values()), key=lambda t: t[1])
spots = [l.rstrip('\n').split('\t') for l in open(sys.argv[1], encoding='utf-8') if l.strip() and not l.startswith('#')]
TAG = sys.argv[2]; crops = []
for k, (pg, ph) in enumerate(spots, 1):
    p = int(pg); ls = lines(p); f = fold(ph)
    hit = None
    for i in range(len(ls)):
        for j in (i + 1, i + 2):
            if f[:12] and f[:12] in fold(' '.join(t for t, a, b in ls[i:j])): hit = (i, j - 1); break
        if hit: break
    if not hit: print('not found', p, ph); continue
    y0 = ls[max(0, hit[0] - 1)][1] - 10; y1 = ls[min(len(ls) - 1, hit[1] + 1)][2] + 10
    im = Image.open(os.path.join(C.IMGDIR, f'{C.pdfpage(p):04d}.jpg')).convert('L'); s = 400 / 300
    cr = im.crop((int(im.width * 0.05), int(y0 * s), int(im.width * 0.95), int(y1 * s)))
    cr = cr.resize((1500, int(cr.height * 1500 / cr.width))); crops.append((k, p, ph, cr))
n = 0
for i in range(0, len(crops), 8):
    part = crops[i:i + 8]; H = sum(c.height + 34 for *_, c in part); S = Image.new('L', (1500, H), 255); d = ImageDraw.Draw(S); y = 0
    for k, p, ph, cr in part:
        d.text((4, y + 4), f'{TAG}-{k:02d}  p.{p}  [{ph}]', fill=0, font=font); S.paste(cr, (0, y + 30)); y += cr.height + 34
    n += 1; S.save(os.path.join(OUT, f'kort-oversigt-{TAG}-{n:02d}.png'))
print(len(crops), 'crops,', n, 'sheets')
