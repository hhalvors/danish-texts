#!/usr/bin/env python3
"""pagemap.py -- Høffding, "Kort Oversigt over den nyere Filosofis Historie", FJERDE, PAANY OMARBEJDEDE UDGAVE
(Kjøbenhavn og Kristiania: Gyldendalske Boghandel, Nordisk Forlag; Forlagets Bogtrykkeri, 1910; 95 pp.; the Fortale til
fjerde Udgave dated 28 March 1910).
Scan: ~/bibliotek/Høffding, Harald/1910-kort-oversigt-4udg.pdf (SCANS.tsv) -- the National Library of Norway's scan (nb.no
item 17246e2b574fbd978af6a80c866e4e4b = URN:NBN:no-nb_digibok_2010102906103), 109 colour page images at 400 dpi, bound with
NB's own OCR (ALTO) as text layer by nb_scan.py; the ALTO is kept beside the scan (1910-kort-oversigt-4udg-alto.tar.gz).
PDF = printed + 10 (ALTO folios of pp. 2-95):  PDF 3 half-title, 5 title, 7 Indhold, 9 Fortale til fjerde Udgave (static
in template.tex), 11-105 text pp. 1-95.
Running head: folio and the chapter title (verso) or the section title (recto), one line.  Sheet signatures
"Høffding: Kort Oversigt. 4. Udg. N" and "N*" at the foot (dropped).
Method (2026-10-17, HOEFFDING-QUEUE #10): religioese-tanketyper's -- draft from NB's layer, tesseract witness (ocr.py); the
SAGA e-book (ISBN 9788726363074) is a LATER edition (>= 1920: Wundt's death year; the Tillæg "Vurderingsprincipets
Historie", verb plurals modernised), so it votes only where it agrees with one reading word for word; Runeberg's kortfil is
an unproofread OCR of the same NB images (not used)."""
import os
AUTHOR = 'hoeffding'
FIRST_PRINTED, LAST_PRINTED, OFFSET = 1, 95, 10
SKIP = set()
# the title (p. 3) and Indhold (p. 5) are static in template.tex
FRONT = {}
REL = os.path.join("bibliotek", "Høffding, Harald", "1910-kort-oversigt-4udg.pdf")
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
BOOKDIR = os.path.join(ROOT, 'texts', AUTHOR, 'kort-oversigt')
EBOOK = os.path.join(BOOKDIR, 'Kort_oversigt_over_den_nyere_filosofis_historie.epub')  # privately owned, gitignored: never committed or published
WITNESS = 'ocr'
ITALCMD = 'textit'          # italics \textit; \emph is the print's letterspacing (house convention)
ITAL = 1.03                 # slant threshold: to be calibrated on this book
JUNK = r'Nasjonalbiblioteket|Depotbiblioteket|VENNLIGST'
def scan_path():
    for p in [os.environ.get("SCAN", ""), os.path.join(os.path.expanduser("~"), REL), os.path.join(os.path.expanduser("~"), "mnt", REL)]:
        if p and os.access(p, os.R_OK): return p
    raise SystemExit("cannot find the scan: ~/" + REL)
def pdfpage(n):
    if n in FRONT: return FRONT[n]
    if not FIRST_PRINTED <= n <= LAST_PRINTED: raise ValueError(n)
    return n + OFFSET
DRAFT_PAGES = [p for p in range(FIRST_PRINTED, LAST_PRINTED + 1) if p not in SKIP]
PAGES = DRAFT_PAGES
# check.py: the running head is folio + short title; the signature "Harald Høffding N" and "N*" at a sheet's foot
HEAD = r'^\W*([\d\s]{1,5}\W*)?([IVXLl1]{1,4}\.?\s*)?([\da-d]\.\s*)?(Indledning|Filosofiske|Den nyere|Opdagelsen|Det nye|Den nye|Systemdannelser|R[ée]n[ée]|Thomas|Baruch|G\. W\.|Erfaringsfilosofien|John|George|David|Oplysningsfilosof\S*|i Frankrig|Immanuel|Kants|Romantikens|Fichte|Schopenhauer|Feuerbach|Positivismen|Auguste|Darwin|Nyere Probl\S*|Det psykologiske|Tilværelses\S*|Erkendelses\S*|Vurderings\S*|Till\S*g)\b.{0,55}?(\s+\d{1,3}\W*)?$|^[\dIlOoSs\s.,*\'!]{1,6}$'
FOOT = r'^\W*H\S{3,9}\W*Kort\W*Oversigt\W.{0,15}$|^[\dil]{1,2}\s?[*«»]$'
SPACING = 'strict'
QUOTES = 'strict'
WMARKS = True
INDENT_MAX = 3.6
TEXFILE = 'transcription.tex'
WHITE_GAP = 1.9
_IB = None
def italic_boxes(p):
    """boxes (x0, y0, x1, y1, pt from the top left) of the words NB's OCR read as italic on printed page p (nb_scan.py italics)"""
    global _IB
    if _IB is None:
        _IB = {}
        for l in open(os.path.join(HERE, 'italics.tsv'), encoding='utf-8'):
            if l[:1].isdigit():
                f = l.split('\t'); _IB.setdefault(int(f[0]), []).append(tuple(map(float, f[1:5])))
    return _IB.get(pdfpage(p), [])
IMGDIR = os.environ.get('KORT_IMG', '/tmp/kort/img')   # nb_scan.py fetch: the page images (400 dpi), for the slant test
def page_image(p):
    f = os.path.join(IMGDIR, f'{pdfpage(p):04d}.jpg')
    if not os.path.exists(f): raise SystemExit(f'no page image {f}: run nb_scan.py fetch {ITEM} /tmp/kort (or set KORT_IMG)')
    return f, 400
ITEM = '17246e2b574fbd978af6a80c866e4e4b'
NOTE_SPACE = True           # check.py: a space after each footnote moved to the page's foot (no glued seams)
