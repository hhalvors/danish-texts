"""pagemap.py -- Kontinuiteten i Kants filosofiske Udviklingsgang (1893). PDF = printed + 0, pp. 5-58. Settings for ebook-method/collate/check.py."""
import os
FIRST_PRINTED, LAST_PRINTED, OFFSET = 5, 58, 0
REL = os.path.join("bibliotek", "Høffding, Harald", "1893-kontinuiteten-kants-udviklingsgang.pdf")
def scan_path():
    for p in [os.environ.get("SCAN", ""), os.path.join(os.path.expanduser("~"), REL), os.path.join(os.path.expanduser("~"), "mnt", REL)]:
        if p and os.access(p, os.R_OK): return p
    raise SystemExit("cannot find the scan: ~/" + REL)
def pdfpage(n):
    if not FIRST_PRINTED <= n <= LAST_PRINTED: raise ValueError(n)
    return n + OFFSET
