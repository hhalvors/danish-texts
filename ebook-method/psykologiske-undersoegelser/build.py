#!/usr/bin/env python3
"""
build.py -- Harald Høffding, PSYKOLOGISKE UNDERSØGELSER (Vidensk. Selsk. Skr. 6. R., hist.-philos. Afd.
III. 1, 1889): the Danish transcription by the E-BOOK METHOD (TRANSCRIPTION-PLAYBOOK §00 point 0).
Copied 2026-10-09 from ../danske-filosoffer/build.py (same SAGA e-book markup; footnotes at the page foot
in the print, endnotes in the e-book); settings changed: the e-book file, FIRST/LAST, the Indledning
(s003-Introduction) in the body stream, and SIG (the Academy's sheet-foot series line).

    python3 build.py           align and list what needs the image (checks.json, punct.json, paras.json)
    python3 build.py --emit    also write ../../transcription.tex (refuses while a check is undecided)

Witnesses: the SAGA / Lindhardt og Ringhof e-book (Psykologiske_undersoegelser.epub, 2023; base text,
paragraphs, italics, notes; pp. 5-103 complete -- the title p. 1 and the Indhold p. 3 are in template.tex)
and Google's scan's text layer (letters,
page turns, letterspacing, footnote placement). The layer is split per page by type size: body
lines vs. the smaller footnote lines at the page foot; each is aligned with its e-book stream
(text / notes) letter by letter in windows. What no rule settles is decided at the image
(sheets.py --todo -> decisions.tsv / patches.tsv), print governing, misprints kept.
"""
import zipfile, re, html, difflib, subprocess, sys, os, json, glob, statistics
HERE = os.path.dirname(os.path.abspath(__file__))     # ebook-method/<book>/: scripts and the decisions (tracked)
BOOK = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'texts', 'hoeffding', os.path.basename(HERE))
WORK = os.path.join(BOOK, '.parts', 'ebook'); os.makedirs(WORK, exist_ok=True)   # scratch output (gitignored)
sys.path.insert(0, HERE); from pagemap import pdfpage, scan_path
z = zipfile.ZipFile(os.path.join(BOOK, 'Psykologiske_undersoegelser.epub'))
L = 'A-Za-zÀ-ÖØ-öø-ÿ0-9'; ISL = re.compile('[' + L + ']')
FIRST, LAST = 5, 103                     # the e-book's text covers pp. 5-103 (Indledning to the end)

# ---------------- e-book ----------------
def events(name):
    s = z.read(name).decode('utf-8'); s = s[s.index('<body'):]
    out = []; stack = []
    clean = lambda x: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', x))).strip()
    for m in re.finditer(r'<h([1-3])[^>]*>(.*?)</h\1>|<p class="title-sub-rw"[^>]*>(.*?)</p>|'
                         r'<p class="decoration-rw"[^>]*>.*?</p>|<p\b[^>]*>|<i>|</i>|<span class="([a-z-]+)"[^>]*>|</span>|'
                         r'<a [^>]*>(\d+)</a>|<[^>]+>|([^<]+)', s, re.S):
        g = m.group(0)
        if m.group(1): out.append(({'1': 'head', '2': 'h2', '3': 'h3'}[m.group(1)], clean(m.group(2))))
        elif m.group(3) is not None: out.append(('sub', clean(m.group(3))))
        elif g.startswith('<p class="decoration'): out.append(('deco',))
        elif g.startswith('<p'): out.append(('pbeg',))
        elif g == '<i>': out.append(('ion',))
        elif g == '</i>': out.append(('ioff',))
        elif m.group(4):
            k = {'smallcaps-rw': 'sc', 'subscript-rw': 'sb', 'superscript-rw': 'sp', 'ref-note-rw': 'ref', 'num-note-rw': 'num'}.get(m.group(4), 'other')
            stack.append(k)
            if k in ('sc', 'sb', 'sp'): out.append((k + 'on',))
        elif g == '</span>':
            k = stack.pop() if stack else 'other'
            if k in ('sc', 'sb', 'sp'): out.append((k + 'off',))
        elif m.group(5):
            out.append(('note' if stack and stack[-1] == 'ref' else 'nnum', int(m.group(5))))
        elif m.group(6) is not None:
            for k, part in enumerate(re.sub(r'\s+', ' ', html.unescape(m.group(6))).split('•')):
                if k: out.append(('pbeg',))
                if part: out.append(('text', part))
    return out
HEADS = ('head', 'sub', 'h2', 'h3')
def stream(EV):
    TOK = []
    for e in EV:
        if e[0] == 'text':
            for m in re.finditer('[' + L + "'’]+|[^" + L + "'’]+", e[1]):
                TOK.append(('w' if ISL.search(m.group(0)) else 's', m.group(0)))
        else: TOK.append(e)
    ecs = []; etok = []; efull = []; epos = []; n = 0
    for i, t in enumerate(TOK):
        if t[0] in ('w', 's') + HEADS:
            txt = t[1] + (' ' if t[0] in HEADS else '')
            for ch in txt:
                if t[0] != 's' and ISL.match(ch): ecs.append(ch); etok.append(i); epos.append(n)
                efull.append(ch); n += 1
        elif t[0] in ('note', 'nnum', 'pbeg'): efull.append('¤' if t[0] != 'pbeg' else ' '); n += 1
    ts = {}
    for k, t in enumerate(etok): ts.setdefault(t, k)
    return {'TOK': TOK, 'ecs': ''.join(ecs), 'etok': etok, 'efull': ''.join(efull), 'epos': epos, 'tokstart': ts}
names = sorted(z.namelist())
BODY = stream(sum((events(n) for n in names if re.search(r's0\d\d-(Introduction|Chapter)', n)), []))
NOTES = stream(events([n for n in names if 'Notes' in n][0]))

# ---------------- text layer, split into body and footnote lines by type size ----------------
def pack(ws):
    chars = []; cbox = []; widx = []; full = []; lpos = []; n = 0
    for k, (w, b) in enumerate(ws):
        for ch in w + ' ':
            if ISL.match(ch): chars.append(ch); cbox.append(b); widx.append(k); lpos.append(n)
            full.append(ch); n += 1
    return {'words': ws, 'chars': ''.join(chars), 'cbox': cbox, 'widx': widx, 'full': ''.join(full), 'lpos': lpos}
SIG = re.compile(r'Vidensk\W*\s*Sel[sk]+\W*\s*Skr', re.I)   # sheet-foot series line „Vidensk. Selsk. Skr., 6. Række ...“ (NOT „Række“ alone: it is a common word)
NOTE_PITCH, NOTE_GAP, SMALL_H = 12.5, 18.0, 4.5     # baseline pitch over pp. 5-103 (2026-10-09): notes 10-12, body 13-16
LAY = {}; NLAY = {}; DROPPED = {}
for p in range(1, LAST + 1):
    x = subprocess.run(['pdftotext', '-bbox', '-f', str(pdfpage(p)), '-l', str(pdfpage(p)), scan_path(), '-'],
                       capture_output=True, text=True).stdout
    ws = [(html.unescape(w[4]), tuple(map(float, w[:4]))) for w in
          re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', x)]
    # Google's word boxes are tight round the letters, so type size cannot be read off box height
    # (body 5.0 pt, notes 4.0-4.5, overlapping).  Split by LINE PITCH instead: body ~14 pt, notes ~10 pt.
    # Lines are clustered by y; the folio line (figures only) at the head and the sheet-foot series
    # line (SIG) are dropped; the footnote block is the trailing run of lines at note pitch (< NOTE_PITCH)
    # that follows a gap > NOTE_GAP; a single trailing line counts as a note only if its type is small.
    ln = []
    for w, b in sorted(ws, key=lambda wb: wb[1][1]):
        if ln and abs(b[1] - ln[-1]['y']) < 4: ln[-1]['ws'].append((w, b))
        else: ln.append({'y': b[1], 'ws': [(w, b)]})
    keep = []
    for k, l in enumerate(ln):
        t = ' '.join(w for w, b in sorted(l['ws'], key=lambda wb: wb[1][0]))
        if SIG.search(t) or (re.fullmatch(r'[\W\d\s]*', t) and (k == 0 or k == len(ln) - 1)):
            DROPPED.setdefault(p, []).append(t); continue
        keep.append(l)
    for l in keep: l['base'] = statistics.median([b[3] for w, b in l['ws']])   # baseline: steadier than yMin
    nstart = len(keep)
    k = len(keep) - 1
    while k > 0 and keep[k]['base'] - keep[k - 1]['base'] < NOTE_PITCH: k -= 1
    if k < len(keep) - 1 and k > 0 and keep[k]['base'] - keep[k - 1]['base'] > NOTE_GAP: nstart = k
    elif k == len(keep) - 1 and k > 0 and keep[k]['base'] - keep[k - 1]['base'] > NOTE_GAP:
        hh = statistics.median([b[3] - b[1] for w, b in keep[k]['ws']])
        if hh <= SMALL_H: nstart = k
    body = [wb for l in keep[:nstart] for wb in sorted(l['ws'], key=lambda wb: wb[1][0])]
    notes = [wb for l in keep[nstart:] for wb in sorted(l['ws'], key=lambda wb: wb[1][0])]
    LAY[p] = pack(body); NLAY[p] = pack(notes)

# ---------------- alignment ----------------
def align(S, pages, LY):
    ecs = S['ecs']; LS = ''.join(LY[p]['chars'] for p in pages); loff = {}; o = 0
    for p in pages: loff[p] = o; o += len(LY[p]['chars'])
    ops = []; i0 = j0 = 0
    while j0 < len(LS):
        lw = LS[j0: j0 + 3000]; last = j0 + len(lw) >= len(LS); ew = ecs[i0:] if last else ecs[i0: i0 + 3600]
        oc = difflib.SequenceMatcher(None, ew, lw, autojunk=False).get_opcodes()
        if not last:
            cut = 2 * len(lw) // 3
            k = max(n for n, x in enumerate(oc) if x[0] == 'equal' and x[3] + 8 <= cut)
            op, a1, a2, b1, b2 = oc[k]; m = min(b2, cut) - b1
            oc = oc[:k] + [(op, a1, a1 + m, b1, b1 + m)]
        ops += [(op, i0 + a1, i0 + a2, j0 + b1, j0 + b2) for op, a1, a2, b1, b2 in oc]
        i0, j0 = i0 + oc[-1][2], j0 + oc[-1][4]
        if last: break
    pl = [p for p in pages if LY[p]['chars']]
    lpage = lambda j: max(p for p in pl if loff[p] <= j)
    pstart = {}; e2l = [None] * len(ecs); l2e = [None] * len(LS); hunks = []
    for op, a1, a2, b1, b2 in ops:
        for p in pl:
            if p not in pstart and b1 <= loff[p] < max(b2, b1 + 1): pstart[p] = a1 + (loff[p] - b1 if op == 'equal' else 0)
        for k in range(a2 - a1): e2l[a1 + k] = b1 + (k if op == 'equal' else 0)
        for k in range(b2 - b1): l2e[b1 + k] = a1 + (k if op == 'equal' else 0)
        if op != 'equal':
            p = lpage(b1); hunks.append({'page': p, 'e': (a1, a2), 'l': (b1 - loff[p], b2 - loff[p]), 'etxt': ecs[a1:a2], 'ltxt': LS[b1:b2]})
    return {'ops': ops, 'loff': loff, 'lpage': lpage, 'pstart': pstart, 'e2l': e2l, 'l2e': l2e, 'hunks': hunks, 'pages': pl, 'LY': LY}
AB = align(BODY, range(FIRST, LAST + 1), LAY); AN = align(NOTES, range(FIRST, LAST + 1), NLAY)

# ---------------- moved blocks ----------------
# Text the two streams place differently -- a footnote set across a page turn, a quotation in small
# type read as footnote, a note line read as text -- shows as a long deletion in one alignment and a
# long insertion in the other (or the same) one. Pair them by content; diff the pair letter by letter.
MOVES = []
def moves():
    dels = [(A, S, h) for A, S in ((AB, BODY), (AN, NOTES)) for h in A['hunks'] if len(h['etxt']) >= 30 and len(h['ltxt']) <= 0.3 * len(h['etxt'])]
    ins = [(A, h) for A in (AB, AN) for h in A['hunks'] if len(h['ltxt']) >= 30 and len(h['etxt']) <= 0.3 * len(h['ltxt'])]
    cov = {}
    for A, S, d in dels:
        for A2, i in ins:
            sm = difflib.SequenceMatcher(None, d['etxt'], i['ltxt'], autojunk=False)
            bl = [x for x in sm.get_matching_blocks() if x.size >= 8]
            if not bl or sum(x.size for x in bl) < 0.6 * min(len(d['etxt']), len(i['ltxt'])): continue
            a0, a1 = bl[0].a, bl[-1].a + bl[-1].size; b0, b1 = bl[0].b, bl[-1].b + bl[-1].size
            cov[id(d)] = cov.get(id(d), 0) + (a1 - a0); cov[id(i)] = cov.get(id(i), 0) + (b1 - b0)
            MOVES.append((d['page'], i['page'], a1 - a0))
            for op, x1, x2, y1, y2 in difflib.SequenceMatcher(None, d['etxt'][a0:a1], i['ltxt'][b0:b1], autojunk=False).get_opcodes():
                if op == 'equal': continue
                A['hunks'].append({'page': i['page'], 'e': (d['e'][0] + a0 + x1, d['e'][0] + a0 + x2), 'l': (i['l'][0] + b0 + y1, i['l'][0] + b0 + y2),
                                   'etxt': d['etxt'][a0 + x1:a0 + x2], 'ltxt': i['ltxt'][b0 + y1:b0 + y2], 'LY': A2['LY']})
    for A, S, d in dels:
        if cov.get(id(d), 0) >= 0.85 * len(d['etxt']): d['moved'] = True
    for A2, i in ins:
        if cov.get(id(i), 0) >= 0.85 * len(i['ltxt']): i['moved'] = True
    for A in (AB, AN): A['hunks'] = [h for h in A['hunks'] if not h.get('moved')]
moves()
print('moved blocks paired:', MOVES)

# ---------------- classify ----------------
LAYER_FAULT = {('V','Y'),('D','B'),('D','H'),('R','H'),('N','H'),('F','E'),('h','li'),('r','i'),('l','i'),('in','m'),
               ('ü','ii'),('L','U'),('0','o'),('1','x'),('1','i'),('f','t'),('r','t'),('e','c'),('t','l'),('f','l'),('h','b'),
               ('m','rn'),('n','u'),('a','u'),('l','I'),('I','l'),('i','l'),('O','0'),('C','G'),('G','C'),('E','F'),('S','8'),('B','R'),
               ('11', '“'), ('l', 'i')}
ACC = str.maketrans('éèêëáàâäóòôöúùûüíìîï', 'eeeeaaaaoooouuuuiiii')
VOC = set()
for f in glob.glob(os.path.join(BOOK, '..', '..', '*', '*', 'transcription.tex')):
    if os.path.samefile(os.path.dirname(f), BOOK): continue      # never this book's own output
    VOC.update(re.findall('[' + L + ']+', re.sub(r'\\[A-Za-z]+', ' ', open(f, encoding='utf-8', errors='replace').read())))
ROMAN = re.compile(r'[IVXL]+')
def classify(S, A, sec):
    TOK, etok = S['TOK'], S['etok']; checks = []; seen = {}; auto = 0
    near = lambda ti, kinds: [t[1] for t in TOK[max(0, ti - 4): ti + 5] if t[0] in kinds]
    for h in A['hunks']:
        e, l = h['etxt'], h['ltxt']; ti = etok[min(h['e'][0], len(etok) - 1)]
        w = TOK[ti][1] if TOK[ti][0] == 'w' else ''
        if TOK[ti][0] == 'head' and (ROMAN.fullmatch(e) or e == '') and re.fullmatch(r'\d*', l): auto += 1; continue  # chapter numeral: e-book roman, print arabic
        if e.lower() == l.lower(): auto += 1; continue
        if e == '' and re.search(r'\d', l) and re.fullmatch(r'\d*([A-ZÆØÅ][a-zæøåö]+)+\d*', l): auto += 1; continue   # running head with folio
        if l and l.replace('l', 'I').replace('y', 'Y').isupper() and difflib.SequenceMatcher(None, e.upper(), l.replace('l', 'I')).ratio() >= 0.6: auto += 1; continue
        if A is AB and ROMAN.fullmatch(e or 'x') and re.fullmatch(r'\d+', l or 'x') and TOK[ti][0] == 'head': auto += 1; continue
        if ((e, l) in LAYER_FAULT or (e.translate(ACC) == l and e != l)) and (w in VOC or not w): auto += 1; continue
        if e == '' and (re.fullmatch(r'\d{1,2}', l) or len(l) <= 2) and any(t[0] == 's' and re.search('[„“”"]', t[1]) for t in TOK[max(0, ti-2): ti+3]):
            auto += 1; continue
        if e == '' and l in ('u', 'w', 'n', 'a', 'f', 'i', 'l', '1', '4', '44', '14', '11', 'r', 'I', 'j', 't'): auto += 1; continue
        v = None
        if w:
            ww = re.sub('[^' + L + ']', '', w); o1 = h['e'][0] - S['tokstart'][ti]; o2 = h['e'][1] - S['tokstart'][ti]
            if 0 <= o1 and o2 <= len(ww): v = ww[:o1] + l + ww[o2:]
        if v and w in VOC and v not in VOC and len(e) <= 2 and len(l) <= 3 and not re.search('[éèêáàóòúù]', l):
            auto += 1; continue
        key = f"{sec}{h['page']}|{w}|{e}>{l}"; seen[key] = seen.get(key, 0) + 1
        if seen[key] > 1: key += f'#{seen[key]}'
        cb = h.get('LY', A['LY'])[h['page']]['cbox']
        checks.append({'id': f'{sec}{len(checks)+1:03d}', 'key': key, 'page': h['page'], 'ebook': e, 'layer': l, 'tok': ti,
                       'word': w, 'variant': v, 'bbox': cb[min(h['l'][0], len(cb) - 1)] if cb else [0, 0, 1, 1]})
    return checks, auto
CB, autoB = classify(BODY, AB, 'F'); CN, autoN = classify(NOTES, AN, 'N')
print(f'body: {len(AB["pstart"])} page starts | {len(AB["hunks"])} letter hunks, {autoB} settled by rule, {len(CB)} checks')
print(f'notes: {len(AN["hunks"])} letter hunks, {autoN} settled by rule, {len(CN)} checks')
lens = sorted(((len(h['etxt']), len(h['ltxt'])), h['page']) for h in AB['hunks'] + AN['hunks'])
print('largest hunks (e, l), page:', lens[-6:])

# ---------------- punctuation ----------------
PUN = '.,;:!?()'
def punct(S, A, sec):
    out = []; LY = A['LY']
    for op, a1, a2, b1, b2 in A['ops']:
        if op != 'equal': continue
        for k in range(a1, a2 - 1):
            eg = S['efull'][S['epos'][k] + 1: S['epos'][k + 1]]
            j = b1 + k - a1; p = A['lpage'](j); jj = j - A['loff'][p]
            if A['lpage'](j + 1) != p: continue
            lay = LY[p]; lg = lay['full'][lay['lpos'][jj] + 1: lay['lpos'][jj + 1]]
            pe = ''.join(c for c in eg if c in PUN); pl = ''.join(c for c in lg.replace(',,', '„').replace('{', '(').replace('}', ')') if c in PUN)
            pe = re.sub(r'\.+', '.', pe); pl = re.sub(r'\.+', '.', pl)       # ellipses and doubled points
            nxt = S['ecs'][k + 1]
            if pe == '' and pl == '.' and nxt.islower(): continue        # a speck: no point before a lower-case word
            if pe == pl or '¤' in eg or ('*' in lg and ')' in pl and pe == pl.replace(')', '')): continue
            ti = S['etok'][k]
            out.append({'id': f'{sec}P{len(out)+1:03d}', 'page': p, 'ebook': pe, 'layer': pl, 'word': S['TOK'][ti][1] if S['TOK'][ti][0] == 'w' else '',
                        'key': f"{sec}{p}|{S['TOK'][ti][1]}|{eg.strip()}>{lg.strip()}", 'bbox': lay['cbox'][jj], 'tok': ti})
    return out
def italic_commas(S, A, sec):
    out = []; TOK = S['TOK']
    for ti, t in enumerate(TOK):
        if t[0] == 'ioff' and TOK[ti-1][0] == 's' and TOK[ti-1][1].rstrip().endswith(','):
            k = max(kk for kk in range(len(S['etok'])) if S['etok'][kk] <= ti); j = A['e2l'][k]
            if j is None: continue
            p = A['lpage'](j); jj = j - A['loff'][p]; lay = A['LY'][p]
            nxt = ''.join(x[1] for x in TOK[ti+1: ti+4] if x[0] in ('w', 's'))
            if not re.match(r'\s*p\.', nxt): continue
            out.append({'id': f'{sec}X{len(out)+1:03d}', 'page': p, 'ebook': 'comma closing italics', 'layer': lay['full'][lay['lpos'][jj]: lay['lpos'][jj] + 8],
                        'word': TOK[S['etok'][k]][1], 'key': f"{sec}{p}|{TOK[S['etok'][k]][1]}|comma closing italics", 'bbox': lay['cbox'][jj], 'tok': ti})
    return out
PB = punct(BODY, AB, 'F') + italic_commas(BODY, AB, 'F'); PN = punct(NOTES, AN, 'N') + italic_commas(NOTES, AN, 'N')
print('punctuation disagreements: body', len(PB), '| notes', len(PN))

# ---------------- paragraph breaks against the printed indents ----------------
def rows(p):
    R = []
    for k, (w, b) in enumerate(LAY[p]['words']):
        if R and abs(b[1] - R[-1]['y']) < 10 and b[0] > R[-1]['x1'] - 5: R[-1]['ks'].append(k); R[-1]['x1'] = b[2]
        else: R.append({'y': b[1], 'x0': b[0], 'x1': b[2], 'ks': [k]})
    return R
def paras(S, A):
    TOK = S['TOK']; out = []
    def broke(ti):
        for t in reversed(TOK[:ti]):
            if t[0] in ('pbeg', 'deco') + HEADS: return True
            if t[0] in ('w', 'note'): return False
        return True
    seen = set()
    for p in A['pages']:
        R = rows(p); mg = statistics.median([r['x0'] for r in R if len(r['ks']) >= 3] or [0]); lay = LAY[p]
        first = {}
        for c, k in enumerate(lay['widx']): first.setdefault(k, c)
        for r in R:
            k = next((k for k in r['ks'] if k in first), None)
            if k is None: continue
            ind = 20 < r['x0'] - mg < 120; e = A['l2e'][A['loff'][p] + first[k]]
            if e is None: continue
            ti = S['etok'][e]
            if ti in seen: continue
            if ind and not broke(ti): seen.add(ti); out.append({'kind': 'indent, no break in the e-book', 'page': p, 'word': lay['words'][k][0], 'bbox': lay['words'][k][1], 'tok': ti})
            if not ind and broke(ti) and TOK[ti][0] == 'w' and r['x0'] - mg < 20:
                seen.add(ti); out.append({'kind': 'break in the e-book, no indent', 'page': p, 'word': lay['words'][k][0], 'bbox': lay['words'][k][1], 'tok': ti})
    return out
PARA = paras(BODY, AB)
_cnt = {}
for x in PARA: _cnt[x['page']] = _cnt.get(x['page'], 0) + 1
PARA = [x for x in PARA if _cnt[x['page']] <= 4]
print('pages skipped by the indent check (layout unmeasurable):', [p for p, n in _cnt.items() if n > 4])
print('paragraph disagreements:', len(PARA), {k: sum(1 for x in PARA if x['kind'] == k) for k in set(x['kind'] for x in PARA)})

# ---------------- letterspacing (the print's emphasis): letters of one word in separate layer words ----------------
def spaced(S, A):
    out = set()
    for ti, t in enumerate(S['TOK']):
        if t[0] != 'w': continue
        k0 = S['tokstart'].get(ti)
        if k0 is None: continue
        n = sum(1 for ch in t[1] if ISL.match(ch))
        if n < 2: continue
        js = [A['e2l'][k] for k in range(k0, k0 + n)]
        if None in js: continue
        ids = set()
        for j in js:
            p = A['lpage'](j); lay = A['LY'][p]; ids.add((p, lay['widx'][j - A['loff'][p]]))
        singles = sum(1 for p, wi in ids if len(re.sub('[^' + L + ']', '', A['LY'][p]['words'][wi][0])) <= 1)
        if len(ids) >= n - (1 if n > 4 else 0) and singles >= n - 2: out.add(ti)
    # short words (2-3 letters: Et, af, os, her, og) are split by the layer without being spaced; keep a
    # short word only when it is capitalized and stands next to a spaced name (Fr. Nielsen, Chr. Olufsen)
    words = [ti for ti, t in enumerate(S['TOK']) if t[0] == 'w']
    for n_, ti in enumerate(words):
        if ti in out and sum(1 for ch in S['TOK'][ti][1] if ISL.match(ch)) < 4:
            nb = [words[m] for m in (n_ - 1, n_ + 1) if 0 <= m < len(words)]
            if not (S['TOK'][ti][1][:1].isupper() and any(x in out and sum(1 for ch in S['TOK'][x][1] if ISL.match(ch)) >= 4 for x in nb)):
                out.discard(ti)
    return out
# ---------------- letterspacing by BOX WIDTH (Google's layer joins spaced letters into one word) ----------------
# danske-filosoffer's spaced() above relies on a layer that sets each spaced letter as its own word; Google's
# does not.  Here: fit a width per character (least squares over every layer word, refitted without the widest
# 12%), separately for body and footnote lines (smaller type), and score each word q = box width / expected
# width.  Measured 2026-10-09: unspaced words peak at q 1.00 (spread 0.95-1.10), spaced words lie at 1.15-1.45.
# q >= SP_HI is taken as spaced by rule; SP_LO <= q < SP_HI, and every spaced word of fewer than 4 letters,
# go to the image as checks keyed S<page>|<word>|spaced? (decision S = spaced, E = not).
import numpy as np
SP_LO, SP_HI = 1.12, 1.18      # calibrated 2026-10-09 on 60 random words read at the image (spcal sheets):
# q 1.08-1.13 0/10 spaced; 1.13-1.16 ~8/10; 1.16-1.19 6/10 (the misses: two words glued into one layer box,
# a drop capital); 1.19-1.22 10/10; 1.22-1.28 10/10.
def widthfit(LY):
    rows = [(p, k, w, b) for p in LY for k, (w, b) in enumerate(LY[p]['words']) if len(re.sub('[^' + L + ']', '', w)) >= 2]
    chars = sorted(set(c for p, k, w, b in rows for c in w)); ix = {c: i for i, c in enumerate(chars)}
    X = np.zeros((len(rows), len(chars) + 1)); y = np.array([b[2] - b[0] for p, k, w, b in rows])
    for i, (p, k, w, b) in enumerate(rows):
        for c in w: X[i, ix[c]] += 1
        X[i, -1] = 1
    coef = np.linalg.lstsq(X, y, rcond=None)[0]
    for _ in range(2):
        q = y / np.maximum(X @ coef, 1e-6); m = q < np.quantile(q, 0.88)
        coef = np.linalg.lstsq(X[m], y[m], rcond=None)[0]
    q = y / np.maximum(X @ coef, 1e-6)
    return {(p, k): float(v) for (p, k, w, b), v in zip(rows, q)}
QB = widthfit(LAY); QN = widthfit(NLAY)
def spaced_w(S, A, Q, sec):
    """Long words (4+ letters): q >= SP_HI in a layer box of its own -> spaced by rule; SP_LO <= q < SP_HI, or a
    layer box shared with another e-book word (glued words), -> to the image.  Short words (2-3 letters: og, af,
    i, et) are judged by context only (spaced_short), never sent to the image: their q is too noisy."""
    out, ask, short, owner = set(), [], {}, {}
    def lw(j):
        p = A['lpage'](j); return (p, A['LY'][p]['widx'][j - A['loff'][p]])
    for ti, t in enumerate(S['TOK']):
        k0 = S['tokstart'].get(ti)
        if t[0] != 'w' or k0 is None: continue
        for k in range(k0, k0 + sum(1 for ch in t[1] if ISL.match(ch))):
            if A['e2l'][k] is not None: owner.setdefault(lw(A['e2l'][k]), set()).add(ti)
    for ti, t in enumerate(S['TOK']):
        if t[0] != 'w': continue
        k0 = S['tokstart'].get(ti)
        if k0 is None: continue
        n = sum(1 for ch in t[1] if ISL.match(ch))
        if n < 2: continue
        js = [A['e2l'][k] for k in range(k0, k0 + n)]
        if None in js: continue
        cnt = {}
        for j in js: cnt[lw(j)] = cnt.get(lw(j), 0) + 1
        ids = sorted(cnt); best = max((i for i in ids if i in Q), key=lambda i: cnt[i], default=None)
        if best is None: continue
        q = Q[best]; p, k = best      # a word divided at a line end: judge it by its longer part (a „for-“ is wide by its hyphen)
        if n < 4: short[ti] = q; continue
        glued = any(len(owner.get(i, ())) > 1 for i in ids)
        if q >= SP_HI and not glued: out.add(ti)
        elif q >= SP_LO:
            ask.append({'id': f'{sec}S{len(ask)+1:03d}', 'page': p, 'ebook': 'spaced?', 'layer': f'q={q:.2f}' + (' glued' if glued else ''),
                        'word': t[1], 'key': f"{sec}{p}|{t[1]}|spaced?", 'bbox': A['LY'][p]['words'][k][1], 'tok': ti, 'q': q})
    return out, ask, short
def spaced_short(S, SP, short):
    """A 2-3 letter word is spaced only when both neighbouring words are (checked at the image on p. 30)."""
    words = [ti for ti, t in enumerate(S['TOK']) if t[0] == 'w']
    for m, ti in enumerate(words):
        if ti not in short: continue
        nb = [words[x] in SP for x in (m - 1, m + 1) if 0 <= x < len(words)]
        if len(nb) == 2 and all(nb): SP.add(ti)     # one spaced neighbour is not enough: „Wolfe, der“ (p. 30, image)
SPB, SAB, SHB = spaced_w(BODY, AB, QB, 'F'); SPN, SAN, SHN = spaced_w(NOTES, AN, QN, 'N')
_seen = {}
for c in SAB + SAN:
    _seen[c['key']] = _seen.get(c['key'], 0) + 1
    if _seen[c['key']] > 1: c['key'] += f"#{_seen[c['key']]}"
print('letterspacing by box width: by rule body', len(SPB), 'notes', len(SPN), '| to the image', len(SAB) + len(SAN))
print('letterspaced words: body', len(SPB), '| notes', len(SPN))
for name, data in (('checks.json', CB + CN), ('punct.json', PB + PN), ('paras.json', PARA), ('spaced-checks.json', SAB + SAN)):
    json.dump(data, open(os.path.join(WORK, name), 'w'), ensure_ascii=False, indent=0)
json.dump({'body': sorted(BODY['TOK'][t][1] for t in SPB), 'notes': sorted(NOTES['TOK'][t][1] for t in SPN)}, open(os.path.join(WORK, 'spaced.json'), 'w'), ensure_ascii=False)

# ---------------- decisions ----------------
DEC = {}
for l in open(os.path.join(HERE, 'decisions.tsv'), encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        k, r = l.rstrip('\n').split('\t')[:2]; DEC[k] = r
listed = [c['key'] for c in CB + CN + PB + PN + SAB + SAN] + [f"P{x['page']}|{x['word']}|{x['kind']}" for x in PARA]
todo = [k for k in listed if k not in DEC]; stale = [k for k in DEC if k not in listed]
print('undecided:', len(todo), '| decisions no longer listed:', stale[:10])
for c in SAB + SAN:                                  # spacing read at the image: S = spaced
    if DEC.get(c['key']) == 'S': (SPB if c in SAB else SPN).add(c['tok'])
for c in SAB + SAN:
    if DEC.get(c['key']) == 'E': (SPB if c in SAB else SPN).discard(c['tok'])
spaced_short(BODY, SPB, SHB); spaced_short(NOTES, SPN, SHN)     # after the long words are settled
if '--emit' not in sys.argv: sys.exit(0)
if todo and '--draft' not in sys.argv: sys.exit('refusing to emit: undecided checks (sheets.py --todo crops them)')
REPL = {}
for c in CB + CN:
    r = DEC.get(c['key'], 'E')
    if r != 'E': REPL[('B' if c in CB else 'N', c['tok'])] = r
PUNCT = {}
for c in PB + PN:       # punctuation read at the image: '-' drop the e-book's marks in the gap, '=X' set them to X
    d = DEC.get(c['key'], 'E')
    if d == '-' or d.startswith('='):
        sec = 'B' if c in PB else 'N'; S = BODY if sec == 'B' else NOTES; ti = c['tok'] + 1
        while ti < len(S['TOK']) and S['TOK'][ti][0] != 's': ti += 1
        t = S['TOK'][ti][1]; new = d[1:] if d.startswith('=') else ''
        REPL[(sec, ti)] = new + re.sub('[' + re.escape(PUN) + ']', '', t)
for c in PB + PN:
    if DEC.get(c['key']) == '.' and 'comma closing italics' in c['key']:
        sec = 'B' if c in PB else 'N'; S = BODY if sec == 'B' else NOTES; ti = c['tok'] - 1
        REPL[(sec, ti)] = S['TOK'][ti][1][::-1].replace(',', '.', 1)[::-1]

# ---------------- LaTeX ----------------
def esc(s):
    s = s.replace('\\', r'\textbackslash{}')
    for a, b in [('&', r'\&'), ('%', r'\%'), ('$', r'\$'), ('#', r'\#'), ('_', r'\_'), ('{', r'\{'), ('}', r'\}')]: s = s.replace(a, b)
    s = re.sub(r'(\d)—(\d)', r'\1--\2', s)
    return s.replace('—', '---').replace('–', '--').replace('’', "'").replace('‘', "'").replace('\u00a0', ' ').replace('…', '...')
OPEN = {'ion': r'\textit{', 'scon': r'\textsc{', 'sbon': r'\textsubscript{', 'spon': r'\textsuperscript{'}
ROM = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
def arabic(r):
    n = 0
    for i, c in enumerate(r):
        v = ROM[c]; n += -v if i + 1 < len(r) and ROM[r[i + 1]] > v else v
    return n
MARK = {k: f'{k})' for k in range(1, 10)}     # this print numbers its notes 1), 2) ... per page
def page_of(A, e):
    ps = sorted(A['pstart'].items(), key=lambda x: x[1])
    return max([p for p, s in ps if s <= e] or [FIRST])
def emit(S, A, sec, spaced, notes=None, markers=True):
    TOK = S['TOK']; out = []
    def close():
        s = ''.join(out); t = s.rstrip(' '); out[:] = [t, '}', ' ' * (len(s) - len(t))]
    mk = {}
    if markers:
        for p, e in A['pstart'].items():
            ti = S['etok'][e]; off = e - S['tokstart'][ti]
            if off == 0:
                while ti > 0 and TOK[ti - 1][0] in ('ion', 'scon'): ti -= 1
            mk.setdefault(ti, []).append((off, p))
    M = lambda p: f'\n% --- p. {p} ---\n\\setcounter{{footnote}}{{0}}%\n\\opage{{{p}}}'
    rank = {}; chunks = {}; cur = None
    for ti, t in enumerate(TOK):
        k = t[0]
        for off, p in mk.get(ti, []):
            if off == 0: out.append(M(p))
        if k == 'nnum':
            cur = t[1]; chunks[cur] = len(''.join(out)); out.append(f'\x00{cur}\x00'); continue
        if k == 'head':
            h = t[1]            # as printed: „I. LUDVIG HOLBERG“, then „2.“-„17.“ (the e-book agrees)
            out.append('\n\n\\begin{center}\\large ' + esc(h.strip()) + '\\end{center}\n\n')
        elif k in ('sub', 'h2', 'h3'): out.append('\n\n\\begin{center}' + esc(t[1]) + '\\end{center}\n\n')
        elif k == 'deco': out.append('\n\n\\begin{center}\\rule{2cm}{0.4pt}\\end{center}\n\n')
        elif k == 'pbeg': out.append('\n\n')
        elif k in OPEN: out.append(OPEN[k])
        elif k in ('ioff', 'scoff', 'sboff', 'spoff'): close()
        elif k == 'note':
            kk = max(x for x in range(len(S['etok'])) if S['etok'][x] < ti) if ti > S['etok'][0] else 0
            p = page_of(A, kk); r = rank[p] = rank.get(p, 0) + 1
            s = ''.join(out).rstrip(' ')
            out[:] = [s, f'%\n% footnote {MARK.get(r, "?")} on p. {p}\n\\footnote[{r}]{{' + notes.get(t[1], '% NOTE MISSING') + '}']
        elif k == 'w':
            w = REPL.get((sec, ti), t[1]); ms = [(o, p) for o, p in mk.get(ti, []) if o > 0]
            def fmt(x): return r'\emph{' + esc(x) + '}' if ti in spaced and x else esc(x)
            if ms:
                (o, p), = ms; n = 0
                for idx, ch in enumerate(w):
                    if ISL.match(ch):
                        if n == o: break
                        n += 1
                out.append(fmt(w[:idx]) + '%' + M(p) + fmt(w[idx:]))
            else: out.append(fmt(w))
        elif k == 's': out.append(esc(REPL.get((sec, ti), t[1])))
    txt = ''.join(out)
    txt = re.sub(r'[ \t]+', ' ', txt); txt = re.sub(r' +([.,;:!?)])', r'\1', txt); txt = re.sub(r'\( +', '(', txt)
    txt = re.sub(r'\n +', '\n', txt); txt = re.sub(r' +\n', '\n', txt); txt = re.sub(r'\n{3,}', '\n\n', txt)
    return txt
def patch(txt, sec):
    for l in open(os.path.join(HERE, 'patches.tsv'), encoding='utf-8'):
        if not l.strip() or l.startswith('#'): continue
        s_, f, r = l.rstrip('\n').split('\t')[:3]; r = r.replace('⏎', '\n')
        if s_[0] != sec: continue
        n = txt.count(f)
        if n != 1: print('PATCH NOT APPLIED (found %d times):' % n, s_, f); continue
        txt = txt.replace(f, r)
    return txt
def wrap(txt):
    lines = []
    for para in txt.split('\n'):
        while len(para) > 85 and not para.startswith('%'):
            cut = para.rfind(' ', 0, 80)
            if cut <= 0: break
            lines.append(para[:cut]); para = para[cut + 1:]
        lines.append(para)
    return '\n'.join(lines).strip() + '\n'
nt = patch(emit(NOTES, AN, 'N', SPN, markers=False), 'N')
NT = {}
for m in re.finditer(r'\x00(\d+)\x00(.*?)(?=\x00\d+\x00|\Z)', nt, re.S):
    NT[int(m.group(1))] = re.sub(r'\s*\n\s*', ' ', m.group(2)).strip()
def mark_paren(t):
    """This print marks a note „1)“, and the e-book keeps the „)“ as text after its note number.  The
    preamble's \\thefootnote already prints „1)“, so drop one „)“ right after each \\footnote{...}."""
    out = []; i = 0
    for m in re.finditer(r'\\footnote\[\d\]\{', t):
        if m.start() < i: continue
        j = m.end(); d = 1
        while d:
            d += {'{': 1, '}': -1}.get(t[j], 0); j += 1
        out.append(t[i:j]); i = j + 1 if t[j:j + 1] == ')' else j
    return ''.join(out) + t[i:]
def merge_emph(t):
    """A spaced run is emitted word by word („\\emph{a} \\emph{b}“); join it into one span („\\emph{a b}“)."""
    return re.sub(r'\}([ \n]+)\\emph\{', lambda m: m.group(1), t)
body = patch(merge_emph(mark_paren(emit(BODY, AB, 'B', SPB, notes=NT))), 'B')
missing = [k for k in range(1, max(NT) + 1) if f'footnote' and k not in NT]
odd = sorted(set(c for c in body if ord(c) > 127 and c not in 'æøåÆØÅéèêëáàâäóòôöúùûüíìîïçÉÖÜÄ„“ɔ§'))
print('footnotes:', body.count('\\footnote['), '| note texts:', len(NT), '| page markers:', body.count('\\opage{'), '| unusual characters:', odd)
tpl = open(os.path.join(HERE, 'template.tex'), encoding='utf-8').read()
out = os.path.join(BOOK, 'transcription.tex')
open(out, 'w', encoding='utf-8').write(tpl.replace('%%BODY%%\n', wrap(body)))
print('wrote', out)
