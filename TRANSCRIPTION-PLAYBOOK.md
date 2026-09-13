# Fraktur/Antiqua → LaTeX transcription playbook

Point a fresh Claude session at this file to transcribe any 19th-century Danish
book in this repo from a page scan into `transcription.tex`. Use it as the
standing method; keep a short per-book **RESUME-NOTES.md** alongside it for
state that changes batch to batch.

**A caution about the word "complete".** This file used to advertise its model
book as "complete (VIII + 174 pp., 0 errors, done in one sitting)". Every term
in that boast is a statement about the *file*: `0 errors` is what LaTeX said,
not what a reader found. The repo said `0 errors` 218 times and had measured
the accuracy of exactly one of its 72 books. Do not describe a book as complete
on the strength of a clean compile. See §0.

For turning a finished transcription into English, see **TRANSLATION-PLAYBOOK.md**.

---

## 0. What the job is

**The job is to transcribe a book _and establish that the transcription is
accurate_. Those are not two jobs. A fragment whose accuracy has not been
established is not finished work.**

This has to be said at the top because for the first half of this corpus it was
never said at all, and the omission was invisible. The pipeline had rigorous
discipline about cost, and rigorous discipline about *structure* — page markers,
paragraphing, emphasis, Greek accents, printer's defects, all of it verified at
the image and logged. What it never had was a discipline about **words**. No
book was ever asked what its error rate was, so no procedure for answering
existed, so books were published `status: complete` with no evidence about the
one thing a transcription is for.

It was concealed by vocabulary. A finished book reported `0 errors`, `0 missing
characters`, `compile clean`, `TRANSCRIPTION COMPLETE`. Every one of those is a
typesetting result. `0 errors` is LaTeX's verdict; `0 missing characters` is a
font-coverage check. They read exactly like accuracy claims and are not. When
*Den menneskelige Tanke* was finally collated it came in at **~0.9 transcription
errors per page** — roughly 350 in one book — having passed every gate the
pipeline had.

### Why this is nearly free during, and ruinous after

**The check is almost free at the moment of transcription and costs a second
transcription afterwards.** This is the whole argument, and it is arithmetic:

The batch agent has already rendered the page. It already has the OCR in its
context. Comparing its own words against that second reading is a diff it is
holding both sides of — ten or so candidates on a thirteen-page batch, each
settled at an image it has *already paid to render*. That is the cheapest review
in this pipeline, and it is the only step that can see a dropped „ikke“.

Deferred, the same check requires rendering and reading all 392 pages again from
cold. *Den menneskelige Tanke*'s repair took forty collation agents over every
page in the book, then five waves of splicing, then a full re-verification — a
second pass comparable in cost to the original transcription, to recover
information that was in the first agent's context window and thrown away.

> **So: the check is not a stage that follows transcription. It is part of
> transcribing.** An agent that returns unchecked words has not done the job
> cheaply; it has deferred the expensive half of it onto someone else, at
> roughly forty times the price.

### The cost constraint, which is real and comes second

Cost discipline is a constraint on *how* the job is done. It never relaxes the
standard above, and confusing the two is what produced this corpus.

The cost of this job is context replay. A batch of twelve pages needs ~30k
tokens of OCR dumps and page images; those stay in the conversation and are
re-sent on every later call, so by batch 15 you are paying to re-transmit batch 1
fourteen times over. The fix is not "start a fresh conversation every batch" —
that works but wastes the user's time. **Dispatch each batch to a subagent.** It
starts cold, burns the OCR and images in its own context window, and returns
~150 words: **~119k–152k tokens inside each agent, a single paragraph in the
calling conversation.** Roughly a hundredfold reduction in what accumulates.

> **In the main conversation, never read a page image and never let OCR output
> land there.** Everything else in this file follows from that.

Both disciplines at once, in one line: *the images are read, and the words are
checked, inside the agent — and only conclusions come back.*

### The mechanism

Every batch is diffed against an independent machine reading of the same pages,
before it is spliced, with no book exempt:

```sh
python3 ocrdiff.py --frag .parts/pp<FIRST>-<LAST>.texfrag
```

Structural checks cannot see a missing „ikke“. Of the errors found in *Den
menneskelige Tanke* without consulting the OCR, **two-thirds were readings the
scan's own text layer had already got right** — the words were not lost by the
OCR, they were lost between the OCR and the file, because an agent handed a page
of OCR does not copy it: it reads it and writes it out again. Nothing compared
the two, so nothing could see it. §3 step 4 is the full rule, §3 step 6 is how
the result is recorded, and `SCANS.tsv` says which witness each book uses.

---

## 1. Set-up (once per book)

A book lives in `texts/<author>/<slug>/`. Before batching, it needs:

- `transcription.tex` — preamble, front matter, and a `\chapter*` skeleton with
  one marker per chapter: `% [text to be added: pp. X--Y]`.
- `pagemap.py` — **the single source of truth for printed page → PDF page.**
  Scans are not uniformly offset: on this book a leaf was scanned twice, so the
  offset changed from +13 to +15 partway through. Never hard-code an offset;
  every script calls `pagemap.py`.
- `ocr.sh` — Fraktur OCR for a page range, with the book's closed set of
  systematic confusions fixed by `sed`.
- `spacing.py` — mechanical letterspacing (Sperrsatz) detection. Fits a
  per-glyph advance width over the page by least squares and flags words that
  come out too wide.
- `check.py` — gap/dupe detection over `% --- p. N ---` markers, brace and quote
  balance, progress.
- `splice.py` — merges batch fragments into `transcription.tex` (see §3).
- `joints.py` — batch-seam paragraph breaks and dangling word-break hyphens, the
  two silent corruptions that survive every other check (see §6).
- `BATCH-AGENT.md` — the prompt body. **It must carry the copy-text discipline
  block from §4**; that block, not the playbook, is what the batch agent
  actually reads, and it is the agent-side half of the fix for the defect in §6.

Copy these from `texts/nielsen/evangelietroen-theologien/` and adjust
`pagemap.py` and the `ocr.sh` sed table for the new scan.

`ocrdiff.py` is **not** per-book: it lives at the repo root beside
`paginate.py`, works on any book with a text-layer scan, and needs no set-up.
§3 step 4 runs it on every fragment.

**None of this harness is tracked in git**, and neither is `BATCH-AGENT.md` or
`RESUME-NOTES.md`. A book directory tracks the **edition only** —
`transcription.tex`, `transcription.pdf`, and later the translation pair. The
root `.gitignore` enforces it; the reasoning is recorded there. In short: the
repo is public, the harness is unrunnable without the scans (which are correctly
not in the repo), and the copies are near-identical from book to book.

So the harness lives on your machine, and **the durable scholarly record goes in
the comment header of `transcription.tex`** — the verified page map, the errata
applied, the emphasis findings, the normalisation conventions, and the log of
printer's defects. Write that header as the thing an outside reader would need in
order to check the edition against the scan, because it is the only thing they
will get. `RESUME-NOTES.md` then carries only volatile state.

**The preamble must define the page macro** before any batch runs, or the
first fragment will not compile:

```latex
\usepackage{marginnote}
\newcommand{\opage}[1]{\marginnote{\footnotesize\textit{[#1]}}}
\newcommand{\apage}[1]{\marginnote{\footnotesize\textit{[#1]}}}
```

**Verify the page map by eye before transcribing a single word.** Read the
printed numeral off every page of the scan and confirm the endpoints. An
undetected offset change silently corrupts the whole book.

---

## 2. Is the OCR usable, or is the image the only witness?

Test this per book; it decides the whole pipeline.

- **Fraktur, clean scan** (this book): the Fraktur tesseract model reads it well.
  OCR carries the *words*; the image only has to carry *structure* — paragraphing,
  footnotes, rules — plus emphasis and doubtful readings.

  **This is the right division of labour and it is what makes a book cheap. But
  read what it commits you to.** If the words come from the OCR and the image is
  not going to be read word by word, then the OCR's words are your copy-text,
  and the only thing that can tell you whether they survived into the file is a
  machine comparing them. That is `ocrdiff.py`, and §3 step 4 makes it
  mandatory. A book transcribed on this premise *without* that comparison has
  nothing whatever checking its prose — which is the state eleven books in this
  repo were in until 2026-09.
- **Antiqua, poor scan** (Nielsen's *Religionsphilosophie*): the text layer was
  rejected outright and every page had to be eyeballed. Much slower.

Keep the PDF's own ABBYY layer (`pdftotext`) as a **second witness**: it fails
differently from tesseract (it tends to lose æ/ø), so where the two agree the
reading is safe, and where they differ, look at the image.

### Find out what the scan can actually resolve, before adjudicating any glyph

**Run `pdfimages -list -f P -l P <scan>` on a body page at the start of every
book.** A KB scan is typically not one image: on *Evangelietroen og den moderne
Bevidsthed* each page is a 96 ppi RGB image **plus a 1-bit mask at 400 ppi**, and
the mask carries all the type. `pdftoppm -r 1200` on such a page is 3× interpolation;
`-r 2400` is 6×. Interpolation preserves the topology of a stroke, so it still
helps you read — but it invents no evidence, and a distinction that lives in one
or two pixels of the mask cannot be settled by rendering bigger.

This matters because Fraktur has pairs that differ by almost nothing: **x/r**
(the x's tail below the baseline), n/u, and long-s/f. On this book an inventory of
some 130 "wrong sorts" — strar for strax, Erempel for Exempel, Tert for Text —
was built up page by page from renders at 1200 and 2400 dpi, defended with
confident measurements, and **had to be withdrawn in its entirety**: calibration
against words the edition already accepted as x showed that four of eleven
certain `strax` carry no visible tail at all, so absence of a tail was never
evidence. Two "control pairs" cited as proof that the compositor mixed the sorts
(a true `strax` twelve lines below a `strar`; a `voxer` above a `vorer`) both
turned out to be the same word twice.

Three rules follow, and they cost fifty hours to learn:

1. **Calibrate on words the edition already reads the other way**, not on your
   sense of what the glyph looks like. Measure the discriminating feature on a
   set of certain instances of each letter and see whether the distributions
   actually separate. If they overlap, the scan cannot decide and no amount of
   zooming will change that.
2. **Only a positive signal counts.** Silence is not evidence for either reading.
3. **Put the burden of proof on the claim of a defect.** Where the printed form
   is not a word in the language, default to the sense-reading unless the glyph
   positively shows otherwise. Errors in the other direction *fabricate* evidence
   about the printing house, which is worse than losing a real datum — and, left
   in a batch brief, they propagate: three consecutive batches here inherited the
   mistake from each other and hardened it into a rule.

Note that this is a departure from strict diplomatic practice, and a deliberate
one. It applies to sort-level distinctions the scan cannot resolve — not to
turned sorts, dropped sorts, broken sorts or punctuation faults, which are
plainly visible and stay logged as printed.

---

## 3. The batch loop

Batches are independent — each touches exactly one marker — so several can run
at once. **Concurrent agents must never edit `transcription.tex` directly:**
`Edit` is a read-modify-write over the whole file, and two agents finishing at
the same moment can clobber each other. `check.py` would catch a whole missing
batch but not a half-written one.

1. **Dispatch** one subagent per batch, 12–17 printed pages each, using the
   prompt body in the book's `BATCH-AGENT.md`. Give it the page range, the
   lecture/chapter name, and the exact marker line. `BATCH-AGENT.md` must tell
   it to open every page with `\opage{N}` at the word the page begins on (§4);
   if the book's copy predates that rule, add it before dispatching.
2. Each agent writes `.parts/pp<FIRST>-<LAST>.texfrag` — the text that will
   replace the marker, starting with its own `% --- p. FIRST ---`.
   **The extension must be `.texfrag`, never `.tex`** (see §6).
3. **Splice** in the calling conversation: `python3 splice.py`. One process, one
   write, no race. It matches each fragment to its marker by filename, archives
   spliced fragments to `.parts/spliced/`, and refuses to run on `.tex` fragments.
4. **Diff the fragment against the scan's own words** — before splicing, and
   non-negotiable for any book with a usable text layer:

   ```sh
   python3 ocrdiff.py --frag .parts/pp45-57.texfrag
   ```

   It prints every place the fragment's words diverge from the OCR's, with three
   exactly matching words on each side, and labels the classes that have
   actually gone wrong here (`dropped word`, `adverbial -t dropped`, `form
   modernised?`, `likely OCR`). Expect roughly ten items on a thirteen-page
   batch and expect about half to be the scan's fault — settle **each** at the
   image and either correct the fragment or dismiss it. Ten adjudications per
   batch is the cheapest review in this pipeline and it is the only step that
   can see a dropped „ikke“. Do not splice a fragment with unresolved items.

   Nothing here is filtered on suspicion of being OCR; the labels are hints.

   **There is no book to which this does not apply.** The check is against a
   *machine witness* — an independent machine reading of the same page — and
   the embedded layer is only the commonest one. Every book names its witness
   in RESUME-NOTES before its first batch is dispatched, in one of three forms:

   - **`USABLE`** — the scan's embedded layer. `SCANS.tsv` at the repo root gives
     every book its scan, that scan's sha256, and its layer state (55 of 72 are
     `USABLE`). `python3 scans.py path <book>` returns the verified path. This
     is the default and needs no argument.
   - **`NO LAYER`** — the embedded layer is absent or unusable. Four books are
     in this state (`hoeffding/pascal-kierkegaard`, the three Treschows).
     **Build the witness**: run tesseract over the batch's pages with the
     book's own model (`-l dan` for antiqua, the `Fraktur` *script* model for
     Fraktur — see `brochner/svar-nielsen/RECON.md` for the recipe and the
     trap), write it to `.parts/ocr/pp<FIRST>-<LAST>.txt`, and pass it:

     ```sh
     python3 ocrdiff.py --frag .parts/pp45-57.texfrag --ocr .parts/ocr/pp45-57.txt
     ```

     A tesseract witness is noisier than ABBYY, so more of its candidates will
     be the witness's fault. That raises the cost of the step; it does not
     excuse it. The point of a second witness is not that it is right — it is
     that it is *independent*, so anything both readings agree on was not
     invented between them.
   - **`NONE POSSIBLE`** — the book has no page images at all, because it is
     not scan-derived (`hoeffding/erindringer`, from an EPUB;
     `hoeffding/forholdet-tro-viden`, from Wikisource). These are the only
     legitimate exemption, they must be named as such in RESUME-NOTES **and**
     in `catalog.yaml`, and a reader must be able to see that the text has no
     original behind it. A book in this state is not a diplomatic
     transcription and should not be published as though it were.

   The distinction that was missed for eleven books is the one between *the
   check found nothing* and *the check never ran*. Those look identical in a
   finished file and opposite in a resume note, so the note must say which.

5. **Verify** in the calling conversation — cheap, text-only:
   `python3 check.py` (no gaps, no dupes, balanced braces, 0 suspect readings),
   then the compile test in §5. **Also check the page markers**: one `\opage`
   per printed page in the batch, numbers strictly increasing, none inside a
   command name. A batch covering pp. 45–57 must contain `\opage{45}` through
   `\opage{57}` and nothing else:

   ```sh
   grep -o '\\opage{[0-9]*}' .parts/pp45-57.texfrag
   ```

   A missing one means a page was skipped — the fault that lost printed p.134
   of *Den menneskelige Tanke* entirely, undetected until the book was
   paginated years later.

6. **Record that the check ran.** Every batch agent returns one line in a fixed
   form, and the caller copies it into RESUME-NOTES beside the batch entry:

   ```
   OCRDIFF: <witness> | <n> candidates | <n> corrected | <n> witness's fault | <n> unresolved
   ```

   e.g. `OCRDIFF: embedded | 11 candidates | 4 corrected | 7 witness's fault | 0 unresolved`.
   Unresolved must be 0 before the fragment is spliced; if it cannot be, the
   line says why. A batch entry in a RESUME-NOTES with no `OCRDIFF:` line is a
   batch whose words were never compared against anything, and a later reader
   should treat that book's word-accuracy as unestablished. `grep -L OCRDIFF
   texts/*/*/RESUME-NOTES.md` is the corpus-wide version of that question.

   **And when the book is finished, the totals go in the comment header of
   `transcription.tex`.** `.gitignore` excludes `RESUME-NOTES.md` and
   `BATCH-AGENT.md` on purpose — they are working files, and the durable
   scholarly record belongs in the header, "where it travels with the
   edition". A reader a year from now needs to know how this book's words were
   established, and a working file that was never committed cannot tell them.
   One line:

   ```
   % Word-accuracy: every batch diffed against <witness> before splicing
   % (ocrdiff.py). <n> batches, <n> candidates, <n> transcription errors
   % corrected, 0 unresolved. See TRANSCRIPTION-PLAYBOOK.md §3 step 4.
   ```

   A finished book whose header cannot carry that line is a book whose words
   were never checked, and the header should say *that* instead, plainly.
7. **Spot-check one emphasis call per batch** against the scan. This is the only
   step where the main conversation may look at an image, and it is worth it:
   the agents have been right every time so far, but the check is a few thousand
   tokens against a silent corruption risk.

Use the task list (TaskCreate/TaskUpdate) per round; it renders as a progress
widget for the user.

**The user commits and pushes — you never do.** (You almost certainly *cannot*
anyway: the sandbox has no git identity and cannot unlink files, and a half-run
`git commit` leaves a `.git/index.lock` behind that blocks the user's next
command.)

---

## 4. Transcription conventions

- **Mark every page turn, as you transcribe it.** Put `\opage{N}` at the exact
  word where printed page N begins — mid-sentence if that is where it falls,
  and mid-word too: where the original hyphenates *inden-/for* across the turn,
  write `inden\opage{30}for`. `\opage` sets no text, only a marginal *[N]*.

  This is not bookkeeping, it is the edition. A transcription without page
  markers cannot be cited: a hit in it is a paragraph number of ours, useless
  in a footnote, and a reader of the PDF cannot find the passage in the
  original. Møller's volumes have always done it and are the model.

  Do it *now*, while the page image is in front of you and the turn is a fact
  you can see. Recovering it afterwards costs a session per book and can only
  be approximate: of 73 transcriptions, 10 carry visible markers, 28 carry the
  page turns only as comments and still await `paginate.py convert`, and 27
  have no record of the original pagination at all — none of those 27 has a
  scan on disk, so for them the information is simply gone until one is found.

  A comment is a record, not a marker. `% --- p. 110 ---` on its own line is
  good practice and the search index now reads it, but the printed page shows
  nothing, so the PDF cannot be cited from. Write `\opage{110}` as well, in the
  body, at the word where the turn falls.

  Use `\opage` — you read the page. `\apage` is reserved for markers placed
  afterwards by machine alignment (see PAGINATION-PLAYBOOK.md); never write it
  by hand.

- 19th-century orthography **exactly as printed**: `Christendommen`,
  `Videnskaben`, `Theologie`, `høiere`, `aa`, capitalised nouns. Do not modernise.
- Danish quotation marks `„…“` low-high, as printed. Em-dash `---`.
- Letterspaced emphasis → `\emph{}`. Latin/foreign set in antiqua against the
  surrounding Fraktur → `\textit{}`. **Check the image**: a German name may be
  antiqua on one page and Fraktur on another, and each occurrence follows its own
  page.
- Footnotes: plain `\footnote{}`, with the printed mark noted in a `%` comment.
  If the book marks them `*)`, set `\renewcommand{\thefootnote}{*)}` in the
  preamble — **not** `\fnsymbol` (math mode, gives U+2217) and **not**
  `footmisc[perpage]` (resets on the *typeset* page, not the printed one, so a
  second note on your page becomes a dagger).
- Page markers: `% --- p. N ---` on its own line where printed page N begins.
  `check.py` depends on these; every page in the batch needs one.
- **Printer's defects: transcribe as printed**, log a `%` comment at the site,
  and report it. Do not silently correct the compositor. Expect the quote balance
  to drift off zero as a result — that is the *signal*, and the running total
  belongs in RESUME-NOTES so nobody later "fixes" it.
- Doubtful readings: zoom, then transcribe your best reading and flag the
  alternative you rejected. Never silently guess.

---

### Copy-text discipline — paste this into every batch prompt

The agent is not writing Danish; it is moving a fixed string of words from one
place to another. Say so, and say it in the prohibitive form — "be accurate" is
not an instruction an agent can act on, whereas "do not improve anything" is:

> You are copying, not composing. Where the text layer and the page agree, the
> words are already settled and your job is to carry them across unchanged —
> including every word you would have phrased differently, every spelling that
> looks like a mistake, and every short word you might not notice dropping.
>
> The 1910 orthography is data. `egentligt`, `navnligt`, `stadigt`,
> `oprindeligt`, `i Regelen`, `Principet`, `stansede` are correct as they stand;
> do not modernise a trailing *t* or a doubled consonant, and do not assume an
> archaic form is OCR noise.
>
> If the PAGE is wrong — a broken letter, a transposed pair, a misspelt name —
> transcribe the error **as printed** and log it in a `%` comment at the spot.
> Never silently correct the print. If you find yourself about to fix
> something, that is the moment to write a comment instead.
>
> When you are unsure between two readings, do not pick the one that reads
> better. Render the page and look.

---

## 5. The sandbox compile test

```bash
cp transcription.tex /tmp/t.tex
sed -i -e 's/\\usepackage{libertinus}/\\usepackage{lmodern}/' \
       -e 's/\\usepackage{libertinust1math}//' \
       -e 's/\\usepackage{textalpha}.*//' \
       -e 's/\\usepackage\[danish\]{babel}//' /tmp/t.tex
pdflatex -interaction=nonstopmode /tmp/t.tex
```

Expect **0 errors, 0 missing-character warnings**. Three false alarms this
produces, none of them defects in the file:

1. **Garbled `æ ø å` in the terminal log** — the terminal's encoding.
2. **`Unicode character … not set up for use with LaTeX` for every Greek letter**
   — caused by the `sed` stripping `textalpha`, which the real preamble loads.
   Confirm with `grep '^!' log | grep -v 'Unicode character'` (must be empty),
   and to test the rest of the file map Greek to a placeholder:
   `re.sub(r'[Ͱ-Ͽἀ-῿]', 'G', s)`. **Never delete Greek from the source.**
3. **`make` fails with `libertinus.sty not found`** — that package isn't in the
   sandbox. It is not a problem with the document; an untouched file in the repo
   fails identically. Real builds happen on the user's machine.
4. **`Undefined control sequence` for a math command** — `\varkappa`,
   `\underset`, `\overset`, `\angle`, `\wedge`, `\to`. The `sed` strips
   `libertinust1math`, which is what supplies them. *Grundideernes Logik* shows
   22 of these and *Den menneskelige Tanke* 49; both are clean on the real
   machine. Confirm by building the file's own backup the same way and
   comparing — **never compare a bare error count across the recipe**, only a
   file against its own untouched backup built identically.

### latexmk caches a failure and will not retry

`make` on the whole tree can end with

```
Latexmk: Nothing to do for 'transcription.tex'.
Collected error summary (may duplicate other messages):
  pdflatex: gave an error in previous invocation of latexmk.
```

and name no book, because the book it is talking about is the one it just
skipped. latexmk records the failed run in `.fdb_latexmk`; if the `.tex` has not
changed since, it reports the old failure instead of rebuilding — so a file that
was *repaired by reverting to a backup* keeps reporting an error it no longer
has. To find which book, look for the logs rather than the make output:

```bash
for f in $(find texts -name transcription.log); do
  n=$(grep -c '^!' "$f"); [ "$n" -gt 0 ] && echo "$n  $f"
done
```

Then check whether the error is still present in the current `.tex` before
fixing anything. Force the rebuild with `latexmk -g` or `make -B`.

---

## 6. Traps that have actually caused damage

- **`glob('/tmp/pg*.png')[0]` returns a stale page.** `/tmp` is shared between
  agents and `009` sorts before `068`, so a verification can confidently examine
  entirely the wrong page. This happened. Always
  `mktemp -d` + `pdftoppm -singlefile`.
- **Fragments named `.tex` break `make`.** The Makefile discovers targets with
  `find texts -name '*.tex'` and a preamble-less fragment dies with
  `Missing \begin{document}`. Hence `.texfrag`, plus `**/.parts/` in `.gitignore`.
- **Never write scratch renders inside the repo.** One agent wrote 26 PNGs
  (25 MB) into the book directory; they were committed and pushed, and the blobs
  are in history permanently. Render to `mktemp -d`. `.scratch-*/` and `*.png`
  are now gitignored, because the ignore rules don't depend on an agent complying.
- **A word the compositor broke across a line becomes `Cau- salitetsforholdet`.**
  A transcription reflows, so the printed line-break hyphen has to be resolved —
  but an agent writing out a page naturally copies the hyphen and starts the next
  source line with the rest of the word, and TeX turns that newline into a space.
  Nothing catches it: braces balance, quotes balance, `check.py` is happy, the
  file compiles with zero errors, and the defect is invisible until you read the
  PDF. Nine such words were in one book's first 147 pages, and eight more hid
  behind an `\emph{}` or a `\setcounter` on the intervening line. Write
  `Cau\-%` — discretionary hyphen, then `%` to eat the newline — and put a
  `%` on any `\setcounter`/`\markboth` line that sits between the two halves.
  **This must be an automated check, not a habit.** `joints.py` in
  `texts/brochner/det-religioese/` does it, and also catches the related seam
  bug: `splice.py` replaces a marker that the skeleton wrote with a blank line
  above it, so wherever a sentence runs across a batch boundary the joined file
  silently acquires a paragraph break the book does not have. Comments do not
  save you — a `%` line eats its own newline, so a comment between the text and
  the marker still leaves two consecutive newlines. Copy `joints.py` alongside
  the rest of the harness and run it after every splice, before `check.py`.
- **An agent rewrites rather than copies, and every structural check passes.**
  This is the costliest defect in the repo's history — ~0.9 errors per page
  through a whole 392-page book, undetected for as long as the book existed.
  The profile is specific, and recognising it is half the battle:
  - **dropped short words that leave grammatical Danish behind** — *kun*, *ikke*,
    *ny*, *og*, *saa*. p.336 of *Den menneskelige Tanke* read "Disse to Emner
    kunne reduceres til hinanden" where the page prints **ikke** reduceres: the
    transcription asserted the opposite of the original and read perfectly well.
  - **archaic forms silently modernised** — `egentligt`→`egentlig`,
    `Regelen`→`Reglen`, `Principet`→`Princippet`, `stansede`→`standsede`. A
    trailing *t* in 1910 orthography looks exactly like OCR noise to a reader who
    expects the modern form, so it gets "cleaned up".
  - **printer's errors silently corrected** — eleven of them in that book
    (*Benouvier*→Renouvier, *donnies*→données, *Anfangsgrunde*→Anfangsgründe).
    The same instinct aimed at the print, and the one thing the editorial stance
    most explicitly forbids.
  - **occasional paraphrase of a whole clause.** You cannot get that by
    mis-copying; it only happens when the text is being re-composed from sense.

  Braces balance, quotes balance, `check.py` is happy, the file compiles, the
  page markers are all present and strictly increasing. **`ocrdiff.py` in §3
  step 4 is the only thing that catches this**, and it catches it for free. The
  agent-side half of the fix is the copy-text discipline in §4: the instruction
  must forbid improving, not merely ask for accuracy.

- **Scope corrections to the heading block.** A skeleton chapter argument read
  `halvspeculative` where the printed head read `halvphilosophiske` — but
  `halvspeculative` occurs 13 times as the author's own term. A global replace
  would have corrupted twelve legitimate occurrences.
- **Don't trust the contents pages' OCR layer.** Chapter arguments reconstructed
  from it carried two errors on this book. Transcribe the Indhold from the image
  like any other page, and cross-check each argument against its printed head.
- **The book's own contents page and its chapter heads may genuinely differ.**
  Two such variants were confirmed at 600 dpi on both witnesses here. Record both
  readings; do not normalise them into agreement. The disagreement is a datum.

---

## 7. Bookkeeping

Keep **RESUME-NOTES.md** in the book directory, updated every ~20 pages, not
every batch. It should carry: the page map and how it was verified; the current
resume point; the running quote-balance total with every logged defect; open
review items; and anything that cost you an hour to learn. Write it for a reader
with no memory of the session — because that is exactly who reads it next.

**RESUME-NOTES.md is untracked** (see §1), so it exists only on your machine.
Anything in it that a *reader of the edition* would need — page map, errata,
emphasis rules, normalisation conventions, defect log — must be duplicated into
the `transcription.tex` header, which is what ships. Treat RESUME-NOTES as the
production log and the `.tex` header as the publication of record. When they
disagree, the header is what the world sees.

### What "done" is allowed to mean

A book is not done because it compiles. Before `status: complete` goes into
`catalog.yaml`, the book must be able to state, in the `transcription.tex`
header, how its accuracy was established:

```
% Word-accuracy: every batch diffed against <witness> before splicing
% (ocrdiff.py). <n> batches, <n> candidates, <n> transcription errors
% corrected, 0 unresolved.
```

If a book cannot carry that line — an older book transcribed before this rule,
or one whose batches have no `OCRDIFF:` record — it is not `complete`. Its
accuracy is *unmeasured*, which is a different thing from *good* and a different
thing from *bad*, and `catalog.yaml` should say so rather than imply a check
that never happened. An unmeasured book's error rate can be estimated cheaply
without re-collating it: **six random pages read at the image against the
transcription** gives a usable rate per book. That is how *Den menneskelige
Tanke*'s problem first surfaced — 8 of the 32 pages in its first collation were
a random control sample that nothing had flagged, and they carried errors at the
same rate as the flagged ones.

When the book is done, two passes remain: the Indhold/contents from the image
(§6), and the outstanding review items. Then update `catalog.yaml` — every
section needs `title`, `status`, and `links` (use `links: []` when empty; the
Haskell parser requires the key) — and the user runs
`~/hhalvors.github.io/publish-danish.sh "message"`, which rebuilds the PDFs,
regenerates the site, and pushes both repos.
