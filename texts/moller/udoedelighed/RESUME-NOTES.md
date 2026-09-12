# Poul Martin Møller — "Om Muligheden af Beviser for Menneskets Udødelighed": resume notes

Source of truth: `transcription.tex` (Danish), **COMPLETE** (both articles).
Translation: `translation.tex` is a stub — **not to be completed**; Jon Stewart
already published an English translation (2022), doi:10.1163/9789004517912_003.

## STATUS
Danish transcription of the whole essay is complete and compiles clean in the
sandbox (0 errors, 0 missing-character warnings, 72 pp.). Marked `complete` in
`catalog.yaml` pending a local compile with the real fonts (libertinus +
textalpha) and a commit/push so the GitHub Pages links resolve.

**`transcription.pdf` in this directory is stale** — it predates the 2026-09-12
repairs below. Rebuild via `~/hhalvors.github.io/publish-danish.sh`.

## 2026-09-12 — repairs to the Art. I digitised transcript
The Art. I text came from a digitised transcript of SiU, not from page images,
and carried that transcript's page-foot damage. Full log, with SiU and MfL page
numbers for every site, is now in the **`transcription.tex` comment header** —
that is the record of publication; this is only the production note.

Summary: 24 paragraphs rejoined (each had been split mid-sentence at a page
foot); 4 sheet-signature asterisks deleted from the text (SiU 172, 175, 186,
213); 3 sentence-final full stops restored (SiU 171, 236, 244, all confirmed
against MfL); Art. I's 4 missing footnotes supplied from the MfL first printing
and normalised SiU-style (SiU 171, 174, 185, 212 = MfL 3, 6, 15, 38); the OCR
junk `*dolgoeO*` at SiU 189 resolved to `Ug.x` (MfL 19, the antiqua x of the
school mark "ug med kryds").

### Open review items
1. **Collate the four restored footnotes against SiU pp. 168--253** when the
   volume is to hand. They are reconstructions from MfL, not readings of the
   copy-text; SiU's wording, and its placement of the mark relative to the
   sentence stop, may differ. This is the one outstanding scholarly debt.
2. Closing high quote is written two ways in the file: literal `“` twice and
   LaTeX `` `` `` twice. Both typeset identically; balance is 4 open / 4 close.
   Normalise if it ever matters.
3. Art. I uses ` - ` for the dash (31x) where Art. II uses ` --- ` (13x). The
   Art. I hyphens are almost certainly the digitised transcript flattening em
   dashes. The 4 restored footnotes use `---`.
4. Footnote marks are printed `*)` throughout MfL but set here with plain
   `\footnote{}` numbering (1--13 continuous across both articles). If per-page
   `*)` is wanted, `\renewcommand{\thefootnote}{*)}` in the preamble --- not
   `\fnsymbol`, not `footmisc[perpage]` (see TRANSCRIPTION-PLAYBOOK §4).

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
