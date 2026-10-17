#!/usr/bin/env python3
"""spotsheets.py -- crop sheets for the odd spots found while translating Om Aandsdannelse (TRANSLATION-PLAYBOOK §6c).
Each crop is the printed lines round a phrase, found in tesseract's word boxes (.parts/collate/ocr/pN.tsv; the best
fuzzy match of the phrase against runs of consecutive words), boxed in red, labelled with an id and the page only.
    python3 ebook-method/kort-oversigt/spotsheets.py SPOTS.tsv TAG     (SPOTS.tsv: page <TAB> phrase [<TAB> note])
Pages are rendered at 300 dpi (as ocr.py did) into a temporary directory, never into the repo.
-> texts/nielsen/om-aandsdannelse/.render/om-aandsdannelse-<TAG>NN.png and .parts/reads/spots-<TAG>.tsv."""
import os, re, sys, difflib, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE); import pagemap as C
BOOK = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt'); OUT = os.path.join(BOOK, '.render')
spots = [l.rstrip('\n').split('\t') for l in open(sys.argv[1], encoding='utf-8') if l.strip() and not l.startswith('#')]
TAG = sys.argv[2]; TMP = tempfile.mkdtemp()
try: font = ImageFont.truetype('DejaVuSans.ttf', 22)
except OSError: font = ImageFont.load_default()
def key(s): return re.sub(r'[^\wæøåÆØÅ]', '', s.lower())
crops, idx = [], []
for k, s in enumerate(spots, 1):
    p, phrase = int(s[0]), s[1]; sid = f'{TAG.upper()}{k:03d}'; n = len(phrase.split())
    rows = [r.split('\t') for r in open(os.path.join(BOOK, '.parts', 'collate', 'ocr', f'p{p}.tsv'), encoding='utf-8').read().splitlines()[1:]]
    rows = [r for r in rows if len(r) == 12 and r[0] == '5' and r[11].strip()]
    best = max(range(len(rows) - n + 1), key=lambda i: difflib.SequenceMatcher(None, key(phrase), key(''.join(r[11] for r in rows[i:i + n]))).ratio())
    W = rows[best:best + n]
    x0 = min(int(r[6]) for r in W); y0 = min(int(r[7]) for r in W)
    x1 = max(int(r[6]) + int(r[8]) for r in W); y1 = max(int(r[7]) + int(r[9]) for r in W); hh = max(int(r[9]) for r in W)
    png = os.path.join(TMP, f'p{p}.png')
    if not os.path.exists(png):
        subprocess.run(['pdftoppm', '-r', '300', '-gray', '-png', '-singlefile', '-f', str(C.pdfpage(p)), '-l', str(C.pdfpage(p)), C.scan_path(), png[:-4]], check=True)
    im = Image.open(png).convert('RGB')
    xs = [int(r[6]) for r in rows]; xe = [int(r[6]) + int(r[8]) for r in rows]
    L, R = max(0, min(xs) - 30), min(im.width, max(xe) + 30)
    top, bot = max(0, y0 - int(2.0 * hh)), min(im.height, y1 + int(2.2 * hh))
    c = im.crop((L, top, R, bot)); ImageDraw.Draw(c).rectangle((x0 - L - 5, y0 - top - 5, x1 - L + 5, y1 - top + 5), outline=(220, 0, 0), width=3)
    c = c.resize((int(c.width * 0.62), int(c.height * 0.62)))
    lab = Image.new('RGB', (c.width, 30), 'white'); ImageDraw.Draw(lab).text((4, 3), f'{sid}   p. {p}', fill=(0, 0, 0), font=font)
    b = Image.new('RGB', (c.width, c.height + 30), 'white'); b.paste(lab, (0, 0)); b.paste(c, (0, 30)); crops.append(b)
    idx.append(f'{TAG}{(k - 1) // 10 + 1:02d}\t{sid}\t{p}\t{phrase}')
for g in range(0, len(crops), 10):
    G = crops[g:g + 10]; sh = Image.new('RGB', (max(x.width for x in G), sum(x.height + 8 for x in G)), (170, 170, 170)); y = 0
    for x in G: sh.paste(x, (0, y)); y += x.height + 8
    sh.save(os.path.join(OUT, f'om-aandsdannelse-{TAG}{g // 10 + 1:02d}.png'))
os.makedirs(os.path.join(BOOK, '.parts', 'reads'), exist_ok=True)
open(os.path.join(BOOK, '.parts', 'reads', f'spots-{TAG}.tsv'), 'w', encoding='utf-8').write('\n'.join(idx) + '\n')
print(len(crops), 'crops,', (len(crops) + 9) // 10, 'sheets')
