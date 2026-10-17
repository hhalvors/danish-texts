# Translator brief — Harald Høffding, *Kort Oversigt over den nyere Filosofis Historie* (4th ed., 1910) → English

(adapted 2026-10-17 from ebook-method/religioese-tanketyper/TRANSLATOR-BRIEF.md)

You translate one part of this book from its Danish LaTeX transcription into English LaTeX.  The Danish is the text of
record: a diplomatic transcription of the 1910 printing, collated against the scan.  Your part's Danish is in the file
you are given.  Read it from there, in chunks; do not read any other part, and do not look at any other translation or
e-book.  The terms are fixed in **GLOSSARY.md** (given with this brief): read it first and follow it; it also gives the
English of every heading.

The book: Høffding's short textbook of the history of modern philosophy for the propædeutic course at the University of
Copenhagen (English title: *A Short Survey of the History of Modern Philosophy*, Hans, 2026-10-17): an introduction on
the four philosophical problems; the origin of modern philosophy in the Renaissance; the systems (Descartes, Hobbes,
Spinoza, Leibniz); the philosophy of experience (Locke, Berkeley, Hume); the Enlightenment; Kant; Romanticism (Fichte,
Schelling, Hegel, Schopenhauer, Kierkegaard, Feuerbach); positivism (Comte, Mill, Darwin, Spencer); recent treatments of
the four problems, with an appendix on the history of the causal principle.  Compact teaching prose, many names and
dates, Latin, French, German and English titles.

## What you write

One LaTeX fragment (no preamble), at the path you are given, mirroring the Danish 1:1:

- **Comments.** The Danish has `%` comment lines: page markers `% --- p. N ---`, running heads `% running head: ...`,
  `% CHECK ...` lines and editorial notes.  Copy every `% --- p. N ---` line exactly where it stands, and every
  `\setcounter{footnote}{0}%` line after it, exactly.  Do NOT copy any other comment, except: where a comment says `PRINTED AS IS` and the misprint affects the sense, translate the
  intended sense and put, on its OWN line just before the line concerned, `% print: <the Danish words> (misprint)`.
  Never put a `%` comment at the end of or inside a line of text.
- **Page turns.** The Danish marks each printed page with `% --- p. N ---` on its own line and `\opage{N}` before the
  first word of the page.  Reproduce both: `\opage{N}` immediately before the English
  word that corresponds to the first word of printed page N (approximately, where the syntax is rearranged).  Every
  `\opage{N}` of your Danish appears exactly once in your English, in order.  A word broken over a page turn
  (`anven%` … `\opage{84}des`) is one word: put the marker before the English word.  **Never end a line of English text
  with `%`.**
- **Paragraphs** exactly as in the Danish: a blank line where the Danish has one, none where it has none (a paragraph
  running over a page turn stays one paragraph).
- **Headings and structure commands** as in the Danish, their text translated by GLOSSARY.md "Headings":
  `\introhead{}`, `\chapterhead{numeral}{TITLE}`, `\chapterheadone{…}{running head}`, `\sectionhead{}`, and the
  run-in `Tillæg.` line (all translated by GLOSSARY.md "Headings"); `\closerule` and `\medskip\noindent` copied as is.
  Run-in labels (a. b. 1. 2. α. β. γ.) stay exactly as printed, Greek as Greek.
- **Footnotes.** The book has one note (p. 4), at its mark as `\footnote[1]{...}` (the print's *)).  Keep each `\footnote[K]{` with the same K right after the corresponding English word or stop, and translate
  its Danish text inside the braces (titles and quotations in other languages stay as printed).  A footnote count per
  page is checked by the build.
- **Emphasis**: `\textit{…}` (italics: titles, foreign words, emphasis) and `\textsc{…}` (names in small capitals,
  as `\textsc{Réné} \textsc{Descartes}`): carry every one over to the corresponding English words, one for one.
  Add none.
- **Quotation marks.** „…“ → ``…'' in LaTeX; a quotation inside a quotation → `…'.  One opening mark for one opening
  mark.
- **Foreign languages.** What Høffding quotes or names in French, Spanish, German, English, Latin, Swedish or Greek stays in the
  original, character for character, set as in the Danish (Greek glyphs verbatim).  Do not add an English gloss.  What
  he writes in Danish — including his own Danish renderings of foreign authors, in quotation marks — is translated
  from his Danish.
- **Titles of books and journals** stay as printed (French, German, Danish, Swedish …).  Do not translate titles.
  Høffding's references to his own Danish books stay in Danish too (*Psykologi*, *Etik*, *Religionsfilosofi*, *Mindre
  Arbejder*, *Den nyere Filosofis Historie*), and so do Kierkegaard's („Enten-Eller“, *Stadier paa Livets Vej*).  The
  reference „Psykologi V D, 3“ etc. stays as printed.
- **Names** as printed (Réné Descartes, Burckardt, Melanchton, Darwin, Kroman: misprints and period forms too; the
  GLOSSARY says where the headings differ), with the English possessive (Kants → Kant's, Hume's → Hume's).  Ancient and Biblical names in
  English (Sokrates → Socrates, Platon → Plato, Aristoteles → Aristotle, Kristus → Christ).  København → Copenhagen;
  well-known places in English form; Tyskland → Germany.
- Dashes `---` stay `---`; `ɔ:` → "i.e."; `f. Eks.` → "e.g."; `o. s. v.` → "etc."; `d. v. s.` → "i.e."; `Smlgn.`,
  `Smlg.`, `Sml.` → "Cf."; `Se` → "See"; `S.` (Side) → "p."; `p.`, `udg. af` (→ "ed. by"), `Overs.` (→ "trans."),
  volume numerals and page numbers in citations exactly as printed; `\dots{}` stays.
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
(kun/kan, har/var, til/vil, en/et, de/det, ham/han), an accent that looks wrong in French, a missing or doubled word, an ending that breaks the grammar,
punctuation that breaks the sense, a paragraph break that looks wrong (inside a sentence), a quotation mark or
parenthesis that does not close, a foreign word misspelt.  Do NOT list the period's spelling (aa, capitalized nouns, ere,
gaaer, x for ks, Exempel) and do NOT list spots a `%` comment already settles.  Do not stop to resolve them; just list
them, and translate the evident sense.

## Mechanics

Work in chunks of two or three printed pages; append each chunk to your fragment file as you finish it (with Bash:
`cat >> FRAGMENT <<'EOF2'` … `EOF2`, so you never re-send the whole file), so nothing is lost.  Container tools only
(Read, Bash, Write, Edit: no remote-device tools, no web).  When finished, check your fragment with the book's script:

```
python3 TOOLDIR/tr_parts.py build --book BOOKDIR --parts OUTDIR      # paths given with your task
```

It must print `OK` for your part's markers, marks and paragraphs (look at each `<-- check` line and fix what is a real
slip).  Also:

```
grep -n '%$' FRAGMENT | grep -v ':%'      # must print nothing
```

Reply with ONE line: `part: …, pages N–M, opage K, footnotes F (Danish F'), build: OK|problems, odd spots S`, and on a
second line, at most three term choices you made that the glossary did not settle (Danish = English).
