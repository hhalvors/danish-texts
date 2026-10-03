#!/usr/bin/env python3
"""ebook-method/collate/check.py -- collate a finished transcription against an independent reading of
its scan (the scan's text layer, or a fresh tesseract OCR), word by word with punctuation.  It finds
(1) the readings to decide at the image, (2) italics the transcription lacks or has in excess, and
(3) the exact page turns.  Self-contained; rerunnable; writes only into the book's .parts/ and .render/
(and transcription.tex on --apply / --mark --write, after a backup).

    python3 ebook-method/collate/check.py BOOK            summary; open checks -> .parts/collate/checks.tsv
    ... BOOK --sheets          crop every open check, 10 to a sheet (.render/BOOK-cNN.png), witness word boxed
    ... BOOK --italics         italics by stroke slant vs the transcription's \\emph; open ones cropped (BOOK-iNN.png)
    ... BOOK --pages           where each printed page begins, and how far each existing marker is off
    ... BOOK --apply           apply decisions.tsv (W, P, =text) to transcription.tex (backup first)
    ... BOOK --mark [--write]  page markers at the exact turns: dry run to .parts/collate/, --write replaces
    ... BOOK --witness ocr     tesseract instead of the text layer (cached in .parts/collate/ocr/)

BOOK is a folder under texts/hoeffding/.  Settings: ebook-method/BOOK/pagemap.py
    required  FIRST_PRINTED, LAST_PRINTED, pdfpage(p) -> PDF page, scan_path()
    optional  FIRST_FROM / LAST_UPTO  witness word where the text starts on the first page / ends on the last
              PAGES (a list, for excerpts), CUTS {page: (first word kept or None, last word kept or None)}
              HEAD / FOOT   regex for a running-head line / foot line (default: folio or all-capitals lines)
              WITNESS 'layer' | 'ocr'   LANG 'dan'   REORDER True (rebuild line order from word boxes)
              ITAL 1.07 (slant score from which a word counts as italic)   START / END (strings in the .tex)
Decisions: ebook-method/BOOK/decisions.tsv, lines   key <TAB> decision <TAB> note   (key as printed)
    T  the transcription is right            W  the witness is right: take its reading (italics: take its style)
    P  the print has the witness reading as a misprint: take it and mark PRINTED AS IS
    =text  neither: put text                 ?  undecided (stays open)
The witness must not be the source the transcription was made from, or shared errors stay invisible.
"""
import re, os, sys, html, difflib, subprocess, glob, shutil, datetime, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
if len(sys.argv) < 2 or sys.argv[1].startswith('-'): sys.exit(__doc__)
NAME = sys.argv[1]; ARGS = sys.argv[2:]
CONF = os.path.join(ROOT, 'ebook-method', NAME); BOOK = os.path.join(ROOT, 'texts', 'hoeffding', NAME)
sys.path.insert(0, CONF); import pagemap as C
def opt(k, d=None): return ARGS[ARGS.index(k) + 1] if k in ARGS else d
WITNESS = opt('--witness', getattr(C, 'WITNESS', 'layer')); LANG = getattr(C, 'LANG', 'dan')
ITAL = float(os.environ.get('ITAL', getattr(C, 'ITAL', 1.07))); DPI = 300
WORK = os.path.join(BOOK, '.parts', 'collate'); OUT = os.path.join(BOOK, '.render')
os.makedirs(WORK, exist_ok=True); os.makedirs(OUT, exist_ok=True)
PAGES = list(getattr(C, 'PAGES', range(C.FIRST_PRINTED, C.LAST_PRINTED + 1)))
CUTS = dict(getattr(C, 'CUTS', {}))                    # page -> (first witness word kept, last witness word kept)
if hasattr(C, 'FIRST_FROM'): CUTS[PAGES[0]] = (C.FIRST_FROM, CUTS.get(PAGES[0], (None, None))[1])
if hasattr(C, 'LAST_UPTO'): CUTS[PAGES[-1]] = (CUTS.get(PAGES[-1], (None, None))[0], C.LAST_UPTO)
L = 'A-Za-zÀ-ÖØ-öø-ÿ0-9'; ISL = re.compile('[' + L + ']')
letters = lambda s: re.sub('[^' + L + ']', '', s)

# ======================= the transcription as plain text, each character traced to the source =========
TEX = os.path.join(BOOK, 'transcription.tex'); SRC = open(TEX, encoding='utf-8').read()
MARK = re.compile(r'% --- p\. (\d+) ---|\\[oa]page\{(\d+)\}')
BEGIN = SRC.index('\\begin{document}') if '\\begin{document}' in SRC else 0
def _first_mark(i):                      # the first page marker after \begin{document} that is not in a comment
    for m in MARK.finditer(SRC, i):
        ls = SRC.rfind('\n', 0, m.start()) + 1
        if not re.search(r'(?<!\\)%', SRC[ls:m.start()]) or m.group(1): return m.start()
START = SRC.index(C.START) if hasattr(C, 'START') else _first_mark(BEGIN)
END = SRC.index(getattr(C, 'END', '\\end{document}'), START)
SKIPARG = {'label', 'ref', 'pageref', 'cite', 'addcontentsline', 'thispagestyle', 'pagestyle', 'setcounter', 'addtocounter',
           'hspace', 'vspace', 'rule', 'includegraphics', 'renewcommand', 'newcommand', 'markboth', 'markright', 'phantom',
           'marginnote', 'begin', 'end', 'url', 'href', 'footnotemark', 'opage', 'apage', 'raisebox', 'fontsize'}
EMPH = {'emph', 'textit', 'textsl', 'spaced', 'so', 'textso', 'sperret'}
REPL = {'ldots': '...', 'dots': '...', 'textellipsis': '...', 'glqq': '„', 'grqq': '“', 'flqq': '«', 'frqq': '»',
        'guillemotleft': '«', 'guillemotright': '»', 'S': '§', 'ae': 'æ', 'o': 'ø', 'aa': 'å', 'AE': 'Æ', 'O': 'Ø',
        'AA': 'Å', 'ss': 'ß', 'textendash': '–', 'textemdash': '—', 'oe': 'œ', 'OE': 'Œ', 'textquoteright': '’'}
ACC = {"'": '\u0301', '`': '\u0300', '^': '\u0302', '"': '\u0308', '~': '\u0303', 'c': '\u0327', 'v': '\u030c', '=': '\u0304'}
LIG = [('---', '—'), ('--', '–'), ('``', '“'), ("''", '”'), (',,', '„'), ('<<', '«'), ('>>', '»'), ('"`', '„'), ('"\'', '“'), ('"-', ''), ('"=', '-')]
PT = []; MARKS = {}; cur = [None]; pending = []; SC = [False]   # SC: inside \textsc (compared in capitals)
def group_end(i):                       # i at '{': index after the matching '}'
    d = 0
    while True:
        c = SRC[i]
        if c == '\\': i += 2; continue
        if c == '%':
            while SRC[i] != '\n': i += 1
            continue
        d += {'{': 1, '}': -1}.get(c, 0); i += 1
        if d == 0: return i
def skip_ws(i):
    while i < END and SRC[i] in ' \t\n': i += 1
    return i
def marker(p):
    p = int(p)
    while pending:                       # the previous page's footnotes go to its foot, where the witness reads them
        a, b, em = pending.pop(0); scan(a, b, em)
    cur[0] = p
    if p not in MARKS: MARKS[p] = len(PT)
def scan(i, j, em):
    while i < j:
        c = SRC[i]
        if c == '%':
            m = re.match(r'% --- p\. (\d+) ---', SRC[i:i + 20])
            if m: marker(m.group(1))
            while i < j and SRC[i] != '\n': i += 1
            i += 1
            while i < j and SRC[i] in ' \t': i += 1
            continue
        if c == '\\':
            m = MARK.match(SRC, i)
            if m and m.group(2): marker(m.group(2)); i = m.end(); continue
            m = re.match(r'\\([A-Za-z]+)\*?|\\(.)', SRC[i:i + 40], re.S); i0 = i; i += len(m.group(0))
            nm = m.group(1) or m.group(2)
            if m.group(2):
                if nm in ACC:
                    if SRC[i] == '{': k = group_end(i); base = SRC[i + 1:k - 1]; i = k
                    else: base = SRC[i]; i += 1
                    PT.append((unicodedata.normalize('NFC', base + ACC[nm]), i0, i, em, cur[0]))
                elif nm in ' ,;:': PT.append((' ' if nm == ' ' else '', i0, i, em, cur[0]))
                elif nm == '\\':
                    PT.append((' ', i0, i, em, cur[0]))
                    if i < j and SRC[i] == '[': i = SRC.index(']', i) + 1
                elif nm in '&%$#_{}': PT.append((nm, i0, i, em, cur[0]))
                continue                                    # \- and the rest: nothing
            if m.group(1): i = skip_ws(i) if SRC[i] in ' \t\n' and not SRC[i:i + 2].count('\n\n') else i
            if nm in REPL: PT.append((REPL[nm], i0, i, em, cur[0])); continue
            if nm == 'footnote':
                if SRC[i] == '[': i = SRC.index(']', i) + 1
                k = group_end(i); pending.append((i + 1, k - 1, em)); i = k; continue
            if nm in ('it', 'em', 'itshape', 'sl', 'slshape'): em = True; continue
            while i < j and SRC[i] == '[': i = SRC.index(']', i) + 1
            if nm in SKIPARG:
                while i < j and SRC[i] == '{': i = group_end(i)
                continue
            if i < j and SRC[i] == '{':
                k = group_end(i); sc0 = SC[0]; SC[0] = sc0 or nm == 'textsc'
                scan(i + 1, k - 1, em or nm in EMPH); SC[0] = sc0; i = k
            continue
        if c == '{':
            k = group_end(i); scan(i + 1, k - 1, em); i = k; continue
        if c == '}': i += 1; continue
        for a, b in LIG:
            if SRC.startswith(a, i): PT.append((b, i, i + len(a), em, cur[0])); i += len(a); break
        else:
            PT.append((' ' if c in ' \t\n~' else (c.upper() if SC[0] else c), i, i + 1, em, cur[0])); i += 1
cur[0] = C.FIRST_PRINTED
scan(START, END, False); marker(10 ** 6)
# collapse whitespace; T = plain text, TI = per character (src start, src end, emphasised, page)
T = []; TI = []; TAT = []                # TAT[n]: length of T before PT entry n (for the markers)
for ch, a, b, em, p in PT:
    TAT.append(len(T))
    for k, x in enumerate(ch):
        if x == ' ' and (not T or T[-1] == ' '): continue
        T.append(x); TI.append((a, b if k == len(ch) - 1 else a, em, p))
T = ''.join(T)
MARKI = {p: (TAT[n] if n < len(TAT) else len(T)) for p, n in MARKS.items() if p < 10 ** 6}
def toks(s, offset=0):
    return [(m.group(0), m.start() + offset, m.end() + offset) for m in re.finditer(r'\S+', s)]
ETOK = toks(T)

# ======================= the witness: words with boxes, page furniture removed ==========================
def render(p, dpi):
    f = os.path.join(OUT, f'{NAME}-p{p}-{dpi}')
    if os.path.exists(f + '.png'):
        from PIL import Image
        try: Image.open(f + '.png').load(); return f + '.png'
        except Exception: pass                            # cut off by an interrupted run: render again
    subprocess.run(['pdftoppm', '-r', str(dpi), '-gray', '-png', '-singlefile', '-f', str(C.pdfpage(p)), '-l', str(C.pdfpage(p)), C.scan_path(), f + '-tmp'], check=True)
    os.replace(f + '-tmp.png', f + '.png')              # atomic: never a half-written image in the cache
    return f + '.png'
def prerender(pages, dpi):
    """render all missing page images in as few pdftoppm calls as possible (one per run of PDF pages)"""
    need = sorted(C.pdfpage(p) for p in pages if not os.path.exists(os.path.join(OUT, f'{NAME}-p{p}-{dpi}.png')))
    back = {C.pdfpage(p): p for p in pages}
    runs = []
    for q in need:
        if runs and q == runs[-1][1] + 1: runs[-1][1] = q
        else: runs.append([q, q])
    for a, b in runs:
        tmp = os.path.join(OUT, f'{NAME}-batch{dpi}')
        subprocess.run(['pdftoppm', '-r', str(dpi), '-gray', '-png', '-f', str(a), '-l', str(b), C.scan_path(), tmp], check=True)
        for f in glob.glob(tmp + '-*.png'):
            q = int(re.search(r'-(\d+)\.png$', f).group(1))
            os.replace(f, os.path.join(OUT, f'{NAME}-p{back[q]}-{dpi}.png'))
def lines_layer(p):
    x = subprocess.run(['pdftotext', '-bbox', '-f', str(C.pdfpage(p)), '-l', str(C.pdfpage(p)), C.scan_path(), '-'], capture_output=True, text=True).stdout
    ph = float(re.search(r'<page width="[\d.]+" height="([\d.]+)"', x).group(1))
    ws = [(html.unescape(w[4]), tuple(map(float, w[:4]))) for w in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', x)]
    if not getattr(C, 'REORDER', True):
        lines = []
        for w, b in ws:
            if lines and abs((b[1] + b[3]) / 2 - lines[-1][0]) < 0.4 * (b[3] - b[1]) and b[0] > lines[-1][1][-1][1][0]: lines[-1][1].append((w, b))
            else: lines.append([(b[1] + b[3]) / 2, [(w, b)]])
        return [ln for yc, ln in lines], ph
    return cluster(ws), ph
def cluster(ws):
    # the content stream's order may be scrambled and the page skewed or curved: fit skew a and curvature c
    # by the sharpest line histogram, then cluster lines and sort each by x
    xm = sum(b[0] for w, b in ws) / max(1, len(ws))
    yof = lambda b, a, c: (b[1] + b[3]) / 2 - a * b[0] - c * (b[0] - xm) ** 2
    def peak(ac):
        h = {}
        for w, b in ws: k = round(yof(b, *ac)); h[k] = h.get(k, 0) + 1
        return sum(v * v for v in h.values())
    # coarse to fine: skew alone, then curvature at that skew, then skew again (same optimum, ~1/20 the work)
    a = max((k / 500 for k in range(-30, 31)), key=lambda a: peak((a, 0)))
    c = max((k / 1e5 for k in range(-20, 21)), key=lambda c: peak((a, c)))
    for _ in range(2):                             # refine both together around the coarse optimum
        a, c = max(((a + i / 1000, c + k / 2e5) for i in range(-4, 5) for k in range(-6, 7)), key=peak)
    ac = (a, c)
    lh = sorted(b[3] - b[1] for w, b in ws)[len(ws) // 2] if ws else 10
    ws = sorted(ws, key=lambda t: yof(t[1], *ac)); lines = []
    for w, b in ws:
        yc = yof(b, *ac)
        if lines and yc - lines[-1][0] < 0.6 * lh: lines[-1][1].append((w, b))
        else: lines.append([yc, [(w, b)]])
    return [sorted(ln, key=lambda t: t[1][0]) for yc, ln in lines]
def lines_ocr(p):
    d = os.path.join(WORK, 'ocr'); os.makedirs(d, exist_ok=True); f = os.path.join(d, f'p{p}.tsv')
    if not os.path.exists(f):
        prerender([q for q in PAGES if not os.path.exists(os.path.join(d, f'p{q}.tsv'))], DPI)
        r = subprocess.run(['tesseract', render(p, DPI), 'stdout', '-l', LANG, '--dpi', str(DPI), 'tsv'], capture_output=True, text=True)
        if r.returncode: sys.exit('tesseract failed: ' + r.stderr[-500:] + '\n(models: TESSDATA_PREFIX, e.g. brew install tesseract-lang)')
        open(f, 'w', encoding='utf-8').write(r.stdout)
    rows = [r.split('\t') for r in open(f, encoding='utf-8').read().splitlines()[1:]]
    from PIL import Image
    ph = Image.open(render(p, DPI)).height * 72 / DPI; s = 72 / DPI; lines = {}
    good = [r for r in rows if len(r) == 12 and r[0] == '5' and r[11].strip()]
    sure = sorted(int(r[6]) for r in good if float(r[10]) >= 80) or [0]
    sure_r = sorted(int(r[6]) + int(r[8]) for r in good if float(r[10]) >= 80) or [10 ** 6]
    lft, rgt = sure[len(sure) // 50] - 40, sure_r[-len(sure_r) // 50 - 1] + 40          # the text block, in pixels
    for r in good:
        x, y, w, h = map(int, r[6:10])
        if (float(r[10]) < 15 and len(letters(r[11])) < 3) or not lft <= x + w / 2 <= rgt: continue                  # pencil, gutter shadow, specks
        lines.setdefault(0, []).append((r[11], (x * s, y * s, (x + w) * s, (y + h) * s)))
    return cluster(lines.get(0, [])), ph                 # tesseract's own lines split running heads: re-cluster
def furniture(ln, ph, top):
    t = ' '.join(w for w, b in ln); y = ln[0][1][1]
    if top:
        if hasattr(C, 'HEAD'): return re.search(C.HEAD, t)
        return y < 0.15 * ph and len(ln) <= 10 and (any(re.fullmatch(r'[\d.,]+', w) for w, b in ln) or not re.search('[a-zæøåäöü]', t)
                                                       or (re.search(r'[A-ZÆØÅ]{3,}', t) and not re.search('[a-zæøåäöü]{4,}', t)))
    if hasattr(C, 'FOOT'): return re.search(C.FOOT, t)
    return y > 0.85 * ph and len(ln) <= 3 and all(re.fullmatch(r'[\d*†]+\.?|[A-ZÆØÅ]?\d*\*?\.?', w) for w, b in ln)
WP = {}; PH = {}
import json as _json
LCACHE = os.path.join(WORK, f'lines-{WITNESS}'); os.makedirs(LCACHE, exist_ok=True)
STAMP = str(os.path.getmtime(C.scan_path())) + open(os.path.join(CONF, 'pagemap.py')).read() + 'lines-v2'   # bump when the line-building changes
for p in PAGES:
    cf = os.path.join(LCACHE, f'p{p}.json')
    try:
        d = _json.load(open(cf, encoding='utf-8'))
        if d['stamp'] != STAMP: raise ValueError
        lines, PH[p] = [[(w, tuple(b)) for w, b in ln] for ln in d['lines']], d['ph']
    except Exception:
        lines, PH[p] = (lines_ocr if WITNESS == 'ocr' else lines_layer)(p)
        _json.dump({'stamp': STAMP, 'ph': PH[p], 'lines': lines}, open(cf, 'w', encoding='utf-8'), ensure_ascii=False)
    hs = sorted(b[3] - b[1] for ln in lines for w, b in ln); gap = 3 * (hs[len(hs) // 2] if hs else 7)
    def trim(ln):                                        # a short token cut off from the line by a wide gap: a margin mark
        while len(ln) > 1 and ln[1][1][0] - ln[0][1][2] > gap and len(ln[0][0]) <= 3: ln = ln[1:]
        while len(ln) > 1 and ln[-1][1][0] - ln[-2][1][2] > gap and len(ln[-1][0]) <= 3: ln = ln[:-1]
        return ln
    lines = [trim(ln) for ln in lines if ln]
    junk = lambda ln: not re.search('[' + L + ']{3,}', ' '.join(w for w, b in ln))
    while lines and (furniture(lines[0], PH[p], True) or (junk(lines[0]) and lines[0][0][1][1] < 0.2 * PH[p])): lines.pop(0)
    while lines and (furniture(lines[-1], PH[p], False) or (junk(lines[-1]) and lines[-1][0][1][1] > 0.8 * PH[p])): lines.pop()
    ws = [(w, b, n) for n, ln in enumerate(lines) for w, b in ln]
    if ws:                                               # words outside the text block: pencil and specks in the margin
        xs = sorted(b[0] for w, b, n in ws); xe = sorted(b[2] for w, b, n in ws)
        lo, hi = xs[len(xs) // 20] - 15, xe[-len(xe) // 20 - 1] + 15
        ws = [t for t in ws if lo <= (t[1][0] + t[1][2]) / 2 <= hi]
    a, z = CUTS.get(p, (None, None))
    if a: ws = ws[next(k for k, t in enumerate(ws) if t[0].startswith(a)):]
    if z: ws = ws[:max(k for k, t in enumerate(ws) if t[0].startswith(z)) + 1]
    WP[p] = ws
# witness tokens (a hyphen at a line end joins the word), and witness letters with their own page and box
WTOK = []; WL = []; WLP = []
for p in PAGES:
    for k, (w, b, n) in enumerate(WP[p]):
        for ch in w:
            if ISL.match(ch): WL.append(ch); WLP.append((p, b))
        nxt = WP[p][k + 1] if k + 1 < len(WP[p]) else None
        last = nxt is None or nxt[2] != n
        if WTOK and WTOK[-1]['open']:
            WTOK[-1]['t'] = WTOK[-1]['t'][:-1] + w; WTOK[-1]['open'] = False
        elif '\xad' in w and not last: WTOK.append({'t': w.replace('\xad', ''), 'p': p, 'b': b, 'open': False})   # a soft hyphen inside a line
        else: WTOK.append({'t': w, 'p': p, 'b': b, 'open': False})
        if last and len(w) > 1 and w[-1] in '-\xad¬‐' and w[-2].isalpha(): WTOK[-1]['open'] = True
WL = ''.join(WL)

# ======================= alignment ======================================================================
def norm(t):
    t = re.sub('[«»„“”"‚‘’\'`´]', '"', t); t = re.sub('[—–‒―]', '—', t); t = t.replace('…', '...')
    return t
def merge_dots(ts):                     # ". . . ." printed spaced: one token
    out = []
    for t in ts:
        if out and re.fullmatch(r'\.+', t[0]): out[-1] = (out[-1][0] + t[0],) + tuple(out[-1][1:])
        else: out.append(t)
    return out
ET = merge_dots([(t, a, b) for t, a, b in ETOK]); WT = merge_dots([(w['t'], w['p'], w['b']) for w in WTOK])
ops = difflib.SequenceMatcher(None, [norm(t[0]) for t in ET], [norm(t[0]) for t in WT], autojunk=False).get_opcodes()
VOC = set()
for f in glob.glob(os.path.join(ROOT, 'texts', '*', '*', 'transcription.tex')):
    if os.path.dirname(os.path.abspath(f)) == os.path.abspath(BOOK): continue          # never this book's own text
    VOC.update(re.findall('[' + L + ']+', re.sub(r'\\[A-Za-z]+', ' ', open(f, encoding='utf-8', errors='replace').read())))
VOCL = {v.lower() for v in VOC}
att = lambda x: x in VOC or x.lower() in VOCL
FAULT = {('h', 'li'), ('h', 'b'), ('b', 'h'), ('n', 'u'), ('u', 'n'), ('e', 'c'), ('c', 'e'), ('t', 'l'), ('l', 't'), ('f', 't'), ('t', 'f'),
         ('f', 'l'), ('f', 'I'), ('l', 'i'), ('i', 'l'), ('r', 'i'), ('m', 'rn'), ('rn', 'm'), ('m', 'in'), ('in', 'm'), ('ø', 'o'), ('æ', 'se'),
         ('æ', 'ae'), ('D', 'B'), ('B', 'D'), ('B', 'R'), ('R', 'B'), ('I', 'l'), ('l', 'I'), ('0', 'o'), ('o', '0'), ('1', 'l'), ('1', 'I'),
         ('1', 'i'), ('V', 'Y'), ('D', 'H'), ('R', 'H'), ('N', 'H'), ('F', 'E'), ('E', 'F'), ('ü', 'ii'), ('L', 'U'), ('O', '0'), ('C', 'G'),
         ('G', 'C'), ('S', '8'), ('a', 'ä'), ('o', 'ö'), ('u', 'ü'), ('à', 'å'), ('e', 'é'), ('d', 'cl'), ('n', 'ri'), ('y', 'g'), ('g', 'y'),
         ('B', 'TJ'), ('h', 'LJ'), ('F', '7'), ('F', 'T'), ('a', 'n'), ('l', 'J'), ('I', 'l'), ('', 'i'), ('', 'l'), ('', 'I'), ('', 'j'), ('', '1')}
def fault_ok(t, w):
    a, b = letters(t), letters(w)
    if a == b or a.lower() == b.lower(): return a == b
    for op, a1, a2, b1, b2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op != 'equal' and (a[a1:a2], b[b1:b2]) not in FAULT: return False
    return att(a) and not att(b)
NOISE = set('|।"*·\'‘’`^~°¬') 
def denoise(s): return ''.join(ch for ch in s if ch not in NOISE)
STYLE = {}
hunks = []
for op, a1, a2, b1, b2 in ops:
    if op == 'equal':
        for k in range(a2 - a1):                       # quote / dash style, counted, not checked
            x, y = ET[a1 + k][0], WT[b1 + k][0]
            if x != y:
                for u, v in zip(x, y):
                    if u != v: STYLE[(u, v)] = STYLE.get((u, v), 0) + 1
        continue
    if op == 'replace' and a2 - a1 == b2 - b1:
        hunks += [(a1 + k, a1 + k + 1, b1 + k, b1 + k + 1) for k in range(a2 - a1)]
    else: hunks.append((a1, a2, b1, b2))
def htext(h): return ' '.join(t[0] for t in ET[h[0]:h[1]]), ' '.join(t[0] for t in WT[h[2]:h[3]])
settled = {}; moved = set()
for k, h in enumerate(hunks):                           # moves: the same words dropped here and added nearby
    if k in moved: continue
    e, w = htext(h)
    for k2 in range(max(0, k - 8), min(len(hunks), k + 9)):
        if k2 == k or k2 in moved: continue
        e2, w2 = htext(hunks[k2])
        if len(letters(e)) > 1 and letters(e) == letters(w2) and not letters(w) and not letters(e2): moved |= {k, k2}; break
        if len(letters(w)) > 1 and letters(w) == letters(e2) and not letters(e) and not letters(w2): moved |= {k, k2}; break
CHECKS = []; seen = {}
for k, h in enumerate(hunks):
    e, w = htext(h)
    if k in moved: settled['moved'] = settled.get('moved', 0) + 1; continue
    if letters(e) == letters(w) and norm(e).replace(' ', '') == norm(denoise(w)).replace(' ', ''): settled['split/noise'] = settled.get('split/noise', 0) + 1; continue
    if re.fullmatch(r'\S+- (og|eller|samt|el\.|and|et|ou)', e) and letters(e) == letters(w):     # „Følelses- og“ at a line end, joined
        settled['suspended hyphen'] = settled.get('suspended hyphen', 0) + 1; continue
    if not e and not letters(w) and not denoise(w): settled['noise'] = settled.get('noise', 0) + 1; continue
    if e and w and len(e.split()) == len(w.split()) and re.sub('[' + L + ']', '', norm(e)) == re.sub('[' + L + ']', '', norm(denoise(w))) \
            and all(fault_ok(x, y) for x, y in zip(e.split(), w.split())): settled['glyph'] = settled.get('glyph', 0) + 1; continue
    if not e and len(w) == 1 and w in 'ilIj1': settled['noise'] = settled.get('noise', 0) + 1; continue
    a1, a2, b1, b2 = h
    if b1 < len(WT): p, bb = WT[b1][1], WT[b1][2]
    else: p, bb = WT[-1][1], WT[-1][2]
    if b2 == b1 and b1 > 0 and a1 < len(ET):            # transcription has words the witness lacks: box the witness word before
        p, bb = WT[b1 - 1][1], WT[b1 - 1][2]
    s0 = TI[ET[a1][1]][0] if a1 < a2 else (TI[ET[a1][1]][0] if a1 < len(ET) else END)
    s1 = TI[ET[a2 - 1][2] - 1][1] if a1 < a2 else s0
    key = f'{p}|{e}>{w}'; seen[key] = seen.get(key, 0) + 1
    if seen[key] > 1: key += f'#{seen[key]}'
    CHECKS.append({'key': key, 'p': p, 'b': bb, 'e': e, 'w': w, 's0': s0, 's1': s1,
                   'ctx': T[max(0, ET[a1][1] - 40) if a1 < len(ET) else -40: (ET[a1][1] if a1 < len(ET) else len(T))] + '[' + e + ']'})
DEC = {}
f = os.path.join(CONF, 'decisions.tsv')
if os.path.exists(f):
    for ln in open(f, encoding='utf-8'):
        if ln.strip() and not ln.startswith('#') and '\t' in ln:
            k, d = ln.rstrip('\n').split('\t')[:2]; DEC[k] = d
OPEN = [c for c in CHECKS if c['key'] not in DEC or DEC[c['key']] == '?']
for n, c in enumerate(OPEN): c['id'] = f'C{n + 1:03d}'
print(f'{NAME}: witness {WITNESS}, pp. {PAGES[0]}-{PAGES[-1]}; {len(ET)} words / {len(WT)} witness words; '
      f'{len(hunks)} disagreements: settled by rule {sum(settled.values())} {settled}, decided {len(CHECKS) - len(OPEN)}, OPEN {len(OPEN)}')
if STYLE: print('quote/dash style (transcription>witness, not checked):', ', '.join(f'{u}>{v}:{n}' for (u, v), n in sorted(STYLE.items(), key=lambda x: -x[1])[:12]))
with open(os.path.join(WORK, 'checks.tsv'), 'w', encoding='utf-8') as fh:
    for c in OPEN: fh.write(f"{c['id']}\t{c['key']}\t{c['ctx']}\n")
if not any(a in ARGS for a in ('--sheets', '--italics', '--pages', '--apply', '--mark')):
    for c in OPEN: print(f"{c['id']}  {c['key']}")

# ======================= crops ==========================================================================
def crop_sheets(items, tag):
    from PIL import Image, ImageDraw, ImageFont
    prerender(sorted({c['p'] for c in items}), 200)
    try: font = ImageFont.truetype('DejaVuSans.ttf', 18)
    except OSError:
        fp = subprocess.run(['fc-match', '-f', '%{file}', 'DejaVu Sans'], capture_output=True, text=True).stdout
        font = ImageFont.truetype(fp, 18) if fp else ImageFont.load_default()
    imgs = {}; crops = []
    for c in items:
        p = c['p']
        if p not in imgs: imgs[p] = Image.open(render(p, 200)).convert('L')
        im = imgs[p]; sc = im.height / PH[p]; x0, y0, x1, y1 = c['b']; lh = max(8, y1 - y0)
        xs = sorted(b[0] for w, b, n in WP[p]); xe = sorted(b[2] for w, b, n in WP[p])
        L0, R0 = xs[len(xs) // 20] - 6, xe[-len(xe) // 20 - 1] + 6
        cr = im.crop((int(L0 * sc), max(0, int((y0 - 1.7 * lh) * sc)), int(R0 * sc), int((y1 + 1.7 * lh) * sc))).convert('RGB')
        ImageDraw.Draw(cr).rectangle((int((x0 - L0) * sc) - 2, int(1.7 * lh * sc) - 2, int((x1 - L0) * sc) + 2, int((1.7 * lh + y1 - y0) * sc) + 2), outline=(220, 0, 0), width=2)
        if cr.width > 1100: cr = cr.resize((1100, int(cr.height * 1100 / cr.width)))
        lab = Image.new('RGB', (cr.width, 26), 'white')
        ImageDraw.Draw(lab).text((4, 3), f"{c['id']}  p.{p}   T: {c['e'] or '∅'}   |   W: {c['w'] or '∅'}", fill=(0, 0, 0), font=font)
        b = Image.new('RGB', (cr.width, cr.height + 26), 'white'); b.paste(lab, (0, 0)); b.paste(cr, (0, 26)); crops.append(b)
    names = []
    for k in range(0, len(crops), 10):
        g = crops[k:k + 10]; sh = Image.new('RGB', (max(x.width for x in g), sum(x.height + 6 for x in g)), (190, 190, 190)); y = 0
        for x in g: sh.paste(x, (0, y)); y += x.height + 6
        n = os.path.join(OUT, f'{NAME}-{tag}{k // 10 + 1:02d}.png'); sh.save(n); names.append(n)
    print('sheets:', ' '.join(os.path.relpath(n, ROOT) for n in names))
if '--sheets' in ARGS and OPEN: crop_sheets(OPEN, 'c')

# ======================= italics by stroke slant ========================================================
if '--italics' in ARGS:
    import numpy as np
    from PIL import Image
    def sharp(a, sh):                                   # column profile of the sheared word image, squared
        h, w = a.shape; off = h + np.round(sh * (h - np.arange(h))).astype(int)
        prof = np.bincount((off[:, None] + np.arange(w)[None, :]).ravel(), weights=a.ravel(), minlength=w + 2 * h + 2)
        return (prof ** 2).sum()
    hs = sorted(t[2][3] - t[2][1] for t in WT); IDPI = int(min(300, max(100, 30 * 72 / hs[len(hs) // 2])))
    print(f'italics: rendering at {IDPI} dpi (median word height {hs[len(hs) // 2]:.1f} pt -> 30 px)')
    prerender(PAGES, IDPI)
    score = []                                           # per witness token: slant score of its first word box
    imgs = {}
    for t in WT:
        p, (x0, y0, x1, y1) = t[1], t[2]
        if p not in imgs: imgs[p] = np.asarray(Image.open(render(p, IDPI)).convert('L'), dtype=float)
        im = imgs[p]; s = IDPI / 72
        a = (im[int(y0 * s): int(y1 * s), int(x0 * s): int(x1 * s)] < 128).astype(float)
        score.append(sharp(a, -0.1) / sharp(a, 0.0) if a.sum() else 1.0)
    ital = [score[k] >= ITAL and len(letters(t[0])) >= 3 for k, t in enumerate(WT)]
    for k in range(1, len(WT) - 1):                      # a short word between italic words is italic
        if len(letters(WT[k][0])) < 3 and ital[k - 1] and ital[k + 1]: ital[k] = True
    q = sorted(score); print('slant scores: median %.2f, 90%% %.2f, 99%% %.2f; italic from %.2f' % (q[len(q) // 2], q[int(.9 * len(q))], q[int(.99 * len(q))], ITAL))
    emph = lambda t: sum(TI[i][2] for i in range(t[1], t[2]) if ISL.match(T[i])) * 2 > max(1, len(letters(t[0])))
    runs = []
    for op, a1, a2, b1, b2 in ops:
        if op != 'equal': continue
        for k in range(a2 - a1):
            et, wt = ET[a1 + k], WT[b1 + k]
            if len(letters(et[0])) < 3 and not ital[b1 + k]: continue          # short roman words decide nothing
            mism = ital[b1 + k] != emph(et)
            if mism and runs and runs[-1]['b_end'] == b1 + k and runs[-1]['it'] == ital[b1 + k]:
                runs[-1]['b_end'] += 1; runs[-1]['e'] += ' ' + et[0]; runs[-1]['s1'] = TI[et[2] - 1][1]
            elif mism:
                runs.append({'b_end': b1 + k + 1, 'it': ital[b1 + k], 'e': et[0], 'p': wt[1], 'b': wt[2], 's0': TI[et[1]][0], 's1': TI[et[2] - 1][1]})
    IOPEN = []
    for r in runs:
        if len(r['e'].split()) == 1 and len(letters(r['e'])) < 4 and r['it']: continue   # lone short slant: the tail of a g, an f
        r['key'] = f"E{r['p']}|{r['e']}>{'italic' if r['it'] else 'roman'}"; r['w'] = 'italic' if r['it'] else 'roman'
        if r['key'] not in DEC or DEC[r['key']] == '?': IOPEN.append(r)
    for n, r in enumerate(IOPEN): r['id'] = f'I{n + 1:03d}'; print(f"{r['id']}  {r['key']}")
    print(f'italics: {len(runs)} mismatches, OPEN {len(IOPEN)}')
    if IOPEN: crop_sheets(IOPEN, 'i')
    CHECKS += runs

# ======================= page turns ======================================================================
def align_letters():
    ecs = [i for i in range(len(T)) if ISL.match(T[i])]; es = ''.join(T[i] for i in ecs)
    opsl = []; i0 = j0 = 0
    while j0 < len(WL):
        lw = WL[j0: j0 + 3000]; last = j0 + len(lw) >= len(WL); ew = es[i0:] if last else es[i0: i0 + 3600]
        oc = difflib.SequenceMatcher(None, ew, lw, autojunk=False).get_opcodes()
        if not last:
            cut = 2 * len(lw) // 3
            k = max(n for n, x in enumerate(oc) if x[0] == 'equal' and x[3] + 8 <= cut)
            op, a1, a2, b1, b2 = oc[k]; m = min(b2, cut) - b1; oc = oc[:k] + [(op, a1, a1 + m, b1, b1 + m)]
        opsl += [(op, i0 + a1, i0 + a2, j0 + b1, j0 + b2) for op, a1, a2, b1, b2 in oc]
        i0, j0 = i0 + oc[-1][2], j0 + oc[-1][4]
        if last: break
    first = {}
    for j, (p, b) in enumerate(WLP): first.setdefault(p, j)
    start = {}
    for op, a1, a2, b1, b2 in opsl:
        # a long stretch only the transcription has (the run-over part of a footnote, which the scan prints at
        # the next page's foot) is not where a page starts: the page starts after it
        if b2 == b1 and a2 - a1 > 10: continue
        for p, j in first.items():
            if p not in start and b1 <= j < max(b2, b1 + 1): start[p] = ecs[min(len(ecs) - 1, a1 + (j - b1 if op == 'equal' else 0))]
    return start                                         # page -> index in T of its first letter
if '--pages' in ARGS or '--mark' in ARGS:
    PS = align_letters()
    if '--pages' in ARGS:
        ok = 0
        for p in sorted(PS):
            mi = MARKI.get(p); d = None
            if mi is not None: d = len(letters(T[min(mi, PS[p]):max(mi, PS[p])])) * (1 if mi > PS[p] else -1)
            if d == 0: ok += 1; continue
            print(f'p.{p}: marker {"missing" if d is None else f"off by {d:+d} letters"}   page begins: …{T[max(0, PS[p] - 30):PS[p]]}‖{T[PS[p]:PS[p] + 30]}…')
        print(f'{ok} of {len(PS)} page markers exact')

# ======================= apply decisions =================================================================
def backup(tag):
    b = TEX + f'.bak.{datetime.date.today():%Y%m%d}-{tag}'; n = 1
    while os.path.exists(b): n += 1; b = TEX + f'.bak.{datetime.date.today():%Y%m%d}-{tag}{n}'
    shutil.copy2(TEX, b); return b
if '--apply' in ARGS:
    edits = []; manual = []
    for c in CHECKS:
        d = DEC.get(c['key'])
        if not d or d in ('T', '?'): continue
        span = SRC[c['s0']:c['s1']]
        if c['key'].startswith('E'):
            if d != 'W': continue
            if c['w'] == 'italic' and not re.search(r'[\\{}%]', span): edits.append((c['s0'], c['s1'], '\\emph{' + span + '}', None))
            elif c['w'] == 'roman' and SRC[c['s0'] - 6:c['s0']] == '\\emph{' and SRC[c['s1']:c['s1'] + 1] == '}': edits.append((c['s0'] - 6, c['s1'] + 1, span, None))
            else: manual.append(c['key'])
            continue
        new = d[1:] if d.startswith('=') else c['w']
        if re.search(r'[\\{}%"`\'„“”»«]', span + new) or (not c['e'] and not new): manual.append(c['key']); continue
        if not c['e']: new += ' '
        elif not new:                                    # drop the words and one space
            if SRC[c['s1']:c['s1'] + 1] == ' ': c['s1'] += 1
        edits.append((c['s0'], c['s1'], new, f"„{c['w']}“" if d == 'P' else None))
    if edits:
        print('backup:', os.path.relpath(backup('collate'), ROOT)); S = SRC
        for s0, s1, new, pai in sorted(edits, reverse=True):
            S = S[:s0] + new + S[s1:]
            if pai: e = S.index('\n', s0); S = S[:e] + f' % PRINTED AS IS: {pai}' + S[e:]
        open(TEX, 'w', encoding='utf-8').write(S)
    print(f'applied {len(edits)}; by hand (markup, quotes or a deletion in the span): {len(manual)}')
    for k in manual: print('  MANUAL', k)

# ======================= page markers at the exact turns =================================================
if '--mark' in ARGS:
    # only the markers that are off (or missing) are touched; exact ones stay as they are
    OFFP = []
    for p, ti in PS.items():
        mi = MARKI.get(p)
        if mi is None or letters(T[min(mi, ti):max(mi, ti)]): OFFP.append(p)
    if '--only' in ARGS:                       # --only 47,52,88: move just these (after checking the others are artifacts)
        keep = {int(x) for x in opt('--only').split(',')}; OFFP = [p for p in OFFP if p in keep]
    if '--except' in ARGS:
        drop = {int(x) for x in opt('--except').split(',')}; OFFP = [p for p in OFFP if p not in drop]
    # 1. take those pages' old markers out, keeping a map from old offsets to new
    pat = '|'.join(rf'%\n% --- p\. {p} ---[^\n]*\n\\opage\{{{p}\}}|^% --- p\. {p} ---[^\n]*\n|\\opage\{{{p}\}} ?| ?\\apage\{{{p}\}} ?' for p in OFFP) or '(?!)'
    S = []; last = 0; cuts = []
    for m in re.finditer('(?m)' + pat, SRC):
        rep = ' ' if 'apage' in m.group(0) and m.group(0).startswith(' ') and m.group(0).endswith(' ') else ''
        S.append(SRC[last:m.start()]); S.append(rep); cuts.append((m.start(), m.end(), len(rep))); last = m.end()
    S.append(SRC[last:]); S = ''.join(S)
    def newpos(o):
        d = 0
        for a, b, r in cuts:
            if a >= o: break
            d += (b - a) - r
        return o - d
    # 2. put each of those pages' markers where the witness says the page begins
    ins = []
    for p in OFFP:
        o = newpos(TI[PS[p]][0]); ls = S.rfind('\n', 0, o) + 1; le = S.find('\n', o); line = S[ls:le]
        cb, ce = S.rfind('\\begin{center}', 0, o), S.rfind('\\end{center}', 0, o)
        k = o - 1
        while k > ls and S[k] in ' \t': k -= 1
        if S[k] == '{' and not (re.match(r'\s*\\(section|subsection|chapter)', line) or cb > ce):   # inside a command's argument
            c = S.rfind('\\', ls, k); ins += [(c, c, f'\\opage{{{p}}}')]
            if not S[ls:c].strip(): ins.append((ls, ls, f'% --- p. {p} ---\n'))
        elif re.match(r'\s*\\(section|subsection|chapter)', line) or cb > ce:
            h = cb if cb > ce else ls
            n = S.index('\\end{center}', o) + 12 if cb > ce else le
            while True:                                   # past the heading's own lines to the first text
                while n < len(S) and S[n] in ' \t\n': n += 1
                m = re.match(r'\\(addcontentsline|label|vspace|bigskip|medskip|smallskip)\*?(\{[^}]*\})*', S[n:])
                if not m: break
                n += len(m.group(0))
            if S.startswith('\\noindent', n): n += len('\\noindent'); n += 1 if S[n] == ' ' else 0
            ins += [(h, h, f'% --- p. {p} ---\n'), (n, n, f'\\opage{{{p}}}')]
        elif ISL.match(S[o - 1]): ins.append((o, o, f'%\n% --- p. {p} ---\n\\opage{{{p}}}'))
        else:
            a = o
            while S[a - 1] in ' \n': a -= 1
            ins.append((a, o, f'\n% --- p. {p} ---\n\\opage{{{p}}}'))
    for a, b, t in sorted(ins, reverse=True): S = S[:a] + t + S[b:]
    if not re.search(r' +\n', SRC): S = re.sub(r' +\n', '\n', S)
    if '\\newcommand{\\opage}' not in S:
        S = S.replace('\\begin{document}', '\\newcommand{\\opage}[1]{\\marginnote{\\footnotesize\\textit{[#1]}}}\n\\begin{document}', 1)
    print('--mark: pages moved or added:', OFFP)
    out = os.path.join(WORK, 'transcription.marked.tex'); open(out, 'w', encoding='utf-8').write(S)
    ch = sum(1 for x in difflib.unified_diff(SRC.splitlines(), S.splitlines(), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---'))
    print(f'--mark: {ch} lines differ; dry run in {os.path.relpath(out, ROOT)}')
    if '--write' in ARGS:
        print('backup:', os.path.relpath(backup('mark'), ROOT)); open(TEX, 'w', encoding='utf-8').write(S); print('transcription.tex rewritten')
