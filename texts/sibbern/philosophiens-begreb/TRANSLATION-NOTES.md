# Sibbern, *On the Concept, Nature, and Essence of Philosophy*
# (*Om Philosophiens Begreb, Natur og Væsen*, 1843) — translation resume notes

State for the **English translation** of this book. Update after each batch.
The user (Hans) compiles/commits/pushes — never the assistant.

Source of truth: `transcription.tex` (Danish), **COMPLETE + image-verified**
(Fortale + §§ 1–21 + the verbatim Rettelser leaf; final compile 59 pp., 0/0). See
`RESUME-NOTES.md` for the transcription's batch-by-batch history and its FLAGs.
**Translate FROM the transcription, not from the PDF scan.**

Standing method: `../../../TRANSLATION-PLAYBOOK.md`. Read it first, then this file,
then `grep -n "text to be added" translation.tex` and run the batch loop.

**Same policy as the companion volume *Om Erkjendelse og Granskning*** (its
translation is complete; see `../erkjendelse/TRANSLATION-NOTES.md` and
`../erkjendelse/GLOSSARY.md` as the model — this book's setup mirrors it).

## Where everything is (orientation for a fresh session)
The repo is **`~/danish-texts`** (a git repo; it is mounted, so read/edit files in
place). This book lives in **`~/danish-texts/texts/sibbern/philosophiens-begreb/`** —
work here. Files in this folder:
- **`transcription.tex`** — the Danish. **Source of truth; translate FROM this.**
  COMPLETE + image-verified (Fortale + §§1–21 + Rettelser). Do not edit it.
- **`translation.tex`** — the English. **This is what you fill**, marker by marker.
  Already scaffolded (title, Preface marker, group heads, §§1–21 markers, Rettelser
  marker); mirrors the transcription 1:1.
- **`GLOSSARY.md`** — the fixed English equivalents. Read before starting; update as
  you fix terms.
- **`TRANSLATION-NOTES.md`** — this file (translation state; update after each batch).
- **`RESUME-NOTES.md`** — the *transcription's* batch history and its per-page FLAGs
  (e.g. the p.38 „dettte" typo, the p.15 „Diet" oddity). Consult it when a Danish span
  reads strangely — the flag usually explains why.
- `transcription.pdf` — the compiled Danish, for eyeballing layout if useful.

Elsewhere:
- **The model to copy:** `../erkjendelse/` — the companion volume, translation DONE.
  Its `translation.tex`, `TRANSLATION-NOTES.md`, and `GLOSSARY.md` are the template
  this setup mirrors; open them when unsure how something was handled.
- **The standing method:** `../../../TRANSLATION-PLAYBOOK.md` (i.e.
  `~/danish-texts/TRANSLATION-PLAYBOOK.md`). Read it first.
- **The scan** (`~/bibliotek/Sibbern, Frederik/om-philosophiens-begreb.pdf`) is for
  reference only — you translate from `transcription.tex`, NOT the scan. No OCR/image
  work is needed for the translation phase (that was the transcription phase).
- **Paths:** the file tools (Read/Write/Edit) use the `~/danish-texts/...` paths above.
  In the bash sandbox the same repo is under a session-specific mount — find it with
  `ls /sessions/*/mnt/` (it maps `~/danish-texts` → `/sessions/<id>/mnt/danish-texts`).

## What to do first (concretely)
1. `Read` `../../../TRANSLATION-PLAYBOOK.md`, then this file, then `GLOSSARY.md`.
2. `grep -n "text to be added" translation.tex` — the markers, in reading order.
3. Start **batch 1 = the Preface**: open `transcription.tex`, find `\chapter*{Fortale.}`
   (≈ L78–111); translate that span; replace the `% [text to be added: Preface …]`
   marker in `translation.tex` via `Edit`; sandbox-compile (recipe below); report.
4. Continue in ~10-printed-page batches per the section→page map and batch plan below.
5. After each batch, update the "DONE so far" and "CURRENT RESUME POINT" here. The
   user compiles/commits/pushes — you never commit.

## Decisions (carried over from the erkjendelse policy)
- **Register: lightly modernized.** Faithful in meaning; untangle Sibbern's long
  periodic syntax into readable modern English; period flavor softened, not erased.
- **Key terms: glossary + bracketed original.** On a term's first use in each
  section, gloss the Danish in brackets — "fundamental cognition [Grunderkjendelse]"
  — then use the English alone. Maintain `GLOSSARY.md` (seeded) for cross-section
  consistency, and keep shared terms identical to `../erkjendelse/GLOSSARY.md`.
- **Layout: English-only, section-keyed.** `translation.tex` mirrors the
  transcription's structure 1:1 (title, Preface, the six centered group-rubrics via
  `\grouphead`, §§ 1–21 each as a centered `\S~N` head + its title line + body +
  petit `Anm.` blocks). Printed page ranges live in the `% [text to be added:
  pp. X--Y]` markers, which also carry the Danish section title to translate.

## Open decisions (resolve with Hans as they come up)
- **Title.** Scaffold uses *On the Concept, Nature, and Essence of Philosophy — A
  Presentation of the Propaedeutic of Philosophy*. Confirm wording (esp. "Fremstilling
  af Philosophiens Propædeutik").
- **Group-head wording.** Provisionally translated in the scaffold (Preliminary
  Remarks; Introductory Considerations — On Cognition in General; The Propaedeutic
  Concept of Philosophy and Its Exposition; The Foundation of Philosophy and Its
  Work; The Full Determination of the Concept of Philosophy; Philosophy as a Member
  and Moment in the Whole Spiritual Life). Revisable.
- **`Anm.` rendering.** Proposed "Note~N." (matching erkjendelse's inline
  `\emph{Anm.}` → `\emph{Note.}`); "Remark~N." is the alternative. Pick one and keep
  it. These are the petit `{\small\emph{Anm.~N.} … \par}` blocks — keep them `{\small}`
  and `\emph`-labelled, mirroring the Danish.
- **Rettelser (errata leaf).** Corrects the *Danish* orthography, so it's meaningless
  in English. Per erkjendelse: render a one-line translator's note at end-of-file (a
  centred rule + `\footnotesize` italic note), or omit. Decide at finish. (Scaffold
  has a marker placeholder there.)

## Page map (from the transcription)
- **Printed page = PDF page − 11.** Title page = PDF 6; Fortale = PDF 8–9.
- Section → printed start page (verified via the Indhold):
  §1 p.1 · §2 p.4 · §3 p.7 · §4 p.12 · §5 p.15 · §6 p.21 · §7 p.22 · §8 p.25 ·
  §9 p.27 · §10 p.28 · §11 p.33 · §12 p.42 · §13,a p.42 · §13,b p.47 · §14 p.56 ·
  §15 p.59 · §16 p.63 · §17 p.66 · §18 p.67 · §19 p.71 · §20 p.81 · §21 p.82.
  Body ends p.86. **Printer's slip:** two consecutive §§ both numbered 13; the Indhold
  lists them §13,a and §13,b (followed in both files).

## Book-specific conventions (differences from erkjendelse worth flagging)
- **Emphasis is BOLD Fraktur (Fett), not letterspacing** — already encoded as `\emph{}`
  throughout the transcription. Carry EVERY `\emph` span into the English as `\emph{}`
  (renders italic; same convention as erkjendelse). The transcription's whole-file
  count is **93 `\emph`** (incl. the `Anm.` run-in labels) — a per-batch parity check
  against the Danish is the main fidelity guard.
- **Latin → `\textit{}` (already tagged; keep).** Notable: the long **Wolff**
  definitions quoted in §13,a Anm.3 (*Philosophia est scientia possibilium, qvatenus
  esse possunt*, and the §17/§7/§31/§32/§37/§46 quotations — the print spells Latin
  *qu* as **qv**; keep it), the ***Scimus, qvia…*** series (§13,b Anm.2), plus
  *sensu eminenti* (§20), *Totum est parte sua prius* (§19), *a priori*, *de facto*,
  *eo ipso*, *prius*, French *c'est moi*. Translate the surrounding prose; leave the
  Latin. (Watch the playbook's rule: if any Latin were *letterspaced* it'd be `\emph`,
  but in this book the Latin is antiqua `\textit`, and the bold-Fett emphasis is Danish.)
- **German block-quotes are plain (Fraktur in the source), kept in `` ``…'' ``:**
  three Steffens quotes (§14 Anm.2 „Es giebt für das wahre Erkennen…"; §18 Anm.2 „Wie
  das Wissen speculativ wird…"; §19 Anm.5/Naturwissenschaft), Hegel's Encyklopädie §5
  „Die Philosophie wird hiemit…", Fichte's „Wissenschaftslehre"/„von den Thatsachen
  des Bewußtseyns", Kant's *Kritik der reinen Vernunft* / „Erkenntnißlehre" /
  „Metaphysische Anfangsgründe". Decide per the playbook whether to italicise German
  *titles* in English; keep quoted German *prose* in `` ``…'' `` quotes.
- **No real Greek** in this book (unlike erkjendelse). Only the transliterated
  „Dikaiosyne"/„Nemesis" (§18 Anm.6), set in Fraktur → plain; render as plain English
  words or keep as proper-ish terms.
- **Quotes:** Danish „…" → English `` ``…'' ``. **Em-dash** `---`. Section-break rules
  (`\begin{center}\rule…\end{center}`) reproduced at the same breaks (they close §2,
  §7, §14, §19, §20, §21 in the transcription).
- **Structure note:** the Danish uses centered `\S~N` heads + a centered title line,
  NOT `\section{}`/`\label{}`. Match markers by § number + page range; translate the
  title line together with that section's body.

## CURRENT RESUME POINT
**TRANSLATION COMPLETE — all 13 batches done (Preface, §§1–21, Rettelser note).**
`translation.tex` compiles clean under the sandbox substitute (Computer-Modern fallback:
**60 pp., 0 char-warnings, 0 errors**). Marker check: `grep -c "text to be added"` reports
**1**, which is the header comment on line 9 (the false positive) — **zero real markers
remain**; `grep -c "translation continues"` → 0.

**Whole-file emphasis parity verified:** Danish 93 `\emph` vs rendered English 95 — every
section matches exactly (per-section diff = 0 across Preface + §§1–21); the +2 is the
translator's-note's own two emphases (\emph{Translator's note.}, \emph{Rettelser}), which
are legitimately English-only since the Danish errata table is replaced by the note. (A
raw grep shows 97 because two \emph{} appear inside a *preamble comment* on line 18 — not
rendered.)

**Two harmless cross-reference quirks in the print (mirrored as-is, no change):** §18
body cites "\S~15, Anm.~4" and §18 Anm.4 cites "\S~5, Anm.~4," but neither §15 nor §5 has
a numbered Anm.4 in the print (both point to the moral-Idea / sympathetic-cognition
passages that sit where a "4" would fall — §5's is the unnumbered body paragraph between
its Anm.3 and Anm.5). Kept verbatim as Sibbern wrote them.

**German-title convention (set §13a, applied §13b):** German work-titles italicized in
English (\textit{Kritik der reinen Vernunft}, \textit{Wissenschaftslehre}, \textit{von den
Thatsachen des Bewußtseyns}, \textit{Encyklopädie}, \textit{Metaphysische Anfangsgründe}),
even where Sibbern set them plain or in „…". Quoted German *prose* takes `` ``…'' `` quotes
(the Hegel Encyklopädie §5 and Steffens "Naturwissenschaft a priori…" sentences carried so
this batch). Inline non-title German (Selbstverständigung, "als ein Wißthum") and the
Danish idiom "det er mig" kept plain, mirroring the source.

**OPEN FLAGS for Hans to verify against the copy:**
- **§5, p.15 "Diet" for "Det"** — print reads "Diet" where "Det" is expected ("…that
  which must guide and determine this our constituting becomes the foundation"). Not in
  the errata leaf; transcription keeps it as printed; English uses the sensible reading.
- **§10 Anm.3, p.31: real Greek ἀταραξία.** The transcription/notes said "no real Greek
  in this book," but Anm.3 ends with "the ἀταραξία of the mind." Carried verbatim
  (needs `textalpha`, which the preamble already has). Heads-up in case you'd expected
  none — the sandbox check substitutes it, the real file keeps the glyphs.

**DECISIONS LOCKED THIS BATCH (flagged to Hans — veto anytime):**
- **`Anm.` → "Note".** Used `\emph{Note~1.}` / `\emph{Note~2.}` / `\emph{Note~3.}` and
  bare `\emph{Note.}` (§2). This is the scaffold/glossary default; "Remark" is the
  alternative. Now applied consistently — say the word to switch and I'll global-swap.
- **Book/work titles in-text → `\textit{}` + Danish, bracket-glossed.** Preface:
  `\textit{Om Erkjendelse og Granskning} [On Cognition and Inquiry]`. §1 Anm.3:
  Sibbern's own `\textit{Logik}` (his 1822 Logik, cited "\S~35"). Note this adds one
  `\textit` beyond the Danish (which sets titles plain in Fraktur) — intentional English
  convention, tracked so the `\textit` parity count reads +1 per title.

Suggested batch plan (~10 pp. each; adjust at clean § boundaries):
b1 Preface · b2 §§1–2 · b3 §§3–4 · b4 §§5–7 · b5 §§8–10 · b6 §11 · b7 §§12–13a ·
b8 §13b · b9 §14–15 · b10 §16–17 · b11 §18 · b12 §19 · b13 §§20–21 + Rettelser note.

## Sandbox compile / verification recipe (English side)
Same as the playbook. The sandbox lacks `libertinus`; substitute and strip the
Greek/danish bits just for the check (do NOT put the substitutions in the real file):
```bash
cd /tmp && mkdir -p verify && cd verify
SRC="<path>/translation.tex"
sed -e 's/\\usepackage{libertinus}/\\usepackage{lmodern}/' -e '/libertinust1math/d' \
    -e '/textalpha/d' -e 's/\\usepackage\[english\]{babel}/\\usepackage{babel}/' "$SRC" > t.tex
# (this book has no real Greek, so no glyph substitution needed)
pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1; pdflatex … t.tex >l.txt 2>&1
grep -o 'Output written.*' l.txt
grep -ic 'not set up\|missing.*character' l.txt   # expect 0
```
NOTE: on THIS sandbox `lmodern` may be absent too — fall back to the transcription's
recipe (delete the libertinus/libertinust1math/textalpha lines, drop the microtype
options, map `[english]{babel}`→`{babel}`) to compile with Computer-Modern. Expect
0 char-warnings, 0 errors.

## DONE so far (don't redo)
- Scaffold + glossary + these notes created 2026-07-19.
- **Batch 1 — Preface (Fortale, PDF 8–9; transcription L83–111).** Single long
  paragraph + dated sign-off ("Copenhagen, the 28th of October 1843. Sibbern."). Emph
  parity vs Danish: 1 `\emph` (denne→\emph{this}) + 3 `\textbf` (NB, Copenhagen, Sibbern)
  all carried. Glossed on first use: science [Videnskab], propaedeutic of philosophy
  [Philosophiens Propædeutik], errata [Rettelser]; companion volume cited as
  `\textit{Om Erkjendelse og Granskning} [On Cognition and Inquiry]`. Closing section
  rule reproduced. Compile: 6 pp., 0/0.
- **Batch 2 — §§1–2 (Preliminary Remarks; transcription L119–297).** §1 "What is to be
  undertaken here…" (3 body paras + Notes 1–3); §2 "A survey of the whole course…"
  (body with inline run-in items 1)–5) kept inline, not a list + one final Note). Emph
  parity vs Danish exact: **11 = 11** `\emph` carried (incl. Note labels ×4 and the term
  emphases nature and essence/concept ×3, science/all-comprehending manner/existence/all
  things ×4). `\textit{initia}` (Latin) carried; `\textit{Logik}` added as title. New
  glossary terms fixed: Verdenstotalitet=world-totality, Grundanskuelse=fundamental view,
  Philosophiens Philosophie=the philosophy of philosophy, explicativ Philosophie. §2
  closing section rule already in scaffold. Compile (cumulative): 10 pp., 0/0.
- **Batch 3 — §§3–4 (Introductory Considerations; transcription L305–524).** §3
  "Philosophy is a) cognition" (the "is", objective/subjective opposition, the
  mediating/receiving vs. producing account + Notes 1–3, incl. the macrocosmic/microcosmic
  self-assertion analysis and the \textit{harmonia originaria} organism-passage); §4
  "Philosophy is b) intelligent and rational cognizing" (the move from immediate to
  mediated cognition via the spirit of inquiry). Emph parity exact: **9 = 9** (er→\emph{is},
  \emph{partly}×2, its truth, ought, all + 3 Note labels). Latin carried: \textit{scimus,
  qvia accepimus}, \textit{scimus, qvia facimus} (qv kept), \textit{harmonia originaria};
  applied errata already folded in the Danish (p.9 "ikke i sig selv", "Modsætningen" i-drop;
  p.14 Tilfredsstillelse). Title italics added (+3 \textit): companion vol. abbrev.
  \textit{Om Erkjend.\ og Granskn.}, \textit{Psychologie}, \textit{Psych., ny Udarb.}.
  New glossary terms fixed (see GLOSSARY): det Objective, Modsætning, Gjørensiggjeldende,
  Gyldighedstillæggelse, Sindshenvendelse, Videdrivt, Randsagelsesaand, Granskning/
  Efterforskning. Compile (cumulative): 15 pp., 0/0.
- **Batch 4 — §§5–7 (rest of Introductory Considerations; transcription L526–775).** §5
  "Continuation. What the intelligent cognizing aims at" (the two necessity-cases, the
  sympathetic/extrarational threefold division + Notes 1,2,3,5,6 — the print skips Anm.4,
  a body paragraph on sympathetic cognition sits between Anm.3 and Anm.5; mirrored as-is);
  §6 "Cognition as rational, working toward an ultimate foundation"; §7 "Philosophy is c)
  scientific cognition" (grounds→connection→system; the Idea/spirit-of-the-science, and
  the Idea/System/Detail reciprocity). Emph parity exact: **13 = 13** (at→\emph{that},
  hvad→\emph{which}, "with respect to the assumed content itself", bør→\emph{ought},
  \emph{Dr.}×2, + 7 Note labels [1,2,3,5,6 in §5; one each in §6, §7]). Latin carried:
  \textit{intellectus}, \textit{intelligere}, \textit{ratio}, \textit{rationes}, the two
  Bojesen dissertation titles (\textit{de harmonica scientia Græcorum}, \textit{de tonis
  s.\ harmoniis Græcorum}). Title/journal italics added (+6 \textit): \textit{Psych., ny
  Udarb.}, \textit{Maanedskr.\ f.\ Liter.}×2, \textit{Om Erkj.\ og Gr.},
  \textit{Pathologie}, \textit{Om Erkj.\ og Granskn.}. p.15 "Diet" oddity flagged above.
  New glossary terms: Styrelse, sympathetisk/extrarationale, ratio/rationes, Methode,
  Totalerkjendelse. Compile (cumulative): 21 pp., 0/0.
- **Batch 5 — §§8–10 (start of "The Propaedeutic Concept…"; transcription L785–1014).**
  §8 "Philosophy aims d) at an all-comprehending fundamental cognition. The subjective
  principal task"; §9 "The objective principal task. ---Philosophy aims e) at the ultimate
  grounds of existence"; §10 "A propaedeutic definition of philosophy" (the first
  definition, the subjective task subsumed under the objective, + Notes 1–5 on
  subjective-idealism, Locke, Greek/Hume skepticism, Kant/Fichte, and the fallen-reason
  caveat). Parity exact: **\emph 5 = 5** (all five Note labels; no in-body emphases this
  span), **\textit 4 = 4** (rationes cognoscendi, universam cognoscendi rationem ×2 [Anm.2
  + §8], universa ratio cognoscendi), **Greek 1 = 1** (ἀταραξία). No title italics this
  batch. Videnskabslære rendered "Doctrine of Science [Videnskabslære]" (Sibbern's Danish
  calque of Fichte's Wissenschaftslehre). Applied errata already folded (p.31 "altomfattende
  Maade" NB, "objective" for "opjective"; p.33 "Begrebet Philosophie" NB). Compile
  (cumulative): 27 pp., 0/0.
- **Batch 6 — §11 (long single section; transcription L1016–1263).** "Philosophy steps
  up to what is otherwise given" — the four numbered spheres of the Given (1 outer
  experience/empirical; 2 a priori construction/mathematics; 3 inner psychical observation
  = explicative philosophy, subdivided a psychology, b reflection-philosophy, c philosophy
  of the Idea; 4 history of philosophy) + Notes 1–9 (mathematics vs. explicative philosophy;
  mixed and intermediate sciences; the Schmidten and Treschow references). Emph parity
  exact: **12 = 12** (Note labels 1–9 + \emph{consciousness's own facts}, \emph{a priori
  that constitutes…}, \emph{we}). Latin \textit 3 (a priori, de facto ×2); +2 title italics
  (\textit{Om Mathematikens Væsen} — Schmidten; \textit{Om Philos.\ Natur og Dele} —
  Treschow). Applied errata folded (p.35 comma, p.39 Teleologie-for-Theologie NB, p.40 "de
  historiskt givne Sprog" NB, p.41 "en vis Stat"). Re-flag: p.38 "dettte" (triple-t) typo
  kept as printed (known RESUME-NOTES flag), translated normally as "this". New glossary
  terms: speculativ/constitutiv, Reflexionsphilosophie, Ideephilosophie, det Givne,
  Ideologie, positiv Theologie/Jurisprudents. Compile (cumulative): 32 pp., 0/0.
- **Batch 7 — §§12–13a (transcription L1265–1416).** §12 "Exposition of the given
  concept of philosophy: three chief points of view" (I/II/III); §13,a "Exposition… in
  the first chief respect" (philosophy as fundamental cognition a–g: calling-to-account,
  the riddle of existence, the possibility of the actual, overcome dubitation,
  Selbstverständigung, orientedness, satisfaction) + Notes 1–3 (Kant's synthetic-a-priori
  question; Fichte's Wissenschaftslehre; and the long **Wolff** Discursus note). Emph
  parity exact: **3 = 3** (only the three Note labels; no in-body emphasis). **All 26
  Danish Latin \textit carried verbatim** with the print's qv-for-qu (the Wolff §6/§7/§17/
  §29/§31/§32/§37/§46 quotations, cognitio philosophica/historica, natura rationalis,
  possibilia, actum conseqvi possit, a priori ×3, de facto). English \textit = 34: the 26
  Latin + 8 italicized titles (Om Erkj. og Gr., Kritik der reinen Vernunft, Wissenschafts-
  lehre ×2, von den Thatsachen des Bewußtseyns, Critique, Discursus [short ref], Wolff's
  Logik). Wolff spelled "Wolff" per glossary (source: "Wolf"); errata p.43 "Jacobi" folded.
  Compile (cumulative): 36 pp., 0/0.
- **Batch 8 — §13,b (long; transcription L1418–1638).** "Exposition of the concept in the
  second chief respect" — the coming-together into unity of objective and subjective;
  philosophy as constitutive construction \textit{a priori} in force of full reason; the
  fundamental Idea as the all-determining prius; astronomy as the model of a priori
  construction. Notes 1–4 (ideal beholding / John 7:17; the Scimus-qvia series; Hegel's
  Encyklopädie §5 def. + the unity of thinking and being; the construction-a-priori
  clarification). The back half of the section is all petit (`{\small}`), mirrored. Emph
  parity exact: **4 = 4** (only the four Note labels). **All 32 Danish Latin \textit
  carried** (Scimus-qvia series ×8, eo ipso ×4, prius ×4, a priori ×many, sumus, c'est
  moi). English \textit 34 = 32 + 2 German titles (\textit{Encyklopädie}, \textit{Metaphysische
  Anfangsgründe}). John 7:17 rendered in English `` ``…'' ``; Hegel + Steffens German quotes
  kept in German inside `` ``…'' ``. Danish idiom "det er mig" kept plain. Errata p.54 "saa
  meget" folded. Compile (cumulative): 41 pp., 0/0.
- **Batch 9 — §§14–15 (transcription L1640–1824).** §14 "Exposition of the concept in
  the third chief respect" (philosophy → speculative cosmology → theology → the Godhead;
  the all-constitutive as eternal/infinite, the finite as moment; + Notes 1–3 incl. the
  Steffens \textit{Grundzüge} quote and the "cycle of definitions of philosophy"); §14's
  closing section-break rule was NOT in the scaffold — **added** before the group head.
  §15 "The philosophical fundamental Idea" (opens the "Foundation of Philosophy" group;
  the a priori speculative Idea that meets the Given, the moral-Idea analogy, the sporadic
  and life-dialectic + Notes 1–3). Emph parity exact: **8 = 8** (6 Note labels + \emph{cycle
  of definitions of philosophy} §14, \emph{They} §15). No Danish Latin; English \textit 3 =
  italicized titles (\textit{Grundzüge der philos.\ Naturwiss.}, \textit{Philos.\ Arch.\ og
  Repert.}, \textit{Psychologie, ny Udarbeidelse}). German prose quotes (Steffens "Es giebt
  für das wahre Erkennen…") in `` ``…'' ``; Danish "Saa og saa er det…" in `` ``…'' ``. Errata
  p.60/p.61 comma-insertions folded. Compile (cumulative): 45 pp., 0/0.
- **Batch 10 — §§16–17 (transcription L1826–1940).** §16 "Wherein the philosophical
  fundamental Idea has its foundation" (the Idea must affirm itself in the all-comprehending
  discussion; philosophy does not \emph{build} on faith/experience but on what sets them in
  the right light; Notes 1–2 + the bracketed synthetic-unity passage); §17 "How philosophy
  comes about. ---a) Explication in speculative tendency" (explicative logic + ontology as
  the most fundamental part). Emph parity exact: **7 = 7** (2 Note labels + \emph{build}
  [bygge] ×5). No Latin, no German quotes this span; textit 0 = 0. Danish "Jøvrigt" (=
  Iøvrigt) rendered "For the rest". Compile (cumulative): 48 pp., 0/0.
- **Batch 11 — §18 (transcription L1942–2033).** "b) Speculation and dialectic in
  essential unity" — the transition to speculative philosophy proper; speculation (=
  spirit of the science) and dialectic defined; Notes 1–6 (references; the Steffens "Wie
  das Wissen speculativ wird…" quote; the mystical/sophistry/Parmenides typology; Plato
  and poetic breakthrough; Dogmatism vs. Kant's Criticism, opposite = dialectic; the
  dialectic of life as Dikaiosyne/Nemesis). Emph parity exact: **7 = 7** (\emph{essential
  unity of speculation and dialectic} + 6 Note labels). No Danish Latin; English \textit 4
  = titles (\textit{Om Erkj.\ og Gr.}, \textit{Philos.\ Arch.\ og Repert.}, \textit{Logik},
  \textit{Grundzüge der philos.\ Naturwiss.}). Steffens German quote in `` ``…'' ``;
  Dikaiosyne/Nemesis plain roman (not real Greek). Errata p.75 "Tilværelsessphære" (in the
  §19 span, folded next batch). Compile (cumulative): 50 pp., 0/0.
- **Batch 12 — §19 (long; transcription L2035–2281).** "Philosophy's stepping-out into
  c) a philosophical system" — the organic system vs. mathematical stringency; the disputes
  among philosophers; the projected division (Fundamentalphilosophie → ontology → nature →
  spirit → logic/philosophy-of-philosophy → aesthetics/morals/religion → state & church &
  immortality); the long rebuttal of the "presuppositionless beginning" (contra Hegel's
  objective/subjective Logic); and philosophy's right to engage Christianity (Anm.7). §19's
  closing section-break rule was NOT in the scaffold — **added** before the §20 group head.
  Emph parity exact: **7 = 7** (all seven Note labels; no in-body emphasis). Latin \textit 2
  carried (\textit{Totum est parte sua prius}, \textit{a priori}); English \textit 11 = 2 +
  9 italicized titles (Om Mathematikens Væsen, Kritik der reinen Vernunft, Critique, Om
  Erkj.\ og Gr., Bemærkn.\ og Undersøg.\ betreffende Hegels Philosophie, Maanedskr.\ f.\
  Literatur, Philosoph.\ Archiv, Theologische Zeitschrift, Christendomsphilosophie). German
  „Erkenntnißlehre" kept in `` ``…'' ``; Hegel's "objective and subjective Logic" descriptive
  (no italics). Errata p.75 "Tilværelsessphære", p.80 "Philosophiens" folded. Compile
  (cumulative): 56 pp., 0/0.
- **Batch 13 (final) — §§20–21 + Rettelser note (transcription L2290–2488).** §20 "Final
  definition of philosophy" (the run-in \emph{Philosophy} definition + Note with
  \textit{sensu eminenti}); §21 "Philosophy on a level with the empirical and the
  suprarational…" (philosophy as one power among several; empiricism/suprarationalism;
  the closing movement to the realms of truth → beauty/poetry → the good → love and
  holiness; Notes 1–4, incl. the Philos. Arch. quotation and the reply to Hegel's claim
  of supremacy). §20 and §21 closing rules were NOT in the scaffold — **added** (0.18 after
  §20, 0.28 after §21). Emph parity exact: §20 **2 = 2**, §21 **4 = 4**. Latin \textit
  carried (\textit{sensu eminenti}); §21 title-italic \textit{Philos.\ Arch.}. **Rettelser:**
  resolved per the erkjendelse policy — a `\footnotesize` italic *Translator's note* (after
  a centred rule) explaining the errata concern only Danish orthography (already folded into
  the transcription) and noting the printer's double-§13 slip that the a/b split follows.
  Compile (cumulative, final): **60 pp., 0/0**.

## FINISH CHECKLIST STATUS
1. Rettelser note — **DONE** (translator's note rendered, erkjendelse-style).
2. `catalog.yaml` id `philosophiens-begreb` — **status flipped to `complete`**, note updated
   to "English translation complete," Translation link added (mirrors erkjendelse). *(Link
   resolves once Hans pushes translation.pdf to the GitHub Pages site.)*
3. **Awaiting Hans:** compile both PDFs locally with the REAL fonts (libertinus +
   libertinust1math + textalpha), confirm 0/0 and that the Transcription + Translation links
   resolve, then commit/push. The one real Greek glyph (ἀταραξία, §10 Anm.3) needs textalpha
   — it renders on the real machine; the sandbox substitutes it only for the compile check.

## Finish checklist (mirror erkjendelse)
1. Resolve the Rettelser note (render one-line translator's note, or omit).
2. `catalog.yaml` id `philosophiens-begreb`: flip the section `status:` to `complete`
   and update the note to "English translation complete."
3. Hans compiles both PDFs locally with the REAL fonts (libertinus + libertinust1math
   + textalpha), confirms 0/0 and that the Transcription + Translation links resolve,
   then commits/pushes.

## Conventions
See `../../../TRANSLATION-PLAYBOOK.md` for the standing method and LaTeX conventions.
Book-specific vocabulary: `GLOSSARY.md`. Companion model: `../erkjendelse/`.
