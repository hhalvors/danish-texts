#!/usr/bin/env python3
"""
pagemap.py <printed_page> [...]   ->  PDF page number(s), one per line
pagemap.py --scan                 ->  absolute path of the working scan

THE SINGLE SOURCE OF TRUTH FOR THE PAGE OFFSET.

    printed  3-123  ->  PDF = printed + 2   (PDF 5-125)

Høffding, Erkendelsesteori og Livsopfattelse (Det Kgl. Danske Vidensk.
Selskab, Filosofiske Meddelelser II, 1; København 1925). Verified 2026-09-30
from the running-head numeral of every page PDF 6-125: all carry printed =
PDF - 2 except PDF 23 (p. 21, opens ch. II, no head) and PDF 117 (p. 115,
numeral garbled in the layer). PDF 5 = p. 3 opens ch. I, no head.

Unpaginated matter: PDF 1 series half-title, PDF 2 series notice,
PDF 3 title leaf, PDF 4 blank, PDF 126 blank/back.
Body = pp. 3-122 (seven chapters, 36 numbered divisions running straight
through). p. 123 = INDHOLD, with the imprint lines "Forelagt paa Mødet den
16 Oktober 1925. Færdig fra Trykkeriet den 7. November 1925."

SCAN: Royal Danish Academy digitisation, ABBYY FineReader Server, 126 pp.,
400 ppi colour, antiqua layer with italics tagged.
sha256 33b0373f56088186677a8295a73467bf542d5c5f3f49c7ef414f2cf059baad4a
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

FIRST_PRINTED, LAST_PRINTED = 3, 123
OFFSET = 2
REL = os.path.join("bibliotek", "Høffding, Harald", "erkendelsesteorie-livsopfattelse.pdf")


def scan_path() -> str:
    cands = [os.environ.get("SCAN", ""),
             os.path.join(HERE, "scan.pdf"),
             os.path.join(os.path.expanduser("~"), REL),          # macOS
             os.path.join(os.path.expanduser("~"), "mnt", REL)]   # Cowork VM
    for p in cands:
        if p and os.access(p, os.R_OK):
            return p
    raise SystemExit("cannot find the scan: expected ~/" + REL)


def pdfpage(printed: int) -> int:
    if printed < FIRST_PRINTED or printed > LAST_PRINTED:
        raise ValueError(f"printed page {printed} is outside {FIRST_PRINTED}-{LAST_PRINTED}")
    return printed + OFFSET


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--scan":
        print(scan_path())
    else:
        for a in sys.argv[1:]:
            print(pdfpage(int(a)))
