# Poul Martin Møller — *Strøtanker* (1843): translation resume notes

**Translation-only project.** A published e-book edition exists, so — per repo
rule — we do **NOT** produce or publish a Danish transcription. There is no
`transcription.tex`; translate directly from the e-book. Deliverable is
`translation.tex` only.

Source (private, gitignored): `Stroetanker.epub` — Lindhardt og Ringhof, 2018
(ISBN 9788726030204), which reprints the *Efterladte Skrifter*, bd. 3
(ed. F.C. Olsen, C.A. Reitzel, 1843) text and **preserves the original
orthography** (aa-spellings, capitalised nouns, etc.).

Reading the Danish while translating: unzip the epub to a scratch dir
(`unzip Stroetanker.epub -d /tmp/epub`); the text is in
`/tmp/epub/EPUB/xhtml/chapter_0NN.xhtml`, one file per chapter, aphorisms as
`<p class="in">` separated by `<hr class="emptyline">`. Do this in the sandbox
only — never commit extracted Danish.

Page-offset: none. The `\opage{N}` marginal notes in `translation.tex` are the
printed page numbers of the 2018 e-book (pp. 15–57); there is no separate scan.

## Structure
The book is 12 thematically-grouped chapters of *strøtanker* (aphorisms / short
paragraphs), each rendered as a `\section*`. Individual aphorisms within a
chapter are separated by `\aphsep` (a centred asterisk) — 171 separators total,
mirroring the epub's `<hr class="emptyline">`; keep the same count and order.
`translation.tex` has 12 sections, each with a `% [text to be added: pp. X--Y]`
marker and the Danish title in a comment. `\opage{N}` and `\aphsep` are already
defined in its preamble.

| # | Chapter | pp. |
|---|---------|-----|
| 1 | Stray Thoughts on Stray Thoughts / *Strøtanker om strøtanker* | 15–16 |
| 2 | On Philosophy and Philosophers / *Om filosofi og filosoffer* | 17–24 |
| 3 | Science and the Knowledge of Nature / *Videnskab og naturerkendelse* | 25–27 |
| 4 | Existentialism / *Eksistentialisme* | 28–31 |
| 5 | Religion, Christianity, and Morality / *Religion, kristendom og moral* | 32–36 |
| 6 | Aesthetic Investigations / *Æstetiske undersøgelser* | 37–40 |
| 7 | Affectation and Conversation / *Affektation og conversation* | 41–42 |
| 8 | Formalism and Stylists / *Formalisme og stylistikere* | 43 |
| 9 | The Problem of "Immortality" / *Problemet »Udødelighed«* | 44–48 |
| 10 | Depth Psychology / *Dybdepsykologi* | 49–51 |
| 11 | Politics and Pedagogy / *Politik og pædagogik* | 52–54 |
| 12 | Ahasuerus Stray Thoughts / *Ahasverus-Strøtanker* | 55–57 |

## CURRENT RESUME POINT
Nothing translated yet. Next marker: **ch. 1, pp. 15--16** (a short chapter — a
good place to lock in aphsep/quote/emph conventions before the longer chapters).
Chapters 2 and 9 are the longest; the rest are short.

## DONE so far (don't redo)
- Folder set up; epub moved in (gitignored); translation.tex skeleton + this
  file created and compile-verified (0/0). No English written yet.

## Book-specific notes for the translator
- **Aphorism form.** Most content is discrete one-paragraph aphorisms separated
  by `\aphsep`. Keep the same count and order; don't merge or re-break them.
- **Italic foreign phrases** (italic in the e-book): `conscientia`,
  `aktuel` (ch. 2), `chaos infusorium` (ch. 3), `summum bonum` (ch. 4),
  `tempus edax rerum` (ch. 11). Render these as `\textit{}` (Latin) in English.
- **Small caps.** Ch. 12 opens one aphorism with `\textsc{Prognostikon}:` —
  keep the small-caps run-in head.
- **Letterspacing → emphasis.** Ch. 10 has `\emph{bona} fide` (the print
  letterspaced "bona"); keep the emphasis.
- **Centred parenthetical.** Ch. 4 has `\begin{center}(og/eller dialektisk
  Realisme).\end{center}` — reproduce as a centred line.
- **Italic note.** Ch. 5 ends an item with an italic `Anm.` (note): translate as
  an italic "Note. …".
- **Greek variant-symbol gotcha.** The epub's OCR Greek used presentation-variant
  code points — kappa-symbol `ϰ` (U+03F0) and theta-symbol `ϑ` (U+03D1) — which
  `greek-fontenc`/`textalpha` cannot set in 8-bit pdfLaTeX ("character kappa symbol
  not available"). These were normalised to the canonical letters `κ`/`θ` (and one
  stray Latin `ó` → Greek `ό`) so the real local build compiles. NOTE: the sandbox
  compile recipe strips `textalpha` and masks Greek as `[Gr]`, so it will NOT catch
  this class of error — check any Greek against the variant code points by hand.
- **Greek.** Ch. 1's tripartite tag `πγευματἱχη, ψυχ, κη, σωματικη` is garbled in
  the epub (intended: πνευματική, ψυχική, σωματική = "spiritual, psychic,
  bodily"). Garbled in the e-book; when translating, gloss it and consider
  checking the 1843 print. Ch. 5 has `αληϑεια` (truth) in the e-book with a
  stray Cyrillic 'а' for the final alpha — set it as Greek alpha if carried over.
- **Guillemets** »…« in the Danish (quoted speech, esp. the long dialogue in
  ch. 9 "Problemet »Udødelighed«") → English curly doubles ``…'' per playbook.

## Conventions
See `../../../TRANSLATION-PLAYBOOK.md` (the standing method). Work ~10-page
batches; compile with the sandbox recipe (substitute `libertinus`→`lmodern`,
strip `textalpha`, and for the sandbox check replace Greek **and** any stray
Cyrillic — regex range `[Ͱ-Ͽἀ-῿Ѐ-ӿ]`). Expect 0 errors / 0 char-warnings.
The user commits and pushes — never Claude.
