# Høffding — Religion og Videnskab (1910): transcription resume notes

Source of truth: transcription.tex (Danish), ▢ in progress.
Page-offset: **PDF = printed + 9** (printed p.1 = PDF p.10). Verified against
printed folio "2" on PDF p.11.
Scan: ~/bibliotek/Høffding, Harald/religion-og-videnskab.pdf
Series: *Religionshistoriske Smaaskrifter* I. Title page: Gyldendalske
Boghandel — Nordisk Forlag, MDCCCCX (1910).
Article span: printed pp. 1–59 = PDF pp. 10–68. (Front matter PDF 4–9; a few
near-blank plate/half-title pages.)

## Structure
Continuous essay, no chapter headings. Divided by:
- one centered section rule near the top (after "…deres fulde Ret.", p.3) →
  rendered `\begin{center}---\end{center}`.
- numbered points "1.", "2.", "3." … introducing successive themes (point 1
  begins on p.4). Rendered as run-in "1." etc.
Footnotes (marked `*)` in print) appear at least on printed p.26 (Hamlet ref)
and p.49 (Udvalgte Stykker ref) — carry them as `\footnote{}` when reached.

## Editorial policy (confirmed with Hans)
- Quotation marks: reproduce as printed — Danish low-high „…“ (U+201E open,
  U+201C close). NOT normalized to guillemets.
- Printer's typos: reproduce verbatim + flag with `% [sic]` LaTeX comment.
  So far: "Bekekendelse" (for "Bekendelse"), printed p.3.

## CURRENT RESUME POINT
TRANSCRIPTION COMPLETE. All 6 batches done = printed pp. 1–59 (PDF 10–68).
No continuation markers remain; file ends with the closing centered rule and
`\end{document}`. Full document compiles clean: 41 pages, 0 overfull boxes,
0 missing characters, 0 undefined control sequences (sandbox lmodern check).

Editorial notes added in batches 5–6:
- Footnote on printed p.49 ("Subjektiviteten er Sandheden*)") rendered as
  `\footnote{I \emph{Udvalgte Stykker af dansk filosofisk Literatur} (1910) …}`.
- Latin phrases reproduced roman as printed: "Theologia experimentalis",
  "(fides implicita)".
- Numbered point "4." and sub-point "b." rendered run-in with a preceding
  `\medskip`, matching earlier points 1–3 / sub-point a.
- Old-spelling "somom" (printed p.49) reproduced verbatim (not a typo).

Translation status: COMPLETE. translation.tex covers all of printed pp. 1–59,
ending "…look toward the future with confidence." + closing centered rule. No
markers remain. Full document compiles clean in the sandbox recipe: 41 pages,
0 errors, 0 char-warnings, 0 overfull boxes.

Translation editorial notes:
- Two footnotes carried as `\footnote{}`: Hamlet I,5 (printed p.24) with
  Shakespeare's original English replacing Niels Møller's Danish verse;
  the \emph{Udvalgte Stykker af dansk filosofisk Literatur} reference (printed
  p.49) kept in Danish per playbook.
- Coinages/terms: „Samfoldighed" → "compound unity"; „Kulsviertro" →
  "charcoal-burner's faith"; \textit{unica}, \textit{fides implicita},
  \emph{Theologia experimentalis} kept Latin.
- Main-text echo „den ukendte Mand" rendered ``the stranger'' to match Hamlet.
- Høffding's own „Religionsfilosofi" rendered ``Philosophy of Religion.''
- catalog.yaml section status set to `complete`.

## Natural-English revision pass (2026-07)
Whole body of translation.tex re-Englished for idiom (thorough recast, period
scholarly register) while preserving Høffding's meaning. Danish-calque syntax
undone: fronted "There makes itself known…" inversions, heavy nominalizations,
"it fares with…as with…", "over against," etc. Preamble untouched. All LaTeX
markup verified unchanged vs. backup: 2 footnotes, 12 \emph, 3 \textit, 2
centered rules, 6 \medskip. Coinages/terms kept: "compound unity,"
"charcoal-burner's faith," unica, fides implicita, Theologia experimentalis,
"the stranger" (Hamlet echo), "Philosophy of Religion." Literal original saved
as translation.literal.bak.tex. Sandbox compile clean: 39 pages, 0 errors,
0 char-warnings.

Both PDFs should be compiled locally with the real libertinus + textalpha fonts
to confirm the Transcription + Translation links resolve before commit/push.

Workflow per batch: `pdftoppm -png -r 200 -f <PDF> -l <PDF>` the ~10 pages,
copy PNGs into the outputs folder, Read each image, de-hyphenate + reflow the
OCR text, fix OCR errors against the image, append before `\end{document}`
(remove the old continuation marker), then compile-check.

## Sandbox compile check
Sandbox lacks `libertinus` AND the `danish` babel option; strip both for the
check only (do NOT put substitutions in the real file):
```
sed -e 's/\\usepackage{libertinus}/\\usepackage{lmodern}/' \
    -e '/libertinust1math/d' -e '/\\usepackage\[danish\]{babel}/d' \
    transcription.tex > t.tex
pdflatex -interaction=nonstopmode -halt-on-error t.tex   # run twice
```
Batch 1 result: 7 pages, 0 char-warnings, 0 errors.
On Hans's machine it compiles with the real libertinus + danish babel.

## Conventions
See ../../../TRANSLATION-PLAYBOOK.md for the standing method (that file is
about translation; this is the transcription counterpart).
