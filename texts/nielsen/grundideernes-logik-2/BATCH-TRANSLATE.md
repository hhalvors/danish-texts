# Batch brief: translating R. Nielsen, *Grundideernes Logik. II.* (Kjøbenhavn 1866)

You are translating one batch of a 19th-century Danish work of speculative logic
into English. The Danish is settled: `transcription.tex` has been transcribed in
full and diffed against the scan's text layer. **Translate from it, never from a
page image, and never re-transcribe.** Do **one** batch: the printed pages you
were given.

The job is to translate those pages **and to establish that nothing was lost**.
Those are not two jobs. A fragment whose counts have not been checked against the
Danish is not finished.

## Paths

Everything happens on Hans's computer through `mcp__remote-devices__device_bash`.
Do not use the container's `Bash`, do not use Read/Write/Edit on repository
paths, and do not touch anything outside this directory.

```sh
cd $HOME/mnt/danish-texts/texts/nielsen/grundideernes-logik-2
python3 tslice.py FIRST LAST      # your Danish, with context before and after
python3 tslice.py front           # the roman front matter, for the pp. 0--0 batch
cat .parts/tr/GLOSSARY.md         # READ THIS FIRST -- terminology locked to Vol. I
```

`tslice.py` prints three zones. Translate **only** the middle one. The zones are
cut exactly at `\opage{}`, so the batch before yours has already done everything
above your first marker and the batch after yours will do everything below your
last: never translate into a neighbour's territory, and never leave a gap at the
seam. Your fragment's first character belongs to `\opage{FIRST}`.

## Output

Write exactly one file:

```
.parts/tr/tr-pp<FIRST>-<LAST>.texfrag
```

The `.texfrag` extension is mandatory — the repo Makefile builds every `.tex` it
finds, and a fragment has no preamble. Do **not** edit `translation.tex`, and do
not touch another batch's fragment: a dozen agents are running at once and the
caller splices.

Begin the fragment with `% --- p. FIRST ---` only if the Danish has that comment
at the head of your span; otherwise begin straight with `\opage{FIRST}`. Carry
the Danish's `% --- p. N ---` comment lines across for every page, and put
`\opage{N}` at the point in the **English** where page N begins — the
corresponding point, not the same word count. Keep the translation paragraph for
paragraph with the Danish: same number of paragraphs, same order, same breaks.

If your span begins mid-sentence (it usually does), begin the English
mid-sentence too, with no capital and no blank line above it. The seam is joined
by the splicer, not by you, and the context zone shows you what it has to join to.

## Conventions

`GLOSSARY.md` in `.parts/tr/` is binding: it is Volume I's finished English, and
Volumes I and II must read as one translation. Volume II's page 1 continues
Volume I's lettering. Read the glossary before you translate a word of this.

Beyond it, `../../../TRANSLATION-PLAYBOOK.md` §2 is the standing method. In brief:

- **Register.** Scholarly, moderately literal, readable. Nielsen's syntax is long
  and nominalized; keep it. Keep his compound coinages as hyphenated English
  compounds (knowledge-concept, idea-movement, unity-in-opposition) rather than
  paraphrasing them into phrases.
- **Emphasis.** Every `\emph{}` in the Danish gets an `\emph{}` on the
  corresponding English words. Carry them all: the counts are checked.
- **Quotation marks.** Danish `„ … “` becomes ``` `` … '' ```. No Unicode curly
  quotes. Guillemets around a foreign term Nielsen keeps foreign stay as printed.
- **Greek** is copied verbatim, polytonic, unmarked — not italicized, not
  transliterated, not glossed. **Latin tags** are set roman and unmarked
  (*a priori*, *per se*): `\emph` marks Nielsen's emphasis, not foreign words.
  Keep the Danish's `\textit{}` where it marks antiqua against the Fraktur.
  **German and French quotations** stay in the original, untranslated.
- **Footnotes** stay at the same anchor word. Translate the note's prose;
  keep Danish work-titles and volume/page references exactly as Nielsen cites
  them (`Gr.\ L.\ I, 442`, `Phil.\ Propæd. p.~72.`). Drop the Danish file's
  `% note *)` comments.
- **`ɔ:`** renders as *i.e.*; `d.\ v.\ s.` as *i.e.*; `o.\ s.\ v.` as *etc.*;
  `f.\ Ex.` as *e.g.*; `Jfr.` as *Cf.*
- **Em dash** `---`. A centred rule between sections stays
  `\begin{center}---\end{center}`.
- **Headings.** Reproduce the Danish's form exactly — centred heads centred,
  run-in heads run in — and translate any `\addcontentsline` that goes with one.
  The lettered ladder and its toc depths are in the glossary's house-style
  section. `1) 2) 3)` items are run-in paragraph openers, not headings.
- **Names** unchanged (Spinoza, Hegel, Kant, Strauß, Kierkegaard, Martensen).

## What NOT to carry over

The Danish is a diplomatic transcription of a book with printer's errors in it.
The English is not.

- Do not copy `% PRINTER:`, `% UNSURE:`, `% SEAM:` or `% note` comments.
- Translate the **sense**, correcting the printer's slip silently — except where
  the book's own errata list covers it. **If your span includes p. 79, 125, 130,
  139, 194, 195, 282, 305, 315, 398 or 400**, the 1866 errata correct a word on
  that page; translate the corrected reading and add a one-line
  `% Errata: p. N — printed "X", corrected to "Y"; translated as corrected.`
  The list is in the header of `translation.tex`.
- **p. 55** carries a footnote with Hebrew. Give the Hebrew in romanized
  transliteration with a bracketed English gloss, and add
  `% Hebrew: transliterated; no Hebrew font in this build.` Do not put Hebrew
  characters in the file.

## Before you return (mandatory)

```sh
python3 trcheck.py FIRST LAST          # or: python3 trcheck.py front
```

It compares your fragment against the Danish span: paragraph count, `\opage`,
`\footnote`, `\emph`, `\textit`, centred blocks, Greek runs, character ratio,
page markers present and ascending, braces balanced, and leaks of Danish
punctuation. **Every mismatch is a dropped paragraph, a lost emphasis or a
skipped footnote until you have proved otherwise.** Fix your fragment and re-run
until the only discrepancies left are ones you can name and defend in one clause
(a legitimate one: English needing 0.83 of the Danish's characters in a span
thick with compounds; almost nothing else is).

Then compile-test the fragment: copy `translation.tex`'s preamble to a file in a
`mktemp -d` directory, append your fragment and `\end{document}`, `sed` out
`libertinus`, `libertinust1math` and `textalpha`, replace `[english]{babel}` with
`{babel}`, map Greek to `G` **in the test copy only**, turn microtype expansion
off, and run `pdflatex -interaction=nonstopmode`. Expect 0 `^!` errors. Never
write scratch files inside the repository.

## What to return (150 words at most)

The pages written; any heading you set, with its English; the two or three
terminology choices a reader could reasonably second-guess, especially any
departure from `GLOSSARY.md` and any term the glossary marked
`(not in Vol. I)`; `% Errata:` sites; anything in the Danish you could not
construe; the compile result. Do not quote the translation and do not paste the
Danish. Make the **last line** exactly:

`TRCHECK: tr-pp<FIRST>-<LAST>.texfrag | <n> discrepancies | <one clause naming them, or "none">`
