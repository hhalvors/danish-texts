#!/usr/bin/env python3
"""ebookdiff.py (2026-10-14, for Oplevelse og Tydning; replaces the copy from moderne-filosoffer) -- the SAGA e-book
(Lindhardt og Ringhof 2020, the 1918 text) against the finished transcription, word by word with punctuation: (1) the
running text (footnotes taken out; the e-book's note references dropped), Fortale to the end; (2) the 141 footnotes in
order against the e-book's 141 numbered notes.  The collation (NB's layer against tesseract, the e-book voting where they
differ) cannot see a fault both OCRs share; the e-book, made independently, can.  Nothing is applied: every difference
is listed with its page for the image.  Spelling the e-book modernised, or its own OCR faults, are expected among them.
    python3 ebook-method/kort-oversigt/ebookdiff.py   -> .parts/ebookdiff.tsv (page, where, tex, ebook, context)"""
import os, re, sys, zipfile, html, difflib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import pagemap as C
z = zipfile.ZipFile(os.path.join(C.BOOKDIR, 'Kort_oversigt_over_den_nyere_filosofis_historie.epub'))
def ebplain(x):
    x = re.sub(r'<span class="ref-note-rw".*?</span>', ' ', x, flags=re.S)
    x = re.sub(r'<title>.*?</title>', ' ', x, flags=re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', x))).replace('\u00ad', '').strip()
body_names = sorted(n for n in z.namelist() if re.search(r'OPS/s0(0[3-9]|1[01])-', n))
EB = ebplain(' '.join(z.read(n).decode('utf-8') for n in body_names))
EB = re.sub(r'^(INDLEDNING )+', 'INDLEDNING ', EB)
notes_x = z.read('OPS/s013-Notes-01.xhtml').decode('utf-8')
EN = [ebplain(re.sub(r'<span class="num-note-rw".*?</span>', '', b.split('</p>')[0], flags=re.S)) for b in notes_x.split('epub:type="rearnote"')[1:]]
T = open(os.path.join(C.BOOKDIR, 'transcription.tex'), encoding='utf-8').read()
T = T[T.index('\\opage{1}'):T.rindex('\\end{document}')]
# a word divided across a page turn (house convention: „plud%“ ... „\opage{13}selige“): join it before splitting on markers
T = re.sub(r'(?<=[^\W\d_])%\n((?:%[^\n]*\n|\\setcounter\{footnote\}\{0\}%\n)*)(\\opage\{\d+\})', lambda m: m.group(2) + '⟨J⟩', T)
T = re.sub(r'(?m)^\\(?:begin|end)\{(?:quote|center)\}', ' ', T)
def texplain(s):
    s = re.sub(r'(?m)^%.*$', '', s).replace('%\n', '')
    s = re.sub(r'\\(?:prefacehead|booktitle|introhead|chapterhead|sectionhead|essayhead|essaysource|subhead|romanhead)\b', ' ', s)
    s = s.replace('\\dots{}', '...').replace('---', '—').replace('\\&', '&').replace('\\\\', ' ')
    s = re.sub(r'\\textsuperscript\{([^{}]*)\}', r'\1', s)
    s = re.sub(r'\\(?:setcounter|addtocounter)\{[^{}]*\}\{[^{}]*\}', ' ', s)
    s = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?', ' ', s)
    return re.sub(r'\s+', ' ', s.replace('{', ' ').replace('}', ' ')).strip()
# split the tex into body tokens (with page) and notes
toks, notes, page = [], [], 1
i = 0
for m in re.finditer(r'% --- p\. (\d+) ---|\\opage\{(\d+)\}|\\footnote\[\d+\]\{', T):
    chunk = T[i:m.start()]
    toks += [(w, page) for w in texplain(chunk).split()]
    if m.group(1) or m.group(2):
        page = int(m.group(1) or m.group(2)); i = m.end()
        if T.startswith('⟨J⟩', i) and toks:                 # the second part of a divided word joins the first
            m2 = re.match(r'⟨J⟩([^\s\\{}%]+)', T[i:])
            if m2 and toks: w0, p0 = toks.pop(); toks.append((w0 + texplain(m2.group(1)), p0)); i += m2.end()
        continue
    j = m.end(); d = 1
    while d: d += {'{': 1, '}': -1}.get(T[j], 0); j += 1
    notes.append((page, texplain(T[m.end():j - 1]))); i = j
toks += [(w, page) for w in texplain(T[i:]).split()]
qn = lambda w: w.replace('„', '"').replace('“', '"').replace('”', '"').replace('’', "'").replace('»', '"').replace('«', '"')
out = []
a = [qn(w) for w, p in toks]; b = [qn(w) for w in EB.split()]
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
    if op == 'equal': continue
    pg = toks[min(i1, len(toks) - 1)][1]
    ctx = ' '.join(w for w, p in toks[max(0, i1 - 4):i1])
    out.append((pg, 'text', ' '.join(w for w, p in toks[i1:i2]), ' '.join(EB.split()[j1:j2]), ctx))
for k, (pg, nt) in enumerate(notes):
    if k >= len(EN): out.append((pg, f'note {k + 1}', nt, '(none)', '')); continue
    a, b = [qn(w) for w in nt.split()], [qn(w) for w in EN[k].split()]
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op != 'equal': out.append((pg, f'note {k + 1}', ' '.join(nt.split()[i1:i2]), ' '.join(EN[k].split()[j1:j2]), ' '.join(nt.split()[max(0, i1 - 3):i1])))
with open(os.path.join(C.BOOKDIR, '.parts', 'ebookdiff.tsv'), 'w', encoding='utf-8') as fh:
    for r in out: fh.write('\t'.join(map(str, r)) + '\n')
print(f'{len(toks)} text words, {len(notes)} notes; {len(out)} differences ({sum(1 for r in out if r[1] == "text")} in the text) -> .parts/ebookdiff.tsv')
