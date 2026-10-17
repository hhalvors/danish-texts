#!/usr/bin/env python3
"""tr_parts.py -- English translation of Høffding, Kort Oversigt over den nyere Filosofis Historie (4th ed., 1910).
2026-10-17, from religioese-tanketyper's; parts cut at chapter heads (anchors), not page turns.

The Danish (texts/hoeffding/kort-oversigt/transcription.tex, from p. 1 to the end, p. 95; the front matter is in tr_template.tex)
is cut into six parts at chapter heads, so that no sentence is shared by two
translators; each part is translated into ebook-method/kort-oversigt/tr/<PART>.texfrag (tracked) (TRANSLATOR-BRIEF.md, GLOSSARY.md), and `build`
splices the parts into translation.tex from tr_template.tex.

    python3 tr_parts.py list                  # parts, pages, Danish words
    python3 tr_parts.py extract PART          # print that part's Danish
    python3 tr_parts.py build [--write]       # check the parts present; --write writes translation.tex
    options: --book DIR (default texts/hoeffding/kort-oversigt), --parts DIR (default ebook-method/kort-oversigt/tr)

Checks made by build: every \\opage of the Danish once and in order; per printed page the endnote marks
(\\textsuperscript) and the paragraph breaks as in the Danish; \\textit, \\emph, \\textsc and opening-quote counts per part
beside the Danish (soft); lines ending in a bare % that are not comment lines (the glue trap)."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
def opt(name, default): return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default
BOOK = opt('--book', os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt'))
TR = opt('--parts', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tr'))
TEMPLATE = opt('--template', os.path.join(HERE, 'tr_template.tex'))
PARTS = [                    # each part starts at the line matching its anchor (a page marker, or a chapter head: the
                             # page turns of this print fall inside sentences, so the parts are cut at the heads)
    ('A-indledning-tilbliven', r'% --- p\. 1 ---', 'Indledning, I. Den nyere Filosofis Tilbliven (pp. 1-17)'),
    ('B-systemdannelser', r'\\chapterhead\{II\.\}', 'II. Systemdannelser (pp. 17-35)'),
    ('C-erfaring-oplysning', r'\\chapterhead\{III\.\}', 'III. Erfaringsfilosofien, IV. Oplysningsfilosofien (pp. 35-49)'),
    ('D-kant', r'% --- p\. 50 ---', 'V. Immanuel Kant og den kritiske Filosofi (pp. 50-63)'),
    ('E-romantik-positivisme', r'\\closerule$(?=\n\n(?:\\opage\{\d+\})?\\chapterhead\{VI\.)', 'VI. Romantikens Filosofi, VII. Positivismen (pp. 63-81)'),
    ('F-problembehandlinger', r'\\closerule$(?=\n\n\\chapterheadone)', 'VIII. Nyere Problembehandlinger, Tillæg (pp. 81-95)'),
]
def danish(): return open(os.path.join(BOOK, 'transcription.tex'), encoding='utf-8').read()
def split_parts(text):
    L = text.split('\n'); starts = []; off = [0]
    for l in L: off.append(off[-1] + len(l) + 1)
    for name, anchor, _ in PARTS:
        hits = sorted({text.count('\n', 0, m.start()) for m in re.finditer('(?m)^' + anchor, text)})
        if len(hits) != 1: sys.exit(f'{name}: anchor {anchor!r} matches {len(hits)} lines')
        starts.append(hits[0])
    end = next(i for i, l in enumerate(L) if l.startswith('\\end{document}'))
    if starts != sorted(starts): sys.exit('anchors out of order')
    out = {}
    for k in range(len(PARTS)):
        seg = L[starts[k]:(starts[k + 1] if k + 1 < len(PARTS) else end)]
        out[PARTS[k][0]] = '\n'.join(seg)
    return out
def strip_comments(t):
    t = '\n'.join(l for l in t.split('\n') if not l.lstrip().startswith('%'))
    return re.sub(r'(?<!\\)%.*', '', t)
def per_page(t):
    """{page: [footnotes, paragraph breaks]} between \\opage markers (comments removed)"""
    out, cur = {}, None; s = strip_comments(t)
    s = re.sub(r'\n[ \t]*\n(?:[ \t]*\n)*', '\n\u00b6\n', s)
    for m in re.finditer(r'\\opage\{(\w+)\}|\\footnote\[\d+\]|\u00b6', s):
        if m.group(1): cur = m.group(1); out.setdefault(cur, [0, 0])
        elif cur is None: continue
        elif m.group(0) == '\u00b6': out[cur][1] += 1
        else: out[cur][0] += 1
    return out
def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'list'
    da = split_parts(danish())
    if cmd == 'list':
        for name, _, desc in PARTS:
            s = strip_comments(da[name]); pg = re.findall(r'\\opage\{(\w+)\}', s)
            print(f'{name:18} {desc:64} pages {pg[0]}-{pg[-1]} ({len(pg)} markers), {len(s.split())} words')
    elif cmd == 'extract': print(da[sys.argv[2]])
    elif cmd == 'build':
        have = [p for p, _, _ in PARTS if os.path.exists(os.path.join(TR, p + '.texfrag'))]
        en = {p: open(os.path.join(TR, p + '.texfrag'), encoding='utf-8').read().strip() for p in have}
        print('parts:', ', '.join(have) or 'none', '| missing:', ', '.join(p for p, _, _ in PARTS if p not in have) or 'none')
        for p in have:
            want = re.findall(r'\\opage\{(\w+)\}', strip_comments(da[p])); got = re.findall(r'\\opage\{(\w+)\}', strip_comments(en[p]))
            print(f'{p}: page markers', 'OK' if got == want else f'DIFFER (Danish {len(want)}, English {len(got)})')
            if got != want:
                print('   twice:', sorted({x for x in got if got.count(x) > 1}), '| missing:', [x for x in want if x not in got])
            dp, ep = per_page(da[p]), per_page(en[p])
            bad = [f'p.{q} marks {dp[q][0]}/{ep.get(q, [0, 0])[0]} paragraphs {dp[q][1]}/{ep.get(q, [0, 0])[1]}' for q in dp if dp[q] != ep.get(q)]
            print(f'{p}: pages whose endnote marks or paragraph breaks differ (Danish/English):', 'OK' if not bad else bad)
            for c in ('\\textit{', '\\emph{', '\\textsc{'):
                d, e = strip_comments(da[p]).count(c), strip_comments(en[p]).count(c)
                print(f'   {c:10} Danish {d:4} English {e:4}' + ('' if d == e else '   <-- check (soft)'))
            d, e = strip_comments(da[p]).count('„'), strip_comments(en[p]).count('``')
            print(f'   quotes     Danish {d:4} English {e:4}' + ('' if d == e else '   <-- check (soft)'))
        body = '\n\n'.join(en[p] for p in have)
        glue = [l for l in body.split('\n') if re.search(r'(?<!\\)%\s*$', l) and not l.lstrip().startswith(('%', '\\setcounter'))]
        print('lines ending in a bare % (glue trap):', len(glue)); [print('   ', l[-80:]) for l in glue[:20]]
        if '--write' in sys.argv:
            tpl = open(TEMPLATE, encoding='utf-8').read(); out = os.path.join(BOOK, 'translation.tex')
            open(out, 'w', encoding='utf-8').write(tpl.replace('%%PARTS%%', body)); print('wrote', out)
    else: sys.exit(__doc__)
if __name__ == '__main__': main()
