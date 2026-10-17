# Danish → English translation playbook

Point a fresh Claude session at this file to translate any 19th-century Danish
book in this repo into English. It captures the workflow proven on Brøchner's
*Problemet om Tro og Viden* (1868), which is now **complete** (transcription +
translation, 182 pp., 0 errors). Use it as the standing method; keep a short
per-book **RESUME-NOTES.md** alongside it for state that changes batch to batch.

---

## 0. What you're doing

A book lives in `texts/<author>/<slug>/` and has two LaTeX files:

- `transcription.tex` — the Danish, in `book` class. **This is the source of
  truth for translation.** Translate FROM it, not from the PDF scan.
- `translation.tex` — the English. Built up over many sessions by filling
  markers (see below). Mirrors the transcription's structure 1:1.

If a book has no transcription yet, that's a *transcription* job, not a
translation job — different playbook (see the Brøchner RESUME-NOTES' OCR
pipeline section for that workflow). This file is about **translation**.

Work in **~10-printed-page batches**. After each batch: compile, give a short
report, and hand back. **The user commits and pushes — you never do.**

---

## 1. The batch loop

1. `grep -n "text to be added" translation.tex` → the markers, in reading order.
   Each looks like `% [text to be added: pp. X--Y]`. Also grep for
   `translation continues` — those are *continuation notes* marking a mid-section
   gap where translated text resumes; fill the gap, don't restructure.
2. Take the next marker. Find the matching Danish in `transcription.tex` (match
   the `\section`/`\subsection` heading and `\label`). Read the whole span,
   start heading to next heading.
3. If the span is much more than ~10 printed pages, do a coherent sub-chunk and
   leave/advance a `% [translation continues from p. N]` note at the seam.
4. Translate it (conventions in §2). Replace the marker via the `Edit` tool.
5. Compile with the sandbox recipe (§3). Expect **0 errors, 0 char-warnings**.
6. Report in 2–4 sentences: what section, page range, notable choices, the
   compile result (page count + 0/0), and markers remaining. Hand back.

Use the task list (TaskCreate/TaskUpdate) per batch: one task to translate, one
to compile/report. It renders as a progress widget for the user.

---

## 2. Translation conventions (keep these consistent across the whole book)

- **Quotes.** Danish „…" (low-high) and guillemets »…« / «…» → English curly
  doubles, written in LaTeX as `` ``…'' ``. (Foreign-language guillemet *terms*
  the author keeps as foreign — e.g. «plus ultra», «bonum est quia Deus vult»,
  «lazzi» — stay in guillemets as printed.)
- **Emphasis.** Danish `\emph{}` (letterspacing in the original) → keep as
  `\emph{}` (renders italic). Preserve every emphasized span — OCR/transcription
  often marks these; carry them all over.
- **Latin phrases** → `\textit{}` (e.g. `\textit{credo ut intelligam}`,
  `\textit{libera necessitas}`, `\textit{eo ipso}`, `\textit{per impossibile}`,
  `\textit{non liquet}`, `\textit{differentia specifica}`). Match the original's
  italicization.
- **Greek.** Copy the glyphs verbatim from the Danish (τέλος, μὴ ὄν, πίστις,
  γνῶσις, Νοῦς, Κόσμος, the Iliad tag, etc.). Translate the surrounding prose,
  not the Greek. Requires `\usepackage{textalpha}` in the preamble (see §4).
  Exception: where the author himself transliterates (e.g. an Antiquity section
  using `\textit{nous}`, `\textit{phronesis}`), keep the transliteration —
  match the author term-by-term.
- **The old "id est" mark `ɔ:`** → render `i.e.` in English. (Also `d.\ v.\ s.`
  → "that is"/"i.e.")
- **Em-dash** `---`. Section-break rules the book marks with a short centered
  rule → `\begin{center}---\end{center}`. Reproduce these at the same breaks.
- **Footnotes** → translate the note content, keep `\footnote{}` at the same
  anchor word. Danish footnotes are sparse — check each page's Danish for any
  `\footnote` and carry it. Keep work-title references (e.g. *Om den gode
  Villie* p. 28) as the author cites them; keep volume/page refs verbatim
  (e.g. `Gr. L. II, 442`).
- **Proper names** unchanged (Spinoza, Hume, Strauß, Kierkegaard, Martensen…).
  Danish book/work titles in footnotes: leave in Danish.
- **Numbered run-in heads** like `1.~\emph{Med Hensyn til…}` → keep the same
  form: `1.~\emph{With Respect to…}`. Enumerate lists with `\arabic*)` etc. need
  `enumitem` (see §4).
- **Register.** Scholarly, moderately literal but readable English. Brøchner's
  syntax is long and nominalized; it's fine — and often clearer for matching —
  to keep compound coinages (essence-willing, knowledge-determination,
  will-concentration, being-for-itself). Match the done sections' feel.
- **Headings / `\label{}`.** Keep labels and structure mirroring
  transcription.tex 1:1. Verify each heading against the FINAL transcription
  before filling — some skeleton headings were drafted against an earlier state.

### Two structural gotchas that recur
- **Section intros.** A `\section{}` often has an intro paragraph in the Danish
  *before* its first `\subsection{}`. The translation skeleton may jump straight
  from section heading to subsection — insert the intro paragraph in between.
- **Bridge paragraphs.** Watch for a paragraph the print places at the end of one
  section that a skeleton accidentally floated to the next chapter's intro. Put
  it where the Danish has it so the translation mirrors transcription 1:1.

---

## 3. Sandbox compile / verification recipe

The sandbox lacks `libertinus`; substitute `lmodern` and strip the Greek/danish
bits just for the check (do NOT put these substitutions in the real file). The
bash mount path is **session-specific** — find it with `ls /sessions/*/mnt/`
each session; below it's written generically.

```bash
cd /tmp && mkdir -p verify && cd verify
SRC="<sandbox-path-to>/translation.tex"   # …/mnt/danish-texts/texts/<author>/<slug>/translation.tex
sed -e 's/\\usepackage{libertinus}/\\usepackage{lmodern}/' -e '/libertinust1math/d' \
    -e '/textalpha/d' -e 's/\\usepackage\[english\]{babel}/\\usepackage{babel}/' "$SRC" > t.tex
python3 - <<'PY'
import re; s=open('t.tex',encoding='utf-8').read()
s=re.sub(r'[Ͱ-Ͽἀ-῿]+','[Gr]',s)   # Greek replaced ONLY because sandbox lacks textalpha
open('t.tex','w',encoding='utf-8').write(s)
PY
pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1; pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1
grep -o 'Output written.*' l.txt
echo "char-warnings:"; grep -ic 'not set up\|missing.*character' l.txt
echo -n "errors: "; grep -c '^!' l.txt || true
echo "markers left:"; grep -c 'text to be added' "$SRC"
```

Expect `0` char-warnings and `0` errors. (`grep -c` exits 1 when it finds zero —
that's the *good* outcome, not a failure; the `|| true` keeps the script going.)
If `pdflatex` errors with "Missing number, treated as zero" at an `enumerate`,
the preamble is missing `enumitem` (see §4).

If the sandbox lacks `lmodern` too (cloud sandbox, 2026-10-03), drop the font packages and replace the babel
line with `\providecommand{\foreignlanguage}[2]{#2}` instead.

On the user's real machine the Danish compiles with `libertinus +
libertinust1math`; the English is fine with `lmodern`. `textalpha` handles the
real Greek there. Don't add the sandbox substitutions to the actual file.

---

## 4. Preamble checklist for a translation.tex

When starting a new book's `translation.tex`, make sure the preamble has:
- `\usepackage[utf8]{inputenc}`, `\usepackage[T1]{fontenc}`
- `\usepackage{libertinus}` + `\usepackage{libertinust1math}`
- `\usepackage{textalpha}` — for real Greek glyphs
- `\usepackage[english]{babel}`
- `\usepackage{enumitem}` — needed for `\arabic*)`-style lists (easy to forget;
  it caused the one mid-project compile failure on Brøchner)
- `geometry`, `setspace`, `fancyhdr`, `hyperref`, `microtype` as desired

---

- Title page credit: **"Translated from the Danish"** -- no translator's name (Hans's standing preference,
  2026-10-03: the translations are made with heavy machine assistance). Not "by [HH]", not "by Hans Halvorson".
- `\opage{N}` (a `\marginnote`) followed directly by `[` takes the bracket as marginnote's optional shift
  argument and fails ("Missing number"): write `\opage{N}\relax[...` (Spinoza p. 165, 2026-10-03).
- A list of terms in the back matter: keep the print's order and page numbers (they are the original
  pagination, given in the margin; say so in one bracketed line) and give the author's Danish
  equivalents in italics after the English term.

- A `%` comment put inline in the middle of a paragraph swallows the rest of its line, and the newline
  too, so the next line's first word is glued on without a space: put such a comment at the END of a
  physical line, with a space before the `%`, and start the text again on a new line (Den store Humor,
  2026-10-04: three slips, all caught by reading the lines with ` %` before the build).
- Quotations: what the author quotes in a foreign language stays in it; what he quotes in Danish
  translation is translated from his Danish, unless the English original is certain (Swift, Carlyle),
  marked at the site; Danish verse is translated in the text with the Danish in a comment below it.
- Names, titles and citation numbers as printed (Wolf, Fontaine, Rhode, "King Lear V, 3, 203"); a
  silent correction of a citation is a change to the text of record.
- Translating is a full reading of the Danish: keep a list of odd spots as you go (specks read as
  ' . , * inside words, stray accents, words glued or split, paragraph breaks at page turns), read the
  doubtful ones at the image, and fix them by patch in the transcription before the translation is
  called done (Den store Humor: 121 faults and 18 misprints after OPEN 0).

## 5. Page-offset (per book)

Find the constant offset between **printed page** and **PDF page** once, by
comparing printed headers in the scan to the PDF page numbers (don't trust OCR
`[side N]` markers — they drift). For Brøchner it was **PDF = printed + 9**.
Record the book's offset in its RESUME-NOTES.

---

## 6. Finishing a book

When `grep -c 'text to be added'` and `grep -c 'translation continues'` both
return `0`:
1. Final sandbox compile → confirm pages, 0/0.
2. In `catalog.yaml`, set the book's section `status:` to `complete`.
3. Tell the user to compile both PDFs locally with the real fonts and confirm the
   Transcription + Translation links resolve.
4. User commits/pushes. You don't.

### 6a. When the transcription changes after the translation (lesson 2026-10-03)

*Den menneskelige Tanke* was translated 2026-06-30 to 07-02 from transcription
commit 3d9b759; the transcription was collated against the scan afterwards
(2026-09-12) and a missing page (134) restored. The English silently kept the
old readings: 61 passages were wrong, some badly (p.143 "the other nine
categories" for *de noget utydelige sex sidste Kategorier*; p.328 "are
concluded" for *ikke ere afsluttede*; p.376 "sorrow" for *Sejr*). So whenever a
transcription is repaired after its translation exists:

1. Note the commit the translation was made from (put it in the translation's
   header when you translate).
2. Use `ebook-method/collate/xcheck.py BOOK --review --from <commit or .epub>`
   (record the source in `ebook-method/collate/xcheck-sources.tsv`; for a selection of an
   e-book, `PATH.epub::FILE-REGEX::NOTES=a-b`, see ebook-method/README.md), then
   `--apply FIXES.txt --write`. What it does by hand, for the record: diff
   that commit's transcription with the current one word by word. Sort
   the changes by script, not by eye: markup-only, punctuation-only, and the
   rest. Read EVERY change in "the rest" — a hand-picked "meaning-relevant"
   subset missed 28 real errors here (kun/kan, har/vare, til/vil are one
   letter apart). Italic changes matter too: names un-italicized, stress
   italics, title extents in footnotes. For each change print the Danish
   context and the English window at the proportional position *within the
   printed page* (between the two `\opage` markers); when the window misses,
   grep the English for a key phrase.
3. Decide each one, apply the fixes with one checked script (every old string
   must match exactly once), back up first, compile, and record the repair in
   the translation's header and the ledger.
4. Pages added to the transcription must be translated and get their `\opage`
   (and an anchor line in `ebook-method/BOOK/anchors-en.txt`).

Cost: about 80 entries to read for a 392-page book; far cheaper than
re-translating.

---


### 6b. Translate from the text of record (2026-10-03)

When the printed original is itself a translation the author authorized (Personlighetsprincipen i
filosofin: lectured in Danish, published only in Irene Leopold's Swedish), transcribe THAT print and
translate from it, not from a later retranslation (Blegvad's Danish of 2013 stands one remove further
off, and its editor's section titles are not Høffding's). Keep the superseded English as a .bak and say
in the new header what it replaces and why. Where the print's wording contradicts its own argument
(möjliggör for omöjliggör), translate the sense, mark the print PRINTED AS IS in the transcription and
say so in a comment in the English.

### 6c. The translation is a second reading of the transcription (Spinoza's Ethica, 2026-10-04)

A book collated to OPEN 0 against a second OCR still had 15 unmarked misprints and 14 small faults, all
found by translating it: faults both OCRs share (a stop read for a comma, "21.73" for "21. 73", "logisk-
matematiske" broken at the line end, a lost opening quote), layout the draft guessed (a false paragraph
break, one outline item set as a centred line, a Greek label left roman), and misprints nobody had read
(kam for ham, knn, polt., en en). So:

1. While translating, keep an odd-spots list (page, the word, the doubt) beside the parts; don't stop to
   check each one.
2. At the end, read them at the image in one or two sheets: a short script crops the line round each
   word's box in the scan's text layer (pdftotext -bbox) at 200 dpi, labelled with the page and the word.
   One sheet held 15 spots legibly.
3. Fix the transcription through the book's POST patches (draft.py --post), never by hand, so that the
   pipeline still rebuilds it; misprints get a PRINTED AS IS marker, the English a comment.
4. A fix made by POST leaves a new disagreement with the collation witness: decide it **T** in decisions.tsv
   (P means "take the witness's reading and mark it PRINTED AS IS", not "keep the print"), and see that
   `check.py BOOK --unapplied` prints no UNAPPLIED line and OPEN 0. A page-scoped POST patch sees only its own
   page, so a false paragraph break at a turn is mended as two patches, one on each side of the marker
   (Om Grundlaget for den humane Ethik, 2026-10-05).
   Small dots and commas between words, which both OCRs read as punctuation, are often risen spacing or specks:
   settle them at 600 dpi, not 300 (Om Aandsdannelse, 2026-10-06: a full-size stop is PRINTED AS IS, anything
   smaller is not transcribed; 9 of 55 spots were such dots).  A clean check.py --italics says nothing about bold:
   look for it on the sheets (one bold „først“, p. 66, found only there).  A misprint corrected by a collation
   DECISION (not a POST patch) is undone by changing that decision to T, not by a POST patch on top of it.
5. Check the footnotes page by page, not only in total: split the English at `\opage{N}` and the Danish at
   its page markers and compare the counts per page.

## 7. Per-book RESUME-NOTES template

Keep a short `RESUME-NOTES.md` in each book's folder. Minimal shape:

```
# <Author> — <Title> (<year>): translation resume notes

Source of truth: transcription.tex (Danish), COMPLETE/▢ in progress.
Page-offset: PDF = printed + N.
Scan: ~/bibliotek/<author>/<file>.pdf

## CURRENT RESUME POINT
Next marker: <% [text to be added: pp. X--Y] — section name>.
<anything unusual about the next span: long quotes, footnote inventory,
 a section intro to fold in, a continuation note to advance, etc.>

## DONE so far (don't redo)
- <front matter, chapters/sections filled, with page ranges>

## Conventions
See ../../../TRANSLATION-PLAYBOOK.md (the standing method). Book-specific
deviations: <e.g. author transliterates Greek in section Z; work-title
abbreviations used in footnotes; etc.>
```

That's it. Read the playbook, read the book's RESUME-NOTES, grep the markers,
and start the batch loop.

### 6d. A whole book by translator agents (Mindre Arbejder, 2026-10-05)

`ebook-method/mindre-arbejder/` (TRANSLATOR-BRIEF.md, tr_template.tex, tr_build.py): each agent gets one or two essays
(10-18k Danish words), writes a LaTeX part with every \opage and footnote of its stretch, and an odd-spots TSV;
tr_build.py splices the parts and checks markers (once, in order) and footnotes per page against the Danish.
Measured: ~130-145k tokens per agent (base ~60k), 1.23M for 243 pages incl. one agent revising three older
translations (283k).  Grep the result for a line ending in `%` before a page marker: three translators glued a
word to the next page's first word that way (`just%` / `\opage{114}as`).  The odd spots repay reading: 59 of 138
read at the image gave 5 transcription errors that a three-witness collation had passed (Wikisource and the layer
agreeing on „tælles“ for „fælles“; „paa vist“ split at a Wikisource line end; two run-over notes never collated
word by word) and 6 unmarked misprints.  Screen the list by hand first: most entries are the period's spelling.

### 6e. A formula-heavy Fraktur book by translator agents (Mathematik og Dialektik, 2026-10-06)

Before dispatching, read the compiled Danish at a few page turns: the transcription had a false paragraph break at ~100
of 146 page turns (the page-fix splice added a blank line after every rewritten page) and 29 line-end hyphens, which the
translators would have mirrored 1:1; fixed in finish.py and rebuilt.  Split the book only where a page opens with a
heading, a paragraph or a new sentence, so no sentence is shared by two translators, and let tr_build.py decide the
join (blank line or not) from the Danish.  Tell the translators to list only what could be a transcription fault and
to leave the period's spelling alone: 114 spots, nearly all real.  Read at the image (spotsheets.py, two rounds, the
second for crops that boxed the wrong word): 52 transcription faults (lost words: „og den“, „i“, „. Et Par“, „. Enhver
uafbrudt“; x read r in Tilvæxt four times; Ø read D in Øieblik 19 times; a doubled formula pair; a note set as body text
over three pages) and 20 misprints confirmed.  The translators also drifted in formulas (a "lim" pulled into math,
punctuation moved in and out of $...$): compare the formula sequence of each part with the Danish by script.
Measured: ~92-140k tokens per agent for 13-21 pages (25-44k Danish characters), 1.06M for the book.
Formula second reading (same book, 2026-10-07): the OCR witnesses vouch for little in mathematics (329 of 758 non-trivial
formulas agreed at the letters-and-digits level), so the triage cut less than hoped.  Proof sheets that set the scan crop
over the typeset formula found few faults (4 in ~430, plus em dashes inside math), but anchor-located crops missed the
formula 15% of the time and readers then compared the wrong line (one false DIFFERS): check every DIFFERS at the image,
and budget a page-view round for the misses.  Cost 0.98M for 429 formulas.

### 6f. Brøchner's Spinoza by translator agents (2026-10-07)

`ebook-method/brochner-spinoza/` (TRANSLATOR-BRIEF.md, tr_parts.py, tr_template.tex, spotsheets.py): tr_parts.py
cuts the Danish at chapter heads by anchor (no line numbers), extracts each part, and on `build` checks markers,
footnotes AND `\setcounter{footnote}{0}` per page (a book whose notes restart per printed page), \emph per part and
bare-% line ends.  Brief the reset as `\opage{N}\setcounter{footnote}{0}word` (no `%`), and give every translator
the chapter titles and the book's Latin convention (here roman, as printed).  Measured: 162k tokens for 8.1k Danish
words in the pilot, ~1.0M for 58k words / 188 pp.  A pilot is worth it: it settled one convention (S. -> p.) before
the wave.  Odd spots: 30, all read at the image on four small sheets; 1 transcription error (`V.,' for `V,') and
17 unrecorded print irregularities, the rest Brøchner's syntax.  spotsheets.py needs multi-word keys (a single
word matches the wrong instance), and a translator's page for a note that runs over is often the mark's page,
not the page where the words stand (p. 112 -> 113); a page given off by one also occurs (24 -> 23).


### 6g. Nielsen's Speculative Logic by five translators, with a glossary first (2026-10-07)

`ebook-method/speculative-logik/` (GLOSSARY.md, TRANSLATOR-BRIEF.md, tr_extract.py, tr_build.py, tr_template.tex, prescreen.py,
trspots.py, trpost.py).  A technical book (Hegelian logic) needs its terms fixed BEFORE the wave: draft the glossary from
the transcription (Danish term, English, one example with its page; check the repo's earlier translations of the same
author, which may disagree with each other), show it for approval, and point the brief at it.  Fix the headings' English
in it too, so every part uses the same.  Cut parts by anchor, at headings, two of them mid-page (tr_extract.py PARTS).
Measured: 158–171k tokens per translator for 8.8–10.5k Danish words (818k for 47k words, five agents).
Before dispatch, run two cheap checks on the "finished" transcription: words per page against tesseract (one page, p. 81,
had lost its whole text to the notes step) and prescreen.py (doubled words and marks left by --apply, o: for ɔ:, words
split into letters, heading debris).  Tell the translators the prescreen list exists so they do not list it again.
The odd spots: 265 from the translators + 137 by script.  Classes went by rule (false paragraph breaks inside a sentence,
sheet signatures and folios in the text, compound hyphens, doubled marks) or by a read sample (ɔ:, Følge, ꝛc.: 3–5 of 3–5);
241 were cropped (trspots.py) and read blind by two Sonnet readers (307k): 204 corrections, 12 more misprints.  Crop
sheets: FOUR crops a sheet (a 16-crop sheet is shrunk below legibility when viewed), id and page only on the label, the
text-block width; where the crop cut the line start, the three OCR readings settled the cut part.  Rendering on the device
is slow (~5 s a page at 220 dpi) and a background job dies with the shell: render in loops under the time limit.
The translators had mirrored the garbles (x + y + 2, „1, 2, 2“, heading debris translated as text): after correcting the
Danish, correct the English at once, by a checked list of exact replacements (55 here).  tr_build.py now also compares
paragraph breaks per page: it caught 24 false breaks the translators had mirrored.  In the compile test never redirect
pdflatex's output to NAME.out: that is hyperref's bookmark file and the second run fails on it.

### 6h. Bringing a "finished" transcription's residue down (speculative-logik, 2026-10-07)
After a sampled page check (TRANSCRIPTION-PLAYBOOK) showed 2.4 word errors / 1000 words, two cheap sweeps halved it (run 2:
1.2 / 1000) for ~250k agent tokens: (1) ocrsweep.py: places where two of four OCR readings (three tesseract models + the
library's layer) agree on an ATTESTED word the transcription lacks or differs from; ~30 plausible hits, 17 real, most of
them lost words and lost enumeration marks a) b) c); (2) boldsweep.py: words measured bold but never marked (the emphasis
step loses words divided at a line end).  Look at every hit in a crop before patching.  Three lessons about my own process:
spots flagged in an earlier round must be closed by script at the end (grep each flagged string; pp. 3 and 37 marks and
„Hceccei“ were flagged and then forgotten); a page-scoped regex patch whose old text spans a newline eats blank lines; and
after any Danish correction grep the English for the old garble (translators mirror garbles: „Ovantum“, „(- 0)“).

### 6i. Om Skjæbne og Forsyn by two translators (2026-10-07)
`ebook-method/skjaebne-og-forsyn/` (GLOSSARY.md -- three ◆ choices put to Hans with the multiple-choice question tool
before dispatch: Scripture in KJV wording where Nielsen's Danish matches it; Tilfælde = accident / Tilfældet = chance;
Mennesket = man -- TRANSLATOR-BRIEF.md, tr_extract.py, tr_build.py, tr_template.tex).  Two parts cut at the heading of
part C (mid-page 48): 7.6k and 6.0k Danish words, 127k and 108k tokens.  prescreen.py before dispatch found two words the
collation rule `tokens` had glued on letter-spaced lines (tesseract drops the space there): check rule-joined words whose
result is unattested.  The 36 odd spots were read in the main session from line crops, 9 to a sheet (cheaper than a reader
agent at this size); match the crop by a distinctive word in tesseract's lines, not by fuzzy line similarity (half the
first sheet showed the wrong line).  A translator mirrored a misprint's stray point into English („the rich man. has“):
after marking misprints, grep the English for `[a-z]\. [a-z]` and `,.`.

### 6j. Høffding's Erindringer by twelve translators (2026-10-07)
`ebook-method/erindringer/` (TRANSLATOR-BRIEF.md, tr_parts.py, tr_template.tex, oddsheets.py).  A memoir, ~104k Danish words:
12 parts cut at page turns where a chapter or a paragraph begins (tr_parts.py PARTS by page number), ~6.5-12k words each,
~120-150k tokens each (~1.6M in all; a pilot of two first).  No glossary file: the brief fixes ~30 institutional and
philosophical terms (Videnskabernes Selskab, Studentersamfundet, Æresboligen, Docent, Personlighed, Livsanskuelse ...) and
American spelling.  Each part checked by script against the Danish per printed page: markers, footnotes, counter resets,
paragraph breaks, \secrule / \whiteline / quote counts -- 0 differences.  The page-turn convention of this book's
transcription (`% --- p. N ---` / `\setcounter{footnote}{0}%` / `\opage{N}word`) was copied verbatim by the translators
without trouble.  145 odd spots, all read at the image (two blind readers on 18 sheets of 8 crops, ~256k): 7 transcription
faults, 75 unmarked misprints; four crops located the wrong instance of a word (fuzzy layer match): check a reader's BOX
against the spot before deciding.

### 6k. Høffding's Philosophien i Tydskland efter Hegel by eleven translators, in one run (2026-10-09/10)
`ebook-method/tydskland-efter-hegel/` (GLOSSARY.md, TRANSLATOR-BRIEF.md, tr_parts.py, tr_template.tex, oddsheets.py).  Glossary
settled without a round of approval (Hans: "settle it yourself"), the unsure choices marked ◆ for later review; term choices the
translators reported after each batch were appended to the glossary ("Settled by the translators of ch. 1-3") and so reached
the next batch.  Pilot one part (front matter + ch. 1, 4.9k words, 111k), then batches of 3-4 by chapter.  Measured: 1.57M for
93k Danish words / 325 pp. (118-188k per part of 5.7-11.7k words: ~55k fixed + ~11 tokens per Danish word; the estimate made
from the pilot and 6g/6j was 7% high).  Lessons:
1. **Before the wave, scan the transcription for blank lines inside a sentence** (a blank line after a text line with no closing
   punctuation, or before a lower-case word): 13 candidates, 11 real, in a book collated to OPEN 0.  Translators mirror them.
2. **A translator is the only reader who reads the text as a whole**: one found that a whole-page reading set by PAGESET had run
   on into a second copy of another page's reading (p. 143 carried 34 lines of p. 139).  No collation sees that (both copies are
   "right").  Mend at the source (the PAGESET entry), not by a POST patch, and grep every page-set text for the readers' page
   dividers ("== PAGE").
3. **The odd spots after a "complete" transcription are mostly real**: 200 listed, 102 transcription faults and 60 misprints at
   the image (unclosed quotation marks ~20, specks read as points ~15, words split or glued at a line end ~15, letterspacing
   missed 4, o: for ɔ:, a straight ' for “).  Two blind Sonnet readers, 6 crops a sheet, 270k for 200 crops, controls 5/5;
   the fuzzy locator boxed the wrong line for ~10%: re-crop those from a distinctive word and read them in the main session
   (full width, 2/3 scale, ~3k tokens a sheet of 6).  Small marks: a small mark where a comma belongs = a comma with a worn tail;
   where no punctuation belongs = a speck, not transcribed.  Doubled words at a line turn (og|og) were all the print's.
4. A misprint on a page set whole (PAGESET) cannot be marked by MISPRINTS at --emit: draft.py now has POSTMIS, applied at --post.
5. tr_parts.py anchors must not contain markup a later fix may add (the section head anchor broke when \emph was added to it).
6. After mending the Danish, rebuild the parts' check (tr_parts.py build) and mend the English by a checked list (each old
   string once); add a `% print:` line at the top of each page with a newly marked misprint.

### 6l. Høffding's Psykologiske Undersøgelser by five translators (2026-10-09)
`ebook-method/psykologiske-undersoegelser/` (6k's tools copied).  ~46k Danish words in 5 parts of 7.7-10.7k, a pilot
then four in parallel: 118-138k tokens each, ~665k in all.  The transcription was made the same day by the e-book
method and gave few odd spots (33, ~14 real).  Two lessons: (1) tr_parts.py's quote check must count only the print's
OPENING mark: this print opens with « and closes with », so counting both doubled every Danish count; (2) the odd spots
caught one of my own wrong crop decisions (knude/kunde) and stray marks the e-book adds („,.“, a „. “ opening a note),
which the letter alignment cannot see because it compares letters only.

### 6m. Nielsen's Om Begrebet Nøiagtighed by two translators (2026-10-10)
`ebook-method/begrebet-noiagtighed/` (GLOSSARY.md, TRANSLATOR-BRIEF.md, tr_extract.py, tr_build.py, tr_template.tex).  The
title term was put to Hans, who asked which concept Nielsen means: the text decides (pp. 51-52 tie Nøiagtighed to the
essential relative to a purpose and to clarity/distinctness/completeness, and reject reducing it to right/wrong), so
Nøiagtighed = precision, not accuracy (correctness) -- quote the passages with page numbers when proposing a key term.
Two parts cut where a page opens a paragraph (p. 29); a note running over pp. 28-30 stays whole in part 01.  160k + 150k.
Formulas copied byte-exact and counted by tr_build.py (`$`, `\[`).  46 odd spots: one real misreading of the Danish
(„og at,“ = „og ak,“), the rest quotation-mark drift and the print's own forms.  After a Danish fix, mend the English by
exact replacement and rebuild (`$o$` → o, \textit{arc (cos-x)} → math, a misplaced `% print:` note).

### 6n. Nielsen's Om Betingelserne for en kraftig Villie by four translators (2026-10-12)
`ebook-method/betingelserne-villie/` (GLOSSARY.md: the title and the triad drive-will / reason-will / spirit-will put to Hans
first, since the earlier Nielsen translations disagree -- instinctive/rational will in religionsphilosophie, drive-will in
videnskabslaere).  Parts cut at lecture openings (each lecture begins on a new page): 7.1k, 7.5k, 5.4k, 5.8k Danish words,
105-119k tokens each, ~440k in all.  The 39 odd spots: checked first against the 1884 resetting's text (most were the
print's own forms: Charakteer-, Chlotaldo, opulmende, Mrc.), then 9 real faults mended by POST patch -- three false
paragraph breaks, a layer line put out of order (p. 20), a word doubled by the collation (p. 82), a lost hyphen, two specks.
Mend the English at the same spots by exact replacement before tr_build.py --write.

### 6o. Nielsen's Om Phantasiens Magt by four translators (2026-10-12)
`ebook-method/phantasiens-magt/` (GLOSSARY.md: Phantasie = imagination and the title put to Hans first; the earlier Nielsen
translations had both "imagination" and "fantasy").  Parts cut at lecture openings: 6.9k, 7.5k, 4.6k, 4.4k Danish words,
102-136k tokens each, ~450k in all.  The 40 odd spots were all read at the image in the main session (two 16-crop zoom
sheets): 16 real faults mended by POST patch -- a word the layer lost at a line end (p. 41, where the translator had put
[\dots]), four false paragraph breaks from pencil in the margin, raised specks both OCRs read as stops -- and four
misprints marked; the rest were the print's.  Mend the English at the same spots (exact replacement) before
tr_build.py --write, and add `% print: … (misprint)` at the line end for each new PRINTED AS IS.

### 6p. Nielsen's Gamle og nye Propheter by six translators (2026-10-12)
`ebook-method/gamle-nye-profeter/` (GLOSSARY.md: the title, Nyrationalisme = neo-rationalism, Opgjørelse = Reckoning,
Troessamvittighed = conscience of faith put to Hans first).  Parts = the six lectures, 4.3-5.1k Danish words, 105-119k
tokens each, ~670k in all (five at once, then the sixth).  47 odd spots, all read at the image in the main session (zoom
sheets zo-01..03, zq): 21 real faults mended by POST patch (TRANSCRIPTION-PLAYBOOK §6, Gamle og nye Propheter), the
English mended at the same spots.  A term the glossary omits gets the translators' own word: Phantasie came out as
"fantasy" twice -- carry the house terms of earlier books (Phantasie = imagination) into every Nielsen glossary.

### 6q. Nielsen's Om Liv og Haab by six translators (2026-10-12)
`ebook-method/liv-og-haab/` (GLOSSARY.md: the title, Oplevelse/Erfaring = experience, Allivet = the universal life put to
Hans first).  Parts = the six lectures, 4.3-4.6k Danish words, 91-103k tokens each, ~595k in all (five at once, then the
sixth).  21 odd spots, all read at the image (zoom zo, zz-par): 13 real faults mended by POST patch, two misprints marked,
the English mended at the same spots (exact replacement) before tr_build.py --write.  A translator met „Lykke“ as luck
and used "fortune" there: give such a split in the glossary from the start.  tr_build.py had the last page of the book
it was copied from hard-coded (`range(1, 113)`): now `C_LAST`; set it per book.

### 6r. Nielsen's Om Samfundets Vilkaar by six translators (2026-10-12)
`ebook-method/om-samfundets-vilkaar/` (GLOSSARY.md: the title On the Conditions of Society, folkelig = popular, the
constitutional names kept in Danish with Grundloven = the Constitution, myndig/umyndig/Myndling/Formynder = of age /
under age / ward / guardian, put to Hans first).  Parts = the six lectures, 3.8-4.7k Danish words, ~95k tokens each,
~575k in all (five at once, then the sixth; Sonnet).  39 odd spots, all read at the image (zoom zo-01, zo-02): 8 real
faults mended by POST patch, 7 misprints marked, the English mended at the same spots.  A translator who italicises
the glossary's foreign names breaks tr_build.py's \textit count: say "roman" in the glossary.  One translator wrote its
odd-spots file beside tr/ instead of in it: look for `odd-*.tsv` in the book's ebook-method folder too.

### 6s. Nielsen's Folkelige Foredrag by ten translators (2026-10-12/13)
`ebook-method/folkelige-foredrag/` (GLOSSARY.md: the title Popular Lectures, Folkekirke = the People's Church, Folke-Aand /
Folketro / Folkelærer = the spirit / faith / teacher of the people, Gudsdom = judgment of God, put to Hans first; Grundlov
= the fundamental law in lectures I-III, the Constitution in VII).  Parts = the nine lectures and the Festtale, 2.3-4.9k
Danish words, ~96k tokens each, ~960k in all (two batches of five; Sonnet).  77 odd spots, ~40 read at the image: ~15
transcription faults mended by POST patch (specks, thin spaces, both-OCR misreads, four f's with an uninked head), the
English comments mended at the same spots.  Lecture heads here are heading + place line only (the titles live in the
Indhold): the template takes the PDF-outline titles from a \lecturetitleN list, so nothing unprinted enters the collated text.

### 6t. Nielsen's five essays in For Ide og Virkelighed 1869 by twelve translators (2026-10-13)
`ebook-method/for-idee-1869/` (GLOSSARY.md: the five titles, Virkelighed = reality, Grund(e) = ground(s), Undervisning =
instruction, Dannelse = cultivation, Sindsformørkelse = darkening of the mind, put to Hans first).  Parts cut at page turns
where no word is broken (tr_extract.py checks the anchors in each essay's own transcription.tex): 12 parts of 3.3-5.2k
Danish words, ~86-113k tokens each, ~1.17M in all (5 + 5 + 2; Sonnet).  tr_build.py builds the five translation.tex files and
checks each part (opage, notes, paragraph breaks per page, \emph, \textit, \essayhead, \signature, quote, \\).  79 odd
spots, ~60 read at the image: ~15 transcription faults mended (uninked f heads, a lost dash, the verse of p. 414, false
paragraph breaks at page turns), the English mended at the same spots (exact replacement) before tr_build.py --write.


### 6u. Nielsen's Propædeutik og Logik 1868–69, the new pages (2026-10-13)
`ebook-method/propaedeutik-1868/` (GLOSSARY.md: Ideelære = doctrine of the idea, Ideernes Logik = logic of ideas,
Oversigt = Synopsis put to Hans; the rest = the Grundideernes Logik glossary).  ~4.6k Danish words translated in the main
session.  Where a page is the SAME TYPE as an earlier book (p. 81 to »B.«, p. 89 from »1) Ordet og Gud«, pp. 263-264
to »C.«), that book's English was taken verbatim, so the same Danish reads the same in English; a continued footnote
from a page not translated here is set with \contnote (no mark).  Check paragraph counts per page against the Danish
by script (only \setcounter artefacts differed).

### 6v. Nielsen's eight essays in For Ide og Virkelighed 1870–73 by fifteen translators (2026-10-14)
`ebook-method/for-idee-1870-73/` (GLOSSARY.md: Aandsvirkelighed = Spiritual Reality, sund Menneskeforstand = Sound Human
Understanding, Videnskritik / Troeskritik = criticism of knowledge / of faith, Under(et) = miracle (Mirakel too),
Forkjærlighed = preferential love, put to Hans first; the rest from the 1869 glossary).  Aandsvirkelighed is ONE
translation.tex in two parts: tr_build.py sets the English title page of Bind 5 before Part II, and each essay opens with
its own volume's title page in English.  15 parts of 2.9-5.1k Danish words, ~88-107k tokens each, ~1.45M in all (pilot 1,
then 5 + 5 + 4; Sonnet); all 15 passed tr_build.py's checks at once.  74 odd spots, ~50 read at 300-dpi zooms (zoom.py):
13 transcription faults and 9 false paragraph breaks at page turns (a line ending without a stop, the next page opening
with a capitalised noun -- the 1869 rule saw only lower case; draft.py now joins both) mended in the Danish by
rebuild.sh, the same paragraph joins made in the English fragments, then tr_build.py --write.  LESSON: a speck beside a
word is read by ALTO or the readers as a quotation mark, ~ or ‘; the translator, who sees the mark opens nothing, finds it.

### 6w. Høffding's Moderne Filosofer by six translators (2026-10-14)
`ebook-method/moderne-filosoffer/` (GLOSSARY.md from the earlier Høffding glossaries; put to Hans first: det Usondrede /
Sondring = the Indistinct / distinction, Gentagelse = recurrence, Overmenneske = overman).  Six parts cut at chapter or
paragraph starts on page turns (tr_parts.py), pilot 1 then 5, ~0.83M tokens in all; the parts were made and checked in
the cloud workspace while the device was offline, then written to `ebook-method/moderne-filosoffer/tr/` and built with `tr_parts.py build
--write` (page markers, endnote marks and paragraph breaks per page vs the Danish: all OK).  117 odd spots, ~70 read at
the image: 10 transcription faults (last.tsv), the rest misprints, now listed PRINTED AS IS.  LESSONS: (1) a glossary
term must name its VARIANTS: one translator met Nietzsche's „Genkomst“ and rendered it „return“ beside „recurrence“ for
„Gentagelse“; grep the English for every variant of a key term.  (2) A dropped brace in one fragment (an unclosed
\textit) compiles into a run of italics, not an error: compile each fragment's build and compare the \textit counts with
the Danish (tr_parts.py does).  (3) Where the Danish set a dash inside a heading or ran two notes together, the
translator followed it; fix the Danish, then the English the same way.

### 6x. Høffding's Oplevelse og Tydning by nine translators (2026-10-14)
`ebook-method/oplevelse-og-tydning/` (GLOSSARY.md; put to Hans first: Oplevelse / Erfaring = experience / experience
[Erfaring] where the two are contrasted, Tydning = interpretation, and nine further terms accepted as proposed).  Nine
parts cut at essay or chapter starts (tr_parts.py), ~1.26M tokens; made and checked in the cloud workspace while the
device was offline, then written to `tr/` and built with `tr_parts.py build --write` (all checks OK).  163 odd spots;
the 128 that touch the Danish became `extra-b3.tsv` and went to the image as blind crops (109; two readers, ~0.17M
tokens, 24/24 controls) or were settled against the e-book (19): 7 transcription faults, all of a kind the collation
cannot see because both OCRs agree (a speck or worn hyphen read as ~, a speck read as a stop, „Modslykke“).  LESSONS:
(1) Feeding the odd spots back as `--extra` crops costs little and finds what neither OCR flags; do it for every book.
(2) Though the brief explains it, a translator still took a page-turn join (`lige%` … `\opage{222}ledes`) for a lost
space; such spots are settled by a grep, not the image.  (3) The glue-trap check must exempt `\setcounter{footnote}{0}%`
lines (tr_parts.py does now).  (4) One translator dropped two parenthetical glosses („(narrative spells)“) in a list:
compare parenthesis counts per page as well as quotes.

### 6y. Høffding's Den engelske Philosophi i vor Tid by eight translators (2026-10-15)
`ebook-method/engelske-philosophi/` (GLOSSARY.md settled by Claude without asking, on Hans's "do the whole book without
stopping"; the choices marked ◆ are for him to review: the title English Philosophy in Our Time; Udvikling = development,
but evolution for Spencer's and Darwin's theory (Udviklingsphilosophien = the Philosophy of Evolution); Forestilling = idea,
the empiricists' word; Aand = mind, spirit only for Hegel and religion; Jeget = the self; Følelse = feeling; Tillempelse =
adjustment, Spencer's word).  Eight parts by chapter and section (tr_parts.py), Sonnet translators, pilot first, then
batches of at most five; Høffding's Danish renderings of Mill, Bain and Spencer translated from his Danish, not replaced
by the English originals.  208 odd spots, all read blind at the image (round b3, three readers, 52/52 controls): 71
transcription faults and 53 misprints of the print.  LESSONS: (1) Parts cut at a section start can still begin in
mid-paragraph or mid-word at a page turn; the build must join such parts without a blank line (tr_parts.py now takes the
join from the Danish).  (2) The odd spots found far more here than in 6x (an Archive scan whose two copies share worn
sorts): run an unattested-word sweep on the Danish before the translators, and send them only what is left.  (3) A
paragraph break the translators query at a page turn is usually the draft's, not the print's (pp. 83, 107, 179): settle by
the image and mend in the Danish, then rebuild the parts.

### 6z. Høffding's Om Religionsfrihed by two translators (2026-10-15)
`ebook-method/tilskueren-1886-90/` (GLOSSARY.md from oplevelse-og-tydning's; put to Hans first: Religionsfrihed = religious
freedom, Trang = need, Følelsesliv = emotional life).  Two parts at section starts on page turns (tr_parts.py), Sonnet,
~0.17M tokens; the three Nietzsche-debate pieces are NOT translated (Banks, The Great Debate, 2024).  8 odd spots, read at
zooms in the main session: 5 transcription faults (lost stops, specks read as . and ').  LESSON: unify terms across parts
after the build (one translator wrote "love of humanity" against the glossary's "love of humankind"): grep the English for
each glossary term's alternatives before writing translation.tex.

### 6aa. Høffding's four pieces of 1875-76 by five translators (2026-10-15)
`ebook-method/hoeffding-1875-76/` (GLOSSARY.md from engelske-philosophi's, Spencer's terms the same; new choices marked ◆
for Hans: Nydelse = enjoyment, Kriticisme = criticism, Anger = repentance, Tolerance = toleration).  Six parts over four
books (tr_parts.py `build SLUG`), Sonnet, pilot then four, ~0.48M tokens; made in the cloud workspace and written back.
64 odd spots, ~45 read at zooms in the main session: 22 transcription faults, 3 misprints.  LESSON: when the Danish is
mended after the translation (a stray footnote removed, a paragraph break at a page turn joined), mend the English the
same way before `build --write`: the per-page paragraph check shows every such spot.

### 6ab. Høffding's Filosofien i Sverig by four translators, while Hans was travelling (2026-10-16/17)
Four parts (tr_parts.py, cut where a paragraph begins), Sonnet, pilot then three, ~0.5M tokens; made in the cloud workspace
while the computer was offline and written back when it returned.  A Swedish-spelled Danish print with Swedish quotations:
GLOSSARY.md S1 (◆ for Hans) translates a Swedish quotation in the text and keeps the Swedish on a `% sv:` line above it.
27 odd spots, all read at zooms: 6 transcription faults after OPEN 0 (a worn e that both OCRs read as c -- „sc“,
„thcologien“ -- and so never reached a reader; ö dropped; é for è; a ' for ”), 3 misprints marked, 1 spot misreported by its
translator (the transcription was right).  LESSONS: (1) a translator's page number can be off by a page or more: find the
spot in transcription.tex before rendering.  (2) In a GENERATED book a final-fixes row that matches nothing stops
proofapply.py --final from writing, and the later steps then run on the unfixed text: rerun the whole rebuild from draft.py
--emit, never only its tail (spaceapply.py run twice doubles every \emph).  (3) proofapply.py turns — into --- in a
replacement: a row must not span a — the print keeps.  (4) A fixed /tmp path for backups (pagemap BAKDIR) fails when another
sandbox user made it first: use tempfile.gettempdir().

### 6ac. Høffding's Religiøse Tanketyper by seven translators (2026-10-17)
Seven parts cut at essay starts (tr_parts.py), Sonnet, pilot then five then one, ~0.86M tokens (~18k per 1000 Danish
words; ~50k of each agent is fixed overhead, so parts of 6-9k words are cheaper per word than short ones).  The parts
were made in the cloud workspace from staged copies and committed back.  Title and Højsind put to Hans; the rest from
the earlier glossaries and the corpus (Grundværdi = fundamental value, Livspoesi = poetry of life).  61 odd spots: 31
read at 400-dpi LINE crops in the main session (four sheets of eight, ~8k tokens): one transcription fault, three
divisions whose hyphen the layer lost, a verse block set wrong, eleven misprints to mark.  LESSONS: (1) pages missing
from the scan and set from another source get a one-line `%` note in the English too (brief); (2) a structural mend
in the Danish after translation (verse, divisions) must be made in the English fragment the same way before
`build --write`, or the per-page paragraph check fails.

### 6ad. Høffding's Kort Oversigt (1910) by six translators (2026-10-17)
Six parts of 4.3-5.9k words cut at chapter heads (tr_parts.py now takes an anchor regex per part, since this print's
page turns fall inside sentences), Sonnet, pilot then five, ~0.78M tokens (~26k per 1000 words, more than 6ac's because
the glossary to read was the 450-line one of Den nyere Filosofis Historie, bound in full).  The title put to Hans (A
Short Survey of the History of Modern Philosophy, distinct from Macmillan's 1912 A Brief History).  The front matter
(title page, Contents, the nine-line Preface) translated in tr_template.tex by the main session.  54 odd spots, ALL read
at line crops: 33 transcription faults (a lost first line, a lost paragraph break, specks, doubled dashes, eight titles
only partly italic), 9 misprints.  LESSON: translators find what a three-witness collation cannot, when both OCRs fail
the same way (a dropped line, an italic span begun one word late); read every odd spot.
