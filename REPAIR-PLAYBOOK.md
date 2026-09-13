# Repairing a transcription that was never accuracy-checked

This is the remediation playbook for the state the corpus is in as of 2026-09-13:
**72 books transcribed, one of them with a known error rate.** It is a
multi-week, resumable programme, not a job. Nothing in it needs to be finished
in one session, and nothing in it should be started without reading §7 on
budget.

For transcribing a *new* book, see **TRANSCRIPTION-PLAYBOOK.md** — its §0 states
the rule whose absence created this backlog. This file is about books
transcribed before that rule existed.

---

## 0. The state, and the goal

Every book in `texts/` was transcribed to a high structural standard and to no
known standard of word-accuracy. The pipeline verified page markers, paragraphs,
emphasis, Greek, printer's defects — and never once compared the words in the
file against the words on the page. Books were published `status: complete` on
the strength of a clean LaTeX compile.

When *Den menneskelige Tanke* was finally collated it came in at **~0.9
transcription errors per page**, ~350 in one book, having passed every gate the
pipeline had. It is the only book whose rate is known. It is not known to be the
worst, or the best.

**The goal is not to certify the corpus.** It is:

> Every book carries an honest, evidence-backed statement of what is known about
> its accuracy; every book found to be bad is repaired; and no book claims a
> standard it has not met.

A book that samples clean is recorded as *sampled clean, rate bounded at X* —
not as *accurate*. The difference is the whole point of this document.

**Order of work: the 41 published books first** (§8), because an error in a
published book is an error in public. Then the 31 unpublished.

---

## 1. What does not work. Do not retry these.

Four cheap proxies for transcription quality were tried on 2026-09-12 and all
four failed. They are recorded here so that a future session does not spend the
budget rediscovering it.

| Proxy | Why it failed |
|---|---|
| `ocrdiff` candidate **density**, ranked across books | Measures the *scan's* OCR reading-order quality, not the transcription's accuracy. 27 candidates drawn from three books were adjudicated at the image: **0 were real errors.** |
| Hapax-typo rate | Did not discriminate. Dominated by genuine 19th-c orthography. |
| Dangling hyphens | Did not discriminate. |
| Compile cleanliness, `check.py`, `paginate.py verify`, `audit` median | All structural. Every one of them is silent on words, by construction. That is how the corpus reached this state. |

**There is no free proxy.** The number costs pages read at the image. What §2
buys you is that it costs *few* pages, not none.

---

## 2. The two numbers, and why you need both

One agent per book returns two numbers. They answer different questions and
neither substitutes for the other.

**(a) The error rate** — from a random sample of pages read in full at the image
against the transcription. This is the real measurement. It sees everything,
including the errors no tool can find.

**(b) `ocrdiff` precision on this book** — from adjudicating a fixed number of
its candidates at the image. This measures *whether the cheap repair tool works
on this particular scan*, and it varies enormously: on the clean ABBYY antiqua
layer of *Den menneskelige Tanke* roughly 85% of candidates were real errors; on
the older Google and HathiTrust Fraktur scans, 0 of 27.

The combination is what selects the treatment. The dangerous quadrant is **high
error rate with low `ocrdiff` precision** — a bad book the cheap tool cannot
help with. That book needs pages read, and there is no way around it.

---

## 3. The assessment — one agent, one book

This is the unit of work. It costs roughly one transcription batch.

### Choosing the sample

Pages must be chosen by a rule, not by eye, or the sample measures where you
looked. Deterministic from the book's own name, so it is reproducible and
auditable:

```sh
python3 -c "
import random,sys,re
book=sys.argv[1]; n=int(sys.argv[2])
src=open('texts/'+book+'/transcription.tex',encoding='utf-8',errors='replace').read()
pp=sorted({int(m.group(1)) for m in re.finditer(r'\\\\[oa]page\{(\d+)\}',src)})
random.seed(book+'|v1'); print(' '.join(str(p) for p in random.sample(pp,min(n,len(pp)))))
" nielsen/videnskabslaere 6
```

Sample size:

- **Books over ~30 printed pages: 6 pages.**
- **Books of 30 printed pages or fewer: read the whole book.** A third of the
  corpus is under 50 KB; sampling one of those costs more in ceremony than
  reading it. See the sizes in §8.
- If a book has no page markers, it was never paginated — sample by section
  instead and say so in the ledger.

### The dispatch

Send a `general-purpose` subagent, one book per agent. It renders and reads
every image in its own context; **no page image enters the calling
conversation.** Give it the book's `BATCH-AGENT.md` for the book-specific
orthography and conventions, plus this brief:

> You are measuring, not repairing. Do not edit any file.
>
> 1. For each page N in the sample list: print the transcription for that page
>    (`python3 pgtools/span.py N`, or read between `\opage{N}` and `\opage{N+1}`),
>    render the page (`pdftoppm -f <N+offset> -l <N+offset> -r 300 -png <scan> /tmp/pN`),
>    and compare **every word** — not for sense, but word against word. Go to 400
>    dpi or crop whenever a letter is not unambiguous.
> 2. Count as an error: a wrong word, a dropped word, an added word, a dropped
>    line, a duplicated word, a wrong figure or name in a citation, a wrong or
>    missing accent. Do **not** count: line breaks, hyphenation, `„…“` quotes,
>    LaTeX markup, or a printer's defect faithfully reproduced.
> 3. **A silently corrected printer's error counts as an error** — this is a
>    diplomatic edition and the page governs.
> 4. Then adjudicate the 15 `ocrdiff` candidates in the list you were given,
>    drawn from elsewhere in the book: for each, is it a real transcription
>    error, or the scan's OCR misreading?
>
> Return **only** this, and nothing else — no page text, no OCR dumps, no images:
>
> ```
> PAGES SAMPLED: <list>
> ERRORS: <n> total across <n> pages  =  <rate> per page
> EACH ERROR: p.N | tex: "<5-8 words>" | print: "<what the page says>"
> OCRDIFF PRECISION: <n> of 15 candidates were real transcription errors
> CONFIDENCE: one sentence — where you had to work hardest, anything you would want re-checked
> ```

The errors it lists are real findings: apply them (§5) even if the book turns
out to need nothing else.

---

## 4. Reading the result

Errors in a 6-page sample, with the treatment each implies:

| Found | Implied rate | Treatment |
|---|---|---|
| **0** | — | **Second sample of 6** (seed `|v2`). If also 0 → record as sampled clean. If not, re-tier on the combined 12. |
| **1–2** | 0.17–0.33 /pg | **Targeted repair** (§5B) |
| **3+** | ≥0.5 /pg | **Full collation** (§5C) — *Menneskelige Tanke* territory |

### Be honest about what a clean sample proves

If errors occur at rate λ per page, the chance of seeing none in *k* pages is
e^(−kλ). So:

- **6 clean pages** bounds the rate at **λ ≤ 0.50/page** at 95% confidence.
  That is barely better than *Menneskelige Tanke*. Six clean pages prove almost
  nothing, which is why a zero triggers a second sample rather than a pass.
- **12 clean pages** bounds it at **λ ≤ 0.25/page** — about one error every
  four pages, still perhaps 100 errors in a 400-page book.

So the ledger entry for a clean book reads `sampled 12 pp., 0 errors, rate
≤0.25/pg (95%)`. It does **not** read `accurate`, and `catalog.yaml` must not
imply that it does. Anyone who later needs a stronger guarantee for a particular
book knows exactly what it would cost: more pages, at the same rate per page.

---

## 5. The three treatments

### A. Sampled clean — record and move on

Write the ledger row (§6) and the `transcription.tex` header line. Apply any
errors the sample did turn up. Done. This should be the majority outcome, and
if it is not, the corpus is in worse shape than *Menneskelige Tanke* suggested.

### B. Targeted repair — 0.17 to 0.5 errors per page

Available **only if `ocrdiff` precision on this book was ≥ ~30%.** Below that
the tool generates more adjudication than it saves, and the book goes to §5C or
stays marked unmeasured until it can be done properly. Say which in the ledger.

1. `python3 ocrdiff.py <book-slug>` — whole-book mode.
2. Dispatch the candidate list to subagents in blocks, ~40 candidates each, with
   the §3 adjudication rules. They return corrections as text; **the calling
   conversation splices with text-only tools.**
3. Apply. Rebuild. `python3 check.py`, the compile test, and
   `paginate.py verify` if the book is paginated.
4. **Re-sample 6 fresh pages** (seed `|post`) to confirm the rate actually fell.
   This is not optional: targeted repair only catches what `ocrdiff` can see,
   and the re-sample is what tells you whether that was most of the problem or a
   third of it. If the post-repair rate is still ≥0.17/pg, escalate to §5C.

### C. Full collation — 0.5 errors per page or worse

The *Menneskelige Tanke* method, which is proven and expensive: every page read
at the image. `pgtools/COLLATE-BRIEF.md` is the standing brief; it already
encodes the error profile to calibrate against (dropped short words that leave
grammatical Danish behind, stripped adverbial `-t`, modernised archaic forms,
paraphrased clauses).

- 10 pages per agent, dispatched in waves.
- Agents return corrections as text. **Never read a page image in the calling
  conversation.**
- Splice per wave, keeping a `.bak` per wave.
- Classify before touching anything: a **printer's** error is transcribed as
  printed and logged in a `%` comment; a **transcriber's** error is corrected.
- Hold `PRN` items for a second eye rather than guessing — restoring a typo that
  was not there is the worst outcome available.
- Log every correction in the `transcription.tex` comment header.

A 400-page book is ~40 agents. Budget it as its own multi-session project, not
as part of an assessment sweep.

---

## 6. The ledger — how this survives several weeks

`ACCURACY-LEDGER.tsv` at the repo root, one row per book. **It must be tracked
in git.** `.gitignore` excludes `RESUME-NOTES.md` and `BATCH-AGENT.md` as
working files; this is not a working file, it is the record of what has been
established, and a record that vanishes on a clean checkout is how the corpus
got here.

Columns:

```
book  state  witness  sampled  errors  rate  ocrdiff_precision  treatment  status  date  note
```

`status` is one of: `unassessed`, `blocked-no-scan`, `sampled-clean`,
`repair-targeted`, `repair-full`, `repaired`, `no-original`.

**`blocked-no-scan` and `no-original` are different things and must not be
merged.** `blocked-no-scan` (13 books) means this session could not find the
scan named in the book's notes — a bookkeeping problem, fixed by locating the
file. `no-original` (2 books) means no page images exist at all because the text
was never scan-derived. Collapsing the first into the second would write off
thirteen checkable books as uncheckable, which is the same category error that
let `0 errors` stand in for accuracy.

Duplicate the conclusion into each book's `transcription.tex` header, which is
what actually ships:

```
% Accuracy: sampled 12 random pp. at the image, 0 errors; rate bounded
% at <=0.25/page (95%). Not a full collation. [2026-09-20]
```

or, after repair:

```
% Accuracy: full collation of all N pages against the scan, <n> transcriber's
% errors corrected, <n> printer's errors restored as printed. [2026-10-04]
```

A book with neither line is `unassessed`, and `catalog.yaml` should not call it
`complete`.

---

## 7. Budget, and the shape of a session

This programme exists because accuracy was never measured. It must not become a
second reason to overspend.

- **A session does one kind of work.** Either a block of assessments, or one
  book's repair. Not both — mixing them is how a 6-page sample turns into an
  unplanned collation.
- **A sensible assessment block is 5–8 books**, dispatched concurrently, one
  agent each. That is roughly one transcription batch's cost per book.
- **Never read a page image in the calling conversation.** Every image lives and
  dies inside a subagent. This rule is what makes the programme affordable at
  all; it is in CLAUDE.md for the same reason.
- **Stop at the budget and write the ledger.** A session that ends with three
  books assessed and the ledger updated has succeeded. A session that ends with
  eight books assessed and no ledger row has produced nothing, because the next
  session cannot tell what was done.
- **Do not start a full collation to "just check something".** If a sample says
  a book is bad, record that it is bad and schedule it. The finding is the
  deliverable.
- **Validate before you believe.** Any script written for this programme is run
  against a case whose answer is already known before its output is acted on.
  Three tools were trusted on first output on 2026-09-12 and all three were
  wrong — two of them reported corpus-wide results that were pure artefact.

---

## 8. The two books transcribed from derived text

> **STATUS: TO DO, decided 2026-09-13 — re-transcribe both diplomatically.**
> Not scheduled; no date set. Ledger status `todo-retranscribe`.

These were transcribed from derived text rather than from page images. When this
section was first written they looked uncheckable. They are not: linking the
corpus by hash turned up a scan for each, so both can become genuine diplomatic
transcriptions instead of being withdrawn.

The first step for each is to confirm the scan really contains the text (the
Høffding volumes are collections, so check the contents page), then transcribe
from the image per TRANSCRIPTION-PLAYBOOK.md — **not** to patch the existing
derived text against the scan, which would inherit its errors invisibly. The
page markers both books now carry were invented and must be discarded, not
adjusted.

- **`hoeffding/forholdet-tro-viden`** — derived from the Wikisource text. No
  scan in the directory. Published `status: complete`. It now also carries 21
  page markers, whose provenance should be established before anyone trusts
  them.
- **`hoeffding/erindringer`** — derived from the Lindhardt og Ringhof 2021 EPUB
  of the 1928 text. Its own notes say "No scan, no page map, no page-offset —
  the e-book has no pagination. This is the one book here that isn't
  scan-based." It now carries 36 page markers, despite PAGINATION-PLAYBOOK.md
  saying such books must be skipped because "inventing numbers would be the
  worst outcome available."

Until that work is done, `catalog.yaml` should not present either as a
diplomatic transcription, and `forholdet-tro-viden` should not sit at
`status: complete`.

Related, from the same evidence: `hoeffding/relation-som-kategori`'s batch 7
collated *pre-existing legacy* text for pp. 72–76 and found it diverged from the
print in eleven places, **including five invented runs of `\emph{}`** — about 2
errors per page, worse than anything the batch pipeline produced. **Any book or
section whose text was imported rather than transcribed from the image should be
assumed bad until sampled.** Note it in the ledger `note` column where known.

---

## 9. The queue

Published books first, largest first within that (a large book has more readers'
exposure and more absolute error). Sizes are `transcription.tex` KB; witness is
from `SCANS.tsv`.

The live queue is `ACCURACY-LEDGER.tsv` — it is seeded with every book, its
state, its witness and its size, and it is the file to read at the start of a
session. This section only records the ordering rule:

1. **Published, and large** (≥200 KB): 19 books, `brochner/philosophiens-historie-1`
   down to `nielsen/johannesclimacos`. These carry most of the corpus's words.
   `hoeffding/menneskelige-tanke` is already done and is the calibration case.
2. **Published, small** (<200 KB): 22 books. Most are under 30 printed pages, so
   per §3 they are read in full rather than sampled — cheap, and they finish the
   published half.
3. **Unpublished**: 31 books, same rule. Several are large
   (`brochner/philosophiens-historie-2`, `nielsen/natur-og-aand`,
   `nielsen/evangelietroen-bevidsthed` are each over 1 MB). Nothing there is
   public, so nothing there is urgent.

Three books in the queue have `SCAN NOT FOUND` in `SCANS.tsv` among the
published set (`moller/udoedelighed`, `hoeffding/darwinismen`,
`moller/qvindelighed`) and several more among the unpublished. **Finding the
scan is a prerequisite, not part of the assessment.** Those books are seeded
`blocked-no-scan`. Clearing that status is cheap desk work — the scans are
almost certainly in `~/bibliotek` under a name the notes spell differently — and
it is worth doing as one batch before the first assessment session, so that no
assessment stalls halfway.
