#!/usr/bin/env python3
"""
build.py -- Erkendelsesteori og Livsopfattelse, pp. FIRST..122, by the E-BOOK METHOD
(TRANSCRIPTION-PLAYBOOK §00 point 0). No agent types text.

  e-book (SAGA, same 1925 text)  = base text, paragraphing, italics, note texts, note anchors
  PDF text layer (ABBYY, 1925)   = page boundaries (\\apage), small caps (ALL-CAPS words),
                                   and the second witness for every word

Every place the two disagree and no rule settles it becomes a CHECK item with a crop of
the print; decisions (print governs) are read from decisions.tsv on the next run.

  python3 .parts/ebook/build.py            -> .parts/ebook/out.texfrag, checks.json, crops/
  python3 .parts/ebook/build.py --apply    -> same, applying .parts/ebook/decisions.tsv
"""
import zipfile, re, html, difflib, subprocess, sys, os, json, glob
HERE = os.path.dirname(os.path.abspath(__file__))     # ebook-method/<book>/: scripts and the decisions (tracked)
BOOK = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'texts', 'hoeffding', os.path.basename(HERE))
WORK = os.path.join(BOOK, '.parts', 'ebook'); os.makedirs(WORK, exist_ok=True)   # scratch output (gitignored)
sys.path.insert(0, HERE); from pagemap import pdfpage, scan_path
FIRST, LAST, ALIGN_FROM = 63, 122, 48
EPUB = os.path.join(BOOK, 'Erkendelsesteori_og_livsopfattelse.epub')
WRE = r"[0-9A-Za-zÀ-ÖØ-öø-ÿ'’]+"
z = zipfile.ZipFile(EPUB)

# ---------- e-book: event stream ----------
def events(name):
    s = z.read(name).decode('utf-8'); s = s[s.index('<body'):]
    out = []
    for m in re.finditer(r'<h1[^>]*>(.*?)</h1>|<p\b[^>]*>|</p>|<i>|</i>|<span class="text-small-rw">|'
                         r'<span class="ref-note-rw"[^>]*><a [^>]*>(\d+)</a></span>|<a [^>]*noteref[^>]*>(\d+)</a>|<[^>]+>|([^<]+)', s, re.S):
        g = m.group(0)
        if m.group(1) is not None: out.append(('head', html.unescape(re.sub(r'<[^>]+>', ' ', m.group(1))).strip()))
        elif g.startswith('<p'): out.append(('pbeg',))
        elif g == '</p>': out.append(('pend',))
        elif g == '<i>': out.append(('ion',))
        elif g == '</i>': out.append(('ioff',))
        elif g.startswith('<span class="text-small'): out.append(('small',))
        elif m.group(2) or m.group(3): out.append(('note', int(m.group(2) or m.group(3))))
        elif m.group(4) is not None: out.append(('text', html.unescape(m.group(4))))
    return out
EV = []
for n in sorted(z.namelist()):
    if re.search(r's00[6-9]-Chapter', n): EV += events(n)
notes = {}
s = z.read([n for n in z.namelist() if 'Notes' in n][0]).decode('utf-8')
for m in re.finditer(r'<p id="[^"]*" epub:type="rearnote">(.*?)</p>', s, re.S):
    b = m.group(1); k = int(re.search(r'rw-num-note-(\d+)', b).group(1))
    b = re.sub(r'<span class="num-note-rw".*?</span>', '', b, flags=re.S)
    notes[k] = b
# flatten e-book body into tokens: ('w', word) | ('s', other text) | markup events
TOK = []
for e in EV:
    if e[0] == 'text':
        for m in re.finditer(WRE + r'|[^0-9A-Za-zÀ-ÖØ-öø-ÿ\'’]+', e[1]):
            TOK.append(('w' if re.fullmatch(WRE, m.group(0)) else 's', m.group(0)))
    else: TOK.append(e)
ewi = [i for i, t in enumerate(TOK) if t[0] == 'w']
ew = [TOK[i][1].replace('’', "'") for i in ewi]

# ---------- layer: words with page + bbox, running heads dropped, hyphens joined ----------
HEAD = re.compile(r'^\s*(\d{1,3}\s*)?(Nr\.\s*1\.\s*Harald\s*H[oø]ffding:?|Erkendelsesteori\s+og\s+Livsopfattelse\.?)?\s*(\d{1,3})?\s*$')
LW = []   # dicts: w, page, bbox, caps
for p in range(ALIGN_FROM, LAST + 1):
    x = subprocess.run(['pdftotext', '-bbox-layout', '-f', str(pdfpage(p)), '-l', str(pdfpage(p)), scan_path(), '-'],
                       capture_output=True, text=True).stdout
    lines = re.findall(r'<line[^>]*>(.*?)</line>', x, re.S)
    words_by_line = [re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', l) for l in lines]
    words_by_line = [wl for wl in words_by_line if wl]
    if words_by_line and HEAD.match(' '.join(html.unescape(w[4]) for w in words_by_line[0])):
        words_by_line = words_by_line[1:]
    flat = []
    for wl in words_by_line:
        for (x0, y0, x1, y1, t) in wl:
            t = html.unescape(t)
            flat.append({'t': t, 'page': p, 'bbox': (float(x0), float(y0), float(x1), float(y1))})
    i = 0
    while i < len(flat):
        f = flat[i]
        if (f['t'].endswith('­') or (f['t'].endswith('-') and len(f['t']) > 1)) and i + 1 < len(flat):
            f = dict(f); f['t'] = f['t'].rstrip('­-') + flat[i+1]['t']; f['bbox2'] = flat[i+1]['bbox']; i += 1
        for m in re.finditer(WRE, f['t']):
            w = m.group(0).replace('’', "'")
            mm = re.fullmatch(r"(.*[A-Za-zÀ-ÖØ-öø-ÿ])(\d{1,2})", w)     # trailing note numeral
            if mm: w = mm.group(1)
            LW.append({'w': w, 'page': p, 'bbox': f['bbox'], 'bbox2': f.get('bbox2')})
        i += 1
lw = [d['w'] for d in LW]

# ---------- vocabulary of the period, from the repo's transcriptions ----------
VOC = set()
for f in glob.glob(os.path.join(BOOK, '..', '..', '*', '*', 'transcription.tex')):
    if os.path.samefile(os.path.dirname(f), BOOK): continue      # never this book's own output (2026-10-02)
    VOC.update(re.findall(WRE, re.sub(r'\\[A-Za-z]+', ' ', open(f, encoding='utf-8', errors='replace').read())))
KNOWN = {('at', 'al'), ('det', 'del'), ('et', 'el'), ('dets', 'dels'), ('Det', 'Del'), ('sit', 'sil'), ('har', 'liar'),
         ('hvem', 'livem'), ('hvorpaa', 'livorpaa'), ('flere', 'liere'), ('flere', 'tiere')}

def ocr_fault(e, l):
    # True if the layer word l is the e-book word e damaged by the layer's known confusions
    pats = [('t', 'l'), ('f', 'l'), ('f', 't'), ('f', 'i'), ('h', 'li'), ('h', 'b'), ('n', 'u'), ('e', 'c'), ('t', 'f'), ('ø', 'o')]
    if len(e) < 2: return False
    sm2 = difflib.SequenceMatcher(None, e, l, autojunk=False)
    for op, a1, a2, b1, b2 in sm2.get_opcodes():
        if op == 'equal': continue
        if op != 'replace' or (e[a1:a2], l[b1:b2]) not in pats: return False
    return True
JUNK = re.compile(r"^(['\d ]+|Nr 1 H ?arald H ?øffding|Erkendelse[a-z]* og Livsopfattelse|\d{1,3})$")
# ---------- align body ----------
sm = difflib.SequenceMatcher(None, ew, lw, autojunk=False)
dec = {}
if '--apply' in sys.argv and os.path.exists(os.path.join(HERE, 'decisions.tsv')):
    for l in open(os.path.join(HERE, 'decisions.tsv'), encoding='utf-8'):
        if l.strip() and not l.startswith('#'):
            cid, txt = l.rstrip('\n').split('\t')[:2]; dec[cid] = txt
emap = {}          # e-book word index -> layer index (aligned)
repl = {}          # e-book token index -> replacement text (from rules/decisions)
checks = []; sc = set()
IDMAP = {}
if os.path.exists(os.path.join(HERE, 'checks-v1.json')):
    IDMAP = {(c['kind'], c['e_i1'], c['e_i2']): c['id'] for c in json.load(open(os.path.join(HERE, 'checks-v1.json')))}
def check(kind, e_i1, e_i2, l_j1, l_j2, ewords, lwords):
    j = l_j1 if l_j1 < len(LW) else len(LW) - 1
    key = (kind, e_i1, e_i2); cid = IDMAP.get(key) or f'D{len(checks)+1:03d}'   # keep the 2026-10-01 ids
    checks.append({'id': cid, 'kind': kind, 'page': LW[j]['page'], 'ebook': ewords, 'layer': lwords,
                   'ctx': ' '.join(ew[max(0, e_i1-6):e_i1]) + ' ⟪' + ewords + '⟫ ' + ' '.join(ew[e_i2:e_i2+6]),
                   'bbox': LW[j]['bbox'], 'e_i1': e_i1, 'e_i2': e_i2})
    return cid
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal':
        for k in range(i2 - i1): emap[i1 + k] = j1 + k
        continue
    if op == 'replace' and i2 - i1 == j2 - j1:
        for k in range(i2 - i1):
            e, l = ew[i1+k], lw[j1+k]; emap[i1+k] = j1+k
            if l.isupper() and len(l) > 1 and l.lower() == e.lower(): sc.add(i1+k); continue      # small caps in print
            if (e, l) in KNOWN or (l not in VOC and e in VOC) or (e in VOC and ocr_fault(e, l)) or (e, l) in {('Smlgn', 'Smign'), ('I', '1'), ('II', 'Il')}: continue   # layer's own fault
            cid = check('word', i1+k, i1+k+1, j1+k, j1+k+1, e, l)
            if cid in dec: repl[ewi[i1+k]] = dec[cid]
        continue
    if op == 'insert' and JUNK.match(' '.join(lw[j1:j2])): continue          # running head, folio, note numerals
    if op == 'replace' and ''.join(ew[i1:i2]).replace("'", '') == ''.join(lw[j1:j2]).replace("'", ''):
        continue                                                                     # spacing only
    if op == 'insert':
        if j2 - j1 <= 6 and all(LW[j]['page'] == LW[j1]['page'] for j in range(j1, j2)):
            cid = check('layer-only', i1, i1, j1, j2, '', ' '.join(lw[j1:j2]))
            if cid in dec and dec[cid] not in ('', '-'): repl[ewi[i1] if i1 < len(ewi) else ewi[-1]] = dec[cid] + ' ' + TOK[ewi[i1]][1]
        continue
    cid = check(op, i1, i2, j1, j2, ' '.join(ew[i1:i2]), ' '.join(lw[j1:j2]))
    if cid in dec:
        repl[ewi[i1]] = dec[cid]
        for k in range(i1 + 1, i2): repl[ewi[k]] = ''
# page starts: first layer word of each page -> nearest aligned e-book word at/after it
rev = {}
for e, l in emap.items(): rev.setdefault(l, e)
pstart = {}
for p in range(FIRST, LAST + 1):
    js = [j for j, d in enumerate(LW) if d['page'] == p]
    for j in js:
        if j in rev: pstart[p] = rev[j]; break
# ---------- emit LaTeX ----------
def esc(s):
    s = s.replace('\\', r'\textbackslash{}')
    for a, b in [('&', r'\&'), ('%', r'\%'), ('$', r'\$'), ('#', r'\#'), ('_', r'\_'), ('{', r'\{'), ('}', r'\}')]: s = s.replace(a, b)
    return s.replace('—', '---').replace('–', '--').replace('’', "'").replace('‘', "'").replace(' ', ' ').replace('…', '...')
def quotes(s):
    out = []; 
    for i, c in enumerate(s):
        if c in '"»«“”„':
            prev = s[i-1] if i else ' '; nxt = s[i+1] if i + 1 < len(s) else ' '
            opening = c in '»„“' or (c == '"' and (prev in ' (\n' and nxt not in ' \n'))
            out.append(r'\guillemotright{}' if opening else r'\guillemotleft{}')
        else: out.append(c)
    return ''.join(out)
def notetext(k):
    b = notes[k]
    b = re.sub(r'<i>(.*?)</i>', lambda m: '\x01' + html.unescape(m.group(1)) + '\x02', b, flags=re.S)
    b = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', b))).strip()
    t = quotes(esc(b)).replace('\x01', r'\textit{').replace('\x02', '}')
    return t
start_tok = ewi[pstart[FIRST]]
_prev = max(i for i in ewi if i < start_tok)
print('p.%d opens a new paragraph:' % FIRST, any(t[0] == 'pbeg' for t in TOK[_prev:start_tok]))
out = []; pend_page = {ewi[e]: p for p, e in pstart.items()}
in_i = False; para_open = False; seen_text = False; wi = 0
eword_index = {t: i for i, t in enumerate(ewi)}
cur = []
for ti, t in enumerate(TOK):
    if ti < start_tok:
        if t[0] == 'ion': in_i = True
        if t[0] == 'ioff': in_i = False
        continue
    if ti == start_tok and in_i: cur.append(r'\textit{')
    if ti in pend_page:
        p = pend_page[ti]
        cur.append(f'\n% --- p. {p} ---\n\\setcounter{{footnote}}{{0}}%\n\\apage{{{p}}}')
    k = t[0]
    if k == 'head':
        cur.append('\n\n' + r'\section*{' + esc(t[1]).replace('. ', '.\\ ', 1) + '}\n' +
                   r'\addcontentsline{toc}{section}{' + esc(t[1].rstrip('. ')).replace('. ', '.\\ ', 1) + '}\n')
    elif k == 'pbeg': cur.append('\n\n')
    elif k == 'pend': pass
    elif k == 'ion': cur.append(r'\textit{'); in_i = True
    elif k == 'ioff': cur.append('}'); in_i = False
    elif k == 'small': cur.append('% (set in smaller type in the print)\n')
    elif k == 'note': cur.append(r'\footnote{' + notetext(t[1]) + '}')
    elif k == 'w':
        w = repl.get(ti, t[1])
        e = eword_index[ti]
        if e in sc and w: w = r'\textsc{' + w + '}'
        cur.append(esc(w) if '\\textsc' not in w else w)
    elif k == 's': cur.append(quotes(esc(t[1])))
txt = ''.join(cur)
txt = re.sub(r'[ \t]+\n', '\n', txt); txt = re.sub(r'\n{3,}', '\n\n', txt)
# wrap long lines at spaces (~80 cols), never inside a command
lines = []
for para in txt.split('\n'):
    while len(para) > 85:
        cut = para.rfind(' ', 0, 80)
        if cut <= 0: break
        lines.append(para[:cut]); para = para[cut+1:]
    lines.append(para)
open(os.path.join(WORK, 'out.texfrag'), 'w', encoding='utf-8').write('\n'.join(lines).strip() + '\n')
json.dump([c for c in checks if c['page'] >= FIRST], open(os.path.join(WORK, 'checks.json'), 'w'), ensure_ascii=False, indent=0)
n = [c for c in checks if c['page'] >= FIRST]
print('pages with markers:', sorted(pstart)[:3], '...', len(pstart), '| checks (p>=%d):' % FIRST, len(n),
      '| by kind:', {k: sum(1 for c in n if c['kind'] == k) for k in set(c['kind'] for c in n)}, '| small caps:', len(sc))
