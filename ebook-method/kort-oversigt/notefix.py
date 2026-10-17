#!/usr/bin/env python3
"""notefix.py (2026-10-14) -- turn the footnotes read whole and blind (r-n1-*.tsv; notereads.py lists them) into
postfix.tsv, the page-scoped literal corrections draft.py --post applies: (1) word corrections the readers saw that both
OCRs (and so the collation) missed -- chiefly accents in the French titles -- listed in WORDS below after review;
(2) every letterspaced run (<sp>) as \\emph{}, (3) every italic run (*..*) as \\textit{}, each only where its words occur
exactly once in that page's notes.  Run against the collated text (draft.py --emit --force; check.py --apply), BEFORE
draft.py --post.     python3 ebook-method/kort-oversigt/notefix.py [--write]"""
import os, re, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import pagemap as C
RD = os.path.join(C.BOOKDIR, '.parts', 'reads')
T = open(os.path.join(C.BOOKDIR, 'transcription.tex'), encoding='utf-8').read()
# (page, find, replace, why): reviewed by the main session from notereads.py (2026-10-14); 'n1' = the note readers
WORDS = [(12, 'reve', 'rêve'), (13, 'elle-méme.', 'elle-même.'), (15, 'Genéve', 'Genève'), (17, 'systéme', 'système'),
    (17, '141--- 199;', '141---199;'), (18, 'Hemmelige“.', 'Hemmelige«.'), (28, '11,', 'II,'), (32, 'Geneve', 'Genève'),
    (34, 'Israéls.', 'Israëls.'), (35, 'Israéls', 'Israëls'), (49, 'Engel hardt', 'Engelhardt'), (59, '25 —38).', '25---38).'),
    (60, 'Térese', 'Térèse'), (65, 'Tércse\\textsuperscript{2}.', 'Térèse\\textsuperscript{2}.'), (71, 'Térese.', 'Térèse.'),
    (74, 'Térése.', 'Térèse.'), (75, 'Francaise', 'Française'), (76, 'Aprés étre', 'Après être'), (76, 'å', 'à'),
    (78, 'Sainte-Térése.', 'Sainte-Térèse.'), (80, 'Claparéde.', 'Claparède.'), (80, 'Céciles', "Cécile's"), (86, "Joél's", "Joël's"),
    (130, 'Francaise', 'Française'), (130, '353 —357.', '353---357.'), (136, 'å', 'à'), (138, 'Francaise', 'Française'),
    (150, "Spinoza'*", "Spinoza's"), (152, 'Hele Kapitlet om philosophiea«', 'Hele Kapitlet om »Consolatio philosophiea«'),
    (157, '1,8.', 'I,8.'), (158, '1,8.', 'I,8.'), (158, 'Boéthii:', 'Boëthii:'), (159, "E u r i p i d e s'", "Euripides'"),
    (159, 'V. 1391', 'v. 1391'), (159, 'Samménligning', 'Sammenligning'), (161, 'VIII, p. 209', 'VIII,1. p. 209'),
    (164, '653 —659.', '653---659.'), (168, 'Durkh e i m:', 'Durkheim:'), (169, 'Thougth', 'Thought'), (170, '11,3.', 'II,3.'),
    (172, 'Harl e s s:', 'Harless:'), (173, 'MesterEckehart:', 'Mester Eckehart:'), (178, 'W arr en:', 'Warren:'),
    (181, 'Naade.*', 'Naade.«'), (185, 'journaliére', 'journalière'), (185, 'å', 'à'), (207, 'temps-lå! Pensées.', 'temps-là! Pensées,'),
    (193, 'i min Religionsfilosofi}. Otto', 'i min Religionsfilosofi § 96.}. Otto'),
    (53, '(Mester Eckehart; Prædikener og Traktater', '(\\textit{Mester Eckehart; Prædikener og Traktater}'),
    (138, 'Die Arunda und Loritja-Stämme in Zentral-Austrálien', '\\textit{Die Arunda und Loritja-Stämme in Zentral-Austrálien}')]
def seg(t, p):
    a = t.index(f'% --- p. {p} ---'); b = t.find('% --- p. ', a + 10); return a, (len(t) if b < 0 else b)
def notespans(s):
    out = []
    for m in re.finditer(r'\\footnote\[\d+\]\{', s):
        j = m.end(); d = 1
        while d: d += {'{': 1, '}': -1}.get(s[j], 0); j += 1
        out.append((m.end(), j - 1))
    return out
rows, miss = [], []
def apply(p, find, repl, why):
    global T
    a, b = seg(T, p); s = T[a:b]
    if s.count(find) != 1: miss.append((p, find, s.count(find), why)); return
    T = T[:a] + s.replace(find, repl) + T[b:]; rows.append((p, find, repl, why))
for p, f, r in WORDS: apply(p, f, r, 'n1: the footnotes read whole at the image')
page_of = {}
for l in open(os.path.join(RD, 'sheets-n1.tsv'), encoding='utf-8'):
    x = l.rstrip('\n').split('\t'); page_of[x[1]] = int(x[2])
for f in sorted(glob.glob(os.path.join(RD, 'r-n1-*.tsv'))):
    for l in open(f, encoding='utf-8'):
        x = l.rstrip('\n').split('\t')
        if len(x) < 3 or x[0] not in page_of or x[1] == 'line': continue
        p = page_of[x[0]]
        for kind, rx, cmd in (('sp', r'<sp>(.*?)</sp>', 'emph'), ('it', r'\*([^*]+)\*', 'textit')):
            src = x[2] if kind == 'sp' else re.sub(r'</?sp>', '', x[2])
            for run in re.findall(rx, src):
                run = run.strip().rstrip(',;:').strip().replace('’', "'")
                if kind == 'it': run = re.sub(r'[.,;:]$', '', run).strip()   # a stop after the run stays roman (readers unsure)
                if len(re.sub(r'\W', '', run)) < 3: continue
                a, b = seg(T, p); s = T[a:b]; spans = notespans(s)
                hits = [m.start() for m in re.finditer(re.escape(run), s) if any(x0 <= m.start() < x1 for x0, x1 in spans)]
                if not hits: miss.append((p, run, 0, kind)); continue
                # the same run in two notes of one page (Seneca, Confessiones): the readers marked it in each -- wrap every one
                for k in sorted(hits, reverse=True):
                    a, b = seg(T, p); s = T[a:b]
                    if s[max(0, k - 9):k].endswith(('\\emph{', 'textit{')): continue
                    ctx = s[max(0, k - 12):k]; find = ctx + run
                    if s.count(find) != 1: miss.append((p, run, -1, kind)); continue
                    apply(p, find, ctx + '\\' + cmd + '{' + run + '}', f'n1: {"letterspaced" if kind == "sp" else "italic"} (read whole)')
                break_ = None
print(f'{len(rows)} corrections; {len(miss)} not placed')
for m in miss: print('  NOT PLACED', m)
if '--write' in sys.argv:
    with open(os.path.join(HERE, 'postfix.tsv'), 'w', encoding='utf-8') as fh:
        fh.write('# postfix.tsv (notefix.py, 2026-10-14): page <TAB> find <TAB> replace <TAB> why -- applied by draft.py --post\n')
        for p, f, r, w in rows: fh.write(f'{p}\t{f}\t{r}\t{w}\n'.replace('\n\t', '\t'))
    print('wrote postfix.tsv')
