"""pagemap.py -- Høffding, "Om Realisme i Videnskab og Tro" (1882), in Mindre Arbejder I (1899).
PDF = printed + 15, pp. 1-14 (PDF 16-29), verified 2026-10-03 on p. 1 (title) and p. 14 (folio).
P. 1 opens with the title and its footnote (set in the transcription's \\maketitle); the foot of p. 1
carries the signature line "Høffding: Mindre Arbejder."; pencil letters in the outer margins.
Scan: ~/bibliotek/Høffding, Harald/1899-1913-mindre-arbejder-bd1.pdf (SCANS.tsv).  Settings for ebook-method/collate/check.py (see its docstring)."""
import os
FIRST_PRINTED, LAST_PRINTED, OFFSET = 1, 14, 15
FIRST_FROM = "Ordet"
FOOT = r"Mindre Arbejder|^[\d*†]+\.?$"
REL = os.path.join("bibliotek", 'Høffding, Harald', '1899-1913-mindre-arbejder-bd1.pdf')
def scan_path():
    for p in [os.environ.get("SCAN", ""), os.path.join(os.path.expanduser("~"), REL), os.path.join(os.path.expanduser("~"), "mnt", REL)]:
        if p and os.access(p, os.R_OK): return p
    raise SystemExit("cannot find the scan: ~/" + REL)
def pdfpage(n):
    if not FIRST_PRINTED <= n <= LAST_PRINTED: raise ValueError(n)
    return n + OFFSET
HEAD = r"Om Realisme i Videnskab|^\W*\d+\W*$"
