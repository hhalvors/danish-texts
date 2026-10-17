#!/usr/bin/env python3
"""ebook-method/kort-oversigt/treads.py -- reads.py adapted for the AUDIT of the e-book's T votes (2026-10-07: the e-book shares
some of the layer's faults, e.g. giede for glede); prints, never writes.  Original docstring:
ebook-method/kort-oversigt/reads.py -- turn the blind readings of the crop sheets (sheets.py) into decisions.
Readers report, per check, BOX (the boxed print with a word either side), LINE (the whole printed line) and NOTE.
For each check the draft's reading (e) and tesseract's (w) are set into their context and looked for in the reader's
LINE/BOX, whitespace ignored (quote kinds and dashes kept distinct); if exactly one fits, it is the decision (T / W);
word-division checks are compared with the spaces.  Everything else is printed for a decision by hand.

    python3 ebook-method/kort-oversigt/reads.py            dry run: decisions found, the rest listed
    python3 ebook-method/kort-oversigt/reads.py --write    append the found ones to decisions.tsv (note "image, blind read")"""
import os, re, sys, glob, shutil, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
BOOK = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt'); DECF = os.path.join(HERE, 'decisions.tsv')
L = 'A-Za-zÀ-ÖØ-öø-ÿ0-9'; letters = lambda s: re.sub('[^' + L + ']', '', s)
def q(s):
    s = s.replace('---', '—').replace('--', '–').replace('∅', '').replace('\\dots{}', '...')
    s = re.sub(r'\\opage\{\d+\}|\\footnote(mark)?\[\d\]\{?|\\[a-zA-Z]+\{|[{}]', '', s)
    return s.replace('"', '“')
nz = lambda s: re.sub(r'\s+', '', q(s))
sp = lambda s: re.sub(r'\s+', ' ', q(s)).strip()
CH = {}
for l in open(os.path.join(BOOK, '.parts', 'collate', 'checks-tvotes.tsv'), encoding='utf-8'):
    f = l.rstrip('\n').split('\t'); CH[f[0]] = f
# readings are matched to checks by PAGE and CONTEXT, not by id: ids change whenever the draft is rebuilt.
# r-<tag>.tsv (cid, BOX, LINE, NOTE) goes with sheets-<tag>.tsv (sheet, cid, page) made when it was read.
READ = []
for fn in sorted(glob.glob(os.path.join(BOOK, '.parts', 'reads', 'r-t[12].tsv'))):
    tag = os.path.basename(fn)[2:-4]; idx = os.path.join(BOOK, '.parts', 'reads', f'sheets-{tag}.tsv')
    pg = {l.split('\t')[1]: int(l.split('\t')[2]) for l in open(idx, encoding='utf-8') if l.strip()}
    for l in open(fn, encoding='utf-8'):
        f = l.rstrip('\n').split('\t')
        if len(f) >= 3 and f[0] in pg: READ.append((tag + ':' + f[0], pg[f[0]], f[1], f[2], f[3] if len(f) > 3 else ''))
done = set()
done = set()   # audit: every e-book T vote is re-read
def decide(e, w, pre, post, box, line):
    if letters(e) == letters(w) and sp(e).replace(' ', '') == sp(w).replace(' ', ''):        # word division / spacing
        b = ' ' + sp(box) + ' '
        if pre and nz(box).find(pre[-4:]) < 0 and nz(post)[:4] and nz(box).find(nz(post)[:4]) < 0: return None
        te, tw = (' ' + sp(e) + ' ') in b, (' ' + sp(w) + ' ') in b
        return ('T' if te else 'W') if te != tw else None
    hay = [nz(line), nz(box)]
    for a, z in ((6, 4), (0, 4), (6, 0)):
        if (a and len(pre) < a) or (z and len(post) < z): continue
        if not (a and z) and (not nz(e) or not nz(w)): continue        # an empty reading needs context on both sides
        ce = any((pre[-a:] if a else '') + nz(e) + post[:z] in h for h in hay)
        cw = any((pre[-a:] if a else '') + nz(w) + post[:z] in h for h in hay)
        if ce != cw: return 'T' if ce else 'W'
        if ce and cw: return None
    return None
out, hand, unread = [], [], []
used = set()
for l in open(os.path.join(BOOK, '.parts', 'collate', 'checks-tvotes.tsv'), encoding='utf-8'):
    f = l.rstrip('\n').split('\t'); key = f[1]; p = int(f[4])
    if key in done: continue
    e, w = key.split('|', 1)[1].split('>', 1); w = re.sub(r'#\d+$', '', w)
    pre, post = nz(re.sub(r'\[[^\[\]]*\]$', '', f[2])), nz(f[3])
    res = {}
    for rid, rp, box, line, note in READ:
        if rp != p: continue
        if pre[-6:] not in nz(line) + nz(box) and post[:4] not in nz(line) + nz(box): continue   # not this spot
        d = decide(e, w, pre, post, box, line)
        if 'pencil' in note.lower() and d is None and not letters(e): d = 'T'
        res[rid] = (d, box, line, note)
    ds = {d for d, *_ in res.values() if d}
    flagged = any(re.search(r'doubt|misprint|PRINTED|as printed', n, re.I) for _, _, _, n in res.values())
    if len(ds) == 1 and not flagged:
        d = ds.pop(); rid = [r for r, v in res.items() if v[0] == d][0]; used.add(rid)
        out.append(f'{key}\t{d}\timage, blind read {rid}' + (f' ({res[rid][3]})' if res[rid][3] else ''))
    elif res:
        for r in res: used.add(r)
        hand.append(f'{f[0]}\t{key}\t' + ' || '.join(f'{r}: BOX[{v[1]}] LINE[{v[2]}] {v[3]}' for r, v in res.items()))
    else: unread.append(f[0])
print(f'{len(READ)} readings; {len(out)} checks decided by comparison; {len(hand)} for a decision by hand; {len(unread)} open checks not yet read; readings matched to no check: ' + ' '.join(r[0] for r in READ if r[0] not in used))
for h in hand: print('  ' + h)
if False:
    shutil.copy2(DECF, os.path.join(BOOK, '.parts', f'decisions.tsv.bak.{datetime.datetime.now():%Y%m%d-%H%M%S}'))
    with open(DECF, 'a', encoding='utf-8') as fh: fh.write(f'# reads.py {datetime.date.today()}\n' + '\n'.join(out) + '\n')
    print('appended', len(out))

print('--- decided W (the e-book vote was wrong):')
for o in out:
    if o.split('\t')[1] == 'W': print('  ' + o)
