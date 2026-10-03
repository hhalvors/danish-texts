#!/usr/bin/env python3
"""sheets.py -- crop sheets for the checks build.py could not settle (8 crops per sheet).
Each crop is the printed line around the disagreement, labelled with the check id,
the e-book reading and the layer reading. Output: ../../.render/df-sheetNN.png"""
import json, os, sys, subprocess
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))     # ebook-method/<book>/: scripts and the decisions (tracked)
BOOK = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'texts', 'hoeffding', os.path.basename(HERE))
WORK = os.path.join(BOOK, '.parts', 'ebook'); os.makedirs(WORK, exist_ok=True)   # scratch output (gitignored)
sys.path.insert(0, HERE); from pagemap import pdfpage, scan_path
OUT = os.path.join(BOOK, '.render'); os.makedirs(OUT, exist_ok=True)
DPI = 200; S = DPI / 72
checks = json.load(open(os.path.join(WORK, 'checks.json')))
if '--todo' in sys.argv:      # only what decisions.tsv does not yet settle, from checks, punct and paras
    done = set(l.split('\t')[0] for l in open(os.path.join(HERE, 'decisions.tsv'), encoding='utf-8') if not l.startswith('#'))
    allc = checks + json.load(open(os.path.join(WORK, 'punct.json'))) + [dict(x, id='PARA', key=f"P{x['page']}|{x['word']}|{x['kind']}", ebook=x['kind'], layer='') for x in json.load(open(os.path.join(WORK, 'paras.json')))]
    checks = [c for c in allc if c['key'] not in done]
if '--find' in sys.argv:      # sheets.py --find p1-p2:regex ... : crop every layer word matching regex
    import re, html
    checks = []
    for arg in sys.argv[sys.argv.index('--find') + 1:]:
        rng, rx = arg.split(':', 1); a, b = map(int, rng.split('-'))
        for p in range(a, b + 1):
            x = subprocess.run(['pdftotext', '-bbox', '-f', str(pdfpage(p)), '-l', str(pdfpage(p)), scan_path(), '-'], capture_output=True, text=True).stdout
            for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', x):
                if re.search(rx, html.unescape(m.group(5))):
                    checks.append({'id': 'Q', 'page': p, 'ebook': rx, 'layer': html.unescape(m.group(5)), 'bbox': tuple(map(float, m.group(1, 2, 3, 4)))})
extra = [] if '--find' in sys.argv or '--todo' in sys.argv else json.load(open(os.path.join(WORK, 'extra-crops.json'))) if os.path.exists(os.path.join(WORK, 'extra-crops.json')) else []
pages = {}
def page_img(p):
    if p not in pages:
        f = os.path.join(OUT, f'df-p{p:03d}')
        for attempt in (0, 1):
            if attempt or not os.path.exists(f + '.png'):
                subprocess.run(['pdftoppm', '-r', str(DPI), '-gray', '-png', '-singlefile', '-f', str(pdfpage(p)), '-l', str(pdfpage(p)), scan_path(), f], check=True)
            try: pages[p] = Image.open(f + '.png').convert('L'); break
            except OSError: continue      # a truncated file from an interrupted run: render again
    return pages[p]
crops = []
for c in checks + extra:
    im = page_img(c['page']); x0, y0, x1, y1 = c['bbox']
    box = (max(0, int((x0 - 140) * S)), max(0, int((y0 - 16) * S)), min(im.width, int((x1 + 140) * S)), min(im.height, int((y1 + 16) * S)))
    cr = im.crop(box); lab = Image.new('L', (cr.width, 26), 255)
    ImageDraw.Draw(lab).text((4, 6), f"{c['id']} p.{c['page']}  e-book: {c['ebook']!r} in {c.get('word','')!r}   layer: {c['layer']!r}", fill=0)
    both = Image.new('L', (cr.width, cr.height + 26), 255); both.paste(lab, (0, 0)); both.paste(cr, (0, 26)); crops.append(both)
for k in range(0, len(crops), 8):
    grp = crops[k:k + 8]; W = max(g.width for g in grp); H = sum(g.height + 6 for g in grp)
    sh = Image.new('L', (W, H), 200); y = 0
    for g in grp: sh.paste(g, (0, y)); y += g.height + 6
    sh.save(os.path.join(OUT, ('df-find' if '--find' in sys.argv else 'df-todo' if '--todo' in sys.argv else 'df-sheet') + f'{k // 8 + 1:02d}.png'))
print(len(crops), 'crops ->', (len(crops) + 7) // 8, 'sheets in', OUT)
