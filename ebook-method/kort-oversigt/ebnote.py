#!/usr/bin/env python3
"""ebnote.py (2026-10-14) -- the e-book's note N with the words before its mark in the text (a finding aid for note
placement; the e-book numbers the page notes 1-141 through the book).   python3 ebnote.py N [N2 ...]"""
import os, re, sys, zipfile, html
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import pagemap as C
z = zipfile.ZipFile(os.path.join(C.BOOKDIR, 'Kort_oversigt_over_den_nyere_filosofis_historie.epub'))
txt = ' '.join(z.read(n).decode('utf-8') for n in sorted(z.namelist()) if n.endswith('.xhtml') and 'Notes' not in n)
notes = z.read('OPS/s017-Notes-01.xhtml').decode('utf-8')
plain = lambda s: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()
for a in sys.argv[1:]:
    n = int(a); m = re.search(r'id="rw-ref-note-%d"' % n, txt)
    before = plain(re.sub(r'<span class="ref-note-rw".*?</span>', '', txt[max(0, m.start() - 1500):m.start()], flags=re.S))[-90:] if m else '?'
    after = plain(txt[m.end():m.end() + 600])[:60] if m else ''
    nb = re.search(r'id="rw-num-note-%d".*?</span>(.*?)</p>' % n, notes, re.S)
    print(f'[{n}] ...{before} ^{n} {after}\n     NOTE: {plain(nb.group(1)) if nb else "?"}')
