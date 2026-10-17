#!/usr/bin/env python3
"""notesheets.py (2026-10-14) -- BLIND strips of every page's footnotes, to be read whole (CLAUDE.md: both OCRs share the
faults of the small type) and for their letterspacing (authors' names, <sp>) and italics (titles, *..*), which no OCR
and not the e-book records.  One strip per page with notes: from the notes' top (notetops.tsv, nb_scan.py notes) to the
last ALTO line of the page, from the 200-dpi render ocr.py made; labelled with a neutral id and the page.  Two CONTROL
strips a sheet: a body line whose words the draft and tesseract read alike (scored by notereads.py).
    python3 ebook-method/kort-oversigt/notesheets.py [--tag n1] [--per 10]
-> .render/kort-oversigt-<tag>-NN.png, .parts/reads/sheets-<tag>.tsv (sheet, id, page, 'notes'),
   controls-<tag>.tsv (sheet, id, page, known line)"""
import os, re, sys, random
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pagemap as C, alto
OUT = os.path.join(C.BOOKDIR, '.render'); RD = os.path.join(C.BOOKDIR, '.parts', 'reads'); os.makedirs(RD, exist_ok=True)
opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
TAG = opt('--tag', 'n1'); PER = int(opt('--per', 10))
try: font = ImageFont.truetype('DejaVuSans.ttf', 20)
except OSError: font = ImageFont.load_default()
DPI = 300; K = DPI / 254                              # ALTO mm10 -> px at 300 dpi (small type: 200 dpi is too coarse)
tops = {}
for l in open(os.path.join(HERE, 'notetops.tsv'), encoding='utf-8'):
    if l[:1].isdigit(): f = l.split('\t'); tops[int(f[0]) - C.OFFSET] = float(f[1])
def strip(lab, p, y0, y1, pad=10):
    im = Image.open(os.path.join(OUT, f'kort-oversigt-p{p}-{DPI}.png')).convert('RGB')
    ox = int(im.width * 0.05)
    cr = im.crop((ox, max(0, int(y0) - pad), im.width - ox, min(im.height, int(y1) + pad)))
    head = Image.new('RGB', (cr.width, 28), 'white'); ImageDraw.Draw(head).text((4, 3), lab, fill=(0, 0, 0), font=font)
    b = Image.new('RGB', (cr.width, cr.height + 28), 'white'); b.paste(head, (0, 0)); b.paste(cr, (0, 28)); return b
items = []
for p in sorted(tops):
    if p not in C.PAGES: continue
    L, _ = alto.alto_lines(C.pdfpage(p))
    bot = max(max(w[2] + w[4] for w in ws) for ws, h in L) * K
    items.append(('notes', p, tops[p] * DPI / 72 - 8, bot + 6))
rng = random.Random(20261014)
pool = []
for p in rng.sample([q for q in C.PAGES if q > 9], 60):
    L, _ = alto.alto_lines(C.pdfpage(p))
    for ws, h in L[3:12]:
        t = ' '.join(w[0] for w in ws)
        if len(t) > 35 and re.fullmatch(r"[A-Za-zÆØÅæøå ,.;]+", t):
            pool.append(('control', p, min(w[2] for w in ws) * K - 4, max(w[2] + w[4] for w in ws) * K + 4, t)); break
rng.shuffle(pool)
# a control strip after every 6th note strip; sheets packed to at most MAXH px (the image reader scales larger ones down)
seq = []
for k, it in enumerate(items):
    seq.append(it)
    if k % 6 == 5 and pool: seq.append(pool.pop())
MAXH = int(opt('--maxh', 1550)); idx, ctl = [], []; g_n = 0; cur = []
def flush():
    global g_n, cur
    if not cur: return
    g_n += 1; crops = []
    for pos, it in enumerate(cur, 1):
        cid = f'{TAG}-{g_n:02d}-{pos:02d}'; crops.append(strip(f'{cid}   p. {it[1]}', it[1], it[2], it[3]))
        if it[0] == 'control': ctl.append(f'kort-oversigt-{TAG}-{g_n:02d}.png\t{cid}\t{it[1]}\t{it[4]}')
        else: idx.append(f'kort-oversigt-{TAG}-{g_n:02d}.png\t{cid}\t{it[1]}\tnotes')
    sh = Image.new('RGB', (max(x.width for x in crops), sum(x.height + 8 for x in crops)), (170, 170, 170)); y = 0
    for x in crops: sh.paste(x, (0, y)); y += x.height + 8
    sh.save(os.path.join(OUT, f'kort-oversigt-{TAG}-{g_n:02d}.png')); cur = []
h = 0
for it in seq:
    hh = it[3] - it[2] + 50
    if cur and h + hh > MAXH: flush(); h = 0
    cur.append(it); h += hh
flush(); groups = range(g_n)
open(os.path.join(RD, f'sheets-{TAG}.tsv'), 'w', encoding='utf-8').write('\n'.join(idx) + '\n')
open(os.path.join(RD, f'controls-{TAG}.tsv'), 'w', encoding='utf-8').write('\n'.join(ctl) + '\n')
print(f'{len(items)} note strips + {len(ctl)} controls on {len(groups)} sheets -> .render/kort-oversigt-{TAG}-NN.png')
