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

## 2026-09-27 — scholarly transcription of the 1892 FIRST EDITION begun

Decision (Hans): the translation-only approach above is superseded. The
e-book is the 1919 revision and cannot be cited to the original pagination;
we now make a diplomatic transcription of the 1892 first edition from the
KB scan (`~/bibliotek/Høffding, Harald/kierkegaard.pdf`, sha256 d19eba84…,
registered in SCANS.tsv). PDF = printed + 9. Brief: BATCH-AGENT.md in this
directory. The existing translation.tex (of the 1919 text) is untouched; it
will later be revised against the 1892 transcription.

Batches (markers in transcription.tex): 1–15 | 16–27 | 28–40 | 41–53 |
54–69 | 70–82 | 83–97 | 98–111 | 112–126 | 127–142 | 143–159.

Pilot, front matter + pp. 1–15 (spliced):
OCRDIFF: embedded | 11 candidates | 0 corrected | 11 witness's fault | 0 unresolved
Findings folded into BATCH-AGENT.md. One UNSURE: p. 5 „ish“ (for „ist“?)
under a reader's ink correction — for the second reading. Indhold prints
„VI.“ for IV (logged). check.py/joints clean for pp. 1–15; sandbox compile
clean. Cost ≈ 185k tokens (≈ 11k per page).



Wave 1, pp. 16–82 (five batches, spliced):
OCRDIFF: embedded | 7 candidates | 0 corrected | 7 witness's fault | 0 unresolved   (pp. 16–27)
OCRDIFF: embedded | 9 candidates | 0 corrected | 9 witness's fault | 0 unresolved   (pp. 28–40)
OCRDIFF: embedded | 8 candidates | 0 corrected | 8 witness's fault | 0 unresolved   (pp. 41–53)
OCRDIFF: embedded | 6 candidates | 0 corrected | 6 witness's fault | 0 unresolved   (pp. 54–69)
OCRDIFF: embedded | 6 candidates | 0 corrected | 6 witness's fault | 0 unresolved   (pp. 70–82)
Caller: 2 spurious blank lines at joints removed (p. 70 mid-word
Kontem-plationens); number ranges harmonized to "--"; spaced ellipses closed
up to "....". Printer's errors logged: p. 26 unclosed guillemet; p. 34n "1"
for I; p. 43n long-s sort in "hosde" (holde); p. 67 "finder men"; p. 71
"der. som". UNSURE: p. 5 "ish"; p. 77 "Bégrundelse" (é printed or pencil?).
Chapter IV head prints "IV." (only the Indhold misprints VI.). 6 footnotes
so far. check.py/joints clean for pp. 1–82; sandbox compile 57 pp., 0 errors.
Cost ≈ 1.27M tokens (≈ 19k per page, above the pilot's rate; one batch,
pp. 41–53, cost 415k). Brief updated with wave-1 findings.

NEXT: wave 2, pp. 83–159 (five batches).

Wave 2, pp. 83–159 (five batches, spliced):
OCRDIFF: embedded | 5 candidates | 0 corrected | 5 witness's fault | 0 unresolved    (pp. 83–97)
OCRDIFF: embedded | 5 candidates | 0 corrected | 5 witness's fault | 0 unresolved    (pp. 98–111)
OCRDIFF: embedded | 7 candidates | 0 corrected | 7 witness's fault | 0 unresolved    (pp. 112–126)
OCRDIFF: embedded | 10 candidates | 0 corrected | 10 witness's fault | 0 unresolved  (pp. 127–142)
OCRDIFF: embedded | 9 candidates | 0 corrected | 9 witness's fault | 0 unresolved    (pp. 143–159)
TRANSCRIPTION COMPLETE: 159/159 pages plus front matter. Totals: 83
candidates, 0 corrected, 83 witness's fault. check.py: all 159 markers,
braces balanced, 11 footnotes; joints clean except p. 143, where joints.py
flags a blank line after "(... p. 54. 313.)" -- a false alarm: p. 143 opens
a new paragraph. Sandbox compile 106 pp., 0 errors. Header LAYOUT and
ACCURACY written. Catalog: Transcription (1892) and KB scan links added;
the note says the translation follows the 1919 edition.
Four UNSURE readings for the second reading (pp. 5, 77, 84n, 146).
Cost of wave 2 ≈ 960k tokens (≈ 12.5k per page). Whole transcription
≈ 2.4M tokens.

NEXT: see below.

## Third-witness check instead of a full second reading (2026-09-27)

Decision (Hans): no full second reading (est. 1.5–2M tokens). Instead:
tesseract 4.1 with the Danish model (Debian package tesseract-ocr-dan) run
over all 159 pages at 300 dpi (--psm 4), compared word by word with the
transcription by a short Python script (difflib per page; flags real-word
substitutions within edit distance 2 and single short words present in one
text only). 100 flags: 73 tesseract insertions (72 stray i/f/p at line ends
from gutter/pencil marks), 10 tesseract drops (9 confirmed by the ABBYY
layer), 17 substitutions + 1 unequal variant; 14 read at the image.
ONE CORRECTION: p. 7 "en" -> "én" (faint printed accent).
The four UNSURE readings settled at the image: p. 5 "ish" (printer's error
for ist, under a reader's ink t); p. 77 "Bégrundelse" (printed é); p. 84n
acute on the omicron; p. 146 stray mark, not transcribed. No UNSURE left.
Header ACCURACY records all this. Cost ≈ 40k tokens.

NEXT: see below.

## 1892 transcription vs the e-book (2026-09-27, script, no agents)

Word-level diff (difflib) of the 1892 body text (footnotes excluded) against
the SAGA e-book body text, lower-cased, å->aa, accents folded.
- 92% of the 1892 words match. The e-book is NOT the 1919 print as printed:
  it is a 2020 modernisation (vilde->ville, ere->er, have->har, Existents->
  eksistens, å, lower-case nouns, compounds closed up) with typos of its own
  (e.g. "Sildetimens", "aflivet"). ~1,170 differences are this spelling layer
  alone; irrelevant to an English translation.
- The e-book body has NO inline citations: ~70 references in the 1892 text
  (Efterladte Papirer with year and page, Uvidensk. Efterskrift p. N,
  Stadier, Enten–Eller, Øjeblikket, Høffding's own Psykologi, Etik, Filosofien
  i Tyskland efter Hegel, Tilskueren) are absent, and so from translation.tex.
- Real revisions (1919): about a dozen passages. Largest: p. 36 (~370 words
  added on Kierkegaard's youth, the "svireperiode" and the father's curse,
  from the Heiberg–Kuhr Papirer); additions pp. 29, 39, 74, 130, 138; the
  closing line p. 159 ("i den sidste Menneskealder" -> "og ud over Norden");
  deletions pp. 9, 21, 52, 62, 65, 80, 83, 113, 115, 123, 156. Plus some
  80–150 small word-level changes (e.g. p. 23 Forudsætninger -> overleveringer,
  p. 28 "Selvmord ere hyppige herovre" dropped, p. 37 Bekendelse -> skriftemål,
  p. 73 Kriser -> storme).
- translation.tex has 19 footnotes (1892: 11), only 9 citations of the
  Papers, and no page markers at all.
The change list (JSON, 1892 page per change) is in the cloud workspace only.

## Translation revision to the 1892 text — pilot (2026-09-27)

Brief: REVISION-BRIEF.md; change map: CHANGES-1892-vs-ebook.txt (script
output, 354 entries on 130 pages). Text-only agents; old English reused
where it renders the 1892 Danish.
Pilot, front matter + pp. 1–27: 20 % REV: sites (1919 "nu 1890" -> 1892
"i det sidste Aars Tid"; 8 inline references restored; 2 1919 notes
removed; retranslations e.g. Forudsætninger = presuppositions, altid =
always, højeste Enhed = highest unity). Caller removed italics the agent
had put on reference titles (the 1892 print sets them roman) and added
that rule to the brief. tr_audit: 27 pages, 1 explained flag (p. 21 italic
part-word "expli-" kept whole on p. 22). Fragment tr/pp1-27.tex held in the
cloud workspace until assembly. Cost ≈ 160k tokens (≈ 6k per page).

Revision completed (2026-09-27): five more text-only batches (pp. 28–53,
54–81, 82–118, 119–142, 143–159), 175 further % REV: sites (195 in all).
Highlights: p. 36 1919 addition removed and the 1892 page translated afresh;
pp. 29, 39, 74, 130 1919 additions removed; 1892 passages restored pp. 62,
65, 80, 83, 113, 149; about 180 inline references restored in all (roman,
Danish titles, as printed); 11 footnotes = the 1892 set (five the old English
lacked restored: pp. 34, 50, 59, 64, 105), 1919 notes removed;
old mistranslations corrected (p. 46 "higher unity" reversed; Synspunktet
title; p. 141 „Mutters Egoisme“); last line = 1892 „i den sidste
Menneskealder“. Assembled translation.tex replaces the 1919-based file
(the old version is in git history). tr_audit: 159 pages, 1 explained flag
(p. 21). Sandbox compile 109 pp., 0 errors. Catalog: note and link label
updated. Cost of the revision ≈ 950k tokens (pilot 160k + 790k).
OPEN (optional): independent review of the revised translation.
