#!/usr/bin/env python3
"""ebook-method/kort-oversigt/frontsheets.py -- whole-page strips of the FRONT MATTER for a blind page reader
(2026-10-14): title page (PDF 9), its verso (PDF 10), the Indhold (pp. V-VI, PDF 11-12) and the Indledning (pp. VII-X,
PDF 13-16), which collate/check.py does not collate (it reads arabic pages only).  Two strips a page, two strips a sheet.
    python3 ebook-method/kort-oversigt/frontsheets.py   -> .render/kort-oversigt-fm-NN.png"""
import os, sys, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE)); sys.path.insert(0, HERE)
import pagemap as C
OUT = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt', '.render')
PAGES = [(9, 'title page'), (10, 'title verso'), (11, 'p. V (Indhold)'), (12, 'p. VI (Indhold)'), (13, 'p. VII'), (14, 'p. VIII'), (15, 'p. IX'), (16, 'p. X')]
try: font = ImageFont.truetype('DejaVuSans.ttf', 22)
except OSError: font = ImageFont.load_default()
T = tempfile.mkdtemp(); strips = []
for pdf, lab in PAGES:
    b = os.path.join(T, f'p{pdf}')
    subprocess.run(['pdftoppm', '-r', '200', '-gray', '-png', '-singlefile', '-f', str(pdf), '-l', str(pdf), C.scan_path(), b], check=True)
    im = Image.open(b + '.png').convert('RGB'); W, H = im.size; x0, x1 = int(W * 0.05), int(W * 0.95)
    for k, (a, z) in enumerate(((0.03, 0.52), (0.50, 0.97)), 1):
        c = im.crop((x0, int(H * a), x1, int(H * z))); l = Image.new('RGB', (c.width, 30), 'white')
        ImageDraw.Draw(l).text((4, 3), f'PDF {pdf} = {lab}   strip {k} of 2', fill=(0, 0, 0), font=font)
        s = Image.new('RGB', (c.width, c.height + 34), 'white'); s.paste(l, (0, 0)); s.paste(c, (0, 32)); strips.append(s)
for i in range(0, len(strips), 2):
    part = strips[i:i + 2]; sh = Image.new('RGB', (max(s.width for s in part), sum(s.height + 12 for s in part)), 'white'); y = 0
    for s in part: sh.paste(s, (0, y)); y += s.height + 12
    sh.save(os.path.join(OUT, f'kort-oversigt-fm-{i // 2 + 1:02d}.png'))
print(len(strips), 'strips on', (len(strips) + 1) // 2, 'sheets')
