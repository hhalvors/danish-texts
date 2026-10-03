"""pagemap.py -- Høffding, "Pascal et Kierkegaard", Revue de Métaphysique et de Morale 30:2 (1923), pp. 221-246.
PDF = printed + 18, pp. 221-246 (PDF 239-264), verified 2026-10-03 by OCR of p. 221.  The scan has no text
layer; the transcription was made from the Internet Archive's tesseract 5 OCR (texts/.../ocr.sh), so the
witness here (tesseract 4, tessdata_best fra) is a different engine and model but not wholly independent.
Running heads: "N REVUE DE METAPHYSIQUE ET DE MORALE" / "H. HOFFDING. -- PASCAL ET KIERKEGAARD. N".
Scan: ~/bibliotek/Høffding, Harald/1923-pascal-kierkegaard.pdf (SCANS.tsv)."""
import os
FIRST_PRINTED, LAST_PRINTED, OFFSET = 221, 246, 18
WITNESS = "ocr"
LANG = "fra"
HEAD = r"REVUE DE M|H\. H.FFDING|PASCAL ET .{1,3}ERK|^\W*\d+\W*$"
FOOT = r"Rev\. M.ta|^\W*[\d*†]+\W*$"
REL = os.path.join("bibliotek", "Høffding, Harald", "1923-pascal-kierkegaard.pdf")
def scan_path():
    for p in [os.environ.get("SCAN", ""), os.path.join(os.path.expanduser("~"), REL), os.path.join(os.path.expanduser("~"), "mnt", REL)]:
        if p and os.access(p, os.R_OK): return p
    raise SystemExit("cannot find the scan: ~/" + REL)
def pdfpage(n):
    if not FIRST_PRINTED <= n <= LAST_PRINTED: raise ValueError(n)
    return n + OFFSET
ITAL = 1.00         # this journal's italic leans less: italic words score 1.00-1.06 here (checked 2026-10-03)
