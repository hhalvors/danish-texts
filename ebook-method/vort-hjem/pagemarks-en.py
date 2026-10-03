#!/usr/bin/env python3
"""pagemarks-en.py -- put the 1903 page numbers into translation.tex at the word where each printed
page begins (exact placement, for citation).  Self-contained; rerunnable.

  python3 ebook-method/vort-hjem/pagemarks-en.py --turns   for every page turn: the Danish words
        around it (‖N‖ marks the turn, from the \\opage markers of transcription.tex) and the English
        paragraph with the same number in the same section (sections I.-IV.)
  (then write anchors-en.txt here: lines "N|first 4-8 English words of page N", verbatim, so that
   \\opage{N} goes before the word that renders the page's first word)
  python3 ebook-method/vort-hjem/pagemarks-en.py --apply   inserts \\opage{N}; checks order and uniqueness
"""
import re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'texts', 'hoeffding', os.path.basename(HERE))
DA = open(os.path.join(BOOK, 'transcription.tex'), encoding='utf-8').read()
EN_PATH = os.environ.get('TRANSLATION') or os.path.join(BOOK, 'translation.tex'); EN = open(EN_PATH, encoding='utf-8').read()

def strip_cmds(s):
    s = re.sub(r'(?m)^%.*\n?', '', s); s = re.sub(r'(?<!\\)%[^\n]*\n?', '', s)
    s = re.sub(r'\\(textit|textsc|textbf|emph)\{', '', s); s = re.sub(r'\\[A-Za-z]+\*?', ' ', s)
    s = s.replace('{', '').replace('}', '').replace('~', ' ').replace('\\-', '')
    return re.sub(r'\s+', ' ', s).strip()
def units(src, marks):
    """section number -> list of paragraphs (the \\opage markers shown as ‖N‖ when marks)"""
    body = src[src.index('\\section*{I.}'): src.index('\\end{document}')]
    if marks: body = re.sub(r'\\opage\{(\d+)\}', lambda m: f'‖{m.group(1)}‖', body)
    out = {}; sec = 0
    for blk in re.split(r'\n\s*\n', body):
        if '\\section*{' in blk: sec += 1; continue
        t = strip_cmds(blk)
        if t: out.setdefault(sec, []).append(t)
    return out

def turns():
    D, E = units(DA, True), units(EN, False)
    print('paragraphs per section  Danish:', {k: len(v) for k, v in D.items()}, ' English:', {k: len(v) for k, v in E.items()})
    for s in D:
        for i, p in enumerate(D[s]):
            for m in re.finditer(r'‖(\d+)‖', p):
                if m.group(1) == '3': continue
                frac = m.start() / len(p)
                print(f"\n=== p.{m.group(1)}  section {s}, paragraph {i + 1}, at {frac:.0%}")
                print('DA:', p[max(0, m.start() - 160): m.start() + 120])
                if i < len(E.get(s, [])):
                    e = E[s][i]; c = int(frac * len(e)); print('EN:', e[max(0, c - 700): c + 700])

def norm(a): return re.sub(r'\s+', ' ', a.strip())
def apply():
    A = [l.split('|', 1) for l in open(os.path.join(HERE, 'anchors-en.txt'), encoding='utf-8').read().splitlines() if '|' in l and not l.startswith('#')]
    src = re.sub(r'\\opage\{\d+\}', '', EN)
    keep = []; i = 0
    while i < len(src):                     # a plain-text view of the source, each character mapped to its offset
        c = src[i]
        if c == '%' and (i == 0 or src[i - 1] != '\\'):
            while i < len(src) and src[i] != '\n': i += 1
            continue
        if c == '\\':
            m = re.match(r'\\[A-Za-z]+\*?|\\.', src[i:i + 40], re.S); s = m.group(0)
            if s in ('\\,', '\\ '): keep.append((' ', i))
            elif len(s) == 2 and not s[1].isalpha() and s != '\\-': keep.append((s[1], i))
            i += len(s); continue
        if c in '{}': i += 1; continue
        if c in ' \n\t~':
            if keep and keep[-1][0] != ' ': keep.append((' ', i))
            i += 1; continue
        keep.append((c, i)); i += 1
    clean = ''.join(k[0] for k in keep); offs = [k[1] for k in keep]
    body0 = src.index('\\section*{I.}'); ins = []; last = -1; bad = []
    for n, a in A:
        a = norm(a); hits = [h for h in (m.start() for m in re.finditer(re.escape(a), clean)) if offs[h] > body0]
        if len(hits) != 1: bad.append((n, a, len(hits))); continue
        o = offs[hits[0]]
        if o < last: bad.append((n, a, 'out of order'))
        last = o; ins.append((o, int(n)))
    if bad:
        for b in bad: print('ANCHOR PROBLEM', b)
        sys.exit(1)
    for o, n in sorted(ins, reverse=True): src = src[:o] + f'\\opage{{{n}}}' + src[o:]
    if '\\newcommand{\\opage}' not in src:
        src = src.replace('\\begin{document}', '\\usepackage{marginnote}\n\\newcommand{\\opage}[1]{\\marginnote{\\footnotesize\\textit{[#1]}}}\n\\begin{document}', 1)
    open(EN_PATH, 'w', encoding='utf-8').write(src); print('inserted', len(ins), 'page markers')
if '--turns' in sys.argv: turns()
if '--apply' in sys.argv: apply()
