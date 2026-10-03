#!/usr/bin/env python3
"""pagemap.py -- Høffding, "Vort Hjem. En Indledning", in Emma Gad (ed.), Vort Hjem I (1903).
PDF = printed + 4, pp. 3-12 (PDF 7-16); the layer carries running heads "VORT HJEM." with folios.
Scan: ~/bibliotek/Høffding, Harald/1903-vort-hjem.pdf (SCANS.tsv)."""
import os, sys
FIRST_PRINTED, LAST_PRINTED, OFFSET = 3, 12, 4
REL = os.path.join("bibliotek", "Høffding, Harald", "1903-vort-hjem.pdf")
def scan_path():
    for p in [os.environ.get("SCAN", ""), os.path.join(os.path.expanduser("~"), REL), os.path.join(os.path.expanduser("~"), "mnt", REL)]:
        if p and os.access(p, os.R_OK): return p
    raise SystemExit("cannot find the scan: ~/" + REL)
def pdfpage(n):
    if not FIRST_PRINTED <= n <= LAST_PRINTED: raise ValueError(n)
    return n + OFFSET

FIRST_FROM = 'I.'          # p. 3 opens with the title block, which the transcription sets with \maketitle
