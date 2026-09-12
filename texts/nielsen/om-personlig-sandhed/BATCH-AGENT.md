# Standing brief for a transcription batch subagent

> **The general method now lives in `../../../TRANSCRIPTION-PLAYBOOK.md`** at the repo
> root, generalised across every book here. This file is the book-specific prompt body
> for *Om personlig Sandhed og sand Personlighed*. If the two ever disagree, the
> playbook is the method and this is the instance.

Paste this file's body as the prompt for a `general-purpose` subagent, substituting the
page range. The agent starts cold, does one batch, and returns ~150 words. Everything
expensive — the OCR dump, the page images, the zooms — lives and dies in the agent's own
context window, so the calling conversation grows by only the summary.

## Running batches concurrently

Batches are independent — each touches exactly one marker line — so several can run at
once. But **concurrent agents must never edit `transcription.tex` directly.** `Edit` is a
read-modify-write over the whole file; two agents finishing within the same moment can
clobber one another, and the loser's pages vanish silently. Gap detection in `check.py`
would catch a whole missing batch, but not a half-written one.

Protocol for parallel runs:

1. Each agent writes its pages to a **fragment file**, `.parts/pp<FIRST>-<LAST>.texfrag`,
   containing exactly the text that will replace the marker line — beginning with its
   `% --- p. FIRST ---` marker. It does not touch `transcription.tex` at all.

   **The extension must be `.texfrag`, never `.tex`.** The repo Makefile builds every
   `.tex` it finds under `texts/`, and a fragment has no preamble and no
   `\begin{document}`, so a fragment named `.tex` makes `make` fail with
   `! LaTeX Error: Missing \begin{document}`. `splice.py` refuses to run if it finds
   `.tex` fragments.
2. Each agent verifies its own fragment: balanced braces, balanced `„`/`“` (or a logged
   printer's defect explaining the imbalance), a page marker for every page in range.
3. The **calling conversation** splices the fragments in, in page order, with
   `splice.py` — deterministic, no read-modify-write race, no context cost.
4. The calling conversation then runs `check.py` and the compile test over the whole file.

Substitute step 5 of the prompt body below with "write the fragment file" when running in
this mode, and skip the whole-file compile in step 6 (the fragment is not compilable on
its own; the caller compiles after splicing).

---

## PROMPT BODY (substitute FIRST, LAST, MARKER, LECTURE)

You are transcribing R. Nielsen, *Om personlig Sandhed og sand Personlighed: Tolv
Forelæsninger for dannede Tilhørere af begge Kjøn, holdte ved Universitetet i Vinteren
1854* (Kjøbenhavn: Gyldendalske Boghandling (F. Hegel), 1854), a Fraktur book, into an
existing LaTeX file. Do **one** batch: **printed pp. FIRST–LAST** (LECTURE). Work in:

    /Users/hhalvors/danish-texts/texts/nielsen/om-personlig-sandhed/

(In bash that directory is `/sessions/<id>/mnt/danish-texts/texts/nielsen/om-personlig-sandhed/`.)

### Before anything else
The scan lives in the `bibliotek` folder. If bash cannot see
`/sessions/*/mnt/bibliotek/Nielsen, Rasmus/om-personlig-sandhed.pdf`, call
`mcp__cowork__request_cowork_directory` with path `/Users/hhalvors/bibliotek` and wait for
it to mount. `pagemap.py` fails without it.

### Page map — never hard-code an offset
`pagemap.py` is the single source of truth. **Printed 1–144 → PDF + 9, uniformly — no
offset change anywhere in this book** (unlike evangelietroen-theologien, whose scan had a
double-scanned leaf mid-book). Every script here already calls `pagemap.py`.

### The embedded text layer is not trustworthy
This scan's own (PyPDF2/KB) text layer is a garbled OCR — systematic æ/ø corruption
throughout (e.g. "Msthetisk" for "Æsthetisk", "Sporgsmaal" for "Spørgsmaal", "vcrre" for
"være"). Never use `pdftotext` output as a source for transcribed words; it is only good
for the roughest structure-finding. Run your own Fraktur OCR with `ocr.sh` and treat the
image as the primary witness for every doubtful word, exactly as the playbook requires.

### Steps
1. `export TESSDATA_PREFIX=/tmp/tessdata`. If `/tmp/tessdata/Fraktur.traineddata` is
   missing, fetch it (see the OCR pipeline note in `RESUME-NOTES.md`).
2. `bash ocr.sh FIRST N` — Fraktur OCR for the batch. **Run this alone**, with a timeout of
   at least 240000 ms; a 12-page OCR takes ~2 minutes. **Note:** the sed table in `ocr.sh`
   is inherited verbatim from evangelietroen-theologien and has not yet been tuned against
   this book's own scan — expect more by-hand fixes on the first couple of batches, and
   add any new systematic confusions you find to the sed table for later batches.
3. `python3 spacing.py FIRST … LAST` — mechanical letterspacing detection. A **RUN** is
   nearly always real emphasis; a **single?** is often noise (short words, display
   headings) and needs the image.
4. Render and read the pages. Prefer **single-page** renders at 200 dpi over the two-up
   spreads. Read the image for every page — the OCR carries the words, but only the image
   carries paragraphing, footnotes, section rules and emphasis.
   To zoom, crop with PIL into the outputs folder and `Read` the crop from there; the
   sandbox `/tmp` is not visible to the file tools.

   **Render to a unique path, and never pick the file with `glob(...)[0]`.** `/tmp` is
   shared and litters: `pdftoppm -png /tmp/pg` leaves stale files behind, and a later
   `glob('/tmp/pg*.png')[0]` can silently return the wrong page. Use `mktemp -d` plus
   `pdftoppm -singlefile "$SCAN" "$D/page"`, which writes exactly one predictable file.
5. Write **all** pages of the batch to the fragment file `.parts/pp<FIRST>-<LAST>.texfrag`
   (see the concurrent-batches protocol above) — starting with `% --- p. FIRST ---`. Do
   **not** edit `transcription.tex` directly.
6. Verify your fragment: balanced braces, balanced quotes (or a logged defect explaining
   an imbalance), a page marker for every page in the batch.

### Transcription conventions
- 19th-century orthography exactly as printed: `Personlighed`, `Videnskaben`, `Kjøn`,
  `Forskjel`, `høiere`, `aa`, capitalised nouns. Do not modernise.
- Danish quotation marks `„…“` low-high, as printed. Em-dash as `---`.
- Letterspaced emphasis → `\emph{}`. Latin/foreign phrases set in antiqua against the
  surrounding Fraktur → `\textit{}`, checked per occurrence on the image (this book has
  not yet turned up any confirmed instance — flag the first one you find).
- Page markers: `% --- p. N ---` on its own line where printed page N begins. `check.py`
  reads these for gap detection, so every page in the batch needs one.
- Footnotes: this book's only confirmed footnote so far is on printed p.49, marked `*)`
  (matching evangelietroen's convention; `\thefootnote` is already set to `*)` in the
  preamble). If you find footnotes marked some other way, stop and flag it — do not
  silently reinterpret the preamble's convention.
- Each lecture opens directly with a drop-cap paragraph — **no italic "argument" summary**
  under the heading (unlike evangelietroen) and **no Indhold anywhere in this book** to
  cross-check the head against (see RESUME-NOTES.md). The heading style itself is a bare
  roman numeral ("I.", "II." …) plus the printed title — already set correctly in the
  skeleton from the image; if your batch's opening page reads differently from the
  skeleton's chapter heading, flag the discrepancy rather than silently editing the
  heading (the fix belongs in a review pass, scoped only to the heading line).
- If a reading stays doubtful after zooming, transcribe your best reading and flag it in
  your summary. Do not silently guess.

### Recurring Fraktur OCR errors (inherited list — verify against this scan)
`ocr.sh` fixes a starting set mechanically. Still fix by hand: `fan`→`kan`,
`beflageligt`→`beklageligt`, dropped `ø` (`gjore`→`gjøre`, `horer`→`hører`), long-s runs,
`0`↔`o`, `9`↔`y` (`udtr9ffelig`→`udtrykkelig`), and stray accents on ordinary letters. This
list has not yet been confirmed against *this* scan specifically — report anything new.

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
wrong. Do not return a fragment with unresolved items. If the scan has no usable
text layer this check does not apply; say so when you return.

### What to return
150 words at most: pages written; word count; the `\emph{}` and `\textit{}` decisions you
made and what image evidence settled them; any doubtful readings, with the alternative you
rejected; fragment self-check result (braces/quotes/page markers). **Do not** quote the
transcription back — it is already in the fragment file. Do not paste OCR output.

**Also report the `ocrdiff.py` result**: how many divergences it found, how many were transcription error (corrected), and how many were the scan's. If any remain unresolved, say which and why.
