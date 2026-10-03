#!/usr/bin/env python3
"""check.py -- check an existing transcription (texts/hoeffding/vort-hjem/transcription.tex) against
the scan's text layer, letter by letter, and find the exact page turns.

    python3 ebook-method/vort-hjem/check.py            list disagreements (.parts/checks.json) + crop sheets
    python3 ebook-method/vort-hjem/check.py --pages    print where each printed page begins in the transcription

The transcription is one witness, the layer the other; every disagreement no rule settles is cropped
(texts/hoeffding/vort-hjem/.render/vh-sheetNN.png) and decided at the image; decisions.tsv records them.
"""
import re, os, sys, json, html, difflib, subprocess, glob
HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'texts', 'hoeffding', os.path.basename(HERE))
WORK = os.path.join(BOOK, '.parts'); os.makedirs(WORK, exist_ok=True)
sys.path.insert(0, HERE); from pagemap import pdfpage, scan_path, FIRST_PRINTED, LAST_PRINTED
L = 'A-Za-zÀ-ÖØ-öø-ÿ0-9'; ISL = re.compile('[' + L + ']')
SRC = open(os.path.join(BOOK, 'transcription.tex'), encoding='utf-8').read()
start = SRC.index('\\section*{I.}'); SRC_END = SRC.index('\\end{document}')
# letters of the transcription with their offsets in the source (commands, comments, braces skipped)
ecs = []; eoff = []; i = start
while i < SRC_END:
    c = SRC[i]
    if c == '%' and SRC[i - 1] != '\\':
        while i < len(SRC) and SRC[i] != '\n': i += 1
        continue
    if c == '\\':
        m = re.match(r'\\[A-Za-z]+\*?(\{\d+\})?|\\.', SRC[i:i + 40], re.S); i += len(m.group(0)); continue
    if ISL.match(c): ecs.append(c); eoff.append(i)
    i += 1
ecs = ''.join(ecs)
# layer, running heads and folios dropped
LAY = {}
for p in range(FIRST_PRINTED, LAST_PRINTED + 1):
    x = subprocess.run(['pdftotext', '-bbox', '-f', str(pdfpage(p)), '-l', str(pdfpage(p)), scan_path(), '-'], capture_output=True, text=True).stdout
    ph = float(re.search(r'<page width="[\d.]+" height="([\d.]+)"', x).group(1))
    ws = [(html.unescape(w[4]), tuple(map(float, w[:4]))) for w in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', x)]
    # the content stream's word order is scrambled and the scan is skewed: deskew (slope with the
    # sharpest line histogram), then rebuild reading order from the boxes
    yof = lambda b, a, c: (b[1] + b[3]) / 2 - a * b[0] - c * (b[0] - 250) ** 2     # skew a, page curvature c
    def peak(ac):
        h = {}
        for w, b in ws: k = round(yof(b, *ac)); h[k] = h.get(k, 0) + 1
        return sum(v * v for v in h.values())
    ac = max(((a / 500, c / 1e5) for a in range(-30, 31) for c in range(-20, 21)), key=peak)
    ws.sort(key=lambda t: yof(t[1], *ac)); lines = []
    for w, b in ws:
        yc = yof(b, *ac)
        if lines and yc - lines[-1][0] < 4: lines[-1][1].append((w, b))
        else: lines.append([yc, [(w, b)]])
    ws = [t for yc, ln in lines for t in sorted(ln, key=lambda t: t[1][0])]
    top = min((b[1] for w, b in ws), default=0)
    ws = [(w, b) for w, b in ws if not (b[1] < top + 12 and re.fullmatch(r'VORT|HJEM\.?|\d+|[^\w]*', w))]
    if p == FIRST_PRINTED:
        k = next(n for n, (w, b) in enumerate(ws) if w.startswith('I.') or w == 'I')
        ws = ws[k:]
    LAY.setdefault('words', {})[p] = [(w, b) for w, b in ws]
    chars = []; cbox = []
    for w, b in ws:
        for ch in w:
            if ISL.match(ch): chars.append(ch); cbox.append(b)
    LAY[p] = {'chars': ''.join(chars), 'cbox': cbox, 'ph': ph}
WORDS = LAY.pop('words')
LS = ''.join(LAY[p]['chars'] for p in LAY); loff = {}; o = 0
for p in LAY: loff[p] = o; o += len(LAY[p]['chars'])
lpage = lambda j: max(p for p in loff if loff[p] <= j)
ops = difflib.SequenceMatcher(None, ecs, LS, autojunk=False).get_opcodes()
pstart = {}; hunks = []
for op, a1, a2, b1, b2 in ops:
    for p in LAY:
        if p not in pstart and b1 <= loff[p] < max(b2, b1 + 1): pstart[p] = a1 + (loff[p] - b1 if op == 'equal' else 0)
    if op != 'equal':
        p = lpage(b1); hunks.append({'page': p, 'e': ecs[a1:a2], 'l': LS[b1:b2], 'eo': eoff[min(a1, len(eoff) - 1)], 'bbox': LAY[p]['cbox'][min(b1 - loff[p], len(LAY[p]['cbox']) - 1)]})
FAULT = {('h', 'li'), ('h', 'b'), ('n', 'u'), ('u', 'n'), ('e', 'c'), ('t', 'l'), ('f', 't'), ('l', 'i'), ('i', 'l'), ('r', 'i'), ('m', 'rn'), ('rn', 'm'),
         ('ø', 'o'), ('æ', 'se'), ('D', 'B'), ('I', 'l'), ('l', 'I'), ('0', 'o'), ('1', 'l'), ('é', 'e')}
FAULT |= {('à', 'å')}
# words the deskewed layer still puts on the wrong line (curvature) come out as a deletion and an
# identical insertion a few hunks apart: a move, not a disagreement
moved = set()
for k, h in enumerate(hunks):
    for k2 in range(max(0, k - 6), min(len(hunks), k + 7)):
        if k2 != k and k2 not in moved and k not in moved and len(h['e']) > 1 and h['e'] == hunks[k2]['l']: moved |= {k, k2}
checks = []; auto = len(moved)
for k, h in enumerate(hunks):
    if k in moved: continue
    # case-only differences and lone extra letters are NOT settled by rule (eks./Eks., værd/værdt):
    # only a lone stroke-like letter the layer adds (a speck or rule read as i, l, I, j, 1) is noise
    if (h['e'], h['l']) in FAULT: auto += 1; continue
    if h['e'] == '' and h['l'] in ('i', 'l', 'I', 'j', '1'): auto += 1; continue
    w = re.findall('[' + L + ']+', SRC[max(0, h['eo'] - 20): h['eo'] + 20])
    h['ctx'] = SRC[max(0, h['eo'] - 30): h['eo'] + 30].replace('\n', ' ')
    h['id'] = f'V{len(checks) + 1:03d}'; checks.append(h)
print(f'{len(hunks)} disagreements, {auto} settled by rule, {len(checks)} to look at')
json.dump(checks, open(os.path.join(WORK, 'checks.json'), 'w'), ensure_ascii=False, indent=0)
if '--pages' in sys.argv:
    for p in sorted(pstart):
        o = eoff[pstart[p]]; print(p, repr(SRC[max(0, o - 40): o]), '‖', repr(SRC[o: o + 40]))
if '--sheets' in sys.argv:
    from PIL import Image, ImageDraw
    OUT = os.path.join(BOOK, '.render'); os.makedirs(OUT, exist_ok=True); imgs = {}; crops = []
    for c in checks:
        p = c['page']
        if p not in imgs:
            f = os.path.join(OUT, f'vh-p{p}'); subprocess.run(['pdftoppm', '-r', '200', '-gray', '-png', '-singlefile', '-f', str(pdfpage(p)), '-l', str(pdfpage(p)), scan_path(), f]); imgs[p] = Image.open(f + '.png')
        im = imgs[p]; s = im.height / LAY[p]['ph']; x0, y0, x1, y1 = c['bbox']
        cr = im.crop((max(0, int((x0 - 120) * s)), max(0, int((y0 - 12) * s)), min(im.width, int((x1 + 120) * s)), int((y1 + 12) * s)))
        lab = Image.new('L', (cr.width, 22), 255); ImageDraw.Draw(lab).text((3, 5), f"{c['id']} p.{p} transcription {c['e']!r} layer {c['l']!r}", fill=0)
        b = Image.new('L', (cr.width, cr.height + 22), 255); b.paste(lab, (0, 0)); b.paste(cr, (0, 22)); crops.append(b)
    for k in range(0, len(crops), 8):
        g = crops[k:k + 8]; W = max(x.width for x in g); H = sum(x.height + 6 for x in g); sh = Image.new('L', (W, H), 200); y = 0
        for x in g: sh.paste(x, (0, y)); y += x.height + 6
        sh.save(os.path.join(OUT, f'vh-sheet{k // 8 + 1:02d}.png'))
    print('sheets:', (len(crops) + 7) // 8)

if '--words' in sys.argv:
    # word-level comparison, punctuation included (the letter alignment above ignores punctuation)
    t = re.sub(r'(?<!\\)%.*', '', SRC[start:SRC_END])
    t = re.sub(r'\\apage\{\d+\}|\\noindent|\\bigskip|\\thispagestyle\{\w+\}', ' ', t)
    t = re.sub(r'\\(?:section\*|emph|textit)\{([^}]*)\}', r'\1', t)
    t = t.replace('\\-', '').replace('\\ ', ' ').replace('~', ' ').replace('---', '—').replace('--', '–')
    et = t.split()
    lt = []; lb = []
    for p in sorted(WORDS):
        for w, b in WORDS[p]:
            if lt and lt[-1].endswith('-') and len(lt[-1]) > 1 and lt[-1][-2].isalpha(): lt[-1] = lt[-1][:-1] + w
            else: lt.append(w); lb.append((p, b))
    sm = difflib.SequenceMatcher(None, et, lt, autojunk=False); wd = []
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op != 'equal':
            wd.append(lb[min(b1, len(lb) - 1)])
            print(f"W{len(wd):02d} p.{wd[-1][0]} {' '.join(et[max(0,a1-3):a1])} [{' '.join(et[a1:a2])} | {' '.join(lt[b1:b2])}] {' '.join(et[a2:a2+2])}")
    # --wsheets 3,7,12: crop those word disagreements, three lines high and full measure, for the image
    if '--wsheets' in sys.argv:
        from PIL import Image, ImageDraw
        OUT = os.path.join(BOOK, '.render'); os.makedirs(OUT, exist_ok=True); imgs = {}; crops = []
        for n in map(int, sys.argv[sys.argv.index('--wsheets') + 1].split(',')):
            p, (x0, y0, x1, y1) = wd[n - 1]
            if p not in imgs:
                f = os.path.join(OUT, f'vh-p{p}'); subprocess.run(['pdftoppm', '-r', '220', '-gray', '-png', '-singlefile', '-f', str(pdfpage(p)), '-l', str(pdfpage(p)), scan_path(), f + 'w']); imgs[p] = Image.open(f + 'w.png')
            im = imgs[p]; sc = im.height / LAY[p]['ph']
            cr = im.crop((int(30 * sc), max(0, int((y0 - 16) * sc)), int(470 * sc), int((y1 + 16) * sc)))
            lab = Image.new('L', (cr.width, 16), 255); ImageDraw.Draw(lab).text((3, 3), f'W{n:02d} p.{p}', fill=0)
            b = Image.new('L', (cr.width, cr.height + 16), 255); b.paste(lab, (0, 0)); b.paste(cr, (0, 16)); crops.append(b)
        for k in range(0, len(crops), 10):
            g = crops[k:k + 10]; sh = Image.new('L', (max(x.width for x in g), sum(x.height + 4 for x in g)), 200); y = 0
            for x in g: sh.paste(x, (0, y)); y += x.height + 4
            sh.save(os.path.join(OUT, f'vh-wsheet{k // 10 + 1:02d}.png'))
        print('wsheets:', (len(crops) + 9) // 10)

if '--italics' in sys.argv:
    # italics are invisible to the layer: shear each word's image and ask whether its vertical strokes
    # line up better slanted (italic) than upright (roman); print the runs of slanted words
    import numpy as np
    from PIL import Image
    OUT = os.path.join(BOOK, '.render'); os.makedirs(OUT, exist_ok=True); ICROPS = []
    def sharp(a, sh):
        h, w = a.shape; prof = np.zeros(w + 2 * h + 2)
        for y in range(h): off = h + int(round(sh * (h - y))); prof[off: off + w] += a[y]
        return (prof ** 2).sum()
    # calibrated on p. 3 and p. 8: italic words score 1.09-1.33 at shear -0.1, roman ones 0.77-1.01
    for p in sorted(WORDS):
        f = os.path.join(OUT, f'vh-p{p}w')
        if not os.path.exists(f + '.png'): subprocess.run(['pdftoppm', '-r', '220', '-gray', '-png', '-singlefile', '-f', str(pdfpage(p)), '-l', str(pdfpage(p)), scan_path(), f])
        im = np.asarray(Image.open(f + '.png').convert('L'), dtype=float); sc = im.shape[0] / LAY[p]['ph']; run = []
        for w, (x0, y0, x1, y1) in WORDS[p] + [('', (0, 0, 0, 0))]:
            ital = False
            a = (im[int(y0 * sc): int(y1 * sc), int(x0 * sc): int(x1 * sc)] < 128).astype(float)
            if a.sum(): r = sharp(a, -0.1) / sharp(a, 0.0); ital = r >= float(os.environ.get("ITAL", "1.07"))
            if ital: run.append((f'{w}({r:.2f})', (x0, y0, x1, y1)))
            elif run:
                print(f'p.{p}', ' '.join(t for t, b in run))
                # crop the run's own line (not a text search, which can land on another line)
                Y0 = min(b[1] for t, b in run); Y1 = max(b[3] for t, b in run)
                g = Image.fromarray(im[int((Y0 - 4) * sc): int((Y1 + 4) * sc), int(30 * sc): int(470 * sc)].astype('uint8'))
                ICROPS.append((f"p.{p} {' '.join(t for t, b in run)}", g)); run = []
    from PIL import ImageDraw
    sh = Image.new('L', (max(g.width for t, g in ICROPS), sum(g.height + 16 for t, g in ICROPS)), 255); y = 0
    for t, g in ICROPS: ImageDraw.Draw(sh).text((3, y + 2), t, fill=0); sh.paste(g, (0, y + 14)); y += g.height + 16
    sh.save(os.path.join(OUT, 'vh-italics.png')); print('vh-italics.png')

if '--lines' in sys.argv:
    # --lines 3:Fylde,9:franca  crop the printed line holding that layer word (first match on the page)
    from PIL import Image, ImageDraw
    OUT = os.path.join(BOOK, '.render'); crops = []
    for spec in sys.argv[sys.argv.index('--lines') + 1].split(','):
        p, word = spec.split(':'); p = int(p); f = os.path.join(OUT, f'vh-p{p}w')
        if not os.path.exists(f + '.png'): subprocess.run(['pdftoppm', '-r', '220', '-gray', '-png', '-singlefile', '-f', str(pdfpage(p)), '-l', str(pdfpage(p)), scan_path(), f])
        im = Image.open(f + '.png').convert('L'); sc = im.height / LAY[p]['ph']
        x0, y0, x1, y1 = next(b for w, b in WORDS[p] if word in w)
        cr = im.crop((int(30 * sc), int((y0 - 5) * sc), int(470 * sc), int((y1 + 5) * sc)))
        b = Image.new('L', (cr.width, cr.height + 14), 255); ImageDraw.Draw(b).text((3, 2), spec, fill=0); b.paste(cr, (0, 14)); crops.append(b)
    sh = Image.new('L', (max(x.width for x in crops), sum(x.height + 3 for x in crops)), 200); y = 0
    for x in crops: sh.paste(x, (0, y)); y += x.height + 3
    sh.save(os.path.join(OUT, 'vh-lines.png')); print('vh-lines.png')

if '--mark' in sys.argv:
    # put \opage{N} where the layer says page N begins (replacing the old approximate \apage{N});
    # a page that opens mid-word gets „%“ at the break, one that opens with a heading gets the
    # comment line before the heading and \opage after \noindent
    S = SRC
    if re.search(r'\\opage\{\d+\}', S[start:]): sys.exit('--mark: the transcription already has \\opage markers (done 2026-10-02)')
    ins = []
    for p in sorted(pstart):
        o = eoff[pstart[p]]
        h = S.rfind('\\section*{', 0, o)
        if h >= 0 and S[h + 10: o].strip() == '':
            n = S.index('\\noindent', h) + len('\\noindent '); ins.append((h, h, f'% --- p. {p} ---\n')); ins.append((n, n, f'\\opage{{{p}}}'))
        elif re.match('[' + L + ']', S[o - 1]):
            ins.append((o, o, f'%\n% --- p. {p} ---\n\\opage{{{p}}}'))
        else:
            a = o
            while S[a - 1] in ' \n': a -= 1
            ins.append((a, o, f'\n% --- p. {p} ---\n\\opage{{{p}}}'))
    for a, b, t in sorted(ins, reverse=True): S = S[:a] + t + S[b:]
    S = re.sub(r' ?\\apage\{\d+\} ?', ' ', S)          # the old markers
    S = re.sub(r' +\n', '\n', S)                         # spaces they leave at line ends
    S = S.replace('\\newcommand{\\apage}[1]{\\marginnote{\\footnotesize\\textit{[#1]}}}\n', '')
    open(os.path.join(BOOK, 'transcription.tex'), 'w', encoding='utf-8').write(S)
    print('marked', sorted(pstart))
