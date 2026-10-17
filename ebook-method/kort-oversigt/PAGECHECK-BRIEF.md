# Reader brief: sampled page check, H. Høffding, *Kort Oversigt over den nyere Filosofis Historie* (4th ed., 1910)

(adapted 2026-10-17 from ebook-method/religioese-tanketyper/PAGECHECK-BRIEF.md)

You transcribe whole printed pages of a Danish book of 1910 in antiqua (roman type), exactly as printed, at the image.
You see no other text of the book and need none: read only what you see. Your reading is compared word by word with an
existing transcription, so exactness matters more than speed. Never correct, modernise or guess toward sense: the book
keeps its period spelling (*Aaret*, *Brevvexling*, capitalised nouns), quotes French, Spanish, German, English, Latin and
some Greek, and misprints stay misprints.

## The images

Sheets on Hans's computer (device paths for staging), the names your instruction gives, e.g.

    /Users/hhalvors/danish-texts/texts/hoeffding/kort-oversigt/.render/kort-oversigt-pc-01.png

Stage all your sheets with `mcp__remote-devices__device_stage_files` in ONE call (two at most), then Read each staged
image in order. Two strips a sheet; each strip is labelled `p. N   strip k of K`; the strips of a page follow each other
without overlap and cover the whole page, head to foot. Do not open anything else in the repo (no transcription.tex, no
`.parts/` except your own output file): the check is blind. If two device calls fail, stop and report.

## What you write

One file, written with `mcp__remote-devices__device_bash` (a heredoc), rewritten whole after every sheet; the path is
in your instruction.

- At the start of each page, a line `=== p. N` (N from the label).
- Then **one printed line per line of your file**, in order, exactly as printed. Do not join or re-wrap lines.
- The running head at the top (page number and short title): one line `HEAD ...`. A signature at the foot of some pages
  ("Høffding: Kort Oversigt. 2"): a line `SIG ...`.  Quotation marks in this book are „ and “ (low opening, high closing).  PENCIL marks of a
  former reader (hand-drawn slashes, crosses, underlining) are NOT print: leave them out.
- A word divided at the line end: end the line with `=` in place of the hyphen (`Tænk=`); the next line begins with the
  rest (`ning ...`).
- Accents exactly as printed: é è ê ë are different (French titles: *Térèse*, *très*).
- Letters, punctuation and quotation marks exactly as printed: » and « (write the direction you SEE); — (long dash) and
  - (hyphen). No space before ; : ? ! even where the printer set one. A speck or a raised dot that is not a printed stop:
  leave it out.
- *Italic* words between asterisks: `*Die Mechanik*` (a run of several words: `*Die Mechanik in ihrer Entwickelung.*`).
- SMALL CAPITALS: names of philosophers are very often set in small capitals (a full-height capital, then small
  capitals: WILLIAM JAMES looks like W-illiam J-ames in small letters of capital shape). Write them `<sc>William James</sc>`
  in normal case; look at EVERY word of a name (first names, initials and surnames may differ) and mark only the
  words that are in small capitals.
- A large initial letter two lines deep at the start of a chapter: write it as the first letter of the word (`Den`).
- L e t t e r s p a c e d words (rare), written unspaced, between underscores: `_Gunkel_`.
- NOTE MARKS (rare: the book has one note) are a star with a parenthesis: write them `*)`: `Opgaver*).`  The footnotes at the page foot (small type) are transcribed line by line too, each beginning
  with its label written `*)`: `*) Se om denne Strid ...`.  A raised figure (an edition number) is `^2`: `*Logica*^2.`
- Greek letters as Greek: paragraphs are often labelled α. β. γ. (write them as Greek, not a b y).
- Headings and centred lines as printed, one per line. A short printed rule: a line `RULE`.
- A letter you cannot make out: your best reading followed by `[?]`. Never leave a word out.

When all sheets are done, check that every page has its `=== p. N` line and reply with ONE line:
`pagecheck: P pages, L lines, uncertain [?] U`.

## Afterwards (main session, not the reader)
`python3 ebook-method/kort-oversigt/pagecheck.py compare <reading file>`, decide every row of
`.parts/pagecheck/diffs.tsv` (T/E/P/M; crops with wordcrop.py), then `pagecheck.py rate`.
