# Høffding — Den menneskelige Tanke, dens Former og dens Opgaver (1910): transcription resume notes

Source of truth: scan.pdf (Gyldendal/Nordisk Forlag, København og Kristiania, 1910).
This is a **transcription** job (no OCR transcription existed); build `transcription.tex`
(Danish) from the scan, then translate later per ../../../TRANSLATION-PLAYBOOK.md.

Page-offset: **PDF = printed + 15** (printed p.1 = PDF p.16; verified vs the p.373 running header).
Scan: ~/bibliotek/Høffding, Harald/den-menneskelige-tanke.pdf → copied to scan.pdf here.
Total: 392 printed pp. / 413 PDF pp.

## Typography / OCR notes
- Roman/antiqua type (NOT Fraktur). The scan carries a usable **embedded OCR text layer**
  (`pdftotext -f P -l P scan.pdf -`); use it as the base, then verify each page against a
  rendered image for the things the text layer drops.
- **Emphasis = true italics** in print (e.g. *søge efter*, *tænke paa*) → `\emph{}`.
- **Cited author names are letterspaced** (Locke, Hume, Mill, William James, Henri Bergson,
  Hamann, Herder, Jacobi, Kant) = emphasis → `\emph{}`. Genitive: `\emph{Hamann}’s`.
  (Usually only the FIRST mention is letterspaced; later mentions are roman.)
- **Foreign inline phrases are set ROMAN**, not italic (e.g. "(continuous transitions)",
  "(durée hétérogène et indistincte; durée dont les moments se pénètrent)",
  "en continuité mouvante, en unité de direction"). Do NOT italicize these.
  Work TITLES in footnotes ARE italic (*The Stream of Thought*, *Principles of Psychology*,
  *Introduction à la Métaphysique*); journal names roman (Mind, Revue de Métaphysique…).
- Quotes: „…“ (low-high). The text layer renders the closing “ as `44` — fix it.
- Common text-layer slips seen: horm→Form, lJ vilkaarligt→Uvilkaarligt, Bes1utning→Beslutning,
  Yirkemaade→Virkemaade, dropped/again-joined words. Always image-verify.

## Orthography (preserve 1910 spelling exactly)
aa (not å); capitalized nouns; **Ti / ti** for "thi" (for/because); **idethele** as one word;
modern **gennem** (not gjennem); **skønt** (not skjønt); but **Skjul**, **afgjørende** keep j;
Existens, Villie, exakt/experimental (x), f.\ Ex., o.\ s.\ v., d.\ v.\ s.

## Structure (from Indhold, PDF pp. 12–13) — printed-page starts
- I. Tankens Psykologi (Funktioner) — p.1 ; A. Psykisk Energi p.1, B. Anskuen… p.37,
  C. Dømmen p.71 (TOC misprints "154" for C; subparts a–d at 71/74/82/99)
- II. Tankens Historie — p.109 ; A. Animisme… p.109, B. Antik og moderne Tænkning p.123
- III. Tankens Former (Kategorier) — p.135 ; A p.135, B p.154, C p.175 (a–d), D p.207, E p.237
- IV. Tankens Opgaver (Problemer) — p.246 ; A. Erkendelsen p.254, B. Verdensanskuelse p.306,
  C. Vurdering p.347 (a. etiske p.350, b. religiøse p.369)
Book ends p.392.

## CURRENT RESUME POINT
Next marker: `% [text to be added: pp. 11--20]` — Part I.A "Psykisk Energi" continues.
Body breaks mid-word at p.10 ("udspringer for der-") → next page starts "efter…"; join the seam.

## DONE so far (don't redo)
- Preamble, title page, Forord (Aug 1910), Part I + §A heading, printed pp. 1–10
  (§§1–4 of A. Psykisk Energi). Footnotes: p.6 Psykologi ref; p.8 James & Bergson; p.10 student quote.

## Conventions
See ../../../TRANSLATION-PLAYBOOK.md plus the book-specific notes above.
