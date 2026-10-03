#!/usr/bin/env python3
"""notes-check.py -- list every word in the Noter (pp. 245-255) of transcription.tex that is attested
nowhere else (other books' transcriptions, or this book's own text pages), find it on the scan's
text layer, and write crop sheets for the image (.render/rf-notes-NN.png) plus notes-check.json.
Cheap targeted check (2026-10-02): the e-book's notes are where its own OCR errors survive."""
import re, os, glob, json, subprocess, html, difflib, sys
HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'texts', 'hoeffding', os.path.basename(HERE))
SCAN = os.path.expanduser('~/mnt/bibliotek/Høffding, Harald/1924-religionsfilosofi-3udg.pdf')
OFF = 18                                  # printed page = PDF page - 18
W = '[A-Za-zÀ-ÖØ-öø-ÿ]+'
def words(t): return re.findall(W, re.sub(r'\\[A-Za-z]+', ' ', re.sub(r'(?m)%.*$', '', t)))
T = open(os.path.join(BOOK, 'transcription.tex'), encoding='utf-8').read()
i = T.index('% ===== NOTER'); body, notes = T[:i], T[i:]
VOC = set(words(body))
for f in glob.glob(os.path.join(BOOK, '..', '..', '*', '*', 'transcription.tex')):
    if not os.path.samefile(os.path.dirname(f), BOOK): VOC.update(words(open(f, encoding='utf-8', errors='replace').read()))
VOCL = {v.lower() for v in VOC}
cands = []
for m in re.finditer(r'% --- p\. (\d+) ---\n(.*?)(?=% --- p\. \d+ ---|\Z)', notes, re.S):
    p = int(m.group(1))
    for w in sorted(set(words(m.group(2)))):
        if len(w) >= 3 and w not in VOC and w.lower() not in VOCL: cands.append((p, w))
print('unattested words in the Noter:', len(cands))
def layer(p):
    x = subprocess.run(['pdftotext', '-bbox', '-f', str(p + OFF), '-l', str(p + OFF), SCAN, '-'], capture_output=True, text=True).stdout
    ph = float(re.search(r'<page width="[\d.]+" height="([\d.]+)"', x).group(1))
    return ph, [(html.unescape(q[4]), tuple(map(float, q[:4]))) for q in re.findall(r'xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)<', x)]
out = []; L = {}
for p, w in cands:
    if p not in L: L[p] = layer(p)
    ph, ws = L[p]
    best = max(ws, key=lambda q: difflib.SequenceMatcher(None, w.lower(), re.sub('[^A-Za-zÀ-ÿ]', '', q[0]).lower()).ratio())
    r = difflib.SequenceMatcher(None, w.lower(), re.sub('[^A-Za-zÀ-ÿ]', '', best[0]).lower()).ratio()
    out.append({'page': p, 'word': w, 'layer': best[0], 'ratio': round(r, 2), 'bbox': best[1], 'ph': ph})
json.dump(out, open(os.path.join(BOOK, '.parts', 'notes-check.json'), 'w'), ensure_ascii=False, indent=0)
KEEP = None
if '--only' in sys.argv: KEEP = set(sys.argv[sys.argv.index('--only') + 1].split(','))
if KEEP: out = [c for c in out if c['word'] in KEEP]
if '--sheets' in sys.argv:
    from PIL import Image, ImageDraw
    os.makedirs(os.path.join(BOOK, '.render'), exist_ok=True); imgs = {}; crops = []
    for c in out:
        p = c['page']
        if p not in imgs:
            f = os.path.join(BOOK, '.render', f'rf-n{p}')
            subprocess.run(['pdftoppm', '-r', '220', '-gray', '-png', '-singlefile', '-f', str(p + OFF), '-l', str(p + OFF), SCAN, f]); imgs[p] = Image.open(f + '.png')
        im = imgs[p]; s = im.height / c['ph']; x0, y0, x1, y1 = c['bbox']
        cr = im.crop((max(0, int((x0 - 70) * s)), max(0, int((y0 - 3) * s)), min(im.width, int((x1 + 70) * s)), int((y1 + 3) * s)))
        lab = Image.new('L', (cr.width, 18), 255); ImageDraw.Draw(lab).text((2, 3), f"p.{p} transcription: {c['word']}", fill=0)
        b = Image.new('L', (max(cr.width, 260), cr.height + 18), 255); b.paste(lab, (0, 0)); b.paste(cr, (0, 18)); crops.append(b)
    per = 16
    for k in range(0, len(crops), per):
        g = crops[k:k + per]; cols = 2; rows = (len(g) + 1) // 2; cw = max(x.width for x in g); rh = max(x.height for x in g)
        sh = Image.new('L', (cw * cols + 8, rh * rows + 4 * rows), 200)
        for n, x in enumerate(g): sh.paste(x, ((n % cols) * (cw + 8), (n // cols) * (rh + 4)))
        sh.save(os.path.join(BOOK, '.render', f'rf-notes-{k // per + 1:02d}.png'))
    print('sheets:', (len(crops) + per - 1) // per)
