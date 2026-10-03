#!/usr/bin/env python3
"""ebook-method/collate/pagemarks.py -- put the printed page numbers into a translation, at the word
where each printed page begins, from the exact \\opage markers of the transcription.  Self-contained.

    python3 ebook-method/collate/pagemarks.py BOOK --turns    write ebook-method/BOOK/turns-en.txt: for each
            page turn the Danish words around it (‖N‖) and the English passage it falls in, found by
            aligning the paragraphs of both texts (Gale-Church, by length); turns at the head of a
            paragraph that aligns one-to-one are answered automatically
    (then complete ebook-method/BOOK/anchors-en.txt: lines "N|4-8 English words, verbatim[@k]", the words
     that begin the rendering of page N's first Danish words; \\opage{N} goes before them)
    python3 ebook-method/collate/pagemarks.py BOOK --apply    insert \\opage{N} into translation.tex (backup first),
            checking that every anchor occurs exactly once and that the pages come in order
    TRANSLATION=path  to try --apply on a copy

Footnotes are cut out of both texts before aligning; a page turn inside a footnote is listed for hand
placement.  The Danish page markers must be exact first (ebook-method/collate/check.py BOOK --pages).
"""
import re, os, sys, shutil, datetime, math
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
if len(sys.argv) < 3: sys.exit(__doc__)
NAME = sys.argv[1]; BOOK = os.path.join(ROOT, 'texts', 'hoeffding', NAME); CONF = os.path.join(ROOT, 'ebook-method', NAME)
DA = open(os.path.join(BOOK, 'transcription.tex'), encoding='utf-8').read()
EN_PATH = os.environ.get('TRANSLATION') or os.path.join(BOOK, 'translation.tex'); EN = open(EN_PATH, encoding='utf-8').read()

def cut_notes(s, keep):
    """remove \\footnote{...} groups; keep collects their contents"""
    out = []; i = 0
    while True:
        m = re.compile(r'\\footnote(?![A-Za-z])').search(s, i); j = m.start() if m else -1
        if j < 0: out.append(s[i:]); return ''.join(out)
        out.append(s[i:j]); k = j + 9
        if s[k:k + 1] == '[': k = s.index(']', k) + 1
        while s[k] in ' \n': k += 1
        if s[k] != '{': out.append('\\footnote'); i = j + 9; continue
        d = 0; a = k
        while True:
            c = s[k]
            if c == '\\': k += 2; continue
            if c == '%':                                  # a comment inside the note: its braces do not count
                k = s.index('\n', k); continue
            d += {'{': 1, '}': -1}.get(c, 0); k += 1
            if d == 0: break
        keep.append(s[a + 1:k - 1]); i = k
def plain(s):
    s = re.sub(r'(?<!\\)%[^\n]*', '', s)
    s = re.sub(r'\\(begin|end)\{[^}]*\}|\\\\(\[[^]]*\])?', ' ', s)
    s = re.sub(r'\\(label|addcontentsline|thispagestyle|vspace|hspace|rule|setcounter|marginnote)\*?(\[[^]]*\])?(\{[^}]*\})*', ' ', s)
    s = re.sub(r'\\(textit|textsc|textbf|emph|textsl|dk|spaced|so)\{', '', s)
    s = re.sub(r'\\[A-Za-z]+\*?(\[[^]]*\])?', ' ', s)
    s = s.replace('\\-', '').replace('{', '').replace('}', '').replace('~', ' ').replace('\\', ' ').replace('---', '—').replace('--', '–')
    return re.sub(r'\s+', ' ', s).strip()
def paragraphs(src, marks):
    body = src[src.index('\\begin{document}'): src.index('\\end{document}')]
    body = re.sub(r'(?<!\\)%[^\n]*\n[ \t]*', '', body)     # comments go, with their line end, as in TeX
    notes = []; body = cut_notes(body, notes)
    if marks: body = re.sub(r'\\[oa]page\{(\d+)\}', lambda m: f' ‖{m.group(1)}‖ ', body)
    out = []; carry = ''
    HEAD = re.compile(r'\s*(‖\d+‖\s*)*(\\noindent\s*)?(\\(part|chapter|(sub)*section|paragraph)\*?\{|\\begin\{center\}|\{\\(large|Large|LARGE|bfseries|scshape)\b)')
    for blk in re.split(r'\n\s*\n', body):
        t = plain(blk)
        if len(re.sub(r'‖\d+‖', '', t)) < 3 or HEAD.match(blk):    # empty, or a heading: its page turn goes to
            carry += ' ' + ' '.join(re.findall(r'‖\d+‖', t)); continue    # the first text under it (house convention)
        if carry.strip(): t = carry.strip() + ' ' + t; carry = ''
        out.append(t)
    return out, notes

DP, DN = paragraphs(DA, True); EP, EN_NOTES = paragraphs(EN, False)
NOTE_TURNS = sorted({int(n) for x in DN for n in re.findall(r'\\opage\{(\d+)\}', x)})

def gale_church(a, b):
    """align two lists of paragraph lengths; returns [(i0,i1,j0,j1)] blocks (1-1, 1-2, 2-1, 1-0, 0-1, 2-2)"""
    ra = sum(b) / max(1, sum(a)); n, m = len(a), len(b)
    def cost(la, lb):
        if la == 0 or lb == 0: return 12.0
        x = la * ra; d = (lb - x) / math.sqrt(max(x, 1) * 6.8)
        return d * d / 2
    INF = float('inf'); D = [[INF] * (m + 1) for _ in range(n + 1)]; P = [[None] * (m + 1) for _ in range(n + 1)]; D[0][0] = 0
    moves = [(1, 1, 0), (1, 0, 6), (0, 1, 6), (2, 1, 2.3), (1, 2, 2.3), (2, 2, 4.6)]
    for i in range(n + 1):
        for j in range(m + 1):
            if D[i][j] == INF: continue
            for di, dj, pen in moves:
                if i + di <= n and j + dj <= m:
                    c = D[i][j] + pen + cost(sum(a[i:i + di]), sum(b[j:j + dj]))
                    if c < D[i + di][j + dj]: D[i + di][j + dj] = c; P[i + di][j + dj] = (di, dj)
    out = []; i, j = n, m
    while i or j:
        di, dj = P[i][j]; out.append((i - di, i, j - dj, j)); i -= di; j -= dj
    return out[::-1]

def turns():
    la = [len(re.sub(r'‖\d+‖', '', p)) for p in DP]; lb = [len(p) for p in EP]
    blocks = gale_church(la, lb); ones = sum(1 for b in blocks if b[1] - b[0] == 1 and b[3] - b[2] == 1)
    lines = [f'# {NAME}: {len(DP)} Danish / {len(EP)} English paragraphs; {ones} of {len(blocks)} aligned one-to-one',
             '# For each turn write a line in anchors-en.txt:  N|English words that begin page N (verbatim, 4-8 words)']
    auto = []; todo = 0
    for i0, i1, j0, j1 in blocks:
        dtext = ' '.join(DP[i0:i1]); etext = ' '.join(EP[j0:j1])
        clean = re.sub(r' ?‖\d+‖ ?', ' ', dtext)
        for m in re.finditer(r'‖(\d+)‖', dtext):
            n = int(m.group(1)); before = re.sub(r' ?‖\d+‖ ?', ' ', dtext[:m.start()]).strip()
            frac = len(before) / max(1, len(clean))
            if not before and i1 - i0 == 1 and j1 - j0 == 1 and etext:      # page begins with the paragraph
                auto.append(f"{n}|{' '.join(etext.split()[:6])}"); continue
            if i1 == i0 or not etext: lines.append(f'\n=== p.{n}: no English counterpart found (place by hand)'); todo += 1; continue
            c = int(frac * len(etext)); w = 260 if (i1 - i0, j1 - j0) == (1, 1) else 450
            da = (before[-110:] + ' ‖' + str(n) + '‖ ' + re.sub(r'‖\d+‖ ?', '', dtext[m.end():]).strip()[:90])
            lines.append(f'\n=== p.{n}\nDA: …{da.strip()}…\nEN: …{etext[max(0, c - w): c + w]}…'); todo += 1
    for n in NOTE_TURNS: lines.append(f'\n=== p.{n}: the turn falls inside a footnote (place by hand)'); todo += 1
    f = os.path.join(CONF, 'turns-en.txt'); open(f, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    af = os.path.join(CONF, 'anchors-en.txt')
    have = open(af, encoding='utf-8').read() if os.path.exists(af) else ''
    known = {l.split('|')[0] for l in have.splitlines() if '|' in l and not l.startswith('#')}
    new = [a for a in auto if a.split('|')[0] not in known]
    if new: open(af, 'a', encoding='utf-8').write(('' if have else f'# {NAME}: N|English words where page N begins (verbatim)\n') + '\n'.join(new) + '\n')
    print(f'{len(blocks)} paragraph blocks ({ones} one-to-one); {len(auto)} turns at a paragraph head answered '
          f'automatically into anchors-en.txt; {todo} to place: {os.path.relpath(f, ROOT)}')

def norm(a): return re.sub(r'\s+', ' ', a.strip())
def apply():
    A = [l.split('|', 1) for l in open(os.path.join(CONF, 'anchors-en.txt'), encoding='utf-8').read().splitlines() if '|' in l and not l.startswith('#')]
    A.sort(key=lambda x: int(x[0]))
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
    body0 = src.index('\\begin{document}'); ins = []; last = -1; bad = []
    for n, a in A:
        a = norm(a); k = None
        mk = re.search(r'@(\d+)$', a)              # "text@2": the 2nd occurrence (when the words recur)
        if mk: k = int(mk.group(1)); a = a[:mk.start()].rstrip()
        hits = [h for h in (m.start() for m in re.finditer(re.escape(a), clean)) if offs[h] > body0]
        if k is not None: hits = hits[k - 1:k]
        if len(hits) != 1: bad.append((n, a, f'{len(hits)} hits')); continue
        o = offs[hits[0]]
        if o < last: bad.append((n, a, 'out of order'))
        last = max(last, o); ins.append((o, int(n)))
    if bad:
        for b in bad: print('ANCHOR PROBLEM', b)
        sys.exit(1)
    for o, n in sorted(ins, reverse=True): src = src[:o] + f'\\opage{{{n}}}' + src[o:]
    if '\\newcommand{\\opage}' not in src:
        if '{marginnote}' not in src: src = src.replace('\\begin{document}', '\\usepackage{marginnote}\n\\begin{document}', 1)
        src = src.replace('\\begin{document}', '\\newcommand{\\opage}[1]{\\marginnote{\\footnotesize\\textit{[#1]}}}\n\\begin{document}', 1)
    if not os.environ.get('TRANSLATION'):
        b = EN_PATH + f'.bak.{datetime.date.today():%Y%m%d}-prepages'
        if not os.path.exists(b): shutil.copy2(EN_PATH, b)
    open(EN_PATH, 'w', encoding='utf-8').write(src); print('inserted', len(ins), 'page markers')
if '--turns' in sys.argv: turns()
if '--apply' in sys.argv: apply()
