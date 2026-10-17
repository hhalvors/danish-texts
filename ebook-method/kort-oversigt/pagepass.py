#!/usr/bin/env python3
"""ebook-method/kort-oversigt/pagepass.py -- the PAGE PASS (2026-10-07): whole pages read at the image against the
collated transcription, for what crops cannot settle: every footnote (both OCRs fail in the small type), verse and
centred lines, chapter heads, section rules, italics (the e-book's and the slant detector's), the places left open by
the collation, and a seeded random sample of ordinary pages that measures what is left.
Writes one fragment per page (the transcription between its page marker and the next) to .parts/pagepass/pN.tex, and
plants two CONTROL errors per reader group (a letter changed in a long word) -- recorded in controls-pp.tsv, never in
the transcription -- so each reader's attention is measured.  Readers return corrections as find/replace lines.
    python3 ebook-method/kort-oversigt/pagepass.py       -> .parts/pagepass/ (fragments, groups.tsv, controls-pp.tsv)"""
import os, re, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
BOOK = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt'); PP = os.path.join(BOOK, '.parts', 'pagepass')
os.makedirs(PP, exist_ok=True)
VERIFIED = set(range(39, 52)) | set(range(55, 70)) | set(range(77, 83)) | set(range(90, 96))   # read 23 Sep 2026
SPECIAL = set(int(x) for x in open(os.path.join(HERE, 'pagepass.txt')).read().split())
SPECIAL |= {52, 110, 231, 260, 292, 304,                                   # places left open by the e-book pass
            28, 131, 133, 149, 150, 157, 158, 193, 194, 272, 283, 307,     # the e-book's italics
            141, 162, 183, 184, 189, 245}                                  # a section rule at the page's foot?
SPECIAL -= VERIFIED
rnd = random.Random('kort-oversigt-pagepass-20261014')
pool = [p for p in range(8, 325) if p not in SPECIAL and p not in VERIFIED]
SAMPLE = sorted(rnd.sample(pool, 12))
PAGES = sorted(SPECIAL | set(SAMPLE))
T = open(os.path.join(BOOK, 'transcription.tex'), encoding='utf-8').read()
T = T[:T.find('\\backmatter')]
marks = [(m.start(), int(m.group(1))) for m in re.finditer(r'% --- p\. (\d+) ---', T)]
frag = {}
for k, (s, p) in enumerate(marks):
    e = marks[k + 1][0] if k + 1 < len(marks) else len(T)
    frag[p] = T[s:e]
groups = [PAGES[i::7] for i in range(7)]                     # 7 readers, pages spread through the book
ctl = []
for g, pages in enumerate(groups):
    for n, p in enumerate(pages):
        t = frag[p]
        if n in (1, len(pages) - 2):                          # two planted errors per reader
            cand = [m for m in re.finditer(r'(?<=\s)[a-zæøå]{8,}(?=[\s,.])', t)]
            m = rnd.choice(cand)
            w = m.group(0); i = rnd.randrange(2, len(w) - 2)
            nw = w[:i] + {'e': 'c', 'n': 'u', 'a': 'o', 'r': 'n', 'l': 'i', 'i': 'l', 'o': 'e'}.get(w[i], 'e') + w[i + 1:]
            if nw == w: nw = w[:i] + 'x' + w[i + 1:]
            t = t[:m.start()] + nw + t[m.end():]
            ctl.append(f'{g + 1}\t{p}\t{nw}\t{w}')
        open(os.path.join(PP, f'p{p}.tex'), 'w', encoding='utf-8').write(t)
open(os.path.join(PP, 'controls-pp.tsv'), 'w', encoding='utf-8').write('# group, page, planted, true\n' + '\n'.join(ctl) + '\n')
open(os.path.join(PP, 'groups.tsv'), 'w', encoding='utf-8').write('\n'.join(f'{g + 1}\t' + ' '.join(map(str, ps)) for g, ps in enumerate(groups)) + '\n')
print(len(PAGES), 'pages; sample:', SAMPLE)
for g, ps in enumerate(groups): print(g + 1, ps)
