# Høffding — Søren Kierkegaard som Filosof (1892 / rev. 1919): translation resume notes

**Project type: translation-only.** We do NOT publish a Danish transcription
(the modern edition is the publisher's copyrighted text). Only `translation.tex`
is built. The catalog links to the public-domain 1892 original (Project Runeberg)
and to the publisher e-book instead of a Transcription PDF.

Source of truth for translating: the Danish **epub**
`~/bibliotek/Høffding, Harald/Soeren_Kierkegaard_som_filosof.epub`
(Lindhardt og Ringhof / SAGA, © 1919, 2020; ISBN 9788726363111).
Extract chapter text from the epub's OPS/*.xhtml files; endnotes live in
`s012-Notes-01.xhtml` and are keyed by `rw-num-note-N` — restore each to a
`\footnote{}` at its anchor word.

Edition note: the epub is the **revised 1919** edition (footnotes cite works up
to 1919). Page ranges in the markers are the **1892 first-edition** pages (from
Runeberg) and are approximate navigational labels only.

epub chapter → book part:
- s004 Introduction  = Indledning (pp. 1–4)
- s005 Chapter-001   = I  (pp. 5–15)
- s006 Chapter-002   = II (pp. 16–27)
- s007 Chapter-003   = III (pp. 28–53)
- s008 Chapter-004   = IV (pp. 54–126)   [Runeberg TOC mislabels this "VI"]
- s009 Chapter-005   = V  (pp. 127–149)
- s010 Conclusion    = Slutning (pp. 150–159)

## STATUS: COMPLETE
All 13 markers filled. translation.tex covers the whole book (Introduction →
Conclusion). Last sandbox compile: 115 pp, 0 errors, 0 char-warnings, 0 markers.
Catalog status set to `complete`.

Remaining for Hans: compile both locally with the real fonts (libertinus +
textalpha) and confirm the Translation PDF renders; then commit/push. (Claude
does not commit.) Optional cleanup: the old `transcription.tex`/`.pdf` (1892-
orthography, IV.A only) can be removed and the transcription target dropped from
the Makefile, per the translation-only decision.

NOTE: garbled Greek in the epub was restored from the original (Xenophon
Memorabilia II,1 in the Aristippus footnote); if proofing turns up other garbled
Greek/foreign strings, restore from context/standard editions.

## DONE so far (don't redo)
- Front matter: title, epigraph, translator's note.
- Introduction (pp. 1–4).
- Chapter I: The Romantic-Speculative Philosophy of Religion (pp. 5–15),
  incl. footnote 1 (Hegel bibliographic note).
- Chapter II: Søren Kierkegaard's Older Contemporaries in Denmark (pp. 16–27),
  incl. footnotes 2 (Danske Filosofer) and 3 (Mindre Arbejder). Heiberg,
  Martensen, Sibbern, Poul Møller. Danish verse (Heiberg) and the Begrebet
  Angest dedication rendered into English; German/Danish work titles kept.
- Chapter III: Søren Kierkegaard's Personality (pp. 28–53), all 7 numbered
  sections, footnotes 4–8. Many block quotations from Kierkegaard's papers/
  Stages/Point of View rendered into English; Danish/German/Latin/French terms
  (Acedia, odium professionis, «désenchantement de dieu», Janus bifrons) kept;
  Danish work titles kept in Danish.
- Chapter IV, Section A: Epistemology (pp. 58–70) — folded in from the earlier
  standalone article-class translation; footnotes 9–11 (Postscript / Sibbern /
  Den menneskelige Tanke) since ADDED, which the article had dropped.
- Chapter IV intro (pp. 54–57): Schelling's 1841 Berlin lectures, the "leap,"
  Trendelenburg, Copenhagen street-life, indirect communication.
- Chapter IV, Section B (Ethics) opening + a. The Leap (pp. 70–82), sections 1–4,
  footnote 12. The "two types of thought" (synthesis/analysis), qualitative
  dialectic, psychology vs. ethics, The Concept of Anxiety on the Fall/dizziness,
  Høffding's critique (circle/straight-line, unconscious decision).
- IV.B.b The Stages intro + α The Aesthetic View of Life (pp. 82–91), sections 1–3,
  footnotes 13 (Aristippus/Xenophon, Greek restored) & 14 (Schopenhauer). Rotation
  of Crops, kaleidoscope/arbitrariness, The Banquet, Johannes the Seducer, Høffding's
  critique (no genetic account; Dante/hell; switch-point image).
- IV.B.b.β Ethical View of Life (pp. 92–109): marriage/resolution, Repetition (full
  garment passage), the Single Individual (den Enkelte), subjectivity as the good,
  Egyptian-monks critique, Christian VIII anecdote, ethical sphere as transition.
- IV.B.b.γ Religious View of Life (pp. 109–119), fns 15–17 (incl. Brøchner quote):
  Fear and Trembling/Abraham, absolute purpose vs. relative, fish-on-land + Ibsen
  Brand verse, Schopenhauer/Nirvana, Religiousness A vs B.
- IV.B.c The Standard (pp. 119–126), fn 18 (Kierkegaard/Nietzsche): the formal
  tension-standard, river vs. waterfall, Greek/humane ethics, deus caritatis,
  God "sitting in sorrow" — theology is psychology. CHAPTER IV COMPLETE.
- Chapter V, Søren Kierkegaard and Christianity (pp. 127–149): A. Personal
  Breakthrough (Easter 1848, Corsair affair, the "new production," Practice in
  Christianity, Luther critique, woman/family) and B. The Last Word (Mynster/
  Martensen, witness-to-truth strife, The Moment, Brorson grave verse, death).
  No footnotes in Ch V.
- Conclusion / Slutning (pp. 150–159), fn 19: Høffding's own verdict — the near-
  horizon eschatology of the NT, "New Testament Christianity does not exist"
  explained historically rather than as apostasy, the humane view of life beside
  Greek culture and Christianity, dogma vs. contemporaneity, new wine/new vessels.
  WHOLE BOOK COMPLETE.

## Conventions
See ../../../TRANSLATION-PLAYBOOK.md (the standing method). Book-specific points:
- File is **book class**; unnumbered chapters via the `\bookchapter{}` macro
  (Roman numeral written into the heading), sections `\section*{A.\quad …}`,
  subsections `a./b./c.`, subsubsections `$\alpha$./$\beta$./$\gamma$.`.
- German book titles / verse (Faust, Schleiermacher, Hegel) stay in the original,
  kept in »…« guillemets as printed. Danish-origin quotes → ``…''.
- Numbered run-in paragraphs (1., 2., …) → `\noindent\textbf{1.}` as in IV.A.
- Restore endnotes to `\footnote{}` at the anchor; keep work-title refs as cited.
- The epub occasionally drops a clause (OCR). One already fixed: in Ch I §3 the
  parenthesis on the religious feeling was completed from context
  ("…both in its older form, as feeling of unity, and in its later form, as
  feeling of dependence…"). Watch for similar gaps; cross-check Runeberg 1892
  (https://runeberg.org/kierkegfil/) when a sentence looks truncated.

## Compile
Sandbox recipe in the playbook §3 (lmodern substitution). Last compile:
33 pp, 0 errors, 0 char-warnings, 13 markers left.

## Note for Hans
The old `transcription.tex` / `transcription.pdf` (1892-orthography IV.A only)
are still in this folder. Given the translation-only decision, decide whether to
remove them from the repo and drop the transcription build from the Makefile.
