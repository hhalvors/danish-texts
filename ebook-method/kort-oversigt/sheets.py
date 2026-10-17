#!/usr/bin/env python3
"""(copied 2026-10-12 from ebook-method/udvalgte-stykker/) ebook-method/kort-oversigt/sheets.py (copied 2026-10-11 from om-aandsdannelse; controls added) -- BLIND crop sheets.
Each crop is the printed line(s) around one spot, a word boxed in red, labelled with a NEUTRAL id (sheet-position) and
the page only: the reader is never shown the two OCR readings (check.py --sheets prints them, which invites picking one).

    python3 ebook-method/kort-oversigt/sheets.py words  [--tag b1] [--per 10]   open word checks (check.py's checks.tsv)
    python3 ebook-method/kort-oversigt/sheets.py italic [--tag i1] [--per 12]   open italics (check.py --italics: italics.tsv)
    ... --pages 45-98   (round 1) controls drawn from these pages only (the open items are those of checks.tsv anyway);
                        italic controls stay roman lines of the Indledning, pp. 1-3

-> texts/hoeffding/kort-oversigt/.render/kort-oversigt-<tag>-NN.png  (the sheets)
   texts/hoeffding/kort-oversigt/.parts/reads/sheets-<tag>.tsv    sheet <TAB> crop id <TAB> page <TAB> check key  (for reads.py)
   texts/hoeffding/kort-oversigt/.parts/reads/controls-<tag>.tsv  sheet <TAB> crop id <TAB> page <TAB> known reading
CONTROLS (house rule: two planted controls per reader, here two per sheet): crops of spots whose reading is KNOWN --
for 'words', a word of 7+ letters on which the draft and tesseract agree exactly (a reader who reads it differently has
misread); for 'italic', a line of Høffding's introduction or Indledning (certainly roman: a reader who marks italics
there is guessing).  They look like every other crop; reads.py scores them.  Seeded, so a rerun gives the same sheets.
Needs the 300-dpi page renders ocr.py made (.render/kort-oversigt-pN-300.png) and tesseract's boxes."""
import os, re, sys, random
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE); import pagemap as C
BOOK = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt'); OUT = os.path.join(BOOK, '.render')
RD = os.path.join(BOOK, '.parts', 'reads'); os.makedirs(RD, exist_ok=True)
KIND = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('-') else 'words'
opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
TAG = opt('--tag', 'b1' if KIND == 'words' else 'i1'); PER = int(opt('--per', 10 if KIND == 'words' else 12))
_pg = opt('--pages', None); SEL = set(range(int(_pg.split('-')[0]), int(_pg.split('-')[1]) + 1)) if _pg else set(C.PAGES)
try: font = ImageFont.truetype('DejaVuSans.ttf', 20)
except OSError: font = ImageFont.load_default()
imgs = {}
def page(p):
    if p not in imgs: imgs.clear(); imgs[p] = Image.open(os.path.join(OUT, f'kort-oversigt-p{p}-300.png')).convert('RGB')
    return imgs[p]
def crop(lab, p, bb, ph, lines_=1.6):
    im = page(p); sc = im.height / ph; x0, y0, x1, y1 = bb; lh = max(9, y1 - y0)
    top, bot = max(0, (y0 - lines_ * lh) * sc), min(im.height, (y1 + lines_ * lh) * sc)
    ox = int(im.width * 0.06)
    cr = im.crop((ox, int(top), im.width - ox, int(bot))).copy()
    ImageDraw.Draw(cr).rectangle((int(x0 * sc) - ox - 3, int(y0 * sc - top) - 3, int(x1 * sc) - ox + 3, int(y1 * sc - top) + 3), outline=(220, 0, 0), width=2)
    head = Image.new('RGB', (cr.width, 28), 'white'); ImageDraw.Draw(head).text((4, 3), lab, fill=(0, 0, 0), font=font)
    b = Image.new('RGB', (cr.width, cr.height + 28), 'white'); b.paste(head, (0, 0)); b.paste(cr, (0, 28))
    return b.resize((b.width * 2 // 3, b.height * 2 // 3), Image.LANCZOS)   # 300 -> 200 dpi equivalent
def ocrwords(p):                                   # tesseract's words with boxes in PDF points
    f = os.path.join(BOOK, '.parts', 'collate', 'ocr', f'p{p}.tsv'); out = []
    ph = page(p).height * 72 / 300; s = 72 / 300
    for r in open(f, encoding='utf-8').read().splitlines()[1:]:
        r = r.split('\t')
        if len(r) == 12 and r[0] == '5' and r[11].strip():
            x, y, w, h = map(int, r[6:10]); out.append((r[11], (x * s, y * s, (x + w) * s, (y + h) * s), float(r[10])))
    return out, ph
items = []
if KIND == 'words':
    for r in open(os.path.join(BOOK, '.parts', 'collate', 'checks.tsv'), encoding='utf-8'):
        r = r.rstrip('\n').split('\t')
        items.append(('check', r[1], int(r[4]), tuple(map(float, r[5].split(','))), float(r[6])))
else:
    for r in open(os.path.join(BOOK, '.parts', 'collate', 'italics.tsv'), encoding='utf-8'):
        r = r.rstrip('\n').split('\t')
        items.append(('check', r[1], int(r[3]), tuple(map(float, r[4].split(','))), float(r[5])))
if _pg: items = [it for it in items if it[2] in SEL]   # round 4: --pages also limits the checks (i5: the Anmærkninger's italics are read whole on the m5 anm strips)
# round 2 (2026-10-11): --extra FILE (in this folder): spots with NO check (layer and tesseract agree) that a third
# witness disputes -- key <TAB> page <TAB> word to box <TAB> word before it; the box is tesseract's word (letters equal,
# case ignored) whose predecessor matches.  Keys start with X: reads.py lists them for the main session, never decides.
if KIND == 'words' and '--extra' in sys.argv:
    _lt = lambda s: re.sub(r'[^A-Za-zÀ-ÖØ-öø-ÿ0-9]', '', s).lower()
    for r in open(os.path.join(HERE, opt('--extra', '')), encoding='utf-8'):
        if r.startswith('#') or not r.strip(): continue
        key, p, w, prev = r.rstrip('\n').split('\t'); p = int(p); ws, ph = ocrwords(p)
        hits = [ws[k] for k in range(len(ws)) if _lt(ws[k][0]) == _lt(w) and (not prev or (k and _lt(ws[k - 1][0]) == _lt(prev)))]
        if len(hits) != 1:                         # moderne-filosoffer: the word alone, if unique on its page; else skip, listed
            h2 = [x for x in ws if _lt(x[0]) == _lt(w)]
            if len(h2) == 1: hits = h2
            else:                                  # the nearest word by letters (and the word before it), if clearly best
                import difflib
                R = lambda a, b: difflib.SequenceMatcher(None, a, b).ratio()
                sc = sorted(((R(_lt(w), _lt(ws[k][0])) + (0.5 * R(_lt(prev), _lt(ws[k - 1][0])) if prev and k else 0), k) for k in range(len(ws))), reverse=True)
                if sc and sc[0][0] >= (0.95 if prev else 0.65) and (len(sc) == 1 or sc[0][0] - sc[1][0] > 0.15): hits = [ws[sc[0][1]]]
                else: print(f'--extra: SKIPPED {key}: {len(hits)}/{len(h2)} boxes for {w!r} after {prev!r} on p. {p}'); continue
        items.append(('check', key, p, hits[0][1], ph))
if '--mix' in sys.argv: random.Random(20261014).shuffle(items)   # oplevelse: spread pages (and the audit spots) over the sheets
# controls: the draft's text (the file check.py collated), so a control word is one both readings share
TEX = open(os.path.join(BOOK, C.TEXFILE), encoding='utf-8').read()
TEXT = re.sub(r'\\[a-zA-Z]+|[{}%]', ' ', TEX[TEX.index('\\mainmatter'):])
rng = random.Random(20261011 + (0 if KIND == 'words' else 1)); pool = []
intro_pages = [p for p in C.PAGES if p not in getattr(C, 'NO_INTRO', ()) or p < 4]
for p in sorted(set(C.PAGES) & (SEL | ({8, 12} if KIND != 'words' else set()))):
    ws, ph = ocrwords(p)
    for w, b, conf in ws:
        if KIND == 'words':
            if conf >= 90 and re.fullmatch(r'[A-Za-zÆØÅæøå]{7,}', w) and not w.isupper() and (TAG in ('b1',) or 0.09 * ph < b[1] < 0.92 * ph) and len(re.findall(r'(?<![A-Za-zÆØÅæøå])' + re.escape(w) + r'(?![A-Za-zÆØÅæøå])', TEXT)) == 1:
                pool.append(('control', w, p, b, ph))
        elif p in (8, 12) and conf >= 90 and re.fullmatch(r'[a-zæøå]{6,}', w):
            pool.append(('control', 'roman line: ' + w, p, b, ph))
rng.shuffle(pool)
groups = [items[k:k + PER] for k in range(0, len(items), PER)]
idx, ctl = [], []
for g_n, g in enumerate(groups, 1):
    g = list(g) + [pool.pop(), pool.pop()]          # two controls per sheet
    rng.shuffle(g)
    crops = []
    for pos, (kind, key, p, bb, ph) in enumerate(g, 1):
        cid = f'{TAG}-{g_n:02d}-{pos:02d}'
        crops.append(crop(f'{cid}   p. {p}', p, bb, ph))
        (ctl if kind == 'control' else idx).append(f'kort-oversigt-{TAG}-{g_n:02d}.png\t{cid}\t{p}\t{key}')
    sh = Image.new('RGB', (max(x.width for x in crops), sum(x.height + 8 for x in crops)), (170, 170, 170)); y = 0
    for x in crops: sh.paste(x, (0, y)); y += x.height + 8
    sh.save(os.path.join(OUT, f'kort-oversigt-{TAG}-{g_n:02d}.png'))
open(os.path.join(RD, f'sheets-{TAG}.tsv'), 'w', encoding='utf-8').write('\n'.join(idx) + '\n')
open(os.path.join(RD, f'controls-{TAG}.tsv'), 'w', encoding='utf-8').write('\n'.join(ctl) + '\n')
print(f'{KIND}: {len(items)} crops + {len(ctl)} controls on {len(groups)} sheets -> .render/kort-oversigt-{TAG}-NN.png')
