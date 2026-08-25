# RESUME-NOTES — Høffding, « Pascal et Kierkegaard » (1923)

Written for a reader with no memory of the session, because that is who reads
it next.

## What this is

Harald Høffding, « Pascal et Kierkegaard », *Revue de Métaphysique et de
Morale*, 30e année, no 2 (avril–juin 1923), **pp. 221–246** (26 pp.).

The issue is the Pascal tercentenary number. **Høffding wrote this in French**
— it is not a translation from Danish, and the French is his own. Catalog entry
`pascal-kierkegaard` under `hoeffding` in `catalog.yaml`.

## STATUS — COMPLETE

**Transcription (French)** — 26/26 pages, 0 gaps, 0 dupes, braces balanced,
guillemets 45/45, compile clean (0 errors, 0 missing characters, 23 pages).

**Translation (English)** — all three markers filled, no `translation continues`
notes outstanding, compile clean (0/0, 23 pages). Structure mirrors the
transcription 1:1: 4 section heads, 2 footnotes, 26 page markers in each.

`catalog.yaml` is set to `status: complete` with Transcription, Translation,
archive.org and JSTOR links. **Not committed — the user commits.** The PDFs
still need a local build with the real fonts, then
`~/hhalvors.github.io/publish-danish.sh "message"`.

## Translation conventions specific to this piece

The source is FRENCH, so TRANSLATION-PLAYBOOK.md applies with one addition: a
title policy, fixed with the user and recorded in full in the `translation.tex`
preamble. In short:

- **Kierkegaard's works → standard English titles.** *Ou l'un ou l'autre* →
  *Either/Or*; *Étapes de la route humaine* → *Stages on Life's Way*;
  *Postscriptum définitif non scientifique* → *Concluding Unscientific
  Postscript*; *(L')Exercice dans le Christianisme* → *Practice in
  Christianity*; *(La) Maladie à la mort* → *The Sickness unto Death*;
  *Le Moment* → *The Moment*.
- **Pascal's works → standard English, except *Pensées***, which keeps its
  French name because that is its standard name in English. *Provinciales* →
  *The Provincial Letters*; *Mémoire sur le Vide* → *Memoir on the Vacuum*;
  *Comparaison des chrétiens…* → *Comparison Between the Christians of Early
  Times and Those of Today*.
- **French secondary literature stays French**: Sainte-Beuve's *Port-Royal*,
  Strowski's *Pascal et son temps*, Høffding's own *Philosophie de la religion*
  and *La Morale*, the *Revue*, the Brunschvicg *Œuvres*. Translating them
  would make the citations untraceable.
- **Latin stays Latin**: *De civitate Dei*, *Augustinus*, \textit{de plano}.
- The p. 232 footnote keeps Høffding's **Danish** citation exactly as the
  journal prints it, misprint included, so the two files agree.

Brunschvicg fragment numbers ("fr. 144 Br.") are carried over verbatim.

A verification script for the title policy is worth rerunning after any edit:
grep the body (comments stripped) for the French forms — all should be 0 —
and for the English forms, which should all be non-zero.

## Source

Internet Archive item **`revue-de-metaphysique-et-de-morale-30-2`**, Public
Domain Mark 1.0, 300 ppi. <https://archive.org/details/revue-de-metaphysique-et-de-morale-30-2>

Working copy is `scan.pdf` in this directory (gitignored — source scans are
never committed). It is the WHOLE 368-page issue, not just this article.

JSTOR has the article at <https://www.jstor.org/stable/40895941> — the citation
of record, not a usable source.

## Page map — VERIFIED, do not re-derive

    printed 221--246  ->  PDF = printed + 18   (PDF 239--264)

Verified by OCR of the running-head line of every PDF page from 232 to 268.
Both endpoints confirmed: PDF 239 = printed 221 (the opening page, which has a
title block and so no running head), PDF 264 = printed 246. PDF 265 = printed
247 opens J. Laporte, « Pascal et la doctrine de Port-Royal ».

**The offset is NOT uniform across the issue** — PDF 100 = printed 98, i.e. +2.
It changes somewhere between PDF 100 and PDF 232. Do not reuse +18 for any
other piece in this issue without re-verifying.

## Structure, as actually printed

- pp. 221–224 — unnumbered introduction. No byline, no standfirst, no epigraph,
  no title footnote; nothing on p. 221 announces the tercentenary. The author's
  name appears only in the running head.
- p. 225 — `I. — LEUR TEMPÉRAMENT ET LEUR CARACTÈRE.`
- p. 230 — `II. — PRÉDISPOSITIONS INTELLECTUELLES.`
- p. 235 — `III. — LE PROBLÈME CHRÉTIEN.`
- p. 242 — `IV. — PARTIS A PRENDRE.`
- p. 246 ends ranged-right `HARALD HÖFFDING.`, caps + small caps. No rule, no
  place-and-date line.

**Typographic datum, confirmed at 400 dpi on both heads:** the journal accents
É and È inside small-cap heads (`TEMPÉRAMENT`, `CARACTÈRE`) but drops the
accent on the preposition *à*, which is set `A` in `PARTIS A PRENDRE`. Both are
transcribed as printed. Do not "fix" the A.

Two footnotes in the whole article: one on p. 224, one on p. 232. The journal
sets a superscript arabic numeral followed by a baseline closing parenthesis in
the text, and small type with no rule at the foot.

## The pipeline used here, and why it is not the Fraktur one

This is French antiqua, not Danish Fraktur, so the book has its own scripts:

- `pagemap.py` — the page map. Everything calls it.
- `ocr.sh` — plain-text OCR for a range, `-l fra` with an `-l eng` fallback.
- `build_frag.py` — **the important one.** Builds a fragment straight from
  tesseract TSV. `--psm 6` throws away the indentation that marks paragraph
  starts, so paragraphing is recovered from *geometry*: a line whose left-x
  exceeds the page's median by 0.55 of the median line height is a paragraph
  start. The median (not the mode) is the right statistic — left edges jitter
  ±20 px from page skew, and the modal left was only 4 lines out of 39.
- `polish.py` — strips marginal specks, normalises apostrophes to ASCII (to
  match the other batches, which are ASCII throughout), and applies an explicit
  table of OCR corrections.
- `markup.py` — italics, section heads, footnote placement, printer's-defect
  comments. Everything OCR cannot see, as a literal find/replace table.
- `check.py`, `splice.py` — as in the playbook.

`TESSDATA_PREFIX` must point at a directory holding **both** `fra.traineddata`
and the system `configs/` directory. If `configs/` is missing, `tesseract ...
tsv` silently falls back to plain text output instead of erroring — that cost
an hour. The repo keeps the model in `.tessdata/` (gitignored):

    mkdir -p /tmp/tess && ln -sf /usr/share/tesseract-ocr/4.00/tessdata/*.traineddata /tmp/tess/
    ln -sfn /usr/share/tesseract-ocr/4.00/tessdata/configs /tmp/tess/configs
    ln -sf "$PWD/../../../.tessdata/fra.traineddata" /tmp/tess/

## !! The content-filter problem — read this before batching this article !!

**Subagents could not transcribe pp. 230–238.** Three dispatches (as 230–238
twice, then as 230–234) each died with `API Error: 400 Output blocked by
content filtering policy`, having written nothing. Batches 221–229 and 239–246
went through normally on the first try. Tightening the agent's report format to
a purely technical bibliographic summary did not help.

The same block then hit the **main conversation** when it tried to write those
pages out directly.

Nothing in the material is objectionable — it is Pascal's religious psychology
(misery, self-hatred, mortification, the *monstre incompréhensible*) and
Kierkegaard on despair. The plausible reading is a self-harm classifier
misfiring on 17th-century devotional vocabulary stripped of its context. It is
a false positive; it was reported via thumbs-down.

**The workaround, which is also just the better method:** do not have a model
retype the text at all. `build_frag.py` + `polish.py` + `markup.py` move the
words from tesseract into the file by deterministic script, and the model's
role shrinks to small targeted corrections that do not trip anything. This is
what TRANSCRIPTION-PLAYBOOK.md §2 meant in the first place — the OCR carries
the words, the image carries the structure. Use this route for pp. 230–238 if
the file ever has to be rebuilt.

## Printer's defects logged (transcribed as printed, never corrected)

| p. | as printed | note |
|---|---|---|
| 222 | `appronfondi` | for *approfondi* |
| 224 | `allemant` | for *allemand* |
| 226 | — | `fr. 935` / `956 Br.` verified at 2×; not the OCR's 985/936 |
| 227 | `Hégel` and `Hegel` | both forms on the same page |
| 228 | "à la production littéraire" | dittography, set twice |
| 232 | `Alsluttende` | for Kierkegaard's *Afsluttende*; verified at 600 dpi |
| 232 | `Paul Moller` | for Poul Møller — Høffding's own French form, no ø |
| 234 | `Epictète` | unaccented, though `Épictète` on p. 231 |
| 235 | damaged sort before `s'assimilant` | illegible at 600 dpi; sense wants *se l'assimilant* |
| 239 | `l'hommé` | for *l'homme* |
| 241 | `méchanceté!` | |
| 245 | `m'expose ».` | |
| 246 | `contiennent` | |

Guillemet balance is **0** (45 open / 45 close) — no defect disturbs it.

## Traps specific to this book

- **`check.py` must not flag French spacing.** A space belongs before `;` `:`
  `!` `?` and inside `« »`. Only a space before a comma or full stop is an
  artefact. The original rule flagged 76 false positives.
- **Marginal dirt is read as text**, at the end of lines as well as the start —
  stray `{`, `‘`, `|`, `_—`. Two stray `{` unbalanced the braces and a `_—`
  produced a `Missing $ inserted` at compile. `check.py` now catches both.
- Danish appears only in the p. 232 footnote (`\dk{}`). Everywhere else
  Kierkegaard is quoted in French.
- The scan is the whole issue; trust `pagemap.py`, never count pages by hand.

## Open review items

- [ ] Build both PDFs locally with the real fonts (libertinus) and confirm the
      Transcription and Translation links on the `/dansk/` page resolve
- [ ] Publish: `~/hhalvors.github.io/publish-danish.sh "message"`
- [ ] Report the content-filter false positive if it recurs

## A late correction pass worth knowing about

After the transcription was first declared complete, translating from it turned
up ~45 further OCR residues that `check.py` could not see, because each was a
*plausible French word or mark*: `atiitudes`, `aussilôt`, `déecrit`, `distinetion`,
`s'oceuper`, `Là Poésie` for `La Poésie`, `pascopernicien` for `pas copernicien`,
`quelles propositions` for `que les propositions`, stray `[`/`{`/`:` mid-sentence,
and a handful of missing word-spaces. All were fixed against the page images and
are listed in the git diff.

The lesson for the next French book: **translating is itself the best proofreading
pass**, because it forces every sentence to be parsed. Budget for a correction
round on the transcription while translating, and do not treat `check.py` coming
back clean as evidence that the text is right — it checks structure, not sense.

---

## PAGE-JOINT AND PARAGRAPH REPAIR — 2026 pass

Fifth item swept. The fault was found in `texts/nielsen/speculative-methode`;
read that book's RESUME-NOTES for the anatomy.

**transcription.tex**
- 2 page-joint hyphens → `\-%` (p. 232 "con-"/"sidérant", p. 236 "concep-"/"tion")
- 9 false paragraph breaks removed — **pp. 231–239, nine consecutive leaves**,
  every one plainly mid-sentence
- 0 missing paragraph breaks
- **and a separate defect: 8 printed LINE-break hyphens left bare mid-page**,
  printing as "précipita- tion", "pour- quoi", "primi- tive", "mar- quée",
  "souf- france", "pro- vincial", "chris- tianisme", "pro- blèmes". Not the
  page-joint fault — these are ordinary line divisions in the printed French
  that were never closed up — but the same artefact and the same fix. The
  `\emph{}` spanning "pro-"/"vincial" was preserved.

**translation.tex**: 1 false break (p. 239). Nothing else.

Both compile at 23 pages with no `word- word` artefact left, and the audit
returns nothing for either file.

### The running head is the hard part of this article

`paragraphs.py` here takes either file as its argument. Its one real problem is
that the Revue's running head is full-measure, so a naive left-edge test takes it
for a body line — **and it lies in both directions**:

- **even** pages set the folio out in the LEFT MARGIN, so the head begins ~340 px
  left of the text block and the page reads as a −337 px hanging indent;
- **odd** pages CENTRE the head, so it begins ~100 px right of the block and is
  indistinguishable from a paragraph indent. Printed p. 245 was reported as a
  +97 px indent on exactly that, and in fact opens flush.

Neither guard works alone: skipping any line followed by extra white space
over-skips on pages carrying a section space or a footnote rule (pp. 236 and 237
walked past the body and reported −323 and −127 px). Requiring the line to sit
within [margin−60, margin+400] lets the centred odd-page head through. **Both
together** give a flat measurement — continuations −19 to +20 px, the single
paragraph opening +77.

### Still outstanding elsewhere in the repo

The mid-page line-break hyphen is its own small population, separate from the
page-joint one: 2 in `hoeffding/relation-som-kategori/transcription.tex` and 4 in
`nielsen/propaedeutik-1860-61/transcription.tex`, neither of which has any
page-joint hyphens at all.

