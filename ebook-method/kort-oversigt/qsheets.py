#!/usr/bin/env python3
"""ebook-method/kort-oversigt/qsheets.py -- BLIND crop sheets for the differences between the transcription and the e-book
(ebookdiff.py -> .parts/ebookdiff.tsv) that need the image: word divisions, letters, punctuation, section rules.
Classes settled without the image (listed in the report, never applied silently): the e-book's note references
("Rejse 9 )."), quote style only (the e-book's straight "), the e-book's o for an old-style 0 inside a number.
Each crop: the printed line(s) at the place, located in the scan's layer by the words before it, the place boxed in
red; labelled with an id and the page only.  Pages read whole in the page pass (PAGEPASS) are left out.
    python3 ebook-method/kort-oversigt/qsheets.py   -> .render/kort-oversigt-qNN.png + .parts/reads/qsheets.tsv (id, page, tex, ebook, kind)"""
import os, re, sys, html, subprocess
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE); import pagemap as C
BOOK = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt'); OUT = os.path.join(BOOK, '.render'); RD = os.path.join(BOOK, '.parts', 'reads')
PAGEPASS = set(int(x) for x in open(os.path.join(HERE, 'pagepass.txt')).read().split()) if os.path.exists(os.path.join(HERE, 'pagepass.txt')) else set()
R = [l.rstrip('\n').split('\t') for l in open(os.path.join(BOOK, '.parts', 'ebookdiff.tsv'), encoding='utf-8')]
def cls(t, e):
    if re.fullmatch(r'(\d{1,2} \)[.,]?\s?)+|[.,]?\s?(\d{1,2} \)[.,]?)', e.strip()) and t.strip() in ('', '.', ','): return 'noteref'
    if re.sub(r' \d{1,2} \)', '', ' ' + e).strip() == t.strip(): return 'noteref'
    if t == '' and re.fullmatch(r'_+', e): return 'rule'
    q = lambda x: re.sub('[“”"]', '"', x)
    if q(t) == q(e): return 'quotestyle'
    if re.sub(r'(?<=\d)o|o(?=\d)', '0', e) == t: return 'eb-o0'
    if re.sub(r'[\s\-]', '', t) == re.sub(r'[\s\-]', '', e): return 'space'
    return 'other'
nm = lambda w: re.sub(r'[^\wæøåÆØÅ]', '', w).lower()
LAY = {}
def layer(p):
    if p not in LAY:
        x = subprocess.run(['pdftotext', '-bbox', '-f', str(C.pdfpage(p)), '-l', str(C.pdfpage(p)), C.scan_path(), '-'], capture_output=True, text=True).stdout
        ph = float(re.search(r'height="([\d.]+)"', x).group(1))
        LAY[p] = ([(html.unescape(w[4]), tuple(map(float, w[:4]))) for w in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', x)], ph)
    return LAY[p]
def locate(p, ctx):
    ws, ph = layer(p)
    pre = [nm(w) for w in ctx.split('[')[0].split()][-3:]; tgt = [nm(w) for w in ctx.split('[')[1].split(']')[0].split()]
    post = [nm(w) for w in ctx.split(']', 1)[1].split()][:3]
    n = [nm(w) for w, b in ws]; best = None
    for i in range(len(n)):
        s = sum(1 for k, a in enumerate(reversed(pre)) if i - 1 - k >= 0 and n[i - 1 - k] == a)
        s += sum(1 for k, a in enumerate(tgt[:2]) if i + k < len(n) and (n[i + k] == a or (a and n[i + k][:3] == a[:3])))
        j = i + max(1, len(tgt))
        s += sum(1 for k, a in enumerate(post) if j + k < len(n) and n[j + k] == a)
        if best is None or s > best[0]: best = (s, i)
    if not best or best[0] < 2: return None
    i = best[1]; i2 = min(len(ws) - 1, i + max(0, len(tgt) - 1))
    b0, b1 = ws[max(0, min(i, len(ws) - 1))][1], ws[i2][1]
    return (min(b0[0], b1[0]), min(b0[1], b1[1]), max(b0[2], b1[2]), max(b0[3], b1[3])), ph, best[0]
try: font = ImageFont.truetype('DejaVuSans.ttf', 20)
except OSError: font = ImageFont.load_default()
crops = []; idx = []; skipped = {}; k = 0
for r in R:
    p, kind, t, e, ctx = int(r[0]), r[1], r[2], r[3], r[4]
    c = cls(t, e)
    if kind != 'body' or c in ('noteref', 'quotestyle', 'eb-o0') or p in PAGEPASS: skipped[c] = skipped.get(c, 0) + 1; continue
    loc = locate(p, ctx)
    k += 1; qid = f'Q{k:03d}'
    if not loc: idx.append(f'{qid}\t{p}\t{t}\t{e}\t{c}\tNOT LOCATED'); continue
    (x0, y0, x1, y1), ph, sc = loc
    im = Image.open(os.path.join(OUT, f'kort-oversigt-p{p}-300.png')).convert('RGB'); s = im.height / ph; lh = max(9, y1 - y0)
    m = 3.2 if c == 'rule' else 1.7
    top, bot = max(0, (y0 - m * lh) * s), min(im.height, (y1 + m * lh) * s)
    ox = int(im.width * 0.04)
    cr = im.crop((ox, int(top), im.width - ox, int(bot))).copy()
    if c == 'rule': ImageDraw.Draw(cr).rectangle((int(x0 * s) - ox - 3, int(y0 * s - top) - 3, int(x0 * s) - ox + 3, int(y1 * s - top) + 3), outline=(220, 0, 0), width=2)
    else: ImageDraw.Draw(cr).rectangle((int(x0 * s) - ox - 3, int(y0 * s - top) - 3, int(x1 * s) - ox + 3, int(y1 * s - top) + 3), outline=(220, 0, 0), width=2)
    lab = Image.new('RGB', (cr.width, 28), 'white'); ImageDraw.Draw(lab).text((4, 3), f'{qid}   p. {p}' + ('   (a section break? see the question)' if c == 'rule' else ''), fill=(0, 0, 0), font=font)
    b = Image.new('RGB', (cr.width, cr.height + 28), 'white'); b.paste(lab, (0, 0)); b.paste(cr, (0, 28))
    crops.append((qid, p, b)); idx.append(f'{qid}\t{p}\t{t}\t{e}\t{c}\t{ctx}')
# controls (controls.tsv: places on the pages read at the image on 23 Sep where the layer is wrong), one in every ~35
CTL = [l.rstrip('\n').split('\t') for l in open(os.path.join(HERE, 'controls.tsv'), encoding='utf-8') if l.strip() and not l.startswith('#')]
for n, c in enumerate(CTL):
    p = int(c[4]); x0, y0, x1, y1 = map(float, c[5].split(',')); ph = float(c[6])
    im = Image.open(os.path.join(OUT, f'kort-oversigt-p{p}-300.png')).convert('RGB'); s = im.height / ph; lh = max(9, y1 - y0)
    top, bot = max(0, (y0 - 1.7 * lh) * s), min(im.height, (y1 + 1.7 * lh) * s); ox = int(im.width * 0.04)
    cr = im.crop((ox, int(top), im.width - ox, int(bot))).copy()
    ImageDraw.Draw(cr).rectangle((int(x0 * s) - ox - 3, int(y0 * s - top) - 3, int(x1 * s) - ox + 3, int(y1 * s - top) + 3), outline=(220, 0, 0), width=2)
    lab = Image.new('RGB', (cr.width, 28), 'white'); ImageDraw.Draw(lab).text((4, 3), f'{c[0]}   p. {p}', fill=(0, 0, 0), font=font)
    b = Image.new('RGB', (cr.width, cr.height + 28), 'white'); b.paste(lab, (0, 0)); b.paste(cr, (0, 28))
    crops.insert(min(len(crops), 5 + n * 35), (c[0], p, b))
for g in range(0, len(crops), 10):
    gr = crops[g:g + 10]; sh = Image.new('RGB', (max(x.width for _, _, x in gr), sum(x.height + 8 for _, _, x in gr)), (170, 170, 170)); y = 0
    for _, _, x in gr: sh.paste(x, (0, y)); y += x.height + 8
    sh.save(os.path.join(OUT, f'kort-oversigt-q{g // 10 + 1:02d}.png'))
open(os.path.join(RD, 'qsheets.tsv'), 'w', encoding='utf-8').write('\n'.join(idx) + '\n')
print(len(crops), 'crops,', (len(crops) + 9) // 10, 'sheets; not located:', sum('NOT LOCATED' in l for l in idx), '; left out:', skipped)
