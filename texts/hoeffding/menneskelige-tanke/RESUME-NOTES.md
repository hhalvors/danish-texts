# Høffding — Den menneskelige Tanke, dens Former og dens Opgaver (1910): transcription resume notes

Source of truth: scan.pdf (Gyldendal/Nordisk Forlag, København og Kristiania, 1910).
This is a **transcription** job (no OCR transcription existed); build `transcription.tex`
(Danish) from the scan, then translate later per ../../../TRANSLATION-PLAYBOOK.md.

Page-offset: **PDF = printed + 15** (printed p.1 = PDF p.16; verified vs the p.373 running header).
Scan: ~/bibliotek/Høffding, Harald/den-menneskelige-tanke.pdf → copied to scan.pdf here.
Total: 392 printed pp. / 413 PDF pp.

## Typography / OCR notes
- Roman/antiqua type (NOT Fraktur). The scan carries a usable **embedded OCR text layer**
  (`pdftotext -f P -l P scan.pdf -`); use it as the base, then verify each page against a
  rendered image for the things the text layer drops.
- **Emphasis = true italics** in print (e.g. *søge efter*, *tænke paa*) → `\emph{}`.
- **Cited author names are letterspaced** (Locke, Hume, Mill, William James, Henri Bergson,
  Hamann, Herder, Jacobi, Kant) = emphasis → `\emph{}`. Genitive: `\emph{Hamann}’s`.
  (Usually only the FIRST mention is letterspaced; later mentions are roman.)
- **Foreign inline phrases are set ROMAN**, not italic (e.g. "(continuous transitions)",
  "(durée hétérogène et indistincte; durée dont les moments se pénètrent)",
  "en continuité mouvante, en unité de direction"). Do NOT italicize these.
  Work TITLES in footnotes ARE italic (*The Stream of Thought*, *Principles of Psychology*,
  *Introduction à la Métaphysique*); journal names roman (Mind, Revue de Métaphysique…).
- Quotes: „…“ (low-high). The text layer renders the closing “ as `44` — fix it.
- Common text-layer slips seen: horm→Form, lJ vilkaarligt→Uvilkaarligt, Bes1utning→Beslutning,
  Yirkemaade→Virkemaade, dropped/again-joined words. Always image-verify.

## Orthography (preserve 1910 spelling exactly)
aa (not å); capitalized nouns; **Ti / ti** for "thi" (for/because); **idethele** as one word;
modern **gennem** (not gjennem); **skønt** (not skjønt); but **Skjul**, **afgjørende** keep j;
Existens, Villie, exakt/experimental (x), f.\ Ex., o.\ s.\ v., d.\ v.\ s.

## Structure (from Indhold, PDF pp. 12–13) — printed-page starts
- I. Tankens Psykologi (Funktioner) — p.1 ; A. Psykisk Energi p.1, B. Anskuen… p.37,
  C. Dømmen p.71 (TOC misprints "154" for C; subparts a–d at 71/74/82/99)
- II. Tankens Historie — p.109 ; A. Animisme… p.109, B. Antik og moderne Tænkning p.123
- III. Tankens Former (Kategorier) — p.135 ; A p.135, B p.154, C p.175 (a–d), D p.207, E p.237
- IV. Tankens Opgaver (Problemer) — p.246 ; A. Erkendelsen p.254, B. Verdensanskuelse p.306,
  C. Vurdering p.347 (a. etiske p.350, b. religiøse p.369)
Book ends p.392.

## CURRENT RESUME POINT
Next marker: `% [text to be added: pp. 191--200]` — Part III.C "Formale Kategorier",
sub-subsection "2) Tal" (§78) continues. p.190 ends MID-SENTENCE/MID-WORD: "…Disse Akter ere
af samme Art, som de, der førte fra Nr. 1 til Nr. 8. Derved" → p.191 continues directly (NO
blank line — join on same line). Compiles 0/0 (152pp w/ amsmath+amssymb).

### IMPORTANT correction logged (batch 18 had skipped pp.179--180)
Batch 18's Edit stopped at the END of p.178 ("…Intellektuelt set") but the marker was wrongly
labelled "181--190". Batch 19 therefore covered **pp.179--190** (the two skipped pages + the
labelled decade), re-aligning the decade scheme. Seam fixed: "…Intellektuelt set" now continues
"er Identiteten et mægtigt Tankevaaben overfor Mangfoldighedens Forvirring." (same paragraph).
Going forward the decades are aligned again (next = 191--200).

### Batch 19 done (pp.179--190, §§74--78)
- **NEW subsection** `\subsection*{b. Kvalitetsforhold}` (+addcontentsline) at **p.180** (§74 follows).
- **NEW sub-subsections** (first use of `\subsubsection*` + `\addcontentsline{toc}{subsubsection}`):
  `1) Tid` at **p.186** (§76), `2) Tal` at **p.189** (§78). These are the "fire Kvaliteter"
  (Tid, Grad, Tal, Sted) — expect `3) Grad` / `4) Sted` headings in coming batches.
- §74 p.180; §75 p.182 (Analogi: Aristoteles/Kant); §76 p.186 (Tid); §77 p.188 (Rum/Tal needed);
  §78 p.189 (Tal). §73 (a. Identitet) ran p.177–180top.
- Greek: παράδειγμα (p.179); δύναμις οὐχ ἥσυχος (p.189 fn, Plotinos).
- Letterspaced names (\emph): Sokrates (p.179), Telesio/Bruno (p.179), Maxwell (p.179, p.183×2),
  Platon (p.180 1st only; "for Platon" 2nd = roman), Aristoteles+Kant (p.182), Leibniz (p.183,
  p.184), Kant (p.183), Cournot (p.183, p.184), Young/Faraday (p.184), Luther/Zwingli/Arrhenius/
  Ostwald/Mach/Ramsay (p.185); fn names \emph: Th. Mertz (p.184), Chr. Christiansen (p.184),
  Plotinos/Augustinus (p.189). ROMAN (passing/2nd mention): Eutyfron + "Platons Eutyfron" (p.179),
  Spinoza/Leibniz/Hume (p.183 "saaledes Spinoza og Leibniz"/"(Hume)"), Aristoteles/Newtons (p.189),
  Adam Homo's (p.180), "Maxwellske" adj (p.188), Mach/Hertz/Maxwell inside p.184 fn.
- Italic work-titles: Fajdon (p.180), Den nyere Filosofis Historie² (p.179 fn, p.183 fn),
  Matter and Motion (p.180 fn), Om Begrebet Analogi… (p.182 fn), History of European Thought…
  (p.184 fn), Om Faradays Kraftlinier (p.183 fn), L'enchainement des idées fondamentales (p.184 fn),
  Om det elektromagnetiske Grundlag for Mekaniken (p.184 fn), Ennead. + Confessiones (p.189 fn).
  Journals/series roman: Tidsskrift for Fysik, Mindre Arbejder; „…"-quoted German titles roman.
- Faithful quirks preserved: "neppe" (p.187); "negte" (p.183); "Kuethed" (p.187); "Førnutiden"
  (p.187); "Det kan vare praktisk" (p.188 — printed "vare", not "være"); "véd" earlier; accents
  "Idé" (p.180). En-dash ranges: p. 74--75, 16--89. Trailing em-dash kept: „at være". ---

### Batch 18 done (pp.171--180, §§70--73)
- **NEW Section C** `\section*{C. Formale Kategorier}` (+addcontentsline +`\label{sec:formale-kategorier}`)
  added at **p.175** (mid-page, after "…den specielle Kategorilæres Tredeling.").
- **NEW subsection** `\subsection*{a. Identitet}` (+addcontentsline) at **p.177** (§73 follows).
- Section breaks: text p.171–172top is the TAIL of §69 (absolut Identitetsrække disc., Leibniz/
  Parmenides/Platon/Spinoza); **§70** begins p.172 ("Hensigten med Opstillingen…"); **§71** p.173
  ("Som allerede bemærket (61)…"); **§72** p.175 (after C heading, "Hvad det saa er…"); **§73**
  p.177 (after a. Identitet heading, "Identitet er en Grad eller Art af Lighed.").
- p.176 inline formula (the only math this batch):
  `$a \overset{\angle}{\underset{=}{\to}} b \overset{\angle}{\underset{=}{\to}} a \ldots$`
  (∠ over each arrow, = under). `\overset/\underset/\angle` from amsmath/amssymb. Other inline:
  `$A = A$`, `$a$ og $a$`, `$a_1$ og $a_2$`, `$a$ og $b$`, `$a$ og non-$a$`, "Identitet$+$Forskel".
  Verified rendered (form_check page).
- Italic defined terms: de formale/reale/ideale Kategorier (p.174–175), Elementer (p.175),
  Identitet + Kvaliteterne + Negationens Kategori + Rationaliteten (p.176), samme (p.177 "samme Art").
- Letterspaced names (\emph): Leibniz ×5 (p.171, genitive `\emph{Leibniz}'s`), Parmenides/Platon/
  Spinoza (p.171), Naphtali Cohen (p.172). In FOOTNOTES names ARE letterspaced too (confirmed by
  existing file convention `\emph{Gassendi}:` etc.): Couturat/Kant (p.171), Husserl (p.177),
  Zeuthen/E. Mach (p.178).
- „…" quotes roman: „subjektive"/„empiriske"/„illusoriske" (p.172), „virkeligt" (p.175), „dele" (p.178).
- Footnotes: p.171 `\emph{Couturat}: \emph{La Logique de Leibniz}` + Bulletin de la Société française
  de philosophie (roman journal) + `\emph{Kant}: \emph{Kritik der reinen Vernunft}²`; p.177
  `\emph{Husserl}: \emph{Logische Untersuchungen}. II. p. 112 f.`; p.178 *) Zeuthen Matematikens
  Historie + Mach Erkenntnis und Irrtum, **) min Psykologi⁵.
- Faithful quirks preserved: "ti" for thi (p.174 "ti om alle Emner"); "véd jeg" with accent (p.177);
  "havt" (p.178 fn); print quirk **"Smlgn." in fn *) but "Smgln." in fn **)** on p.178 — kept verbatim.
- Ranges en-dash: (2)--(4), (62--69). Trailing em-dash before paragraph break kept ("…skydes ud. ---").

### Sandbox compile recipe UPDATE (batch 16+)
Because of $\gtrless$ (batch 16) and $\underset$ (batch 17), the throwaway sandbox copy must
swap libertinus→lmodern AND inject amsmath+amssymb. Working sed:
`s/\\usepackage{libertinus}/\\usepackage{lmodern}\\usepackage{amsmath}\\usepackage{amssymb}/`
(plus delete libertinust1math + textalpha lines, plain babel, Greek→[Gr]). Order matters: do
the line-deletes/babel BEFORE the libertinus→lmodern swap. The REAL file is unaffected —
libertinust1math already provides all of these.

## (previous) RESUME POINT
Next marker was `% [text to be added: pp. 141--150]`. Body broke mid-word at p.140
("…Lighed og Ulig-") → p.141 "[hed]…". DONE.
**PART III "Tankens Former (Kategorierne)" BEGUN** — chapter heading added at p.135, with
`A. Kategorilærens Historie og Metode` section heading. §§51--53 (Aristoteles/Kant as the two
Mestre; the category question-list; Platon). Greek this batch: δύναμις (p.131, one instance
only — the 2nd "(δύναμις)" the OCR suggested is NOT in print). Latin/foreign ALL roman as
printed: salva veritate, qualitates occultæ (p.131); spatium absolutum/sensorium dei (p.140);
the Leibniz Latin fragment + French "La loi du changement…" (Lettre à Basnage 1698, p.132);
Couturat's Vis activa… Work-titles italic: Fajdon (p.131), Den nyere Filosofis Historie² +
journal "Bulletin de la Société Française de Philosophie" roman (p.132 fn), L'évolution
créatrice (p.133 fn, Bergson), Filosofien og Livet (p.138 fn). Name letterspacing verified by
zoom: emphasized = Platon (p.131, p.140 "For Platon"), Leibniz ("danner her Overgangen" p.132
ONLY — "Leibniz ikke bragte"/"Leibniz er klar over" are ROMAN), Henri Bergson (p.133, 1st),
Aristoteles (p.135, p.136 "gjorte af"), Kant (p.136 "og Kant"), Kant+Stumpf (p.139);
Kopernikus/Bruno/Descartes/Kant ALL letterspaced (p.134). NOT emphasized (roman) = Spinoza/
Hegel/Newton (p.140), 2nd mentions (Bergson, Aristoteles/Kant "gaar den ene Vej", Stumpfs
Udtryk), Platon/Aristoteles in passing-list (p.140 "Modsætningen mellem"). Section B "Antik og
moderne Tænkning" CLOSED at p.134 (ends with centered rule before Part III). Question-list on
pp.137--138 set as separate short paragraphs. Edition markers superscript. Compiles 0/0 (113pp).
Notes: footnote-cited author names ARE letterspaced too (Wundt, Ramon y Cajal, Herrlin, p.27).
Emphasis can be ordinary contrast words too (e.g. *slutte*/*udlede* p.31; *hvem/har/udøver*
p.34). Latin set ROMAN when the print sets it roman (e.g. "qvalitas occulta" p.33) — match the
page, do not auto-italicize Latin. "Ramon y Cajal" printed without accent → keep as printed.
Section B added at p.37 ("B. Anskuen, Association og Sammenligning" → "a. Sansning").

Refined name rule (important): author names are letterspaced ONLY when the figure is the
key subject under discussion — NOT every mention. Verify each by zoom. Examples seen:
emphasized = Locke/Hume/Mill, William James, Henri Bergson, Hamann/Herder/Jacobi, Kant
(p.8); Hume, Kant (p.15); Fries, Henri Bergson (p.16); Stumpf (p.18); Sir William Ramsay,
Ernst Mach (p.19); Pawlow (p.20). NOT emphasized (roman) = Platon/Aristoteles/Plotinos/
Leibniz, "Lockes Forudsætning" (p.15); "John Locke" (p.12); 2nd mentions of Fries/Bergson/
Stumpf. For "J. F. Fries" only the surname is letterspaced → `J.\ F. \emph{Fries}`.
Emphasis is also true italics for ordinary words (e.g. *hvilken* … *hvilken*, p.17).

## DONE so far (don't redo)
- Through p.170: Part III.B continues — §§61–69, the systematic typology of Forskels-/
  Lighedsrækker (chaotic, indefinitely/regularly/identically varying, progressive,
  reciprocal, identity), each with its centered formula (1)–(8). Heavy use of display math
  (\wedge with \underset subscripts, \smile, arrows). Footnotes: p.161 Lipps; p.163 de Morgan
  + James; p.170 Leibniz (ed. Erdmann).

- Through p.160: Part III.A finished (§§56–57: Kategorilære history — Comte, Renouvier,
  Hartmann, Herbart, Aristoteles; the method of building from simplest categories). **Part
  III.B "Fundamentale Kategorier" BEGUN** (heading at p.154): §58 Syntesen as first category,
  §59 Kontinuitet/Diskontinuitet (Poincaré antinomy, Kierkegaard's Spring, Newton/
  Aktualitetsprincip), §60 begun (Ligheds-/Forskelsforhold). Footnotes batch 16: p.151 Den
  nyere Filosofis Historie² (×2); p.152 Séailles/Dauriac + Arthur Drews (Hartmanns phil.
  System); p.157 La Science et l'Hypothèse.

- Through p.150: Part III.A "Kategorilærens Historie og Metode" §§53(end)–56: Platon &
  Aristoteles' category-doctrines (the ten categories, οὐσία as substrate), Plotinos and
  Augustinus on the categories vs. the divine; §54 Kant (categories from the judgment-table,
  the Continuity criterion, the Størrelse/Kausalitet schema-table p.145); §55 Hegel (the
  dialectic, Goethe quote, the I/II/III system-list p.149); §56 William Hamilton begun
  ("to think is to condition"). Footnotes: p.142 Trendelenburg + Grote; p.143 Arthur Drews;
  p.144 G. E. Schulze; p.145 Kritik der reinen Vernunft²; p.146 Om Kontinuiteten….

- Through p.140: Part II.B "Antik og moderne Tænkning" §§49--50 finished (Leibniz's
  identity-logic, force vs. law, Bergson on the modern vs. antique). Part II CLOSED at p.134.
  PART III "Tankens Former (Kategorierne)" BEGUN: A. Kategorilærens Historie og Metode,
  §§51--53 (Aristoteles & Kant as the two masters; the category question-list; Platon).
  Footnotes batch 14: p.132 Den nyere Filosofis Historie² + Couturat/Bulletin (Latin
  fragment); p.133 Bergson L'évolution créatrice; p.138 Filosofien og Livet.

- Through p.130: Part II.A "Animisme, Platonisme og Positivisme" §45 COMPLETE; Part II.B
  "Antik og moderne Tænkning" §§46–49 (Parmenides/Herakleitos/Demokritos, Platon, Aristoteles,
  Renaissance: Cusanus/Bruno/Tyge Brahe/Galilei/Bacon, Leibniz). Batch 13 footnotes: p.124
  Parmenides (Mindre Arbejder); p.126 Sextus Empiricus + Platon/Demokritos Afhandling; p.127
  Religionsfilosofi; p.130 Den nyere Filosofis Historie + Couturat (La Logique de Leibniz).

- Through p.120: Part II.A "Animisme, Platonisme og Positivisme" §§41–44 (Hegel/Comte,
  Frazer, the Kepler/Descartes/Leibniz/Newton/Linné/Kant animism examples, Platon's Ideas).
  Batch 12 footnotes: p.112 Holberg/Schneedorff (Danske Filosofer); p.113 Den nyere Filosofis
  Historie + Hobhouse, and Frazer Golden Bough/Adonis-Attis-Osiris; p.115 Religionsfilosofi;
  p.117 Den nyere Filosofis Historie; p.119 Natorp (Plato's Ideenlehre) + Stewart.

- Through p.110: PART I "Tankens Psykologi" COMPLETE (A Psykisk Energi, B Anskuen/Association/
  Sammenligning, C Dømmen incl. d. Dommens Gyldighed §§36–39). PART II "Tankens Historie"
  begun: A. Animisme, Platonisme og Positivisme §40. Batch 11 footnotes: p.102 Meinong/Stumpf;
  p.104 Psykologi V D + Sextus Empiricus; p.105 Galilei Dialogo + Bradley/Moderne Filosofer;
  p.110 É. Durckheim (Revue de Métaphysique).

- Preamble, title page, Forord (Aug 1910), printed pp. 1–60. Part I.A "Psykisk Energi"
  (§§1–10) COMPLETE; Part I.B "Anskuen, Association og Sammenligning": a. Sansning,
  b. Genkendelse (§§14–16) COMPLETE, c. Erindrings- og Fantasianskuelse (§§17–18) COMPLETE,
  d. Forestillingsassociation (§§19–20), e. Sammenligning (§§21–23) — Part I.B COMPLETE.
  Part I.C "Dømmen": a. Domsdannelse (§§24–25), b. Hindringer for Domsdannelse (§§26–28),
  c. Subjekt og Prædikat (§§29–35), d. Dommens Gyldighed (§36) begun, through p.100.
  Footnotes added batch 10: p.93 Erdmann Logik; p.96 Aristoteles (Analyt. post./De categ.)
  + Eilschow + Jens Kraft + Højsgaard; p.97 Wundt (Logik³) + Erdmann + Jerusalem (Die
  Urteilsfunktion); p.98 Leibniz Dialogus + my Analogi-Afhandling. Earlier footnotes
  pp.6–90 as listed above.

## Conventions
See ../../../TRANSLATION-PLAYBOOK.md plus the book-specific notes above.
