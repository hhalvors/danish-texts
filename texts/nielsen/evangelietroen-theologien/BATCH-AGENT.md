# Standing brief for a transcription batch subagent

> **The general method now lives in `../../../TRANSCRIPTION-PLAYBOOK.md`** at the repo
> root, generalised from this file and applicable to any book here. This file is the
> book-specific prompt body for *Evangelietroen og Theologien*. If the two ever disagree,
> the playbook is the method and this is the instance.

Paste this file's body as the prompt for a `general-purpose` subagent, substituting the
page range. The agent starts cold, does one batch, and returns ~150 words. Everything
expensive — the OCR dump, the page images, the zooms — lives and dies in the agent's own
context window, so the calling conversation grows by only the summary.

**Why this exists.** The old rule was "fresh conversation every sitting," because images
and OCR text accumulate and get re-sent on every later call. Dispatching a subagent
achieves the same isolation without ending the conversation. Do not read the page images
in the main conversation.

## Running batches concurrently

Batches are independent — each touches exactly one marker line — so several can run at
once. But **concurrent agents must never edit `transcription.tex` directly.** `Edit` is a
read-modify-write over the whole file; two agents finishing within the same moment can
clobber one another, and the loser's twelve pages vanish silently. Gap detection in
`check.py` would catch a whole missing batch, but not a half-written one.

Protocol for parallel runs:

1. Each agent writes its pages to a **fragment file**, `.parts/pp<FIRST>-<LAST>.texfrag`,
   containing exactly the text that will replace the marker line — beginning with its
   `% --- p. FIRST ---` marker. It does not touch `transcription.tex` at all.

   **The extension must be `.texfrag`, never `.tex`.** The repo Makefile builds every
   `.tex` it finds under `texts/`, and a fragment has no preamble and no
   `\begin{document}`, so a fragment named `.tex` makes `make` fail with
   `! LaTeX Error: Missing \begin{document}`. This has already broken one build.
   `splice.py` refuses to run if it finds `.tex` fragments, and the Makefile now also
   excludes `.parts/`.
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

You are transcribing R. Nielsen, *Evangelietroen og Theologien* (Copenhagen 1850), a
Fraktur book, into an existing LaTeX file. Do **one** batch: **printed pp. FIRST–LAST**
(LECTURE). Work in:

    /Users/hhalvors/danish-texts/texts/nielsen/evangelietroen-theologien/

(In bash that directory is `/sessions/<id>/mnt/danish-texts/texts/nielsen/evangelietroen-theologien/`.)

### Before anything else
The scan lives in the `bibliotek` folder. If bash cannot see
`/sessions/*/mnt/bibliotek/Nielsen, Rasmus/1850-evangelietroen-theologien.pdf`, call
`mcp__cowork__request_cowork_directory` with path `/Users/hhalvors/bibliotek` and wait for
it to mount. `pagemap.py` fails without it.

### Page map — never hard-code an offset
`pagemap.py` is the single source of truth. Printed 1–83 → PDF +13; printed 84–174 → PDF
+15 (the leaf with printed 82–83 was scanned twice). Every script already calls it.

### Steps
1. `export TESSDATA_PREFIX=/tmp/tessdata`. If `/tmp/tessdata/Fraktur.traineddata` is
   missing, fetch it (see the OCR pipeline section of `RESUME-NOTES.md`).
2. `bash ocr.sh FIRST N` — Fraktur OCR for the batch. **Run this alone**, with a timeout of
   at least 240000 ms; a 12-page OCR takes ~2 minutes and `batch.sh` as a whole will time
   out if you run all its stages in one call.
3. `python3 spacing.py FIRST … LAST` — mechanical letterspacing detection. A **RUN** is
   nearly always real emphasis; a **single?** is often noise (short words, display
   headings) and needs the image.
4. Render and read the pages. Prefer **single-page** renders at 200 dpi over the two-up
   spreads: in a two-up each page is only ~650 px wide, which is not enough to settle a
   doubtful reading and forces a second zoom anyway. Read the image for every page — the
   OCR carries the words, but only the image carries paragraphing, footnotes, section
   rules and emphasis.
   To zoom, crop with PIL into the outputs folder and `Read` the crop from there; the
   sandbox `/tmp` is not visible to the file tools.

   **Render to a unique path, and never pick the file with `glob(...)[0]`.** `/tmp` is
   shared and litters: `pdftoppm -png /tmp/pg` leaves `pg-009.png` behind, and a later
   `glob('/tmp/pg*.png')[0]` will silently return that stale page 9 instead of the page you
   just rendered, because `009` sorts before `068`. This has already produced one confident
   verification of entirely the wrong page. Use `mktemp -d` plus
   `pdftoppm -singlefile "$SCAN" "$D/page"`, which writes exactly one predictable file.
5. Write **all** pages of the batch in **one** `Edit` call, replacing the marker line
   `MARKER` exactly. Do not read `transcription.tex` whole; `tail -60` it if you need to
   see the joint.
6. Verify: `python3 check.py` (expect no gaps, balanced braces and quotes, 0 suspect
   readings), then a compile test — copy the file to `/tmp`, `sed` out `libertinus`,
   `libertinust1math`, `textalpha` and `babel` (none are installed in the sandbox),
   substitute `lmodern`, and run `pdflatex -interaction=nonstopmode`. Expect 0 errors and
   0 missing-character warnings.

   Two false alarms this test produces, neither a defect in the file:
   - Garbled `æ ø å` in the *terminal log* is the terminal's encoding.
   - **`Unicode character … not set up for use with LaTeX` for every Greek letter.** That is
     caused by the `sed` above stripping `textalpha`, which the real preamble loads and the
     sandbox does not have. Before concluding anything, check that *all* errors are Greek:
     `grep '^!' log.txt | grep -v 'Unicode character'` must come back empty. To test the
     rest of the file properly, map Greek to a placeholder in the test copy
     (`re.sub(r'[Ͱ-Ͽἀ-῿]', 'G', s)`) and recompile — that should give 0 errors.
     **Never "fix" this by deleting Greek from `transcription.tex`.**

### Transcription conventions
- 19th-century orthography exactly as printed: `Christendommen`, `Videnskaben`,
  `Theologie`, `høiere`, `ueensartet`, `aa`, capitalised nouns. Do not modernise.
- Danish quotation marks `„…“` low-high, as printed. Em-dash as `---`.
- Letterspaced emphasis → `\emph{}`. Latin set in antiqua against the surrounding Fraktur
  → `\textit{}` (e.g. `in specie`, `Ecclesia est congregatio sanctorum…`).
- Page markers: `% --- p. N ---` on its own line where printed page N begins. `check.py`
  reads these for gap detection, so every page in the batch needs one.
- Each lecture's opening italic argument is printed at the head of the lecture in the book
  as well as in the Indhold. Verify the one already in the skeleton against the printed
  page and correct it if they differ.
- If a reading stays doubtful after zooming, transcribe your best reading and flag it in
  your summary. Do not silently guess.

### Recurring Fraktur OCR errors
`ocr.sh` already fixes a closed set mechanically. Still fix by hand: `fan`→`kan`,
`beflageligt`→`beklageligt`, dropped `ø` (`gjore`→`gjøre`, `horer`→`hører`), long-s runs,
`0`↔`o`, `9`↔`y` (`udtr9ffelig`→`udtrykkelig`), and stray accents on ordinary letters.

### What to return
150 words at most: pages written; word count; the `\emph{}` and `\textit{}` decisions you
made and what image evidence settled them; any doubtful readings, with the alternative you
rejected; `check.py` output; compile result. **Do not** quote the transcription back —
it is already in the file. Do not paste OCR output.
