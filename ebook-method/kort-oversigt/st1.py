#!/usr/bin/env python3
"""st1.py (2026-10-17) -- STRUCTURE and NOTES sheets for a blind reader: front and back matter, chapter and section
heads, the run-in small-capital name openings, doubtful paragraph starts, misprint zooms, and the one footnote.
Regions are found from phrases on tesseract's lines; each crop is labelled `s1-NN-KK p.N` with its question.
    python3 ebook-method/kort-oversigt/st1.py  -> .render/kort-oversigt-s1-NN.png, .parts/reads/s1-items.tsv"""
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
def at(p, phrase):                                    # (y0, y1) px at 300 dpi of the line holding phrase
    ls = lines(p); f = fold(phrase)
    for t, y0, y1 in ls:
        if f[:14] in fold(t): return y0, y1
    for i in range(len(ls) - 1):
        if f[:14] in fold(ls[i][0] + ls[i + 1][0]): return ls[i][1], ls[i + 1][2]
    sys.exit(f'not found: p. {p} {phrase!r}')
def img(p, dpi=300):
    if C.FIRST_PRINTED <= p <= C.LAST_PRINTED: return Image.open(os.path.join(OUT, f'kort-oversigt-p{p}-300.png')).convert('L')
    im = Image.open(os.path.join(C.IMGDIR, f'{p + C.OFFSET:04d}.jpg')).convert('L'); return im.resize((im.width * 300 // 400, im.height * 300 // 400))
IT = []                                                # (page, y0, y1, scale, question) -- y in px at 300 dpi; None = whole page
# front and back matter: p < 1 or p > LAST are PDF pages (p + OFFSET)
for p, sc, q in [(-7, 0.5, 'Whole page: transcribe every printed line exactly (line breaks as /); describe any ornament or rule.'),
                 (-6, 0.3, 'Whole page: is anything printed on it? If so, transcribe it exactly.'),
                 (-5, 0.55, 'Whole page (title page): transcribe every printed line exactly, top to bottom (line breaks as /), with capitals, commas and stops as printed; describe any ornament, device or rule.'),
                 (-4, 0.3, 'Whole page: is anything printed on it (e.g. a printer\'s line at the foot)? If so, transcribe it exactly.'),
                 (-3, 0.62, 'Whole page (contents): transcribe every entry exactly with its page number, one entry per line, keeping indentation (main entry / sub-entry), numerals, letters, stops and spelling as printed.'),
                 (-2, 0.3, 'Whole page: is anything printed on it? If so, transcribe it exactly.'),
                 (-1, 0.62, 'Whole page (preface): transcribe the heading exactly; give the first words of every indented (new paragraph) line; transcribe the closing lines (date, signature) exactly and say how they are set.'),
                 (0, 0.3, 'Whole page: is anything printed on it? If so, transcribe it exactly.')]:
    IT.append((p, None, None, sc, q))
for p in (96, 97, 98, 99): IT.append((p, None, None, 0.3, 'Whole page: is anything printed on it (text, advertisement, printer\'s line)? If so, transcribe its first lines and any printer\'s line exactly.'))
Q_HEAD = 'Transcribe every heading line in this crop exactly (capitals, stops, numerals; line breaks as /), and say how each is set: centred or run in at the start of a paragraph; capitals, small capitals, s p a c e d, italic, larger type. Say what ornament or rule stands above it.'
for p in (1, 5, 17, 35, 43, 50, 63, 74): IT.append((p, 0, 1000, 0.6, Q_HEAD))
SEC = [(10, 'Verdensbillede'), (14, 'Den nye Videnskab'), (81, 'Problembehandlinger'), (82, 'psykologiske Problem'),
       (85, 'Tilværelsesproblemet'), (88, 'Erkendelsesproblemet.'), (92, 'Vurderingsproblemet'),
       (53, 'Erkendelsesteori'), (59, 'Etik. (Kritik'), (61, 'Enhedslære paa')]
for p, ph in SEC:
    y0, y1 = at(p, ph); IT.append((p, y0 - 200, y1 + 120, 0.9, Q_HEAD))
y0, y1 = at(91, 'Aarsagssætningens Historie')
IT.append((91, y0 - 260, y1 + 420, 0.9, 'Transcribe the line(s) of "Tillæg" exactly and say how set (centred heading, run in, italic, s p a c e d, smaller type). Is the text that follows set in SMALLER type than the text above it?'))
y0, y1 = at(92, 'Vurderingsproblemet')
IT.append((92, y0 - 420, y1 + 40, 0.9, 'Is the text above the heading set in SMALLER type than normal? Give the last words before the heading, and say what space or rule separates them from the heading.'))
Q_SC = 'Transcribe the line that begins the paragraph (the indented one) exactly: put words set in SMALL CAPITALS in [square brackets], words in italics in *stars*, s p a c e d words spaced. Keep the label (a. b. 1. α. β. γ.) exactly as printed.'
SC = [(5, 'har i sit Værk'), (7, 'Indenfor Protestantismen'), (12, 'staar her som den'), (15, 'den berømte Astro'), (18, 'kan kaldes den nyere'),
      (21, 'har gjort det første'), (26, 'har i sin Ethica'), (32, 'er ligesom'), (36, 'skal have faaet'), (38, 'ønskede at fjerne'),
      (39, 'bragte den erfarings'), (44, 'Ved et Besøg'), (45, 'Jacques'), (48, 'det især'), (64, 'Bondesøn'),
      (65, 'Romantikens egentlige'), (66, 'Romantikens Systematiker'), (68, 'Søn af en rig'), (70, 'I Danmark havde'), (71, 'religiøse Tænker'),
      (72, 'under Hegels Indflydelse'), (74, 'Positivismen har sit'), (75, 'Positivismens egentlige'), (77, 'af Aarhundredet indtog'),
      (78, 'faar med Rette'), (79, 'gik fra det praktiske'), (82, 'Af stor Betydning'), (84, 'Med Hensyn til Bevidsthedslivets'), (90, 'har fremstillet den')]
for p, ph in SC:
    y0, y1 = at(p, ph); IT.append((p, y0 - 60, y1 + 60, 1.0, Q_SC))
PAR = [(14, 'Himlen'), (17, 'Tænk Jorden'), (21, 'Sjæl og Legeme'), (22, 'synes ad sin egen'), (34, 'Kontinuitetens Lov'),
       (59, 'ordnes efter Love'), (84, 'Syntesebegrebet fører'), (81, 'tredie Udviklingsform')]
for p, ph in PAR:
    y0, y1 = at(p, ph); IT.append((p, y0 - 120, y1 + 10, 0.9, 'Does the LAST line of this crop begin a new paragraph (indented, or the line above it short)? Answer: new paragraph / same paragraph. Transcribe the first three words of the last line exactly, with any quotation mark (say which: „ “ « » ").'))
ZOOM = [(10, 'Bevægelsee'), (20, 'Principia'), (23, 'Elementa'), (67, 'om Mennesketilblivelsen'), (67, 'Enhed af Modsætninger'),
        (77, 'Aarhundres'), (79, 'Hypetese'), (83, 'kvantitive'), (94, 'Livsvurdening'), (90, 'har fremstillet den')]
for p, ph in ZOOM:
    y0, y1 = at(p, ph); IT.append((p, y0 - 70, y1 + 70, 1.0, 'Transcribe the middle line exactly, letter by letter for any odd-looking word (do not correct misprints); for a dash, say whether it is one dash or two, and whether a line break falls inside the dates.'))
y0, y1 = at(4, 'Smlg')
IT.append((4, y0 - 80, None, 0.9, 'FOOTNOTE(S): transcribe every note exactly, line by line (/), with its label as printed (1) *) etc.); mark *italic* and s p a c e d words; and say how the mark in the text above is printed.'))
rows = []; sheets = []; cur = []; hcur = 0
CR = []
for k, (p, y0, y1, sc, q) in enumerate(IT):
    im = img(p)
    if y0 is None: cr = im
    else: cr = im.crop((int(im.width * 0.04), max(0, y0), int(im.width * 0.96), min(im.height, y1 if y1 else im.height - 60)))
    cr = cr.resize((int(cr.width * sc), int(cr.height * sc)))
    wide = q.startswith('FOOTNOTE') or 'middle line' in q or q.startswith('Transcribe the line that begins')   # small type: a whole row, ~300 dpi
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
            k += 1; cid = f's1-{n:02d}-{k:02d}'; d.text((j * 780 + 4, y + 4), f'{cid}  p.{p}', fill=0, font=font); S.paste(cr, (j * 780, y + 30))
            rows.append(f'{cid}\t{p}\t{q}')
        y += max(c.height for p, q, c in r) + 40
    if S.height > 1560: S = S.resize((int(S.width * 1560 / S.height), 1560))
    S.save(os.path.join(OUT, f'kort-oversigt-s1-{n:02d}.png'))
open(os.path.join(RD, 's1-items.tsv'), 'w', encoding='utf-8').write('id\tpage\tquestion\n' + '\n'.join(rows) + '\n')
print(len(rows), 'crops,', len(sheets), 'sheets')
