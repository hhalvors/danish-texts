#!/usr/bin/env python3
"""(adapted 2026-10-17 for kort-oversigt: TITLE_PDF 5, four strata over pp. 1-95; copied 2026-10-12 from ebook-method/udvalgte-stykker/; TITLE_PDF 11) ebook-method/kort-oversigt/pagecheck.py (2026-10-11, adapted from speculative-logik/pagecheck.py) -- the SAMPLED PAGE
CHECK: whole printed pages chosen at random (seeded) are transcribed BLIND at the image by a reader who sees no
transcription (PAGECHECK-BRIEF.md), and the reading is compared word by word with the transcription (pagemap.TEXFILE).
Every difference is then decided by hand (the reader may be wrong: tesseract's reading is printed beside it; doubtful
ones are cropped with zoom.py), and the confirmed errors give an error rate with a 95 % upper bound.
    python3 ebook-method/kort-oversigt/pagecheck.py sample [N] [SEED]  -> .parts/pagecheck/sample.tsv  (pilot: 4 pages of
                                                                            pp. 1-44, two strata, + the title page = page 0)
    python3 ebook-method/kort-oversigt/pagecheck.py sheets            -> .render/udvalgte-stykker-pc-NN.png + sheets.tsv
    python3 ebook-method/kort-oversigt/pagecheck.py selftest          the transcription read back must give 0 differences,
                                                                         and injected faults (a word, a letter, a comma, an
                                                                         italic, a letterspacing) must all show
    python3 ebook-method/kort-oversigt/pagecheck.py compare READINGS  -> .parts/pagecheck/diffs.tsv
    python3 ebook-method/kort-oversigt/pagecheck.py rate              -> the error rate from column 1 of diffs.tsv
READINGS: the reader's file: one printed line per line, each page opened by `=== p. N` (`=== p. 0` = the title page).
Decisions (column 1 of diffs.tsv, by hand): T = transcription right (reader slip), E = word error, P = punctuation
error, M = emphasis/markup error (italics, letterspacing, small caps), ? = undecided.
ROUNDS (2026-10-11): PCRUN=2 (environment) = round 1 of the whole book, pp. 45-98: one stratum, no title page, sheets
udvalgte-stykker-pc2-NN.png, files sample-2.tsv, sheets-2.tsv, diffs-2.tsv, words-2.tsv (the reader writes reading-2.tsv).
    PCRUN=2 python3 ebook-method/kort-oversigt/pagecheck.py sample 3 202610112; ... sheets; ... selftest
PCRUN=3 = round 2, pp. 99-161: three strata (99-121: 2 pages, 122-126: 1, 127-161: 1), sheets pc3-NN, files *-3.tsv.
    PCRUN=3 python3 ebook-method/kort-oversigt/pagecheck.py sample 4 202610113; ... sheets; ... selftest
PCRUN=5 = round 4, pp. 222-306: strata 222-240, 241-259, 260-278, 279-299 and the Anmærkninger 301-306, sheets pc5-NN, files *-5.tsv.
    PCRUN=5 python3 ebook-method/kort-oversigt/pagecheck.py sample 5 202610115; ... sheets; ... selftest
PCRUN=4 = round 3, pp. 162-221: four strata (163-181, 182-184 letterspaced Kierkegaard, 185-198, 199-221), sheets pc4-NN, files *-4.tsv.
    PCRUN=4 python3 ebook-method/kort-oversigt/pagecheck.py sample 4 202610114; ... sheets; ... selftest
Footnotes: the transcription's \\footnote[k]{X} is compared as the mark „*)“ at its word and the note „*) X“ at the page
foot, where the reader writes it (marks normalised to ⁎) on both sides before the italics are read)."""
import os, re, sys, random, subprocess, difflib, math
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE); import pagemap as C
B = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt'); PC = os.path.join(B, '.parts', 'pagecheck'); OUT = os.path.join(B, '.render')
TEXF = os.path.join(B, C.TEXFILE); DPI = 220; TITLE_PDF = 5   # kort-oversigt: the title page is PDF 5
STRATA = [(1, 24), (25, 49), (50, 73), (74, 95)]   # kort-oversigt (2026-10-17): Indledning-II; II-IV; V-VI; VII-VIII.  Earlier books:   # religioese (2026-10-17): the two own pieces; Platon-Spinoza; Pascal + Sibbern; Rationalisme-Bakkehus; the four literary pieces   # oplevelse (2026-10-14): the title essay in two; Sociologi + Om Trøst; Bønnen + To Præster; Madvig + Aristoteles
RUN = os.environ.get('PCRUN', '1'); SUF = '' if RUN == '1' else '-' + RUN; PCTAG = 'pc' if RUN == '1' else 'pc' + RUN
if RUN == '2': STRATA = [(45, 98)]                 # round 1: sections II-III
if RUN == '3': STRATA = [(99, 121), (122, 126), (127, 161)]   # round 2: sections IV-V; a stratum of its own for Sibbern's heavily letterspaced pp. 122-126 (short spaced words off the l3 candidate lines go unread there)
if RUN == '4': STRATA = [(163, 181), (182, 184), (185, 198), (199, 221)]   # round 3: sections VI-VII; a stratum for Kierkegaard's heavily letterspaced pp. 182-184 (the pp. 183-184 passage)
if RUN == '5': STRATA = [(222, 240), (241, 259), (260, 278), (279, 299), (301, 306)]   # round 4: section VIII in four strata + one page of the ANMÆRKNINGER (p. 300 blank; bold page references are not compared -- the m5 anm strips read them)
EXCLUDE = set()                                   # kort-oversigt: the whole text is in the scan
os.makedirs(PC, exist_ok=True)
cmd = sys.argv[1] if len(sys.argv) > 1 else ''
def pdf_of(p): return TITLE_PDF if p == 0 else C.pdfpage(p)

def sample(n=4, seed=20261011):
    rnd = random.Random(seed); per = [n // len(STRATA) + (1 if i < n % len(STRATA) else 0) for i in range(len(STRATA))]
    pages = []
    for (a, b), k in zip(STRATA, per): pages += sorted(rnd.sample([p for p in range(a, b + 1) if p not in EXCLUDE], k))
    pass                                            # moderne-filosoffer: the front matter is read apart (frontread)
    with open(os.path.join(PC, f'sample{SUF}.tsv'), 'w') as fh:
        fh.write(f'# seed {seed}, {n} pages stratified over {STRATA}' + (f' + the title page (0 = PDF {TITLE_PDF})' if RUN == '1' else '') + '\n')
        for p in pages: fh.write(f'{p}\n')
    return pages
def read_sample(): return [int(l) for l in open(os.path.join(PC, f'sample{SUF}.tsv')) if l.strip() and not l.startswith('#')]

def lines_of(pdf):
    xml = subprocess.run(['pdftotext', '-bbox-layout', '-f', str(pdf), '-l', str(pdf), C.scan_path(), '-'], capture_output=True, text=True).stdout
    W, H = [float(x) for x in re.search(r'<page width="([\d.]+)" height="([\d.]+)"', xml).groups()]
    L = [tuple(float(v) for v in m) for m in re.findall(r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">', xml)]
    return W, H, sorted(L, key=lambda b: b[1])

def sheets():
    import tempfile
    from PIL import Image, ImageDraw, ImageFont
    try: font = ImageFont.truetype('DejaVuSans.ttf', 22)
    except OSError: font = ImageFont.load_default()
    strips = []; TMP = tempfile.mkdtemp(dir='/tmp')
    for p in read_sample():
        pdf = pdf_of(p); W, H, L = lines_of(pdf)
        base = os.path.join(TMP, f'p{pdf}')
        subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(pdf), '-l', str(pdf), '-png', '-singlefile', '-gray', C.scan_path(), base], check=True)
        im = Image.open(base + '.png').convert('RGB'); sc = im.width / W
        lab0 = f'title page (PDF {TITLE_PDF})' if p == 0 else f'p. {p}'
        if p == 0 or not L:                         # the title page: whole, in two halves
            cuts = [0, H / 2, H]; x0, x1 = 0, W
        else:
            x0 = max(0, min(b[0] for b in L) - 10); x1 = min(W, max(b[2] for b in L) + 10)
            top, bot = max(0, min(b[1] for b in L) - 8), min(H, max(b[3] for b in L) + 8)
            cuts = [top]; n = 0
            for a, b in zip(L, L[1:]):
                n += 1
                if n >= 10 and b[1] - a[3] > 0: cuts.append((a[3] + b[1]) / 2); n = 0
            cuts.append(bot)
        for k, (y0, y1) in enumerate(zip(cuts, cuts[1:]), 1):
            c = im.crop((int(x0 * sc), int(y0 * sc), int(x1 * sc), int(y1 * sc)))
            lab = Image.new('RGB', (c.width, 30), 'white')
            ImageDraw.Draw(lab).text((4, 3), f'{lab0}   strip {k} of {len(cuts) - 1}', fill=(0, 0, 0), font=font)
            s = Image.new('RGB', (c.width, c.height + 34), 'white'); s.paste(lab, (0, 0)); s.paste(c, (0, 32)); strips.append((p, k, s))
    PER = 2; rows = []
    for i in range(0, len(strips), PER):
        part = strips[i:i + PER]; wd = max(s.width for _, _, s in part)
        sh = Image.new('RGB', (wd, sum(s.height for _, _, s in part) + 12 * len(part)), 'white'); y = 0
        for _, _, s in part: sh.paste(s, (0, y)); y += s.height + 12
        name = f'kort-oversigt-{PCTAG}-{i // PER + 1:02d}.png'; sh.save(os.path.join(OUT, name))
        rows += [f'{name}\t{p}\t{k}' for p, k, _ in part]
    open(os.path.join(PC, f'sheets{SUF}.tsv'), 'w').write('\n'.join(rows) + '\n')
    print(len(strips), 'strips on', (len(strips) + PER - 1) // PER, 'sheets in', OUT)

# ---------- comparison ----------
def tex_page(p):
    T = open(TEXF, encoding='utf-8').read()
    if p == 0:
        a = T.index('% --- front matter'); return T[a:T.index('\\end{titlepage}', a)]
    a = T.index(f'% --- p. {p} ---'); b = T.find(f'% --- p. {p + 1} ---')
    if b < 0: b = T.index('\\end{document}', a)
    return T[a:b]
def brace(s, i):
    d = 0
    for j in range(i, len(s)):
        d += {'{': 1, '}': -1}.get(s[j], 0)
        if d == 0: return j + 1
    return len(s)
def unwrap(x, cmd, f):                              # \cmd{...} (nested braces allowed) -> f(inner)
    while '\\' + cmd + '{' in x:
        i = x.index('\\' + cmd + '{'); j = brace(x, i + len(cmd) + 1)
        x = x[:i] + f(x[i + len(cmd) + 2:j - 1]) + x[j:]
    return x
def tex_to_stream(s):
    notes = []                                       # round 1: footnotes to the page foot, the mark at the word
    while '\\footnote[' in s:
        i = s.index('\\footnote['); k = int(s[i + 10]); j = brace(s, s.index('{', i))
        notes.append('⁎)' * 1 + ' ' + s[s.index('{', i) + 1:j - 1]); s = s[:i] + '⁎)' + s[j:]
    if notes: s = s.rstrip('\n') + '\n' + '\n'.join(notes) + '\n'
    s = re.sub(r'\\(addcontentsline|markboth)\{[^{}]*\}\{[^{}]*\}(\{[^{}]*\})?', ' ', s)   # moderne-filosoffer: heading furniture
    s = re.sub(r'\\chapter\*\{([^{}]*)\}', r' \1 ', s); s = re.sub(r'\\(grouphead|chapterhead|chapterheadb)\{([^{}]*)\}\{([^{}]*)\}', r' \2 \3 ', s)
    s = re.sub(r'\\sectionhead\{([^{}]*)\}', r' \1 ', s); s = re.sub(r'\\textsuperscript\{(\d+)\}', r'^\1', s)
    s = re.sub(r'(?m)^% --- p\. \d+ ---$', '', s); s = re.sub(r'\\setcounter\{footnote\}\{0\}%?', '', s); s = re.sub(r'\\opage\{\d+\}', '', s)
    s = re.sub(r'(?<!\\)%[^\n]*\n', lambda m: ' ' if 'PRINTED' in m.group(0) or 'Greek' in m.group(0) else '', s)   # a line-end % joins the word
    s = re.sub(r'(?<!\\)%[^\n]*$', '', s)
    s = s.replace(',{},', ',,')
    s = re.sub(r'\\anthsection\{([^{}]*)\}\s*\{([^{}]*)\}', r' \1 \2 ', s)
    s = unwrap(s, 'excerpthead', lambda x: ' ' + x.replace('\\\\', ' ') + ' ')
    s = re.sub(r'\\sectionrule|\\begin\{intro\}|\\end\{intro\}|\\begin\{quote\}|\\end\{quote\}|\\begin\{smallquote\}|\\end\{smallquote\}|\\clearpage|\\begin\{titlepage\}|\\begin\{center\}|\\end\{center\}|\\vspace\*?\{[^}]*\}|\\quad|\\,', ' ', s)
    s = re.sub(r'\\\\(\[[^\]]*\])?', ' ', s)
    s = unwrap(s, 'textsc', lambda x: ' '.join('<' + w + '>' for w in x.split()))
    s = unwrap(s, 'emph', lambda x: ' '.join('_' + w + '_' for w in x.split()))
    s = unwrap(s, 'textit', lambda x: ' '.join('*' + w.strip('_') + '*' if not w.startswith('_') else '_*' + w.strip('_') + '*_' for w in x.split()))
    s = re.sub(r'\{\\(Huge|huge|LARGE|Large|large|small|footnotesize)\s', '{', s)
    s = s.replace('\\dots{}', '...').replace('---', '—').replace('\\&', '&')
    s = re.sub(r'\\[a-zA-Z]+', ' ', s).replace('{', '').replace('}', '')
    return s
def tokens(x, emph=True):
    x = re.sub(r'\*+\)', '⁎)', x)                      # round 1: a note mark is no italic asterisk
    x = re.sub(r'<sc>(.*?)</sc>', lambda m: ' '.join('<' + w + '>' for w in m.group(1).split()), x, flags=re.S)
    x = re.sub(r'_=\s*\n\s*_', '', x)                # round 3: a letterspaced run closed and reopened at each line (`Sand_=` / `_heden`):
    x = re.sub(r'_\s*\n\s*_', ' ', x)                #   one run, the divided word joined (\w matches _, so the next line used to glue „Sand__heden“)
    x = re.sub(r'(\w)=\s*\n\s*', r'\1', x)            # a word divided at the line end (the reader writes =)
    x = re.sub(r'(?<![\w*])\*([^*\n]+?)\*(?![\w*])', lambda m: ' '.join('*' + w + '*' for w in m.group(1).split()), x)
    x = re.sub(r'(?<![\w_])_([^_\n]+?)_(?![\w_])', lambda m: ' '.join('_' + w + '_' for w in m.group(1).split()), x)
    x = x.replace('„', ' „ ').replace('“', ' “ ')
    toks = re.findall(r'<[^<>\s]+>|_\*[^\s]+?\*_|\*[^*\s]+\*|_[^_\s]+_|[\wæøåÆØÅéöüäÄÖÜßœ·\u0370-\u03ff\u1f00-\u1fff-]+|[^\s\w]', x)
    out = []
    for t in toks:
        flag = ''
        if t.startswith('<'): t, flag = t[1:-1], 'c'
        if t.startswith('_*'): t, flag = t[2:-2], 'si'
        elif t.startswith('*') and len(t) > 2: t, flag = t[1:-1], 'i'
        elif t.startswith('_') and len(t) > 2: t, flag = t[1:-1], 's'
        for sub in re.findall(r'[\wæøåÆØÅéöüäÄÖÜßœ·\u0370-\u03ff\u1f00-\u1fff-]+|[^\s\w]', t) or [t]:
            out.append((sub.upper() if flag == 'c' else sub, flag if emph and re.match(r'\w', sub) else ''))
    return out
def read_stream(txt):
    return '\n'.join(l.rstrip() for l in txt.split('\n') if l.strip() and not re.match(r'\s*(FOLIO|SIG|HEAD|RULE)\b', l))
def witness_ctx(p, word):
    f = os.path.join(B, '.parts', 'collate', 'ocr', f'p{p}.tsv')
    if p == 0 or not os.path.exists(f): return '-'
    ws = [r.split('\t')[11] for r in open(f, encoding='utf-8').read().splitlines()[1:] if len(r.split('\t')) == 12 and r.split('\t')[11].strip()]
    txt = ' '.join(ws); key = re.sub(r'\W', '', word.lower())[:6]
    i = txt.lower().find(key) if key else -1
    return 'tesseract: ' + (txt[max(0, i - 30):i + 40] if i >= 0 else '-')
def diff_page(p, reading):
    A, Bt = tokens(tex_to_stream(tex_page(p))), tokens(read_stream(reading)); rows = []
    sm = difflib.SequenceMatcher(None, [w.replace('-', '').upper() if f == 'c' else w.replace('-', '') for w, f in A],
                                 [w.replace('-', '').upper() if f == 'c' else w.replace('-', '') for w, f in Bt], autojunk=False)
    for op, a0, a1, b0, b1 in sm.get_opcodes():
        if op == 'equal':
            for (w1, f1), (w2, f2) in zip(A[a0:a1], Bt[b0:b1]):
                if f1 != f2: rows.append(['?', str(p), 'EMPH', f'{w1}[{f1 or "-"}]', f'{w2}[{f2 or "-"}]', ''])
            continue
        ta = ' '.join(w for w, _ in A[a0:a1]); tb_ = ' '.join(w for w, _ in Bt[b0:b1])
        if ta.replace('-', '').replace(' ', '') == tb_.replace('-', '').replace(' ', '') or {ta, tb_} <= {'—', '-', ''}: continue
        ctx = ' '.join(w for w, _ in A[max(0, a0 - 5):a0]) + ' [' + ta + '] ' + ' '.join(w for w, _ in A[a1:a1 + 5])
        rows.append(['?', str(p), 'PUNCT' if not re.search(r'\w', ta + tb_) else 'WORD', ta, tb_, ctx + '  ||  ' + witness_ctx(p, (ta or tb_).split(' ')[0])])
    return rows, sum(1 for w, _ in Bt if re.match(r'\w', w))
def compare(readfile):
    R = open(readfile, encoding='utf-8').read(); pages = re.split(r'(?m)^=== p\. (\d+)\s*$', R)
    rows = []; stats = []
    for i in range(1, len(pages), 2):
        p = int(pages[i]); r_, n = diff_page(p, pages[i + 1]); rows += r_; stats.append((p, n))
    with open(os.path.join(PC, f'diffs{SUF}.tsv'), 'w', encoding='utf-8') as fh:
        fh.write('#decision\tpage\tkind\ttranscription\treading\tcontext || OCR witness\n')
        for r in rows: fh.write('\t'.join(r) + '\n')
    open(os.path.join(PC, f'words{SUF}.tsv'), 'w').write(''.join(f'{p}\t{n}\n' for p, n in stats))
    from collections import Counter
    print(f'{len(stats)} pages, {sum(n for _, n in stats)} words read; differences:', dict(Counter(r[2] for r in rows)))
def as_reading(p):                                 # the transcription written back in the reader's notation
    s = tex_to_stream(tex_page(p))
    s = re.sub(r'<([^<>\s]+)>', r'<sc>\1</sc>', s)
    return s
def selftest():
    ok = True
    for p in read_sample():
        r_, n = diff_page(p, as_reading(p))
        print(f'p. {p}: read back {n} words, {len(r_)} differences' + ('' if not r_ else ' ' + str(r_[:3]))); ok &= not r_
    p = [q for q in read_sample() if q][0]; t = as_reading(p); ws = t.split(); faults = 0
    i = next(k for k, w in enumerate(ws) if re.fullmatch(r'[a-zæøå]{5,}', w)); ws[i] = ws[i][:-1] + ('x' if ws[i][-1] != 'x' else 'y'); faults += 1   # a letter
    j = next(k for k, w in enumerate(ws) if k > i + 5 and re.fullmatch(r'[a-zæøå]{4,}', w)); del ws[j]; faults += 1                          # a word
    k = next(k for k, w in enumerate(ws) if k > j + 5 and w.endswith(',') and len(w) > 2); ws[k] = ws[k][:-1]; faults += 1                  # a comma
    it = [k for k, w in enumerate(ws) if w.startswith('*') and w.endswith('*')]
    if it: ws[it[0]] = ws[it[0]].strip('*'); faults += 1                                                                                    # an italic
    sp = [k for k, w in enumerate(ws) if k > k and re.fullmatch(r'[a-zæøå]{4,}', w)]
    m = next(k_ for k_, w in enumerate(ws) if k_ > k + 5 and re.fullmatch(r'[a-zæøå]{4,}', w)); ws[m] = '_' + ws[m] + '_'; faults += 1     # a letterspacing
    r_, n = diff_page(p, ' '.join(ws))
    print(f'injected {faults} faults on p. {p}: {len(r_)} differences found:'); [print('   ', r[2:5]) for r in r_]
    ok &= len(r_) == faults
    print('SELFTEST', 'PASSED' if ok else 'FAILED')
def rate():
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(PC, f'diffs{SUF}.tsv'), encoding='utf-8') if not l.startswith('#')]
    words = sum(int(l.split('\t')[1]) for l in open(os.path.join(PC, f'words{SUF}.tsv')))
    from collections import Counter
    c = Counter(r[0] for r in rows)
    def upper(k):
        lo, hi = 0.0, 50.0 + 3 * k
        for _ in range(60):
            mid = (lo + hi) / 2; cdf = sum(math.exp(-mid) * mid ** j / math.factorial(j) for j in range(k + 1))
            lo, hi = (mid, hi) if cdf > 0.05 else (lo, mid)
        return hi
    print(f'words read {words}; decisions {dict(c)}')
    for lab, k in (('word errors (E)', c.get('E', 0)), ('punctuation (P)', c.get('P', 0)), ('emphasis/markup (M)', c.get('M', 0))):
        print(f'  {lab}: {k} = {1000 * k / words:.2f} per 1000 words (95 % upper {1000 * upper(k) / words:.2f})')
    if c.get('?'): print('  UNDECIDED:', c['?'])
if cmd == 'sample': print('sample:', sample(*(int(x) for x in sys.argv[2:4])))
elif cmd == 'sheets': sheets()
elif cmd == 'selftest': selftest()
elif cmd == 'compare': compare(sys.argv[2])
elif cmd == 'rate': rate()
else: print(__doc__)
