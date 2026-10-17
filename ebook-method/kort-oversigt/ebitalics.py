#!/usr/bin/env python3
"""ebook-method/kort-oversigt/ebitalics.py -- list the e-book's italics (<i>/<em>) with the page each falls on in the
transcription (found by the three words before it), as a list for the image: the slant detector (check.py --italics)
misses short words, and the e-book marks the italics of the 41 pages read on 23 Sep 2026 exactly (maa, mit, Kulturformer).
    python3 ebook-method/kort-oversigt/ebitalics.py   -> prints: file | words before [italic] words after | p. N"""
import os, re, zipfile, html
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
BOOK = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt')
z = zipfile.ZipFile(os.path.join(BOOK, 'Kort_oversigt_over_den_nyere_filosofis_historie.epub'))
T = open(os.path.join(BOOK, 'transcription.tex'), encoding='utf-8').read()
marks = [(m.start(), int(m.group(1))) for m in re.finditer(r'% --- p\. (\d+) ---', T)]
def page(i):
    p = 6
    for s, q in marks:
        if s <= i: p = q
        else: break
    return p
def plain(x): return html.unescape(re.sub('<[^>]+>', ' ', x))
for n in sorted(z.namelist()):
    if not n.endswith('.xhtml'): continue
    t = z.read(n).decode('utf-8')
    for m in re.finditer(r'<(i|em)\b[^>]*>(.*?)</\1>', t, re.S):
        pre = plain(t[max(0, m.start() - 120):m.start()]).split()[-3:]
        w = plain(m.group(2)).split()
        post = plain(t[m.end():m.end() + 80]).split()[:2]
        sep = r'(?:\s|%[^\n]*\n|\\opage\{\d+\}|\\setcounter\{footnote\}\{0\})+'
        mm = re.search(sep.join(map(re.escape, pre + w[:1])), T) if w else None
        print(os.path.basename(n), '|', ' '.join(pre), '[', ' '.join(w), ']', ' '.join(post), '| p.', page(mm.start()) if mm else '?')
