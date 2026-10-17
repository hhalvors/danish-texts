#!/usr/bin/env python3
"""nohead.py -- take the RUNNING HEAD (folio + the page's summary line) out of the tesseract witness before collate/check.py
reads it (moderne-filosoffer, 2026-10-14).  check.py's HEAD regex drops a head only when it is the witness's first line
and reads as one; on this book tesseract often merged the head's words into the first text line ("BeBradleys
Mysticisme. kræftelse").  Here the head is found by position: on every page that has one (not pagemap.NOHEAD), the
words above the first wide gap (over 1.5 x the page's median line pitch) within the top three lines.  The original TSV
is kept as pN.tsv.orig; rerunnable (always works from .orig).
    python3 ebook-method/kort-oversigt/nohead.py        -> rewrites .parts/collate/ocr/pN.tsv, clears check.py's line cache"""
import os, sys, glob, shutil, statistics
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE); import pagemap as C
O = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt', '.parts', 'collate', 'ocr')
n = 0
for p in range(C.FIRST_PRINTED, C.LAST_PRINTED + 1):
    f = os.path.join(O, f'p{p}.tsv')
    if not os.path.exists(f + '.orig'): shutil.copy2(f, f + '.orig')
    rows = open(f + '.orig', encoding='utf-8').read().splitlines()
    if p in C.NOHEAD: open(f, 'w', encoding='utf-8').write('\n'.join(rows) + '\n'); continue
    W = [r.split('\t') for r in rows[1:]]
    W = [r for r in W if len(r) == 12 and r[0] == '5' and r[11].strip()]
    ys = sorted(int(r[7]) + int(r[9]) / 2 for r in W if int(r[9]) > 15)       # word centres (px), ignoring specks
    lines = []
    for y in ys:
        if lines and y - lines[-1][-1] < 20: lines[-1].append(y)
        else: lines.append([y])
    cy = [statistics.median(l) for l in lines if len(l) >= 2]
    d = sorted(b - a for a, b in zip(cy, cy[1:])); m = d[len(d) // 2] if d else 0
    cut = None
    for i in range(min(3, len(cy) - 1)):
        if cy[i + 1] - cy[i] > 1.5 * m: cut = (cy[i] + cy[i + 1]) / 2; break
    keep = [rows[0]] + [r for r in rows[1:] if not (cut and len(r.split('\t')) == 12 and r.split('\t')[0] == '5'
                                                    and int(r.split('\t')[7]) + int(r.split('\t')[9]) / 2 < cut)]
    open(f, 'w', encoding='utf-8').write('\n'.join(keep) + '\n'); n += cut is not None
    if cut is None: print('no head found on p.', p)
# check.py's line cache (.parts/collate/lines-ocr) is keyed on pagemap.py: bump its last line after running this
print(f'running head cut on {n} pages')
