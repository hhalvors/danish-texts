#!/usr/bin/env python3
"""
build.py -- Harald Høffding, FILOSOFISKE PROBLEMER (1902): the Danish transcription by the
E-BOOK METHOD (TRANSCRIPTION-PLAYBOOK §00 point 0). No one types the text. Rerunnable:

    python3 build.py           align and list what needs the image (checks.json, punct.json, paras.json)
    python3 build.py --emit    also write ../../transcription.tex (refuses while a check is undecided)

Witnesses
  e-book (SAGA, Filosofiske_problemer.epub): the base text -- words, punctuation, paragraphs,
      italics, small caps, subscripts, headings, the endnote texts.
  PDF text layer of the KB scan (SCANS.tsv): a second witness for every letter and digit, the
      page boundaries, the print's own endnote labels, the paragraph indents, punctuation.
Alignment is on letters and digits only, one continuous alignment per section (body pp. 1-84,
Noter pp. 85-90) in windows of 3000 layer characters, so the layer's split words do not matter.
What no rule settles is listed; sheets.py crops it from the scan; the reading at the image goes
into decisions.tsv (words) or patches.tsv (anything else), print governing, misprints kept.
"""
import zipfile, re, html, difflib, subprocess, sys, os, json, glob, statistics
HERE = os.path.dirname(os.path.abspath(__file__))     # ebook-method/<book>/: scripts and the decisions (tracked)
BOOK = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'texts', 'hoeffding', os.path.basename(HERE))
WORK = os.path.join(BOOK, '.parts', 'ebook'); os.makedirs(WORK, exist_ok=True)   # scratch output (gitignored)
sys.path.insert(0, HERE); from pagemap import pdfpage, scan_path
z = zipfile.ZipFile(os.path.join(BOOK, 'Filosofiske_problemer.epub'))
L = 'A-Za-zÀ-ÖØ-öø-ÿ0-9'; ISL = re.compile('[' + L + ']')
# The print's endnote labels (Noter pp. 85-90 and the text, at the image): 1-12, 12b, 13-31, 31b, 31c,
# 32-60 = 63 notes, which the e-book renumbered 1-63. In the Noter the 12b note is labelled "12)".
PRINTNO = [str(n) for n in range(1, 13)] + ['12b'] + [str(n) for n in range(13, 32)] + ['31b', '31c'] + [str(n) for n in range(32, 61)]
assert len(PRINTNO) == 63

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
                if k: out.append(('pbeg',))          # the e-book's bullet marks a paragraph break of the print
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
BODY = stream(sum((events(n) for n in names if re.search(r's00[3-7]-(Introduction|Chapter)', n)), []))
NOTES = stream(events([n for n in names if 'Notes' in n][0]))

# ---------------- text layer ----------------
LAY = {}
for p in range(1, 91):
    x = subprocess.run(['pdftotext', '-bbox', '-f', str(pdfpage(p)), '-l', str(pdfpage(p)), scan_path(), '-'],
                       capture_output=True, text=True).stdout
    ws = [(html.unescape(w[4]), tuple(map(float, w[:4]))) for w in
          re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', x)]
    chars = []; cbox = []; widx = []; full = []; lpos = []; n = 0
    for k, (w, b) in enumerate(ws):
        for ch in w + ' ':
            if ISL.match(ch): chars.append(ch); cbox.append(b); widx.append(k); lpos.append(n)
            full.append(ch); n += 1
    LAY[p] = {'words': ws, 'chars': ''.join(chars), 'cbox': cbox, 'widx': widx, 'full': ''.join(full), 'lpos': lpos}

# ---------------- alignment ----------------
def align(S, pages):
    ecs = S['ecs']; LS = ''.join(LAY[p]['chars'] for p in pages); loff = {}; o = 0
    for p in pages: loff[p] = o; o += len(LAY[p]['chars'])
    ops = []; i0 = j0 = 0
    while j0 < len(LS):
        lw = LS[j0: j0 + 3000]; last = j0 + len(lw) >= len(LS); ew = ecs[i0:] if last else ecs[i0: i0 + 3600]
        oc = difflib.SequenceMatcher(None, ew, lw, autojunk=False).get_opcodes()
        if not last:
            cut = 2 * len(lw) // 3      # stop inside an equal run at or before 2/3 of the window
            k = max(n for n, x in enumerate(oc) if x[0] == 'equal' and x[3] + 8 <= cut)
            op, a1, a2, b1, b2 = oc[k]; m = min(b2, cut) - b1
            oc = oc[:k] + [(op, a1, a1 + m, b1, b1 + m)]
        ops += [(op, i0 + a1, i0 + a2, j0 + b1, j0 + b2) for op, a1, a2, b1, b2 in oc]
        i0, j0 = i0 + oc[-1][2], j0 + oc[-1][4]
        if last: break
    lpage = lambda j: max(p for p in pages if loff[p] <= j)
    pstart = {}; e2l = [None] * len(ecs); l2e = [None] * len(LS); hunks = []
    for op, a1, a2, b1, b2 in ops:
        for p in pages:
            if p not in pstart and b1 <= loff[p] < max(b2, b1 + 1): pstart[p] = a1 + (loff[p] - b1 if op == 'equal' else 0)
        for k in range(a2 - a1): e2l[a1 + k] = b1 + (k if op == 'equal' else 0)
        for k in range(b2 - b1): l2e[b1 + k] = a1 + (k if op == 'equal' else 0)
        if op != 'equal':
            p = lpage(b1); hunks.append({'page': p, 'e': (a1, a2), 'l': (b1 - loff[p], b2 - loff[p]), 'etxt': ecs[a1:a2], 'ltxt': LS[b1:b2]})
    return {'ops': ops, 'loff': loff, 'lpage': lpage, 'pstart': pstart, 'e2l': e2l, 'l2e': l2e, 'hunks': hunks, 'pages': list(pages)}
AB = align(BODY, range(1, 85)); AN = align(NOTES, range(85, 91))

# ---------------- classify the letter/digit disagreements ----------------
LAYER_FAULT = {('V','Y'),('D','B'),('D','H'),('R','H'),('N','H'),('F','E'),('h','li'),('r','i'),('l','i'),('in','m'),
               ('ü','ii'),('L','U'),('0','o'),('1','x'),('1','i'),('f','t'),('r','t'),('e','c'),('t','l'),('f','l'),('h','b'),
               ('m','rn'),('n','u'),('a','u'),('l','I'),('I','l'),('i','l'),('O','0'),('C','G'),('G','C'),('E','F'),('S','8'),('B','R')}
ACC = str.maketrans('éèêëáàâäóòôöúùûüíìîï', 'eeeeaaaaoooouuuuiiii')
VOC = set()
for f in glob.glob(os.path.join(BOOK, '..', '..', '*', '*', 'transcription.tex')):
    if os.path.samefile(os.path.dirname(f), BOOK): continue      # never this book's own output
    VOC.update(re.findall('[' + L + ']+', re.sub(r'\\[A-Za-z]+', ' ', open(f, encoding='utf-8', errors='replace').read())))
def classify(S, A, sec):
    TOK, etok = S['TOK'], S['etok']; checks = []; seen = {}; auto = 0; numseen = []
    near = lambda ti, kinds: [t[1] for t in TOK[max(0, ti - 4): ti + 5] if t[0] in kinds]
    for h in A['hunks']:
        e, l = h['etxt'], h['ltxt']; ti = etok[min(h['e'][0], len(etok) - 1)]
        w = TOK[ti][1] if TOK[ti][0] == 'w' else ''
        if e.lower() == l.lower(): auto += 1; continue                                   # case only (small caps)
        if l and l.replace('l', 'I').replace('y', 'Y').isupper() and difflib.SequenceMatcher(None, e.upper(), l.replace('l', 'I')).ratio() >= 0.6:
            auto += 1; continue                                                             # spaced small caps, layer lossy
        if ((e, l) in LAYER_FAULT or (e.translate(ACC) == l and e != l)) and (w in VOC or not w):
            auto += 1; continue      # layer's glyph faults, layer drops accents -- only where the e-book's word is attested
                                     # (the notes' e-book has its own OCR errors: Grandlag, suffieiunt, Wissensehaftslehre)
        if re.search(r'\d', l) and near(ti, ('note', 'nnum')):
            numseen.append((near(ti, ('note', 'nnum'))[0], l, h['page'])); auto += 1; continue  # the print's note label
        if e == '' and (re.fullmatch(r'\d{1,2}', l) or len(l) <= 2) and any(t[0] == 's' and re.search('[„“”"]', t[1]) for t in TOK[max(0, ti-2): ti+3]):
            auto += 1; continue                                                             # quote glyphs read as figures
        if e == '' and l in ('u', 'w', 'n', 'a', 'f', 'i', 'l', '1', '4', '44', '14', '11'): auto += 1; continue   # specks
        v = None
        if w:
            ww = re.sub('[^' + L + ']', '', w); o1 = h['e'][0] - S['tokstart'][ti]; o2 = h['e'][1] - S['tokstart'][ti]
            if 0 <= o1 and o2 <= len(ww): v = ww[:o1] + l + ww[o2:]
        if v and w in VOC and v not in VOC and len(e) <= 2 and len(l) <= 3 and not re.search('[éèêáàóòúù]', l):
            auto += 1; continue                                                             # e-book word attested, layer's not
        key = f"{sec}{h['page']}|{w}|{e}>{l}"; seen[key] = seen.get(key, 0) + 1
        if seen[key] > 1: key += f'#{seen[key]}'
        cb = LAY[h['page']]['cbox']
        checks.append({'id': f'{sec}{len(checks)+1:03d}', 'key': key, 'page': h['page'], 'ebook': e, 'layer': l, 'tok': ti,
                       'word': w, 'variant': v, 'bbox': cb[min(h['l'][0], len(cb) - 1)]})
    return checks, auto, numseen
CB, autoB, numB = classify(BODY, AB, 'F'); CN, autoN, numN = classify(NOTES, AN, 'N')
print(f'body: {len(AB["pstart"])} page starts | {len(AB["hunks"])} letter hunks, {autoB} settled by rule, {len(CB)} checks')
print(f'notes: {len(AN["pstart"])} page starts | {len(AN["hunks"])} letter hunks, {autoN} settled by rule, {len(CN)} checks')
bad = [(k, l, p) for k, l, p in numB if not re.sub(r'\D', '', l).startswith(PRINTNO[k-1][0])]
print('body note labels seen in the layer:', len(set(k for k, l, p in numB)), 'of 63 | not starting with the expected figure:', bad)

# ---------------- punctuation (the e-book's, witnessed by the layer where the letters agree) ----------------
PUN = '.,;:!?()'
def punct(S, A, sec):
    out = []; LF = {}
    for op, a1, a2, b1, b2 in A['ops']:
        if op != 'equal': continue
        for k in range(a1, a2 - 1):
            eg = S['efull'][S['epos'][k] + 1: S['epos'][k + 1]]
            j = b1 + k - a1; p = A['lpage'](j); jj = j - A['loff'][p]
            if A['lpage'](j + 1) != p: continue
            lay = LAY[p]; lg = lay['full'][lay['lpos'][jj] + 1: lay['lpos'][jj + 1]]
            pe = ''.join(c for c in eg if c in PUN); pl = ''.join(c for c in lg if c in PUN)
            if pe == pl or '¤' in eg: continue
            ti = S['etok'][k]
            out.append({'id': f'{sec}P{len(out)+1:03d}', 'page': p, 'ebook': pe, 'layer': pl, 'word': S['TOK'][ti][1] if S['TOK'][ti][0] == 'w' else '',
                        'key': f"{sec}{p}|{S['TOK'][ti][1]}|{eg.strip()}>{lg.strip()}", 'bbox': lay['cbox'][jj], 'tok': ti})
    return out
PB = punct(BODY, AB, 'F'); PN = punct(NOTES, AN, 'N')
# Both OCRs read the point after an italic word as a comma (p. 87: „Efterskrift. p. 83“): list every comma
# that closes an italic span in the notes, and the last mark of every note (the e-book drops some).
def extra_punct(S, A, sec):
    out = []; TOK = S['TOK']
    lastletter = lambda ti: max(k for k in range(len(S['etok'])) if S['etok'][k] <= ti) if ti > S['etok'][0] else None
    for ti, t in enumerate(TOK):
        kind = None
        if t[0] == 'ioff' and TOK[ti-1][0] == 's' and TOK[ti-1][1].rstrip().endswith(','): kind = 'comma closing italics'
        if t[0] == 'pbeg' and ti > 0 and any(x[0] == 'nnum' for x in TOK[:ti]): kind = 'end of note'
        if t[0] == 'pbeg' and ti == len(TOK) - 1: kind = 'end of note'
        if not kind: continue
        k = lastletter(ti); j = A['e2l'][k]
        if j is None: continue
        p = A['lpage'](j); jj = j - A['loff'][p]; lay = LAY[p]
        tail = ''.join(x[1] for x in TOK[S['etok'][k]:ti] if x[0] in ('w', 's'))
        pe = re.sub('[^' + re.escape(PUN) + ']', '', re.sub('^[' + L + "'’]+", '', tail))
        lt = lay['full'][lay['lpos'][jj] + 1:]; lt = lt[:re.search('[' + L + ']|$', lt).start()]
        pl = re.sub('[^' + re.escape(PUN) + ']', '', lt)
        if kind == 'end of note' and pe.rstrip(')') == pl.rstrip(')') and pe: continue
        out.append({'id': f'{sec}X{len(out)+1:03d}', 'page': p, 'ebook': kind + ': ' + tail[-12:], 'layer': lay['full'][lay['lpos'][jj]: lay['lpos'][jj] + 8],
                    'word': TOK[S['etok'][k]][1], 'key': f"{sec}{p}|{TOK[S['etok'][k]][1]}|{kind}", 'bbox': lay['cbox'][jj], 'tok': ti})
    return out
PN += extra_punct(NOTES, AN, 'N')
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
    def broke(ti):   # is token ti the first word after a paragraph break or a heading?
        for t in reversed(TOK[:ti]):
            if t[0] in ('pbeg', 'deco') + HEADS: return True
            if t[0] in ('w', 'note') or (t[0] == 's' and t[1].strip()): return False
        return True
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
            if ind and not broke(ti): out.append({'kind': 'indent, no break in the e-book', 'page': p, 'word': lay['words'][k][0], 'bbox': lay['words'][k][1], 'tok': ti})
            if not ind and broke(ti) and TOK[ti][0] == 'w' and r['x0'] - mg < 20:
                out.append({'kind': 'break in the e-book, no indent', 'page': p, 'word': lay['words'][k][0], 'bbox': lay['words'][k][1], 'tok': ti})
    return out
PARA = paras(BODY, AB)
print('paragraph disagreements:', len(PARA), {k: sum(1 for x in PARA if x['kind'] == k) for k in set(x['kind'] for x in PARA)})
for name, data in (('checks.json', CB + CN), ('punct.json', PB + PN), ('paras.json', PARA)):
    json.dump(data, open(os.path.join(WORK, name), 'w'), ensure_ascii=False, indent=0)

# ---------------- decisions ----------------
DEC = {}
for l in open(os.path.join(HERE, 'decisions.tsv'), encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        k, r = l.rstrip('\n').split('\t')[:2]; DEC[k] = r
listed = [c['key'] for c in CB + CN + PB + PN] + [f"P{x['page']}|{x['word']}|{x['kind']}" for x in PARA]
todo = [k for k in listed if k not in DEC]; stale = [k for k in DEC if k not in listed]
print('undecided:', len(todo), todo[:8], '| decisions no longer listed:', stale)
if '--emit' not in sys.argv: sys.exit(0)
if todo and '--draft' not in sys.argv: sys.exit('refusing to emit: undecided checks (sheets.py --todo crops them)')
REPL = {}
for c in PB + PN:      # a comma closing an italic span that the print sets as a point
    if DEC.get(c['key']) == '.' and 'comma closing italics' in c['key']:
        sec = 'B' if c in PB else 'N'; S = BODY if sec == 'B' else NOTES; ti = c['tok'] - 1
        REPL[(sec, ti)] = S['TOK'][ti][1][::-1].replace(',', '.', 1)[::-1]
for c in CB + CN:
    r = DEC.get(c['key'], 'E')
    if r != 'E': REPL[(id(c) and ('B' if c in CB else 'N'), c['tok'])] = r

# ---------------- LaTeX ----------------
def esc(s):
    s = s.replace('\\', r'\textbackslash{}')
    for a, b in [('&', r'\&'), ('%', r'\%'), ('$', r'\$'), ('#', r'\#'), ('_', r'\_'), ('{', r'\{'), ('}', r'\}')]: s = s.replace(a, b)
    s = re.sub(r'(\d)—(\d)', r'\1--\2', s)
    return s.replace('—', '---').replace('–', '--').replace('’', "'").replace('‘', "'").replace(' ', ' ').replace('…', '...')
OPEN = {'ion': r'\textit{', 'scon': r'\textsc{', 'sbon': r'\textsubscript{', 'spon': r'\textsuperscript{'}
def emit(S, A, sec):
    TOK = S['TOK']; out = []
    def close():
        s = ''.join(out); t = s.rstrip(' '); out[:] = [t, '}', ' ' * (len(s) - len(t))]
    mk = {}
    for p, e in A['pstart'].items():
        ti = S['etok'][e]; off = e - S['tokstart'][ti]
        if off == 0:      # before the word, but after a paragraph break; before any opening italic/small caps
            while ti > 0 and TOK[ti - 1][0] in ('ion', 'scon'): ti -= 1
        mk.setdefault(ti, []).append((off, p))
    M = lambda p: f'\n% --- p. {p} ---\n\\opage{{{p}}}'
    pending = None
    for ti, t in enumerate(TOK):
        k = t[0]
        for off, p in mk.get(ti, []):
            if off == 0: out.append(M(p))
        if k == 'head':
            if re.fullmatch(r'[IVX]+\.', t[1]): pending = t[1]
            elif sec == 'N': out.append('\n\n\\begin{center}{\\LARGE ' + esc(t[1]) + '.}\\\\[6pt]\\rule{1.5cm}{0.4pt}\\end{center}\n\n')   # print: „Noter.“
            else: out.append('\n\n\\begin{center}\\textbf{\\large ' + esc(t[1]) + '}\\end{center}\n\n')
        elif k == 'sub':
            out.append(f'\n\n\\begin{{center}}{pending}\\\\[6pt]\n\\textbf{{\\Large {esc(t[1])}}}\\end{{center}}\n\n'); pending = None
        elif k == 'h2': out.append('\n\n\\begin{center}\\textbf{\\large ' + esc(t[1]).replace('. ', '.\\ \\ ', 1) + '}\\end{center}\n\n')
        elif k == 'h3': out.append('\n\n\\begin{center}\\textit{' + esc(t[1]) + '}\\end{center}\n\n')
        elif k == 'deco': out.append('\n\n\\begin{center}\\rule{2cm}{0.4pt}\\end{center}\n\n')
        elif k == 'pbeg': out.append('\n\n')
        elif k in OPEN: out.append(OPEN[k])
        elif k in ('ioff', 'scoff', 'sboff', 'spoff'): close()
        elif k == 'note':
            s = ''.join(out).rstrip(' '); out[:] = [s, r'\textsuperscript{' + PRINTNO[t[1] - 1] + '})']
        elif k == 'nnum':
            lab = PRINTNO[t[1] - 1]
            if lab == '12b': out.append('% PRINTED AS IS: the Noter label this note „12)“; its anchor in the text (p. 14) is 12b\n\\textsuperscript{12})')
            elif lab[-1] in 'bc': out.append(r'\textsuperscript{' + lab[:-1] + '} ' + lab[-1] + ')')
            else: out.append(r'\textsuperscript{' + lab + '})')
        elif k == 'w':
            w = REPL.get((sec == 'F' and 'B' or 'N', ti), t[1]); ms = [(o, p) for o, p in mk.get(ti, []) if o > 0]
            if ms:
                (o, p), = ms; n = 0
                for idx, ch in enumerate(w):
                    if ISL.match(ch):
                        if n == o: break
                        n += 1
                out.append(esc(w[:idx]) + '%' + M(p) + esc(w[idx:]))
            else: out.append(esc(w))
        elif k == 's': out.append(esc(REPL.get((sec == 'F' and 'B' or 'N', ti), t[1])))
    txt = ''.join(out)
    txt = re.sub(r'[ \t]+', ' ', txt); txt = re.sub(r' +([.,;:!?)])', r'\1', txt); txt = re.sub(r'\( +', '(', txt)
    txt = re.sub(r'\n +', '\n', txt); txt = re.sub(r' +\n', '\n', txt); txt = re.sub(r'\n{3,}', '\n\n', txt)
    # names the e-book gives in capitals outside its small-caps spans; the print sets them in small capitals
    txt = re.sub(r"\b(PH\.|HERBERT|HOBBES|HUME|JEVONS|PLATON|SPENCER|EBBINGHAUS|GRÜNBAUM|HEINRICH|LIPPS|RENAN)(?![A-Za-zæøå])",
                 lambda m: r'\textsc{' + m.group(1).capitalize() + '}', txt)
    return txt
def patch(txt, pages):
    for l in open(os.path.join(HERE, 'patches.tsv'), encoding='utf-8'):
        if not l.strip() or l.startswith('#'): continue
        p, f, r = l.rstrip('\n').split('\t')[:3]; r = r.replace('⏎', '\n')
        if int(p) not in pages: continue
        parts = re.split(r'(\n% --- p\. \d+ ---\n)', txt)
        # page chunk n = text after the marker of page n
        hits = 0
        for i in range(1, len(parts), 2):
            if parts[i].strip() == f'% --- p. {p} ---' and f in parts[i + 1]:
                parts[i + 1] = parts[i + 1].replace(f, r, 1); hits += 1
        if hits == 0 and int(p) in range(1, 2):
            if f in parts[0]: parts[0] = parts[0].replace(f, r, 1); hits = 1
        if hits != 1: print('PATCH NOT APPLIED:', p, f)
        txt = ''.join(parts)
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
body = patch(emit(BODY, AB, 'F'), range(1, 85)) + '\n\n\\begin{center}\\rule{2cm}{0.4pt}\\end{center}\n'
notes = patch(emit(NOTES, AN, 'N'), range(85, 91))
open(os.path.join(WORK, 'body.texfrag'), 'w', encoding='utf-8').write(wrap(body))
open(os.path.join(WORK, 'notes.texfrag'), 'w', encoding='utf-8').write(wrap(notes))
odd = sorted(set(c for c in body + notes if ord(c) > 127 and c not in 'æøåÆØÅéèêëáàâäóòôöúùûüíìîïçÉÖÜÄ„“ɔ'))
print('body.texfrag, notes.texfrag written | markers:', body.count('\\opage{'), '+', notes.count('\\opage{'), '| unusual characters:', odd)
tpl = open(os.path.join(HERE, 'template.tex'), encoding='utf-8').read()
out = os.path.join(BOOK, 'transcription.tex')
open(out, 'w', encoding='utf-8').write(tpl.replace('%%BODY%%\n', wrap(body)).replace('%%NOTES%%\n', wrap(notes)))
print('wrote', out)
