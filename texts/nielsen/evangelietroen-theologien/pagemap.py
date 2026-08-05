#!/usr/bin/env python3
"""
pagemap.py <printed_page> [...]   ->  PDF page number(s), one per line

THE SINGLE SOURCE OF TRUTH FOR THE PAGE OFFSET. twoup.sh, ocr.sh and spacing.py
all call this; do not hard-code +13 anywhere.

The KB scan of this book is NOT uniformly printed+13. The leaf bearing printed
pp. 82-83 was scanned TWICE: it appears at PDF 95-96 and again at PDF 97-98.
Everything from printed p. 84 on is therefore pushed back by two.

    printed   1- 83  ->  PDF = printed + 13     (PDF  14- 96)
    [PDF 97-98 = a duplicate of printed 82-83; skip them]
    printed  84-174  ->  PDF = printed + 15     (PDF  99-189)

Verified by reading the printed page numbers off the scan for every page from
PDF 14 to 192: the only sustained change of offset is at PDF 97, and the
endpoints check out (PDF 14 = printed 1, PDF 96 = printed 83, PDF 99 = printed
84, PDF 189 = printed 174, PDF 190-191 = Indhold).

Apparent one-page jumps at PDF 47, 68, 119 and 141 are OCR misreadings of the
header numeral (34 read as 31, 55 as 53, 104 as 101, 128 as 426) — the following
page reverts, so they are not real.
"""
import glob
import os
import sys

SCAN_NAME = "1850-evangelietroen-theologien.pdf"


def scan_path() -> str:
    """Locate the KB scan. Several /sessions/<id>/ dirs may exist and only the
    current one is readable, so test readability rather than taking the first."""
    if os.environ.get("SCAN") and os.access(os.environ["SCAN"], os.R_OK):
        return os.environ["SCAN"]
    for p in glob.glob(f"/sessions/*/mnt/bibliotek/Nielsen, Rasmus/{SCAN_NAME}"):
        if os.access(p, os.R_OK):
            return p
    raise SystemExit(
        f"cannot find a readable {SCAN_NAME} under /sessions/*/mnt/bibliotek/ — "
        "is the bibliotek folder mounted in this session?")


def pdfpage(printed: int) -> int:
    if printed < 1 or printed > 174:
        raise ValueError(f"printed page {printed} is outside the body (1-174)")
    return printed + (13 if printed <= 83 else 15)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--scan":
        print(scan_path())
    else:
        for a in sys.argv[1:]:
            print(pdfpage(int(a)))
