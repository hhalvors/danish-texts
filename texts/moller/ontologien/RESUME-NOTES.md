# Poul Martin Møller — Ontologien eller Kategoriernes System: resume notes

Source of truth: transcription.tex (Danish), **COMPLETE** (printed pp. 189–212).
Translation: translation.tex (English), **COMPLETE** (mirrors transcription 1:1).
Scan: ~/bibliotek/Møller, Poul Martin/efterladte-skrifter3.pdf
Page-offset: **PDF = printed + 11** (printed 189 = PDF p.200; piece runs PDF pp. 200–223).

## STATUS
Both files transcribed/translated in full and compile clean in the sandbox
(0 errors, 0 char-warnings, 18 pp. each). Marked `in-progress` in catalog.yaml
pending your local compile with the real fonts (libertinus + textalpha) and a
commit/push so the GitHub Pages links resolve. Flip the catalog section
`status:` to `complete` once the two PDFs build and the links work.

## Structure of the fragment
- **Indledning** (pp. 189–206): metaphysics as propaedeutic; the deduction of
  the categories; against the subjectivity of the categories (Kant); Schelling's
  Absolute; Hegel's *Wissenschaft der Logik*; the aim/method of ontology;
  categories as linguistic tradition; the dialectic of single categories.
  Ends p.206 with a rule.
- **Første Capitel — Læren om de enkelte Begreber; Første Afsnit —
  Begyndelsesbegreberne** (pp. 206–212): idealism/skepticism/nihilism; the
  concept **Væren** (Being) as point of departure; *A. Væren*; Being = Nothing;
  *B. Noget* (Something). Breaks off mid-section on p.212 ("...er Noget — —").

## Conventions used (book-specific)
See ../../../TRANSLATION-PLAYBOOK.md for the standing method. Specifics here:
- Fraktur setting → original orthography kept (aa, capitalised nouns, æ/ø,
  "philosophisk", "Kategorie", "Begreb"). Long-s → s.
- Letterspaced emphasis → `\emph{}` (e.g. *Lys*, *Tyngde*, *Seyn*, *Noget*, the
  run-in heads *A Væren*, *B. Noget*).
- Latin → `\textit{}` (*sub specie æternitatis*, *qui bene distinguit, bene
  docet*, *bene*, *être*); the algebra variable *x* also italic.
- Greek copied verbatim (τὸ χωριστόν, τὸ ὄν, τὸ εἶναι); needs `textalpha`.
- Old "id est" mark **ɔ:** — the reversed-c glyph (U+0254) is mapped in the
  preamble via `\DeclareUnicodeCharacter{0254}{\reflectbox{c}}` (needs
  `graphicx`); in the English translation it is rendered "i.e."
- Quotes: Danish „…" → transcription keeps „…"; translation uses ``…''.
- Printed page numbers → `\opage{N}` (all of 189–212 present, sequential).
- **Footnotes** (4 authorial/editorial notes): the title-note on
  "Kategoriernes System"; the long note defining Ontologie on p.202 (with the
  editor's bracketed manuscript-margin remark appended); the "Forf.s
  Marginalnote" on p.203; and the p.209 note ("written during my illness this
  year (1838)…").

## Preamble note (differs from the standard translation.tex checklist)
transcription.tex adds `graphicx` + the `\DeclareUnicodeCharacter{0254}` mapping
for the ɔ: mark. Keep it if re-generating. Sandbox compile: strip
libertinus/textalpha/[danish]babel and replace Greek, per the playbook recipe.

## Next candidate pieces in bd. 3 (not yet done)
Other philosophical Brudstykker: *Om Begrebet Ironie* (pp. 152–158),
*Om en didaktisk Logiks Foredrag* (149), *Ahasverus* (159), *Affectation* (163),
*Om Sjælen* (Oversættelse, 213–236). Plus the Strøtanker (pp. 1–147) and the
vol. 4 lecture course on the history of ancient philosophy (PDF pp. 240ff).
