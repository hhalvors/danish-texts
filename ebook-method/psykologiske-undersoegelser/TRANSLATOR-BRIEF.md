# Translator brief — Harald Høffding, *Psykologiske Undersøgelser* (1889) → English

You translate one part of this book from its Danish LaTeX transcription into English LaTeX.  The Danish is the text of
record: a transcription of the 1889 printing, collated against the scan.  Your part's Danish is in the file you are
given (made by `tr_parts.py extract PART`).  Read it from there, in chunks; do not read any other part, and do not look
at any other translation or e-book.  The terms are fixed in **GLOSSARY.md** (given with this brief): read it first and
follow it; it also gives the English of every heading and of the title page.

The book: a psychological treatise (103 pp.) published by the Royal Danish Academy, continuing Høffding's *Psykologi i
Omrids* (1882, 2nd ed. 1885), which he cites as „min Psykologi“.  Introduction (§§1-2); I. immediate recognition and the
„quality of familiarity“, against Lehmann's and Löchen's expectation theory, with a long critique of Alfred Lehmann's
experiments (§§3-14); II. the presuppositions of association by contiguity (§§15-18); III. free association by
similarity, against attempts to reduce it to contiguity (§§19-25); IV. association of ideas and comparison (§§26-29);
V. the concept of psychical activity (§§30-33); VI. psychical and physical activity, the identity hypothesis (§§34-37);
VII. the conformity to law of psychical activity, determinism, Kroman (§§38-42).  Clear, argumentative scientific prose;
experimental details; formulas in letters (A, a, b, β, a₁ + a₂).

## What you write

One LaTeX fragment (no preamble), at the path you are given, mirroring the Danish 1:1:

- **Comments.** The Danish has `%` comments (editorial notes, some at the END of a text line, e.g.
  `Spiritualisme. men af ... % PRINTED AS IS (...)`).  Do not translate or copy them, with two exceptions: copy every
  page-marker comment `% --- p. N ---` on its own line exactly where it stands; and where a comment says
  `PRINTED AS IS` and the misprint affects the sense, translate the intended sense and put, on its OWN line just
  before the line concerned, `% print: <the Danish words> (misprint)`.  Never put a `%` comment at the end of or
  inside a line of text.
- **Page turns.** The Danish marks each printed page with three lines/items:
  ```
  % --- p. 42 ---
  \setcounter{footnote}{0}%
  \opage{42}ger, hvor der ...
  ```
  Reproduce them: the `% --- p. N ---` line and the `\setcounter{footnote}{0}%` line exactly as they are (that line,
  and only that line, may end in `%`), and `\opage{N}` immediately before the English word that corresponds to the
  first word of printed page N (approximately, where the syntax is rearranged).  Every `\opage{N}` of your Danish
  appears exactly once in your English, in order.  A word broken over a page turn (`efter%` … `\opage{68}tryk`) is one
  word: put the marker before the English word.  **Never end a line of English text with `%`.**
  A footnote that runs over to the next page is set whole at its mark, with that page's `\opage{N}` INSIDE the note
  (and the page's `% --- p. N ---` / `\setcounter` lines somewhere after it in the text): keep `\opage{N}` inside the
  English note at the corresponding word, and the other two lines where the Danish has them.
- **Footnote anchors.** The Danish sets a note as `bundet til%` / `% footnote 1) on p. 30` / `\footnote[1]{...}. Det er`:
  the word, the mark and the text after the note's `}` are one run of text.  In English write
  `bound\footnote[1]{...}. It is` (the `\footnote` directly after the anchor word, no `%`, no comment line).
- Where a Danish line ends in `}%` or `}% a comment` after a footnote, and the next line goes on with `. Carl Vogt` or
  `, og`, that is one line of text: in English write the text after the `}` on the SAME line (no `%`).
- **Paragraphs** exactly as in the Danish: a blank line where the Danish has one, none where it has none (a paragraph
  running over a page turn stays one paragraph).
- **Headings.** `\begin{center}\large I. Umiddelbar Genkendelse.\end{center}` → `\begin{center}\large I. Immediate
  Recognition.\end{center}` (GLOSSARY.md, "Headings"); `\begin{center}\rule{...}\end{center}` lines copied unchanged.
  The numbered paragraphs (`10. Den anførte Paastand ...`) keep their numbers at the start of the paragraph.
- **Front matter** (part A only): the title page and the Indhold (`\tocline{I.}{Umiddelbar Genkendelse}{8.}`) as in
  the Danish, with the English of GLOSSARY.md; the `% --- p. 1 --- (title)` and `% --- p. 3 --- (contents)` lines copied
  as they are; the `% CHECK: ...` comment block is not copied.
- **Formulas** `$\left({a\atop A}\right)$`, `\textit{A}`, `\textit{a}\textsubscript{1}`, `\textit{β}`: copy them
  character for character (they are letters, not words).
- **Verse** (the Danish ballad on p. 55, „En Humleranke alene i Haven ...“): translate each line in the text, as a
  line of its own as in the Danish, and put the Danish line in a comment on its OWN line just after it.
- **Footnotes** `\footnote[N]{…}`: same number N, at the same anchor word, translated whole.  The notes per printed page
  must equal the Danish.
- **Emphasis** `\emph{…}` (letterspacing in the print): carry every one over to the corresponding English words, one
  `\emph` for one `\emph`.  `\textit{…}`: likewise.  Add none.
- **Quotation marks.** This print uses «…» (and sometimes „…“) → ``…'' in LaTeX; a quotation inside a quotation →
  `…'.  One opening mark for one opening mark.
- **Foreign languages.** What Høffding quotes or names in German, Latin, French or Greek stays in the original,
  character for character, set as in the Danish (upright, in quotation marks where he has them; Greek glyphs
  verbatim, never transliterated, never italicized).  Do not add an English gloss.  What he writes in Danish —
  including his own Danish renderings of German authors, in quotation marks — is translated from his Danish.
- **Titles of books and journals** stay as printed (German, Danish …): „Kritik der reinen Vernunft“ →
  ``Kritik der reinen Vernunft''.  Do not translate titles.
- **Names** as printed (Lehmann, Löchen, Kroman, Wundt, Maine de Biran, James Ward), with the English possessive
  (Lehmanns → Lehmann's).  Exceptions: the Danish forms of ancient names → English (Aristoteles → Aristotle, Platon →
  Plato); Tydskland → Germany; Kjøbenhavn → Copenhagen; well-known places in English form.
- Dashes `---` stay `---` (Høffding ends many paragraphs with „. ---“: keep it); `ɔ:` → "i.e."; `d. v. s.` → "i.e.";
  `f. Ex.` / `f. Eks.` → "e.g."; `o. s. v.` → "etc."; `Smlgn.` / `Jfr.` → "Cf."; `2. Udg.` → "2nd ed."; `S.` (Side) → "p."; `p.`, volume numerals and page numbers in citations exactly as printed; `\dots` stays;
  formulas (`$…$`) character for character.
- **Spelling: American** (color, labor, realize, center, skeptical).

## Register

Faithful, readable scholarly English of a kind a philosopher today would read with pleasure: precise, unadorned.
Translate every sentence; never summarize, smooth away, add or explain.  Keep Høffding's emphasis and, where English
allows, his long sentences and their order of thought; break a sentence only when English demands it.  The terms are
the glossary's: a term the glossary fixes is never varied for elegance.  A Danish word the glossary does not list:
choose its plain English and keep to it within your part.

## While you translate: the odd-spots list

Translating is also a second reading of the Danish.  Write a TSV `odd-<PART>.tsv` next to your fragment, one line per
doubtful spot in the DANISH: `page <TAB> the Danish words exactly as in the file (3-6 words) <TAB> the doubt`.  List ONLY
what could be a fault of the transcription or an unrecorded misprint: a non-word, a letter that makes the wrong word
(kun/kan, har/var, til/vil, en/et, de/det, ham/kam, før/for), a missing or doubled word, an ending that breaks the grammar,
punctuation that breaks the sense (a point for a comma), a paragraph break that looks wrong (inside a sentence), a
quotation mark or parenthesis that does not close, a German word misspelt.  Do NOT list the period's spelling (aa,
capitalized nouns, Philosophi, Erkjendelse, kunde, ere, gaaer, Grændse, qv, x for ks, -ts for -z) and do NOT list spots a
`%` comment already settles.  Do not stop to resolve them; just list them, and translate the evident sense.

## Mechanics

Work in chunks of two or three printed pages; append each chunk to your fragment file as you finish it (with Bash:
`cat >> FRAGMENT <<'EOF'` … `EOF`, so you never re-send the whole file), so nothing is lost.  Container tools only
(Read, Bash, Write, Edit: no remote-device tools, no web).  When finished, check your fragment with the book's script:

```
python3 tr_parts.py build --book BOOKDIR --parts OUTDIR      # paths given with your task
```

It must print `OK` for your part (lines marked `(soft)` are for information: look at each and fix what is a real slip;
a German quotation the Danish marks with „ but no closing mark, for instance, explains a quote difference).  Also:

```
grep -n '%$' FRAGMENT | grep -v ':%' | grep -v 'setcounter{footnote}{0}%$'    # must print nothing
```

Reply with ONE line: `part: …, pages N–M, opage K, footnotes F (Danish F'), build: OK|problems, odd spots S`, and on a
second line, at most three term choices you made that the glossary did not settle (Danish = English).
