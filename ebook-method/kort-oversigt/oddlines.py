#!/usr/bin/env python3
"""oddlines.py (2026-10-17) -- crop the printed line behind given lines of transcription.tex, for reading in the
main session (sweeps: unknown words, quotes, translators' odd spots).  The line is found on its page from three of
its words on tesseract's lines (st1.py's at()); the crop keeps a sliver of the lines above and below.
    python3 ebook-method/kort-oversigt/oddlines.py TAG LINE [LINE ...]  -> .render/kort-oversigt-TAG-NN.png"""
import os, re, sys
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, 'st2.py'), encoding='utf-8').read().replace('__file__', repr(os.path.join(HERE, 'st2.py')))
exec(src[:src.index('Q2 = ')])
tag, nums = sys.argv[1], [int(a) for a in sys.argv[2:]]
T = open(os.path.join(B, 'transcription.tex'), encoding='utf-8').read().split('\n')
pg = {}; p = 0
for i, l in enumerate(T):
    m = re.search(r'\\opage\{(\d+)\}', l)
    if m: p = int(m.group(1))
    pg[i + 1] = p
plain = lambda l: re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?|[{}%]', ' ', l)
CR = []
for n in nums:
    w = [x for x in plain(T[n - 1]).split() if re.search(r'\w', x)]
    found = None
    for k in range(0, max(1, len(w) - 2)):
        try: found = at(pg[n], ' '.join(w[k:k + 3])); break
        except SystemExit: continue
    if not found: print('not found:', n, T[n - 1][:60]); continue
    im = img(pg[n]); y0, y1 = found
    CR.append((n, pg[n], im.crop((int(im.width * 0.04), y0 - 22, int(im.width * 0.96), y1 + 22))))
sheets = []; cur = []; h = 0
for c in CR:
    if h + c[2].height + 34 > 1500 and cur: sheets.append(cur); cur = []; h = 0
    cur.append(c); h += c[2].height + 34
if cur: sheets.append(cur)
for s, sh in enumerate(sheets, 1):
    W = max(c[2].width for c in sh); S = Image.new('L', (W, sum(c[2].height + 34 for c in sh)), 255); d = ImageDraw.Draw(S); y = 0
    for n, p, cr in sh: d.text((4, y + 4), f'line {n}  p.{p}', fill=0, font=font); S.paste(cr, (0, y + 30)); y += cr.height + 34
    S.save(os.path.join(OUT, f'kort-oversigt-{tag}-{s:02d}.png'))
print(len(CR), 'crops,', len(sheets), 'sheets')
