#!/usr/bin/env python3
"""ebook-method/kort-oversigt/parcmp.py -- paragraph starts in the transcription against the e-book's <p> starts
(2026-10-14).  draft.py takes paragraphs from the layer's indents, which a dash or a shifted word can mislead; the e-book
has its own paragraphs.  Lists (a) paragraphs the transcription begins that the e-book runs on, (b) e-book paragraphs the
transcription runs on: each goes to the image (a 'par' crop: is the boxed line indented?).
    python3 ebook-method/kort-oversigt/parcmp.py      -> .parts/parcmp.tsv (kind, page, first words)"""
import os, re, zipfile, html
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
BOOK = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt')
z = zipfile.ZipFile(os.path.join(BOOK, 'Kort_oversigt_over_den_nyere_filosofis_historie.epub'))
K = lambda s: re.sub(r'[^a-zæøåäöüéèàò0-9]', '', s.lower())[:22]
EP = []
for n in sorted(x for x in z.namelist() if re.search(r's0(0[3-9]|1[0-46])-', x)):
    for m in re.finditer(r'<p\b[^>]*>(.*?)</p>', z.read(n).decode('utf-8'), re.S):
        t = html.unescape(re.sub(r'<[^>]+>', ' ', m.group(1)))
        t = re.sub(r'^\s*\d{1,2}\s*\)?\s*(?=S\.)', '', t)
        if K(t): EP.append(K(t))
EPS = set(EP)
src = open(os.path.join(BOOK, 'transcription.tex'), encoding='utf-8').read()
src = src[src.find('% --- p. VII ---'):]
page = 'VII'; paras = []; cur = []; curp = page
for l in src.split('\n'):
    m = re.match(r'% --- p\. (\w+) ---', l)
    if m: page = m.group(1); continue
    if l.lstrip().startswith('%') : continue
    if not l.strip():
        if cur: paras.append((curp, ' '.join(cur))); cur = []
        continue
    if not cur: curp = page
    cur.append(l)
if cur: paras.append((curp, ' '.join(cur)))
clean = lambda t: re.sub(r'\\(opage|textsuperscript)\{\w+\}|\\[a-zA-Z]+\*?|[{}]', ' ', t).replace('---', '—')
TP = [(p, K(clean(t)), clean(t)) for p, t in paras if K(clean(t)) and not re.match(r'\s*\\(grouphead|chapterhead|chapterheadb|sectionhead|chapter|backmatter|end)', t)]
TPS = {k for p, k, t in TP}
out = []
for p, k, t in TP:
    if k not in EPS: out.append(('tex-only', p, ' '.join(t.split()[:8])))
alltex = K(' '.join(clean(t) for p, t in paras).replace(' ', ''))
flat = re.sub(r'\s', '', ' '.join(clean(t) for p, t in paras)).lower()
for k in EP:
    if k not in TPS: out.append(('ebook-only', '?', k))
open(os.path.join(BOOK, '.parts', 'parcmp.tsv'), 'w', encoding='utf-8').write('\n'.join('\t'.join(o) for o in out) + '\n')
print(len(TP), 'tex paragraphs,', len(EP), 'e-book paragraphs;', sum(o[0] == 'tex-only' for o in out), 'tex-only,', sum(o[0] == 'ebook-only' for o in out), 'e-book-only')
