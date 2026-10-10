#!/usr/bin/env python3
"""pagemap.py <printed> -> PDF page; --scan -> scan path.
Høffding, Psykologiske Undersøgelser (Vidensk. Selsk. Skr., 6. Række, hist.-philos. Afd. III, no. 1;
Kjøbenhavn: Bianco Luno 1889), pp. 1-103, in Google's scan of the whole Academy volume (Stanford copy,
Google Books hgMNAQAAIAAJ; SCANS.tsv). PDF = printed + 24, verified 2026-10-09 by folio at pp. 6, 30,
50, 76, 100, 102, 103: p. 1 = title (PDF 25), p. 3 = Indhold (PDF 27; its left edge is cut off in the
gutter), p. 5 = Indledning (PDF 29). PDF 128 blank; Blinkenberg's Eretriske Gravskrifter from PDF 129.
Scan: ~/bibliotek/Høffding, Harald/1889-1895-vidensk-selsk-skrifter-6r-hist-filos-III.pdf."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
FIRST_PRINTED, LAST_PRINTED, OFFSET = 1, 103, 24
REL = os.path.join("bibliotek", "Høffding, Harald", "1889-1895-vidensk-selsk-skrifter-6r-hist-filos-III.pdf")
def scan_path():
    for p in [os.environ.get("SCAN", ""), os.path.join(os.path.expanduser("~"), REL), os.path.join(os.path.expanduser("~"), "mnt", REL)]:
        if p and os.access(p, os.R_OK): return p
    raise SystemExit("cannot find the scan: ~/" + REL)
def pdfpage(n):
    if not FIRST_PRINTED <= n <= LAST_PRINTED: raise ValueError(n)
    return n + OFFSET
if __name__ == "__main__":
    print(scan_path() if sys.argv[1:] == ["--scan"] else "\n".join(str(pdfpage(int(a))) for a in sys.argv[1:]))
