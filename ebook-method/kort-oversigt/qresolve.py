#!/usr/bin/env python3
"""ebook-method/kort-oversigt/qresolve.py -- the blind readings of the e-book-difference crops (qsheets.py; readers'
r-q*.tsv: id, BOX, LINE, NOTE) against the two readings (the transcription's t, the e-book's e).  For each: E (the
e-book's reading is the print's), T (the transcription's is), RULE/BLANK (a section rule / white line before the
marked line), or HAND (neither fits, or the reading is doubtful) -- printed for a decision by hand.  Comparison is
on the BOX first (a reader's LINE outside the box has dropped a word once), whitespace-sensitive for word divisions.
    python3 ebook-method/kort-oversigt/qresolve.py      -> .parts/reads/qdecisions.tsv"""
import os, re, glob
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
RD = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt', '.parts', 'reads')
Q = {l.split('\t')[0]: l.rstrip('\n').split('\t') for l in open(os.path.join(RD, 'qsheets.tsv'), encoding='utf-8') if l.strip()}
READ = {}
for f in sorted(glob.glob(os.path.join(RD, 'r-q*.tsv'))):
    for l in open(f, encoding='utf-8'):
        x = l.rstrip('\n').split('\t')
        if len(x) >= 3: READ[x[0]] = (x[1], x[2], x[3] if len(x) > 3 else '')
def n(s): return re.sub(r'\s+', ' ', s.replace('—', '—').replace('---', '—').replace('’', "'").replace('‘', "'").replace('”', '“').replace('"', '“')).strip()
def nz(s): return n(s).replace(' ', '')
out = []
for qid, q in Q.items():
    _, p, t, e, kind = q[:5]
    if qid not in READ: out.append((qid, p, kind, t, e, 'UNREAD', '')); continue
    box, line, note = READ[qid]
    if kind == 'rule':
        b = box.strip().upper(); d = 'RULE' if b.startswith('RULE') else 'BLANK' if b.startswith('BLANK') else 'NONE' if b.startswith('NONE') else 'HAND'
        out.append((qid, p, kind, t, e, d, f'{box} | {line} | {note}')); continue
    hay = ' ' + n(box) + ' '; hayz = nz(box)
    def has(x):
        if kind == 'space': return (' ' + n(x) + ' ') in hay or (n(x) and hay.strip().startswith(n(x)) ) or (n(x) and hay.strip().endswith(n(x)))
        return nz(x) in hayz if nz(x) else False
    ht, he = has(t), has(e)
    if kind == 'space':                       # a division: the spaced form must be absent for the joined one to win
        tj, ej = ' ' in n(t), ' ' in n(e)
    d = 'T' if ht and not he else 'E' if he and not ht else 'HAND'
    if re.search(r'doubt|unsure|misprint|⟨\?⟩|unclear|cannot', note, re.I) and d != 'HAND': d += '?'
    out.append((qid, p, kind, t, e, d, f'{box} | {line} | {note}'))
with open(os.path.join(RD, 'qdecisions.tsv'), 'w', encoding='utf-8') as f:
    for r in out: f.write('\t'.join(map(str, r)) + '\n')
import collections; print(collections.Counter(r[5] for r in out))
for r in out:
    if r[5] not in ('T', 'E', 'RULE', 'NONE', 'BLANK'): print('\t'.join(map(str, r)))
