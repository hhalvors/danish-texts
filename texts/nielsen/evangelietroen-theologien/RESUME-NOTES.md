# R. Nielsen, *Evangelietroen og Theologien* (1850) — resume notes

Twelve lectures, Copenhagen winter 1849–50. C. A. Reitzel, 1850. VIII + 174 pp., Fraktur.
Why this book: the compact statement of the heterogeneity thesis — faith and knowledge rest
on absolutely heterogeneous principles — written in the winter right after the *Johannes
Climacus* review. The target text for the question of how Nielsen stayed Kierkegaardian
without giving up science.

## Files
- Scan: `bibliotek/Nielsen, Rasmus/1850-evangelietroen-theologien.pdf` (195 PDF pp., 37 MB).
  Same file as KB `e-mat/dod/11030800271D.pdf`.
- Transcription: `transcription.tex` (this dir). Translation: not begun.
- Catalog entry: `catalog.yaml`, author `nielsen`, id `evangelietroen-theologien`.

## ⚠ PAGE MAP — NOT UNIFORM. Use `pagemap.py`; never hard-code +13.
The leaf bearing **printed pp. 82–83 was scanned twice** — it appears at PDF 95–96
and again at PDF 97–98 — so everything from printed p. 84 on is pushed back by two.

| printed | PDF |
|---|---|
| 1–83 | + 13  (PDF 14–96) |
| *(PDF 97–98 = duplicate of printed 82–83 — skip)* | |
| 84–174 | + 15  (PDF 99–189) |
| Forord III–VIII | PDF 8–13 |

Verified by reading the header numeral off every page from PDF 14 to 192. Endpoints
check: PDF 14 = printed 1, PDF 96 = printed 83, PDF 99 = printed 84, PDF 189 =
printed 174, PDF 190–191 = Indhold. Apparent one-page jumps at PDF 47, 68, 119 and
141 are OCR misreadings of the numeral (34→31, 55→53, 104→101, 128→426); the next
page reverts, so they are not real.

`pagemap.py` is the single source of truth and every script calls it.

## CURRENT RESUME POINT
**Forord (pp. III–VIII, PDF 8–13): DONE.** ~1770 words.

**Første Forelæsning (pp. 1–13, PDF 14–26): DONE.** Transcribed in one batch, image-verified
against all 13 pages (six two-up renders). Letterspacing confirmed and marked `\emph{}`:
the Thesis on p.2, `videnskabelig forstaaet` / `christelig forstaaet` on p.6,
`Aabenbaringssandheden og den almindelige Fornuftsandhed` on p.7, the augsburgske
Confession's `rettelig forkyndes` / `rettelig forvaltes` on pp.11–12 (twice each), and the
closing thesis restatement on p.13. `in specie` (p.8) and the Latin Confession text
(p.11, `Ecclesia est congregatio...`) marked `\textit{}` — both print in antiqua against
the surrounding Fraktur, confirmed on the image. One doubtful reading resolved by zooming
to 5×: p.6 "uden at den maaskee **i Heden selv** ret mærker det" (hyphenated He-den across
the line break) — read this way, not "Hjertets Grund"; check again if it looks wrong in
context later. Verified compile in the sandbox (lmodern substitute, babel/textalpha
stripped): **41 pp., 0 LaTeX errors, 0 missing-character warnings.**

**Anden Forelæsning (pp. 14–25, PDF 27–38): DONE.** ~3260 words. First batch done by a
dispatched subagent (see "The loop"), then independently re-verified in the main
conversation: `check.py` clean, compile 0 errors / 0 missing chars, and the p.18
letterspacing spot-checked against the scan — „Christendommen eensartet med Videnskaben,
Evangelietroen eensartet med Theologien“ is genuinely Sperrsatz, so the agent's call was
right. The skeleton's italic argument matches the printed p.14 heading verbatim; no
correction needed. `fides religiosa` / `fides historica` set `\textit{}` (antiqua).

**Three printer's defects in this lecture, transcribed as printed and logged in `%`
comments at each site** — this is why `check.py` now reports quote balance **+1** rather
than 0:
- p. 15: the Religious man's second speech has one opening `„` but two closing `“`.
- pp. 23–24: `„lad os kun indrømme` is opened and never closed; it simply stops.
- pp. 24–25: a single `“` closes both the inner and the outer quotation.

Expect `balance=1` from here on until another defect is logged. Do not "fix" it.

**Lectures III, IV and V (pp. 26–65): DONE.** ~10,999 words, transcribed by three agents
running **concurrently**, each to a fragment in `.parts/`, then spliced with `splice.py`.
This worked: `check.py` reports 65/174, no gaps, no dupes, braces 251/251. Independently
spot-checked in the main conversation — p. 55 „Skriften — hedder det — skal fortolke sig
selv.“ is genuine Sperrsatz with the interpolated „hedder det“ *not* spaced, exactly as
marked up.

- **III (26–37):** skeleton's argument had `consequent`; the printed p. 26 reads
  `conseqvent`. **Corrected.** Defects logged: p. 26 a closing `“` with no opener;
  p. 32 `Refomatorerne`; p. 35 a missing full stop.
- **IV (38–51):** argument matches p. 38 verbatim. First lecture with footnotes.
  Defects logged: p. 41 `lil` for `til`; p. 42 `medele` for `meddele`.
- **V (52–65):** argument matches p. 52 verbatim. Defect logged: the p. 57 footnote opens
  `„Weil` and never closes. Doubtful: `L.\ I.\ Rückert` — the Fraktur I/J is ambiguous;
  `I.` chosen. Only `De Wette` (p. 57) is antiqua; the other German names are Fraktur.

**Quote balance is now +1 and should stay there.** Arithmetic: +1 (lecture II) −1 (III)
+0 (IV) +1 (V). If it moves without a newly logged defect, something is wrong.

### ⚠ OPEN EDITORIAL QUESTION — footnotes
The print marks footnotes `*)`. The 7 footnotes so far are plain `\footnote{}`, which
renders as `1, 2, 3…`. Decide before the count grows: keep LaTeX numbering, or restore
`*)` (`\renewcommand{\thefootnote}{*)}` or `\footnote[symbol]`). Uniform now, so a global
change is still cheap.

### ⚠ FRAGMENTS MUST NOT BE NAMED `.tex` — this broke `make`
The repo Makefile discovers targets with `find texts -name '*.tex'`, so staging batch
fragments as `.parts/pp26-37.tex` made it try to build them standalone. A fragment has no
preamble, so `make` died with `! LaTeX Error: Missing \begin{document}`. Fixed three ways:
fragments are now `.texfrag`; `splice.py` refuses to run if it finds `.tex` fragments and
archives spliced ones to `.parts/spliced/`; and the Makefile excludes `*/.parts/*`.

Leftover `.aux/.log/.fls` from that failed build are still in `.parts/` — gitignored and
harmless; `make clean` clears them. So is `.parts/_scratch-delete-me.txt`.

**Note on the sandbox:** `make` cannot build this book (or any other in the repo) inside the
Claude sandbox, because `libertinus.sty` is not installed there — verified by failing an
untouched file the same way. That failure is environmental and says nothing about the
document. Use the `lmodern` substitution recipe in BATCH-AGENT.md for sandbox compile tests.

### ⚠ TWO TRAPS THAT PRODUCED FALSE CONCLUSIONS — both now documented in BATCH-AGENT.md
1. **The sandbox compile reports ~22 `Unicode character … not set up` errors for Greek.**
   These are an artefact of stripping `textalpha` for the sandbox test, *not* a defect.
   Check `grep '^!' log.txt | grep -v 'Unicode character'` is empty; map Greek to a
   placeholder to test the rest. Never delete Greek from the file.
2. **`glob('/tmp/pg*.png')[0]` returns a stale page.** `/tmp` is shared between agents and
   `009` sorts before `068`, so a spot-check can confidently verify the wrong page — this
   happened once here. Render with `mktemp -d` + `pdftoppm -singlefile`.

**7 markers remain** — lectures VI–XII. `grep -n "text to be added" transcription.tex`.

Next batches = **VI pp. 66–80 · VII 81–96 · VIII 97–111** (15/16/15 pp.). Note VII–VIII
cross the p. 83/84 page-map seam, where the offset changes from +13 to +15 — `pagemap.py`
handles it, which is exactly why nothing may hard-code an offset.

Note for a fresh session: the `bibliotek` folder is not mounted by default — request it
explicitly (host path `/Users/hhalvors/bibliotek`) before running any script, since
`pagemap.py` needs the scan to be readable. `BATCH-AGENT.md` tells the subagent to do this
itself.

## Skeleton
`transcription.tex` already carries all twelve `\chapter*` headings with the lecture
*arguments* (the long italic summaries) taken from the book's own Indhold, pp. 177–178.
**Caveat: those summaries were reconstructed from the ABBYY text layer of the contents
pages and normalised by hand; they have NOT been image-verified against PDF 190–191.**
Do that pass before the book is called finished.

Lecture page ranges (from the Indhold):
I 1–13 · II 14–25 · III 26–37 · IV 38–51 · V 52–65 · VI 66–80 · VII 81–96 · VIII 97–111 ·
IX 112–128 · X 129–143 · XI 144–158 · XII 159–174.
(The contents page prints VI as "66—86"; that is an OCR/typo artefact — VII begins at 81,
so VI ends at 80. Worth confirming against the printed page.)

## ★ HOW TO WORK THIS BOOK — read this before doing anything else

The cost of this job is **context replay**, not transcription. The rules from the
Religionsphilosophie harness apply, with one superseded — see the loop below:

1. ~~Fresh conversation every sitting.~~ **Superseded: dispatch each batch to a
   subagent instead.** See "The loop".
2. **Never read `transcription.tex` whole.** `python3 check.py` prints the resume
   page; `tail -60 transcription.tex` shows where you are.
3. **Twelve pages per turn, not two.**
4. **One `Edit` per batch** — all twelve pages in a single call.
5. **Zoom only on real doubt.** `spacing.py` already tells you where to look.
6. **Bookkeeping every ~20 pages**, not every batch.

### The loop — one subagent per batch, one conversation for the whole book

The reason the old rule demanded a fresh conversation was that the page images and the
OCR dumps accumulate and get re-sent on every later API call, so batch 15 was paying to
re-transmit batch 1. A subagent gives the same isolation without ending the conversation:
it starts cold, burns ~30k tokens of OCR and images in **its own** window, and returns a
~150-word summary. The main conversation therefore grows by a couple of hundred tokens
per batch instead of tens of thousands, and Hans never has to restart.

```
Dispatch a general-purpose subagent with the prompt body in BATCH-AGENT.md,
substituting FIRST/LAST/MARKER/LECTURE. Then, in the main conversation:
    python3 check.py          # cheap, text-only, independent of the agent's claims
```
**In the main conversation, never read a page image and never let `ocr.sh` output land
there.** That is the whole discipline; everything else follows from it.

174 printed pages ÷ 12 ≈ **15 batches**. Batches are independent — pages FIRST..LAST touch
exactly one marker line — so two or three agents can run concurrently if you want the book
finished in fewer sittings. Verify with `check.py` after each returns.

### Trust but verify
The subagent reports its own compile and `check.py` result. Re-run `check.py` yourself
anyway: it is a few hundred tokens and it is the one check that does not depend on the
agent's honesty about its own work. Spot-check emphasis on a page or two per lecture.

### Where this book DIFFERS from Religionsphilosophie
That book was Antiqua with poor OCR, so the image was the only witness and the
text layer was rejected outright. **This book is different and was re-tested:**

- **The Fraktur model reads it cleanly.** `ocr.sh` runs it and mechanically fixes
  this book's closed set of confusions. So the OCR carries the *words*, and the
  image only has to carry *structure* — paragraphing, footnotes, section rules —
  plus doubtful readings.
- Because of that, `twoup.sh` renders at **130 dpi grayscale, capped at 1800 px**
  (Religionsphilosophie used 160/2000). Confirmed legible on the pp. 1–2 spread.
- **`spacing.py` finds the letterspacing mechanically**, which is the thing OCR
  cannot see and the reason that book needed every page eyeballed. It fits a
  per-glyph advance width over the whole page by least squares and flags words that
  come out too wide, grouping adjacent hits into RUNs.

  **Validated twice against ground truth confirmed by eye:**
  - printed p. IV → recovers the prayer quotation „jeg takker Dig, Gud i Himlene,
    at Du ikke har fordret af et Menneske, at han skal begribe Christendommen!“
  - printed p. 2 → recovers the thesis, across the line break: „Christendommen
    (er) høiere end Videnskaben, (og) Evangelietroen ueensartet med Theologien.“

  A **RUN** is nearly always real emphasis. A **single?** is often noise (short
  words, and display headings like *Første Forelæsning*) — confirm those on the
  image. The PDF's own ABBYY layer (`pdftotext`) stays useful as a **second
  witness**: it fails differently from tesseract (it loses æ/ø: "sergeligt",
  "hændes"→"handes"), so where the two agree the reading is safe.

### Page markers
Convention: `% --- p. N ---` on its own line where printed page N begins.
`check.py` uses these for gap-detection and progress. The Forord carries roman
ones (`% --- p. III ---`), which check.py ignores.

### Each lecture prints its own argument
The long italic summary at the head of every lecture in `transcription.tex` is
**also printed at the head of that lecture in the book** (confirmed on p. 1), not
only in the Indhold. So verify each one against its own opening page as you reach
it — no separate pass over the contents pages is needed.

## OCR pipeline (rebuild each session; models don't persist — `batch.sh` does it)
```bash
cd /tmp && mkdir -p tessdata && cd tessdata
wget -q https://github.com/tesseract-ocr/tessdata_best/raw/main/script/Fraktur.traineddata -O Fraktur.traineddata
wget -q https://github.com/tesseract-ocr/tessdata_best/raw/main/dan.traineddata -O dan.traineddata
export TESSDATA_PREFIX=/tmp/tessdata
SRC="/sessions/<id>/mnt/bibliotek/Nielsen, Rasmus/1850-evangelietroen-theologien.pdf"
pdftoppm -f P -l P -r 300 -png "$SRC" /tmp/ro >/dev/null 2>&1
tesseract /tmp/ro-*.png stdout -l Fraktur --psm 6 2>/dev/null | sed -e 's/ſ/s/g' -e 's/œ/æ/g' | tr -s ' '
```
Two pages per bash call is safe. The `Fraktur` model is far better here than the PDF's own
ABBYY text layer, which systematically loses æ/ø ("sergeligt" for "sørgeligt", "handes" for
"hændes", "Religisse" for "Religiøse"). Keep the ABBYY layer (`pdftotext -f P -l P`) as a
**second witness** — where the two engines agree, the reading is safe; where they differ,
look at the image.

### Recurring Fraktur OCR errors in this book
`iffe`/`ife` → ikke · `ﬀal`/`\kal` → skal · `fritisfe` → kritiske · `sulde`/`ﬀulde` → skulde ·
`fan` → kan · `nof`/`Nofk` → nok · `fif` → fik · `beflageligt` → beklageligt ·
`besmgkke` → besmykke · `udtr9ffelig` → udtrykkelig · `Jronie`/`Jndsigelser` → Ironie/Indsigelser ·
`selo` → selv · `0g` → og · stray `’ ´ ˆ` accents on ordinary letters (drop them).

### Verification images
Render to the outputs folder and read them there (the sandbox `/tmp` is not visible to the
file tools):
```bash
cd /sessions/<id>/mnt/outputs && pdftoppm -f P -l P -r 200 -png "$SRC" pg
# then crop into 2–3 horizontal bands with PIL and Read the band files
```
200 dpi in bands is enough to see letterspacing.

## Conventions (as in the Brøchner playbook — follow it, not this file, for anything general)
- 19th-c orthography exactly as printed: Christendommen, Videnskaben, Theologie, Forsøg,
  hviIken→hvilken, aa, ø, `Existens`, capitalized nouns.
- Quotes: Danish „…“ low-high, as printed. Em-dash `---`.
- Letterspaced emphasis → `\emph{}`. **This is the thing OCR cannot see; it needs the image.**
- Latin → `\textit{}`: so far `reservatio mentalis` (p. VII), `propter iniquitatem temporum`
  and `in republica litterarum` (p. VIII).
- „en Anden“ (pp. VII–VIII) = Kierkegaard, unnamed. Leave as printed; do not gloss in the
  transcription.
- The Forord's opening block quote is from Kierkegaard/Anti-Climacus, *Sygdommen til Døden*;
  Nielsen names only "en christelig Psycholog, der kjender „Sygdommen til Døden“".

## Emphasis pass — outstanding on the Forord
Only **p. IV** has had its image checked (confirmed letterspacing on the prayer
quotation and on `personlig`). **pp. III and V–VIII still need the pass** — absence
of `\emph{}` there means "not yet checked", not "not emphasized". Now that
`spacing.py` exists this is cheap, but note it takes *printed body* pages, so the
roman front matter needs the PDF page passed by hand (Forord III–VIII = PDF 8–13):

```bash
SPACING_PAGES_ARE_PDF=1 python3 - <<'PY'
# quick one-off for the front matter
import spacing, tempfile
for pdfp in range(8, 14):
    with tempfile.TemporaryDirectory() as t:
        print(pdfp, spacing.flags(spacing.tsv_for(pdfp, t)))
PY
```

**One candidate already outstanding:** on p. IV the detector flagged a RUN
`Men strides` — i.e. „Men at \emph{strides} om Troen er dog kun menneskeligt“ may
be letterspaced in the print. It is *not* marked in the transcription yet. Check it
when doing the Forord emphasis pass; Nielsen letterspaces the
*stride for* / *strides om* distinction elsewhere, so it is likely real.
