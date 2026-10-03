"""pagemap.py -- Høffding (ed.), Udvalgte Stykker af dansk filosofisk Litteratur (1910): ch. IV opening (p. 99) and Treschow, "Udviklingslære" (pp. 108-113).
PDF = printed + 8 (Internet Archive scan), verified 2026-10-03 on pp. 108, 113, 114.  The transcription
was made from this scan's own OCR layer, so the witness is a fresh OCR.  P. 114 (Sibbern) is not transcribed.
Scan: ~/bibliotek/Høffding, Harald/1910-udvalgte-stykker-dansk-filosofisk-litteratur.pdf (SCANS.tsv).  Settings for ebook-method/collate/check.py (see its docstring)."""
import os
FIRST_PRINTED, LAST_PRINTED, OFFSET = 99, 113, 8
PAGES = [99] + list(range(108, 114))
WITNESS = "ocr"
REL = os.path.join("bibliotek", 'Høffding, Harald', '1910-udvalgte-stykker-dansk-filosofisk-litteratur.pdf')
def scan_path():
    for p in [os.environ.get("SCAN", ""), os.path.join(os.path.expanduser("~"), REL), os.path.join(os.path.expanduser("~"), "mnt", REL)]:
        if p and os.access(p, os.R_OK): return p
    raise SystemExit("cannot find the scan: ~/" + REL)
def pdfpage(n):
    if not FIRST_PRINTED <= n <= LAST_PRINTED: raise ValueError(n)
    return n + OFFSET
HEAD = r"Dansk filosofisk Litteratur|UDVIKLINGSL|^\W*\d+\W*$"
CUTS = {99: (None, "UUDT"), 108: ("B.", None)}   # excerpt A (Treschow, pp. 99-108) is deliberately not transcribed
FOOT = r"Dansk filosofisk Litt|^\W*[\d*†]+\W*$"
