#!/usr/bin/env python3
"""ebook-method/kort-oversigt/emarks.py -- the print's ITALICS and LETTERSPACING taken from the e-book (2026-10-14).
Neither OCR shows them; the e-book marks italics <i> and the print's letterspacing as <span class="underline-rw">
(88 spans: names in the Noter, emphasis in the text; checked at the image on samples).  The e-book's words are aligned
with the transcription's (difflib on letter-normalised tokens, as ebookdiff.py) and every marked span whose words
all align is written as  page <TAB> two words before <TAB> span  to italics.tsv / spaced.tsv in this folder; draft.py
--post wraps each in \\textit{} / \\emph{} within its page (each must match once).  Spans that do not align whole are
listed for a decision by hand.  Run on the collated text before --post (it reads transcription.tex as it stands).
    python3 ebook-method/kort-oversigt/emarks.py      -> italics.tsv, spaced.tsv (+ report)"""
import os, re, zipfile, html, difflib
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
BOOK = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt')
z = zipfile.ZipFile(os.path.join(BOOK, 'Kort_oversigt_over_den_nyere_filosofis_historie.epub'))
raw = ' '.join(z.read(n).decode('utf-8') for n in sorted(x for x in z.namelist() if re.search(r's0(0[3-9]|1[0-46])-', x)))
raw = re.sub(r'<title>.*?</title>', ' ', raw, flags=re.S)
raw = re.sub(r'<span class="underline-rw"[^>]*>', ' ⟦S ', raw); raw = re.sub(r'<i>', ' ⟦I ', raw); raw = re.sub(r'</i>', ' ⟧ ', raw)
raw = re.sub(r'</span>', ' ⟧ ', raw)                     # every span closes here (only the underline ones opened a mark)
t = html.unescape(re.sub(r'<[^>]+>', ' ', raw)).replace('\u00ad', '')
E = []; mode = []; stack = []
for w in t.split():
    if w in ('⟦S', '⟦I'): stack.append(w[1]); continue
    if w == '⟧':
        if stack: stack.pop()
        continue
    E.append((w, ''.join(stack)))
K = lambda w: re.sub(r'[^a-zæøåäöüéèàòìù0-9]', '', w.lower())
src = open(os.path.join(BOOK, 'transcription.tex'), encoding='utf-8').read()
a0 = src.find('% --- p. VII ---'); body = src[a0:]
T = []; page = 'VII'
for l in body.split('\n'):
    m = re.match(r'% --- p\. (\w+) ---', l)
    if m: page = m.group(1); continue
    if l.lstrip().startswith('%'): continue
    l = re.sub(r'(?<!\\)%.*$', '', l)
    for w in l.split():
        c = re.sub(r'\\(opage|textsuperscript)\{\w+\}|\\[a-zA-Z]+\*?|[{}]', '', w)
        if K(c): T.append((c, page))
a = [K(w) for w, p in T]; b = [K(w) for w, m in E if K(w)]; Em = [(w, m) for w, m in E if K(w)]
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
mapE = {}
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal' or (op == 'replace' and i2 - i1 == j2 - j1):
        for k in range(i2 - i1): mapE[j1 + k] = i1 + k
out = {'I': [], 'S': []}; bad = []
j = 0
while j < len(Em):
    m = Em[j][1][-1:] if Em[j][1] else ''
    if not m: j += 1; continue
    k = j
    while k < len(Em) and Em[k][1][-1:] == m: k += 1
    idx = [mapE.get(x) for x in range(j, k)]
    if None in idx or idx != list(range(idx[0], idx[0] + len(idx))):
        bad.append((m, ' '.join(w for w, _ in Em[j:k]))); j = k; continue
    pieces = []                                          # a span over a page turn: one piece per page
    for i in idx:
        if pieces and T[i][1] == T[pieces[-1][-1]][1]: pieces[-1].append(i)
        else: pieces.append([i])
    for pc in pieces:
        i0 = pc[0]; pg = T[i0][1]
        before = ' '.join(T[i][0] for i in range(max(0, i0 - 2), i0) if T[i][1] == pg)
        out[m].append(f'{pg}\t{before}\t' + ' '.join(T[i][0] for i in pc))
    j = k
# the e-book's underline-rw spans proved NOT to be the print's letterspacing (zoom-02, spacecmp.py, 2026-10-14): they are
# kept for the record in .parts/ebook-underline.tsv only; the Noter's letterspacing is measured (spaced-noter.tsv)
for m, fn in (('I', os.path.join(HERE, 'italics.tsv')), ('S', os.path.join(BOOK, '.parts', 'ebook-underline.tsv'))):
    open(fn, 'w', encoding='utf-8').write(f'# page\twords before\tspan  (from the e-book by emarks.py, {"italics" if m == "I" else "letterspacing"}; checked at the image on samples)\n' + '\n'.join(out[m]) + '\n')
print(len(out['I']), 'italic spans,', len(out['S']), 'spaced spans placed;', len(bad), 'not placed:')
for m, s in bad: print('  ', m, s[:90])
