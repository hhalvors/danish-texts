#!/usr/bin/env python3
"""st2.py (2026-10-17) -- second STRUCTURE sheet (heads found below the running head; zooms), from st1.py.  STRUCTURE and NOTES sheets for a blind reader: front and back matter, chapter and section
heads, the run-in small-capital name openings, doubtful paragraph starts, misprint zooms, and the one footnote.
Regions are found from phrases on tesseract's lines; each crop is labelled `s1-NN-KK p.N` with its question.
    python3 ebook-method/kort-oversigt/st1.py  -> .render/kort-oversigt-s2-NN.png, .parts/reads/s1-items.tsv"""
import os, re, sys, unicodedata
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import pagemap as C
B = C.BOOKDIR; OUT = os.path.join(B, '.render'); RD = os.path.join(B, '.parts', 'reads')
try: font = ImageFont.truetype('DejaVuSans.ttf', 20)
except OSError: font = ImageFont.load_default()
fold = lambda s: re.sub(r'[^a-z]', '', ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn').replace('ø', 'o').replace('æ', 'ae'))
def lines(p):
    L = {}
    for l in open(os.path.join(B, '.parts', 'collate', 'ocr', f'p{p}.tsv'), encoding='utf-8'):
        r = l.rstrip('\n').split('\t')
        if len(r) >= 12 and r[0] == '5' and r[11].strip():
            x, y, w, h = map(int, r[6:10]); L.setdefault(tuple(r[2:5]), []).append((r[11], x, y, x + w, y + h))
    return sorted(([' '.join(w[0] for w in ws), min(w[2] for w in ws), max(w[4] for w in ws)] for ws in L.values()), key=lambda t: t[1])
def at(p, phrase, ymin=0):                                    # (y0, y1) px at 300 dpi of the line holding phrase
    ls = [t for t in lines(p) if t[1] >= ymin]; f = fold(phrase)
    for t, y0, y1 in ls:
        if f[:14] in fold(t): return y0, y1
    for i in range(len(ls) - 1):
        if f[:14] in fold(ls[i][0] + ls[i + 1][0]): return ls[i][1], ls[i + 1][2]
    sys.exit(f'not found: p. {p} {phrase!r}')
def img(p, dpi=300):
    if C.FIRST_PRINTED <= p <= C.LAST_PRINTED: return Image.open(os.path.join(OUT, f'kort-oversigt-p{p}-300.png')).convert('L')
    im = Image.open(os.path.join(C.IMGDIR, f'{p + C.OFFSET:04d}.jpg')).convert('L'); return im.resize((im.width * 300 // 400, im.height * 300 // 400))
IT = []
Q2 = 'Transcribe the heading line(s) exactly (line breaks as /) and say how set (centred; capitals, small capitals, bold, italic; larger type). Say exactly what stands ABOVE the heading: a short centred rule (closing the previous chapter), blank space, or nothing.'
for p, ph in [(17, 'SYSTEMDANNELSER'), (35, 'ERFARINGSFILOSOFIEN'), (43, 'OPLYSNINGSFILOSOFIEN'), (74, 'POSITIVISMEN'),
              (81, 'Problembehandlinger'), (91, 'Aarsagssætningens Historie'), (85, 'Tilværelsesproblemet'), (53, 'Erkendelsesteori')]:
    y0, y1 = at(p, ph, 250); IT.append((p, y0 - 330, y1 + 130, 0.9, Q2))
y0, y1 = at(84, 'fører naturligt til at betone')
IT.append((84, y0 - 120, y1 + 10, 0.9, 'Does the LAST line of this crop begin a new paragraph (indented, or the line above it short)? Answer: new paragraph / same paragraph.'))
for p, ph in [(10, 'Bevægelsee'), (67, 'om Mennesketilblivelsen'), (67, 'Enhed af Modsætninger'), (94, 'Livsvurdening')]:
    y0, y1 = at(p, ph); IT.append((p, y0 - 25, y1 + 25, 1.7, 'ZOOM: transcribe the line letter by letter exactly as printed (do not correct). Spell out, letter by letter, the long compound word in it.'))
IT.append((95, None, None, 0.45, 'Last text page: is anything printed below the last line of the text (a short rule, "Slut", nothing)?'))
rows = []; sheets = []; cur = []; hcur = 0
CR = []
for k, (p, y0, y1, sc, q) in enumerate(IT):
    im = img(p)
    if y0 is None: cr = im
    else: cr = im.crop((int(im.width * 0.04), max(0, y0), int(im.width * 0.96), min(im.height, y1 if y1 else im.height - 60)))
    cr = cr.resize((int(cr.width * sc), int(cr.height * sc)))
    wide = q.startswith('ZOOM') or q.startswith('FOOTNOTE') or 'middle line' in q or q.startswith('Transcribe the line that begins')   # small type: a whole row, ~300 dpi
    if wide: cr = cr.resize((1540, int(cr.height * 1540 / cr.width)))
    elif cr.width > 760: cr = cr.resize((760, int(cr.height * 760 / cr.width)))   # two columns of 760 px
    CR.append((p, q, cr, wide))
ROWS = []
for c in CR:                                         # two narrow crops side by side; a wide one alone
    if c[3] or not ROWS or len(ROWS[-1]) == 2 or ROWS[-1][0][3]: ROWS.append([c])
    else: ROWS[-1].append(c)
ROWS = [[(p, q, cr) for p, q, cr, w in r] for r in ROWS]
for r in ROWS:
    h = max(c.height for p, q, c in r) + 40
    if hcur + h > 1560 and cur: sheets.append(cur); cur = []; hcur = 0
    cur.append(r); hcur += h
if cur: sheets.append(cur)
for n, sh in enumerate(sheets, 1):
    H = sum(max(c.height for p, q, c in r) + 40 for r in sh); S = Image.new('L', (1540, H), 255); d = ImageDraw.Draw(S); y = 0; k = 0
    for r in sh:
        for j, (p, q, cr) in enumerate(r):
            k += 1; cid = f's2-{n:02d}-{k:02d}'; d.text((j * 780 + 4, y + 4), f'{cid}  p.{p}', fill=0, font=font); S.paste(cr, (j * 780, y + 30))
            rows.append(f'{cid}\t{p}\t{q}')
        y += max(c.height for p, q, c in r) + 40
    if S.height > 1560: S = S.resize((int(S.width * 1560 / S.height), 1560))
    S.save(os.path.join(OUT, f'kort-oversigt-s2-{n:02d}.png'))
open(os.path.join(RD, 's2-items.tsv'), 'w', encoding='utf-8').write('id\tpage\tquestion\n' + '\n'.join(rows) + '\n')
print(len(rows), 'crops,', len(sheets), 'sheets')
