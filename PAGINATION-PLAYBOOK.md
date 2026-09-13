# Putting printed-page numbers back into the transcriptions

A transcription without page markers cannot be cited. A search hit in it is a
paragraph number of ours, useless in a footnote, and the edition's whole point
is that a reader can go to the page. This is the job of closing that gap, book
by book, over as many sessions as it takes.

The markers are **printed, not hidden**. Poul Martin Møller's volumes already
do it properly — `\opage{169}` set in the text at the word where the page
turns, rendering as a marginal *[169]* — and that is the convention for
everything else. A comment would serve the search index and nobody else; a
marginal number makes `transcription.pdf` and the website independently
citable, which is what a diplomatic edition is for.

`python3 paginate.py status` is the resume point. It reads the transcriptions
themselves, needs no index and no setup, and prints what is left, biggest
first. Start every session with it.

## Three different jobs, not one

Sort the book before choosing a method. `paginate.py status` tells you which
it is.

**Already visible (64 books, 8,479 markers).** Nothing to do.

**The 9 that remain**, and what each is waiting on:

| book | what stops it |
|---|---|
| `hoeffding/psykologi`, `nielsen/om-hindringer`, `kroman/hansen-relativitetsprincipet` | empty scaffolds — chapter headings, no text. Nothing to paginate until someone transcribes them |
| `brandes/levned` | selections with gaps across pp. 87–270; needs one range per extract |
| `moller/hvad-er-philosophie` | no folio measurable in `efterladte-skrifter3.pdf`; read one by eye and pass `--offset N` |
| `nielsen/propaedeutik-darwin` | `locate` cannot find its text in the matched scan — the scan is wrong, re-run `find_source.py --pages 0` |
| `hoeffding/darwinismen` | no scan exists anywhere; KB-VISIT-TODO.md item 8 |
| `kierkegaard/essential-kierkegaard` | assembled from SKS TEI; its pagination is SKS's, not a scan's |
| `nielsen/religionsphilosophie/indledning` | fragment; check whether it belongs to the parent book |

## Read the folio yourself before believing a diagnosis

Six books were once written up here as "the offset is wrong". Rendering one
mid-book page from each and reading the folio showed that **four of the six
offsets were already correct** — the failures were four different problems
wearing the same symptom. The lesson is the cheap one: a page image settles in
thirty seconds what an alignment score only hints at.

```sh
pdftoppm -f 90 -l 90 -r 100 -png "$SCAN" /tmp/pg    # then look at it
```

What the six actually were:

- **`religionsfilosofi`** — offset genuinely unmeasurable (no folio survives in
  the scan's text layer). Read by eye: scan 190 = printed 179, offset 11.
- **`psykologi`** — offset measured 33, true 15, *and* the transcription turned
  out to be an empty scaffold, so the offset never mattered. Its header also
  names the 2nd edition (1885, IV + 421 s.), so `Psykologi_1.pdf` is the wrong
  file of the five in that folder; the right one is `Psykologi i Omrids 1885.pdf`.
- **`religion-og-videnskab`** — offset 141 correct at scan p. 200 and useless,
  because the volume holds several works and **pagination restarts**. Where the
  text actually is, the offset is 9. Now 59/59 pages, 100% audit coverage.
- **`bemaerkninger`** — offset right. The scan is Fraktur and its OCR is badly
  garbled ("Lontradrctionsprincipet" for "Contradictionsprincipet"), so a
  55-letter anchor could not survive. See `--width` below.
- **`om-elskov`** — offset right, 173/173 matched, and refused for two anchors
  out of 173 landing backwards. See `longest_rising` below.
- **`erindringer`** — offset right. It is *Udvalgte Stykker af Kapitel II*:
  selections with gaps, so its misses are the gaps, not failures.

## `--width`: when the OCR is too garbled for a long anchor

The default 55-letter anchor assumes the scan's text layer roughly matches the
transcription. On a Fraktur scan it does not. Shortening the anchor trades
precision for reach, and the trade is worth making only as far as the
monotonicity check tolerates:

| width | matched | usable after dropping bad anchors |
|---|---|---|
| 55 | 52% | 52% |
| 40 | 77% | 77% |
| 30 | 90% | **133 of 152 pages** |
| 24 | 97% | refused — too many contradictions |

Width 24 matching 97% is not a better result; it is the anchor becoming short
enough to match the wrong place. The refusal is the tool working.

## `longest_rising`: two bad anchors should not condemn a book

A handful of anchors in a long book will land wrong — a stock phrase, a running
head that recurs in the text, a passage the author quotes from himself.
Refusing the whole alignment for two anchors out of 173 throws away a good
result; keeping them puts a page marker earlier in the text than the page
before it, which is worse than no marker. So `probe`/`apply` now keep the
longest rising run of positions and drop what contradicts it — the same
longest-increasing-subsequence argument `measure_offset` already uses on
folios, for the same reason: pagination rises, and whatever does not rise is
not pagination.

It reports what it dropped, and still refuses outright when more than 10% of
anchors contradict each other, since that is no longer a stray match or two but
a wrong alignment. *Om Elskov* went from refused to 165 of 173 pages this way.

## Excerpts inside collected volumes

A third of these texts are one essay inside a big PDF: Høffding's *Forholdet
mellem Tro og Viden* is 21 pages of a 263-page *Mindre Arbejder*, Møller's *En
dansk Students Eventyr* sits at p. 88 of volume I of the *Efterladte Skrifter*,
Nielsen's Darwin piece is an offprint whose own pages are 449–459.

`probe` defaults to pages 1..len(scan)−offset, which for those is mostly other
people's text, so it reports 8% matched and looks like a failed alignment when
nothing is wrong. **Run `locate` first**: it finds the transcription's opening
and closing in the scan's own pages and converts them to printed pages with the
measured offset.

```sh
python3 paginate.py locate moller/students-eventyr
#   found on scan pages 365-371 of 567
#   printed pages 88-94
python3 paginate.py probe moller/students-eventyr --first 88 --last 94
#   pages 88-94: matched 7/7 (100%)
```

`locate` is also the cheapest check there is on a weak offset. Brøchner's
*Brandes-Levned* measured offset 329 from two folios that agreed by chance;
`locate` put the text at printed page −189, which is arithmetically impossible,
and refused. Reading one page image gave the true offset, 11 — the scan's
folio-looking numbers were gathering signatures.

## When a book is half hand-marked: `--fill`

Nielsen's *Grundideernes Logik* had 425 `% p. N` comments over its 456 pages —
the transcriber marked the first two thirds and then, from p. 323, only every
other page. Neither tool alone is right: `convert` would make an incomplete
sequence look authoritative, `apply` would bury 425 hand-read positions under
machine guesses. So `convert` first, then `apply --fill`, which places markers
only where no hand mark exists: 425 `\opage` plus 32 `\apage`, one duplicate
(p. 417 is marked twice in the comments), strictly increasing, no gaps.

**Then audit it, because hand marks are not automatically right.** The median
page in that book collates at 95% against the scan, but p. 17 spans 131
characters where its neighbours span 1,900: the transcriber's comment sits at
the end of the page it names, so p. 16 absorbed most of p. 17's text. Twenty-one
of its 456 pages sit more than 12 points below the median. Hand evidence beats
alignment on average and not on every page, and the audit is what tells them
apart.

## Three ways a page turn is written in a comment

This corpus uses three conventions, all of them legitimate, none of them
announced anywhere:

| form | books |
|---|---|
| `% ---- printed p.110 (PDF 35) ----` | 21 |
| `% --- p. 110 ---` | 26 |
| `% p. 110` | 3 |

For most of this project `paginate.py` and `sks_search.py` recognised only the
first. The cost of that was not a missing feature but a **false picture of the
work**: 28 books that were fully paginated read as unpaginated, and one of them
(`nielsen/propaedeutik-1860-61`, 482 hand-established marks) was given 474
machine-aligned `\apage` markers before the duplication was noticed and the
book reverted from its backup. Two thirds of the queue was not work at all.

The regex is shared in spirit between `paginate.py` (`MARK_COMMENT`) and
`sks_search.py` (`PAGE_BODY`). **Keep them in step.** Each alternative demands
that the page number be the whole content of the line — fenced by dashes on
*both* sides, or followed by the printed form's `(PDF n)`, or by nothing at
all. Without that the annotations that merely mention a page would be read as
pagination, and there are far more of those than there are markers:

```
% p. 110 bears ONE footnote.              <- prose
% p.174 --- THE LONGEST SPACED RUN        <- prose (one-sided dash)
% printed p. 121. Verified at 300 dpi.    <- prose
% The p. 33/34 join falls mid-word.       <- prose
```

The general lesson, which cost a session: **before building a tool that reads a
convention out of the corpus, survey what the corpus actually contains.** One
`grep -rhoE '^%[^\n]*p\.? ?[0-9]+' | sed 's/[0-9]+/N/g' | sort | uniq -c`
would have shown all three forms in the first minute.

## The one rule

**Probe before apply, and verify before commit.** `probe` writes nothing and
prints exactly what `apply` would do. `apply` keeps a `.bak` and touches only
comment lines, but a wrong offset will silently paginate an entire book
incorrectly, and a wrong page number in the edition is worse than none.

## How it works, and why it works that way

Three stages, each of which failed in a more obvious form first.

A worked example of why the refusal matters: on *Religionsphilosophie* the
tool reported `offset: 13 (measured from 504 folios, 2 values seen — CHECK)`
and then refused, because the positions ran backwards. Its two offsets were 13
for most of the book and 15 across scan pages 275–288 — which is exactly the
misbound leaf the transcriber had already found and documented in the header.
The machine rediscovered a physical defect in the scan, and was right to stop.
A book that refuses is telling you something about the object.

**The offset is measured, not assumed.** Printed folios are read out of the
scan's own running heads, kept only where a page within six agrees
arithmetically, then forced monotonic — pagination rises across a whole file,
footnote numbering does not. It cannot be derived from the alignment itself:
*every* offset appears to match, because each scan page's text occurs somewhere
in the transcription whatever number you attach to it. Ten agreeing folios is
plenty; unanimity is the signal to trust.

**Both texts become a bare letter-stream.** Lowercase, letters and digits only,
LaTeX commands dropped. Hyphenation, line breaks, letterspacing, markup and
punctuation all differ between the scan's OCR and our transcription; the
sequence of letters does not.

**Anchors are tried several ways.** A page may open with a running head that
never entered the transcription, and any single window may sit on an OCR error,
so anchors are taken from a few starting lines and from further into the page.
The first that lands fixes the position.

Markers go in **at the word where the page turns**, not at a paragraph
boundary — Møller's volumes place 192 of their 204 markers mid-sentence, and
anything coarser is a worse edition. `paginate.py` will not drop one inside
braces, inside math, or after a `%`, where it would change the typesetting or
vanish with the commented line.

Two macros, rendering identically and indexed identically:

| written | means |
|---|---|
| `\opage{169}` | the page was read at the image |
| `\apage{169}` | the page was placed by alignment against the scan |

That distinction is the point of the exercise being honest. Everything this
tool writes is `\apage`, so a rerun replaces its own work and never a
person's, and a reader of the source can see which numbers carry which
authority. **Promote an `\apage` to `\opage` when you have checked it against
the page image** — that is real editorial work and it is worth doing for the
passages you actually quote. The preamble definitions are added automatically
if the file lacks them.

A paragraph straddling a page turn is cited by the page it begins on, and the
search index records both, so a hit in it reads `pp. 169–170`.

## Doing one book

```sh
cd ~/danish-texts
python3 paginate.py status                       # pick the top of the queue
python3 paginate.py probe hoeffding/menneskelige-tanke
python3 paginate.py apply hoeffding/menneskelige-tanke
python3 paginate.py verify hoeffding/menneskelige-tanke
```

A good probe looks like this:

```
  offset: 15  (measured from 10 folios, unanimous)
  pages 1-392: matched 390/392  (99%), 2 missed
  monotonic: True   chars/page: median 2084
```

Read those four numbers before going on:

- **offset** — unanimous is good. If several values were seen it says `CHECK`,
  and you should establish the offset by eye and pass `--offset N` instead.
- **match rate** — 95%+ is normal for a clean scan. Below about 80% means the
  scan and the transcription may not be the same edition, or the text layer is
  poor. Investigate rather than applying.
- **monotonic** — must be `True`. The tool refuses to write otherwise.
- **chars/page** — should be steady and plausible, roughly 1,500–3,000 for a
  normal octavo. A median of 400 or 9,000 means something is wrong.

Then `verify`, which re-reads the written file: page numbers strictly
increasing, few non-consecutive steps, no single gap wildly larger than the
rest. A large gap is a stretch the aligner skipped; look at it by eye.

**Then build the PDF**, because these markers are now part of the document and
a broken build is a broken edition. `make` cannot run in the sandbox —
`libertinus.sty` is not installed there and every file in the repo fails
identically — so compile-test with the substitution recipe in
TRANSCRIPTION-PLAYBOOK.md §5, and confirm the marginal numbers actually appear:

```sh
pdftotext -q transcription.pdf - | grep -coE '\[[0-9]{1,3}\]'
```

That count should match the number of markers written.

**The strongest check is free and independent.** Most `RESUME-NOTES.md` carry a
structural page map — chapter and section starts by printed page, written by
reading the book. After applying, confirm those headings land on those pages.
For *Den menneskelige Tanke* the notes give `A. Animisme… p.109`,
`A. Kategorilærens Historie p.135`, `a. Videnskab og Verdensanskuelse p.306`,
`α. Det etiske Arbejde p.350` — and the alignment put all four exactly there.
That is the confirmation worth having, because nothing in the algorithm knows
about it.

For a final spot-check, render the page and look:

```sh
pdftoppm -f 191 -l 191 -r 150 -png scan.pdf /tmp/pg     # printed 176 + offset 15
```

## Two known limits of the alignment

A marker anchors to the first *text* of a page, so a heading printed at the top
of a page is attributed to the page before it. In Den menneskelige Tanke the
Part III heading sits on p.135 and cites as p.134. Harmless for a quotation,
wrong for a citation to a heading — check those at the image.

A marker snaps to the nearest word boundary within about twelve characters, so
it can sit one word before the true turn where a page breaks mid-word.

## When the simple path does not work

**No scan on disk.** `paginate.py` looks for `scan.pdf` in the book directory,
then for a path named in `RESUME-NOTES.md` or the transcription's own comment
header — most of them record one, e.g.
``Scan: `~/bibliotek/Brøchner, Hans/1869-om-det-religiøse.pdf` ``. If none is
named, search `~/bibliotek` for the work; `~/bibliotek-search/bib.py authors`
and `works -a <name>` are the quick way. Pass it with `--scan PATH`. If it is
nowhere on disk, the scan has to come from KB again — record the shelfmark from
the header when you fetch it.

**The scan has no text layer.** `probe` says so and stops. `ocrmypdf in.pdf
out.pdf` first, then point `--scan` at the output. Do not put the OCR'd copy in
the book directory unless you mean to keep it; `scan.pdf` is gitignored, most
book directories no longer have one, and they are large.

**Folios cannot be read.** Fraktur, heavy foxing, or running heads without
numbers. Establish the offset by hand — find any page whose printed number you
can read in the scan, subtract — and pass `--offset N`. Then check the match
rate and the checkpoints especially carefully, since the measured-offset safety
net is gone.

**The text is a journal article.** Several Kroman and Høffding pieces are
offprints from *Fysisk Tidsskrift* whose `RESUME-NOTES.md` records the printed
range, e.g. `Source: Fysisk Tidsskrift 15, printed pp. 192–205`. The offset is
then `first_scan_page - 192`, usually small; use `--offset` and `--first`
/`--last` to confine the run to the article.

**The source is an e-book.** `hoeffding/erindringer` and its kind came from
reflowable EPUB and have no printed pagination at all. **Skip them.** They are
correctly unpaginated, and inventing numbers would be the worst outcome
available. Note in `RESUME-NOTES.md` that they are out of scope, so a later
session does not keep reaching for them.

**The book already has hand-made markers.** `probe` says how many. `apply`
leaves them alone and adds `[auto]` ones around them — every line this tool
writes is tagged `[auto]`, so a rerun replaces its own work and never a
person's, and a reader can tell them apart. Where the two disagree, the
hand-made one is right: it was written at the page against the image.

## Collating against the scan, once a book is marked

Marking a book makes something else possible. Each page is now a bounded
stretch of text with a known counterpart in the scan, so the two can be
compared:

```sh
python3 paginate.py audit hoeffding/menneskelige-tanke --worst 20
```

It reports each page's coverage and flags those well below the book's median.
Three different things cause a low score, and they are worth telling apart:

- **OCR noise.** The commonest. Scores are trigram overlap, so a scan that
  misreads one letter everywhere drags a whole book down without any page
  being wrong: the Nielsen scans render "være" as "vcrre" and "Følelse" as
  "Folelse". Compare the letter counts for the page: if the transcription and
  the scan agree in length, suspect the text layer, not the transcription.
- **A misplaced marker.** p.9 ran long by 719 letters and p.10 short by 722,
  every neighbour agreeing to within three. No text was missing; `\apage{10}`
  simply sat too late. A matched pair of opposite excursions is the signature.
- **A real error in the transcription.** This is why it is worth doing. The
  same pass found p.133 reading "deri finder man Fremskridtet" where the page
  prints **han**, and a line where the transcriber's eye had skipped from
  "historiske Emner" to the "Totaliteter" of the next line, silently dropping
  a word and duplicating another.

The median is a measure of the scan, not of the edition: 98% for Den
menneskelige Tanke, 91% for Om personlig Sandhed, whose scan is much worse.
Do not chase the median upward, and never compare one book's score with
another's. Only the distance below a book's *own* median means anything.

Read the outliers against the image and correct what is wrong at the page.
That is ordinary collation; the marking is what made it cheap.

## Recording it

The durable scholarly record lives with the source, not in this file. After a
book verifies:

- In the **comment header of `transcription.tex`**, record the offset and how
  it was established, e.g. `Page-offset: PDF = printed + 15 (measured from the
  scan's running heads; 390/392 pages placed by paginate.py as \apage, not yet
  verified at the image)`. The `\apage` / `\opage` split already carries this
  per marker; the header says it once, for a reader who is not counting.
- In **`RESUME-NOTES.md`**, note the date, the match rate, and any stretch left
  unmarked, so the next session knows what was left rather than re-deriving it.
- Where the edition is published, the **Editorial note in `note.md`** should say
  that page markers were recovered by alignment against the scan rather than
  read at the page, and that a paragraph straddling a break carries the page it
  begins on. A reader is entitled to know which numbers were verified by eye.

Then rebuild the search index so the pages become usable, and commit:

```sh
cd ~/sks-search && SKS_TEXTS=~/danish-texts/texts python3 sks_search.py index
python3 sks_search.py search --topic irrationality -c texts --paged
```

**You commit; the assistant does not.** Review the diff first — it should
consist entirely of added comment lines. `paginate.py verify` plus
`git diff --stat` is enough to see that.

## Order of work

`status` sorts by size, which is the right order: the biggest books carry the
most uncitable text. But two other considerations override it.

Do **thin** books before **none** books of the same size. Thin ones are
actively producing wrong citations; unmarked ones merely produce none.

And do the books you are actually writing from first. Høffding's *Den
menneskelige Tanke* was the first one done because a question about the
irrational needed it — its §397, the definition of `det Irrationelle`, is
printed p. 176, and could not be cited before.

## Three bugs that damaged files, all now fixed

**The marker that ate a paragraph break.** `write()` inserts the marker AT the
nearest safe whitespace. Where a page turn fell at a paragraph boundary, the
spot `nearest_safe` chose could be the *second* newline of the `\n\n` pair, so
the marker was written between the two newlines and the blank line was gone —
two paragraphs silently became one. Nothing downstream could see it: braces
balance, quotes balance, `check.py` is happy, `verify` passes, not a letter
changes, and the document compiles. A run across the queue on 2026-09-12
destroyed **65 paragraph breaks in 15 books**, on top of 39 in *Den menneskelige
Tanke*, and it surfaced only because a reader collating against the page images
kept reporting paragraph starts the transcription did not have.

`snap_out_of_break()` now moves any spot inside a blank-line run to the head of
the *new* paragraph, where the marker belongs anyway — the break survives and
the marginal number sits beside the page's first line. Regression-tested by
re-running `apply` on the same book and scan: 0 lost where the old code lost 39,
0 standalone marker lines where it left 38, blank-line count identical.

**Repairing it, if it ever recurs.** `apply` writes a `.bak` before it writes
anything, so the pre-pagination paragraph structure is still on disk and the
repair is exact rather than inferred:

```sh
python3 parafix.py check           # every paginated book, against its own .bak
python3 parafix.py repair --all
python3 parafix.py check           # must print 0
```

Two things that cost hours, both recorded in `parafix.py`'s own docstring and
worth knowing before you touch it. **Compare in the letter stream, never in a
window of characters** — inserting a marker shifts what falls inside a character
window, so the same paragraph yields a different key before and after and reads
as damaged when nothing is wrong; one version of that heuristic reported 4,569
losses where the true number was 65. And **walk the insertion point back out of
any enclosing `\command{`** — a paragraph may open `\emph{Stumpf} vil…`, and a
blank line inserted at its first *letter* lands inside the argument, which no
text-only check sees and only the compiler catches.



**The comment that says `\begin{document}`.** Three preambles explain their own
structure in a comment — "The PDF metadata is set with `\hypersetup` AFTER
`\begin{document}`, NOT as package options here". `convert` split the file on
the first literal occurrence, which is that comment: the preamble macros were
inserted into the middle of the sentence, un-commenting its remainder, and
`hyperref` and `\pdfstringdefDisableCommands` then ran inside the body. The
build still "passed" in the sense of producing a PDF. `split_document()` now
takes the first occurrence that no `%` precedes on its line; `sks_search.py`
does the same. Any tool that splits a `.tex` on `\begin{document}` must.

**Comparing error counts across the `sed` recipe.** Section 5 of
TRANSCRIPTION-PLAYBOOK warns that stripping `textalpha` makes every Greek letter
an error. For a book with Greek that also makes the *count* meaningless: the
pre-conversion build of `nielsen/speculative-methode` aborted at TeX's error
ceiling after 602, the post-conversion build ran further and reported 979, and
the conversion looked like a regression when nothing had changed. Map Greek to a
placeholder first (`re.sub(r'[\u0370-\u03ff\u1f00-\u1fff]', 'G', s)`) and both
builds come out at 0 errors and 132 pages. **Always compare a converted file
against its own backup, built the same way, not against a bare error count.**

## What not to do

Do not paginate a translation. `translation.tex` follows the English, not the
original's pages; cite the Danish and let the translation follow.

Do not hand-edit markers into a file to "fill in" the gaps a run left. A gap is
a stretch where the aligner was not confident; guessing there is exactly the
error this whole exercise exists to remove. Leave it, and note it. If you do
establish one at the image, write it as `\opage`, which is what that means.

Do not convert Møller's existing `\opage` markers to `\apage`, or let a run
overwrite them. They were placed by hand at the page and they outrank anything
this tool produces.

Do not run `apply` on more than a book or two per session without looking at
the results. The failure mode is silent and uniform: a whole book confidently
paginated wrong.

Do not write scratch files into the repository. Render to a temp directory.
