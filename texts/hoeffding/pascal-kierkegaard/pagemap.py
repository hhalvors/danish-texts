#!/usr/bin/env python3
"""
pagemap.py <printed_page> [...]   ->  PDF page number(s), one per line
pagemap.py --scan                 ->  path to the source scan

THE SINGLE SOURCE OF TRUTH FOR THE PAGE OFFSET. ocr.sh and every batch agent
call this; do not hard-code an offset anywhere else.

Source: Internet Archive item `revue-de-metaphysique-et-de-morale-30-2`
        (Revue de Métaphysique et de Morale 30:2, avril--juin 1923 — the
        Pascal tercentenary number). Public Domain Mark 1.0.
        The whole issue is one PDF; Høffding's article is printed pp. 221--246.

    printed 221--246  ->  PDF = printed + 18   (PDF 239--264)

VERIFIED 2026-08-06 by OCR of the running-head line of every PDF page from 232
to 268. The heads are unambiguous: even pages carry "N REVUE DE METAPHYSIQUE ET
DE MORALE", odd pages "H. HOFFDING. — PASCAL ET KIERKEGAARD. N".

Both endpoints check out:
  PDF 239 = printed 221 — the article's opening page (title block, no running
            head, hence no numeral to read; bracketed by PDF 238 = printed 220,
            the last page of the preceding Filleau de la Chaise article, and
            PDF 240 = printed 222).
  PDF 264 = printed 246 — head reads "246 REVUE DE METAPHYSIQUE ET DE MORALE".
            PDF 265 = printed 247 opens J. Laporte, "Pascal et la doctrine de
            Port-Royal" (confirmed by its running head at PDF 267 = 249).

The offset is NOT uniform across the whole issue — PDF 100 = printed 98, i.e.
+2 — so it changes somewhere between PDF 100 and PDF 232. That does not matter
for this article, but do not reuse this offset for any other piece in the issue
without re-verifying it.

Apparent one-page jumps in the OCR of the heads (PDF 236 read "248" for 218,
PDF 243 "228" for 225, PDF 249 "934" for 231, PDF 259 "244" for 241) are
misreadings of the numeral: the surrounding pages revert, so they are not real.
"""
import glob
import os
import sys

FIRST_PRINTED = 221
LAST_PRINTED = 246

# PDF page = printed page + OFFSET.  Verified — see the module docstring.
OFFSET = 18


def scan_path() -> str:
    """Locate the scan. Several /sessions/<id>/ dirs may exist and only the
    current one is readable, so test readability rather than taking the first."""
    if os.environ.get("SCAN") and os.access(os.environ["SCAN"], os.R_OK):
        return os.environ["SCAN"]
    here = os.path.dirname(os.path.abspath(__file__))
    local = os.path.join(here, "scan.pdf")
    if os.access(local, os.R_OK):
        return local
    for pat in ("/sessions/*/mnt/bibliotek/Høffding, Harald/*pascal*.pdf",
                "/sessions/*/mnt/bibliotek/Hoffding, Harald/*pascal*.pdf",
                "/sessions/*/mnt/danish-texts/texts/hoeffding/pascal-kierkegaard/scan.pdf"):
        for p in glob.glob(pat):
            if os.access(p, os.R_OK):
                return p
    raise SystemExit(
        "cannot find the scan. Put the Internet Archive PDF at\n"
        f"  {local}\n"
        "(it is gitignored — source scans are never committed), or set $SCAN.")


def pdfpage(printed: int) -> int:
    if printed < FIRST_PRINTED or printed > LAST_PRINTED:
        raise ValueError(
            f"printed page {printed} is outside the article "
            f"({FIRST_PRINTED}--{LAST_PRINTED})")
    return printed + OFFSET


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--scan":
        print(scan_path())
    else:
        for a in sys.argv[1:]:
            print(pdfpage(int(a)))
