# Sibbern, *On Cognition and Inquiry* (*Om Erkjendelse og Granskning*, 1822) — translation resume notes

State for the **English translation** of this book. Update after each batch.
The user compiles/commits/pushes — never the assistant.

Source of truth: `transcription.tex` (Danish), **COMPLETE + proofed** (§§1–22 +
Slutning + Rettelser; a full image proof pass was done on §§21–22, 2026-07-19).
Translate FROM the transcription, not from the PDF scan.

Standing method: `../../../TRANSLATION-PLAYBOOK.md`. Read it first, then this file,
then grep the markers and run the batch loop.

## Decisions (fixed with Hans, 2026-07-19)
- **Register: lightly modernized.** Faithful in meaning; untangle Sibbern's long
  periodic syntax into readable modern English; period flavor softened, not erased.
- **Key terms: glossary + bracketed original.** On a term's first use in each
  section, gloss the Danish in brackets — "cognition [Erkjendelse]" — then use the
  English alone. Maintain `GLOSSARY.md` (seeded) for cross-section consistency.
- **Layout: English-only, section-keyed.** `translation.tex` mirrors the
  transcription's structure 1:1 (title, Preface, Synopsis, §§1–22 each with a
  "Remark and Supplement" where the Danish has "Anmærkning og Tillæg", Conclusion).
  Original printed page ranges live in the `% [text to be added: pp. X--Y]` markers.

## Open decisions (resolve as they come up)
- **Title. RESOLVED 2026-07-19: "Granskning" = Inquiry** (Hans confirmed). Title
  page stays *On Cognition and Inquiry*; glossary term unchanged. Subtitle
  rendered "Toward an Introduction to Academic Study".
- **Synopsis page refs. RESOLVED 2026-07-19: drop the Danish page numbers** (Hans
  confirmed). Synopsis entries keyed to § number only; final entry → "(Conclusion.)".
- **Rettelser (errata leaf, p.205).** Corrects the *Danish* text's orthography, so
  it's meaningless in English. Currently a commented note at the end of
  `translation.tex`. Decide at finish: omit, or keep a one-line translator's note.

## Page map (from the transcription)
- Body: printed page = PDF page − 22. Front matter (roman): printed = PDF − 6.
- Section → printed start page (verified via the Oversigt):
  §1 p.3 · §2 p.18 · §3 p.24 · §4 p.29 · §5 p.36 · §6 p.48 · §7 p.55 · §8 p.72 ·
  §9 p.88 · §10 p.104 · §11 p.112 · §12 p.116 · §13 p.120 · §14 p.128 · §15 p.133 ·
  §16 p.146 · §17 p.153 · §18 p.159 · §19 p.160 · §20 p.162 · §21 p.165 · §22 p.194.
  Body ends p.204. (§§18–19 have no Remark; all other sections do.)

## CURRENT RESUME POINT
**TRANSLATION DRAFT COMPLETE.** Front matter (Preface + Synopsis) + §§1–22 +
Conclusion all filled. 0 fillable markers, 0 "translation continues" seams.
Sandbox substitute compile: **109 pp., 0 warnings, 0 errors, 382 \emph spans.**

## FINISH CHECKLIST
1. **RESOLVED** — **Rettelser (errata leaf):** kept as a one-line rendered translator's
   note at the end of translation.tex (a centred rule + \footnotesize italic note stating
   the Danish errata correct only the original's orthography and are not reproduced).
2. **RESOLVED** — **catalog.yaml:** erkjendelse section `status:` flipped to `complete`;
   note updated to "English translation complete."
3. **Remaining for Hans:** compile both PDFs locally with the REAL fonts (libertinus +
   libertinust1math + textalpha), confirm 0/0 and that the Transcription + Translation
   links resolve, then commit / push. (The published Translation pdf link resolves after
   push.) Whole-book sandbox substitute compile now: **110 pp., 0 warnings, 0 errors.**

Notes for the next batches:
- The Oversigt is a section-by-section synopsis; kept as running prose keyed to
  the same § numbers (it doubles as the book's analytical contents).
- §21's "Remark and Supplement" is the longest single span in the book
  (transcription ~lines 3435–3912, printed pp.~166–193) — subdivide with a
  `% [translation continues from p. N]` note per the playbook.
- Greek occurs in the body (e.g. αὐτὸς ἔφα, φύσις, ὠδίς near pp.186–191): copy
  glyphs verbatim, translate only the surrounding prose.

## DONE so far (don't redo)
- **batch 1 (2026-07-19)** Front matter: **Preface** (Fortale, pp. III–XII) and
  **Synopsis** (Oversigt, pp. XIII–XVI). Register lightly modernized; Sibbern's
  long periods untangled. Glossary glosses added on first use. Sandbox substitute
  compile: **15 pp., 0 warnings, 0 errors.** GLOSSARY.md extended with Tro,
  Grunde, Gransken, Tilværelsesgrunde, Forstandighed, Forstandsmæssighed,
  Middelpunct, Er- og Vedkjendelse. No \emph/Greek in these front-matter spans.
- **batch 2 (2026-07-19)** **§1** main text + Remark and Supplement (pp.3–17,
  transcription L376–662). All **27 \emph spans** and the Greek πάθος carried
  verbatim; run-in numbered heads 1./2./3. kept; Latin (Scimus qvia accepimus,
  nisus formativus, primus motor) → \textit. Register lightly modernized. Added
  glossary term Grundidee; noted "scientific culture" variant for Videnskabelighed.
  Sandbox compile (whole file so far): **22 pp., 0 warnings, 0 errors, 27 \emph.**
  FLAG carried: transcription p.10 "imøde" (Fraktur m/n) rendered by sense
  ("is met by"). Internal cross-refs kept: "See §~11, Remark~2" and "See §~7,
  in the Remark."
  Note: transcription FLAGs carried through — p.XII "sinden"→sense "inden"
  (before), rendered by sense; p.XIII "som der ude" uncertain, rendered "out
  there" by sense.
- **batch 3 (2026-07-19)** **§§2–4** main text + Remarks (pp.18–35, transcription
  L663–1011). All **28 \emph spans** carried (running total 55); run-in numbered
  heads kept; Latin (Scimus qvia facimus; Scientia et potentia in idem coincidunt;
  ponere; primus motor; actu) → \textit. Work refs kept as cited: Hegel's
  Encyklopädie §379ff; author's Psychologie §55; Franz Baader in Jahrbücher der
  Medicin vol.3 pt.1. Internal cross-refs kept (§4 Anm.3; §§19–21). Added glossary
  term Reale. Sandbox compile (whole file): **30 pp., 0 warnings, 0 errors, 55
  \emph.** FLAGs carried: p.22 "Gjenstandenr" (stray r) → "object"; p.28 printer's
  manicule before "den geniale" (no effect on English).
- **batch 4 (2026-07-19)** **§5** main text + Remark (pp.36–47, transcription
  L1015–1233). All **10 \emph spans** carried (running total 65); Danish quote
  „ethvert Vidne om menneskelig Nødtørftighed.“ → ``every witness of human
  neediness.'' Key content: cognition "by force of grounds," the highest Idea, the
  ontological proof, and the thesis that all cognition ultimately rests on
  immediate faith/grace. Ref kept: "ontological proof of God's existence."
  Sandbox compile (whole file): **36 pp., 0 warnings, 0 errors, 65 \emph.**
  No new glossary terms (Vished, Overbeviisning, Tro, Grunderkjendelse already in).
- **batch 5 (2026-07-19)** **§6** main text + Remark (pp.48–54, transcription
  L1237–1373). All **11 \emph spans** carried (running total 76); Latin
  „rationes cognoscendi“ → \textit; refs kept: Plato's Theaetetus; ontological
  proof. Content: cognizing "truth in its truth," pursuit to the highest/last
  grounds, and academic study as intellectual coming-of-age (Selvtænkning vs.
  school "learning"). Added glossary term Fuldmyndighed (coming-of-age). Sandbox
  compile (whole file): **39 pp., 0 warnings, 0 errors, 76 \emph.**
- **batch 6 (2026-07-19)** **§7** main text + 4-part Remark (pp.55–71, transcription
  L1377–1686). All **15 \emph spans** carried (running total 91); no Greek/Latin in
  this span. Content: the "intelligent" (vs. empirical) cognizing, construction
  a priori, the identity of the intelligence in mind and in nature, the "book of
  nature," and the empiricism/rationalism relation (esp. in medicine). Rendered
  Intelligenthed as "intelligence-character" (glossed); ref kept "empiricism and
  rationalism." FLAGs carried: p.59 two letterspaced questions (emphasis extent
  approximate); "Maae" (poss. "Maade") → "manner" (twice). Sandbox compile (whole
  file): **47 pp., 0 warnings, 0 errors, 91 \emph.**
- **batch 7 (2026-07-19)** **§8** main text + long Remark (pp.72–87, transcription
  L1690–1992). All **21 \emph spans** carried (running total 112). Content: shift
  from rationes cognoscendi to rationes essendi (grounds of existence), then a long
  excursus arguing mathematics gives only grounds-of-cognition (Demonstration, not
  philosophical Deduction) and is not fully "organic" science; ends at the highest
  absolutely-fixed point / ontological proof. Latin kept as \textit: rationes
  cognoscendi/essendi, causa in facto posita, crux mathematicorum. Refs kept:
  Ørsted's genetic geometry; Hegel's Logik vol.1 Remark p.206. Preserved the
  square-bracketed authorial aside [Mathematics as a whole…organic.] and the
  DUPLICATED point-number "3." (Danish prints "3." twice — FLAG p.85, kept verbatim).
  Sandbox compile (whole file): **55 pp., 0 warnings, 0 errors, 112 \emph.**
- **batch 8 (2026-07-19)** **§9** main text + 4-part Remark (pp.88–103, transcription
  L1996–2239). All **17 \emph spans** carried (running total 129); Greek νοῦς,
  εἰς τοὺς λόγους, αἴτιον copied verbatim (Plato, Phaedo 97c/99e/99b; refs kept).
  Content: things' grounds sought in their concepts (Realbegreber); the heat/cold,
  poison/death, north-wind/frost examples; the "tautology" worry answered; ends
  pointing to the need for something "quite other than the whole chain" (→ §10).
  Latin kept: sensu eminenti, ratio essendi. FLAG: p.~[§9.4] "men kun nok" reads
  elliptically in the Danish — rendered "but is only just so much" by sense; verify.
  Sandbox compile (whole file): **61 pp., 0 warnings, 0 errors, 129 \emph.**
- **batch 9 (2026-07-19)** **§10** (pp.104–111, L2243–2388, emphasis-dense: 41 emph)
  **+ §11** (pp.112–115, L2392–2467, 4 emph). Running total **174 \emph**, all
  carried. Content: the "Third"/active First that both determines and makes actual;
  the shift from "Why" to "By-which"; God as loving highest Personality positing a
  kingdom of love/freedom (Son-of-God aside kept); the Idea defined; cognition itself
  as "the Idea's life and self-presentation in consciousness"; truth as what livingly
  produces the agreement. Latin kept: rationes essendi, ratio essendi. Refs kept:
  §4 Anm.3, §1 Anm.3, §7 Anm., author's Psychologie §58 p.212. FLAG carried: p.111
  "iog med Hensyn" (broken ligature) → "and with respect to". Sandbox compile (whole
  file): **67 pp., 0 warnings, 0 errors, 174 \emph.**
- **batch 10 (2026-07-19)** **§12** (pp.116–119, L2471–2543, 10 emph) **+ §13**
  (pp.120–127, L2547–2695, 15 emph). Running total **199 \emph**, all carried. Content:
  science as the Idea's self-presentation, the inseparability of Idea/System/Detail;
  §13 on the Idea as spirit of a science ("not in standing results but in what makes
  results come forth"), the speculative vs. the immediately "judicious," and the
  concept↔Idea distinction. No Greek/Latin in these sections. Also updated
  **catalog.yaml** (erkjendelse: transcription complete, translation in progress,
  added Translation pdf link — resolves once Hans compiles/pushes). Sandbox compile
  (whole file): **73 pp., 0 warnings, 0 errors, 199 \emph.**
- **batch 11 (2026-07-19)** **§14** main text + 3-part Remark (pp.128–132, L2699–2786).
  All **14 \emph spans** carried (running total 213). Content: the dialectic as both
  "philosophical art of annihilation" (not mere skepticism) and art of construction;
  logical↔metaphysical identity; the three negative targets (modes of representation,
  objects, the concepts themselves a priori). NOTE: `eo ipso` is letterspaced in the
  Danish (\emph), so kept as \emph{eo ipso} (renders italic + preserves emphasis),
  not \textit. Refs kept: author's Psychologie §5; Plato's Parmenides p.129. Sandbox
  compile (whole file): **75 pp., 0 warnings, 0 errors, 213 \emph.**
- **batch 12 (2026-07-19)** **§15** main text + 6-part Remark (pp.133–145, L2790–3024).
  All **37 \emph spans** carried (running total 250). Content: cognition as
  system-of-concepts; plurality of Ideas/sciences (relative absoluteness); the two
  dangers — "nebulism" (Goethe's word, rendered "nebulism") and "crystallization" —
  plus one-sidedness; the need for the free judicious to both precede and follow the
  system; "possibility of several methods/systems"; history as "historical composition."
  No Greek/Latin. Refs kept: §6 Anm.2. Sandbox compile (whole file): **82 pp., 0
  warnings, 0 errors, 250 \emph.**
- **batch 13–15 (2026-07-19, continuous)** **§16** (pp.146–152, 22 emph: Detail +
  spirit-of-observation, Dutch-painter/light example, crystallography, ethics),
  **§17** (pp.153–158, 11 emph: method, analytic vs. synthetic, study of a science's
  history), **§§18–20** (pp.159–164, 4+8+14 emph: Idea's outer existence & the
  "element of genius"; the Idea calling forth its opposite / self-thinking; doubt,
  double negation, possibility of error). Running total **309 \emph**, all carried.
  §18/§19 inline "\emph{Anm.}" notes folded into the main-text fills (rendered
  "\emph{Note.}"). §20 German ref kept as \textit: Baader, "über die Ekstase, zweites
  Stük, S.6" (with ref. to Hegel); §20 "a priori" letterspaced → kept as \emph{a
  priori}. Refs kept: author's Psychologie §22 (§18) & §16 Anm.1. Sandbox compile
  (whole file): **91 pp., 0 warnings, 0 errors, 309 \emph.**
- **batch 16 (2026-07-19)** **§21** main + 4-part Remark (pp.165–193, L3391–3911),
  the book's longest section. All **55 \emph** carried (10 main + 45 Remark; running
  total **364**), incl. two line-spanning spans. Greek verbatim: ἐστιν ἐφ' ἡμῖν /
  τὰ οὐκ ἐφ' ἡμῖν (Epictetus p.167), ὠδίς (Plato 2nd Letter p.186), φύσις (p.190),
  αὐτὸς ἔφα (p.191). German kept in ``…'': Schiller "Du mußt hoffen…", Fichte "über
  das Wesen des Gelehrten", Schiller "die Ideale und das Leben"; Baader title +
  in suspenso → \textit; Latin periculum vitæ letterspaced → \emph. Refs: Phil 2:13,
  3:14; Bacon. Content: the "trial by fire," theology student, egoism/party-spirit,
  Indifferentism vs. Intolerance vs. Tolerance, "the way to truth goes through error."
  FLAGs by sense: p.171 Fordølgelse→"concealment"; p.179 "Snigmord, Saul begik"→"the
  assassination that Saul committed." Sandbox compile: **104 pp., 0/0, 364 \emph.**
- **batch 17 (2026-07-19)** **§22** main + 4-part Remark (pp.194–204, L3915–4072, 17 emph)
  **+ Slutning/Conclusion** (L4076–4102, 1 emph). Running total **382 \emph** — DRAFT
  COMPLETE. Content: the Idea realized through outward practice in a human community;
  choosing one's vocation (inclination for the *field* vs. for the *science*; village-
  priest/physician examples); "take the science into life"; the peril of serving two
  masters. Conclusion = 1 Cor. 13 (love above all knowledge/prophecy) → ends "Blessed
  are they who are poor in spirit." Kept verbatim: Fichte quote (``let his particular
  science be given him by science''), "Gestaltung", Steffens ref, Matt 6:33 & 5:3.
  FLAG carried: p.203 "havde al Prophetie"/"Blik at skue" (per §§21–22 image proof).
  Sandbox compile (whole book): **109 pp., 0 warnings, 0 errors, 382 \emph.**

## Conventions
See `../../../TRANSLATION-PLAYBOOK.md` for the standing method and the LaTeX
conventions (quotes, emphasis, Latin → \textit, Greek verbatim, em-dash, run-in
numbered heads, sandbox compile recipe). Book-specific vocabulary: `GLOSSARY.md`.
Book-specific note: the Danish uses centered heads (`\begin{center}\large\S.~N.`),
not `\section{}`/`\label{}`, so match markers by the § number + page range.
