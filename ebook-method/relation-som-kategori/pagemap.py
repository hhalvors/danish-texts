"""pagemap.py -- Relation som Kategori (1921). PDF = printed + 2, pp. 3-109. Settings for ebook-method/collate/check.py."""
import os
FIRST_PRINTED, LAST_PRINTED, OFFSET = 3, 109, 2
HEAD = r"Harald H.ffding|Relation som Kategori|^\\W*\\d+\\W*$"
REL = os.path.join("bibliotek", "Høffding, Harald", "1921-relation-som-kategori.pdf")
def scan_path():
    for p in [os.environ.get("SCAN", ""), os.path.join(os.path.expanduser("~"), REL), os.path.join(os.path.expanduser("~"), "mnt", REL)]:
        if p and os.access(p, os.R_OK): return p
    raise SystemExit("cannot find the scan: ~/" + REL)
def pdfpage(n):
    if not FIRST_PRINTED <= n <= LAST_PRINTED: raise ValueError(n)
    return n + OFFSET
