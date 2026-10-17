#!/usr/bin/env python3
"""rules2.py (2026-10-17) -- this book's own classes of NB fault, settled by rule after rules.py (decisions noted rule2:NAME):
  smallcaps  the witness reads the word in CAPITALS where the draft has it in mixed case: the print's small capitals
             (names) -> SC (check.py wraps the span in \\textsc); only when the letters agree
  aa         NB sets å for the print's a in aa (beståa, formåa, tåger): the witness's form is the draft's with å -> a -> W
  uml        NB adds an umlaut to u/U (übevægede, Übegribelige, übi): the witness's form is the draft's without it -> W
    python3 ebook-method/kort-oversigt/rules2.py [--write]"""
import os, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
B = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt'); DECF = os.path.join(HERE, 'decisions.tsv')
dec = {l.split('\t')[0] for l in open(DECF, encoding='utf-8') if '\t' in l}
out = []; n = {}
lets = lambda s: re.sub(r'[^A-Za-zÀ-ÿ]', '', s)
for l in open(os.path.join(B, '.parts', 'collate', 'checks.tsv'), encoding='utf-8'):
    f = l.rstrip('\n').split('\t'); key = f[1]
    if key in dec: continue
    e, w = key.split('|', 1)[1].split('>', 1); w = re.sub(r'#\d+$', '', w)
    r = None
    if len(lets(e)) >= 4 and re.fullmatch(r"[A-Za-zÀ-ÿ' .,-]+", e) and lets(w) and lets(w).isupper() and lets(e) and not lets(e).isupper() and lets(e).upper() == lets(w).upper().replace('0', 'O') and e.replace(' ', '') .upper() == w.replace(' ', '').upper():
        r = ('smallcaps', 'SC')
    elif 'å' in e and e.replace('å', 'a') == w: r = ('aa', 'W')
    elif re.search('[üÜ]', e) and e.replace('ü', 'u').replace('Ü', 'U') == w: r = ('uml', 'W')
    if r: out.append(f'{key}\t{r[1]}\trule2:{r[0]}'); n[r[0]] = n.get(r[0], 0) + 1
print(n)
for o in out[:12]: print(' ', o)
if '--write' in sys.argv:
    open(DECF, 'a', encoding='utf-8').write('# rules2.py 2026-10-17\n' + '\n'.join(out) + '\n'); print('appended')
