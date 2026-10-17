#!/usr/bin/env python3
"""b1.py (2026-10-17) -- round b1 of BLIND crop sheets for Religiøse Tanketyper: the open word checks, the e-book
differences the collation could not see, an AUDIT of rule and hand decisions, and lines where the e-book or NB's layer
suggests letterspacing.  Every crop is labelled with a neutral id and the page only; the reader is never shown a reading.
Two controls a sheet (a 7+-letter word the draft and tesseract agree on).  Seeded: a rerun gives the same sheets.
    python3 ebook-method/kort-oversigt/b1.py   -> .render/kort-oversigt-b1-NN.png, .parts/reads/b1-items.tsv
Item kinds: w = transcribe the boxed word(s) exactly; l = name every letterspaced or italic word in the whole line."""
import os, re, sys, random, unicodedata
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import pagemap as C
B = C.BOOKDIR; OUT = os.path.join(B, '.render'); RD = os.path.join(B, '.parts', 'reads'); os.makedirs(RD, exist_ok=True)
random.seed(17)
font = ImageFont.truetype('DejaVuSans.ttf', 20) if os.path.exists('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf') else ImageFont.load_default()
try: font = ImageFont.truetype('DejaVuSans.ttf', 20)
except OSError: pass
fold = lambda s: ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn').replace('ø', 'o').replace('æ', 'ae')
lets = lambda s: re.sub(r'[^a-z]', '', fold(s))
OCR = {}
def owords(p):                                      # tesseract words of page p: (text, (x0,y0,x1,y1) pt, line key)
    if p not in OCR:
        ws = []
        for l in open(os.path.join(B, '.parts', 'collate', 'ocr', f'p{p}.tsv'), encoding='utf-8'):
            r = l.rstrip('\n').split('\t')
            if len(r) >= 12 and r[0] == '5' and r[11].strip():
                x, y, w, h = (int(v) * 72 / 300 for v in r[6:10]); ws.append((r[11], (x, y, x + w, y + h), tuple(r[2:5])))
        OCR[p] = ws
    return OCR[p]
def find(p, tok, nth=0):
    t = lets(tok)[:12]
    if len(t) < 2: return None
    hits = [w for w in owords(p) if lets(w[0]).startswith(t[:max(2, min(len(t), 6))]) or (len(t) >= 4 and t in lets(w[0]))]
    return hits[nth][1] if len(hits) > nth else None
def linebox(p, box):
    ws = owords(p); k = min(ws, key=lambda w: abs((w[1][1] + w[1][3]) / 2 - (box[1] + box[3]) / 2))[2]
    ln = [w[1] for w in ws if w[2] == k]
    return (min(b[0] for b in ln), min(b[1] for b in ln), max(b[2] for b in ln), max(b[3] for b in ln))
items = []                                          # (kind, page, box, key, known)
dec = {l.split('\t')[0]: l.rstrip('\n').split('\t') for l in open(os.path.join(HERE, 'decisions.tsv'), encoding='utf-8') if '\t' in l and not l.startswith('#')}
chk = [l.rstrip('\n').split('\t') for l in open(os.path.join(B, '.parts', 'collate', 'checks.tsv'), encoding='utf-8') if l.startswith('C')]
SKIP_OPEN = re.compile(r'^(10|11|12|13|16|17)\||^(48|109|115|116|122|37)\|')   # dividers and headings -> structure; note marks -> notes pass
for f in chk:
    if f[1] in dec or SKIP_OPEN.search(f[1]): continue
    items.append(('w', int(f[4]), tuple(map(float, f[5].split(','))), 'open:' + f[1], ''))
for l in open(os.path.join(B, '.parts', 'collate', 'italics.tsv'), encoding='utf-8'):   # kort-oversigt: the open italics
    f = l.rstrip('\n').split('\t')
    if len(f) >= 5: items.append(('w', int(f[3]), tuple(map(float, f[4].split(','))), 'ital:' + f[1], ''))
# e-book differences the collation never saw (tex word, page): list in ebx below; box found on tesseract's words
EBX = [(1, 'halvfjerde'), (10, 'Bevægelsee'), (19, 'lagttagelse'), (19, 'yilde'), (24, 'hovere'), (37, 'lagttagne'), (40, 'Aår'),
       (52, 'Rousseav'), (53, 'hravde'), (53, 'lagttagelser'), (59, 'Erhabene'), (67, 'Mennesketilblivelsen'), (70, 'Eksistensens'),
       (74, 'Gmndsatze'), (76, 'reduit'), (77, 'Aarhundres'), (79, 'Hypetese'), (83, 'kvantitive'), (86, 'Ziirich'), (87, 'Bucher'),
       (89, 'Eniwickelung'), (89, 'Irrtiim'), (90, 'Kraftmaasses'), (90, 'Erfahrang'), (92, 'Arbeidshypotese'), (94, 'Livsvurdening'), (94, 'Bose')]
for p, t in EBX:
    b = find(p, t)
    if b: items.append(('w', p, b, 'ebx:' + t, ''))
    else: print('not found', p, t)
# audit: rule and hand decisions
allc = [l.rstrip('\n').split('\t') for l in open(os.path.join(B, '.parts', 'collate', 'checks-all.tsv'), encoding='utf-8')]
allc = [['A'] + f for f in allc if len(f) >= 5]             # same columns as checks.tsv from 1 on: key, ctx, post, page, box
aud = [f for f in allc if f[1] in dec and dec[f[1]][2].startswith(('rule:ebook', 'hand-3wit'))]
eb = [f for f in aud if dec[f[1]][2] == 'rule:ebook']; hd = [f for f in aud if dec[f[1]][2].startswith('hand')]
r2 = [f for f in allc if f[1] in dec and dec[f[1]][2].startswith('rule2')]
for f in random.sample(eb, 22) + random.sample(r2, 8):
    items.append(('w', int(f[4]), tuple(map(float, f[5].split(','))), 'audit:' + f[1] + '\t' + dec[f[1]][1], ''))
spd = [f for f in allc if f[1] in dec and dec[f[1]][2] == 'rule:ebook-sp']
for f in random.sample(spd, 3): items.append(('w', int(f[4]), tuple(map(float, f[5].split(','))), 'audit:' + f[1] + '\t' + dec[f[1]][1], ''))
# letterspacing: the e-book's italics in the text, NB's wide words
SPX = []
for p, t in SPX:
    b = find(p, t)
    if b: items.append(('l', p, linebox(p, b), 'space:' + t, ''))
    else: print('not found', p, t)
random.shuffle(items)
# controls: 7+-letter words, draft and tesseract agree (no check on the page near them)
def control():
    while True:
        p = random.choice([q for q in C.PAGES if q >= 9]); ws = [w for w in owords(p) if re.fullmatch(r'[a-zæøå]{8,}', w[0])]
        if ws: w = random.choice(ws); return ('w', p, w[1], 'control', w[0])
PER = 16; sheets = [items[i:i + PER] for i in range(0, len(items), PER)]
rows = []
for n, sh in enumerate(sheets, 1):
    sh = sh + [control(), control()]; random.shuffle(sh)
    crops = []
    for k, (kind, p, b, key, known) in enumerate(sh, 1):
        im = Image.open(os.path.join(OUT, f'kort-oversigt-p{p}-300.png')).convert('RGB'); s = im.height / 600.2 if abs(im.height - 2501) < 5 else im.height / C_H if False else 300 / 72
        lh = max(9, b[3] - b[1])
        if kind == 'l': x0, x1 = b[0] - 10, b[2] + 10
        else: cx = (b[0] + b[2]) / 2; x0, x1 = max(0, cx - 80), cx + 80
        y0, y1 = b[1] - 0.9 * lh, b[3] + 0.9 * lh
        cr = im.crop((int(x0 * s), int(y0 * s), int(x1 * s), int(y1 * s)))
        if kind == 'w': ImageDraw.Draw(cr).rectangle((int((b[0] - x0) * s) - 4, int((b[1] - y0) * s) - 4, int((b[2] - x0) * s) + 4, int((b[3] - y0) * s) + 4), outline=(220, 0, 0), width=2)
        cid = f'b1-{n:02d}-{k:02d}'; rows.append(f'{cid}\t{p}\t{kind}\t{key}\t{known}')
        crops.append((cid, p, kind, cr))
    W = 1540; y = 0; x = 0; colh = 0; place = []
    for cid, p, kind, cr in crops:
        if kind == 'l':
            if cr.width > W: cr = cr.resize((W, int(cr.height * W / cr.width)))
            if x: y += colh; x = 0; colh = 0
            place.append((0, y, cid, p, kind, cr)); y += cr.height + 30; continue
        if cr.width > 760: cr = cr.resize((760, int(cr.height * 760 / cr.width)))
        place.append((x, y, cid, p, kind, cr)); colh = max(colh, cr.height + 30)
        if x: y += colh; x = 0; colh = 0
        else: x = 775
    H = y + colh + 10; sheet = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(sheet)
    for x, y, cid, p, kind, cr in place:
        d.text((x + 4, y), f'{cid}  p.{p}' + ('  [LINE]' if kind == 'l' else ''), fill=(0, 0, 160), font=font); sheet.paste(cr, (x, y + 26))
    if H > 1560: sheet = sheet.resize((int(W * 1560 / H), 1560))   # Read downscales anything larger (begrebet-noiagtighed lesson 7)
    sheet.save(os.path.join(OUT, f'kort-oversigt-b1-{n:02d}.png'))
open(os.path.join(RD, 'b1-items.tsv'), 'w', encoding='utf-8').write('id\tpage\tkind\tkey\tknown\n' + '\n'.join(rows) + '\n')
print(len(items), 'items,', len(sheets), 'sheets')
