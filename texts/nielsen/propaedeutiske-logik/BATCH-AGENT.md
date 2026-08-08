# Standing brief for a transcription batch subagent

> The general method lives in `../../../TRANSCRIPTION-PLAYBOOK.md`. This file is the
> book-specific prompt body for *Den propædeutiske Logik* (1845). If the two disagree,
> the playbook is the method and this is the instance.

Paste the PROMPT BODY below as the prompt for a `general-purpose` subagent, substituting
FIRST, LAST and MARKER. The agent starts cold, does one batch, and returns ~150 words.
The OCR dump, the page images and the zooms live and die in the agent's own context
window. **Do not read page images in the calling conversation** (one emphasis spot-check
per batch is the sole exception).

Batches are independent, so several can run at once — but **no agent may edit
`transcription.tex`**. Each writes `.parts/pp<FIRST>-<LAST>.texfrag`; the calling
conversation runs `python3 splice.py`, then `check.py`, then the compile test.
The extension must be `.texfrag`, never `.tex` (the repo Makefile builds every `.tex`
under `texts/` and a preamble-less fragment breaks the build).

---

## PROMPT BODY (substitute FIRST, LAST, MARKER)

You are transcribing R. Nielsen, *Den propædeutiske Logik* (Kjøbenhavn: P. G. Philipsen,
1845), a Fraktur book, into an existing LaTeX file. Do **one** batch: **printed pp.
FIRST–LAST**. Work in:

    /Users/hhalvors/danish-texts/texts/nielsen/propaedeutiske-logik/

(In bash that is `/sessions/<id>/mnt/danish-texts/texts/nielsen/propaedeutiske-logik/`.)

### Before anything else
The scan lives in the `bibliotek` folder. If `python3 pagemap.py --scan` fails, call
`mcp__cowork__request_cowork_directory` with path `/Users/hhalvors/bibliotek` and wait for
it to mount. Every script needs it.

### Page map — never hard-code an offset
`pagemap.py` is the single source of truth: **printed + 9**, uniform, body pp. 1–283 =
PDF 10–292. It is already verified three ways; do not re-derive it.

### Steps
1. `export TESSDATA_PREFIX=/tmp/tessdata` (the Fraktur model is already there; if
   `Fraktur.traineddata` is missing, stop and say so — do not try to fetch it).
2. `bash ocr.sh FIRST N` — Fraktur OCR for the batch. **Run this alone**, with a timeout of
   at least **300000 ms**: the scan is 105 MB and `pdftoppm` seeks slowly, ~6 s a page.
3. `python3 spacing.py FIRST … LAST` — mechanical letterspacing detection. A **RUN** is
   nearly always real emphasis; a **single?** is often noise and needs the image.
4. **Second witness, free:** `pdftotext -f P -l P -layout "$SCAN" -` gives the PDF's own
   ABBYY layer. It fails differently from tesseract (loses æ/ø, reads Fraktur I as J), so
   where the two agree the reading is safe and where they differ, look at the image.
5. Render and read **every** page at 200–300 dpi, single-page. The OCR carries the words;
   only the image carries paragraphing, the display heads, the rules and the emphasis.
   Use `mktemp -d` + `pdftoppm -f P -l P -r 300 -png -singlefile "$SCAN" "$D/page"`.
   **Never `glob('/tmp/pg*.png')[0]`** — `/tmp` is shared and `009` sorts before `068`,
   so you will silently verify the wrong page. This has happened.
   To zoom, crop with PIL into the **outputs** folder and `Read` the crop from there; the
   sandbox `/tmp` is invisible to the file tools. **Never write a scratch file — above all
   a PNG — inside the repo.** Clean up your crops when you are done.
6. Write the batch to `.parts/ppFIRST-LAST.texfrag` — exactly the text that will replace
   the marker line `MARKER`, beginning with `% --- p. FIRST ---`. Do **not** touch
   `transcription.tex`.
7. Verify your own fragment before returning: a `% --- p. N ---` for every page in range,
   balanced braces, balanced `„`/`“` (or a logged printer's defect that explains the
   imbalance). Do not compile — the caller runs `bash verify.sh` after splicing.
   **Do not introduce a raw non-ASCII character that the preamble does not already
   handle.** Anything new — an unusual dash, a symbol, a diacritic the book uses once —
   must be reported, not just typed: it will be fatal on the user's machine while looking
   fine in the sandbox. Already available, type these RAW and do not use accent commands:

   - Danish `æ ø å Æ Ø Å` and the Danish quotes `„ “`
   - **German `ß ä ö ü Ä Ö Ü`** — T1 fontenc covers these natively (tested). Much German
     follows in the Anden Deel; keep it raw and readable, not `\ss{}` / `\"u`.
   - polytonic Greek **base** letterforms, via `textalpha` (but see the normalisation rule)
   - `\dsi` for the id-est sign ɔ: — `ɔ` needs `\DeclareUnicodeCharacter` and is set up
   - `\&c.` for the Fraktur r-rotunda *et cetera*; raw U+A75B ꝛ is NOT available (tested)

### Use the preamble macros — do not hand-roll display heads
Defined in `transcription.tex`; `check.py` counts them and flags hand-rolled
`\begin{center}` heads as suspect.

| Printed form | Write |
|---|---|
| Part opening (double rule + "Den propædeutiske Logiks" + Deel line + argument) | `\deel{Første Deel:}{Læren om det subjective Begreb.}` |
| Chapter head (bold letterspaced label + argument one size down) | `\capitel{Første Capitel.}{Det subjective Begrebs Dannelse.}` |
| `§ N.` centred, then centred bold letterspaced argument | `\parag{1}{Almeenforestillingen.}` |
| The bold letterspaced `A n m. 2.` lead-in | `\anm{2} Text of the remark…` |
| `Indledning.` as a top-level division (pp. 1 and 97) | `\division{Indledning.}` |
| The Indledning's roman-numeral sections (I., II.) | `\romsec{I.}{Den formelle og speculative Logik.}` |
| The Danish "that is" sign ɔ: | `\dsi` (never a plain `o:`, never the raw character) |

If you need a head form that has no macro, **do not hand-roll an `\addcontentsline` with a
bare `\quad` in it** — hyperref rejects it and warns on every build. Wrap the argument in
`\texorpdfstring{…\quad …}{… …}`, as every existing head macro does, or better, report
the new form and let the caller add a macro for it.

### What this book does and does not have
- **No footnotes at all.** Confirmed on the image and by a type-size sweep of all 283
  pages. References are inline in parentheses. The `3*`, `12*`, `18*` at some page feet
  are **signature marks**, not note marks — do not transcribe them.
- **`Anm.` remarks are NOT smaller type.** Measured on printed p. 7: the baseline pitch is
  identical to body text. Only the lead-in is distinguished. The remark runs on as an
  ordinary indented paragraph and simply ends — nothing marks where.
- **No figures, no tables, no displayed equations.** Inline antiqua symbols only
  (`A=A`, `A er ei = --- A`, A/B/C placeholders). Set these in `\textit{}`, not math mode,
  unless a real relation makes math mode clearer.
- **Polytonic Greek occurs inline** (pp. 138, 147, 179, 187, 241, …). Type it as raw
  Unicode; `textalpha` renders it. Zoom-verify every Greek string; breathings and accents
  matter (see the errata).
  **NORMALISE THE FOUNT'S VARIANT LETTERFORMS.** This book's Greek fount prints theta as
  the script `ϑ` and sometimes kappa as the cursive `ϰ`. Type them as plain **θ** and
  **κ**, with a `%` note at the site. This is the repo's standing convention (see
  `texts/nielsen/religionsphilosophie/transcription.tex`) — they are fount variants, not
  distinct letters, exactly as we render Fraktur in a roman face rather than reproducing
  its letterforms. It is also a hard build requirement: `ϑ` (U+03D1) and `ϰ` (U+03F0) are
  **fatal errors** under `textalpha`/`greek-fontenc` in text mode. This has already broken
  the user's build once. Same for `ϕ ϖ ϱ ϐ ϵ ϲ` → `φ π ρ β ε σ`.
  Accents and breathings are NOT fount variants — reproduce those exactly as printed.
- **No running heads** in the original — only a centred bold antiqua folio at the head.
  Do not transcribe folios.

### Transcription conventions
- **The ABBYY layer turns every Fraktur `x` into `r`.** Tesseract garbles it differently
  (`forverles` for `forvexles`). The Fraktur x is identifiable at 600 dpi by its right leg
  dropping below the baseline. Suspect any word where `r` makes no sense.
- **If your first page completes a word broken at the previous page's foot, verify that
  word on the image yourself.** Do not trust the joint word as given in your brief or in
  RESUME-NOTES — it may have come from an agent that never read your page. This has already
  produced one wrong reading (`ligesaa` for `ligefremme` at the p. 53/54 joint).
- 19th-century orthography exactly as printed: `Christendommen`, `Videnskaben`,
  `Theologie`, `høiere`, `aa`, capitalised nouns. Do not modernise.
- Danish quotation marks `„…“` low-high, as printed. Em-dash as `---`.
- Letterspaced emphasis → `\emph{}`. Latin, French, English and all figures set in antiqua
  against the surrounding Fraktur → `\textit{}`. German *quotations* are in Fraktur (no
  italic), but Latin words inside them are antiqua → `\textit{}`. Emphasis follows the
  page, not the word: the same name may be antiqua on one page and Fraktur on the next.
- The Fraktur double-hyphen `=` in compounds (`Dyre=Rige`, `Ikke=Jeg`) is printed as `=`.
  Keep it as `=`; do not silently turn it into `-`.
- Page markers: `% --- p. N ---` on its own line where printed page N begins.
- **Printer's defects: transcribe as printed**, log a `%` comment at the site, and report
  it. Do not correct the compositor silently. The quote balance is allowed to drift off
  zero as a result — that drift is the signal.
- **Errata are different**: the nine `Rettelser` corrections ARE applied, each flagged with
  a `% ERRATA` comment. The list is in the header of `transcription.tex`. Check whether any
  fall in your range (pp. 80, 92, 93, 112, 152, 154, 187, 206, 241).
- Doubtful readings: zoom, transcribe your best reading, and flag the alternative you
  rejected. Never silently guess.

### Recurring Fraktur OCR errors on this scan
`ocr.sh` fixes a closed set mechanically. Still fix by hand: `f`/`k` inside words
(`Adſfillelſe`→`Adskillelse`), `v` read as `o` (`ſelo`→`selv`), dropped `ø`
(`Sporgsmaal`→`Spørgsmaal`, `gjore`→`gjøre`), `B`/`V` (`BVillede`→`Billede`), `d`/`b`
confusion, `0`↔`o`, `9`↔`y`. `--psm 6` also picks up the facing leaf's black edge as a
column of stray `|`, `l`, `i`, `:` at the right margin — ignore it.

**Scan caveat:** printed p. 96 (PDF 105) carries a previous reader's yellow highlighter
across the Sibbern quotation. It is not a printing feature.

### What to return
150 words at most: pages written; the `\emph{}` / `\textit{}` decisions you made and what
image evidence settled them; any printer's defect logged; any errata applied; any doubtful
reading with the alternative you rejected; your fragment's own brace/quote counts.
**Do not** quote the transcription back — it is in the fragment. Do not paste OCR output.
