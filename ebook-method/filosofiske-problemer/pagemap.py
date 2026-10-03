#!/usr/bin/env python3
"""pagemap.py <printed> -> PDF page; --scan -> scan path.
Høffding, Filosofiske Problemer (Universitetsprogram, København 1902).
PDF = printed + 13, pp. 1-90 (text 1-84, Noter 85-90). Verified 2026-10-02 against the
book's own INDHOLD (PDF 12): chapter heads found in the layer at PDF 19/41/66/83 = pp.
6/28/53/70 as the Indhold gives. The layer carries no folios. PDF 10 = Forord, PDF 12 =
Indhold; PDF 104-123 = bound-in university list of new doctors (not part of the work).
Scan: ~/bibliotek/Høffding, Harald/1902-filosofiske-problemer.pdf (KB, 300 ppi 1-bit)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
FIRST_PRINTED, LAST_PRINTED, OFFSET = 1, 90, 13
REL = os.path.join("bibliotek", "Høffding, Harald", "1902-filosofiske-problemer.pdf")
def scan_path():
    for p in [os.environ.get("SCAN", ""), os.path.join(os.path.expanduser("~"), REL), os.path.join(os.path.expanduser("~"), "mnt", REL)]:
        if p and os.access(p, os.R_OK): return p
    raise SystemExit("cannot find the scan: ~/" + REL)
def pdfpage(n):
    if not FIRST_PRINTED <= n <= LAST_PRINTED: raise ValueError(n)
    return n + OFFSET
if __name__ == "__main__":
    print(scan_path() if sys.argv[1:] == ["--scan"] else "\n".join(str(pdfpage(int(a))) for a in sys.argv[1:]))
