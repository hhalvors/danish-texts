# Poul Martin Møller — "Om Muligheden af Beviser for Menneskets Udødelighed": resume notes

Source of truth: `transcription.tex` (Danish), **COMPLETE** (both articles).
Translation: `translation.tex` is a stub — **not to be completed**; Jon Stewart
already published an English translation (2022), doi:10.1163/9789004517912_003.

## STATUS
Danish transcription of the whole essay is complete and compiles clean in the
sandbox (0 errors, 0 missing-character warnings, 72 pp.). Marked `complete` in
`catalog.yaml` pending a local compile with the real fonts (libertinus +
textalpha) and a commit/push so the GitHub Pages links resolve.

## Two-part provenance (important)
The essay appeared in *Maanedsskrift for Litteratur* 17 (1837) in two
installments:

- **Article I** ("Første Artikel", §§ I–VII) — MfL pp. 1–72. Transcribed here
  from **Skrifter i Udvalg** (1930), pp. 168–253, in that edition's modernized
  orthography. `\opage{}` margin numbers in this part are the SiU page numbers.
- **Article II** ("Fortsat og sluttet", §§ VIII–XI) — MfL pp. 422–453. This
  installment was **omitted from Skrifter i Udvalg** (a selection), so it is
  transcribed from the **Fraktur first printing** (`moller-udoedelighed-scan.pdf`,
  scan pp. 73–104), rendered in the *same* SiU-style modernized orthography for
  continuity. `\opage{}` numbers 422–453 in this part are the 1837 MfL page
  numbers. A bracketed editorial note in the .tex flags the source switch at the
  Article I/II boundary.

## Article II section map (pp. 422–453)
- **§ VIII** p. 422 — restatement; the immortality proof belongs in the doctrine
  of absolute spirit. Long block quotation from **Weiße** (pp. 423–430) on the
  aesthetic consciousness as approach to the proof.
- **§ IX** p. 431 — the younger **Fichte**, *Die Idee der Persönlichkeit* (1834);
  long block quotation (pp. 432–439) on the natural-analogy / physiological proof.
- **§ X** p. 440 — **Göschel**, *Von den Beweisen …* (1835); two block
  quotations (the second closes p. 449), then Møller's critique of Göschel's
  Hegelian re-casting.
- **§ XI** p. 450 — survey of the wider literature (Dr. Mises = Fechner;
  Hubert-Becker), and the closing methodological point that a rigorous proof is
  possible only inside a fully articulated system. Ends p. 453, signed
  "Poul Møller."

## Conventions (book-specific)
See `../../../TRANSLATION-PLAYBOOK.md` for the standing method. Specifics:
- Main block quotations use Danish guillemets »…«; the German footnote quote and
  the short titles-in-quotes use „…``.
- Orthography modernized SiU-style: `Beviis`→`Bevis`, `speculativ`→`spekulativ`,
  `philosoph`→`filosof`, `æsthetisk`→`æstetisk`, `Existents`→`Eksistens`,
  `kj`→`k` / `gj`→`g` (but `gjort` stays), `ei`→`ej`, `øi`→`øj`, `ee`→`e`
  (`Fordeel`→`Fordel`), `stræng`→`streng`, `Villie`→`Vilje`, `Linier`→`Linjer`,
  `Literatur`→`Litteratur`. Emphatic numeral kept as `Eet`/`een`. `aa` retained.
- Old "id est" mark **ɔ:** (U+0254) mapped in the preamble via
  `\DeclareUnicodeCharacter{0254}{\reflectbox{c}}` (needs `graphicx`).
- German book titles and embedded Latin/French phrases in `\textit{}`.
- Footnotes rendered with `\footnote{}` (Göschel/Fichte/Weiße/Mises titles;
  the long authorial note in § VIII on "individuality"; the Sibbern program note
  on p. 451; the Mises and Hubert-Becker notes on p. 452).

## Sandbox compile recipe
Strip libertinus→lmodern, delete `libertinust1math`/`textalpha`, drop the
`[danish]` babel option; then `pdflatex` twice. Expect 0 errors, 0
missing-character warnings (a handful of Overfull hboxes from long unbreakable
quotation strings are harmless).
