# R. Nielsen, *Om personlig Sandhed og sand Personlighed* (1854) — resume notes

Twelve popular lectures ("for dannede Tilhørere af begge Kjøn", i.e. for an educated
mixed audience), delivered at the University in the winter of 1854. Gyldendalske
Boghandling (F. Hegel), 1854. [1] + 144 pp., Fraktur. Same author and genre as
*Evangelietroen og Theologien* (1850), which is the reference implementation for the
whole method used here (pagemap.py / ocr.sh / spacing.py / check.py / splice.py /
BATCH-AGENT.md) — see `../evangelietroen-theologien/` for the fully worked example.

**Status: SET-UP ONLY. No transcription has been done yet.** This is a fresh skeleton;
the next session should read `../../../TRANSCRIPTION-PLAYBOOK.md` and start batching
from printed p. 1.

## Files
- Scan: `bibliotek/Nielsen, Rasmus/om-personlig-sandhed.pdf` (157 PDF pp., 33.5 MB,
  PyPDF2-produced, KB digitisation). KB metadata: physical extent "[1], 144 s."
- Transcription: `transcription.tex` (skeleton only — 13 markers: Forord + 12 lectures,
  no body text yet). Translation: not begun (separate later job).
- Catalog entry: `catalog.yaml`, author `nielsen`, id `om-personlig-sandhed`.

## ✅ PAGE MAP — VERIFIED UNIFORM, no offset change anywhere

    printed   1--144   ->   PDF = printed + 9      (PDF  10--153)

**How this was verified** (read directly off the page image, never off the embedded
text layer — see the warning below): rendered PDF 1–12, 21, 41–44, 64, 102, 141,
148–157 at 150 dpi and read the printed numeral by eye at each of the following
checkpoints, spaced across the full 157-page scan:

| printed | PDF | what's on the page |
|---|---|---|
| — | 1–5 | KB scan-metadata / barcode leaves (not part of the book) |
| — | 6 | title page (unnumbered) |
| — | 7 | blank verso |
| — | 8 | **Forord** — ONE page, unfoliated, dated "Kjøbenhavn, d. 1. Mai 1854", signed "R. Nielsen." |
| — | 9 | blank verso |
| 1 | 10 | "I. Indledning: en Phantasie." (chapter-opening page; no folio printed on p.1 itself) |
| 12 | 21 | "II. Æsthetisk og religiøs Phantasie..." (folio "12" printed at top) |
| 33 | 42 | "IV. Personlig Hjælp." (folio "33" printed at top, directly above the heading) |
| 55 | 64 | "VI. Store Mænd: personlig Overlegenhed." (folio "55" at top) |
| 93 | 102 | "IX. Skyld i Skrøbelighed." (folio "93" at top) |
| 132 | 141 | "XII. Personlig Stræben: en Slutning." (folio "132" at top) |
| 144 | 153 | last page of the book — ends mid-argument ("...og til denne Indledning vende vi nu tilbage...", the Slutning's closing testimony); no Indhold follows |
| — | 154 | blank |
| — | 155–156 | pastedowns / endpapers |
| — | 157 | back cover |

No jump anywhere in this range — every chapter-opening page's own folio (read at the
checkpoints above) agrees exactly with 9-plus-printed. This is unlike
evangelietroen-theologien, where a double-scanned leaf shifted the offset by +2
partway through; nothing analogous happens here. **Confidence: high** — six
independent checkpoints across the full body, plus both endpoints, all agree with a
single constant offset.

### The Forord has NO printed folio at all
Unlike evangelietroen's Forord (paginated III–VIII in roman numerals), this book's
Forord is a **single unfoliated leaf** — no numeral anywhere on the page, front or
back. Since `splice.py`'s batch-marker filename convention requires two plain arabic
integers (`pp<FIRST>-<LAST>.texfrag`), and there is no real printed number to use, the
skeleton keys the Forord's batch marker as the **synthetic pair `0--0`**:

    % [text to be added: pp. 0--0]      ->  fragment file .parts/pp0-0.texfrag

`0` was chosen because it can never collide with a real printed page (the body starts
at 1) and is self-evidently synthetic. When that batch is eventually written, use the
**non-digit** in-text page marker `% --- p. [Forord] ---` rather than `% --- p. 0 ---`
— `check.py`'s page-gap regex is arabic-only (`\d+`) and will silently ignore a
non-digit marker, exactly the mechanism evangelietroen relies on to ignore its roman
Forord markers. Do NOT use `% --- p. 0 ---`: that WOULD be picked up by the regex and
would corrupt the gap/dupe report for the real body pages.

### No Indhold anywhere in this scan
Checked the back of the book (PDF 154–157) directly on the image: blank page, then
pastedowns/endpapers, then the back cover — no table of contents. The front matter
(PDF 1–9) has none either. **This book's scan simply has no Indhold to transcribe or
to cross-check the lecture heads against** — unlike evangelietroen, where the Indhold
at the back caught two genuine OCR errors and two genuine printer variants. Here, the
titles and page ranges baked into the skeleton were read directly off each lecture's
own opening-page image, with no second witness to check them against. Flag anything
that looks off rather than trusting these entries blindly on the first pass through
each lecture.

## ⚠ TEXT LAYER WARNING
The embedded (PyPDF2/KB) text layer in this PDF is a **garbled OCR**, not a clean
witness — do not trust it for anything beyond the roughest structure-finding (e.g.
locating where a roman-numeral heading falls). Examples of its systematic corruption,
seen while locating the lecture heads via `pdftotext -layout`:

- `Æsthetisk` → `Msthetisk`; `religiøs` → `religiös`
- `Spørgsmaal` → `Sporgsmaal`; `være` → `vcrre`; `Sjælen` → `Sjcelen`
- `personlig Sandhed` renders fine, but `sand Personlighed` on the title page came out
  as `sand Personsighed`
- general æ→"cr" and ø→"o" substitution throughout

The scan itself, by contrast, looks like a clean, crisp Fraktur print in good
condition — similar to evangelietroen's. **Expectation, not yet confirmed:** a fresh
Fraktur tesseract pass (`ocr.sh`) should do much better than this embedded layer, the
same way it did on evangelietroen. Confirm this on the very first transcription batch
before trusting the OCR-first pipeline; if the Fraktur model struggles here the way it
did on Religionsphilosophie, switch to an eyeball-first pipeline instead (see playbook
§2).

## Footnote convention
Surveyed for footnote marks while locating the chapter heads; found exactly **one**
occurrence in the whole book, on printed p. 49 (inside Lecture V, "Selskab i
Eensomhed"): `...den personlige Sandhed.*)` with the note beginning `*) At den
Tænker, der i vor Tid sigtede...`. Set `\thefootnote` to the constant `*)` in the
preamble, matching evangelietroen's convention (same publisher-era house style).
**This has only been confirmed on one page** — if later batches turn up footnotes
marked differently, stop and reconsider rather than silently forcing them into `*)`.

## Structure: the twelve lectures (from the images — no Indhold to cross-check against)

| # | Printed title (verbatim) | Printed pp. | PDF pp. |
|---|---|---|---|
| I | Indledning: en Phantasie. | 1–11 | 10–20 |
| II | Æsthetisk og religiøs Phantasie: en personlig Forskjel. | 12–22 | 21–31 |
| III | Det evige Liv: en personlig Trang. | 23–32 | 32–41 |
| IV | Personlig Hjælp. | 33–42 | 42–51 |
| V | Selskab i Eensomhed: en personlig Opgave. | 43–54 | 52–63 |
| VI | Store Mænd: personlig Overlegenhed. | 55–67 | 64–76 |
| VII | Ubetydelige Mennesker. | 68–79 | 77–88 |
| VIII | En Timelærer. | 80–92 | 89–101 |
| IX | Skyld i Skrøbelighed. | 93–104 | 102–113 |
| X | Den Stærke og den Skrøbelige: et personligt Mellemværende. | 105–117 | 114–126 |
| XI | Personlighedens Vilkaar. | 118–131 | 127–140 |
| XII | Personlig Stræben: en Slutning. | 132–144 | 141–153 |

Total: 144 printed pages, matching KB's "144 s." exactly. Each lecture is headed by a
bare roman numeral ("I.", "II." …) plus its printed title — **not** the ordinal-word
style ("Første Forelæsning") used in evangelietroen. Each opens directly with a
drop-cap paragraph; **no italic "argument" summary** under the heading (unlike
evangelietroen, which prints one both at the chapter head and in its Indhold — moot
here anyway, since there is no Indhold).

## Compile / skeleton check (done)
`python3 check.py` on the untouched skeleton reports:

    pages: no arabic % --- p. N --- markers yet
    progress: 0/144 = 0.0%   next page to transcribe: 1
    braces balanced: True (130 open / 130 close)
    markers remaining (text to be added): 13
    quotes: „=0 “=0  balance=0

13 markers = Forord (pp. 0--0) + 12 lectures. Sandbox compile test (libertinus →
lmodern, libertinust1math/textalpha stripped, babel stripped) succeeds: 29 pages,
0 `!`-errors.

## CURRENT RESUME POINT
**Nothing transcribed yet.** Next: dispatch a batch-agent for the Forord
(`% [text to be added: pp. 0--0]`, ~1 page) or start directly with Lecture I
(`% [text to be added: pp. 1--11]`), per `BATCH-AGENT.md`. Running quote-balance
total so far: **0** (nothing transcribed to unbalance it yet).

## Standing method
See `../../../TRANSCRIPTION-PLAYBOOK.md` for the batch-dispatch protocol, and
`../evangelietroen-theologien/RESUME-NOTES.md` for the fully worked example of the
same author, genre and era (including how its one real offset change was tracked, and
how its Indhold pass caught two printer variants — for contrast with this book, which
has no Indhold at all).
