#!/usr/bin/env python3
"""ebook-method/kort-oversigt/xresolve.py -- the blind readings of the --extra crops (ebextra.py's XE / XA items) set
against the two candidates (2026-10-14).  XE (an e-book difference): the transcription's span and the e-book's, each with
the word before, looked for in the reader's LINE/BOX (markup, spaces and quote kinds ignored) -> TEX / EBOOK / ?.
XA (an audited e-book T vote): the transcription's word (the draft = the e-book) or tesseract's in the BOX -> OK / WRONG / ?.
    python3 ebook-method/kort-oversigt/xresolve.py [TAG]   -> .parts/reads/xres-<TAG>.tsv (+ summary)"""
import os, re, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
RD = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt', '.parts', 'reads'); TAG = sys.argv[1] if len(sys.argv) > 1 else 'b2'
def nz(s):
    s = re.sub(r'</?sc>|</?sp>|\*|\^|\\textsuperscript\{|[{}]', '', s).replace('---', '—').replace('―', '—').replace('–', '—')
    s = re.sub(r'[’‘´`]', "'", s); s = re.sub(r'[„“”"]', '"', s)
    return re.sub(r'\s+', '', s)
idx = {l.split('\t')[1]: l.rstrip('\n').split('\t') for l in open(os.path.join(RD, f'sheets-{TAG}.tsv'), encoding='utf-8') if l.strip()}
EX = {l.split('\t')[0]: l.rstrip('\n').split('\t') for l in open(os.path.join(HERE, 'extra-r2.tsv'), encoding='utf-8') if l.strip() and not l.startswith('#')}
out = []
for fn in sorted(glob.glob(os.path.join(RD, f'r-{TAG}-*.tsv'))):
    for l in open(fn, encoding='utf-8'):
        f = (l.rstrip('\n').split('\t') + ['', '', ''])[:4]; cid = f[0].strip()
        if cid not in idx: continue
        key = idx[cid][3]
        if not key.startswith('X'): continue
        box, line, note = f[1], f[2], f[3]; hay = nz(line) + '|' + nz(box)
        _, p, w, prev = EX[key]
        if key.startswith('XE'):
            tex, eb = key.split('|', 2)[2].split('>', 1)
            ct, ce = nz(prev + tex), nz(prev + eb)
            a, b = (ct in hay), (ce in hay)
            if a == b: a, b = (nz(tex) in hay and nz(tex) != ''), (nz(eb) in hay and nz(eb) != '')
            v = 'TEX' if a and not b else 'EBOOK' if b and not a else '?'
        else:
            e, wv = key.split('|', 2)[2].split('>', 1); wv = re.sub(r'#\d+$', '', wv)
            a, b = nz(e) in nz(box), nz(wv) in nz(box)
            v = 'OK' if a and not b else 'WRONG' if b and not a else '?'
        out.append(f'{v}\t{key}\t{cid}\tBOX[{box}]\tLINE[{line}]\t{note}')
open(os.path.join(RD, f'xres-{TAG}.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
from collections import Counter
print(Counter((o.split('\t')[1][:2], o.split('\t')[0]) for o in out))
