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
Next marker: `% [text to be added: pp. 81--90]` — Part I.C.b "Hindringer for Domsdannelse"
continues (after §28). Body breaks mid-word at p.80 ("…bestemt og positivt karakteri-") →
p.81 (PDF 96) continues "seret…"; join the seam.
Math set in math mode ($x^2=x$, $A_x$/$B_x$); the AB-combinatorics letters (A, AB, AX, B, X)
and the algebraic A,B set ROMAN in text. Edition markers as superscript (Vernunft$^2$,
Logik\textsuperscript{1}). §-numbers run continuously: p.71 is §24 (OCR misreads as 21).
Notes: footnote-cited author names ARE letterspaced too (Wundt, Ramon y Cajal, Herrlin, p.27).
Emphasis can be ordinary contrast words too (e.g. *slutte*/*udlede* p.31; *hvem/har/udøver*
p.34). Latin set ROMAN when the print sets it roman (e.g. "qvalitas occulta" p.33) — match the
page, do not auto-italicize Latin. "Ramon y Cajal" printed without accent → keep as printed.
Section B added at p.37 ("B. Anskuen, Association og Sammenligning" → "a. Sansning").

Refined name rule (important): author names are letterspaced ONLY when the figure is the
key subject under discussion — NOT every mention. Verify each by zoom. Examples seen:
emphasized = Locke/Hume/Mill, William James, Henri Bergson, Hamann/Herder/Jacobi, Kant
(p.8); Hume, Kant (p.15); Fries, Henri Bergson (p.16); Stumpf (p.18); Sir William Ramsay,
Ernst Mach (p.19); Pawlow (p.20). NOT emphasized (roman) = Platon/Aristoteles/Plotinos/
Leibniz, "Lockes Forudsætning" (p.15); "John Locke" (p.12); 2nd mentions of Fries/Bergson/
Stumpf. For "J. F. Fries" only the surname is letterspaced → `J.\ F. \emph{Fries}`.
Emphasis is also true italics for ordinary words (e.g. *hvilken* … *hvilken*, p.17).

## DONE so far (don't redo)
- Preamble, title page, Forord (Aug 1910), printed pp. 1–60. Part I.A "Psykisk Energi"
  (§§1–10) COMPLETE; Part I.B "Anskuen, Association og Sammenligning": a. Sansning,
  b. Genkendelse (§§14–16) COMPLETE, c. Erindrings- og Fantasianskuelse (§§17–18) COMPLETE,
  d. Forestillingsassociation (§§19–20), e. Sammenligning (§§21–23) — Part I.B COMPLETE.
  Part I.C "Dømmen": a. Domsdannelse (§§24–25), b. Hindringer for Domsdannelse (§§26–28)
  begun, through p.80. Footnotes added batch 8: p.73 Jevons; p.77 Kant (Vernunft) + Hegel
  (Wissenschaft der Logik); p.78 Sigwart/Lotze/Bergson/Diog.Laërt + Hermann Cohen; p.79
  Moderne Filosofer; p.80 Kr. Nyrop. Earlier footnotes pp.6–69 as listed above.

## Conventions
See ../../../TRANSLATION-PLAYBOOK.md plus the book-specific notes above.
