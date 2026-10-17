#!/usr/bin/env python3
"""ebook-method/kort-oversigt/ebextra.py -- turn the e-book differences (ebookdiff.py's .parts/ebookdiff.tsv) and an
audit sample of the e-book's T votes (decisions.tsv, rule:ebook T) into sheets.py --extra items (2026-10-14):
    key <TAB> page <TAB> word to box <TAB> word before it
Keys: XE<n>|<page>|tex>ebook (an e-book difference) and XA<n>|<key> (an audited T vote).  The box is the transcription's
word (or, where the transcription lacks words, the word before the gap); sheets.py finds it among tesseract's boxes.
Arabic pages only (the Indledning, pp. VII-X, is read whole with the front matter).  Differences at a spot that is still
an open check are left to that check.  Seeded sample.
    python3 ebook-method/kort-oversigt/ebextra.py [--audit N]   -> ebook-method/kort-oversigt/extra-r2.tsv"""
import os, re, sys, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
BOOK = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt')
N = int(sys.argv[sys.argv.index('--audit') + 1]) if '--audit' in sys.argv else 80
clean = lambda w: re.sub(r'\\[a-zA-Z]+\{|[{}]', '', w)
openchk = set()
for l in open(os.path.join(BOOK, '.parts', 'collate', 'checks.tsv'), encoding='utf-8'):
    f = l.rstrip('\n').split('\t'); e = f[1].split('|', 1)[1].split('>', 1)[0]
    for w in e.split(): openchk.add((f[4], re.sub(r'\W', '', w).lower()))
out = []; n = 0
for l in open(os.path.join(BOOK, '.parts', 'ebookdiff.tsv'), encoding='utf-8'):
    p, kind, tex, eb, ctx = l.rstrip('\n').split('\t')
    if not p.isdigit(): continue
    pre = ctx.split(' [')[0].split()
    if tex.strip():
        w = clean(tex.split()[0]); prev = clean(pre[-1]) if pre else ''
    else:
        if not pre: continue
        w = clean(pre[-1]); prev = clean(pre[-2]) if len(pre) > 1 else ''
    if not re.search(r'\w', w): w, prev = prev, ''
    if (p, re.sub(r'\W', '', w).lower()) in openchk: continue
    n += 1; out.append(f'XE{n:03d}|{p}|{tex}>{eb}\t{p}\t{w}\t{prev}')
rows = []
for l in open(os.path.join(HERE, 'decisions.tsv'), encoding='utf-8'):
    f = l.rstrip('\n').split('\t')
    if len(f) >= 3 and f[1] == 'T' and f[2] == 'rule:ebook' and f[0].split('|')[0].isdigit():
        e = f[0].split('|', 1)[1].split('>', 1)[0]
        if re.search(r'[A-Za-zÆØÅæøå]{2}', e) and len(e.split()) == 1: rows.append(f[0])
rng = random.Random(20261014); rng.shuffle(rows)
# the T vote's context: the word before, from the transcription (first exact hit on its page)
TEX = open(os.path.join(BOOK, 'transcription.tex'), encoding='utf-8').read()
PG = dict(re.findall(r'% --- p\. (\d+) ---\n(.*?)(?=% --- p\. \w+ ---|\\end\{document\})', TEX, re.S))
k = 0
for key in rows:
    if k >= N: break
    p = key.split('|')[0]; e = key.split('|', 1)[1].split('>', 1)[0]
    words = [clean(x) for x in re.sub(r'(?m)^%.*$', '', PG.get(p, '')).split()]
    hits = [i for i, w in enumerate(words) if w == e]
    if len(hits) != 1: continue
    w0 = re.sub(r'#\d+$', '', key.split('>', 1)[1])                  # the box is TESSERACT's word (it read otherwise)
    if not re.search(r'\w', w0) or len(w0.split()) != 1: continue
    k += 1; out.append(f'XA{k:03d}|{key}\t{p}\t{w0}\t{words[hits[0] - 1] if hits[0] else ""}')
open(os.path.join(HERE, 'extra-r2.tsv'), 'w', encoding='utf-8').write('# key\tpage\tword to box\tword before\n' + '\n'.join(out) + '\n')
print(n, 'e-book differences,', k, 'audited T votes ->', 'extra-r2.tsv')
