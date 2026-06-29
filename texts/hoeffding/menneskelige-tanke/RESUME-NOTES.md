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
Next marker: `% [text to be added: pp. 281--290]` — Part IV.A.b.β §117 continues (Aarsag/
Erfaringens Analogier; we keep applying the cause-form to examine objects). p.280 ends
MID-SENTENCE: "…Vi faa ved dette Synspunkt en stadig Opfordring til at undersøge Emnerne saa
nøje som muligt, for at" → p.281 continues the sentence (join directly, no blank line).
Compiles 0/0 (221pp).

### Batch 28 done (pp.271--280, §§112(end)--117) — NEW subsection IV.A.b + sub-subsections α, β
- §§112(end)--113 finish "a. Former og Principer" (the three -ismer balanced; Kriticismens
  analytic method). **NEW subsection** `\subsection*{b. Former og Emner}` (+addcontentsline) at
  **p.274** (§114, Identitetsprincipet). Under it, **NEW sub-subsections** (centered headings with
  **Greek-letter** leads): `\subsubsection*{α. Kvalitet og Kvantitet}` at **p.274** (§115--116)
  and `\subsubsection*{β. Succession og Kausalitet}` at **p.278** (§117). (These α/β ARE headings,
  unlike the run-in α/β/γ -ismer of batch 27.)
- Seam p.270→271: "…som James saa mesterligt har skildret, er der ingen Forskel mellem Motiv,
  Form og Emne;…".
- Greek (real file): φορά, μεταβολή, αὔξησις καὶ φθορά (p.276, Aristotle's kinds of change).
- Letterspaced names (\emph): \emph{Kant} (p.275/278 "Kant gik"; also fn p.272), \emph{Aristoteles}
  + \emph{Demokrit}s/\emph{Platon}s genitives (p.276), \emph{Galilei} (p.276 1st; later roman),
  \emph{Descartes}/\emph{Newton}/\emph{Holbach} (p.277), \emph{Leibniz}/\emph{Berkeley}/\emph{Kant}
  (p.277), \emph{Hume} (p.279; fn). Footnote-name leads \emph: \emph{Will.\ Occam}/\emph{Kopernikus}/
  \emph{Newton}/\emph{Kant} (p.272 fn), \emph{Hume} (p.279 fn).
- Italic emphasis word: \emph{hvad} (p.273). 2nd-mention names roman (Galilei, Kant, Hume,
  Descartes p.279).
- Footnotes: p.272 *) long Occam/Simpelhedens-Princip note — Latin "frustra fit per plura qvod
  fieri potest per pauciora" (roman, v-spell "qvod") + „favor ille unitatis… necessitatem" (roman
  Latin in „") + \emph{De mundi sensibilis atqve intelligibilis forma et principiis} (italic) +
  \emph{Kritik der reinen Vernunft}² ; p.279 *) \emph{Hume}: \emph{Treatise on Human Nature}. I,3,6.
  (ed. Selby-Bigge p. 91).
- German/Latin/quote ROMAN as printed: Kant Hertz-letter quote „Kun derved blive Tingene…" with
  "a priori" roman (p.276); „den mekaniske Mytologi"/„første og reale Egenskaber"/„forsaavidt"/
  „fordi"/„Erfaringens Analogier"/„Ideernes" all roman in „".
- FAITHFUL oddities kept: **"hvorom"** (p.271 "Den Økonomi, hvorom… virker"), event-labels
  "Begivenheden A"/"Begivenheden B" as plain roman (p.278). x-spell: Exempel, existerer, exakte,
  Praxis; but **"Eksperiment"/"Eks."** with k also occur. En-dash ranges: 12--13. No display math.

### Batch 27 done (pp.261--270, §§108(end)--112) — IV.A.a continues, the three -ismer
- Part IV.A.a "Former og Principer" §§108(end)--112. §112 surveys the three modern
  erkendelsesteoretiske retninger; subsections are run-in **Greek-letter** markers
  **α. / β. / γ.** (Formalisme / Empirisme / Pragmatisme) — NOT centered headings, just inline
  paragraph leads (kept literal α β γ; real preamble has textalpha).
- Seam p.260→261: sentence joined "…der er affaldet fra „Ideernes" rene Verden; det er Ideerne…".
- Letterspaced names (\emph): \emph{Leibniz} (p.261; later "Leibniz"/"Leibniz'" roman),
  \emph{Kant} (p.262 "Kant, der dog ellers"; elsewhere on these pages Kant/Kants mostly ROMAN —
  verify each), \emph{Spinoza}s og \emph{Hegel}s genitives (p.263), \emph{Kopernikus} (p.264),
  \emph{Platon}/\emph{Aristoteles}/\emph{Grote}/\emph{Gomperz}/\emph{Teichmüller} (p.265--266),
  \emph{Kant} α-lead genitive \emph{Kant}s (p.266), \emph{Thomas Hobbes}/\emph{Fichte} (p.267),
  \emph{Kierkegaard}/\emph{Kroman} (p.268), \emph{Hume}/\emph{Stuart Mill}/\emph{Herbert Spencer}
  (p.269), \emph{Avenarius}×2/\emph{Ernst Mach}/\emph{William James} (p.270). 2nd mentions roman.
- Greek (real file): νοῦς, ἀρχαί (p.265, Aristotle's Fornuft/Principer).
- French/Latin/German set per print: Leibniz "cela donne \emph{un parfait retour}, suffisant à
  démontrer la vérité de l'hypothèse" + \emph{à rebours} (p.261; ONLY those two italic, rest
  roman); „suivant son point de vue," (p.262, roman in „"); "Gross ist die Welt, und das Gehirn
  ist klein" (p.262, reversed Wallenstein, roman); Hobbes "rationis prima principia vera esse
  facimus nosmet ipsi" (p.267, roman); „Thatsache"/„Thathandlung", „Ding an sich" (roman).
- Footnotes: p.261 *) \emph{Leibniz}: \emph{Nouveaux Essais}…(Erdmann)…\emph{Hobbes}:
  \emph{De corpore}; p.263 *) \emph{Om Kontinuiteten i Kants filosofiske Udviklingsgang}…+
  \emph{Kritik der reinen Vernunft}²…+ \emph{Mindre Arbejder}; p.266 *) \emph{Aristotle}.
  II.237… **) \emph{Studien zur Geschichte der Begriffe} 409--426; p.267 *) Computatio siva
  Logica (1655) III, 8--9 (ROMAN, faithful "siva"); p.268 *) \emph{Grundlage der gesammten
  Wissenschaftslehre} **) \emph{Uvidenskabelig Efterskrift} ***) \emph{Vor Naturerkendelse}.
- FAITHFUL typos kept: **"f. Eks."** (p.266, vs the usual "f. Ex." which also appears p.265/268),
  **"siva"** for sive (p.267 fn), **"paa hvilket Trin"** (p.262). Italic emphasis word:
  \emph{foruden} (p.262). „…"-quotes roman: „Ideernes"/„Tingen i sig selv"/„Stoffet"/„Former"/
  „Stof"/„Form"/„Hoved(et)"/„Hjerte(t)"/„Fornuften"/„Bevis"/„Fornuften tigger ikke…". x-spell:
  Vexelvirkning, Reflexion. En-dash ranges: 33--35, 237/275/375, 409--426, 8--9, 1--3, 270--274.

### Batch 26 done (pp.251--260, §§104(end)--108) — NEW SECTION IV.A "Erkendelse"
- Part IV.Indledning finishes §§104(end)--105 (p.251 cross-refs author's own Psykologi/Etik, set
  ROMAN in body — NB the footnote version of \emph{Psykologi} stays italic); the centered rule at
  end of Indledning closes it at p.254.
- **NEW Section A** `\section*{A. Erkendelse}` (+addcontentsline +`\label{sec:erkendelse}`) at
  **p.254**, immediately followed by **subsection** `\subsection*{a. Former og Principer}`
  (+addcontentsline). Print heads: "A. Erkendelse." / "a. Former og Principer." (running header
  combines both). §§106--108 (Former/Principer; the dynamic truth-concept).
- The four Principer named in one long §106 paragraph, each set italic: the Relation principle
  \emph{ethvert Emne skal betragtes i saa mange Forhold (Relationer) som muligt} (italic ENDS at
  "som muligt" — rest roman), \emph{Konsekvensens Princip}, \emph{Aarsagsprincipet},
  \emph{Spørgsmaalet om Helheddannelser og om Udviklingsstadier}.
- Letterspaced names (\emph): \emph{Kant} (p.258 "Kant begik", p.260 "saa Kant selv"),
  \emph{Maimon} (p.259). Passing-list names ROMAN: "(Maimon, Fichte, Fries)" (p.260),
  "Pytagoras/Platon/Spinoza/Newtons" (p.260). Italic emphasis word: \emph{vi} (p.260).
- Footnotes: p.253 *) Se herom min \emph{Psykologi}. Kap. I.; p.256 *) …\emph{Psykologi}, V D., 1--4…
  (Aarsagsprincip); p.259 *) \emph{Den nyere Filosofis Historie}² II. p. 121; 123 (Maimon).
- German/Latin ROMAN as printed: Wallenstein quote "Eng ist die Welt, und das Gehirn ist weit."
  (p.254), „Ding an sich"/„Erfaringsanalogi" (p.260). „…"-quotes roman: „Stoffet"/„Ide"/
  „Overensstemmelse"/„selve Tilværelsen"/„andre"/„Virkeligheden".
- FAITHFUL typos kept: **"fornegte"** (p.256), **"underligge"** (p.256), **"uafsluttelig
  Tankearbejde"** (p.259), **"paa hvilket vi rent logisk"** (p.256). x-spell: Vexelvirkning,
  existerende, strax. En-dash ranges: 1--2, 1--4, 36--38; 68; 121; 123. No math, no Greek.

### Batch 25 done (pp.241--250, §§100-bis(end)--104) — PART IV BEGINS
- Part III.E "Ideale Kategorier" finishes: §100-bis end (p.241), §101 with TWO new subsections
  `\subsection*{1) Formale Forskelligheder}` (p.241) and `\subsection*{2) Reale Forskelligheder}`
  (p.243), each +addcontentsline subsection. §102 (p.244) closes Part III at p.245 (centered rule).
- **NEW PART IV** at **p.246**: `\chapter*{IV. Tankens Opgaver (Problemer)}` (+addcontentsline
  chapter +`\markboth{IV. Tankens Opgaver}{…}` +`\label{ch:opgaver}`), then centered rule, then
  `\section*{Indledning}` (+addcontentsline section). Print shows the heading as "IV" / "TANKENS
  OPGAVER (PROBLEMER)" (all-caps) with a rule beneath; rendered title-case to match Parts I--III.
- §§103--104 (Indledning): §103 Problemernes Naturhistorie (\emph{Richard Avenarius}); §104 the
  three Elements (Form/Emne/Værdi) → the three master-problems: \emph{Erkendelsesproblemet} (1st
  italic, 2nd roman), \emph{Tilværelsesproblemet}, \emph{Vurderingsproblemet}, + det æstetiske/
  etiske/religiøse Problem.
- Lettered run-in items under the subsections begin with an italic term: a) \emph{Elementære
  Værdier}/\emph{Ideelle Værdier}; b) \emph{Umiddelbare Værdier}/\emph{middelbare Værdier}/
  \emph{Formaal}; c) \emph{potentielle og aktuelle Værdier}; (reale) two groups \emph{Værdiernes
  Indhold}/\emph{deres Omfang}; a) \emph{biologiske}/\emph{intellektuelle, æstetiske og etiske
  Værdier}/\emph{religiøse Værdier}; b) \emph{individuelle, sociale og kosmiske Værdier}. Also
  \emph{Norm}.
- Letterspaced name: \emph{Richard Avenarius} (p.246). Latin ROMAN as printed: "amor intellectualis"
  (p.247). No footnotes, no math, no Greek this batch.
- FAITHFUL Danish typos kept: **"Forskydnnig"** for Forskydning (p.242), **"fra umiddelbar Værdi"**
  for faa (p.242), **"dismonisk"** for disharmonisk (p.244). „…"-quote roman: „har" (p.243). x-spell:
  Vexelvirkning, Væxt, Existensbetingelser. En-dash range: (86) cross-refs are plain parens; no
  ranges. Parenthetical/break em-dashes p.241--250 throughout.

### Batch 24 done (pp.231--240, §§97(end)--100, then §100-bis under new Section E)
- Part III.D "c. Udvikling" finishes (§§97(end)--100); **NEW Section E** `\section*{E. Ideale
  Kategorier}` (+addcontentsline +`\label{sec:ideale-kategorier}`) at **p.237** (mid-page, after a
  centered rule `\begin{center}---\end{center}`).
- **FAITHFUL QUIRK — section number 100 REPEATS.** §100 "Teoretisk set…" (p.235, end of D.c) and
  then §100 "Vor Tænkning behandler…" (p.237, first § of Section E) are BOTH printed "100." Kept
  verbatim; expect the next § (p.241) to be 101.
- Seam p.230→231: sentence joined "…i Forholdet mellem Kulturen med den stedse mere fremtrædende
  Arbejdsdeling og Naturtilstandens ensartede og uvilkaarlige Livsform."
- Letterspaced names (\emph), per print: C.\ F. \emph{Wolff} (p.231 & p.233; only surname, as p.230),
  \emph{Goethes} genitive (p.231; whole word letterspaced incl. -s), \emph{Hegel} (p.232 1st; "at
  Hegel"/"hvad Hegel kaldte" 2nd = roman), \emph{Herbert Spencer} + v.\ \emph{Baer}'s (p.232;
  "Spencers" later roman), \emph{Sibbern}, \emph{Roberto Ardigo} (p.232), \emph{Hegel}+\emph{Spencer}
  (p.236, both 1st in context), \emph{Rickert} (p.236). Footnote names \emph: \emph{Goldzieher}
  (p.231), \emph{Diels} (p.238).
- Italic emphasis words: \emph{kun} (p.231; the later „kun" in quotes is roman), \emph{En} Verden
  (p.235), \emph{naar} (p.239 "spørge, naar en Stjerne").
- Footnotes: p.231 *) \emph{Religionsfilosofi} \S\ 14 og 43 + \emph{Goldzieher}/(Die orientalischen
  Religionen. Kultur der Gegenwart…); p.232 *)/**)/***) \emph{Den nyere Filosofis Historie}² II.175 /
  II.457;471--473 / \emph{Danske Filosofer} 99--101; p.233 *) \emph{Moderne Filosofer} 33--37; p.236
  *) \emph{Die Grenzen der naturwissenschaftlischen Begriffsbildung} 451--463 (FAITHFUL German typo
  "naturwissenschaftlischen" w/ extra s); p.238 *) Melissos fra Samos (\emph{Diels}:
  \emph{Vorsokratiker}¹ 150 f.).
- FAITHFUL Danish typos kept: **"emllem"** for mellem (p.239 "i Forholdet emllem Form og Emne"),
  "negte" (p.234), "ligge" for ligger (p.235, p.240), "Nevtrale" for Neutrale (p.240), "metodisk"
  (p.236). Foreign roman as printed: "eo ipso" (p.236), (Ziel)/(Genesis)/(Orthogenesis) (p.236).
  „…"-quotes roman: „kun"/„Verden"/„en højere Enhed"/„Maal"/„foretrække"/„negative".
- En-dash ranges: 471--473, 99--101, 33--37, 451--463, 36--38, 85--88. Parenthetical em-dashes
  (--- … ---) p.231/239. No math this batch.

### Batch 23 done (pp.221--230, §§93(end)--97)
- Part III.D "Reale Kategorier": §§93--96 finish `b. Totalitet`; **NEW subsection** `c. Udvikling`
  at **p.227** (§97) — `\subsection*` + `\addcontentsline{toc}{subsection}`.
- Seam: p.220→221 sentence joined "…Forholdet mellem Kategorierne er jo det, at…".
- §94 p.221 (Totalitet vs. tilfældige Produkter; Teleologi/Mekanisme), §95 p.222 (Totalitet-grader,
  Pascal „tænkende Siv", Naturvidenskab vs. Historie, Newton/Kant/Laplace), §96 p.226 (Helhed/Del
  relativitet; Ardigo; absolut Totalitet = „Ide"; Huyghens/Leibniz), §97 p.227 (Udvikling;
  Aristoteles' Mulighed/Virkelighed; Præformation vs. Epigenese).
- Letterspaced names (\emph), per print: Pascal genitive `\emph{Pascal}'s` (p.223); Aristoteles
  (p.223, p.228, p.229 — but many repeated mentions ROMAN); Newton, Kant, Laplace (p.225);
  Ardigo genitive `\emph{Ardigo}'s` + Kant (p.226); Huyghens, Leibniz (p.227); Kant, Salomon Maimon
  (p.228); Leibniz/Haller/Bonnet active mentions (p.229; the list "(Leibniz, Haller, Bonnet)" ROMAN);
  C.\ F. Wolff, Jean Jacques Rousseau (p.230; "Rousseau" 2nd = roman). Renouvier og Hartmann ROMAN
  in cross-ref "(smlgn. 56: …)" (p.221).
- Greek kept verbatim (real file): `κίνησις`, `ἐνεργείᾳ` (p.228--229, Aristotle).
- Latin/German/French/Italian ROMAN as printed: compages mirabilis (p.225), das Einmalige (p.225),
  (indistinto)/(distinti) (p.226), (Stetighed) (p.228); footnote French "La génération apparente…
  [Afvikling]…" (p.230). „…"-quoted phrases roman: „tænkende Siv"/„ædlere" (p.223), „Væsenet"/„Energi"
  (p.228), „Geschichtsphilosophie"/„Göttingische gelehrte Anzeigen" (p.224 fn).
- Footnotes: p.222 self-cites (Vitalisme/„Mindre Arbejder"/Filosofiske Problemer/Om Kategorier);
  p.224 *) H.\ C. Ørsted + \emph{Danske Filosofer}, **) \emph{H.\ Rickert}: Ueber die Grenzen…
  + „Geschichtsphilosophie" + Kuno Fischer + Tænkning og Tro i vore Dage; p.226 *) Moderne Filosofer
  35--37; p.227 *) Den nyere Filosofis Historie² I.346; p.228 *) Versuch über die
  Transscendentalphilosophie (Maimon); p.230 *) \emph{Leibniz}: Système nouveau de la nature, **)
  \emph{Kölliker}: Entwickelungsgeschichte…
- Faithful quirks: "uafslutteligt" (p.226), "antike" (p.229), "Voxen"/"udvoxne"/"Væxten" (x-spelling),
  "Transscendentalphilosophie" (double-s, p.228 fn). En-dash ranges: 5--11, 35--37, 1901--1902.
- Note: scan p.221--222 have pencil ovals/yellow highlights (e.g. „Virkelighedskriteriet", „Emner",
  „Naar man ofte stiller Teleologi…") — annotations, ignored.

### Batch 22 done (pp.211--220, §§89(end)--93)
- Part III.D "Reale Kategorier": §§89--92 finish subsection `a. Kausalitet`; **NEW subsection**
  `b. Totalitet` at **p.218** (§93) — `\subsection*` + `\addcontentsline{toc}{subsection}`.
- Seam: p.210's page-split word completed → "…givne Udviklingstrin former sig." (for-|mer).
- Math (sandbox needs amsmath/amssymb): subscripts p.214 `$B_1$ $A_1$ $B_2$ $A_2$`, series
  `$A_1\,A_2\,B_1\,B_2$`; quantity formulas p.214 `$B = A + \times$` (printed × cross kept) and
  `$C = B \div y$` (÷ = old MINUS glyph, rendered \div as before).
- Letterspaced names (\emph), per print: Zeuthen+Heiberg genitives `\emph{Zeuthen}'s`/`\emph{Heiberg}'s`
  (p.211); Spinoza, Kant, Hamilton, Spencer, Robert Mayer, Colding, Joule, Helmholtz (p.213, all
  1st; "Mayer/Colding/Joule" 2nd = roman); Leibniz (p.215 genitive `\emph{Leibniz}'`, and p.219
  "opstillede derfor"); Heinrich Hertz, Ernst Mach, Hugo de Vries (p.216); Maxwell (p.217);
  Kant genitive `\emph{Kant}'s` + Hume + Fichte (p.217--218; "Hume"/"Fichte" 2nd = roman);
  Hesiodos (p.220). Roman/passing: "Leibniz'" (p.216, p.217), "Efter Leibniz" (p.217), Euklids (p.220).
- Latin/German ROMAN as printed: "causa æqvat effectum" (p.213, faithful "æqvat"), „Ding an sich"
  (p.217), "(sich völlig im latenten Zustande abspielt)" (p.216).
- Footnotes: p.213 (Helmholtz) self-cite \emph{Den nyere Filosofis Historie}² II. 497--499; 597;
  p.216 *) \emph{E.\ Mach}: \emph{Die Mechanik in ihrer Entwickelung}.⁶ p.281, **) \emph{Die
  Mutationstheorie}. I.353. Kfr. II.637; 662; p.217 *) \emph{Matter and Motion}. \S\ 103, **)
  \emph{Zeuthen}: \emph{Matematikens Historie}. II.340; p.218 *) \emph{Begrebet Villie} in „Psyche".
- Italic emphasis word: \emph{blevet til} (p.220). Faithful quirks: "ligessom" (p.214 double-s),
  "irredutible" (p.214), "naat" (p.213), "godtgør" (p.220). En-dash ranges: 497--499.
- Note: scan has pencil ovals/highlights (e.g. around „Virkelighedskriteriet", „Emner") — ignored.

### Batch 21 done (pp.201--210, §§83--89)
- Part III.C "Formale Kategorier": **NEW subsections** `c. Negation` at **p.201** (§83–84) and
  `d. Rationalitet` at **p.204** (§85–86) — `\subsection*` + `\addcontentsline{toc}{subsection}`.
- **NEW section** `\section*{D. Reale Kategorier}` (+addcontentsline + `\label{sec:reale-kategorier}`)
  at **p.207** (§87), then subsection `a. Kausalitet` at **p.208** (§88–89).
- §83 p.201 (Negtelse; Spinoza "omnis determinatio est negatio" Ep.50; Herbart), §84 p.203
  (Platon Sophistes Greek cite), §85 p.204 (Rationalitet), §86 p.205 (∠/= arrow row on p.206),
  §87 p.207 (A=B=C=D; Spinoza/Hume), §88 p.208 (Kausalitet), §89 p.210 (Platon Hulebillede).
- Math (sandbox needs amsmath/amssymb): PLAIN `$A \to B \to C$`/`$A \to C$` (no decorations, p.204);
  `$A=B=C=D$` (p.207); ∠-over/=-under arrows recur p.206:
  `$A \overset{\angle}{\underset{=}{\to}} B … D$`. Letter-series PLAIN roman: "AB og A", "A (non B)"
  (p.202), "A B C D" (p.210).
- Letterspaced names (\emph), per print: Kant (p.201 fn-lead & p.209), Spinoza (p.202 1st;
  "Spinozas" 2nd roman), Herbart (p.202; genitive `\emph{Herbart}'s` p.206), Platon (p.203, p.210),
  Hegel (p.204 1st; "Hegel" 2nd roman), Lessing (p.206), Spinoza+Hume (p.207). Roman:
  Aristoteles og Leibniz BOTH (p.205).
- Greek kept verbatim (real file): `ὄντος πρὸς ὂν ἀντίθεσις` (p.203, Plato Sophist 257); note the
  printed UNBALANCED parens "(ὄντος… ἀντίθεσις.) Sophistes p. 257 E)" — preserved.
- Latin/German ROMAN as printed: omnis determinatio est negatio (p.202), „zufällige Ansichten"
  (p.206). Italic titles: Metaphysische Anfangsgründe der Naturwissenschaft (p.201 fn);
  „Statens" syvende Bog roman (p.210); Sophistes roman (p.203).
- Footnote: p.201 *) Metaphysische Anfangsgründe… p.149 (Kant).
- Faithful quirks: **"Negtelse"/"negtes"** (p.201–202), **"betydnigsfuldere"** typo (p.206),
  **"fordetmeste"** one word (p.205), "Existentialkvaliteten"(36) vs "Existenskvaliteter" (p.208).
  En-dash ranges: (2--3), (22; 26--28), (46--50), (37--38). Parenthetical em-dashes p.201/206/209.

### Batch 20 done (pp.191--200, §§78--82)
- §78 (2) Tal) ran p.189–193; **NEW sub-subsections** `3) Grad` at **p.193** (§79–80) and
  `4) Sted` at **p.197** (§81–82) — `\subsubsection*` + `\addcontentsline{toc}{subsubsection}`.
- §79 p.193 (Grad/Intensitet), §80 p.196 (det bestemte Antals Lov; Renouvier/Dühring),
  §81 p.197 (Sted/Rum; Berkeley), §82 p.200 (Rummets uendelighed/kontinuitet; Russell fn).
- Math (libertinust1math provides; sandbox needs amsmath/amssymb): `$7+1$`, `$100 \div 92$`
  (NB: the ÷ glyph here is the old Scandinavian/German MINUS sign — 100−92=8 — rendered with
  \div to reproduce the printed glyph faithfully); `$A + A = A$`, `$x^2 = x$`, `$A + A = 2A$`,
  `$A < A^2$`. Letter-series rendered as PLAIN roman text (matching print): (A A A\ldots),
  (A B C\ldots).
- Letterspaced names (\emph), 1st mention: Helmholtz, Kronecker, Georg Cantor (p.191; later
  "Cantor" roman), Leibniz (p.191, p.193), Boole (p.191), Kant (p.195; later "Kant" roman),
  Renouvier, Dühring (p.196), Berkeley (p.197; "for Berkeley" 2nd = roman), Kopernikus, Kepler,
  Newton (p.199). Roman/passing: Brunos (p.199), E. Zeller (in p.191 fn parenthetical).
  Footnote citation-lead names \emph: Helmholtz/Kronecker/Cantor (p.191), B. Russell (p.200).
- Foreign ROMAN as printed: notæ ordinales, numeri ordinarii (p.191), indifferenza della natura
  (p.199, Italian), communis universorum locus, loca primaria (p.199, Latin); French Leibniz
  quote „La considération de l'infini…" (p.193). „…"-quoted German/Danish phrases roman:
  „det Sidste og Uvæsenligste…", „Uvæsentligt", „Fremgang"/„Tilbagegang", „Styrke", „samme",
  „naturlige Steder", „fire Elementer", „absolut"/„absolute".
- Italic titles: Zahlen und Messen… / Ueber den Zahlbegriff (p.191 fn), Mitteilungen zur Lehre
  vom Transfiniten (p.191 fn), Nouveaux Essais (p.193 fn), Kritik der reinen Vernunft² (p.195 fn),
  The Foundations of Geometry (p.200 fn). Journals roman: Zeitschrift für Philosophie…
- Faithful quirks preserved: **"ikke blot blot"** dittography (p.191); "havt" (p.191); "voxende"/
  "voxer" (p.193/198); "antike" (p.198); "Villiens" (p.198); "Inerti" (p.199); "Ti" for thi
  (p.199); "behøver ved den ikke" (p.196, printed behøver). En-dash ranges: 65--89 style.

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
