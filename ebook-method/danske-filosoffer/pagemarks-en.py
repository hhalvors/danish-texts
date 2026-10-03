#!/usr/bin/env python3
"""pagemarks-en.py -- put the 1909 page numbers into translation.tex at the word where each printed
page begins (exact placement, for citation).  Self-contained; rerunnable.

  python3 .parts/pagemarks-en.py --turns   writes .parts/turns-en.md: for every page turn, the Danish
        words around it (‖N‖ marks the turn, from transcription.tex) and a window of the English
        found by paragraph alignment (chapter, paragraph, fraction of the paragraph; notes: footnote)
  (an agent or a person then writes .parts/anchors-en.txt: lines "N|first 4-8 English words of page N",
   verbatim from the window, so that \\opage{N} goes before the word that renders the page's first word)
  python3 .parts/pagemarks-en.py --apply   inserts \\opage{N} before each anchor; checks order and uniqueness
"""
import re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'texts', 'hoeffding', os.path.basename(HERE))
DA = open(os.path.join(BOOK, 'transcription.tex'), encoding='utf-8').read()
EN_PATH = os.environ.get('TRANSLATION') or os.path.join(BOOK, 'translation.tex'); EN = open(EN_PATH, encoding='utf-8').read()

def strip_cmds(s):
    s = re.sub(r'(?m)^%.*\n?', '', s); s = re.sub(r'(?<!\\)%[^\n]*', '', s)
    s = re.sub(r'\\textsuperscript\{[^}]*\}\)?', '', s)
    s = re.sub(r'\\setcounter\{[^}]*\}\{[^}]*\}', '', s)
    s = re.sub(r'\\(textit|textsc|textbf|emph|textsubscript)\{', '', s); s = re.sub(r'\\[A-Za-z]+\*?(\[[^]]*\])?', ' ', s)
    s = s.replace('{', '').replace('}', '').replace('~', ' ')
    return re.sub(r'\s+', ' ', s).strip()

# ---- Danish: chapters -> paragraphs, with the page turns inside them
def cut_braced(s, cmd):
    out = []; i = 0
    while True:
        j = s.find(cmd, i)
        if j < 0: out.append(s[i:]); break
        out.append(s[i:j]); k = s.index('{', j) + 1; depth = 1
        while depth:
            depth += {'{': 1, '}': -1}.get(s[k], 0); k += 1
        i = k
    return ''.join(out)
body = cut_braced(DA[DA.index('% ===== INDLEDNING'): DA.index('\\end{document}')], '\\footnote[')
notes = ''
def da_units(txt, split_heads):
    units = []; ch = 0 if split_heads else -1; pend = []
    for blk in re.split(r'\n\s*\n', txt):
        if split_heads and re.search(r'\\begin\{center\}\\large \d+\. ', blk): ch += 1
        b = re.sub(r'\\opage\{(\d+)\}', lambda m: f' ‖{m.group(1)}‖ ', blk)
        if '\\begin{center}' in b or not strip_cmds(re.sub(r'‖\d+‖', '', b)):
            pend.extend(re.findall(r'‖\d+‖', b)); continue       # a turn before a heading: give it to the next paragraph
        t = strip_cmds(b)
        if pend: t = ' '.join(pend) + ' ' + t; pend.clear()
        if re.sub(r'‖\d+‖', '', t).strip(): units.append((ch, t))
        elif re.search(r'‖\d+‖', t) and units: units[-1] = (units[-1][0], units[-1][1] + ' ' + t)
    return units
DU = da_units(body, True)
DN = []
# ---- English: chapters -> paragraphs (footnotes cut out and kept in order)
start = EN.index('\\dfchapter{Introduction}'); end = EN.index('\\end{document}')
ENB = EN[start:end]
FOOT = []
def cut_foot(s):
    out = []; i = 0
    while True:
        j = s.find('\\footnote{', i)
        if j < 0: out.append(s[i:]); break
        out.append(s[i:j]); k = j + 10; depth = 1
        while depth:
            depth += {'{': 1, '}': -1}.get(s[k], 0); k += 1
        FOOT.append(s[j + 10:k - 1]); i = k
    return ''.join(out)
EU = []; ch = -1
for blk in re.split(r'\n\s*\n', ENB):
    if '\\dfchapter{' in blk: ch += 1
    t = strip_cmds(cut_foot(blk))
    hd = re.sub(r'(?m)^%.*\n?', '', blk).lstrip()
    if len(t) > 40 and '\\dfchapter' not in blk and not hd.startswith(('\\section', '\\subsection', '\\begin{center}')):
        EU.append((ch, t))
def by_ch(U):
    d = {}
    for c, t in U: d.setdefault(c, []).append(t)
    return d
dc, ec = by_ch(DU), by_ch(EU)
print('paragraphs per chapter  Danish:', {k: len(v) for k, v in dc.items()}, ' English:', {k: len(v) for k, v in ec.items()})
print('notes: Danish', len([u for u in DN if not u[1].startswith('‖')]), '| English footnotes', len(FOOT))

def turns():
    out = []
    for c, paras in dc.items():
        ep = ec.get(c, [])
        for i, t in enumerate(paras):
            for m in re.finditer(r'‖(\d+)‖', t):
                n = int(m.group(1)); plain = re.sub(r'‖\d+‖', '', t[:m.start()])
                frac = len(plain) / max(1, len(re.sub(r'‖\d+‖', '', t)))
                if len(ep) == len(paras):
                    e = ep[i]; pos = int(frac * len(e)); w = e[max(0, pos - 500): pos + 500]
                    if frac < 0.08 and i > 0: w = ep[i - 1][-300:] + ' ¶ ' + w
                else:      # paragraphing differs (verse, quotations): place by the share of the chapter's text
                    dl = [len(re.sub(r'‖\d+‖', '', x)) for x in paras]; done = sum(dl[:i]) + frac * dl[i]
                    E = ' ¶ '.join(ep); pos = int(done / max(1, sum(dl)) * len(E)); w = E[max(0, pos - 1100): pos + 1100]
                words = t.split(); k = len(re.sub(r'‖\d+‖', '', t[:m.start()]).split())
                da = ' '.join(words[max(0, k - 28): k + 30])
                out.append((n, da, w))
    # notes: the e-book order of the notes = the footnote order of the translation
    notes_da = [t for c, t in DN]
    for i, t in enumerate(notes_da):
        for m in re.finditer(r'‖(\d+)‖', t):
            n = int(m.group(1)); k = len(t[:m.start()].split()); words = t.split()
            frac = len(t[:m.start()]) / max(1, len(t)); fi = i
            f = strip_cmds(FOOT[min(fi, len(FOOT) - 1)]) if FOOT else ''
            pos = int(frac * len(f)); w = f[max(0, pos - 500): pos + 500]
            if frac < 0.08 and fi > 0: w = strip_cmds(FOOT[fi - 1])[-300:] + ' ¶(next footnote) ' + w
            out.append((n, ' '.join(words[max(0, k - 28): k + 30]), '[FOOTNOTE] ' + w))
    out.sort()
    with open(os.path.join(BOOK, '.parts', 'turns-en.md'), 'w', encoding='utf-8') as f:
        for n, da, w in out: f.write(f'### p. {n}\nDA: {da}\nEN: {w}\n\n')
    print('turns written:', len(out), 'pages', out[0][0], '-', out[-1][0])

def norm(s): return re.sub(r'\s+', ' ', s).strip()
def apply():
    A = [l.rstrip('\n').split('|', 1) for l in open(os.path.join(HERE, 'anchors-en.txt'), encoding='utf-8') if '|' in l]
    src = EN
    # cleaned view of the source with a map back to offsets (commands and comments dropped, whitespace collapsed)
    keep = []; i = 0
    while i < len(src):
        c = src[i]
        if c == '%' and (i == 0 or src[i - 1] != '\\'):
            while i < len(src) and src[i] != '\n': i += 1
            continue
        if c == '\\':
            m = re.match(r'\\[A-Za-z]+\*?|\\.', src[i:i+40], re.S); s = m.group(0)
            if s in ('\\textit', '\\emph', '\\textsc', '\\footnote', '\\textbf'): i += len(s); continue
            if s in ('\\,', '\\ ', '\\quad'): keep.append((' ', i)); i += len(s); continue
            if s.startswith('\\') and len(s) == 2 and not s[1].isalpha(): keep.append((s[1], i)); i += 2; continue
            i += len(s); continue
        if c in '{}': i += 1; continue
        if c in ' \n\t~':
            if keep and keep[-1][0] != ' ': keep.append((' ', i))
            i += 1; continue
        keep.append((c, i)); i += 1
    clean = ''.join(k[0] for k in keep); offs = [k[1] for k in keep]
    clean = clean.replace('---', '—').replace('--', '–') if False else clean
    ins = []; last = {True: -1, False: -1}; bad = []   # text pages and Noter pages (footnotes) are ordered separately
    body0 = src.index('\\dfchapter{Introduction}')
    for n, a in A:
        a = norm(a); hits = [m.start() for m in re.finditer(re.escape(a), clean)]
        hits = [h for h in hits if offs[h] > body0]
        if len(hits) != 1: bad.append((n, a, len(hits))); continue
        o = offs[hits[0]]
        g = False
        if o < last[g]: bad.append((n, a, 'out of order'))
        last[g] = o; ins.append((o, int(n)))
    if bad:
        for b in bad: print('ANCHOR PROBLEM', b)
        sys.exit(1)
    for o, n in sorted(ins, reverse=True): src = src[:o] + f'\\opage{{{n}}}' + src[o:]
    if '\\newcommand{\\opage}' not in src:
        src = src.replace('\\begin{document}', '\\usepackage{marginnote}\n\\newcommand{\\opage}[1]{\\marginnote{\\footnotesize\\textit{[#1]}}}\n\\begin{document}', 1)
    open(EN_PATH, 'w', encoding='utf-8').write(src); print('inserted', len(ins), 'page markers')
if '--turns' in sys.argv: turns()
if '--apply' in sys.argv: apply()
