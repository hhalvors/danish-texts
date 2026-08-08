# Rasmus Nielsen — *Den propædeutiske Logik* (1845): transcription resume notes

**Phase 1 (transcription) job.** Read this, then `BATCH-AGENT.md`, then continue the
batch loop. The standing method is `../../../TRANSCRIPTION-PLAYBOOK.md`.

## CURRENT RESUME POINT

**THE FØRSTE DEEL IS COMPLETE — printed pp. 1–96 done.**

**Next: printed p. 97 (PDF 106)** — the opening of the **anden Deel**. The next batch
(pp. 97–108) starts a Part, so it must place:

1. the full-measure **double rule** across the page top,
2. `\deel{anden Deel:}{Læren om det objective Begreb.}` — **note the printed LOWERCASE
   `anden`**, against p. 6's `Første Deel:` and the Indhold's `Anden Deel.` Verify on the
   image and reproduce the lowercase; both readings are on record and neither is normalised,
3. `\division{Indledning.}` — the anden Deel has its own Indledning,
4. `\parag{12}{Den dialektisk-speculative Methode.}`

**p. 96 ends cleanly** with the division tail ornament (`\divrule`); there is no mid-word or
mid-sentence joint to close, and no signature mark or catchword at that foot. So the
pp. 97–108 fragment begins with `% --- p. 97 ---` and a fresh paragraph, and the blank line
above its marker should be **left in place**.

**Three errata are still to come:** p. 112 (`Daddel` → `Dadel`), p. 152 (`med` → `ved`),
p. 154 (`Dyr=Rige` → `Dyre=Rige`), then p. 187, p. 206, p. 241. The p. 80, p. 92 and p. 93
entries are **done**.

## The two tail ornaments — settled by measurement

The book uses **two** distinct tail ornaments, at two structural levels. Measured at 300 dpi
by longest-contiguous-dark-run per pixel row, over a 1412 px text column:

| printed | closes | bands | max width | as fraction |
|---|---|---|---|---|
| 5 | the Indledning | one, 6 px | 403 px | **0.26** |
| 96 | the Første Deel | one, 5 px | 416 px | **0.27** |
| 35 | § 5 | **two**, ~310 + ~155 px | 310 px | **0.20** |
| 68 | § 8 and the Capitel | **two**, ~303 + ~153 px | 303 px | **0.20** |

So a **wider** ornament ends a top-level division and a **narrower double** rule ends a §.
The rule is **not** a Capitel marker — the same narrow double stands mid-Capitel at p. 35.

On pp. 5 and 96 the per-row widths are irregular (254/336/232/385/403 and
200/288/316/416/142): the band is not a rectangle but a **swelled rule**, thick at the centre
and tapering to points, the same class of ornament as the title page's centre-lozenge
fleuron. `\rule` cannot make one without graphics, so it is represented by a plain rule of
the measured width — an approximation recorded in the preamble rather than hidden.

These four rules had been hand-rolled **three different ways**, and p. 5's coding had missed
part of the ornament. All four now go through **`\divrule`** and **`\secrule`**. Do not
hand-roll a tail rule. (The 0.35-measure rules elsewhere are editorial decoration under
heads and in the front/back matter, not reproductions — leave them.)

Running tally of § ends: § 5 rule, § 6 none, § 7 none, § 8 rule, § 9 none, § 10 none,
§ 11 → division rule (it ends the Deel).

### A process lesson worth more than the page it cost

Batch 4 reported that p. 53's broken word `lige=` was completed by **`saa`** on p. 54. It is
completed by **`fremme`** — the word is *ligefremme*, in "Imod den simple Bekræftelse
stiller sig den ligefremme Benegtelse". Batch 5 caught it on the image; both OCR witnesses
agree with batch 5.

The error was mine to catch and I did not: **a batch agent's report about the page after its
own range is unverified by construction** — it has read that page only glancingly, if at all.
I copied "saa" into RESUME-NOTES and into batch 5's brief without checking, and only the next
agent's diligence stopped it entering the text. So: **when a batch ends mid-word, confirm the
completing fragment against the scan yourself before writing it into the notes, and state it
in the next brief as something to verify rather than as fact.**

`python3 check.py` prints progress; `bash verify.sh` compiles.

**RUNNING QUOTE BALANCE: raw 0 as of p. 89 — and that zero is a trap.** Two logged
printer's defects now cancel each other:

| page | effect | defect |
|---|---|---|
| 29 | −1 | Sibbern quotation **closes** with “ and has no opening „ anywhere |
| 86 | +1 | quotation **opened** „Hvis A er et … at p. 85's foot never closes |

Both are reproduced verbatim and flagged inline. A bare `balance=0` would read as all-clear,
so **`check.py` now carries the defect list explicitly** (`QUOTE_DEFECTS`) and reports the
raw balance against the expected sum, naming each defect and saying outright when a zero is
cancellation rather than soundness. **Add a row there whenever a new one is found.**

**Batches are 12 pages**, boundaries aligned so that **p. 97 starts a batch** (the anden
Deel opening). 23 markers cover pp. 18–283 with no gaps or overlaps.

## This book, concretely

- **Title:** *Den propædeutiske Logik*, af Lie. theol. R. Nielsen, Professor i
  Philosophien. Kjøbenhavn: Forlagt af Boghandler P. G. Philipsen; Trykt i BiancoLunos
  Bogtrykkeri, 1845. (The title page really does print **Lie.** for *Lic.* — a wrong-sort
  error, transcribed as printed and flagged. **BiancoLunos** is set solid as one word.)
- **Scan:** `~/bibliotek/Nielsen, Rasmus/1845-propædeutiske-logik.pdf` — KB, ABBYY
  Recognition Server, **297 PDF pp.**, A4, 105 MB. `propædeutiske_logik.pdf` in the same
  directory is the same scan. NB the filename contains `æ` and macOS hands it over in
  **NFD**, so a bash glob written in NFC will not match it — `pagemap.py --scan` walks the
  directory and normalises instead. Use it; do not glob by hand.
- **Script:** **Fraktur** throughout; Latin, French, English and all figures in antiqua
  → `\textit{}`. Polytonic Greek inline. Theta prints as the script form `ϑ`.
- **Offset (VERIFIED, UNIFORM): PDF = printed + 9.** Body printed pp. **1–283** =
  PDF 10–292. See the header of `transcription.tex` for how it was verified three ways.
  No leaf was scanned twice; the offset never changes.
- **catalog.yaml:** id `propaedeutiske-logik`, status in-progress.

## Structure (from the Indhold, PDF 8–9, read off the image)

- **Indledning** (pp. 1–5): sections **I.** *Den formelle og speculative Logik* and
  **II.** *Den propædeutiske Logiks Formaal*
- **Første Deel: Læren om det subjective Begreb** (pp. 6–96)
  - Første Capitel: *Det subjective Begrebs Dannelse* — §§ 1–5
  - Andet Capitel: *Det subjective Begrebs Fremstilling: den logiske Dom* — §§ 6–8
  - Tredie Capitel: *Det subjective Begrebs Gyldighed: Slutning og Beviis* — §§ 9–11
- **anden Deel: Læren om det objective Begreb** (pp. 97–283)
  - Indledning — § 12
  - Første Capitel: *Det objective Begrebs Dannelse* — §§ 13–15
  - Andet Capitel: *Det objective Begrebs Frihed* — §§ 16–18
  - Tredie Capitel: *Det objective Begrebs Fylde: Ideens Logik* — §§ 19–21

Three structural facts that are easy to get wrong:

1. **The §§ run continuously 1–21 across both Parts.** They do **not** restart in the
   Anden Deel. `check.py` reports a repeated `\parag` number as an error.
2. **The Indledning's two sections are numbered I./II., not as §§** — but the Anden Deel's
   Indledning **is** a § (§ 12). That asymmetry is in the book. Do not normalise it.
3. **The Indhold carries no page numbers at all.** Bare text, no leaders, nothing in the
   right margin. It is reproduced as printed in the front matter; the generated
   `\tableofcontents` carries this edition's own numbers.

## Printed-vs-Indhold variants — record both, do NOT normalise

- Body heads use a **colon** (`Første Deel:`); the Indhold uses a **period**
  (`Første Deel.`).
- Printed p. 97 prints **lowercase `anden Deel:`** against p. 6's `Første Deel:` and
  against the Indhold's `Anden Deel.` **The p. 97 batch must reproduce the lowercase.**

## Rendering conventions (locked in, batch 1)

Structure goes in through **preamble macros**, not hand-rolled centre blocks; `check.py`
counts the macros and flags hand-rolled display heads inside `\mainmatter`.

| Printed form | Macro |
|---|---|
| `Indledning.` as a top-level division (occurs at p. 1 and again at p. 97) | `\division{Indledning.}` |
| Part opening: double rule + `Den propædeutiske Logiks` + Deel line + argument | `\deel{Første Deel:}{Læren om det subjective Begreb.}` |
| Chapter head | `\capitel{Første Capitel.}{Det subjective Begrebs Dannelse.}` |
| `§ N.` + argument | `\parag{1}{Almeenforestillingen.}` |
| The bold letterspaced `A n m. 2.` lead-in | `\anm{2} Text…` |
| The Indledning's roman-numeral sections (I., II. — pp. 1 and 4 only) | `\romsec{I.}{Den formelle og speculative Logik.}` |
| The Danish "that is" sign ɔ: | `\dsi` |

Every head macro wraps its ToC argument in `\texorpdfstring`. If you add another, do the
same — a bare `\quad` inside `\addcontentsline` makes hyperref warn on every build.

**What is and is not letterspaced — settled at 400 dpi on printed p. 6, after two agents
disagreed about it:**

- `Den propædeutiske Logiks` — bold, **not** letterspaced
- `Første Deel:` — bold, **not** letterspaced
- `Læren om det subjective Begreb.` (the Deel argument) — **letterspaced**
- `Første Capitel.` (the Capitel label) — **letterspaced**
- `Det subjective Begrebs Dannelse.` (the Capitel argument) — not letterspaced, one size down
- `Almeenforestillingen.` (the § argument) — bold, **not** letterspaced

There is **no short centred rule** between the Deel argument and the Capitel head. An
early note claiming one was wrong; `\deel` no longer emits it.

Other conventions: Sperrsatz → `\emph{}`; Danish quotes `„…“` (U+201E / U+201C); em-dash
`---`; the Fraktur double-hyphen in compounds (`Dyre=Rige`, `Ikke=Jeg`) kept as `=`;
page-break comments `% --- p. N ---` at each boundary; a)/b)/c) sub-items as a plain
`itemize` with `\item[a)]` (enumitem is not loaded).

## What this book does NOT have

- **No footnotes anywhere.** Confirmed on the image and by a type-size sweep of all 283
  pages. References are inline in parentheses; the `Anm.` remarks do that work. The `3*`,
  `12*`, `18*` at some page feet are **signature marks** — do not transcribe them.
- **`Anm.` remarks are NOT smaller type.** The baseline pitch on printed p. 7 is identical
  to body text. Only the lead-in is distinguished, and nothing marks where a remark ends.
- **No figures, no tables, no displayed equations.** Inline antiqua symbols only
  (`A=A`, `A er ei = --- A`, A/B/C placeholders).
- **No running heads** in the original — only a centred bold antiqua folio.
- **No half-title, no dedication, no motto, no Forord.** Front matter is title page
  (PDF 6) and Indhold (PDF 8–9); PDF 4, 5 and 7 are blank.

## ERRATA to apply (from "Rettelser", PDF 293)

All nine are reproduced in the back matter and are to be **applied inline**, each flagged
with a `% ERRATA` comment at its site. None falls before p. 80.

| Page | Line | Printed | Read |
|---|---|---|---|
| 80 | 3 f.o. | Omsætningen | **Oversætningen** |
| 92 | 13 | A er ei = A, | **A er ei = --- A** |
| 93 | 7 | Betingelser | **Betingethed** |
| 112 | 4 f.n. | Daddel | **Dadel** |
| 152 | 8 | med | **ved** |
| 154 | 15 | Dyr=Rige | **Dyre=Rige** |
| 187 | 9 | εἵδη | **εἴδη** |
| 206 | 9 | en miniatur | **en miniature** |
| 241 | 1 | ϑετον | **ϑεῖον** |

The p. 92 entry **misprints `ci` for `ei` in its own right-hand column** (verified at
2400 dpi: the `c` has an open bowl, the `e` a crossbar). The errata page is transcribed
with that typo intact; the correction applied to p. 92 is the intended one, i.e. the
missing negation dash before `A`.

## Tooling notes (all learned the hard way in batch 1)

- **`ocr.sh`'s `J`→`I` rule is a WHITELIST on purpose.** A blanket
  `s/\bJ\([a-zæøå]\)/I\1/` destroys this book's commonest technical term — `Jeg`, `Jeget`,
  `Jegets`, `Ikke=Jeg` — and also `Jord`, `Jordbund`, `Ja`, `Jo`. Do not "improve" it into
  a general rule. `check.py`'s matching test carries the same exemptions.
- Systematic confusions still needing hand correction, in rough order of frequency:
  `ſ`→`s` (mechanised, the table's real earner), `f`↔`k` inside words (`lykfes`,
  `Adſfillelſe`, `stykfeviis`), `Ø` read as `D` (`Die`→`Øie`, now mechanised), dropped `ø`
  (`gjore`, `horer`, `Sporgsmaal`), `o`↔`v` (`selo`, `objectio`, `bles`), and `ll` read as
  `ﬅ`/`ff` in `o. s. f.` / `o. s. v.`
- **`spacing.py` narrows the search; it does not replace the image.** On batch 1 it gave
  21 RUNs (14 confirmed, 7 false, all on loosely justified lines) and ~45 singles (about a
  third confirmed). The single-word threshold is now 1.30, RUNs stay at 1.16. It has false
  **negatives** too — it missed `særskilt` (p. 12 l. 1) and the whole p. 6 display line.
  Printed p. 14 is the worst page in the batch; treat its output as noise.
- **Batch size: use 12 pages, not 17.** The content is fine at 17, but the sandbox caps a
  bash call at ~178 s and kills backgrounded processes, so `ocr.sh 1 17` cannot finish in
  one call. Practical recipe: one `pdftoppm -f A -l B -r 300 -png` per 8–9 pages, then OCR
  from the saved PNGs. Reading every page as two 300-dpi half-page crops is what the
  emphasis work actually needs.
- **Scan caveat:** printed p. 96 (PDF 105) carries a previous reader's **yellow
  highlighter** across the Sibbern quotation. Not a printing feature.

## Portable verify: run `bash verify.sh`

**Do not hand-type a sed chain.** Use `verify.sh`; it exits 0 when clean and prints a
labelled pass/fail line per check.

The first version of this recipe was a hand-typed chain that, besides substituting the
four packages the sandbox lacks, also rewrote `ɔ:` to `o:`. It reported **0 errors on a
file that could not build on the user's machine at all** — the raw ɔ (U+0254) was a fatal
error under the real preamble. Two further defects were warnings the recipe never looked
at. A test that edits away the thing under test is worse than no test. `verify.sh`
therefore substitutes **only** libertinus / libertinust1math / textalpha / babel-danish
and maps Greek to a placeholder, and it explicitly fails on:

- `^!` errors, missing characters, undefined control sequences
- hyperref `Token not allowed in a PDF string` (a `\quad` or other non-text token inside
  `\addcontentsline`, or a non-ASCII letter in the PDF metadata)
- pdfTeX `destination with the same identifier` (duplicate `page.N` labels)
- undefined references

Overfull hboxes are reported as **info only**: the sandbox substitutes lmodern for
libertinus, so its line breaking is not the real build's.

`make` cannot run in the sandbox — `libertinus.sty` is not installed there and every file
in the repo fails identically. **Never delete Greek from the source** to silence a
sandbox-only warning.

## Three build defects found after batch 1, and how they are fixed

The user's `make` failed on the first real build. All three were mine, all three were
invisible to the original sandbox recipe, and all three are now caught by `verify.sh`.

1. **Fatal: `Unicode character ɔ (U+0254) not set up for use with LaTeX`.** The `\dsi`
   macro contains the raw character. Fixed the way the rest of the repo already does it
   (see `texts/brochner/problemet-tro-viden/transcription.tex`):
   `\usepackage{graphicx}` + `\DeclareUnicodeCharacter{0254}{\reflectbox{c}}`.
   `\dsi` is kept for greppability.
2. **`destination with the same identifier (name{page.1})`.** `\begin{titlepage}` resets
   the page counter to 1 in whatever numbering is in force. With the titlepage before
   `\frontmatter` that was arabic, so the title page and the first page of `\mainmatter`
   both claimed `page.1`. Fixed by moving `\frontmatter` **before** the titlepage, adding
   `plainpages=false,pdfpagelabels`, and deleting the redundant `\pagenumbering` calls
   that were fighting `\frontmatter`/`\mainmatter`.
3. **`Token not allowed in a PDF string`, twice over.** First from a bare `\quad` inside
   the hand-rolled `\addcontentsline` for the I./II. heads — those are now the `\romsec`
   macro, which wraps the argument in `\texorpdfstring` like every other head macro.
   Second from the `æ` of `pdftitle={Den propædeutiske Logik}` given as a *package
   option*, where fontenc still has it as `\T1\ae`. The metadata is now set with
   `\hypersetup` **after** `\begin{document}`, where the æ comes through intact.

## A fourth build defect: Greek variant letterforms (found after batch 2)

`! Package greek-fontenc Error: character theta symbol not available in text mode.`

The book's Greek fount prints theta as the script **ϑ** (U+03D1). Batch 1 typed it raw,
because the brief told it to "keep it" — my mistake twice over, since **the repo already
has a standing convention for exactly this** and I failed to pass it on. See
`texts/nielsen/religionsphilosophie/transcription.tex`, which uses the same `textalpha`
preamble and carries comments like *"the script theta ϑ of the fount is normalised to θ
per the standing convention"* and *"the cursive kappa ϰ to κ, as fount variants"*.

**The convention, restated:** `ϑ→θ`, `ϰ→κ`, `ϕ→φ`, `ϖ→π`, `ϱ→ρ`, `ϐ→β`, `ϵ→ε`, `ϲ→σ`,
each with a `%` note at the site. These are fount variants, not distinct letters — we
already render Fraktur in a roman face rather than reproducing its letterforms, and
insisting on script theta while doing so would be inconsistent. **Accents and breathings
are NOT fount variants** and are reproduced exactly as printed.

(The `essential-kierkegaard` files do keep raw `ϑ`, but they use a completely different
Greek pipeline — `newunicodechar` + `\ensuremath{\vartheta}` in math mode — not ours.)

**Why no test caught it, and what now does.** The sandbox cannot compile Greek at all:
`textalpha`/`greek-fontenc` is not installed, and `tlmgr` cannot install it (local TeX
Live 2021 against a 2026 remote). `verify.sh` therefore has to map the Greek range to a
placeholder — so any unusable Greek character sails through the compile and dies on the
user's machine. `verify.sh` now runs a **static lint** over the original source for those
eight variant codepoints, skipping `%` comment lines so a comment may still discuss the
variant form. Self-tested: reintroducing a single `ϑ` makes it fail.

Point 3's second half is a **repo-wide latent issue**: `philosophisk-propaedeutik` and
probably other books set a `pdftitle` containing `æ`/`ø` as a package option and will be
emitting the same warning and losing the letter from their PDF metadata. Harmless to the
build; worth a sweep some day.

## DONE so far

- **Batch 8 (pp. 90–96), image-verified. FØRSTE DEEL COMPLETE. Two errata applied.**
  **p. 92 errata applied:** the phrase runs across the line break — l. 13 ends "…den anden:
  A er ei =" and l. 14 opens "A derimod Jegets Forskjel fra Ikke=Jeg." The negation dash is
  set between the `=` and the second A. The same page's third Grundsætning, printed
  `A og --- A`, settles that a full em-dash is the sort wanted — a good piece of internal
  evidence. **p. 93 errata applied:** `Betingelser` → `Betingethed`, located **by the word**
  (unique on the page), not by counting lines, since the Rettelser's line number is off by one
  against the OCR's split.
  **The two tail ornaments were settled here** — see the table above. The agent measured all
  four rules on one threshold and found pp. 5/96 distinct from pp. 35/68; I re-measured
  independently by a different method (longest contiguous dark run per row) and confirmed it,
  additionally showing the pp. 5/96 band to be a **swelled** rule rather than thick-over-thin.
  `\divrule` and `\secrule` added and all four sites retrofitted, including p. 5, whose
  coding had missed part of the ornament.
  **Fichte's apparatus** (`A`, `Non-A`, `Ikke=Jeg`) set as antiqua `\textit{}` placeholders
  with plain `=` and `---`, per the house style already at pp. 18 and 82 — **not** math mode,
  since nothing here is a real relation.
  **Antiqua → `\textit{}`:** *circulus in probando*, *Anal. post. c. 2* (whole parenthesis,
  per p. 89), *methodus mathematica*, *a priori*, *in abstracto*, *in concreto*, the A
  placeholders. German quotations stay Fraktur („discursive Grundsätze“, „Ding an sich“,
  *Die Disciplin der reinen Vernunft*, „Daseyn zu enthüllen“ — ä/ü raw). `cfr.` is **Fraktur**
  here (verified at 8×) and left upright, as are the figures "Pag. 24; 81" per p. 89.
  **Letterspacing:** p. 92's run *Identitet* / *Modsætning* **drops the intervening "og"**,
  which is solid — **seventh consecutive batch** of this. Also *begrændse*, *Grundens*
  (p. 92), *Methode*, *Fornuftkunstner* (the run carries across the `For=/nuftkunstner`
  break), *afsløre Tilværelsen* (p. 93). pp. 90, 94, 95, 96 carry none at all.
  Rejected as false: *sætter* (p. 91 — the line opens with antiqua *in abstracto*, which
  inflates the model), *Formen;* (p. 93), and **tesseract's whole highlighted p. 96 passage**,
  which is solid under the wash.
  **Printer's defects, as printed and logged:** p. 90 no full stop after "fra Plato" (clean
  paper at 8×; `\quad` per pp. 21/40); p. 91 `1 Haupst.)` for *Hauptst.*; **p. 92's Anm. 2
  paragraph ends with a comma** ("Demonstration tilbage,") — the mark carries the comma's
  tail, unlike the wedge point after "frem." eleven lines above; p. 93 a near-blind *r* in
  "Demonstrations" and a doubled point in `Miscredit..` (p. 15 "Pg.." precedent); p. 94 an
  **under-inked em-dash** after "overflødig.", a third of its length inked at dash height,
  where the same page sets a well-printed `---` twelve lines below (press debris rejected).
  **Glyph ID:** Fraktur *x* confirmed in *existerende*, *Exempel*, *Reflexions*, *Reflexion*,
  *forvexle*, *forvexles*; **Fraktur *E* in *Eensidighed*, which ABBYY reads as G throughout**;
  `beviisning` double-i confirmed against ABBYY's single.
  **Greek (p. 90, the Anal. post. I 2 quotation):** normalised ϰ→κ ×12, ϱ→ρ ×10, ϑ→θ ×1.
  Reproduced as printed, not corrected: **ἀναγκη** with psili but no oxia; **γαρ** with no
  varia; **οὑτος** with dasia only (the mark opens rightwards, where the psili of ἀ/ἐ on the
  same line opens leftwards); γνωριμοτέρων with omicron for omega; **συμπεράςματος** with a
  final sigma standing medially — a wrong sort on the p. 89 / p. 33 precedent, so not
  normalised; **οἰκεῖαι**, where the perispomeni stands over the ε in print and Unicode forces
  it onto the ι (p. 32 ὁποῖόν precedent).
  The elision mark on **τ’** was flagged rather than invented: the agent set an ASCII
  apostrophe rather than introduce U+1FBD koronis. I changed it to the typographic apostrophe
  **U+2019**, which T1 handles natively — an ASCII straight quote inside a Greek word would
  also have escaped `check.py`'s straight-quote test, which only looks for `"`.
  Compile: **75 pp., 0/0/0/0**; braces balanced; quotes „85 / “85 = raw 0, matching the two
  logged defects; suspect readings 0.

- **Batch 7 (pp. 78–89), image-verified. FIRST ERRATA APPLIED.**
  **p. 80 errata applied and flagged:** line 3 f.o. confirmed on PDF 89 as "tagelse af
  Omsætningen, og Alhedsslutningen bliver desaarsag"; set as **Oversætningen** with a
  `% ERRATA` comment. p. 85's own "Oversætningen bliver da en hypothetisk Dom" corroborates
  the direction. **Keep the asymmetry straight: printer's defects are transcribed as printed
  and merely logged; Rettelser entries ARE applied.**
  `\parag{11}{Slutningens reelle Gyldighed: Beviis og Methode.}` placed (p. 88), matching the
  Indhold. **§ 10 closes with no rule** — measured, not eyeballed: the 111 px band carries a
  flat ~66 dark px/row, which is the scan's edge noise, where the pp. 35/68 ornament spikes to
  ~300. Tally: § 5 rule, § 6 none, § 7 none, § 8 rule, § 9 none, § 10 none.
  **A claim I measured and rejected.** The agent reported that the § thesis is set *one size
  up* from the body, and flagged it for a possible macro and retrofit across all eleven §§. I
  measured p. 88 at 400 dpi, taking x-height as the band where a line's ink density is ≥ half
  its max: **body lines 35–43 px (mean ~39), § 11's thesis lines 38–43 px (mean ~40.5)** —
  inside the page's own spread. Baseline pitch is ~105 px above and below the head alike. What
  *is* larger is the § **argument** line, at 58 px, which `\parag` already sets larger. So no
  size change, no macro, no retrofit; the finding is recorded in the file so it is not revived.
  What was real is the tooling consequence: `spacing.py` fits one glyph-width model per page,
  so its pp. 88–89 flags ("poetisk", "logi") are justification artefacts.
  **No tabular or multi-column layout** in range — the schema letters are inline antiqua
  (`\textit{E---S---A}`), and p. 78's three Yderligheder are separate capitals with Fraktur
  "og" between, italicised singly.
  **Antiqua → `\textit{}`:** *universale/universalia*, *terminus medius*, *termini*, *genus*,
  the a/b/c and A/E/S placeholders, *universalia ante rem / in re / in mente*, *modus
  ponens/tollens*, *posita conditione…*, *sublato conditionato…*, *conditio/conditionatum*,
  *propositio major*, *a non posse…*, *ab esse…*, *principium exclusi medii*, *Analytic. post.
  c. 1---3*. Two whole-run cases on the p. 67 precedent, where an intervening Danish word is
  itself antiqua: **"implicite eller explicite"** (p. 84) and the Aristotle reference. "Pag.
  99" and "(§ 8 Anm. 4)" left unitalicised per pp. 21/52. Note ***comprehensive*** (p. 79) is
  letterspaced **Fraktur**, not antiqua — long ſ and Fraktur h/v at 4×.
  **Printer's defects, as printed and logged:** p. 78 **"Uviversalqvalitet"** (wrong sort, v
  for n — the glyph matches the v two positions later, not the n before it); p. 81 near-blind
  *r* in **Grundlag** (witnesses fail in opposite directions, "Guundlag"/"Gnindlag"); p. 83
  **"ngenlunde"** for *ingenlunde*, initial i never set, clean paper and no ghost; **p. 86 a
  quotation opened at p. 85's foot („Hvis A er et …) that never closes** — the source of the
  new +1; p. 89 a stray vertical hairline between "den" and "Vished", press debris, logged not
  transcribed. Wedge full stops confirmed (not commas): "beboet." p. 81, "Analytic." / "post."
  p. 89.
  **Greek (p. 89 only):** one normalisation, **ϰ→κ** in *ἐπιστημονικός*. **NOT normalised:
  συλλογιςμὸς, printed twice with a final sigma standing medially** — the second occurrence is
  mid-line and mid-word with a correct final ς three letters later for comparison, so a wrong
  sort on the p. 33 „Ειςαγωγη“ precedent, not a line-break form.
  Compositor takes in a preceding "et" twice on p. 80 — **sixth batch running**. Rejected as
  false: **"det andet Schema"** (p. 80 — ABBYY spaces it, the image does not, and it is the
  exact parallel of p. 79's solid "det første"), "Slutningernes Antal er" (p. 87),
  Combination/det. (p. 81), udvikles (p. 84), deri (p. 86), poetisk/logisk (p. 89).
  **Reader's marks (not transcribed):** grey pencil marginal lines at p. 80 left (ll. ~10–12,
  the Induction definition) and p. 81 right (ll. ~10–14); a brown foxing speck in p. 83's
  right margin.
  Compile: **71 pp., 0/0/0/0**; braces 876/876; quotes „74 / “74 = **raw 0, which is the
  p. 29 −1 and the p. 86 +1 cancelling** — see the trap noted above; suspect readings 0.

- **Batch 6 (pp. 66–77), image-verified.** Closes **§ 8 and the Andet Capitel** at p. 68,
  opens **Tredie Capitel** with **§ 9 *Slutningens logiske Reqvisiter*** and
  **§ 10 *Slutningens formelle Gyldighed***; all heads match the Indhold word for word.
  **The section-end rule is now understood:** p. 68's rule was *measured* — 301 px, two ~4 px
  rules with a ~4 px gap — against p. 35's 305 px, identical build. So it is **the same
  ornament in both places**, and since p. 35 falls mid-Capitel while p. 68 falls at a Capitel
  end, **the rule is not a Capitel marker**. § 9 ends with no rule. Running tally of section
  ends: § 5 rule, § 6 none, § 7 none, § 8/Capitel rule, § 9 none.
  **German is now typed RAW.** This batch brought the book's first **ß** (the Hegel „der
  Schluß ist nicht nur vernünftig…"). The agent conservatively wrote `\ss{}` and `\"u`; I
  tested raw `ß ä ö ü Ä Ö Ü` under T1 fontenc, found them native and identical in output, and
  converted the whole file (3 `\ss{}`, 7 umlaut commands, incl. p. 32's „Qvidität"). Verified
  in the built PDF. Much more German follows in the Anden Deel, so keeping it raw matters for
  readability; BATCH-AGENT.md now lists the full set of characters that may be typed raw.
  **Two glyph-ID readings kept as printed, alternatives rejected:** **φαλαρκός** (p. 71) with
  ρκ where κρ is wanted — the rho's descender precedes the baseline-only ϰ at 6× — and
  **σοφιστιχῶν** (p. 72) with a **χ** where κ belongs, that glyph carrying the same long
  descender as the χ of ἐλέγχων, unlike p. 71's ϰ. Greek normalised: ϱ→ρ, ϰ→κ (φαλαρκός,
  περὶ, σωρείτης, παράδοξα). Lint clean.
  **Fraktur x confirmed throughout** against ABBYY's systematic x→r (Extremer, Reflexer,
  t. Ex., Alexander).
  **Antiqua → `\textit{}`:** the *ratiocinium* series, *conclusum/conclusio*, *terminus
  minor/major/medius*, *propositio major/minor*, *Ex meris…*, *nota notæ est nota rei
  ipsius*, *Elenchus in dictione*, *partitio*, *implicite* (p. 70 — antiqua, verified against
  the Fraktur beside it), *universalia/res/universale*, and the E–S–A schema letters. Note the
  Danish **"eller" inside `(conclusum eller conclusio…)` is itself antiqua**, so the whole
  parenthesis is italicised. German quotations stay Fraktur.
  **Printer's defects logged in place:** p. 67 no full stop after `(partitio)` (set `\quad`
  per p. 40); p. 71 near-blind point after "Sophistik." and near-blind comma after
  ψευδόμενος; p. 74 **"auden"** for *anden*; **p. 75 a SECOND "Anm. 1." inside § 10** —
  unmistakable at 4×, both witnesses agreeing, so § 10 has two Anm. 1; p. 75 a stray
  mid-height stroke after "dydig," logged as press debris and *not* transcribed (an intended
  dash was rejected); p. 76 a near-blind *r* in "Fremskridt" and an ink speck over the *m* of
  "fremhæves"; "fiirbenet" with a doubled i (tesseract "fürbenet", ABBYY "fiirbenet").
  **Compositor lapse, fifth batch running:** on p. 77 `Det Enkelte er kun Enkelt` takes in
  "er kun", while `bliver` stays solid before `det Enkelte almindeligt`. Rejected as false:
  dicat/der (68), eer (69), jule/ife (71), viser (74), iet (76).
  **Two new layout forms**, neither tripping `check.py`'s hand-rolled-head test: the displayed
  three-line Latin syllogism on p. 71 (`\begin{center}` + `\textit{}`, resumption carries
  `\noindent`) and the 1)/2)/3) hanging list on p. 70 (plain `itemize`).
  **Scan artefacts (not transcribed):** p. 68 the scan's colour balance **flips to magenta at
  the rule** — straight-edged, type undisturbed, a scanner artefact not an ink change; p. 66 a
  pencil stroke under "maa" and a margin tick, same hand as pp. 47/56.
  Compile: **63 pp., 0/0/0/0**; braces 775/775; quotes „66 / “67 = **−1, still only the p. 29
  defect** (batch internally balanced 18/18); suspect readings 0.

- **Batch 5 (pp. 54–65), image-verified.** Finishes **§ 7** — which closes on p. 55 with **no
  rule at all** (checked at full autocontrast; the band is blank, what shows is verso
  bleed-through) — then `\parag{8}{Dommens logiske Totalitet.}`, matching the Indhold word
  for word. So section ends now run: § 5 double rule, § 6 none, § 7 none. **The book is
  simply inconsistent here; check each one and record what is there.** `Anm. 1–4` of § 8 all
  fall in range; **Tredie Capitel not reached**.
  Also caught **my propagated error on the p. 53/54 joint** — see the process lesson above.
  **Two glyph-ID cases, both settled on the image:** *forvexles* (p. 55) and *fixere* (p. 58)
  — the sort is a **Fraktur x**, whose right leg drops below the baseline at 600 dpi. Both
  engines read "forverles", and **ABBYY turns every Fraktur x on these pages into r**, which
  is a systematic trap worth remembering. And `o. s. f.` (p. 62) — the first sort's nub is
  left (long ſ), the second's bar right (f); tesseract read "o. ﬅ ff.", ABBYY "o. s. s.".
  **Compositor lapses, reproduced not regularised:** p. 59's run takes in "de" and "og" —
  *de over= og underordnede* spaced entire, while the identical phrase three words later is
  solid. Conversely p. 62's *analyseres* is spaced but the parallel "synthetisk" is not.
  That is **four batches running**; treat it as this compositor's habit.
  Rejected as ABBYY false positives: "Sammenhæng", "Forhold" (p. 54), "Sætningers" (p. 56),
  "da finder Læren om de" (p. 59), "Domme…Subject" (p. 60).
  **Printer's defects logged in place:** p. 57 "Mere" with an almost unprinted *e*
  (tesseract "M.,re", ABBYY "Mvre"); p. 57 a blotted *g* in "dog"; p. 60 "endydermere" set
  solid; p. 61 near-blind full stop after "forfeiles."; p. 65 a badly under-inked antiqua *B*
  in "ikke B."; p. 65 **"pricipium"** for *principium*, as printed; p. 65 a comma set inside
  the closing quote of „og,“, reproduced. The point after the 8 in "§ 8." is the fount's
  wedge full stop — **both engines read it as a comma**.
  **Greek: none normalised.** The only Greek is the sub-item pair **α) / β)** on p. 56, plain
  U+03B1/U+03B2 in italic Greek sorts — genuine labels here, unlike p. 48's wrong-sort β.
  No breathings or accents; lint clean.
  **Reader's marks (not transcribed):** pale wavy pencil underline under p. 56 ll. 1–4, same
  hand as p. 47; a curved pen brace in p. 63's right margin against the last three lines; a
  small brown pen tick in p. 60's left margin.
  **Mid-word joints inside the batch**, each already carrying a trailing `%`: p. 56/57
  ("egent=" / "lige") and p. 59/60 ("under=" / "ordnede"). p. 63/64 is a paragraph break.
  Compile: **53 pp., 0/0/0/0**; braces 687/687; quotes „48 / “49 = **−1, still only the p. 29
  defect** (batch internally balanced 6/6); suspect readings 0. Confirmed in the built PDF
  that the p. 53/54 seam emits a single "ligefremme".

- **Batch 4 (pp. 42–53), image-verified.** Finishes **§ 6** — which ends on p. 46 with **no
  rule at all** (checked at high contrast; contrast the double rule closing § 5 on p. 35,
  so the book is not consistent about section ends) — then
  `\parag{7}{Dommens logiske Indhold.}`, matching the Indhold word for word. `Anm. 1–5` of
  § 7 all fall in range. **§ 8 not reached.** The a)/b)/c) discussion on pp. 43–46 is a
  plain `itemize` per the pp. 3/15 precedent; its labels are antiqua in print but left
  unitalicised for consistency with the earlier lists.
  **Emphasis spot-checked by the caller at 600 dpi** on the batch's most interesting claim:
  p. 52's run **takes in "har Schelling"** — `det Absolute har Schelling` is spaced across
  all four words while `gribeliggjøre` on the same line is solid. Confirmed, reproduced, not
  regularised. That is now three batches running in which the compositor's letterspacing
  takes in or drops an adjacent word; treat it as normal for this book. Rejected as false:
  "speculativt Standpunkt" (p. 52).
  Antiqua → `\textit{}`: *Diversi respectus tollunt/faciunt contradictionem*, *diversi
  respectus*, *idem per idem*, *in mente*, *res*, *universalia*, *sub specie æternitatis*,
  and the A/B/C/D placeholders. „Das Urtheil des Daseyns" / „der Reflexion" stay Fraktur.
  **Greek** normalised with `%` notes: ϕ→φ and ϱ→ρ (φλυαρία, p. 44), ϰ→κ and ϱ→ρ
  (κατὰ … χρόνῳ, p. 45), ϰ→κ (ὑποκείμενον, p. 50). Accents and breathings reproduced as
  printed, incl. ἀδολεσχία with psili + oxia and a round medial sigma.
  **Printer's defects logged in place:** p. 43 a nearly blind full stop after "opfattes"
  (both OCR witnesses drop it); p. 45 **"Parodox"** for Paradox; **p. 48 a Greek β) standing
  where "b)" is wanted** — a wrong sort out of the Greek case, transcribed as printed
  (U+03B2, *not* ϐ, so the Greek lint stays clean); p. 51 an ink blot between "ere" and
  "Mennesker" (press debris, not a sort); p. 51 "forskiellige" with -ie-; p. 52 a "fordi"
  whose *r* is almost unprinted — tesseract read "for di", ABBYY "fo di", the stem's ghost
  is visible on the image, so **fordi**.
  **Scan caveat 3:** printed **p. 47** (PDF 56) carries a reader's **pencil underline**
  under "Diremtioner" — wavy, grey, overrunning the word. Not a printed rule.
  `check.py` now exempts **"Just"** (an ordinary Danish adverb, printed with J, both
  witnesses agreeing) from the Fraktur-I test.
  Compile: **45 pp., 0/0/0/0**; braces 578/578; quotes „42 / “43 = **−1, still only the
  p. 29 defect** (batch internally balanced 16/16); suspect readings 0.

- **Batch 3 (pp. 30–41), image-verified.** Finishes **§ 5** (ends p. 35, closed by a short
  centred **double** rule — two 0.4 pt rules at ~0.22 of the measure, verified at high
  contrast, *not* one under-inked heavy rule, so not the p. 5 ornament). Then
  `\capitel{Andet Capitel.}{Det subjective Begrebs Fremstilling: den logiske Dom.}` and
  `\parag{6}{Dommens logiske Form.}`, both matching the Indhold word for word. **§ 7 not
  reached.**
  **Greek**, word-by-word at 600 dpi, normalised with `%` notes: ϑ→θ, ϰ→κ, ϱ→ρ, ϕ→φ, and
  **ϲ→σ** in σώματά (p. 33, the one lunate sigma). Reproduced as printed, not corrected:
  γενων (no perispomeni), ταύτα (oxia for perispomeni), κατεγορεῖται (ε for η), the graves
  on διαφορὰ/συμβεβηκὸς/χωριστὰ, and ἰδιον psili-only on p. 32 against ἴδιον on p. 31. In
  ὁποῖόν the perispomeni sits over the omicron in print; Unicode forces it onto the iota,
  noted at the site.
  **`ꝛc.` — decided, and I overruled the agent here.** The agent transcribed the Fraktur
  *et cetera* sort literally as "2c." on the diplomatic principle. That was wrong: it is
  the **r-rotunda abbreviation ꝛc.**, whose sort merely *looks* like a figure 2 — and both
  OCR witnesses fell for it in different ways (tesseract "2c.", ABBYY ":c."), which is the
  tell that neither is evidence. Verified on the image at 600 dpi. Rendered **`\&c.`** per
  repo precedent (`texts/moller/qvindelighed`, `texts/moller/affectation`); raw U+A75B is
  not available in T1/libertinus (tested). Printed p. 2 sets the spelled-out "etc." in
  antiqua — both forms kept distinct, neither normalised to the other.
  **The general lesson:** "transcribe as printed" applies to what the compositor *set*, not
  to what an OCR engine *reports*. When the two witnesses disagree in different directions
  on the same glyph, that is a glyph-identification problem, and only the image settles it.
  **Printer's defect:** p. 40, no full stop after "(Stilpons Kaal)" — clean gap at 4×; set
  as `\quad`, as batch 2 did for p. 21. Compositor inconsistency logged: the letterspaced
  run takes in "det" on p. 30 but leaves it solid in the parallel phrases on pp. 30–31.
  Emphasis rejected as false: *blot* (p. 30, kerning gap), *Valg* (p. 38), *ere disse*
  (p. 40).
  **`„Ειςαγωγη“` (p. 33)** has no breathing, no accent, and a **final sigma used medially**
  — a wrong sort, not a fount variant (the same page sets round σ six times), so it is
  **not** normalised.
  **`„Qvidit\"at“` (p. 32)** written with the accent command `\"a`, not a raw ä. `check.py`
  now excludes `\"` from its straight-quote test.
  **Scan caveat 2:** printed **p. 34** (PDF 43) carries the same reader's yellow
  highlighter as p. 96, across "da maae begge disse Extremer … skaberiske Productivitet."
  Tesseract garbles it and reports it letterspaced; the type underneath is solid.
  Compile: **37 pp., 0/0/0/0**; braces 473/473; quotes „26 / “27 = **−1, still just the
  p. 29 defect** (the batch itself was internally balanced 19/19); suspect readings 0.

- **Batch 2 (pp. 18–29), image-verified.** Finishes **§ 3** and adds
  **`\parag{4}{Begrebets Aprioritet.}`** (p. 20) and **`\parag{5}{Begrebets Totalitet.}`**
  (p. 26); both printed heads match the Indhold exactly. Andet Capitel is *not* reached —
  § 5 still runs at the foot of p. 29 and there is no section-end rule in range.
  Latin antiqua → `\textit{}`: *Cogito, ergo sum*, *a priori*/*a posteriori*,
  *dignitate prius/posterius*, *conceptus superiores/inferiores*, *genus*, *species*, the
  *universalia* series, *principium individuationis*, and the placeholders *a*/*A*.
  „Wissenschaftslehre" stays Fraktur inside the quotes, as „Ding an sich" does.
  Greek zoom-verified: γένη, εἴδη (the iota carries psili+oxia, U+1F34 — already the form
  the Rettelser prescribe at p. 187). p. 18 needed an infinity sign and a less-than: set
  as `$\infty$` and `$<$`, **no raw glyph**.
  **Emphasis:** every call settled on 300-dpi zooms, because the ABBYY layer proved a bad
  witness here — it letterspaces whole loosely justified lines. Rejected as false:
  "Forhold til" (p. 18), "Derfor kaldes dette Forhold et" (p. 19), "hævet til en fri
  Totalitet" (p. 20), "Theorier" (p. 25). Two real **compositor lapses** logged in place:
  *almindelige* is letterspaced but **"Grundformer" is set solid** (p. 20), and **"i og"
  is solid** before letterspaced *med* (p. 27).
  **Printer's defects (as printed, logged in place):** p. 21 the dash between "Pag. 190"
  and "200" was never set; p. 21 "Bgrebet" for "Begrebet"; p. 28 a stray bar prints over
  the *e* of "det"; **p. 29 the Sibbern quotation closes with “ but has no opening „** —
  this is the source of the running −1. p. 22's full stop after "Gyldighed" is nearly
  blind but present.
  **Joint:** the p. 17/18 join runs on mid-`Anm. 4`, so the blank line the skeleton keeps
  above a marker had to be closed up after splicing or a paragraph break appears that is
  not in the book. **Check this at every joint that lands mid-paragraph.**
  Compile: **29 pp., 0/0/0/0**; braces 392/392; `$` even; quotes „7 / “8 = **−1, the
  documented p. 29 defect**; suspect readings 0.
  Batch size 12 confirmed comfortable: two `pdftoppm` calls of six pages, ~60 s each,
  well inside the sandbox's ~178 s cap.

- **Setup, image-verified.** Scan chosen; page map verified three ways (see the
  `transcription.tex` header). `pagemap.py`, `ocr.sh`, `spacing.py`, `check.py`,
  `splice.py`, `twoup.sh`, `BATCH-AGENT.md` in place. Preamble built (book class; amsmath,
  libertinus, libertinust1math, textalpha, fancyhdr, hyperref, microtype; no tikz/graphicx
  — prose only) with the six structural macros. Title page (PDF 6) reproduced. Indhold
  (PDF 8–9) and Rettelser (PDF 293) transcribed from the image, complete. Skeleton laid
  down with 22 batch markers; compiled clean at 9 pp.
- **Batch 1 (pp. 1–17), image-verified.** The **Indledning** (pp. 1–5, sections I. and
  II.) and the opening of the **Første Deel** through **§ 3** (pp. 6–17). `\deel` +
  `\capitel` + `\parag{1,2,3}` placed; 18 `\anm{}` remarks. Greek zoom-verified: p. 12
  `ἕν … πολλὰ … (ἀγαίμην ἂν ϑαυμαστως, ὦ Ζήνων)` — `ϑαυμαστως` has **no** circumflex as
  printed; p. 17 `(ἐπιστήμη --- νοητόν)`. Latin antiqua → `\textit{}`: *tabula rasa*,
  *in concreto*, *nomina apellativa* (one `p`, as printed), *ratio essendi*,
  *pro*/*contra* (the intervening "og" is Fraktur). The a)/b)/c) sub-items on pp. 3 and 15
  set as plain `itemize` with `\item[a)]`. Two features have no macro and are hand-rolled
  with comments: the raised initial (~1.5× body, flush left) opening the Indledning and
  § 1, and the short heavy rule closing the Indledning on p. 5.
  **Print defects logged in place (transcribed as printed, not corrected):** p. 1
  "Skjæbne" final `e` under-inked; p. 8 l. 1 missing full stop after "for Lidet"; p. 15
  "Pg.." doubled point. Also logged: p. 8 "omslutter" is **not** letterspaced though the
  sense wants it. **No errata fall in this range.**
  Compile: **21 pp., 0 errors / 0 missing char / 0 undefined cs / 0 overfull hbox**;
  braces 309/309; `$` even; quotes **„6 / “6, balanced**; suspect readings 0.
