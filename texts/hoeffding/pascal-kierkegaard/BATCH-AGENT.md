# Batch-agent brief — Høffding, « Pascal et Kierkegaard » (1923)

> **The job is to transcribe these pages _and establish that the transcription
> is accurate_. Those are not two jobs.** A fragment whose words have not been
> compared against a second reading of the page is not finished work, however
> clean its structure, its emphasis and its markup are. You are already
> rendering the pages and already hold the OCR: checking your own words against
> them is the cheapest thing you will do in this batch. Deferred, the same check
> costs a second transcription — that is not hypothetical, it is what *Den
> menneskelige Tanke* cost, ~350 errors found by forty agents re-reading all 392
> pages, to recover what the first agents had in context and discarded.
> See "Diff your fragment against the scan before you return it", below.



Paste the body below into a subagent, filling in PAGE RANGE and MARKER.
One agent per batch. Agents run concurrently and **must not edit
`transcription.tex`** — each writes a fragment; the caller splices.

Read `../../../TRANSCRIPTION-PLAYBOOK.md` §0 and §3 if anything here is unclear.

---

You are transcribing printed pages **FIRST–LAST** of Harald Høffding's article
« Pascal et Kierkegaard », *Revue de Métaphysique et de Morale* 30:2
(avril–juin 1923), pp. 221–246.

Working directory: `texts/hoeffding/pascal-kierkegaard/`.

**This article is in French.** Høffding wrote it in French for the Pascal
tercentenary number; it is not a translation. Set it as printed.

## Method

1. `bash ocr.sh FIRST N` gives you tesseract `-l fra` output for the range.
   That is your *first* witness and it carries the words.
2. Render each page and **look at it**:
   `pdftoppm -f $(python3 pagemap.py P) -l ... -r 300 -png -singlefile "$(python3 pagemap.py --scan)" $TMP/pg`
   — into `mktemp -d`, **never** into the repo. The image is the only witness
   for italics, paragraphing, footnote rules, and the section numerals.
3. Write `.parts/pp<FIRST>-<LAST>.texfrag` — the text replacing the marker.
   **`.texfrag`, never `.tex`**: the repo Makefile builds every `.tex` under
   `texts/` and a preamble-less fragment breaks it.
4. Report back in ~150 words: pages done, doubtful readings, printer's defects,
   anything structural the skeleton got wrong. **Do not paste the transcription
   into your reply.**

## Conventions

- **Diplomatic.** 1923 French orthography exactly as printed. Printer's errors
  transcribed *as printed*, with a `%` comment at the site. Never silently correct.
- Page markers: `% --- p. N ---` on its own line where printed page N begins.
  Every page in your range needs one; `check.py` depends on them.
- Quotation marks: the journal's **« … »**, as printed, with the French
  spacing it actually uses. Nested quotes “ … ” if that is what is set.
- Em-dash `---`. Do not convert the journal's dashes to `--`.
- Italics → `\emph{}`. **OCR cannot see italics** — read every one off the image.
  Expect them on titles, on Danish and Latin words, and on Høffding's emphases.
- **Danish quotations from Kierkegaard**: wrap in `\dk{...}` (defined in the
  preamble). Transcribe the Danish exactly as the 1923 journal sets it — with
  `aa` where it prints `aa`, and with whatever accidentals it has. This is
  Høffding quoting; it is not our job to correct his Danish or his citations.
  Tesseract's French model has no æ/ø/å, so **every** Danish word must be read
  off the image, not taken from the OCR.
- Greek, if any, typed directly as Unicode (`textalpha` is loaded). Never
  delete Greek; never transliterate it.
- Footnotes: `\footnote{}`, with the printed mark recorded in a `%` comment.
  Note the journal's own footnote numbering scheme when you meet the first one
  and report it — the preamble may need a `\thefootnote` fix.
- Doubtful reading: zoom, transcribe your best reading, and flag the rejected
  alternative in your report. **Never silently guess.**
- **Section heads.** The article is in four parts. The skeleton does NOT mark
  them — the OCR cannot see them. If a section numeral (I, II, III, IV, or
  whatever the journal actually sets) appears on one of your pages, set it as
  `\section*{...}` at the right point in your fragment and say so in your
  report, with the printed page. If none appears in your range, say that too.

## Traps

- `glob('/tmp/pg*.png')[0]` returns a **stale page from another agent**.
  Always `mktemp -d` + `pdftoppm -singlefile`.
- The scan is the whole 200+ page issue, not just this article. Trust
  `pagemap.py`; do not count pages by hand.
- Høffding's own French is idiosyncratic in places and a native editor may have
  left it alone. Do not smooth it.

---

### Copy-text discipline — read this before you write a word

You are copying, not composing. Where the text layer and the page agree, the
words are already settled, and your job is to carry them across unchanged —
including every word you would have phrased differently, every spelling that
looks like a mistake, and every short word you might not notice dropping.

This is not a hypothetical risk. Collating *Den menneskelige Tanke* against its
scan in 2026 found about **0.9 errors per page** through the whole book, and
two-thirds of them were readings the OCR had already got right. They were
introduced between the OCR and the file, by agents doing exactly this job.
The four ways it happened:

- **dropped short words that leave grammatical Danish behind** — *kun*, *ikke*,
  *ny*, *og*, *saa*. One page read "Disse to Emner kunne reduceres til hinanden"
  where the page prints **ikke** reduceres: the opposite of the original, and it
  read perfectly well.
- **archaic forms modernised.** The 1910/19th-c. orthography is data.
  `egentligt`, `navnligt`, `stadigt`, `oprindeligt`, `gensidigt`,
  `selvfølgeligt`, `i Regelen`, `Principet`, `stansede` are correct as they
  stand. Do not strip a trailing *t*, do not double a consonant, and never
  assume an archaic form is OCR noise.
- **printer's errors silently corrected.** If the PAGE is wrong — a broken
  letter, a transposed pair, a misspelt name — transcribe it **as printed** and
  log it in a `%` comment at the spot. Never silently correct the print. If you
  find yourself about to fix something, that is the moment to write a comment
  instead.
- **paraphrase of a whole clause.** If you are reconstructing a sentence from
  its sense, stop and look at the page.

When you are unsure between two readings, do not pick the one that reads better.
Render the page and look.

### Diff your fragment against the scan before you return it

Structural checks cannot see a missing „ikke“. This one can, and it costs
nothing:

```sh
python3 ../../../ocrdiff.py --frag .parts/pp<FIRST>-<LAST>.texfrag
```

It prints every place your words diverge from the OCR's, with three exactly
matching words on each side, labelled by class (`dropped word`, `adverbial -t
dropped`, `form modernised?`, `likely OCR`). Expect roughly ten items on a
thirteen-page batch, and expect about half to be the scan's fault. **Settle
every one at the image** — correct your fragment, or satisfy yourself the OCR is
wrong. Do not return a fragment with unresolved items.

This book's scan has **no usable embedded layer**. Build the witness yourself:
run tesseract over your pages with the model named above, write it to
`.parts/ocr/pp<FIRST>-<LAST>.txt`, and pass `--ocr .parts/ocr/pp<FIRST>-<LAST>.txt`.
It will be noisier than ABBYY — more candidates will be the witness's fault.
That is the cost of the step, not a reason to skip it.

There is no version of this job that skips the check. If you believe your
book is an exception, stop and say so rather than returning unchecked words.

*(This brief predates the PROMPT BODY convention; include the two
sections above in whatever prompt you give the batch agent.)*


**Report the check, in exactly this form**, as the last line of your return:

```
OCRDIFF: <witness> | <n> candidates | <n> corrected | <n> witness's fault | <n> unresolved
```

e.g. `OCRDIFF: embedded | 11 candidates | 4 corrected | 7 witness's fault | 0 unresolved`.
Unresolved must be 0. The caller cannot tell "found nothing" from "never ran" unless you say.
