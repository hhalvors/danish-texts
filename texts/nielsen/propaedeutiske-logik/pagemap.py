#!/usr/bin/env python3
"""
pagemap.py <printed_page> [...]   ->  PDF page number(s), one per line
pagemap.py --scan                 ->  path to the scan

THE SINGLE SOURCE OF TRUTH FOR THE PAGE OFFSET. ocr.sh and spacing.py call
this; do not hard-code +9 anywhere.

R. Nielsen, *Den propædeutiske Logik* (Kjøbenhavn: P. G. Philipsen, 1845).
KB scan, ABBYY Recognition Server, 297 PDF pages, A4.

    printed  1-283  ->  PDF = printed + 9      (PDF 10-292)

UNIFORM. Unlike the Evangelietroen scan, no leaf was scanned twice and the
offset never changes.

How it was verified (do not redo casually):
  * The PDF's own ABBYY text layer puts the printed numeral on its own first
    line for 233 of the 298 pages. 224 of those give offset exactly +9; the
    seven that do not (PDF 69, 104, 195, 215, 226, 235, 265, 270, 271) are
    single-digit OCR misreadings whose immediate neighbours are +9, so none is
    a real offset change.
  * A text-similarity sweep over every adjacent and next-but-one page pair
    found no duplicated leaf.
  * The endpoints and the numeral-less opening run were read off the image at
    200 dpi: PDF 11=2, 12=3, 13=4, 14=5, 16=7, 292=283.

Front and back matter (outside pagemap's range, addressed by PDF page):
    PDF   1  KB digitisation notice (not part of the book)
    PDF   3  Kongelige Bibliotek stamp leaf
    PDF   6  title page
    PDF   8-9  Indhold (contents)
    PDF  10  printed p. 1, "Indledning"
    PDF  15  printed p. 6, division title "Den propædeutiske Logiks / Første Deel"
    PDF 292  printed p. 283, last page of text
    PDF 293  "Rettelser" (errata) -- APPLY THESE, flagged with % ERRATA
    PDF 294-297  blank
"""
import glob
import os
import sys

SCAN_NAME = "1845-propædeutiske-logik.pdf"
FIRST_PRINTED, LAST_PRINTED = 1, 283
OFFSET = 9


def scan_path() -> str:
    """Locate the KB scan. Several /sessions/<id>/ dirs may exist and only the
    current one is readable, so test readability rather than taking the first.

    NB the filename contains 'æ'. macOS hands it over in NFD, so a literal
    bash glob written in NFC will not match; this walks the directory and
    compares with unicodedata.normalize instead."""
    import unicodedata
    if os.environ.get("SCAN") and os.access(os.environ["SCAN"], os.R_OK):
        return os.environ["SCAN"]
    want = unicodedata.normalize("NFC", SCAN_NAME)
    for d in glob.glob("/sessions/*/mnt/bibliotek/Nielsen, Rasmus"):
        if not os.access(d, os.R_OK):
            continue
        for f in os.listdir(d):
            if unicodedata.normalize("NFC", f) == want:
                p = os.path.join(d, f)
                if os.access(p, os.R_OK):
                    return p
    raise SystemExit(
        f"cannot find a readable {SCAN_NAME} under /sessions/*/mnt/bibliotek/"
        "'Nielsen, Rasmus'/ — is the bibliotek folder mounted in this session? "
        "If not, call mcp__cowork__request_cowork_directory with "
        "path /Users/hhalvors/bibliotek and wait for it to mount.")


def pdfpage(printed: int) -> int:
    if printed < FIRST_PRINTED or printed > LAST_PRINTED:
        raise ValueError(
            f"printed page {printed} is outside the body "
            f"({FIRST_PRINTED}-{LAST_PRINTED})")
    return printed + OFFSET


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--scan":
        print(scan_path())
    else:
        for a in sys.argv[1:]:
            print(pdfpage(int(a)))
