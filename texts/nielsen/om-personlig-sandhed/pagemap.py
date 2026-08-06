#!/usr/bin/env python3
"""
pagemap.py <printed_page> [...]   ->  PDF page number(s), one per line

THE SINGLE SOURCE OF TRUTH FOR THE PAGE OFFSET. ocr.sh, spacing.py, twoup.sh and
splice.py's callers all go through this; do not hard-code +9 anywhere.

Book: R. Nielsen, "Om personlig Sandhed og sand Personlighed" (Gyldendal, 1854).
Scan: KB, 157 PDF pages, PyPDF2-produced. KB metadata gives the physical extent
as "[1], 144 s." — one unnumbered leaf (the Forord) plus 144 numbered body pages.

OFFSET (VERIFIED, UNIFORM — no jump anywhere in the book):

    printed   1-144   ->  PDF = printed + 9      (PDF  10-153)

Verified by reading the printed numeral off the image (not the embedded text
layer — see below) at both endpoints and at every lecture's own opening page:

    printed p.1   (PDF  10) = "I. Indledning: en Phantasie."      [chapter head, no folio]
    printed p.12  (PDF  21) = "II. Æsthetisk og religiøs Phantasie..." (folio "12" at top)
    printed p.33  (PDF  42) = "IV. Personlig Hjælp."               (folio "33" at top)
    printed p.55  (PDF  64) = "VI. Store Mænd: personlig Overlegenhed." (folio "55" at top)
    printed p.93  (PDF 102) = "IX. Skyld i Skrøbelighed."          (folio "93" at top)
    printed p.132 (PDF 141) = "XII. Personlig Stræben: en Slutning." (folio "132" at top)
    printed p.144 (PDF 153) = last page of the book (ends mid-testimony, no Indhold follows)

No offset change anywhere in this range — unlike evangelietroen-theologien, where a
double-scanned leaf shifted the offset by +2 partway through. This scan has no such
duplicate; PDF 154 is blank, PDF 155-156 are pastedowns/endpapers, PDF 157 is the
back cover.

FRONT MATTER (all unnumbered — no roman-numeral folios anywhere in this scan):
    PDF 1-5   = KB scan-metadata / barcode leaves (not part of the book)
    PDF 6     = title page ("Om personlig Sandhed og sand Personlighed.")
    PDF 7     = blank verso
    PDF 8     = Forord (ONE page, unfoliated, signed "Kjøbenhavn, d. 1. Mai 1854. / R. Nielsen.")
    PDF 9     = blank verso
    PDF 10    = printed p. 1 (body begins)

The Forord carries no printed folio at all (unlike evangelietroen's Forord, which is
paginated III-VIII). See RESUME-NOTES.md and transcription.tex for how this is keyed:
the batch marker uses the synthetic pair "0--0" (plain arabic, never printed, chosen so
it cannot collide with any real printed page number) and the in-text page marker for
that fragment is the non-digit `% --- p. [Forord] ---`, which check.py's page-marker
regex (arabic-only) ignores by design — the same mechanism evangelietroen relies on to
ignore its roman-numeral Forord markers.

NO INDHOLD: this scan has no table of contents anywhere, front or back (PDF 154 is
blank and PDF 155-157 are binding/cover). Unlike evangelietroen, there is nothing to
cross-check the lecture heads against; the titles and page ranges here were read
directly off each lecture's own opening page image.

TEXT LAYER WARNING: the embedded (PyPDF2/KB) text layer is a garbled OCR, not a clean
witness — systematic æ/ø corruption throughout (e.g. "Msthetisk" for "Æsthetisk",
"Sporgsmaal" for "Spørgsmaal", "vcrre" for "være", "cr" for "æ", "o" for "ø"). Treat it
as a rough structure-finder only, never as a source for transcribed text; every printed
numeral and every word must be verified against the page image, exactly as the
playbook requires for any OCR'd Fraktur book.
"""
import glob
import os
import sys

SCAN_NAME = "om-personlig-sandhed.pdf"

FORORD_PDF = 8  # unfoliated single leaf; see docstring above


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
    if printed < 1 or printed > 144:
        raise ValueError(f"printed page {printed} is outside the body (1-144)")
    return printed + 9


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--scan":
        print(scan_path())
    elif len(sys.argv) > 1 and sys.argv[1] == "--forord":
        print(FORORD_PDF)
    else:
        for a in sys.argv[1:]:
            print(pdfpage(int(a)))
