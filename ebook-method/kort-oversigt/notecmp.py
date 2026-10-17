#!/usr/bin/env python3
"""notecmp.py (2026-10-14) -- the footnotes of transcription.tex, in order, against the e-book's 141 numbered notes
(s017-Notes-01.xhtml): aligned by their letters, so that a note split in two, two notes run together, a note lost or a
note set on the wrong page shows.  A FINDING AID: the print governs (the e-book renumbers the page notes 1-141).
    python3 ebook-method/kort-oversigt/notecmp.py"""
import os, re, sys, zipfile, html, difflib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import pagemap as C
T = open(os.path.join(C.BOOKDIR, 'transcription.tex'), encoding='utf-8').read()
def notes(t):
    out, i, page = [], 0, None
    for m in re.finditer(r'% --- p\. (\d+) ---|\\footnote\[(\d+)\]\{', t):
        if m.group(1): page = int(m.group(1)); continue
        j = m.end(); d = 1
        while d: d += {'{': 1, '}': -1}.get(t[j], 0); j += 1
        out.append((page, int(m.group(2)), t[m.end():j - 1]))
    return out
N = notes(T[T.index('\\mainmatter'):] if '\\mainmatter' in T else T)
z = zipfile.ZipFile(os.path.join(C.BOOKDIR, 'Kort_oversigt_over_den_nyere_filosofis_historie.epub'))
x = z.read('OPS/s017-Notes-01.xhtml').decode('utf-8')
E = [html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<span class="num-note-rw".*?</span>', '', b.split('</p>')[0], flags=re.S))) for b in x.split('epub:type="rearnote"')[1:]]
E = [re.sub(r'\s+', ' ', e).strip() for e in E]
lt = lambda s: re.sub(r'[^a-zæøåäöüéèà]', '', re.sub(r'\\[a-z]+\{?', '', s.lower()))
a, b = [lt(n[2]) for n in N], [lt(e) for e in E]
print(f'transcription: {len(N)} notes; e-book: {len(E)}')
# greedy alignment by ratio
i = j = 0
while i < len(a) and j < len(b):
    r = difflib.SequenceMatcher(None, a[i], b[j], autojunk=False).ratio()
    if r > 0.75: i += 1; j += 1; continue
    # merged: our note = e-book j + j+1 ?
    r2 = difflib.SequenceMatcher(None, a[i], b[j] + (b[j + 1] if j + 1 < len(b) else ''), autojunk=False).ratio()
    r3 = difflib.SequenceMatcher(None, a[i] + (a[i + 1] if i + 1 < len(a) else ''), b[j], autojunk=False).ratio()
    if r2 > 0.75 and r2 > r3: print(f'MERGED  p. {N[i][0]} [{N[i][1]}] = e-book {j + 1}+{j + 2}: {N[i][2][:70]}'); i += 1; j += 2; continue
    if r3 > 0.75: print(f'SPLIT   p. {N[i][0]} [{N[i][1]}]+[{N[i + 1][1]}] = e-book {j + 1}: {E[j][:70]}'); i += 2; j += 1; continue
    ra = max((difflib.SequenceMatcher(None, a[i], b[k], autojunk=False).ratio(), k) for k in range(j, min(len(b), j + 4)))
    rb = max((difflib.SequenceMatcher(None, a[k], b[j], autojunk=False).ratio(), k) for k in range(i, min(len(a), i + 4)))
    if ra[0] > 0.75 and (ra[1] - j) <= (rb[1] - i or 9):
        for k in range(j, ra[1]): print(f'MISSING e-book {k + 1} (after p. {N[i - 1][0] if i else "-"}): {E[k][:80]}')
        j = ra[1]; continue
    if rb[0] > 0.75:
        for k in range(i, rb[1]): print(f'EXTRA   p. {N[k][0]} [{N[k][1]}]: {N[k][2][:80]}')
        i = rb[1]; continue
    print(f'DIFFER  p. {N[i][0]} [{N[i][1]}] ({r:.2f}): {N[i][2][:60]} || e-book {j + 1}: {E[j][:60]}'); i += 1; j += 1
for k in range(i, len(a)): print(f'EXTRA   p. {N[k][0]} [{N[k][1]}]: {N[k][2][:80]}')
for k in range(j, len(b)): print(f'MISSING e-book {k + 1}: {E[k][:80]}')
