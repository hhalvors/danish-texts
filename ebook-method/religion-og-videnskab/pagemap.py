"""pagemap.py -- Høffding, "Religion og Videnskab", Religionshistoriske Smaaskrifter I (1910).
PDF = printed + 9 in the bound volume 1-6, pp. 1-59 (PDF 10-68), verified 2026-10-03 by text on pp. 2-3.
Scan: ~/bibliotek/Høffding, Harald/1910-1911-religionshistoriske-smaaskrifter-bd1-6.pdf (SCANS.tsv).  Settings for ebook-method/collate/check.py (see its docstring)."""
import os
FIRST_PRINTED, LAST_PRINTED, OFFSET = 1, 59, 9
REL = os.path.join("bibliotek", 'Høffding, Harald', '1910-1911-religionshistoriske-smaaskrifter-bd1-6.pdf')
def scan_path():
    for p in [os.environ.get("SCAN", ""), os.path.join(os.path.expanduser("~"), REL), os.path.join(os.path.expanduser("~"), "mnt", REL)]:
        if p and os.access(p, os.R_OK): return p
    raise SystemExit("cannot find the scan: ~/" + REL)
def pdfpage(n):
    if not FIRST_PRINTED <= n <= LAST_PRINTED: raise ValueError(n)
    return n + OFFSET
FOOT = r"Høffding: Religion|^\W*[\d*†]+\W*$"
