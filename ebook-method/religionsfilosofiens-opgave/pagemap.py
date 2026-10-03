"""pagemap.py -- Høffding, "Om Religionsfilosofiens Opgave og Fremgangsmaade", Oversigt 1900 Nr. 5.
PDF = printed - 410, pp. 411-421 (PDF 1-11), verified 2026-10-03.  The transcription was made from this
scan's ABBYY layer, so the witness is a fresh OCR.  Offprint folios 1-11 at the foot.
Scan: ~/bibliotek/Høffding, Harald/1900-religionsfilosofiens-opgave.pdf (SCANS.tsv).  Settings for ebook-method/collate/check.py (see its docstring)."""
import os
FIRST_PRINTED, LAST_PRINTED, OFFSET = 411, 421, -410
WITNESS = "ocr"
REL = os.path.join("bibliotek", 'Høffding, Harald', '1900-religionsfilosofiens-opgave.pdf')
def scan_path():
    for p in [os.environ.get("SCAN", ""), os.path.join(os.path.expanduser("~"), REL), os.path.join(os.path.expanduser("~"), "mnt", REL)]:
        if p and os.access(p, os.R_OK): return p
    raise SystemExit("cannot find the scan: ~/" + REL)
def pdfpage(n):
    if not FIRST_PRINTED <= n <= LAST_PRINTED: raise ValueError(n)
    return n + OFFSET
HEAD = r"Religionsfilosofiens Opgave og Fremgangsmaade|^\W*Harald H.ffding\.?\W*\d*\W*$|^\W*\d+\W*$|OVERSIGT OVER|FORHANDLINGER|Meddelt i M.det|^\W*Af\W*$"
FOOT = r"Vid\. Selsk|^\W*[\d*†]+\W*$"
