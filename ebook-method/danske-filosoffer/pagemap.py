#!/usr/bin/env python3
"""pagemap.py <printed> -> PDF page; --scan -> scan path.
Høffding, Danske Filosofer (Gyldendal, København 1909).
PDF = printed + 15, pp. 1-206. Verified 2026-10-02 against the INDHOLD (PDF 14): chapter heads
found in the layer at PDF 40/64/88/112 = pp. 25/49/73/97; running heads with folios (p. 181 at
PDF 196) agree. The layer carries folios only on a few pages. PDF 10 = half-title,
PDF 12 = title, PDF 14 = Indhold; PDF 222-227 = publisher. pages/blank (not part of the work).
Scan: ~/bibliotek/Høffding, Harald/danske-filosoffer.pdf (KB)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
FIRST_PRINTED, LAST_PRINTED, OFFSET = 1, 206, 15
REL = os.path.join("bibliotek", "Høffding, Harald", "danske-filosoffer.pdf")
def scan_path():
    for p in [os.environ.get("SCAN", ""), os.path.join(os.path.expanduser("~"), REL), os.path.join(os.path.expanduser("~"), "mnt", REL)]:
        if p and os.access(p, os.R_OK): return p
    raise SystemExit("cannot find the scan: ~/" + REL)
def pdfpage(n):
    if not FIRST_PRINTED <= n <= LAST_PRINTED: raise ValueError(n)
    return n + OFFSET
if __name__ == "__main__":
    print(scan_path() if sys.argv[1:] == ["--scan"] else "\n".join(str(pdfpage(int(a))) for a in sys.argv[1:]))
