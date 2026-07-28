# RESUME-NOTES — Sibbern, *Udaf Gabrielis' Breve til og fra Hjemmet* (5th ed., 1893)

State for the **transcription** of this book. Update after each batch.
The user compiles/commits/pushes — never the assistant.

Source of truth: `transcription.tex` (Danish), ▢ in progress (scaffold only).
See `../../../TRANSLATION-PLAYBOOK.md` for the standing method (the translation
job comes later, from the finished transcription).

## Edition & source

- Scan: `~/bibliotek/Sibbern, Frederik/Udaf_Gabrielis_breve_til_og_fra_hjemmet.pdf`
  (Google Books, **Harvard College Library / Widener copy**, **364 PDF pages**,
  has a roman-type OCR text layer — decent draft quality; verify every page
  against the image).
- **Edition:** *Udaf Gabrielis' Breve til og fra Hjemmet. Samlet og udgivet af
  Frederik Christian Sibbern. Med et Forord af Prof. Harald Høffding. Femte
  Udgave.* Kjøbenhavn: Det Reitzelske Forlag (George C. Grøn); Fr. Bagges
  Bogtrykkeri, 1893.
- **Typography:** roman/antiqua throughout (**NOT Fraktur** — unlike
  *Erkjendelse*). Høffding's Forord is set largely in *italic*; Sibbern's
  Tilegnelse and the body of letters are in upright roman.
- **Work identity (important — reconcile with catalog.yaml):** this is the
  mature, collected form of Sibbern's Gabrielis epistolary novel. The novel
  first appeared 1826 as *Efterladte Breve af Gabrielis*; Sibbern later planned
  companion collections "til Hjemmet" / "fra Hjemmet" (see his Tilegnelse). The
  catalog's bibliography currently lists **1826 "Efterladte Breve af Gabrielis"**
  and **1850 "Ud af Gabrielis's Breve til og fra Hjemmet"** as separate items;
  neither is (yet) a curated `works` entry. This scan is the **1893 5th ed.** of
  the latter. Decide with Hans whether these bibliography lines should
  `incollection:`-link to the new `gabrielis` work.

## Page map (important)

Roman/antiqua, three paginated regions with **three different offsets** because
the front matter has two independent roman sequences plus title/blank leaves:

- **Title leaves:** half-title PDF 7; **full title page PDF 9** (transcribed in
  the `\title` block).
- **Høffding's Forord** (roman num., its own sequence): `printed = PDF − 10`
  (p.III = PDF 13; p.XXX = PDF 40; ends ~p.XXXVII ~PDF 47; blank verso PDF 48).
- **Sibbern's Tilegnelse to Bishop Mynster** (roman num., a *separate* sequence):
  `printed = PDF − 46` (dedication half-title PDF 49, blank verso PDF 50,
  text p.V = PDF 51 … p.VIII = PDF 54). NB the two roman sequences overlap in
  numbering — they are independent; go by the offsets, not the numerals.
- **Body / the letters** (arabic): `printed = PDF − 54` (p.1 = PDF 55).
  Body ends ~**p.302** (PDF ~356). PDF 357–364 are Harvard library slips/blanks.
- **No table of contents (Indhold)** in the volume.

| Section | Printed pp. | PDF pp. | Status |
|---|---|---|---|
| Half-title | — | 7 | (not transcribed) |
| Title page | — | 9 | **done** (in title block) |
| Forord (Høffding) | III–~XXXVII | 13–~47 | **NOT started** (~35 pp italic) |
| Tilegnelse (to Mynster) | V–VIII | 51–54 | **done** (image-verified) |
| Body — the letters | 1–~302 | 55–~356 | pp. **1–10 done**; 11+ NOT started |

## Structure of the body

Epistolary novel: a sequence of **dated letters** (first letter opens
"Fredag den 21de Mai 1824. Aften."). Per Sibbern's Tilegnelse the material is
conceived as letters "til Hjemmet" and "fra Hjemmet"; watch for internal part
divisions and a possible second/third *Del* as the letters proceed (Høffding's
Forord refers to "første Del" and "anden Del" of the Breve). Map the
letter/part headings against the images during the first body batch.

## CURRENT RESUME POINT
**Next: Body p.11 (PDF 65) onward**, continuing the first letter ("Fredag den
21de Mai 1824. Aften."), which is still running at the end of p.10
("…og saadan gaaer" → continues p.11). Work in ~10-page batches. Watch for the
first letter's end and the next dated letter-heading, and for any part divider
("til Hjemmet" / "fra Hjemmet"). The `% [Brev fortsætter …]` comment at the end
of the body marks the exact seam.

Still outstanding elsewhere: **Høffding's Forord, pp. III–XXXVII** (PDF 13–47,
~35 pp italic) — not started; can be done anytime.

## DONE so far (don't redo)
- **Scaffold** — preamble (house style: book / libertinus / textalpha / danish
  babel), image-verified **1893 title page**, and Sibbern's **Tilegnelse** to
  Bishop Mynster (pp. V–VIII, dated 1850 + a July-1870 note).
- **Body pp. 1–10 (PDF 55–64)** — the opening of the first letter, verbatim and
  image-verified. Sandbox compile (font-substitute recipe): **11 pp., 0
  char-warnings, 0 errors.** Page seams marked with `% [printed p.N / PDF M]`
  comments.

## Transcription conventions
- LaTeX `book` class, libertinus (matches the repo's other transcriptions).
- **Preserve 1890s-reprint-of-1820s orthography verbatim:** aa (not å), kj/gj
  (Kjøbenhavn, Gjerninger, Gjenfødelse), ei (Veie, høi), doubled vowels
  (Vande, Haab, see, Glæde), maaskee, Qvægelse, capitalised nouns, etc. Do NOT
  modernise.
- **Danish quotes:** low-high `„ … “` (U+201E opening, U+201C closing) — matches
  the house style used in `om-elskov`.
- Em-dash `---`; printed ornamental rules → `\begin{center}\rule{0.28\linewidth}{0.4pt}\end{center}`.
- No `\emph`/italics in the transcription body (house practice). Exception noted:
  Høffding's Forord is *printed* in italic — decide whether to reproduce that as
  `\itshape` or set it upright like the rest when it is transcribed.

## Spot-checks / flags from the scaffold batch (verify against scan when proofing)
- **Tilegnelse p.VI** "…i de offentlige Omtalers **Gebeet**…" — old spelling of
  *Gebet* (domain/sphere); kept verbatim.
- **Tilegnelse p.V** opens with a decorative drop-cap **J** ("Jeg"); rendered as
  ordinary text.
- Two dated signatures close the Tilegnelse: **"Den 4de Oktober 1850. Sibbern."**
  (the dedication proper) and a note to the 4th ed. **"Juli 1870. Sibbern."**
  on the Zodiakallys usage — both carried over.
- **Body p.5** "…som deres Mænd og Ungkarle." — the scan shows a stray dot after
  "og" ("og. Ungkarle"); read as a speck, transcribed "Mænd og Ungkarle."
- **Body pp.3, 8, 9** contain German quotations (Goethe's *Geheimnisse*; Moses
  Aaron's German-Jewish speech) — kept verbatim in „…“, incl. the printed Danish
  "høren" for *hören* (p.8) and "Schpricht der Herr" (p.7).
- Drop-cap initial "J" opening the first letter (p.1) rendered as ordinary text.
