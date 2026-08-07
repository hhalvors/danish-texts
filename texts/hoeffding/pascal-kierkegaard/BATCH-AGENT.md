# Batch-agent brief — Høffding, « Pascal et Kierkegaard » (1923)

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
