#!/usr/bin/env python3
"""notereads.py (2026-10-14) -- compare the footnotes read whole and blind (notesheets.py -> r-n1-*.tsv, NOTE-READER-BRIEF.md)
with the footnotes of transcription.tex (after check.py --apply), page by page and note by note, word by word with
punctuation; lists every difference with the reader's words, and the <sp> (letterspaced) and *..* (italic) runs the
reader saw.  Controls (body lines whose reading is known) are scored.  Nothing is changed: fixes go into patches.POST.
    python3 ebook-method/kort-oversigt/notereads.py [--tag n1] > .parts/notereads.txt"""
import os, re, sys, glob, difflib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import pagemap as C
RD = os.path.join(C.BOOKDIR, '.parts', 'reads'); TAG = sys.argv[sys.argv.index('--tag') + 1] if '--tag' in sys.argv else 'n1'
T = open(os.path.join(C.BOOKDIR, 'transcription.tex'), encoding='utf-8').read()
def texnotes():
    out, page = {}, None
    for m in re.finditer(r'% --- p\. (\d+) ---|\\footnote\[(\d+)\]\{', T):
        if m.group(1): page = int(m.group(1)); continue
        j = m.end(); d = 1
        while d: d += {'{': 1, '}': -1}.get(T[j], 0); j += 1
        out.setdefault(page, []).append((int(m.group(2)), T[m.end():j - 1]))
    return out
TN = texnotes()
page_of, ctl = {}, {}
for l in open(os.path.join(RD, f'sheets-{TAG}.tsv'), encoding='utf-8'):
    x = l.rstrip('\n').split('\t'); page_of[x[1]] = int(x[2])
for l in open(os.path.join(RD, f'controls-{TAG}.tsv'), encoding='utf-8'):
    x = l.rstrip('\n').split('\t'); ctl[x[1]] = (int(x[2]), x[3])
R = {}
for f in sorted(glob.glob(os.path.join(RD, f'r-{TAG}-*.tsv'))):
    for l in open(f, encoding='utf-8'):
        x = l.rstrip('\n').split('\t')
        if len(x) >= 3 and x[0].strip(): R.setdefault(x[0].strip(), []).append((x[1].strip(), x[2], x[3] if len(x) > 3 else ''))
def plain_tex(s):
    s = s.replace('\\dots{}', '...').replace('---', '—').replace('\\&', '&').replace('\\%', '%')
    s = re.sub(r'\\textsuperscript\{([^{}]*)\}', r'^\1', s)
    s = re.sub(r'\\(?:textit|emph|textsc)\{([^{}]*)\}', r'\1', s)
    return re.sub(r'\s+', ' ', re.sub(r'\\[a-zA-Z]+\{?|[{}]', '', s)).strip()
def plain_rd(s): return re.sub(r'\s+', ' ', re.sub(r'</?sp>|\*', '', s).replace('...', '...')).strip()
qn = lambda w: w.replace('„', '"').replace('“', '"').replace('”', '"').replace('’', "'")
ok = bad = 0
for cid, (p, known) in sorted(ctl.items()):
    got = ' '.join(t for lab, t, r in R.get(cid, []))
    if re.sub(r'\W', '', plain_rd(got)) == re.sub(r'\W', '', known): ok += 1
    else: bad += 1; print(f'CONTROL? {cid} p. {p}: known [{known}] read [{got}]')
print(f'controls: {ok} right, {bad} not')
nd = 0
for cid in sorted(page_of, key=lambda c: (page_of[c], c)):
    p = page_of[cid]; rn = [x for x in R.get(cid, []) if x[0] != 'line']; tn = TN.get(p, [])
    if len(rn) != len(tn): print(f'\n== p. {p} {cid}: reader {len(rn)} notes, transcription {len(tn)}: ' + ' | '.join(l for l, t, r in rn))
    for k in range(max(len(rn), len(tn))):
        lab, rt, rem = rn[k] if k < len(rn) else ('?', '', '')
        tt = plain_tex(tn[k][1]) if k < len(tn) else ''
        a, b = qn(tt).split(), qn(plain_rd(rt)).split()
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        diffs = [(' '.join(a[i1:i2]), ' '.join(b[j1:j2])) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal']
        sps = re.findall(r'<sp>(.*?)</sp>', rt); its = re.findall(r'\*([^*]+)\*', re.sub(r'</?sp>', '', rt))
        if diffs or rem: nd += len(diffs); print(f'p. {p} {cid} [{lab}] ' + ' ; '.join(f'«{x}»→«{y}»' for x, y in diffs) + (f'   REMARK: {rem}' if rem else ''))
        if sps: print(f'   SP p. {p}: ' + ' | '.join(sps))
        if its: print(f'   IT p. {p}: ' + ' | '.join(its))
print(f'\n{nd} word differences')
