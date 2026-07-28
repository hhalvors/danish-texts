# Høffding — *Den menneskelige Tanke, dens Former og dens Opgaver* (1910): TRANSLATION resume notes

**This is the translation job.** The transcription is finished; do not re-transcribe.
Read the standing method first: `../../../TRANSLATION-PLAYBOOK.md`. This file holds
only the book-specific state and decisions.

- **Source of truth:** `transcription.tex` (Danish), **COMPLETE** — 392 printed pp.,
  compiles 0 errors / 0 missing-char. Translate FROM it, not from `scan.pdf`.
- **Target:** `translation.tex` (English) — already **scaffolded**: English preamble,
  every heading translated and in place, a `% [text to be added: …]` marker under each.
  53 markers. The skeleton compiles (sandbox: 14 pp., 0 errors).
- **Page-offset (scan only):** PDF = printed + 15. You won't normally need the scan;
  match Danish by heading/`\label`, not by page.
- **English title chosen:** *Human Thought: Its Forms and Its Tasks.*
- **The user commits and pushes. You never do.**

---

## STATUS: TRANSLATION COMPLETE ✅ (Foreword through §162, all 53 markers filled)
Every `text to be added` marker is gone (a lone grep match on line 11 is just the playbook-note
comment, not a marker); 0 seams open. Final sandbox compile (lmodern substitute): **311 pp,
0 errors, 0 char-warnings**. `catalog.yaml` menneskelige-tanke status set to **complete**.

Structure of the final stretch, for reference: C. Vurdering = section intro §§145–146; a. Det
etiske Problem = α. Ethical Work §§147–150 + β. Real Ethics §§151–154; b. Det religiøse Problem =
intro §§155–156 + α. Psychological Place of Religion §§157–160 + β. Historical & Philosophical
Consideration §§161–162. (β. Real Ethics subsubsection heading was added — skeleton had lacked it;
the b-subsubsection headings α/β were already present.)

## REMAINING FOR HANS (per playbook §6):
1. Compile BOTH PDFs locally with the REAL fonts (libertinus + libertinust1math + textalpha) — the
   sandbox uses lmodern + [Gr] placeholders only for the error/character check; the real Greek
   (φρόνησις, γαλήνη, πρὸς οἷσπερ θεὸς ὢν θεῖος ἐστιν, etc.) needs textalpha to render.
2. Confirm the Transcription + Translation links resolve on the site.
3. Commit & push (Hans does this — never the assistant).

## FINISHING (per playbook §6) — when 0 real markers + 0 seams:
1. Final sandbox compile → confirm 0/0.
2. In `catalog.yaml`, set the menneskelige-tanke `status:` to `complete` (currently in-progress).
3. Tell Hans to compile BOTH PDFs locally with the real fonts (libertinus + libertinust1math +
   textalpha) and confirm the Transcription + Translation links resolve. He commits/pushes — I never do.

Term notes: Samfoldighed=``samfoldighed'' (Ørsted). Verdensanskuelse="world-view";
Verdensbillede="world-picture"; Urfænomen="primal phenomenon" (Goethe's Urphänomen kept in
German only inside direct German quotes); Aand/Materie="spirit"/"matter"; kritisk
Monisme="critical monism"; Bestaaen="subsistence".

**NB — DUPLICATE PARAGRAPH NUMBER:** the source numbers TWO consecutive paragraphs "100."
(end of D/c Development, and the opening of E. Ideal Categories); §101 follows correctly.
Reproduced faithfully (two §100s). Likely a 1910 print/transcription slip — FLAG for Hans:
may want to renumber to 100/101/102… downstream, or leave as the original has it.

**PREAMBLE NOTE:** added `\usepackage{amssymb}` (for `\gtrless` in §59's Poincaré note).
It loads after libertinust1math; harmless. Sandbox compile still 0/0.

Recommended batch size: ~10 printed pp. Several markers already span ~10–20 pp.
(e.g. A. Psychic Energy 1–37; β. Succession and Causality 278–296; a. Forms and
Principles 254–274) — sub-chunk those and drop a `% [translation continues from p. N]`
note at the seam, per playbook §1.3.

---

## How the skeleton is laid out (read before filling)
- Markers sit **under** each heading and cover the Danish prose from that heading to
  the **next** heading. So: take a marker → open `transcription.tex` → find the same
  heading text / `\label` → read to the next heading → translate → replace the marker.
- **Empty-span markers (just delete them when you reach them):** a few section heads
  have no intro text before their first sub-heading. These are flagged in-file with
  "section intro, if any" / "subsection intro, if any":
  `B. Intuition…` (p.37), `C. Judging` (p.71), `A. Cognition` (p.254),
  `B. World-View` (p.306), `a. The Ethical Problem` (p.350). Check the Danish: if the
  heading is immediately followed by its sub-heading, there's nothing to translate —
  delete that marker. The other "intro" markers (C. Formal Categories 175–177;
  b. Quality-Relations 181–187; D. Real Categories 207–208; E. Ideal Categories
  237–242; C. Valuation 347–350; b. The Religious Problem 369–374) **do** have intro
  prose — fill them.
- Page numbers in the markers are **best-fit estimates** (interpolated from known
  section starts; the religious-chapter ones were checked during transcription and
  are exact). They're size hints only — trust the heading match, not the number.

---

## Conventions (book-specific; general rules are in the PLAYBOOK)
- **Quotes.** Danish „…" → English ``…''. The book uses „…" throughout (no guillemets).
- **Emphasis = the original's letterspacing.** The transcription already encodes every
  one as `\emph{}` — carry them ALL over as `\emph{}`. These are overwhelmingly
  **actively-cited author names** (Locke, Hume, Kant, Fichte, Platon, Plotinos, Frazer,
  Kierkegaard, Martensen, Hubert et Mauss, Wundt, Wilamowitz-Moellendorff, …) plus the
  occasional emphasized common word (e.g. `\emph{sit}`, `\emph{medens}`). A given name
  is `\emph{}` only on its first/active mention and roman thereafter — the transcription
  already reflects this, so just mirror it.
- **Greek** — copy glyphs verbatim, translate only the surrounding Danish. Needs
  `textalpha` (already in the preamble). Greek appears e.g. p.365 (γαλήνη, φρόνησις),
  p.386 `(πρὸς οἷσπερ θεὸς ὢν θεῖος ἐστιν)`. Don't transliterate; Høffding prints the
  glyphs.
- **Latin / French / German phrases stay in the source language**, set ROMAN exactly as
  the print/transcription has them — do NOT italicize (the book keeps them roman):
  e.g. *asylum ignorantiæ*, *caritas sapientis*, *animus sedatus*, *(affected)*,
  *plus ultra*, the long French Hubert-et-Mauss quote (p.390 fn), the German Pindar
  tag (p.391 fn). Translate the Danish around them. (This differs from the playbook's
  default of italicizing Latin — **follow the transcription**, which sets them roman.)
- **Work titles** in footnotes are italic (`\emph{}`): keep them, and keep them in
  their original language (do not translate *Natural History of Religion*,
  *Essai sur la nature et la fonction du sacrifice*, *Danske Filosofer*,
  *Mythus und Religion*, *Religionsfilosofi*, etc.). Journal names roman.
- **`\S` ranges, numeric cross-refs.** The book cites itself by running paragraph
  number, e.g. "(155)", "(143--146)", "(101, 1 a)", "(108; 115)", and uses `\S\ 26--31`
  in footnotes. These are the AUTHOR's references — copy verbatim, do not convert to
  `\ref`. The numbered paragraphs in the body (e.g. "155.", "156.") are likewise the
  author's — keep them.
- **Inline numbered points.** In §161 the argument runs "1) … 2) … 3) …" as paragraph
  openers (not a LaTeX list). Keep them as literal "1)" "2)" "3)" paragraph starts.
- **Em-dash** `---`; numeric/section ranges `--`; `\S\ ` for §.
- **Orthography is moot for the target** — the Danish 1910 spelling (aa, capitalized
  nouns, x-spellings, "Ti" for thi, etc.) just needs *understanding*, not reproducing;
  you're writing modern English.
- **Register.** Scholarly, moderately literal but readable. Høffding's key terms recur;
  keep them consistent across the whole book (see glossary below).

### Running glossary (pick one English term and keep it everywhere)
| Danish | suggested English | note |
|---|---|---|
| Anskuelse / Anskuen | intuition / intuiting | Høffding's "Anschauung"; "perception" also defensible — pick one |
| Forestilling | representation / idea | |
| Erkendelse | cognition | (knowledge in some contexts) |
| Vurdering | valuation | (evaluation) |
| Verdensanskuelse | world-view | |
| Aand | spirit (or mind) | "Aand og Materie" → Spirit and Matter; be consistent |
| Bestaaen | subsistence / persistence | "Bestaaen og Udvikling" |
| Villie | will | |
| Emne | object / subject-matter | "Former og Emner" → Forms and Objects |
| Sjæleliv | mental life | DECIDED (keeps Aand=spirit distinct) |
| Eftertanke | reflection | DECIDED. Høffding's central term. In §2 he etymologizes it ("seeks after"/"comes after"); gloss the literal "after-thought" there only, render "reflection" everywhere else. |
| det uvilkaarlige (Sjæleliv) | the involuntary (mental life) | "uvilkaarlig"=involuntary; reserve "spontaneous" for Høffding's own "spontan/Spontaneitet" |
| Oplevelse | experience | (Erlebnis); "tænke paa"=think of, "tænke over"=think over/reflect on |
| Kraft | force / energy | "psykisk Energi" = psychic energy |

### Heading glosses — PROVISIONAL, verify on first use
These are baked into the skeleton; revisit and adjust if you settle on different terms.
The deeper-question ones:
- B. *Anskuen, Association og Sammenligning* → "Intuition, Association, and Comparison"
  (Anskuen is the verbal noun "intuiting"; "Intuition" reads better as a heading).
- c. *Erindrings- og Fantasianskuelse* → "Memory- and Imagination-Intuition"
  (lit. "intuition in memory and in fantasy/imagination").
- d. *Forestillingsassociation* → "Association of Ideas" (lit. "association of
  representations").
- C. *Dømmen* → "Judging" (the act; "Judgment" also fine).
- A. *Erkendelse* → "Cognition".
- b. *Former og Emner* → "Forms and Objects".
- B. *Verdensanskuelse* → "World-View".
- c. *Aand og Materie* → "Spirit and Matter" (or "Mind and Matter").
- d. *Bestaaen og Udvikling* → "Subsistence and Development".
- The IV.C subsubsection titles keep the original's `\emph{}` on the title clause and the
  parenthetical roman, e.g. `α. \emph{Ethical Work}. (Formal Ethics)` — mirrors the Danish.

---

## DONE so far (don't redo)
- Skeleton `translation.tex` created and compiling (0 errors, 53 markers).
- **Foreword (Forord, August 1910)** — translated. Signature kept as
  `\emph{Harald Høffding.}` with `\bigskip`/`\hfill`.
- **Ch. I structural fix**: added `\markboth{...}` and the `\begin{center}---\end{center}`
  section-rule between the chapter heading and `A. Psychic Energy` to mirror the Danish
  (skeleton had omitted both).
- **A. Psychic Energy §§1–5** (pp. 1–~20) — translated; seam advanced.
- **A. Psychic Energy §§6–8** (pp. ~20–30) — translated; seam advanced.
- **B. Intuition… section-intro marker** (empty span) — deleted (B heading → a. Sansning
  directly in the Danish).
- **B/a. Sensation §§11–13** (pp. 37–47) — translated.
- **B/b. Recognition §§14–16** (pp. 47–52); **B/c. Memory- & Imagination-Intuition
  §§17–18** (pp. 52–59); **B/d. Association of Ideas §§19–20** (pp. 59–64);
  **B/e. Comparison §§21–23** (pp. 64–71) — translated. Section B complete.
  C. Judging empty-span intro marker deleted.
- **C/a. Formation of Judgment §§24–25** (pp. 71–74); **C/b. Obstacles §§26–28**
  (pp. 74–82); **C/c. Subject and Predicate §§29–35** (pp. 82–99) — translated; subsection
  c complete.
- **C/d. The Validity of Judgment §§36–39** (pp. 99–109) — translated; **CHAPTER I COMPLETE.**
  Closing `\begin{center}---\end{center}` added before Ch. II heading.
  - Term choices: *Existenskvalitet* = "existence-quality" (Høffding's coinage);
    *Existentialdom/Existensdom* = "existential judgment / existence-judgment";
    *Existensforvisning* = "existence-assurance"; *Virkelighedskriterium/-begreb* =
    "criterion/concept of reality"; *real/formal Sandhed* = "real/formal truth";
    *Vurderingsdom/Værdidom* = "valuation-/value-judgment"; *Grundværdi* = "fundamental
    value". Greek kept verbatim (πιθανή, ἀπερίστατος, διεξωδευμένη, συνδρομή). Galileo
    Danish quote translated with Italian tag "(la proprietà e condizione…)" kept roman;
    Kant "Ding an sich", Bradley "the one absorbing experience" kept. Existence-judgment
    examples keep \emph{are} ("There \emph{are} good people!").
- **Ch. IV / A. Cognition — empty intro deleted; a. Forms and Principles §§106–113**
  (pp. 254–274); **b. Forms and Objects intro §114** (pp. 274–275) — translated.
  §§106–113: the principles matching each category-group (relation, consistency, causality,
  totality-development); truth as "work-value"; the STATIC vs DYNAMIC concept of truth (truth
  = achieved connection, not correspondence); the three epistemologies **Formalism/Empiricism/
  Pragmatism** (Kant/Hobbes/Fichte/Kierkegaard/Kroman; Hume/Mill/Spencer; Mach/Avenarius/James),
  with the analytic/regressive method + "working hypothesis" as Høffding's synthesis. Kept:
  Wallenstein "Eng ist die Welt, und das Gehirn ist weit" & its reversal "Gross ist die Welt…";
  Latin (rationis prima principia vera esse facimus nosmet ipsi; frustra fit per plura…; Kant's
  favor ille unitatis…); French (Leibniz "un parfait retour", "à rebours", "suivant son point
  de vue"); German Thatsache/Thathandlung, "Ding an sich"; Greek νοῦς/ἀρχαί; "Reason does not
  beg, it commands." §114: identity as the "principle of principles" but the world an
  irreducible multiplicity ("a living world").
- **Ch. III / D/c. Development §§97–100** (pp. 227–237) — Section D complete. *Udvikling* =
  "development"; direction→development; Maimon on cause=continuity; Aristotle's possibility/
  actuality (κίνησις, ἐνεργείᾳ kept); preformation vs epigenesis (Wolff; Leibniz "développement
  [an unwinding]"); Rousseau; the 3-stage schema (concentration→differentiation→"higher unity")
  as a regularly varying difference-series; development a NEUTRAL concept (contra Hegel/Spencer,
  *eo ipso* valuable); Rickert (Ziel/Genesis/Orthogenesis) rebutted.
- **Ch. III / E. Ideal Categories intro §§100–101 + 1) Formal Differences + 2) Real Differences
  §102** (pp. 237–246) — **CHAPTER III COMPLETE.** Value = what satisfies an urge; value-quality
  as testable hypothesis; the fundamental value (value measured only by value); Melissus kept.
  Formal diffs: elementary/ideal, immediate/mediate (→ *Formaal*=purpose, *Norm*=norm),
  potential/actual values. Real diffs: content (biological vs intellectual/aesthetic/ethical →
  religious) and extent (individual/social/cosmic). "to be or not to be" kept.
- **Ch. IV / Introduction §§103–105** (pp. 246–254) — translated. Problem = form of psychic
  energy (Avenarius's "natural history of problems", homesickness); the three philosophical
  problems from the Form–Object–Interest triad: **problem of cognition** (form/object),
  **problem of existence** (metaphysical/cosmological), **problem of valuation** (ethical +
  religious; aesthetic as analogue); their division of labor & mutual analogy; psychology as
  the historical introduction. *amor intellectualis* roman; "man is understood by the world…".
- **Ch. III / D/b. Totality §§93–96** (pp. 218–227) — translated. Direction as bridge from
  causality to totality (Leibniz's conservation of direction; resultant); totalities = systems
  of directions (solar systems, organisms, personalities, societies); against chaos-as-origin
  (Hesiod) and against teleology-vs-mechanism (both externalize whole/parts); intensity vs
  extensity (Pascal's "thinking reed"); Aristotle on the individual as barrier; the
  natural-science/history (Rickert) opposition as only degree — "biography of existence";
  *das Einmalige*; whole/part relativity (Ardigò's *indistinto/distinti*; Kant's world as an
  "Idea"; no absolute atoms, Huygens/Leibniz). Terms: *Totalitet* = "totality"; *Retning* =
  "direction"; *Samfoldighed* (Ørsted's coinage) = ``samfoldighed'' (glossed "con-foldedness",
  = "interplay of laws"). Latin *compages mirabilis* roman; Italian/German kept.
- **Ch. III / D/a. Causality §§88–92** (pp. 208–218) — translated. Causality vs formal
  categories (existence-quality, criterion of reality); cause first practical (means→goal,
  "first encounter with necessity"); the whole-series cause (Plato's cave-image, Republic
  bk. 7; Hannibal/primal nebula; Zeuthen/Heiberg Archimedes); cause/effect continuity, the
  "leap" as ours not nature's; the equivalence question & conservation of energy (Mayer's
  *causa æquat effectum*, Colding, Joule, Helmholtz); law = antecedent→consequent, cause as
  aggregate of conditions; *Kraft*=force (Leibniz's def.; Mach vs Hertz; Hugo de Vries's
  pre-mutation "sich völlig im latenten Zustande abspielt"); substance as a "dying category"
  (Hume, Fichte). **NB math notation:** kept verbatim per source — `$B = A + \times$` and
  `$C = B \div y$` (author's ×/÷ signs; ÷ = the old Danish minus). Etymology aside rendered
  with bracket glosses: "possibility [Mulighed] … 'fortune' [Formue]". Latin/German quotes
  kept.
- **Ch. III / D. Real Categories intro §87** (pp. 207–208) — translated. The last opposition:
  rationality (ground/consequence, eternal system) vs time (before/after, surging sea) —
  Spinoza chose the first (time → illusion), Hume the second (rationality → illusion); the
  real categories are needed for "what is distinguishable in time." Spinoza's attributes,
  Aand og Materie = "Spirit and Matter", $A=B=C=D$, "still world" kept.
- **Ch. III / C/d. Rationality §§85–86** (pp. 204–207) — translated; **Section C complete.**
  Inference from the transitive/partial-identity series ($A\to B\to C$ ⊢ $A\to C$); estimate/
  intuition vs grounding; inference as pure form (not a metaphysical law, contra Aristotle/
  Leibniz); conclusion as one-sided equivalent losing middle-terms (Herbart's "zufällige
  Ansichten"); Lessing (seeking > finding); "thought-worlds"/logical systems. Rationality
  schema formulas kept verbatim.
- **Ch. III / C/b/3) Degree §§79–80** (pp. 194–197); **C/b/4) Place §§81–82** (pp. 197–202);
  **C/c. Negation §§83–84** (pp. 202–204) — translated.
  - Degree: quality vs intensity not original (analogy w/ number-series & measurable space);
    Kant on intensive magnitudes; *det bestemte Antals Lov* = "the law of definite number"
    (Renouvier, Dühring). Place: Berkeley on space-analogy; *naturlige Steder* = "natural
    places"; Renaissance purging (*indifferenza della natura* kept Italian); relativity of
    place (Copernicus *communis universorum locus*, Kepler/Bruno, Newton *loca primaria* —
    Latin roman); metric vs projective/descriptive geometry; Euclidean vs non-Euclidean
    (Russell *Foundations of Geometry*); *Udenforværen* = "being-outside-one-another";
    Kant *Metaphysische Anfangsgründe* (space as Idea). Negation: Spinoza *omnis determinatio
    est negatio* (Ep. 50) roman; Herbart on "No"; Plato Greek ὄντος πρὸς ὂν ἀντίθεσις kept
    (Sophist 257 E); Hegel confusing negation w/ opposition. *A (non B)*, *A (non-B)* kept.
- **Ch. III / C/b/2) Number §78** (pp. 190–194) — translated. Number from repeated identical
  acts of thought (number-quality → serial number → amount); Helmholtz/Kronecker (ordinal
  start) vs Cantor (sets; "notæ ordinales" not "numeri ordinarii"); repetition's positive
  role separating math from logic ($A+A=A$/Boole $x^2=x$ logically, but $A+A=2A$
  mathematically); positive/negative/imaginary numbers, infinity (Leibniz "La considération
  de l'infini vient de celle de la similitude…"). **NB math notation:** the source uses "÷"
  as the old Danish MINUS sign — `$100 \div 92$` means 100−92 = 8; reproduced verbatim per
  transcription. Latin (notæ ordinales, numeri ordinarii) roman; German/French titles &
  quote kept.
- **Ch. III / C/b/1) Time §§76–77** (pp. 187–190) — translated. Time = sensation of change,
  the 3-/4-membered rhythm (now / interval / attainment; + fore-time), the purging to "pure
  succession" and "a pure form of intuition"; mechanics defines only equality of times;
  Aristotle (heavenly bodies), Newton's "true, absolute, mathematical, equably flowing time,"
  Plotinus (world-soul's unrest δύναμις οὐχ ἥσυχος), Augustine (time & creation). Terms:
  *Forandringsfornemmelse* = "sensation of change"; *Udrensning* = "purging"; *ren
  Succession* = "pure succession"; *Anskuelsesform* = "form of intuition"; *Førnutid* =
  "time-before-the-now". Greek kept; Ennead/Confessiones cited; poetic quote "the still world
  at our feet in eternal evening light."
- **Ch. III / C/b. Quality-Relations intro §§74–75** (pp. 181–187) — translated. §74
  quality-relations & the four rationalizing qualities (time/number/degree/place); §75 a
  long treatment of **Analogy** across domains (against Aristotle/Kant excluding it; Leibniz
  on idealist metaphysics; Kant's Analogies of Experience = cause as ground→consequence
  analogy; Maxwell "By physical analogy…" from *On Faraday's Lines of Force*; Cournot;
  optics undulation/emission; Young, Faraday, Merz; Luther/Zwingli "it is"/"it means";
  Arrhenius vs Ostwald/Mach/Ramsay on atoms). Terms: *Kvalitetsforhold* = "quality-relations";
  *Forholdslighed* = "relational likeness"; *Hudrespiration* = "skin-respiration"; *Tracheer*
  = "tracheae". Work titles kept in cited language; Maxwell/Cournot quotes rendered from the
  Danish.
- **Ch. III / C/a. Identity §73** (pp. 177–181) — translated. Identity = highest degree of
  likeness / possibility of substitution (Leibniz), against Husserl's reverse view; likeness
  itself undefinable; analytic definition (point by line…); conservation of energy &
  psychic equivalents; space/time uniformity (Telesio, Bruno, Maxwell's *Matter and Motion*
  §19). Greek παράδειγμα kept (Euthyphro); *Fajdon*→*Phaedo*, *Eutyfron*→Euthyphro; *Adam
  Homo* (Paludan-Müller) kept. **NB:** Maxwell quote — transcription drops "ikke"; rendered
  with Maxwell's correct sense ("does not depend merely… but only…"), matching Matter &
  Motion §19 (obvious source glitch).
- **Ch. III / C. Formal Categories intro §72** (pp. 175–177) — translated. Introduces the
  formal-category quartet: *Identitet* (Identity), *Kvalitetsforhold* (quality-relations:
  qualitative likeness $a_1/a_2$, qualitative difference $a/b$), *Negation* ($a$/non-$a$),
  *Rationalitet* (Rationality). *Elementer* (points of likeness/difference) = "Elements";
  "To sense is to distinguish"; "There must be relief." Rationality schema kept verbatim:
  $a \overset{\angle}{\underset{=}{\to}} b \ldots$ (needs amsmath+amssymb, both loaded).
- **Ch. III / B. Fundamental Categories §§69–71** (pp. 172–175) — translated; **Section B
  complete.** §69 absolute identity-series $A=B=C=D$ (8) + $A=A$ (Leibniz, monism);
  §70 closed/conceptually-bounded series (Naphtali Cohen; equilateral-triangle vertices,
  Decemvirs); §71 the KEY transition: the triad **Form—Object—Interest** yields the three
  special-category groups — *formale/reale/ideale Kategorier* = "formal/real/ideal
  categories" (time → real; value → ideal). Latin roman (in quibus substitutio aliquando
  non succedit; Non inelegans specimen…). *Norbagger* rendered "Norwegian pony";
  Decemvirer = "Decemvirs"; "equal before the law". Formula (8) verbatim.
- **Ch. III / B. Fundamental Categories §§62–68** (pp. 164–172) — translated; seam at §69.
  The seven difference-series types, each with a numbered display equation (1)–(7) using
  `\underset{...}{\wedge}`, `<`, `\to`, `\smile` (needs amsmath — added). Terms:
  *kaotisk/ubestemt varierende/regelmæssigt varierende/identisk varierende/fremskridende
  Forskelsrække* = "chaotic / indefinitely varying / regularly varying / identically
  varying / progressive difference-series"; *partiel Identitetsrække* = "partial
  identity-series"; *Gensidighedsrække* = "reciprocity-series"; *absolute Korrelatrækker*
  = "absolute correlate-series"; *inkonvertibel/intransitiv/asymmetrisk*. Latin roman
  (experientia vaga, docta ignorantia, ratio). Herbart "Realer" = "reals"; Hobbes tag
  "war of all against all". Formulas reproduced verbatim from transcription.
- **Ch. III / B. Fundamental Categories §§58–61** (pp. 154–164) — translated; seam at §62.
  Two first categories = *Synthesis* and *Relation* (relational determinacy); then
  *Continuity/Discontinuity*; then the likeness/difference basis and series-types.
  Terms: *transitiv/konvertibel/symmetrisk/intransitiv/omvendt symmetrisk Række* =
  "transitive/convertible/symmetric/intransitive/inversely symmetric series";
  *Aktualitetsprincip* = "principle of actuality"; *rationelt/empirisk Kontinuum* =
  "rational/empirical continuum"; *Sammenfatnings-/Sammenligningsdom* = "combination-/
  comparison-judgment"; *Benævningsdom* = "naming-judgment". Math kept ($A=B$, $A \gtrless C$;
  series ABCD). James's English footnote kept verbatim ("skipping" — OCR "shipping"
  corrected, obvious glitch in an English quotation). Poincaré *La Science et l'Hypothèse*,
  Lipps *Grundzüge der Logik*, de Morgan kept.
- **Ch. III / A. History & Method §§54–57** (pp. 145–154) — translated; Section A complete.
  - Kant's category scheme reproduced as a `tabular` (Synthesis/Continuity → Magnitude |
    Causality); Hegel's system as a `quote` block (Being/Essence/Concept). Terms:
    *Domsfunktion* = "judgment-function"; *Anskuelsesform* = "form of intuition";
    *Forholdsbestemthed* = "relational determinacy"; *Kriticisme/Pragmatisme* = "Criticism/
    Pragmatism". Greek κατηγορίαι τοῦ ὄντος kept; Latin *generatio æquivoca* roman (qv→qu).
    Foreign quotations kept verbatim & roman: Goethe "Ist nicht der Kern der Natur Menschen
    im Herzen?"; Hamilton "to think is to condition"; Comte "tout se réduit toujours à lier",
    "(généralité décroissante — complication croissante)"; Renouvier's 9-term French list;
    Hartmann "Urkategorie"; Bradley "(experience entire)". German work titles (Phänomenologie
    des Geistes, System der Logik, Reflexionen) untranslated. Kant's Danish-rendered quotes
    translated to English.
- **Ch. III / A. History & Method of Doctrine of Categories §§51–53** (pp. 135–145) —
  translated; Ch. III markboth + opening center rule added.
  - Terms: *Kategori/Kategorilære* = "category / doctrine of categories"; *Grundprædikat/
    Grundbegreb* = "fundamental predicate/concept"; *Passerben* = "leg of the compass"
    (Tankens Passerben image); *Psykologisme* = "psychologism"; *deskriptiv Erkendelsesteori*
    = "descriptive epistemology"; *Forholdsbestemthed* = "relational determinacy";
    Aristotle's 9 categories: Quantity, Quality, Relation, Acting, Being-acted-upon, Place,
    Time, Condition, Having. Greek kept (οὐσία, τὸ ὑποκείμενον, ἄτομον καὶ ἓν ἀριθμῷ, ἀρχαί,
    πρός τι, συμπλοκή). Latin roman (spatium absolutum / sensorium dei, decem prædicamenta,
    subjectum). German „unzergliedert"/„zergliedert" (Stumpf), „Ding an sich" kept. Plato
    dialogue titles → English (Theaetetus, Sophist); other work titles untranslated.
    Plotinos→Plotinus, Augustinus→Augustine.
- **Ch. II / B. Ancient and Modern Thinking §§46–50** (pp. 123–135) — translated; **CHAPTER II
  COMPLETE.**
  - §§49–50 terms: *Subsumtionsproces* = "process of subsumption"; *Identitetslogik* =
    "identity-logic"; *Loverkendelse* = "cognition of law"; *Kraft/Kraftbegreb* = "force/
    concept of force". Greek δύναμις kept. Latin roman (latens processus — per minima; salva
    veritate; qualitates occultæ; the Leibniz fragment "Vis activa nihil aliud dicit…").
    French roman (Leibniz "La loi du changement fait l'individualité…", Lettre à Basnage).
    „Fajdon" → ``Phaedo''; „Lighedens Ide" = "Idea of Likeness". Bergson *L'évolution
    créatrice* kept.
- **Ch. II / B. Ancient and Modern Thinking §§46–48** (pp. 123–131) — translated; seam at §49.
  - Terms: *formal/real Viden* = "formal/real knowledge"; *det Værende* = "Being / what is";
    „Dødeliges Meninger" = "opinions of mortals"; *sublunarisk* = "sublunary";
    Statik/Morfologi/Dynamik = "statics/morphology/dynamics"; Apoteoser/Inkarnationer =
    "apotheoses/incarnations". Greek kept (λόγος, τὰ αἰσθητά, μόνοις ἑπόμενοι τοῖς νοητοῖς).
    Tyge Brahe → "Tycho Brahe"; Galileo's Italian "(nobilissima e ammirabile)" roman.
- **Ch. II / A. Animism… §§40–45** (pp. 109–123) — translated; Section A complete
  (Ch. II markboth + opening center rule added).
  - §§44–45 additions: Greek kept verbatim (ὁ μὲν γὰρ συνοπτικὸς διαλεκτικός…; Republic
    536 C); *Idelære* = "doctrine of Ideas"; *det Godes Ide* = "the Idea of the Good";
    „Fajdros" → ``Phaedrus''; „Delagtighed" = "participation"; *Skinforklaring* =
    "pseudo-explanation"; *Livskraft/Tyngdekraft* = "life-force/force of gravity";
    *Synopsi* = "synopsis". Latin *vera causa* roman; work titles (Plato's Ideenlehre,
    Plato's doctrine of Ideas) untranslated.
  - Term choices: *Tydning* = "interpretation"; *Animisme/Platonisme/Positivisme* =
    "Animism/Platonism/Positivism"; Comte's stages *teologisk/metafysisk/positiv* =
    "theological/metaphysical/positive"; *Øjebliksguder* = "momentary gods";
    *Polyteisme/Monoteisme* = "polytheism/monotheism". Hegel's „ophævet" rendered
    ``sublated''; „højere Enhed" = "higher unity"; "Aand"(Geist) = "Spirit". Latin
    *asylum ignorantiæ* roman; French "la loi du changement (Leibniz)" roman; German work
    titles (Phänomenologie des Geistes) untranslated. Frazer *The Golden Bough*, *Adonis
    — Attis — Osiris* kept.
  - §§33–35 additions: Goethe "Italienische Reise" quote kept German; Galileo "to swing
    is to fall"; Leibniz $A = A + B$, $A < B$ kept as math; Greek ὑποκείμενον kept; Latin
    (continens/contentum, tertium comparationis, terminus a quo/ad quem) roman. Danish
    logic-terminology coinages kept in quotes WITH bracket glosses (the point is the
    terminology itself): Eilschow ``Hoved-Sag'' (principal matter)/``Bi-Sag'' (subordinate
    matter); Jens Kraft ``Sag'' (thing)/``Tillæg'' (addition); Højsgaard ``Hoved-Ord''
    (head-word); Højsgaard's verb-quotation translated to English (archaic flavor).
  - Term choices: *Domsdannelse* = "formation of judgment"; *Begrebsdannelse* =
    "concept-formation"; *Almenbegreb* = "general concept"; *konkret/typisk
    Individualbegreb* = "concrete/typical individual-concept"; *Prædikatsdom* =
    "predicate-judgment"; *Udgangsforestilling/Slutforestilling* = "initial/final
    representation" (= terminus a quo / ad quem); *Bestemmelses-/Afgørelsesspørgsmaal* =
    "determination-/decision-question"; *Udfyldnings-/Frigørelsesproblemer* =
    "completion-/liberation-problems"; *Attribut* = "attribute"; *upersonlige/subjektløse
    Sætninger* = "impersonal/subjectless sentences".
  - Kept verbatim/roman: Latin (terminus a quo/ad quem — spelling standardized from
    qvo/qvem; Felix qui potuit…; Ethica II. Ax. 5); German quotations (Kant's "Alle
    Begriffe der Negation sind abgeleitet"; Husserl's "Ich halte es mit ihm…"; Wortsinn/
    Sinn); French (Port-Royal "L'unique et véritable règle…" with \emph{regarder par le
    sens}, and "ɔ:" → "[i.e. le prédicat]"); logic letters A/B, $A_x$/$B_x$.
  - Quotations translated to English: Shakespeare given in the ORIGINAL wording (Claudio,
    Much Ado II,1; Edgar, King Lear IV,1); Cuvier (from Danish); Luther "I can do no
    other"; Biblical tags ("Great is Diana of the Ephesians!", "Thou art the man!").
    Work/poem/story titles left in cited language & quoted: ``Nissernes Vandring'',
    ``Die Erwartung'' (+ German verse kept), ``Gudsønnen''. *Nisser* = "nisses".
  - Term choices: *Genkendelse* = "recognition"; *Bekendthedskvalitet* =
    "familiarity-quality"; *Udraabsdom* = "exclamatory judgment"; *Erindrings- og
    Fantasianskuelse* = "memory- and imagination-intuition"; *artikuleret Anskuen* =
    "articulated intuiting"; *Anskuelighed* = "intuitability"; *Domsdannelse* =
    "formation of judgment"; *Forestillingsassociation* = "association of representations"
    (heading stays "Association of Ideas"); *Lighedsassociation/Berøringsassociation* =
    "association by likeness / by contiguity"; *Enshed (Dækningslighed)* = "Sameness
    (Congruence)"; *Kvalitetslighed* = "Qualitative Likeness"; *Forholdslighed (Analogi)*
    = "Relational Likeness (Analogy)"; *Dualitetens Lov* = "the Law of Duality"; *Drift*
    = "drive" (defined = urge + goal-representation; NB §8 earlier used "impulse" for
    Drift — harmonize to "drive" if desired). *Skærsild* = "purgatory (of reflection)".
  - Kept verbatim/roman: Boole's math ($x^2=x$, $x(1-x)=0$, $a_1$/$a_2$); Latin
    (cogitatio finis, imaginari hominem herum, etc.); French maxim "L'attention est la
    mère du génie"; Goethe's ``das zersplitternde Urteil'' / ``die stille Fruchtbarkeit'';
    Ribot's (logique des images); Janet's (synthèse). Quotations translated: Democritus
    fragment, Peer Gynt ("We are thoughts; you should have thought us!"), Gassendi,
    Jerusalem, Dante ("the will's first thought"). Cross-refs "(Smlgn. N)" → "(Cf. N)".
  - Term choices: *Sansning* and *Fornemmelse* both → "sensation" (English mass vs count
    noun carries Høffding's act/datum distinction naturally); *Sansefornemmelse* =
    "sense-sensation". *Sanseanskuelse* = "sense-intuition"; *Rumsanskuelse/Tidsanskuelse*
    = "space-/time-intuition"; *Sammensmeltning* = "fusion"; *Skelnen* = "a distinguishing";
    *Verdensbillede* = "world-picture" (vs Verdensanskuelse = "world-view"); *de rationelle
    Sanser* = "the rational senses". Democritus fragment & the "undifferentiated continuum"
    kept in quotes; Einar Buch work title left untranslated. "(Smlgn. 6)" → "(Cf. 6)".
- **A. Psychic Energy §§9–10** (pp. ~30–37) — translated; **section A now complete.**
  Transition sentence + closing centered rule placed before B. (51 markers, 0 seams.)
  - New terms: *Inertisætningen* = "law of inertia"; *Identitetshypotesen* = "identity
    hypothesis"; *Æter / ponderabel / imponderabel* = "ether / ponderable / imponderable";
    *Verdenssystem* = "world-system"; *Taagemasse* = "nebular mass"; *Bærer* = "bearer";
    \emph{slutte}/\emph{udlede} = "infer"/"derive". *qualitas occulta* kept roman
    (source's "qvalitas" standardized). Højsgaard (1752) quotation translated with light
    archaic flavor; his Latin "Grammatice" → "Grammatically"; Danish section title
    ``Register og Forklaringer'' left untranslated. Author cross-ref "(Smlgn. 8)" →
    "(Cf. 8)".
  - New terms this batch: *Motivforskydning* = "displacement of motive"; *betingede
    Reflexer* = "conditioned reflexes" (Pawlow→Pavlov); *Energiens Bestaaen* =
    "conservation of energy" (physics sense; elsewhere Bestaaen = subsistence);
    *Stof- og Kraftskifte* = "exchange of matter and force"; *Symptomlære* =
    "symptomatology"; *Sindssygelæge* = "psychiatrist"; *Urfænomen* = "primal
    phenomenon"; *helstøbt Karakter* = "integral character"; *Anlæg/Spor/Evne* =
    "predisposition/trace/capacity". Work titles in „…" quotes kept untranslated &
    requoted (e.g. ``Nydelsernes Fysiologi''). Transcription glitch "Hudsans?" rendered
    as "the skin-sense," (the `?` is an OCR artifact, not a real question).

### Term decisions made this batch (flag if you disagree)
- *Eftertanke* = **reflection** (literal "after-thought" glossed once in §2).
- *Sjæleliv* = **mental life**; *sjælelig Energi* = "mental energy"; *psykisk* stays
  "psychic" (psychic energy/work). *Sjælefunktion* (Kant) = "function of the soul"
  (matches Kemp Smith's Kant).
- *Aand/Aandsliv* = spirit / life of the spirit, BUT the activity-compounds rendered
  "intellectual/mental": *Aandsretning* = "intellectual orientation"; *Aandsarbejde/
  Aandsvirksomhed/aandeligt Arbejde* = "mental work/activities". (Possible point of
  contention — easy to globalize later.)
- *uvilkaarlig* = involuntary; *spontan/Spontaneitet* = spontaneous/spontaneity (kept
  distinct). *Sammenfatten* = combining; *Sammenholden* = holding-together.
- *Mangfoldighed* = multiplicity (not "manifold"). *Forestilling(en)* = representation.
  *Anskuen* = intuiting; *Skuen* = beholding; *Dømmen* = judging.
- §5 Kant: Høffding wrote „Sansningen" og „Forstanden"; I rendered ``sensation'' and
  ``understanding'' (mirrors his Danish; note Kant's own term is *sensibility*).
- §5 Stumpf list "(Emne og Eftertanke … Spontaneitet og Reflexion …)": both *Eftertanke*
  and *Reflexion* came out "reflection" (Danish near-synonyms) — deliberate.

## Sandbox compile recipe (for the translation)
Same idea as the transcription, but English babel; substitute `lmodern`, drop
`libertinust1math`/`textalpha`, and replace Greek with `[Gr]` for the check only
(never put these substitutions in the real file). Per PLAYBOOK §3:

```bash
cd /sessions/<session>/mnt/outputs && mkdir -p vtrans && cd vtrans
SRC="/sessions/<session>/mnt/danish-texts/texts/hoeffding/menneskelige-tanke/translation.tex"
sed -e 's/\\usepackage{libertinus}/\\usepackage{lmodern}/' -e '/libertinust1math/d' \
    -e '/textalpha/d' -e 's/\\usepackage\[english\]{babel}/\\usepackage{babel}/' "$SRC" > t.tex
python3 -c "import re;s=open('t.tex',encoding='utf-8').read();s=re.sub(r'[Ͱ-Ͽἀ-῿]+','[Gr]',s);open('t.tex','w',encoding='utf-8').write(s)"
pdflatex -interaction=nonstopmode -halt-on-error t.tex && pdflatex -interaction=nonstopmode -halt-on-error t.tex
# expect: 0 errors; markers left decreasing by the number you filled
```

## Finishing the book (PLAYBOOK §6)
When `grep -c "text to be added" translation.tex` and `grep -c "translation continues"`
both return 0: final sandbox compile (0/0), set this book's `status:` to `complete` in
`../../../catalog.yaml`, tell the user to compile both PDFs locally with the real fonts
and confirm the Transcription + Translation links resolve. User commits/pushes.
