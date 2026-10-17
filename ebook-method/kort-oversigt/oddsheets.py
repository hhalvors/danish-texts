#!/usr/bin/env python3
"""ebook-method/kort-oversigt/oddsheets.py -- BLIND crop sheets for the translators' odd spots (.parts/tr/odd-*.tsv:
page, the Danish words, the doubt): TRANSLATION-PLAYBOOK §6c, the translation as a second reading.  Each spot is
located in the scan's layer by its words (on its page, or the next, for a spot that runs over), the line(s) cropped
and boxed in red, labelled with an id and the page only (the doubt is not shown: the reader transcribes).
    python3 ebook-method/kort-oversigt/oddsheets.py    -> .render/kort-oversigt-oNN.png + .parts/reads/osheets.tsv"""
import os, re, sys, glob, html, subprocess
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE); import pagemap as C
BOOK = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt'); OUT = os.path.join(BOOK, '.render'); RD = os.path.join(BOOK, '.parts', 'reads')
nm = lambda w: re.sub(r'[^\wæøåÆØÅäöüé]', '', w).lower()
LAY = {}
def layer(p):
    if p not in LAY:
        x = subprocess.run(['pdftotext', '-bbox', '-f', str(C.pdfpage(p)), '-l', str(C.pdfpage(p)), C.scan_path(), '-'], capture_output=True, text=True).stdout
        ph = float(re.search(r'height="([\d.]+)"', x).group(1))
        LAY[p] = ([(html.unescape(w[4]), tuple(map(float, w[:4]))) for w in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', x)], ph)
    return LAY[p]
def locate(p, words):
    tw = [nm(w) for w in re.sub(r'\\[a-zA-Z]+|[{}]|\\\\', ' ', words).split() if nm(w)]
    best = None
    for q in (p, p + 1, p - 1):
        if not C.FIRST_PRINTED <= q <= C.LAST_PRINTED: continue
        ws, ph = layer(q); n = [nm(w) for w, b in ws]
        for i in range(len(n)):
            s = sum(1 for k, a in enumerate(tw) if i + k < len(n) and (n[i + k] == a or (len(a) > 3 and n[i + k][:3] == a[:3])))
            if best is None or s > best[0]: best = (s, q, i, len(tw), ph)
    if not best or best[0] < max(1, min(2, len(tw))): return None
    s, q, i, k, ph = best; ws, _ = layer(q); seg = ws[i:i + max(1, k)]
    return q, (min(b[0] for w, b in seg), min(b[1] for w, b in seg), max(b[2] for w, b in seg), max(b[3] for w, b in seg)), ph
try: font = ImageFont.truetype('DejaVuSans.ttf', 20)
except OSError: font = ImageFont.load_default()
rows = []
for f in sorted(glob.glob(os.path.join(BOOK, '.parts', 'tr', 'odd-*.tsv'))):
    for l in open(f, encoding='utf-8'):
        x = l.rstrip('\n').split('\t')
        if len(x) >= 3 and re.match(r'\d+', x[0]): rows.append((int(re.match(r'\d+', x[0]).group(0)), x[1], x[2], os.path.basename(f)))
crops, idx = [], []
for k, (p, words, doubt, src) in enumerate(rows, 1):
    oid = f'O{k:03d}'
    loc = locate(p, words)
    if not loc: idx.append(f'{oid}\t{p}\t{words}\t{doubt}\tNOT LOCATED'); continue
    q, (x0, y0, x1, y1), ph = loc
    fn = os.path.join(OUT, f'kort-oversigt-p{q}-300.png')
    if not os.path.exists(fn):
        subprocess.run(['pdftoppm', '-r', '300', '-gray', '-png', '-singlefile', '-f', str(C.pdfpage(q)), '-l', str(C.pdfpage(q)), C.scan_path(), fn[:-4]], check=True)
    im = Image.open(fn).convert('RGB'); s = im.height / ph; lh = 10
    top, bot = max(0, (y0 - 2.2 * lh) * s), min(im.height, (y1 + 2.2 * lh) * s); ox = int(im.width * 0.04)
    cr = im.crop((ox, int(top), im.width - ox, int(bot))).copy()
    ImageDraw.Draw(cr).rectangle((int(x0 * s) - ox - 3, int(y0 * s - top) - 3, int(x1 * s) - ox + 3, int(y1 * s - top) + 3), outline=(220, 0, 0), width=2)
    lab = Image.new('RGB', (cr.width, 28), 'white'); ImageDraw.Draw(lab).text((4, 3), f'{oid}   p. {q}', fill=(0, 0, 0), font=font)
    b = Image.new('RGB', (cr.width, cr.height + 28), 'white'); b.paste(lab, (0, 0)); b.paste(cr, (0, 28))
    crops.append((oid, q, b)); idx.append(f'{oid}\t{q}\t{words}\t{doubt}\t{src}')
for g in range(0, len(crops), 8):
    gr = crops[g:g + 8]; sh = Image.new('RGB', (max(x.width for _, _, x in gr), sum(x.height + 8 for _, _, x in gr)), (170, 170, 170)); y = 0
    for _, _, x in gr: sh.paste(x, (0, y)); y += x.height + 8
    sh.save(os.path.join(OUT, f'kort-oversigt-o{g // 8 + 1:02d}.png'))
open(os.path.join(RD, 'osheets.tsv'), 'w', encoding='utf-8').write('\n'.join(idx) + '\n')
print(len(crops), 'crops,', (len(crops) + 7) // 8, 'sheets; not located:', sum('NOT LOCATED' in l for l in idx))
