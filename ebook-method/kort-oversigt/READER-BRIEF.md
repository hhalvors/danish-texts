# Reader brief: blind crop sheets for H. Høffding, *Oplevelse og Tydning* (1918)

(adapted 2026-10-14 from ebook-method/kort-oversigt/READER-BRIEF.md)

You are reading crops of a printed Danish book of 1918, set in antiqua (roman type), with period spelling: *Aaret*,
*Brevvexling*, *Iagttagelse*, *saadan*, capitalised nouns.  Passages and titles in French, Spanish, German, English,
Latin and some Greek occur, mostly in the footnotes (small type).  Your reading decides between machine readings you are **not shown**.  Read the print and nothing else.

## What you receive
Your instruction names sheet files, e.g. `b1-01 b1-02`.  Each is a PNG on Hans's computer:

    device path: /Users/hhalvors/danish-texts/texts/hoeffding/kort-oversigt/.render/kort-oversigt-<SHEET>.png

Stage them into your container with `mcp__remote-devices__device_stage_files` (all your sheets in ONE call; at most two
calls), then Read each staged image.  If two device calls fail, stop and report.  Each sheet is a column of crops; every
crop has a label `ID  p. N`, and one spot boxed in red.

## Blind means blind
Do not open anything else in the repo: not `transcription.tex`, not `.parts/` (checks, sheets-*.tsv, controls-*.tsv,
OCR), not the scan's text layer, not any e-book.  Do not guess what the "expected" reading is; some crops are controls
whose reading is known.  Write exactly what is printed, misprints included: never correct, modernise or complete a word.

## What to write, and where
One TSV file, written with `mcp__remote-devices__device_bash` (a heredoc, `cat > FILE <<'EOF2' ... EOF2`), rewritten
with ALL lines so far after EVERY sheet, so nothing is lost if you stop:

    ~/mnt/danish-texts/texts/hoeffding/kort-oversigt/.parts/reads/r-<TAG>-<YOURNAME>.tsv

`<TAG>` is the sheets' prefix (`b1`); `<YOURNAME>` is the letter in your instruction.  One line per crop, fields
separated by a TAB, the crop's ID first exactly as on its label (`b1-03-07`):

    ID ⇥ BOX ⇥ LINE ⇥ NOTE

- BOX: the boxed print exactly, with one word either side.
- LINE: the whole printed line the box stands in.
- NOTE: empty unless something is doubtful (`doubt: c or e`), damaged, or looks like a misprint (`misprint?`).
  A pen or pencil mark that is not print: say `pencil`.

Conventions in every field:
- Letters, punctuation and quotation marks exactly as printed.  This book quotes with guillemets » and « (»Ting«);
  write the ones you SEE, and say in NOTE if a mark is unclear.  — (long dash) and - (hyphen) are different.
- A stop, comma or colon: only if it is a printed mark of normal size on the baseline.  A speck or dirt is not a stop:
  leave it out and write `speck` in NOTE.
- A word broken at the line end: as printed, `Tænk-`.
- Do not write the space the printer sets before ; : ? ! (write `Grund;` not `Grund ;`).
- SMALL CAPITALS (a full capital, then small capitals) are rare here: if you see them, write the word in normal case
  inside `<sc>..</sc>`.  Words in full capitals of the same height (headings) are written in capitals, no `<sc>`.
- l e t t e r s p a c e d words: `<sp>..</sp>`, written unspaced.  Italic words: `*..*`.
- Greek letters as Greek (α β γ … and accents as printed); a superscript figure as `^3` (an edition number:
  *The Golden Bough*^3).  NOTE MARKS in this book are STARS with a parenthesis, after the word or its stop:
  `Jordskælv.*)`, `Koncentration**)`, `Værk.***)`; a footnote at the page foot begins with its label `*)` / `**)`.
  Count the stars carefully and write them as printed.  Some pages run on to daggers, `†)` `††)`: write them as printed.
- Accents exactly as printed: é and è are different (French titles: *Térèse*, *très*, *modèle*).
- Capital I and lower-case l look alike in this face: decide by height against the capitals beside them and say so in
  NOTE if unsure.  Danish ø is often worn: if you see any trace of the stroke, write ø.

## Other sheet kinds (the prefix of the sheet name tells you which)

- **i1** sheets (ITALICS): one line per crop, `ID ⇥ LINE ⇥ NOTE`.  LINE is the whole printed line through the red box,
  with every *italic* run between asterisks: `udkom *La psychologie anglaise contemporaine* 1870`.  A line with nothing
  italic has no asterisks.  Judge each word by the slant and shape of its letters (italic a, e, f, k, v, w differ in
  form, not only in slant); a stop or parenthesis after an italic word: say in NOTE whether it looks italic.
- **l1** sheets (LETTERSPACING, small type of the footnotes, mostly authors' names): one line per crop, `ID ⇥ LINE ⇥ NOTE`.  LINE is the whole
  printed line (the crop shows it with a sliver of the lines above and below: write only the middle, complete line),
  every l e t t e r s p a c e d word or run written unspaced between `<sp>` and `</sp>`:
  `henvise til <sp>Edmund König</sp>: W. Wundt.`  Italics as `*..*`.  A line with nothing spaced has no `<sp>`.

## Report back
When every sheet is done, report in at most 80 words: the file you wrote, its number of lines, and anything you could
not read.  Do not paste the readings into your report.
