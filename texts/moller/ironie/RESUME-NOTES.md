# Poul Martin Møller — "Om Begrebet Ironie": resume notes

Source of truth: `transcription.tex` (Danish), **COMPLETE** (printed pp. 152–158).
Translation: `translation.tex` (English), **COMPLETE** (mirrors transcription 1:1).
Scan: ~/bibliotek/Møller, Poul Martin/efterladte-skrifter3.pdf
Page-offset: **PDF = printed + 11** (printed 152 = PDF p.163; piece runs PDF pp. 163–169).

## STATUS
Both files transcribed/translated in full and compile clean in the sandbox
(0 errors, 0 char-warnings, 6 pp. each). Marked `in-progress` in `catalog.yaml`
pending your local compile with the real fonts (libertinus + textalpha) and a
commit/push so the GitHub Pages links resolve. Flip the section `status:` to
`complete` once both PDFs build and the links work.

## What this piece is
Brudstykke II of Efterladte Skrifter vol. 3. Occasioned by Provost Tryde's
review of Sibbern's *Æsthetik* (Maanedsskrift for Litteratur, bd. 13, 1835).
Møller, on the journal's editorial board, began aphoristic remarks on the
concept of irony but **completed only the Introduction** — the treatment of
*moral* irony. The fragment ends at printed p. 158 with "Vi gaae nu over til den
poetiske Ironie. — —"; p. 159 begins the next Brudstykke ("III. Ahasverus").
The long opening footnote is the **editor's** (F.C. Olsen), explaining the
occasion; it is reproduced as a `\footnote{}`.

## Argument map
Greek moral consciousness (natural desire vs. reason as limiting principle;
Aristotle) → British moral philosophy's a priori project → Kant/Fichte forced
back on heteronomous maxims → Fichte lodges highest authority in individual
conviction → moral idealism, one-sidedly held, yields the subjective will above
the moral law → F. Schlegel's *Lucinde* → Hegel's irony = "the subjectivity
that knows itself as the highest," one of "the moral forms of evil." A parallel
figure, morbid *sentimentality*, is contrasted with irony (both hold themselves
"too good to have duties"). Directly upstream of Kierkegaard's *Concept of
Irony*.

## Conventions (book-specific)
See ../../../TRANSLATION-PLAYBOOK.md for the standing method. This piece follows
the **Ontologien** conventions (same volume, same Fraktur source):
- Original orthography kept (aa-spellings, capitalised nouns, "Conseqvents",
  "Qvantum", "Philosophie", the -us endings Egoismus/Nihilismus/Idealismus).
  Long-s → s.
- Danish quotes „…" kept in the transcription; → ``…'' in the translation.
- Book titles (*Lucinde*, *Æsthetik*) → `\emph{}`.
- Printed page numbers → `\opage{N}` (all of 152–158 present, sequential).
- One authorial/editorial footnote (the Tryde/Sibbern occasion note on p. 152).
- No Greek and no ɔ: mark occur in this piece (unlike Ontologien), but the
  preamble keeps `textalpha` + the graphicx/`\DeclareUnicodeCharacter{0254}`
  setup for consistency across the Møller folder.
- Watch-word verified against the scan: "Livets **Øiemed**" (p. 153) and
  "eneste værdige **Øiemed**" (p. 157) — the Fraktur capital Ø reads D-like at
  low resolution; it is Ø.

## Next candidate pieces (priority list)
Per PHILOSOPHY-PRIORITIES.md: Forelæsnings-Paragrapher over Moralphilosophien
(vol. 5, pp. 141–164); Forberedelser til en Afhandling om Affectation (vol. 3,
Brudstykke IV, pp. 163–188); a Fraktur transcription of the Strøtanker
(vol. 3, pp. 1–147); the vol. 4 history-of-philosophy course.
