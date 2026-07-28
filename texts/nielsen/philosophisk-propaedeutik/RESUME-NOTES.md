# Rasmus Nielsen — *Philosophisk Propædeutik i Grundtræk* (1857): transcription resume notes

**Phase 1 (transcription) job.** Read this, then the two standing-method files, then
continue the batch loop.

## The two standing methods
- **Transcription discipline:** follow `../grundideernes-logik/RESUME-NOTES.md`
  (Fraktur Danish → image-verified LaTeX: Sperrsatz → `\emph{}`, Danish quotes,
  footnotes, page-break comments, portable verify compile, balance checks).
- (Phase 2, later: translation via `../../../TRANSLATION-PLAYBOOK.md`.)

## This book, concretely
- **Title:** *Philosophisk Propædeutik i Grundtræk*, af R. Nielsen, Professor i
  Philosophien. Kjøbenhavn: Gyldendal (F. Hegel), Thieles Bogtrykkeri, 1857.
  Same imprint as *Philosophie og Mathematik* (its closest sibling for house style).
- **Scan:** `~/bibliotek/Nielsen, Rasmus/PPG-1857.pdf` — Google Books, **220 PDF pp.**
  (identical-title twin `Philosophisk_Propædeutik_i_Grundtræk.pdf` is the same scan).
- **Script:** **Fraktur** throughout; Latin phrases in antiqua → `\textit{}`.
  **No mathematics, no figures** — clean prose (unlike *Philosophie og Mathematik*).
- **Offset (VERIFIED): PDF = printed + 8.** printed p.4 = PDF 12, … p.8 = PDF 16,
  p.200 = PDF 208, p.204 = PDF 212. Title = PDF 9 (printed p.1); Indledning opens
  printed p.3 (PDF 11; number suppressed on the opening leaf). The Indhold lists the
  Indledning as "1–5" (loose; running text is 3–5).
- **Extent:** body printed pp. **3–204** (PDF 11–212). Back matter in the scan:
  Bacon motto (PDF 213), "Rettelser" errata (PDF 214), "Indhold" (PDF 215).
- **catalog.yaml:** id `philosophisk-propaedeutik` (added, status in-progress).

## Structure (from the Indhold, PDF 215)
- **Indledning** (pp.3–5)
- **I. Erkjendelseslære** (5–67): A. Sensualisme (7–17), B. Idealisme (18–40),
  C. Sagerkjendelse (40–67)
- **II. Videnskabslære** (68–117): A. Videnskabernes Videnskab (70–80),
  B. De særskilte Videnskaber (81–98), C. Philosophien og de særskilte Videnskaber
  (99–117)
- **III. Ideelære** (118–198): A. Ideen i dens Væsenhed (124–158),
  B. Virkeligheden mod Ideen (158–178), C. Ideens Gyldighed (178–198)
- **Slutning** (199–204)
- Fine structure: numbered paragraphs "§ 1.", "§ 2." … (rendered as centred bold
  markers; NOT listed in the Indhold, so kept out of the ToC).

## Rendering conventions (locked in, batch 1)
- Part heads ("I. Erkjendelseslære") = centred block {\large\bfseries N.} +
  {\Large\bfseries Title.} + short `\rule`, then `\phantomsection` +
  `\addcontentsline{toc}{section}{\texorpdfstring{...\quad ...}{...}}` + `\markboth`.
- A/B/C sub-heads = centred bold + `\addcontentsline{toc}{subsection}{…}`.
- "§ N." → `\begin{center}{\bfseries \S\,N.}\end{center}` (not in ToC).
- Sperrsatz → `\emph{}` (verify each page by 300-dpi zoom render — pdftoppm).
- Danish quotes „…“ as U+201E / U+201C, matching the *Philosophie og Mathematik*
  transcription (compiles clean under lmodern in the sandbox).
- Latin phrases → `\textit{}` (e.g. *omnis determinatio est negatio*,
  *scimus, quia accepimus/facimus*, *scientia et potentia in idem concidunt*).
- Page-break comments `% ---- printed p.N (PDF M) ----` at each boundary.
- Bacon motto: in the scan the leaf sits at the BACK (PDF 213); reproduced at the
  FRONT (conventional motto placement), flagged in a comment.

## ERRATA to apply (from the "Rettelser" page, PDF 214)
- p.12 l.18 fra oven: Gjenstandenes → **Gjenstandens** (APPLY in batch reaching p.12)
- p.15 l.9 fra neden: Continuitet → **Contiguitet**
- p.16 l.1 fra oven: Continuitet → **Contiguitet**
- p.42 l.14 fra neden: det vilkaarlige → **det virkelige**
- p.48 l.16 fra neden: Punkt; → **Punkt;"**
- p.48 l.15 fra neden: opløse." → **opløse**
- p.106 l.14 fra neden: Ilter → **Metalilter**

## Portable verify recipe (locked in)
```bash
cd /tmp && rm -rf vp && mkdir vp && cd vp
SRC="$(ls -d /sessions/*/mnt)/danish-texts/texts/nielsen/philosophisk-propaedeutik/transcription.tex"
sed -e 's/\\usepackage{libertinus}//' -e 's/\\usepackage{libertinust1math}//' \
    -e 's/\\usepackage{textalpha}//' \
    -e 's/\\usepackage\[danish\]{babel}/\\usepackage{babel}/' \
    -e 's/α/a/g' -e 's/β/b/g' -e 's/γ/g/g' -e 's/δ/d/g' "$SRC" > t.tex
perl -0pi -e 's/(\\documentclass\[[^\]]*\]\{book\})/$1\n\\usepackage{lmodern}/' t.tex
pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1; \
pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1
grep -o 'Output written.*' l.txt
```
Expect 0 errors / 0 undefined cs / 0 missing char. Greek α/β/γ/δ occur as list
markers (Kant/Hegel/Fichte sections) — mapped to a/b/g/d in the sandbox only; in the
real file `textalpha` renders them. Extend the map if further glyphs appear.
**Polytonic Greek** now also occurs (p.47 πρῶτον ψεῦδος; p.57 ἐπαγωγή / συλλογισμός /
ἐπιστήμη / ἀρχή ἐστι καὶ τοῦ καθόλου). The sandbox sed's α/β/γ/δ map does NOT catch
these, so the verify adds a python step stripping the whole Greek range to `[Gr]`:
`re.sub(r'[Ͱ-Ͽἀ-῿]+','[Gr]',s)` (covers U+0370–03FF and U+1F00–1FFF). In the real
file these rely on `textalpha`; confirm they render when compiling with libertinus
(textalpha's LGR/CB-Greek substitution should handle the polytonic accents).

## CURRENT RESUME POINT
**✅ TRANSCRIPTION COMPLETE — whole book done (printed pp.3–204).** The final batch (19) closed
**C. Ideens Gyldighed §36** (a/b/c: Naturen som Idee / Ideen som Natur / Naturideens Realitet) and
added the concluding **Slutning** division; the file ends with the book-end rule then
`\end{document}`. catalog.yaml status set to **complete**. Final compile: **163 pp., 0/0/0**;
`$`=182 (even); braces 904/904; guillemets 1/1; whole-file „/“ = **400/400 (perfectly balanced)** —
documented p.129 anomaly (−1) offset by the p.162–163 repeated-opening „ (+1); no dangling quotes.
Nothing left to transcribe. (Possible future polish only: proofreading pass, figure/ToC review.)

### (earlier resume note, superseded)
**~~Next: printed p.184 (PDF 192)~~** — continue **III. Ideelære / C. Ideens Gyldighed §34**.
Batch 17 ended mid-sentence at p.183 foot.

### (earlier resume note, superseded)
**~~Next: printed p.173 (PDF 181)~~** — continue **III. Ideelære / B. Virkeligheden mod Ideen §32**.
Batch 16 ended mid-quote/mid-sentence at p.172 foot.

### (earlier resume note, superseded)
**~~Next: printed p.162 (PDF 170)~~** — continue **III. Ideelære / B. Virkeligheden mod Ideen §31**.
Batch 15 ended mid-sentence at p.161 foot ("…Istedetfor at følge den mathematiske Anviisning").

### (earlier resume note, superseded)
**~~Next: printed p.151 (PDF 159)~~** — continue **III. Ideelære §29 / a) Modsigelsens Dialektik**
(inside A. Ideen i dens Væsenhed; the Plato–Hegel comparison). Batch 14 ended mid-word at p.150
foot ("…kritiske Side bragt til Bevidsthed. Be-"). A. ran to p.158, then B. Virkeligheden mod Ideen.

### (earlier resume note, superseded)
**~~Next: printed p.140 (PDF 148)~~** — continue **III. Ideelære §28 / a) Aristoteles's Kritik af
Ideelæren** (still inside A. Ideen i dens Væsenhed). Batch 13 ended mid-sentence at p.139 foot
("…men derimod — dette er just det"). **Quote-balance note:** from p.129 onward the document
carries a **net −1** in Danish quotes because of a print anomaly on p.129 (a closing quote at
"…gjensidig.“" with no matching opening on p.128/129 — the Sophistes paraphrase runs unquoted;
reproduced verbatim and flagged inline). Future batch quote-checks should expect closings =
openings + 1.

### (earlier resume note, superseded)
**~~Next: printed p.129 (PDF 137)~~** — continue **III. Ideelære §27 / A. Ideen i dens Væsenhed**.
Batch 12 ended mid-sentence at p.128 foot ("…da Talen jo netop bestaaer deri, at man i").
**III. Ideelære** Part head is placed (p.118); **§26** (Kant/Plato/Schelling/Hegel Idee-lære,
teleology antinomy) done through the section-end rule at p.124; **A. Ideen i dens Væsenhed**
sub-head + **§27** opened (p.124), the run-in head *1) Ideer og Begreber* (p.125). Structure
ahead: rest of A. (to p.158), **B. Virkeligheden mod Ideen** (158–178), **C. Ideens Gyldighed**
(178–198), **Slutning** (199–204). **No errata pending** — all Rettelser applied.

## DONE so far
- **Batch 19 (pp.195–204), image-verified — FINAL BATCH, book complete.** Closes **C. Ideens
  Gyldighed §36** and adds the **Slutning** (Conclusion). §36 c) *Naturideens Realitet* centred
  sub-head (p.196). The atom/aggregation critique of Materialism (Forchhammer *Chemie* quotes on
  Svovl/Selen/Tellur and Element-decomposition; Ammoniet/Cyanet). Big Hegel *Naturphilosophie*
  German quote „Die Natur ist an sich, in der Idee göttlich…" (p.196→197) with Latin antiqua →
  `\textit{non-ens}` and German letterspacing → `\emph{}`: *Abfall* (p.196), *sinnlichen* (p.197);
  the Moleschott „ohne Phosphor kein Gedanke!"; the phosphorus/brain-materialism discussion. **C.
  Ideens Gyldighed** (and III. Ideelære) closed with a centred section-end rule at p.198 foot.
  **Slutning** rendered as a top-level division (`{\Large\bfseries Slutning.}` + rule + ToC
  `section` entry, p.199): the retrospective on Propædeutik as both a scientific whole and an
  "Indledning til Philosophien", the Hvad/Hvorledes distinction, the induction/system/idea
  examples (Kepler's Mars orbit, crystallography/botany/zoology), and the closing polemic against
  the superficial "Overbliksmænd" critics — ending „…de rette Uvedkommendes taabelige
  Selvvigtighed." + the final book-end rule. Danish embedded quotes: „Punkter af Philosophiens
  Historie", „en Indledning til Philosophien", the imagined-critic speech „At, maadeligt!…"
  (p.202→203), „det Fremstillede er uforstaaeligt!"/„…trivialt…". Silent Fraktur-glyph corrections
  (correct word, no flag): *Vrimmel* (V, p.195), *betyder/Betydning* (y), *afsluttet* (long-s,
  p.201), *uafviselig* (u, p.200). **Print flags (d/b glyph confusions), corrected + flagged
  inline — six on this batch:** "besuden"→"desuden" (p.195), "forbi"→"fordi" in the Forchhammer
  quote (p.195), "Ombannelser"→"Omdannelser" (p.195), "undbrage"→"unddrage" (p.196), "forbi"→
  "fordi" (p.201). Page joins: p.194→195 mid-sentence ("…med andre" + "Ord…"); paragraph-boundary
  section-end before Slutning; others mid-sentence. Compile: **163 pp., 0/0/0**; `$`=182 (even);
  braces 904/904; guillemets 1/1; whole-file „/“ = **400/400 (perfectly balanced)**. Book ends at
  p.204; **whole book pp.3–204 now transcribed.**
- **Batch 18 (pp.184–194), image-verified.** **III. Ideelære §35 + §36 (opening),** all inside
  **C. Ideens Gyldighed** — the Idea as the common ideal of the real sciences (§35: the
  cosmological / geological / physiological ideals) and Nature as Idea (§36). **§35** and **§36**
  headings placed. Both §-opening sentences are **fully letterspaced** (whole Sperrsatz paragraphs
  → `\emph{At fornegte Ideen … Ideen.}`). Five centred sub-heads (letterspaced, run-in style →
  `\begin{center}\emph{…}\end{center}`, no ToC entries): *a) Det kosmologiske Ideal* (p.184),
  *b) Det geologiske Ideal* (p.186), *c) Det physiologiske Ideal* (p.187), *a) Naturen som Idee*
  (p.192), *b) Ideen som Natur* (p.193). Danish Sperrsatz single words → `\emph{}`: *Natur*
  (p.190, in "Begrebet: Natur"), *Atomer* / *Aggregation* (p.194) — note "Ordet: Natur" on p.191 is
  **not** letterspaced (zoom-checked). Verbatim quotes: the Valentin *Physiologie* machine-analogy
  „Man har ofte sammenlignet Organismen…" (Kbhvn. 1857, S. 5) with Latin antiqua → `\textit{Camera
  obscura}`, continued by „Men vore mechaniske Apparaters…" (closes p.188); the Dilemma „enten skeer
  Noget i Naturen…"; the hypothetical-syllogism „Dersom A er…" / „nu er A" and „Tingen er, fordi den
  er…"; the Materialist Naturens-Orden speech „der er i Naturen en Tingenes Orden…" (closes p.190);
  and the four big Hegel *Naturphilosophie*/*Einleitung* German quotes on p.192–193 („Beim
  theoretischen Verhalten…", „durch den sich eindrängenden Gedanken…", „Nämlich wir wollen die
  Natur erkennen…" closing p.193, „So ist die Natur die Braut…", „von der Idee entfremdet…" with
  `\ldots{}` elisions). Greek raw Unicode: platonisk ἰδέα / aristotelisk εἶδος (p.184). Hegel term
  „des Andersseyns" (p.193, -seyn per the p.174 zoom). **Print flags (d/b glyph confusions),
  corrected + flagged inline — five „forbi"→„fordi" on p.189** (all in the „Tingen er…" and „der er
  i Naturen…" quotes, each zoom-verified). Page joins: p.183→184 mid-sentence ("…i Kraft" + "af
  dialektisk…"); mid-word "Be-"/"regninger" (184→185); paragraph boundaries at 186→187, 188→189,
  191→192, 192→193(mid-quote), others mid-sentence. Compile: **156 pp., 0/0/0**; `$`=182 (even);
  braces 881/881; guillemets 1/1; whole-file „/“ = **390/390 (perfectly balanced)**.
- **Batch 17 (pp.173–183), image-verified.** **III. Ideelære §32 (rest) + §33 + closes B.
  Virkeligheden mod Ideen; opens C. Ideens Gyldighed (§34).** §32 finishes with the Hegel
  Naturphilosophie Erde/Magnet quote „Ueberhaupt … dessen Mitte Deutschland ist." (S. 442).
  **§33** (p.173, Materie as vanishing moment; Plato's Timæus-solids — Ilddelene Pyramiden etc.;
  Aristotle matter/form; crystal teleology). **§34** (p.178, opens **C. Ideens Gyldighed** — the
  apriority of the Idea vs. the new Materialism: Büchner/Vogt/Moleschott/Feuerbach quotes, Kant's
  analytic/synthetic distinction, the hegelske Logik as proof of the Idea). **C. Ideens Gyldighed**
  sub-head placed at p.178 (section-end rule + ToC subsection + rules), preceded by the rule that
  closes B. **§33** and **§34** headings placed. **§34's opening sentence is fully letterspaced**
  (whole Sperrsatz paragraph → `\emph{At fornegte Ideen … at anerkjende Ideen.}`). German
  letterspacing → `\emph{}`: the Kant *Materialismus, Fatalismus, Atheismus* / *Unglauben* /
  *Schwärmerei* / *Aberglauben* series (p.179). Danish Sperrsatz → `\emph{}`: *Aggregation*
  (p.176). Many verbatim-Fraktur German block quotes (no italic): the Erde/Magnet passage (S. 442);
  the crystal „Die Thätigkeit in ihr Product…" (S. 265) with inline Greek α)/β); the multi-paragraph
  „Der Magnet ist noch nicht zweckmäßig…" / „Indem der Krystall…" (S. 267, opening „ once, close
  once across two paragraphs — balanced); Feuerbach „Der außer- und übermenschliche Gott…";
  Moleschott „Es ist so unmöglich…"; Büchner „Wenn der Hirsch…" (S. 178); C. Vogt „Die Gedanken
  stehen…"; the Büchner *Kraft und Stoff* / „Ewigkeit" material (p.178); the Kant Fornuftkritik
  Vorrede „Durch diese kann allein…" (p.179); the analytic/synthetic Domme with „$5 + 7 = 12$" and
  the Kant Einleitung „Denn ich nehme zuerst die Zahl 7…" (p.180); Hegel „Raum und Zeit sind
  besonders dann keine Gedankenbestimmungen…" (p.181). Danish embedded quotes: „ruhige Zweck"
  (p.175), „Materien er et Udstrakt"/„Materien er Materie…" (p.180), „en Caprice"/„den sunde
  Forstand". Eschricht quote „Alle Planter og Dyr begynde …" (Læren om Livet, S. 35, p.176). Greek:
  παράδειγμα (p.174, raw Unicode). Hegel terms verbatim: „Außersichseyn", „Andersseyn" (p.174,
  zoom-verified -seyn). **Print flag (d/b glyph confusion), corrected + flagged inline:**
  "auszubrücken"→"auszudrücken" in the C. Vogt quote (p.178). Math: fall-law series carried over;
  the "5 + 7 = 12" set in math mode. Page joins: p.172→173 mid-quote/mid-sentence
  ("…bestimmt" + "zu faßen…"); mid-word "Skik-"/"kelse" (175→176); paragraph boundaries at
  179→180 and 182→183; all others mid-sentence. Compile: **147 pp., 0/0/0**; `$`=182 (even);
  braces 852/852; guillemets 1/1; whole-file „/“ = **374/374 (perfectly balanced)** — the p.129
  −1 offset by the p.162–163 repeated-opening +1, and the p.172 trailing quote closed on p.173.
- **Batch 16 (pp.162–172), image-verified.** **III. Ideelære §31 (rest) + §32 (opening),** inside
  **B. Virkeligheden mod Ideen** — Hegel's *Naturphilosophie* critique of the mathematical treatment
  of motion (fall law, Taylor series, planetary orbits, teleology). **§32** heading placed (p.167).
  Long German Hegel block quotes (verbatim Fraktur): „In dem Satze…" (Naturphil. S. 87);
  the multi-paragraph „Das Gesetz des Falles…" / „Dieser Zusammenhang…" / „Dieß ist der Beweis…"
  block (pp.162–163) — a **repeated opening „** at each paragraph start with a single close → **+1**
  quote imbalance (print convention, reproduced verbatim); „Die Voraussetzung…"; „Bestimmungen…";
  „Nur das Suchen des Centrums…"; „Was nun die Gestalt der Bahn…" (p.168→169); „Da der Mond…" /
  „Das ist aber zunächst…" / „Man sagt…" (S. 111); „Die Bewegung der Himmelskörper…" (S. 97);
  „die besondern Formationen der Erde"; the trailing „Dieß erscheint zunächst als zufällig…" (open,
  closes on p.173). German letterspacing → `\emph{}`: *Falles*/*freies*/*Begriffe*/*Qvadrate*
  (p.162), *Zeit*/*frei*/*Größebestimmungen*/*Negation*/*Einheit*/*Raum*/*Außereinandersehn*/
  *keiner andern Größe*/*freien*/*äußerlich* (p.162), *Eine*/*Einheit*/*Außereinander*/*Qvadrat*/
  *keiner andern als ihrer eignen*/*Falls*/*Begriffe der Sache* (p.163), *gleichförmig*/
  *beschleunigende*/*Trägheit* (p.163), *Kreis*/*schlecht-gleichförmigen*/*Denkbar* (p.168),
  *gleich*/*Eine*/*ganze*/*Verschiedenheit*/*an dem Räumlichen*/*Differenz*/*Ellipse* (p.169).
  Danish Sperrsatz → `\emph{}`: *Bevægelse*/*Hastighed*/*Kraft*/*Forandring i Kraft* (p.166), *Solen*
  (p.168). Math: fractions `$\frac{s}{t}$`/`$\frac{s}{t^2}$`, fall-law integrals
  `$r\int_0^n p\,dp=\frac{n^2 r}{2}$…` (p.164), Taylor-series display + a 3-line `aligned` system with
  `\varphi` (p.166–167), `$v=\frac{s}{t}$` (p.165). Latin antiqua → `\textit{}`: *punctum
  æquatorium*/*p. æquans*/*punctum æquans* (p.168), the Copernicus *lucernam mundi* /
  *circumagentem gubernans astrorum familiam* / *Quis enim in hoc pulcherrimo templo…* + ref
  (p.168), *Sinus versus*/*Sagitta* (p.170), Bacon *Causarum finalium inquisitio sterilis est…*
  (p.169), Leibniz *Finalem causam non tantum prodesse…De ipsa natura* (p.171), *causæ finales*/
  *causæ efficientes* (p.172). French antiqua → `\textit{}`: the Leibniz *Bien loin d'exclure les
  causes finales…* letter (p.169), the Laplace guillemet quote »*Sire, je n'avais pas besoin de
  cette hypothèse!*« (p.172). Greek zoom-verified: (τὸ ἐξ ὑποθέσεως ἀναγκαῖον) (p.171). German
  parentheticals kept in Fraktur (no italic): (die äußere Zweckmässigkeit) (p.172). **Print flags
  (d/b glyph confusions), corrected + flagged inline:** "forbi"→"fordi" (p.165), "forbi"→"fordi"
  ×2 (p.169). Page joins: p.161→162 mid-sentence ("…Anviisning" + "vil Hegel…"); mid-word none;
  paragraph-boundary at 163→164, 171→172. Compile: **139 pp., 0/0/0**; `$`=180 (even); braces
  818/818; guillemets 1/1; whole-file „/“ = **347/346** (net +1, reconciles p.129 −1 with the
  p.162–163 repeated-opening +1 and the p.172 trailing-open +1).
- **Batch 15 (pp.151–161), image-verified.** **III. Ideelære §29 (rest) + closes A. Ideen i dens
  Væsenhed; opens B. Virkeligheden mod Ideen (§30–§31).** Run-in heads *b) Den uendelige
  Negativitet* (p.152), *c) Den speculative Form* (p.155) → `\emph{}`. **B. Virkeligheden mod
  Ideen** sub-head placed at p.158 (ToC subsection entry + rules), preceded by the section-end
  rule that closes A. **§30** (p.158) and **§31** (p.161) headings. Many German Hegel/Apelt block
  quotes (all verbatim Fraktur, no italic): the Antinomien / Sprüchwörter / Skepticismus /
  Wissenschaft-der-Logik / „Die Idee ist die Wahrheit" passages; German letterspacing → `\emph{}`:
  *die Einheit* (p.156), *Die Idee ist die Wahrheit*/*richtige*/*alles* (p.157), *urtheilend*/
  *zunächst* (p.158). Latin antiqua → `\textit{}`: *qui bene distingvit, bene docet* (p.151),
  *summum jus summa injuria* (p.151), *summa injuria*/*summum jus* (p.152). Greek zoom-verified:
  (εἰ ἓν ἔστι)/(εἰ ἓν μὴ ἔστι) (p.157); the Apelt passage εἶδος, (ἀρχαί) ὑποκείμενον / ἀντικείμενα
  / στέρησις, τὸ εἶδος→τὸ τί, τὸ ὑποκείμενον/οὐσία, (ὕλη)/(δυνάμει ὄν)/(ἐντελεχείᾳ ὄν)/(μορφή),
  ἐμπειρία/νοῦς/ἐπαγωγή/αἴσθησις (pp.159–160). Math: `$v=\frac{s}{t}$` (p.161). **Print flags
  (d/b glyph confusions), corrected + flagged inline:** "forbi"→"fordi" ×2 (p.152), "venbing"→
  "vending" (Indvending, p.153), "abæqvate"→"adæqvate" (p.157), "forbi"→"fordi" (p.159).
  Mid-word page joins: Be-/grebsanalyser (150→151), Ind-/vending (152→153), Be-/greb (158→159),
  bekræf-/tende (159→160). Compile: **130 pp., 0/0/0**; `$`=140 (even); braces 684/684; batch
  quotes 31/31 (internally balanced); whole-file „/“ = 324/325 (the documented p.129 −1).
- **Batch 14 (pp.140–150), image-verified.** **III. Ideelære §28 (b/c) + §29 opening**, all
  inside A. Ideen i dens Væsenhed — Aristotle's substance/matter–form/entelechy doctrine, again
  extremely Greek-dense (every polytonic passage zoom-verified: τὸ πρώτως ὂν…, ἡ ὕλη ἄγνωστος
  καθ' αὑτήν, ὅταν ἐνεργῇ…, the four-causes εἰσὶν ἄρα δύ' αἰτίαι…, ἓν ἄρα καὶ λόγῳ καὶ ἀριθμῷ…,
  the νόησις νοήσεως νόησις line, etc.). Run-in heads *b) Aristoteliske Principer* (p.140),
  *c) Den aristoteliske Entelechie* (p.143), *a) Modsigelsens Dialektik* (p.149) → `\emph{}`;
  inline α)/β)/γ) argument on pp.144–147. **§29** heading (p.148). Two long Schwegler quotes
  span pages (p.141→142 and p.143→144); the „Man seer ikke (Schwegler)…“ and „Det Ikke-Værende
  er ikke“ quotes. Latin → `\textit{}`: *esse potentia* / *esse actu* (p.141), *principium
  exclusi medii inter duo contradictoria* (p.148). Danish "og" sits inside a Greek paren on
  p.142 (τὸ κινητόν og τὸ κινητικόν) — verbatim. **Print flag (p.148):** the word read "dødt"
  is set with an ambiguous d/b glyph ("døbt"); context "i det Døde" makes "dødt" certain —
  transcribed so, flagged inline. Compile: **122 pp., 0/0/0**; `$`=138 (even); braces 647/647;
  1 marker; batch-14 Danish quotes 9/9 (balanced; the whole-file −1 from the documented p.129
  anomaly persists).
- **Batch 13 (pp.129–139), image-verified.** **III. Ideelære §27 (b/c) + §28 (a)**, all inside
  A. Ideen i dens Væsenhed — extremely Greek-dense (Plato *Parmenides*/*Sophistes*/*Philebus*/
  *Timæus* and Aristotle's *Metaphysics* critique). Run-in heads reproduced verbatim as printed:
  *b) Ideerne selv og de sandselige Ting* (p.129), *c) Ideernes indbyrdes Forhold* (p.134),
  *a) Aristoteles's Kritik af Ideelæren* (p.137) → `\emph{}` (note the §27 series is printed
  **1)/b)/c)**, a source quirk kept as-is). Inline paragraph markers **α)/β)/γ)** on pp.131–132.
  §28 heading (p.136). Danish quotes: Menon quote + „I Erkjendelsens Sphære…“ (Republiken)
  (p.135); the Aristotle „der meente ikke at kunne regne…“ (p.138); „Ideernes Materie“,
  „Deeltagen.“ Every polytonic-Greek passage zoom-verified (long Parmenides strings ὀνόματα/
  ῥήματα … μεταλαμβάνειν; Ἀμφοτέρως…; τὸ ὄντως ὄν…; ἀριθμοὶ νοητοί/συμβλητοί/ἀσύμβλητοι;
  ὁ τρίτος ἄνθρωπος; etc.). One Danish "og" sits inside a Greek paren on p.136 (ἀριθμοὶ
  μαθηματικοί og αἰσθητοί) — kept verbatim. **Print anomaly flagged inline (p.129):** a closing
  quote at "…gjensidig.“" with no matching opening; reproduced verbatim → document quote balance
  is net −1 from here on. Compile: **113 pp., 0/0/0**; `$`=138 (even); braces 638/638; 1 marker;
  batch-13 Danish quotes 19 open / 20 close (the −1 is the documented p.129 anomaly).
- **Batch 12 (pp.118–128), image-verified.** Opens **III. Ideelære** (Part head + ToC `section`
  + `\markboth`). **§26**: Kant's Idee-definition (*Kritik der r. Vern.* S. 289; *Kritik der
  Urtheilskraft*; *Einleitung*), the long Plato/Kant quotes on Ideas vs. Forstandsbegreber and
  the platonic Republic; *Notio*; Naturens *Hensigtsmæssighed* (æsthetisk/teleologisk;
  *ydre*/*indre*, *Naturmechanisme alene*); Hylozoisme/Theisme/Fatalisme (Fraktur — NOT
  italic); *intellectus archetypus*; Schelling/Hegel (*Geschichte der Philosophie, 3 Th.,
  Berlin 1844, S. 613*); the teleology antinomy (*Sætning*/*Modsætning*); Raphael/anatomy
  Idee-examples; closes §26 with a centred rule at p.124 (previewing *Ideen i dens Væsenhed*,
  *Virkeligheden mod Ideen*, *Ideens Gyldighed*). **A. Ideen i dens Væsenhed** sub-head + ToC
  `subsection`. **§27** (Poul Møller quote; Plato Ideelære ↔ Dialektik with polytonic Greek;
  run-in head *1) Ideer og Begreber*; Protagoras/Theætet/Sophistes material — heavy polytonic
  Greek, incl. στ **stigma ligature ϛ** kept verbatim in ἔϛιν/ἐϛὶν/ἐπιϛτήμη; eleatic maxim
  *kun det Værende er, det Ikke-Værende er ikke* letterspaced). Fraktur fix: **Forandringerne**
  (p.126, not "Foranbringerne"), **udhæve** (p.122, d/b). Latin/German inserts → `\textit{}`.
  Compile: **105 pp., 0/0/0**; `$`=138 (even); braces 632/632; 1 marker; batch-12 quotes 23/23.
- **Batch 11 (pp.107–117), image-verified.** **Finishes II. Videnskabslære** (C.
  Philosophien og de særskilte Videnskaber), §23 cont.–§25, and closes Section II with a
  centred rule. §23 (Opposita juxta se posita magis illucescunt → `\textit{}`). **§24**
  Fremstilling/Forstaaelse (two letterspaced run-in heads *Fremstillingsmaaden* /
  *Forstaaelsen* → `\emph{}`; the hegelske Methode critique; „det Abstracte"/„det Taagede"/
  „det Svævende"/„det Tvetydige"). **§25** the three-fold philosophical labour with
  letterspaced numbered run-ins **1) Tilegnelse: en assimilerende Virksomhed** (*in succum
  et sanguinem*), **2) Frigjørelse: en humaniserende Virksomhed** (Hegel's Mechanisme/
  Chemisme; „Function"/„Tilnærmelse"/„Reflexion" cross-sphere examples), **3)
  Inderliggjørelse: en totaliserende Virksomhed** (*omnia mea porto mecum*; kritisk /
  dialektisk / kritisk-dialektisk Methode → `\emph{}`; „der Begriff"; hegelske vs.
  kierkegaardske Analyser, Teleskop/Mikroskop). Latin phrases → `\textit{}`. Compile:
  96 pp., 0/0/0; `$`=138 (even); braces 570/570; 1 marker; batch-11 quotes 18/18.
- **Batch 10 (pp.96–106), image-verified.** **II. Videnskabslære**: finishes **B. De
  særskilte Videnskaber** (§21 cont.: Bifag/Hovedfag, university Faculteter, Theorie/Praxis
  — closes B. with a centred rule at p.98 foot), then opens **C. Philosophien og de
  særskilte Videnskaber** (sub-head + ToC `subsection`, p.99) with **§22** (the antike
  Meno-problem quote; Plato *Phædrus*, ἀνάμνησις ×2 — polytonic Greek; a priori/a
  posteriori) and **§23** (Philosophy as non-Fagvidenskab; the Eros/Poros/Penia
  *Symposion* image; αὐτάρκεια; philosophy needs history + Realvidenskaberne; Mathematik
  & Chemie as Nøgler). Chemistry/maths inline: Trilogier $\frac{A+C}{2}=B$ (Barium/
  Strontium/Calcium; Svovl/Selen/Tellur), polymer hydrocarbons $\mathrm{CH_2}$/
  $\mathrm{C_2H_4}$/$\mathrm{C_4H_8}$/$\mathrm{C_{16}H_{32}}$; oxide density series. Latin
  *juxtapositio* → `\textit{}`. **ERRATA APPLIED: p.106 l.14 fra neden Ilter → Metalilter**
  (flagged with `% ERRATA`). Compile: 87 pp., 0/0/0; `$`=138 (even); braces 549/549;
  1 marker; batch-10 quotes 4/4, dollars 24 (even).
- **Batch 10 (pp.96–106), image-verified.** **II. Videnskabslære**: finishes **B. De
  særskilte Videnskaber** (§21 cont.: Bifag/Hovedfag, university Faculteter, Theorie/Praxis
  — closes B. with a centred rule at p.98 foot), then opens **C. Philosophien og de
  særskilte Videnskaber** (sub-head + ToC `subsection`, p.99) with **§22** (the antike
  Meno-problem quote; Plato *Phædrus*, ἀνάμνησις ×2 — polytonic Greek; a priori/a
  posteriori) and **§23** (Philosophy as non-Fagvidenskab; the Eros/Poros/Penia
  *Symposion* image; αὐτάρκεια; philosophy needs history + Realvidenskaberne; Mathematik
  & Chemie as Nøgler). Chemistry/maths inline: Trilogier $\frac{A+C}{2}=B$ (Barium/
  Strontium/Calcium; Svovl/Selen/Tellur), polymer hydrocarbons $\mathrm{CH_2}$/
  $\mathrm{C_2H_4}$/$\mathrm{C_4H_8}$/$\mathrm{C_{16}H_{32}}$; oxide density series. Latin
  *juxtapositio* → `\textit{}`. **ERRATA APPLIED: p.106 l.14 fra neden Ilter → Metalilter**
  (flagged with `% ERRATA`). Compile: 87 pp., 0/0/0; `$`=138 (even); braces 549/549;
  1 marker; batch-10 quotes 4/4, dollars 24 (even).
- **Batch 9 (pp.85–95), image-verified.** **II. Videnskabslære / B. De særskilte
  Videnskaber**, §18 cont.–§21. p.85 finishes the Hegel-encyclopedia division of the
  sciences (Aandsvidenskab a) Anthropologie/Psychologie/Philologie · b) Retslæren/
  Statsvidenskaben/Historien · c) Æsthetik/Religionslære/Philosophie — letterspaced
  discipline names → `\emph{}`); the Encyklopædi quote; **Apelt** (*die Theorie der
  Induction*) on the three kinds of knowledge (empiriske/mathematiske/philosophiske),
  the kategorisk/hypothetisk/conjunctiv systems, *in abstracto* (→ `\textit{}`).
  **§19** *Historien fortæller, Philosophien reflecterer* (letterspaced opening): history
  vs. philosophy of history, Historieskrivning som Kunst, the franske Revolutionshistorie
  example. **§20** the typical Naturformer with run-in heads **a) Den døde Form**
  (Krystallographie; Berzelius vs. Mohs), **b) Den levende Form** (Linné's Sexualsystem;
  Reichenbach), **c) Den besjælede Form** (Bløddyr/Leddyr/Hvirveldyr; Cuvier vs. Geoffroi
  St. Hilaire) — all letterspaced → `\emph{}`. **§21** opens: Fagvidenskaber, the
  Physiologie („et levende Maskinerie", G. Valentin) vs. Psychologie strife, science vs.
  Mirakelvidenskab, mathematics as Hjælpevidenskab. Fraktur fixes: **Afsnit** (not Affnit),
  **Indordnen** (not Inbordnen), **de selv have hjulpet** (p.95, d/b). Cross-refs to
  *Philosophie og Mathem.* plain. Compile: 79 pp., 0/0/0; `$`=114 (even); braces 515/515;
  1 marker; batch-9 quotes 14 open / 14 close (balanced).
- **Batch 9 (pp.85–95), image-verified.** **II. Videnskabslære / B. De særskilte
  Videnskaber**, §18 cont.–§21. p.85 finishes the Hegel-encyclopedia division of the
  sciences (Aandsvidenskab a) Anthropologie/Psychologie/Philologie · b) Retslæren/
  Statsvidenskaben/Historien · c) Æsthetik/Religionslære/Philosophie — letterspaced
  discipline names → `\emph{}`); the Encyklopædi quote; **Apelt** (*die Theorie der
  Induction*) on the three kinds of knowledge (empiriske/mathematiske/philosophiske),
  the kategorisk/hypothetisk/conjunctiv systems, *in abstracto* (→ `\textit{}`).
  **§19** *Historien fortæller, Philosophien reflecterer* (letterspaced opening): history
  vs. philosophy of history, Historieskrivning som Kunst, the franske Revolutionshistorie
  example. **§20** the typical Naturformer with run-in heads **a) Den døde Form**
  (Krystallographie; Berzelius vs. Mohs), **b) Den levende Form** (Linné's Sexualsystem;
  Reichenbach), **c) Den besjælede Form** (Bløddyr/Leddyr/Hvirveldyr; Cuvier vs. Geoffroi
  St. Hilaire) — all letterspaced → `\emph{}`. **§21** opens: Fagvidenskaber, the
  Physiologie („et levende Maskinerie", G. Valentin) vs. Psychologie strife, science vs.
  Mirakelvidenskab, mathematics as Hjælpevidenskab. Fraktur fixes: **Afsnit** (not Affnit),
  **Indordnen** (not Inbordnen), **de selv have hjulpet** (p.95, d/b). Cross-refs to
  *Philosophie og Mathem.* plain. Compile: 79 pp., 0/0/0; `$`=114 (even); braces 515/515;
  1 marker; batch-9 quotes 14 open / 14 close (balanced).
- **Batch 8 (pp.74–84), image-verified.** **II. Videnskabslære**, §14 cont.–§18:
  finishes **A. Videnskabernes Videnskab** (to p.80) and opens **B. De særskilte
  Videnskaber** (sub-head + ToC `subsection`, p.81). The „absolute Videns" Philosophie
  critique; §18 opens the Hegel encyclopedia division (Logik / Naturvidenskab /
  Aandsvidenskab; Naturvidenskab a) Mechanik · b) Det Uorganiskes Physik · c) Det
  Organiskes Physik — letterspaced → `\emph{}`). Fraktur fix: **Udveie**. Compile:
  71 pp., 0/0/0; `$`=114 (even); braces 482/482; 1 marker.
- **Batch 7 (pp.63–73), image-verified.** Ends **§11** (b) Tingene og deres Egenskaber
  — optics/atom-theory, Fechner *Atomenlehre*; c) Den væsentlige Viden og de virkelige
  Objecter — Hegel *Phänomenologie*, the „Sølv“ substrate example) and **closes
  Section I. Erkjendelseslære** with a centred rule. Then opens **Part II.
  Videnskabslære** (full Part head + ToC `section` + `\markboth`): **§12** (Kant
  *Kritik der reinen Vernunft*, *reservatio mentalis*, Fichte *Wissenschaftslehre*,
  Hegel *Phänomenologie des Geistes*; Philosophy/Theology/Physics epochs; rule),
  **A. Videnskabernes Videnskab** sub-head (ToC `subsection`) + **§13** (science's
  mythic origins; outer/inner/conflict hindrances a)/b)/c) with letterspaced run-ins),
  **§14** (Philosophy as the Videnskabernes Videnskab; Sibbern „Debat af Alt imod Alt“;
  Theology's *credo ut intelligam* / *de omnibus dubitandum est*). Fraktur fixes:
  lovløs, sondrede, kaste Vrag paa. Latin/German inserts → `\textit{}`. Compile: 62 pp.,
  0/0/0; `$`=108 (even); braces 437/437; 1 marker.
- **Batch 6 (pp.52–62), image-verified.** **C. Sagerkjendelse** §9 cont.–§11: the
  Hegel Naturphil.-optics critique (S. 141, „die für die Erkenntniß…nutzen“); **§10**
  on Erfaringslæren, Kant vs. Hegel on aprioriske Former, causation/law; the three
  run-in heads **a) Abstractionen · b) Inductionen · c) Den virkelige Lov** (all
  letterspaced → `\emph{}`); the density/molecule maths ($m/v=\varrho$, $v/n=e^3$,
  $dm/dv=\varrho$, $\Sigma\!\to\!\int$, $\varrho\int dv$, $\int\varrho\,dv$); the Apelt
  *Theorie der Induction* material with **polytonic Greek** (ἐπαγωγή/συλλογισμός/
  ἐπιστήμη); the Kepler Mars-orbit induction ($O_1\ldots O_n$ ditto-table, polar
  equation $r=a(1-e^2)/(1-e\cos v)$); **§11** opening + **a) Tingene og Lovene**
  (Newton *Philosophiæ naturalis principia mathematica*, force/matter, chemistry).
  Cross-ref to the companion *Philosophie og Mathematik* S. 12–14. Latin/German inserts
  → `\textit{}`. Compile: 53 pp., 0/0/0; `$`=108 (even); braces 371/371; 1 marker.
- **Batch 5 (pp.41–51), image-verified.** **C. Sagerkjendelse** §8 cont.–§9: „den sunde
  Forstand“ vs. Idealismen; Modsigelse/Dialektik (Herbart vs. Hegel, „Alles ist ein
  Widerspruch“; Dialektikens Nerve); **§9** the logical „Blad“/„dette“ example, Stilpon,
  scholastic *res*/*universalia*; then the three-fold analysis with run-in heads
  **a) Det Sandselige og det Tænkelige** (Feuerbach *Philosophie der Zukunft*; Hegel
  Naturphil. S. 271 with print „algemeine“ flagged), **b) Det Individuelle og det
  Almene** (Herbart Qvalia/*principium indiscernibilium*; *Phänomenologie*), **c) Det
  Virkelige og det Væsentlige** (Schelling line-image with $A=A$, $\overset{+}{A}=B$,
  $A=\overset{+}{B}$; potencies $A,A^2,A^3$; Lagrange's planetary formula). ERRATA
  APPLIED: **p.42** (det vilkaarlige→det virkelige), **p.48** (quote-mark relocation:
  Herbart quote closes at „Punkt;“, not „opløse.“) — each flagged. Polytonic Greek
  πρῶτον ψεῦδος (p.47). Compile: 45 pp., 0/0/0; braces balanced; 1 marker.
- **Batch 4 (pp.30–40), image-verified.** Finishes **B. Idealisme**. §6 cont.: the
  Kant Antinomier (Thesis/Antithesis pairs) and the Ideal (ontological-proof critique,
  „Hundrede virkelige Daler…"); **1) Mod Skepticismen · 2) Mod Dogmatismen · 3) Den
  transcendentale Idealisme** (the last two centred-bold letterspaced heads). §7:
  Fichte's Wissenschaftslehre — the $A=A$ / Jeg $=$ Jeg / Non-$A$ / $X$ apparatus
  (α Thesis, β Antithesis, γ Synthesis, all letterspaced heads), the long Fichte and
  Herbart quotations; Schelling (*Von der Weltseele*, *System des transc. Idealismus*)
  and Hegel (*Phänomenologie des Geistes*) with the Bevidsthed/Selvbevidsthed/Fornuft
  (a/b/c, α/β/γ) march; closes B. with the Hegel „Maalet…" quote + rule. Opens **C.
  Sagerkjendelse** heading + §8. German/Latin/English inserts → `\textit{}`.
  Compile: 36 pp., 0/0/0, braces/`$` balanced, 1 marker. (Greek α/β/γ/δ markers need
  the extra `-e 's/δ/d/g'` etc. in the sandbox sed — recipe updated below.)
- **Batch 3 (pp.19–29), image-verified.** **B. Idealisme** §5 cont.–§6: Descartes
  (*cogito ergo sum*, *ideæ innatæ*), Spinoza, Leibnitz (*Nouveaux essais*,
  *principium contradictionis/rationis sufficientis/indiscernibilium*), Berkeley
  (three English work-titles + the long „It is therefore plain…" quote in antiqua),
  the Kant §6 opening (*Kritik der reinen Vernunft*), „1) Mod Skepticismen" with the
  transcendental Æsthetik/Analytik/Dialektik (a/b/c) and the α/β/γ/δ Grundsætninger,
  Paralogismer + Antinomier. Latin/German/English antiqua → `\textit{}`. One flagged
  print oddity (p.24 „n Erkjendelse" for „en"). Compile: 27 pp., 0/0/0.
- **Batch 2 (pp.9–18), image-verified.** Rest of **A. Sensualisme** (§3–§4: the
  Renaissance speculative/empirical split — „Den speculative Retning"/„Den empiriske
  Vei" letterspaced run-in heads; Bacon, Locke a)/b)/c) on Ideernes Oprindelse/Væsen +
  Tingenes Erkjendelse; Condillac, Hume, La Mettrie) and opens **B. Idealisme** §5.
  ERRATA APPLIED: p.12 (Gjenstandenes→Gjenstandens), p.15 & p.16 (Continuitet→
  Contiguitet), each flagged in a comment. Latin phrases (*tabula rasa*, *qualitates
  primariæ/secundariæ*, *cum hoc aut post hoc…*) + English work-titles → `\textit{}`.
  Compile: 19 pp., 0/0/0.
- **Batch 1 (setup + front matter + pp.3–8), image-verified.** Preamble (book class;
  amsmath, libertinus, libertinust1math, textalpha, fancyhdr, hyperref, microtype;
  no tikz/graphicx — prose only). Title page (PDF 9) reproduced. Bacon motto placed
  at front. `\tableofcontents`. **Indledning** (pp.3–5): the two Grundspørgsmaal
  („hvad er Philosophie?", „hvilken Gyldighed…") set as `\emph{}` (Sperrsatz,
  zoom-verified); Philosophien-as-Bevidsthedslære programme; the a)/b)/c) Grundforhold
  and the I/II/III Hoveddele. **I. Erkjendelseslære** heading + **§1** (pp.5–7):
  Bevidsthed=Indhold identity; Positivt/Negativt = Sandsning/Tænkning; the Latin
  maxims (*omnis determinatio est negatio*, *scimus quia accepimus/facimus*,
  *scientia et potentia in idem concidunt*) with the Sibbern reference; the
  Sensualisme/Idealisme/Sagerkjendelse triad (all three Sperrsatz → `\emph{}`).
  **A. Sensualisme** heading + **§2** (pp.7–8): Individets Bevidsthed; the Greek
  Ionere→Sensualisme historical sketch (Thales/Anaximander/Anaximenes; „Vandet",
  „Luften"; Pythagoræer/Eleater/Plato; Aristoteles; Stoikere/Epikuræere).
  Portable compile clean: **11 pp., 0 errors, 0 undefined cs, 0 missing char,
  0 overfull hbox**, braces/`$` balanced, 1 continuation marker. Pages zoom-verified
  at 300 dpi (letterspacing confirmed on pp.3 and 7; none on pp.4,5,6,8).
