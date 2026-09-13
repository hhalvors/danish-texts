# Working in danish-texts

Transcriptions and English translations of public-domain 19th-century Danish
philosophical works, from Royal Danish Library scans. Read this before starting.

## Which job is this?

| The user wants | Read first |
|---|---|
| A scan turned into `transcription.tex` | **TRANSCRIPTION-PLAYBOOK.md** |
| A finished transcription turned into English | **TRANSLATION-PLAYBOOK.md** |
| To continue a book already under way | that book's `texts/<author>/<slug>/RESUME-NOTES.md` |
| To find or read a passage — in Kierkegaard or in our own texts | **SEARCH-PLAYBOOK.md** |
| Commentary on a text, or an essay about several | **NOTES-PLAYBOOK.md** |
| Printed-page markers put back into a transcription | **PAGINATION-PLAYBOOK.md** |
| To check or repair the accuracy of a book already transcribed | **REPAIR-PLAYBOOK.md** + `ACCURACY-LEDGER.tsv` |
| To find the scan a book was transcribed from | `python3 scans.py path <book>` — see **SCANS.tsv** |

Always check for a `RESUME-NOTES.md` in the book directory first — 30 of them
exist, and each carries the page map, the resume point, and the traps specific
to that book. `python3 check.py` in the book directory prints current progress.

## Transcribing a book means transcribing it *and* establishing it is accurate

Those are not two jobs, and a fragment whose words have not been compared
against a second reading of the page is not finished work. The check is nearly
free inside the batch — the agent has already rendered the pages and already
holds the OCR — and costs a second full transcription if deferred. *Den
menneskelige Tanke* is the worked example: ~0.9 errors per page, ~350 in the
book, recovered only by forty agents re-reading all 392 pages.

A clean compile is not evidence of accuracy. `0 errors` is LaTeX's verdict and
`0 missing characters` is a font check; this repo said `0 errors` 218 times
while having measured the accuracy of one book in 72. Before `status: complete`,
a book states in its `transcription.tex` header how its accuracy was
established — see TRANSCRIPTION-PLAYBOOK.md §7.

### The mechanism

No book is exempt. Before a fragment is spliced it is diffed against an
independent machine reading of the same pages:

```sh
python3 ocrdiff.py --frag .parts/pp45-57.texfrag          # embedded layer
python3 ocrdiff.py --frag .parts/pp45-57.texfrag --ocr .parts/ocr/pp45-57.txt
```

`SCANS.tsv` at the repo root says, for every book in the corpus, where
its scan is and whether the embedded layer will serve (55 of 72) or a tesseract
witness must be built (4). The batch agent returns one line recording the
result, and the caller copies it into RESUME-NOTES:

```
OCRDIFF: <witness> | <n> candidates | <n> corrected | <n> witness's fault | <n> unresolved
```

This exists because *Den menneskelige Tanke* was transcribed to ~0.9 errors per
page, and two-thirds of those were words the scan's own text layer had already
read correctly. Nothing compared the two, so nothing could see it. A batch entry
with no `OCRDIFF:` line is a batch whose words were never compared against
anything. Full rule: TRANSCRIPTION-PLAYBOOK.md §3 step 4.

## Which scan is this book's scan?

`SCANS.tsv` links every book to its scan **by sha256, not by name**, and
`scans.py` resolves it:

```sh
python3 scans.py path hoeffding/menneskelige-tanke   # verified absolute path
python3 scans.py verify                              # OK / MOVED / CHANGED / MISSING
python3 scans.py update                              # rewrite paths for moved files
```

`~/bibliotek` is a 17 GB general library — 1285 PDFs, 513 author folders, shared
with other projects — of which this repo uses about 72. **Do not rename it to
suit this repo.** Identity is the hash, so the library can be reorganised freely
and `verify` re-finds everything (a moved file keeps its byte size; stat is free,
so only size-matches get hashed).

The hash is not bureaucracy. Every `\opage{N}` encodes an offset into one
specific PDF: substitute a different printing and every marker in the book is
silently wrong, with nothing to detect it. A `CHANGED` result is never routine —
if the page count and page size still match it is probably a re-OCR and needs
only the hash updated; if they do not, the book's page map is suspect.

Renaming is safe because identity is the hash: edit `SCAN-RENAME.tsv`, then
`python3 rename-scans.py --dry` and `python3 rename-scans.py`. It verifies each
file's sha256 before touching it, never overwrites, logs every move to
`SCAN-RENAME.done.tsv`, and rewrites `SCANS.tsv` so `scans.py` keeps resolving.
**Scans are named for the physical volume, not the text inside** — one PDF often
carries several of our books.

59 of 72 books are resolved; 13 are `UNRESOLVED` and need a human to identify
the volume. Five books share a scan with another book (anthology volumes), which
is correct and expected.

## The one rule that saves the most money

**Transcription batches go to subagents, not to the main conversation.**

A batch needs ~30k tokens of OCR and page images. Anything read in the main
conversation is re-sent on every later call, so a long book done inline costs
enormously more than the same book done through subagents — measured at roughly
a hundredfold difference on *Evangelietroen og Theologien*. A subagent burns that
context in its own window and returns ~150 words.

So: **in the main conversation, never read a page image and never let OCR output
land there.** Dispatch, splice, verify with text-only tools, spot-check one page.
Details in TRANSCRIPTION-PLAYBOOK.md §0 and §3.

Translation is different — it reads `transcription.tex`, not images, and is
cheap enough to do inline in ~10-page batches.

## The one rule that saves the most text

**Diff every batch against the scan's own words before splicing it.**

```sh
python3 ocrdiff.py --frag .parts/pp45-57.texfrag      # per batch, before splice
python3 ocrdiff.py hoeffding/menneskelige-tanke       # audit of a finished book
```

The rule above keeps the job cheap; this one keeps it right, and for eleven
books the two were confused. Where the scan has a usable text layer the method
takes the *words* from the OCR and spends the image budget on structure and
emphasis — which is correct, and is what makes antiqua books cheap. But it means
nothing is checking the prose, because an agent handed a page of OCR does not
copy it: it reads it and writes it out again.

Collating *Den menneskelige Tanke* in 2026-09 measured that: **~0.9
transcription errors per page**, and of the errors found without consulting the
OCR, two-thirds were readings the scan's text layer **had already got right**.
Dropped short words that leave grammatical Danish behind (*kun*, *ikke*, *ny*),
archaic forms modernised (`egentligt`→`egentlig`, `Regelen`→`Reglen`), printer's
errors silently corrected against the editorial stance. Braces balance, quotes
balance, `check.py` is happy, the file compiles, the page markers are all there.
Only a word-level diff sees it. TRANSCRIPTION-PLAYBOOK.md §0, §3 step 4 and §6.

## Repo facts worth knowing before you touch anything

- **The user commits and pushes. You never do.** The sandbox has no git identity
  and cannot unlink files; a half-run `git commit` strands a `.git/index.lock`
  that blocks the user's next command.
- **Never write scratch files inside the repo.** Render to `mktemp -d`. An agent
  once wrote 25 MB of PNGs into a book directory; they were committed and pushed
  and are in the history permanently. `.scratch-*/`, `**/.parts/` and `*.png` in
  book directories are gitignored, but don't rely on that.
- **A book directory tracks the edition and its note** — `transcription.tex` /
  `transcription.pdf`, the translation pair, and `note.md`. The per-book harness
  (`pagemap.py`, `ocr.sh`, `spacing.py`, `check.py`, `splice.py`, `verify.sh`),
  `BATCH-AGENT.md` and `RESUME-NOTES.md` all stay on disk **untracked**; the root
  `.gitignore` enforces it and explains why. The durable scholarly record —
  verified page map, errata applied, emphasis findings, normalisation
  conventions, printer's-defect log — goes in the **comment header of
  `transcription.tex`**, which travels with the LaTeX source, and in the
  **Editorial note section of `note.md`**, which travels to the website. Keep
  the two in step; the header is the authority, being written at the page
  against the image. See NOTES-PLAYBOOK.md.
- **Printed-page markers: 64 of 73 transcriptions carry them, 9 do not.**
  A hit in an unmarked book cannot be cited. `paginate.py convert` makes
  existing comment marks visible; `paginate.py apply` recovers them by
  aligning against the scan; `python3 paginate.py status` is the work queue.
  `paginate.py locate` measures the printed page range of an essay that sits
  inside a collected volume — run it before `probe` on any excerpt, or probe
  reports 8% matched and looks like a failure. `apply --fill` places markers
  only where the transcriber left none. `--width 30` rescues a Fraktur scan
  whose OCR is too garbled for the default 55-letter anchor. Before believing
  any diagnosis about an offset, render the page and read the folio.
  See PAGINATION-PLAYBOOK.md.
- **Page turns are recorded in three comment conventions**, not one:
  `% ---- printed p.110 (PDF 35) ----`, `% --- p. 110 ---`, and `% p. 110`.
  Any tool that reads pagination must accept all three, and must require the
  number to be the whole line — annotations that merely mention a page are far
  commoner than markers. `MARK_COMMENT` in `paginate.py` and `PAGE_BODY` in
  `sks-search/sks_search.py` must stay in step.
- **`\begin{document}` appears inside a preamble comment in three books.**
  Never split a `.tex` on the first literal occurrence; take the first one no
  `%` precedes on its line (`split_document()` in `paginate.py`).
- **A transcription's scan is in `~/bibliotek`**, usually under a filename that
  bears no resemblance to the slug. `python3 find_source.py <slug>` identifies
  it by content. Record the result as a `Scan:` line in the book's
  `RESUME-NOTES.md`, which is where `find_scan` looks.
- **`make` builds every `.tex` under `texts/`.** Never leave a preamble-less
  fragment with a `.tex` extension anywhere in the tree; use `.texfrag`.
- **`make` cannot run in the sandbox** — `libertinus.sty` isn't installed there,
  and every file in the repo fails identically. Use the substitution recipe in
  TRANSCRIPTION-PLAYBOOK.md §5 to compile-test.
- **`catalog.yaml`** drives the `/dansk/` page on the Hakyll site via a symlink.
  **Run `python3 validate-catalog.py` before handing the file back** — it checks
  every record against the definitions in `~/hhalvors.github.io/DanishTexts.hs`,
  which is what actually fails the build. Two breakages have been caused by
  editing this file blind. Required keys, per record: **Author** `id`, `name`,
  `dates`, `bio`, `works`; **Work** `id`, `title`, `year`, `sections`;
  **Section** `title`, `status`, `links` (use `links: []` when empty);
  **Link** `label`, `url`; **SecondaryLit** `id`, `author`, `title`, `year`,
  `sections`; **Edition** (`modern-editions`) the same but with `editor`
  optional; **Reference** (top-level `references:`) `id`, `title`, `authors`,
  `year`. Note the trap: secondary literature takes **`author`, singular**, and
  only that — `authors:` or `editor:` there fails with
  `parsing DanishTexts.SecondaryLit failed, key "author" not found`; put the
  role in the value, `"Vibeke Koch & Carl Henrik Koch (eds.)"`. Unknown keys are
  ignored rather than rejected, so a misspelt key reads as a missing one, and an
  unknown `status:` silently renders as a "to do" badge with your string as its
  label.
  Its `note:` field is a two-or-three-sentence blurb, nothing longer: it renders
  as escaped plain text, so no markup survives there. Anything longer belongs in
  a `note.md`. The catalog has **no field recording which works have notes** —
  the site discovers them and resolves their ids against the catalog, so a typo
  in a note's `author:`/`work:` fails the build rather than silently orphaning it.
- **Publishing** is `~/hhalvors.github.io/publish-danish.sh "message"`, which
  rebuilds PDFs, regenerates the site, and pushes both repos. Not `sync-pdfs.sh`.

## Editorial stance

These are diplomatic transcriptions. Printer's errors are transcribed **as
printed** and logged in a `%` comment at the site, never silently corrected —
so quote-balance counts drift off zero on purpose, and the running total is
recorded in RESUME-NOTES. Where a book's own contents page disagrees with its
chapter heads, record both readings rather than normalising them.

