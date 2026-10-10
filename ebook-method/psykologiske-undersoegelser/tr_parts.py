#!/usr/bin/env python3
"""tr_parts.py -- English translation of Høffding, Psykologiske Undersøgelser (1889).
Copied 2026-10-09 from ebook-method/psykologiske-undersoegelser/tr_parts.py; changed: PARTS, the book folder, and the
Danish opening quotation mark « (this print's; » closes) counted with „.

The Danish (texts/hoeffding/psykologiske-undersoegelser/transcription.tex, the text of record) is cut into parts by
ANCHOR (a line that begins a chapter, a section or a printed page), so no sentence is shared by two translators.
Each part is translated into BOOK/.parts/tr/<PART>.texfrag (TRANSLATOR-BRIEF.md, GLOSSARY.md), and `build`
checks the parts against the Danish and splices them into translation.tex from tr_template.tex.

    python3 ebook-method/psykologiske-undersoegelser/tr_parts.py list              # parts, pages, words, notes
    python3 ebook-method/psykologiske-undersoegelser/tr_parts.py extract PART      # print that part's Danish
    python3 ebook-method/psykologiske-undersoegelser/tr_parts.py build [--write]   # check the parts present;
                                                                             # --write writes translation.tex
    options: --book DIR, --parts DIR, --template FILE

Checks made by build, per part and per printed page (text between two \\opage markers; comments removed):
every \\opage of the Danish once and in order (also inside run-over notes); the "% --- p. N ---" comment lines;
\\footnote and \\setcounter{footnote}{0}; paragraph breaks; opening quotation marks („ » against ``);
\\emph and \\textit per part; the Greek identical, character for character, in order; lines ending in a bare %
that are not comment lines (the glued-word trap, TRANSLATION-PLAYBOOK §6d)."""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
def opt(name, default):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default
BOOK = opt('--book', os.path.join(ROOT, 'texts', 'hoeffding', 'psykologiske-undersoegelser'))
TR = opt('--parts', os.path.join(BOOK, '.parts', 'tr'))
TEMPLATE = opt('--template', os.path.join(HERE, 'tr_template.tex'))

# (name, chapter, anchor: the start of the line that begins the part).  The part runs to the next anchor;
# the last to \end{document}.  Text before a part's first page marker belongs to the page it starts on.
PARTS = [
    ('A-front-ch1a', 'front, Introduction, I §§3-10', '% --- p. 1 --- (title)'),
    ('B-ch1b-ch2',   'I §§11-14, II',                  '11. Vi kunne ikke undvære'),
    ('C-ch3',        'III',                            '\\begin{center}\\large III. Den frie Lighedsassociation.\\end{center}'),
    ('D-ch4-ch5',    'IV, V',                          '\\begin{center}\\large IV. Forestillingsassociation og Sammenligning.\\end{center}'),
    ('E-ch6-ch7',    'VI, VII',                        '\\begin{center}\\large VI. Sjælelig og fysisk Aktivitet.\\end{center}'),
]
GREEK = re.compile(r'[\u0370-\u03ff\u1f00-\u1fff][\u0370-\u03ff\u1f00-\u1fff\u0300-\u036f’\' .,;:]*[\u0370-\u03ff\u1f00-\u1fff]|[\u0370-\u03ff\u1f00-\u1fff]')
FN = '\\footnote['

def danish():
    return open(os.path.join(BOOK, 'transcription.tex'), encoding='utf-8').read()

def split_parts(text):
    starts = []
    for name, _, a in PARTS:
        hits = [m.start() + 1 for m in re.finditer(re.escape('\n' + a), text)]
        if len(hits) != 1: sys.exit(f'{name}: anchor {a!r} matches {len(hits)} times')
        starts.append(hits[0])
    if starts != sorted(starts): sys.exit('anchors out of order')
    end = text.index('\n\\end{document}') + 1
    bounds = starts + [end]
    out = {}
    for k, (name, _, _) in enumerate(PARTS):
        before = re.findall(r'^% --- p\. (\d+) ---$', text[:bounds[k]], re.M)
        raw = text[bounds[k]:bounds[k + 1]]
        # seam: does a blank line (a paragraph break) separate this part from the next?
        out[name] = (int(before[-1]) if before else 0, raw.rstrip() + '\n', bool(re.search(r'\n[ \t]*\n\s*$', raw)))
    return out

def strip_comments(t):
    t = '\n'.join(l for l in t.split('\n') if not l.lstrip().startswith('%'))
    return re.sub(r'(?<!\\)%.*', '', t)

def per_page(t, first):
    """{page: [notes, resets, paragraph breaks, opening quotes]} between \\opage markers (comments removed)."""
    s = strip_comments(t)
    bits = re.split(r'\\opage\{(\d+)\}', s)
    out = {first: [0, 0, 0, 0]}
    def add(p, x):
        r = out.setdefault(p, [0, 0, 0, 0])
        r[0] += x.count(FN); r[1] += x.count('\\setcounter{footnote}{0}')
        r[2] += len(re.findall(r'\n[ \t]*\n\s*(?=\S)', x))
        r[3] += x.count('„') + x.count('«') + x.count('``')     # this print opens with « (and „) and closes with »
    add(first, bits[0])
    for i in range(1, len(bits), 2):
        add(int(bits[i]), bits[i + 1])
    return out

def check(name, first, da, en):
    """Return a list of problems (strings) for one part."""
    bad = []
    dS, eS = strip_comments(da), strip_comments(en)
    want = re.findall(r'\\opage\{(\d+)\}', dS); got = re.findall(r'\\opage\{(\d+)\}', eS)
    if got != want:
        bad.append(f'\\opage DIFFER: Danish {len(want)}, English {len(got)}; twice '
                   f'{sorted({p for p in got if got.count(p) > 1}, key=int)}; missing {[p for p in want if p not in got]}')
    dm = re.findall(r'^% --- p\. \d+ ---$', da, re.M); em = re.findall(r'^% --- p\. \d+ ---$', en, re.M)
    if dm != em: bad.append(f'page-marker comment lines differ: Danish {len(dm)}, English {len(em)}')
    dp, ep = per_page(da, first), per_page(en, first)
    names = ['notes', 'resets', 'paragraphs', 'quotes']
    for p in sorted(set(dp) | set(ep)):
        a, b = dp.get(p, [0] * 4), ep.get(p, [0] * 4)
        for k in range(3):
            if a[k] != b[k]: bad.append(f'p.{p} {names[k]} Danish {a[k]} English {b[k]}')
        if a[3] != b[3]: bad.append(f'p.{p} (soft) opening quotes Danish {a[3]} English {b[3]}')
    for mac in ('\\emph{', '\\textit{'):
        d, e = dS.count(mac), eS.count(mac)
        if d != e: bad.append(f'(soft) {mac[:-1]} Danish {d} English {e}')
    dg, eg = GREEK.findall(dS), GREEK.findall(eS)
    if [g.strip() for g in dg] != [g.strip() for g in eg]:
        bad.append(f'Greek differs: Danish {dg} / English {eg}')
    glue = [l for l in en.split('\n') if re.search(r'(?<!\\)%\s*$', l) and not l.lstrip().startswith('%')
            and not re.search(r'\\setcounter\{footnote\}\{0\}%$|\\-%$', l) and not re.search(r'(?<!\\)%.', l)]
    for l in glue: bad.append(f'line ends in a bare %: ...{l[-60:]}')
    left = [w for w in ('ɔ:', '„', '“', '»', '«') if w in eS]
    if left: bad.append(f'Danish marks left in the English: {left}')
    return bad

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'list'
    da = split_parts(danish())
    if cmd == 'list':
        for name, ch, _ in PARTS:
            first, t, _ = da[name]; s = strip_comments(t); pg = re.findall(r'\\opage\{(\d+)\}', s)
            print(f'{name:14} {ch:32} from p. {first}: markers {pg[0] if pg else "-"}-{pg[-1] if pg else "-"} '
                  f'({len(pg)}), {len(s.split())} words, {s.count(FN)} notes')
    elif cmd == 'extract':
        print(da[sys.argv[2]][1], end='')
    elif cmd == 'build':
        have = [p for p, _, _ in PARTS if os.path.exists(os.path.join(TR, p + '.texfrag'))]
        print('parts:', ', '.join(have) or 'none', '| missing:', ', '.join(p for p, _, _ in PARTS if p not in have) or 'none')
        en = {p: open(os.path.join(TR, p + '.texfrag'), encoding='utf-8').read().strip() + '\n' for p in have}
        total = 0
        for p in have:
            bad = check(p, da[p][0], da[p][1], en[p])
            hard = [b for b in bad if '(soft)' not in b]; total += len(hard)
            print(f'{p:12} {"OK" if not hard else str(len(hard)) + " problems"}'
                  + (f' ({len(bad) - len(hard)} soft)' if len(bad) > len(hard) else ''))
            for b in bad[:40]: print('    ', b)
        if '--write' in sys.argv:
            if total and '--force' not in sys.argv: sys.exit('not written: fix the problems first (or --force)')
            body = ''.join(en[p] + ('\n' if da[p][2] else '') for p in have)
            tpl = open(TEMPLATE, encoding='utf-8').read()
            out = os.path.join(BOOK, 'translation.tex')
            open(out, 'w', encoding='utf-8').write(tpl.replace('%%PARTS%%', body)); print('wrote', out)
    else:
        sys.exit(__doc__)

if __name__ == '__main__':
    main()
