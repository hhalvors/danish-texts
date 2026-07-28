# Sibbern — *Om Philosophiens Begreb, Natur og Væsen* (1843): transcription resume notes

Hand-off for continuing in a **fresh session**. Work in batches of ~10 pages,
then compile + give a short report. Companion to *Om Erkjendelse og Granskning*
(1821/22) — the Fortale explicitly relates the two; the vocabulary and §-style
match. Reuse the *erkjendelse* conventions.

## Goal
Faithful LaTeX transcription (Danish, Fraktur) of the whole book, then an
English translation. Files in `texts/sibbern/philosophiens-begreb/`:
- `transcription.tex` — active Danish file (book class). **Source of truth.**
- `translation.tex` — English; NOT YET STARTED (Phase 2).
- Source scan: `~/bibliotek/Sibbern, Frederik/om-philosophiens-begreb.pdf`
  (KB scan, 101 PDF pp.; physical extent [6], 86 s.).
- Catalog entry: `catalog.yaml`, id `philosophiens-begreb`, status in-progress.

## PAGE MAP
- **Body (arabic): printed page = PDF page − 11.** (§ 1 opens printed p.1 = PDF 12.)
- Title page = PDF 6; Fortale = PDF 8–9; Indhold (TOC) + Rettelser = PDF 10–11.
- Body runs printed pp. 1–86 = PDF 12–97.

## SECTION → PAGE MAP (from the Indhold, PDF 10–11)
Group headings (centered bold rubrics, appear in the body too):
- **Foreløbige Bemærkninger** — §1 (p.1), §2 (p.4)
- **Indledende Betragtninger. Om Erkjendelse i Almindelighed** — §3 (p.7),
  §4 (p.12), §5 (p.15), §6 (p.21), §7 (p.22)
- **Propædeutisk Begreb om Philosophie og sammes Exposition** — §8 (p.25),
  §9 (p.27), §10 (p.28), §11 (p.33), §12 (p.42), §13.a (p.42), §13.b (p.47),
  §14 (p.56)
- **Philosophiens Grundlag og dens Værk** — §15 (p.59), §16 (p.63), §17 (p.66),
  §18 (p.67), §19 (p.71)
- **Fuldelig Bestemmelse af Philosophiens Begreb** — §20 (p.81)
- **Philosophien som Led og Moment i den hele aandelige Leven** — §21 (p.82)

NB (author's own): two consecutive §§ both got numbered 13 by a printer's
slip; the Indhold lists them as § 13, a and § 13, b (followed here).

## RETTELSER (errata leaf, PDF 11) — POLICY
Unlike the *Erkjendelse* errata (pure Danish orthography), several here are
**substantive** and the author asks that especially the NB ones be noted.
Apply the NB corrections to the Danish body as each page is transcribed, and
drop a `% Rettelse` note at each site. Key NB items:
- p.9,  l.28  — for "ikke i selv" read "ikke i **sig** selv"
- p.33, l.4   — Begrebets → **Begrebet**
- p.39, l.17–18 — for **Theologie** read **Teleologie**
- p.40, l.18  — for "det" read "de"
- p.60, l.19  — insert comma after "Enkeltheder"
Non-NB (orthography/spacing) items: p.14, 18, 24, 25, 26, 30, 31, 35, 41, 43,
54, 61, 75, 80 — apply silently. (Full list still to be transcribed verbatim
into the `% Rettelser` block at the end of transcription.tex.)

## CONVENTIONS (same as erkjendelse/brøchner)
- Preamble: libertinus + libertinust1math + textalpha + `[danish]{babel}`.
- „…" / »…« → keep Danish as printed in the transcription (quotes converted
  only in the *translation*). Em-dash `---`. Section-break ornament → a short
  centered `\rule`.
- **Emphasis (letterspacing / Sperrung) → `\emph{}`.** Preserve every span;
  parity is checked against the Danish per batch.
- Latin → `\textit{}` (e.g. `\textit{initia}`). Greek glyphs verbatim (textalpha).
- "Anm. 1./2./3." remarks are set in petit in the original → wrapped in
  `{\small … \par}` with an `\emph{Anm.~N.}` run-in label.
- Group headings via the `\grouphead{}` macro defined in the preamble.

## SANDBOX COMPILE (this session's mount is session-specific: `ls /sessions/*/mnt/`)
Substitute lmodern for libertinus, strip libertinust1math/textalpha, and map
`[danish]{babel}`→`{babel}`; replace any Greek with `[Gr]` (see the erkjendelse
RESUME-NOTES recipe). Do NOT put these substitutions in the real file.

## CURRENT RESUME POINT
**Batch 1 DONE:** preamble + title page + **Fortale** (PDF 8–9) + **§§ 1–2**
(printed pp. 1–6). Full §-skeleton with page markers laid in for §§ 3–21.
Verified sandbox compile: **10 pp., 0 errors, 0 char-warnings, 12 `\emph{}`.**
- ⚠️ Emphasis in batch 1 was marked conservatively from 200-dpi images. A
  dedicated **400-dpi emphasis-parity pass** over pp. 1–6 is still owed, and
  the verbatim Rettelser block is still to be added.

**Batch 2 DONE (2026-07-19):** **§§ 3–4** (printed pp. 7–14 = PDF 18–25),
image-verified page by page at 320 dpi (targeted 400-dpi crops for emphasis).
Stopped at the §5 boundary (8 pp., a touch under the ~10-pp. target but on a
clean section break). Verified sandbox compile (Computer-Modern substitute —
this sandbox lacks lmodern; also had to drop `microtype`, bitmap CM can't do
font-expansion): **15 pp., 0 errors, 0 char-warnings, 21 `\emph{}`.**
- **Emphasis in THIS book is BOLD Fraktur (Fett), not letterspacing.** Confirmed
  against a batch-1 `\emph` span ("altomfattende", p.5 = bold in print). Encoded
  as `\emph{}` per the established convention — no new macro. Batch-2 bold spans:
  §3 `er`, `deels`×2; §4 `sin Sandhed`, `bør`, `al`. (Some batch-1 `\emph`, e.g.
  "Videnskab"/"Maade", look normal-weight in print — over-marked; the owed parity
  pass should re-check batch 1 for bold-vs-normal, not just letterspacing.)
- Quotes render as Danish `„…"`; Latin phrases (scimus qvia accepimus / facimus,
  harmonia originaria) in `\textit{}`; `cfr.` left upright (not italicised).
- **Dittography flagged, kept as printed:** p.8 prints "i Eet og og Alt" ("og"
  repeated across the line break); NOT in the errata leaf → kept, with a % note.

**ERRATA — full leaf now transcribed (PDF 11).** The leaf's NB markers sit next
to: p.27 (altomfattende→altomfattende Maade), p.33 (Begrebets→Begrebet),
p.39 (Theologie→Teleologie), p.40 (det→de), p.60 (comma after Enkeltheder).
NOTE: the leaf does **NOT** NB-mark the p.9 items (RESUME's earlier summary
labelled p.9 l.28 "NB" — that was a mis-catalogue). Full list:
```
p.9  l.26  bortfalder Ordet i.          (delete the word "i")
p.9  l.28  "ikke i selv" → "ikke i sig selv"
p.14 l.28  Tilfredsstillelelse → Tilfredsstillelse
p.18 l.3   Tredelig → Tredeling
p.24 l.13  snaledes → saaledes
p.25 l.11  bemærkede → Bemærkede
p.26 l.16  det → Dette
p.30 l.17  bestemt → Bestemt
p.31 l.26  opjective → objective
NB p.—  l.27  altomfattende → altomfattende Maade   (belongs with p.31 block)
NB p.33 l.4   Begrebets → Begrebet
p.35 l.20  udslettes Kommaet
NB p.39 l.17–18 Theologie → Teleologie
NB p.40 l.18  det → de
p.41 l.14  hvis → vis
p.43 l.24  Jakobi → Jacobi
p.54 l.20  saameget → saa meget
NB p.60 l.19  sæt Komma efter Enkeltheder
p.61 l.15  (comma) efter spørges
p.75 l.15  læs: Tilværelsessphære
p.80 l.13  Philosophiens
```
Plus author's tail notes: the double-§13 slip (§13,a / §13,b, already followed),
and a self-correction to his *Psychologie, ny Udarb.* p.133 (umiddelbare→middelbare).
**Applied so far:** p.9 l.26 (deleted "i"), p.9 l.28 (+"sig"), p.14 l.28
(→Tilfredsstillelse). Each site carries a % Rettelse note in transcription.tex.
The verbatim Rettelser block at end-of-file is still a to-do (the list above is
ready to drop in).

**Batch 3 DONE (2026-07-19):** **§§ 5–7** (printed pp. 15–24 = PDF 26–35),
image-verified page by page at 320 dpi. Verified sandbox compile (CM substitute):
**21 pp., 0 errors, 0 char-warnings, 34 `\emph{}`, 12 `\textit{}`.**
- §5 and §7 **interleave normal body with petit Anmærkninger** (confirmed by
  glyph-size crops, not just line counts): §5 = body / Anm.1–3 / body / Anm.5–6 /
  body; §7 = body / Anm / body. §6 = body + one Anm. Anm.\ blocks wrapped in
  `{\small … \par}` with `\emph{Anm.~N.}` run-in labels.
- Latin in `\textit{}`: intellectus, intelligere, ratio, rationes, and the two
  antiqua dissertation titles \textit{de harmonica scientia Græcorum} /
  \textit{de tonis s. harmoniis Græcorum}. Bold `\emph{}` spans: §5 `at`, `hvad`,
  `Henseende til selve det Antagne`, `bør`; and \emph{Dr.} (the abbreviation is
  bold Fett in the Bojesen citation, p.19).
- **Errata applied:** p.18 l.3 Tredelig→Tredeling (silent, in Anm.5); p.24 l.13
  snaledes→saaledes (with a % note). Both non-NB.
- **⚠ FLAG for the scholar (p.15):** print reads “Diet for Det, som maa lede og
  bestemme denne vor Constitueren” — “Diet” (cap D, dotted i, e, t) is
  semantically odd in Danish and is NOT in the errata; transcribed as printed
  with a % FLAG. Please verify against your copy (possible mis-set word).
- Minor judgment call: §5 Anm.6 quotes his own title as „om Erkj.\ og Gr.“ with
  the closing quote after “Gr.” (the printed closing mark is faint); “i Anm.\ til
  §4, Pag.\ 32–36” left outside the quote, matching the p.8 precedent.

**SANDBOX-STAGING GOTCHA (for next session):** re-staging the SAME device path
(`transcription.tex`) served a STALE cached copy at `/mnt/user-data/uploads/...`
(old bytes, old content) even though `device_stage_files` reported the new size.
Workaround that worked: `device_bash cp transcription.tex transcription_sbx.tex`,
stage the **fresh-named** copy, compile that, then `mv` the copy into
`_to_delete/`. (A leftover `_to_delete/transcription_sbx.tex` is in the book
folder — Hans can delete that folder.)

**Batch 4 DONE (2026-07-19):** **§§ 8–10** (printed pp. 25–32, +§10's Anm.\ tail
on p.33 = PDF 36–44), image-verified page by page. §10's Anmærkninger run long
(Anm.1 pp.29–31, all petit; the whole §10 = body / Anm.1–5). Verified sandbox
compile (CM substitute): **26 pp., 0 errors, 0 char-warnings, 39 `\emph{}`,
16 `\textit{}`.** First **Greek** of the book: ἀταραξία (p.32, end of §10 Anm.3).
- No bold-Fett spans in this stretch; the 5 new `\emph` are all Anm.\ labels.
  Latin `\textit{}`: rationes cognoscendi, universam cognoscendi rationem (×2),
  universa ratio cognoscendi.
- **Errata applied.** NB (with % notes): p.31 l.27 altomfattende→altomfattende
  Maade (a reader's pencil “Maade” in the scan margin confirms it), p.33 l.4
  Begrebets→Begrebet. Non-NB (silent): p.25 l.11 bemærkede→Bemærkede (“det i
  §1 Bemærkede”), p.26 l.16 det→Dette (“uagtet Dette”), p.30 l.17 bestemt→Bestemt
  (“noget vist Bestemt”), p.31 l.26 opjective→objective.

**STAGING GOTCHA — use a UNIQUE temp name EACH batch.** The mount caches by path,
and it also caches a reused temp name. Batch 4 first reused `transcription_sbx.tex`
(cached from batch 3) and compiled STALE bytes again. Fix: `cp transcription.tex
transcription_sbx_bN.tex` with a **fresh N** each time, stage that, compile, then
`mv` it into `_to_delete/`. (Leftovers now in `_to_delete/` — Hans can delete the
whole folder.)

**Batch 5 DONE (2026-07-19):** **§ 11** (printed pp. 33–41 = PDF 44–52),
*Philosophien træder det ellers Givne imøde. — Overblik over Indbegrebet af alt
dette* — image-verified page by page (300-dpi OCR crib + 400-dpi crops for
emphasis/errata). Covers the four-fold overview of the "Sphærer" of the Givne
(1) empirisk / 2) apriorisk-Construction / 3) den explicative Philosophies Gebeet
[a) Psychologie/Ideologie, b) Reflexionsphil./Logik+Ontologie, c) explicativ
Ideephil.] / 4) Philosophiens Historie) + Anm.~1–9. Verified sandbox compile
(Computer-Modern substitute; libertinus/lmodern absent, microtype dropped):
**32 pp., 0 errors, 0 char-warnings; whole-file 51 `\emph{}`, 19 `\textit{}`.**
- **Bold-Fett emphasis (this book's "emph"):** confirmed at 400 dpi — §11 has just
  three prose bold spans, all in Anm.: `\emph{Bevidsthedens egne Kjendsgjerninger}`
  and `\emph{Bevidsthedslivet selv constituerende Aprioriske}` (Anm.1, the
  Logik/Ontologie contrast, p.38), and `\emph{vi}` in „saa bør \emph{vi} det;" (Anm.3,
  p.39). The p.40 Anm.7 words "Mellemled"/"synthetiske Eenheder" look heavier at first
  glance but are NORMAL weight (checked) — not marked. The other nine new `\emph` are
  the Anm.~1–9 run-in labels.
- Latin in `\textit{}`: `a priori` (item 2, p.34), `de facto` ×2 (item 3a, p.35).
  No Greek in this stretch.
- **Errata applied (all four in-range):** NB p.39 l.17–18 Theologie→**Teleologie**
  (fits „det Nyttige" in Treschow's parallel list; a reader's pencil correction sits
  in the scan margin beside the word — corroborates); NB p.40 l.18 det→**de** („af de
  historiskt givne Sprog", plural); non-NB p.35 l.20 delete comma after „Forfølgen";
  non-NB p.41 l.14 hvis→**vis** („i en vis Stat"). Each carries a % Rettelse note.
- **FLAG for the scholar (p.38):** print reads „hvori **dettte** Aprioriske" —
  triple-t, an apparent printer's typo, NOT in the errata leaf; kept as printed with a
  % FLAG. (The „Dette vel kan siges" a line earlier is the normal cap-D word.) Please
  verify against your copy.
- §11 ends cleanly at the foot of p.41 (end of Anm.9, „…haves for Øie."); PDF 53 =
  p.42 opens directly with § 12.
- Housekeeping: `_to_delete/` (batch 3–4 sandbox leftovers) deleted. The repo is now
  mounted directly, so this session read/edited/compiled in place — no device staging,
  so the stale-cache gotcha did not apply. Fraktur+dan tesseract crib rebuilt per the
  Brøchner recipe (`/tmp/tessdata`; models don't persist — rebuild each session).

**Batch 6 DONE (2026-07-19):** **§ 12 + § 13,a + § 13,b** (printed pp. 42–56-top =
PDF 53–67-top), image-verified page by page (300-dpi OCR crib + 400-dpi crops for the
Latin, the German quotes, the errata, and glyph-size checks). §12 (three
Hovedsynspuncter), §13,a (a–g exposition + Anm.1–3, incl. the long **Wolff** Latin in
Anm.3), §13,b (a–d exposition + Anm.1–4). Verified sandbox compile (Computer-Modern
substitute): **40 pp., 0 errors, 0 char-warnings; whole-file 58 `\emph{}`, 77
`\textit{}`.**
- **NO bold-Fett Danish emphasis anywhere in §§12–13,b** (checked at 400 dpi). The 7
  new `\emph` are all the Anm.~1–3 / Anm.~1–4 run-in labels. This stretch's markup is
  almost all foreign-language, not emphasis.
- **Latin → `\textit{}` (58 new spans).** The heavy ones: Wolff's definitions quoted
  at length (§13,a Anm.3, pp.45–47: *Philosophia est scientia possibilium, qvatenus
  esse possunt*, the §17/§7/§31/§32/§37/§46 quotations, etc.) and the *Scimus, qvia…*
  series (§13,b Anm.2, pp.49–50). Also *a priori* (many), *eo ipso*, *prius*, *de
  facto*, *natura rationalis*, *possibilia*, French *c'est moi*. **Orthography kept as
  printed:** Wolff/Sibbern spell Latin *qu* as **qv** (qvatenus, qvæ, qvia, conseqvi,
  qvodsi…) — verified on the page, incl. the *scimus qvia* series (OCR misreads some
  as "quia"; the print is uniformly **qvia**). The print sets these Latin quotations in
  antiqua (mostly upright, some words italic); per the project convention all Latin is
  folded to a single `\textit{}` (italic) — Wolff's internal upright/italic alternation
  is not separately reproduced.
- **German → plain (Fraktur in the source, so no `\textit`), keeping „…" quotes:**
  Kant's *Kritik der reinen Vernunft*, Fichte's *Wissenschaftslehre* / „von den
  Thatsachen des Bewußtseyns" / *als ein Wißthum* (§13,a Anm.2), Hegel's Encyklopädie
  §5 „Die Philosophie wird hiemit für die Wissenschaft der Vernunft ausgegeben…"
  (§13,b Anm.3), Steffens „Naturwissenschaft *a priori* ist der Tod aller
  Naturphilosophie" and Kant's „Metaphysische Anfangsgründe" (§13,b Anm.4). NB: only
  the embedded Latin *a priori* inside the Steffens line is antiqua → `\textit`.
- **Errata applied (both in-range):** p.43 l.24 Jakobi→**Jacobi** („som Jacobi kaldte
  det", §13,a); p.54 l.20 saameget→**saa meget** („komme vi saa meget mere", §13,b
  Anm.4). Each carries a % Rettelse note.
- **Anmærkning size confirmed by 400-dpi glyph crops:** all Anm.\ here are **petit**
  (`{\small}`), same as §§1–11 — incl. the long §13,b **Anm.4** (pp.51–56), which is
  petit throughout (verified smaller than the §14 body on p.56). Multi-paragraph Anm.\
  are split into separate `{\small …\par}` blocks, label only on the first (project
  precedent).
- **Boundary:** §13,b actually completes at the **top of p.56** (through „…komme vi til
  at tale længere hen i § 15 og 16."), immediately before the § 14 heading — the batch
  extends to there for a clean cut. Bridge verified: p.55 ends „…i sin Gyldighed. Og
  herved bliver da at be-" / p.56 „-mærke, at denne Grundidee…".

**Batch 7 DONE (2026-07-19):** **§ 14 + § 15 + § 16** (printed pp. 56–66-top =
PDF 67–77-top), image-verified page by page (300-dpi OCR crib + 400-dpi crops for
emphasis and glyph-size checks). §14 (third Hovedsynspunct → speculativ Kosmologie +
Theologie; ends the *Propædeutisk Begreb* group with a section-break rule), then the
group **Philosophiens Grundlag og dens Værk** opens: §15 (den philosophiske
Grundidee) and §16 (hvori den har sit Grundlag; the Tro-vs-speculativ-Philosophie
discussion). Verified sandbox compile (Computer-Modern substitute): **47 pp., 0
errors, 0 char-warnings; whole-file 73 `\emph{}`, 77 `\textit{}` (no new Latin this
batch).**
- **Bold-Fett Danish emphasis (checked at 400 dpi):** `\emph{Cyklus af Definitioner
  paa Philosophie}` (§14 Anm.3, p.58); `\emph{De}` (§15 Anm.3, p.63, in the bracketed
  „[Hvad vi kalde Kræfter i Naturen…]" passage); and **five** `\emph{bygge}` in §16's
  faith-discussion (p.65 „ei \emph{bygge} paa Erfaring", „maa \emph{bygge} paa Tro";
  p.65/66 „Philosophien \emph{bygge} paa Tro"; p.66 „ikke \emph{bygge} paa Troen",
  „maa \emph{bygge} paa Det") — Sibbern pointedly emphasizes whether philosophy may
  *build* on faith. The other 8 new `\emph` are the Anm.\ run-in labels (§14 Anm.1–3,
  §15 Anm.1–3, §16 Anm.1–2).
- **German quotes → plain (Fraktur in source), „…" kept:** two Steffens quotes —
  §14 Anm.2, p.58 „Grundzüge der philos.\ Naturwiss." Pag. 3: „Es giebt für das wahre
  Erkennen kein endliches Ding; … in welcher es aber mit diesem eins ist." No Latin
  spans in this batch; „a priori"-type words here are Danish „apriorisk"/„aprioriske"
  (Fraktur), left plain — only standalone antiqua Latin gets `\textit`, and there is
  none in §§14–16.
- **Errata applied (both NB, both in §15):** p.60 l.19 insert comma after
  „Enkeltheder" (a reader's pencil slash marks the spot in the scan); p.61 l.15 insert
  comma after „spørges". Each carries a % Rettelse note.
- **Anm.\ size (400-dpi crops):** all Anm.\ petit as usual. §16 is body → Anm.1 (petit)
  → Anm.2 (petit, the §5-cross-ref remark) → **body resumes** (full size) for the whole
  Tro/Philosophie discussion (verified: p.66 Tro text == §17 body size, both full).
  The two bracketed „[…]" asides are in-line (§15 Anm.3 bracket is petit; §16 closing
  bracket is full body).
- **Boundary:** §16 ends at the foot of p.66 („…i § 21, til at tale nærmere.]" — a
  single closing „]", the OCR's „])" was a misread), immediately before the § 17
  heading, which shares p.66. Clean cut there.

**Batch 8 DONE (2026-07-19):** **§ 17 + § 18** (printed pp. 66–71-top = PDF 77–82-top),
image-verified page by page. §17 (a) Explication i speculativ Tendents — short, body
only, no Anm.) and §18 (b) Speculation og Dialektik i væsentlig Eenhed — body + Anm.1–6).
Verified sandbox compile (Computer-Modern substitute): **49 pp., 0 errors, 0
char-warnings; whole-file 80 `\emph{}`, 77 `\textit{}` (no new Latin this batch).**
- **Bold-Fett (400 dpi):** one prose span — `\emph{væsentlig Eenhed af Speculation og
  Dialektik}` (§18 body, p.67–68). The definitional „Ved Speculation…"/„Ved Dialektik…"
  terms and the Anm.\ key-words (Dogmatismus, Kriticismus, Stringents/Fluiditet, det
  Mystiske) are all NORMAL weight — not marked. The other 6 new `\emph` are the §18
  Anm.1–6 run-in labels.
- **German → plain (Fraktur), „…" kept:** a second Steffens quote — §18 Anm.2, p.69
  „Grundzüge der philos.\ Naturwiss.", Pag. 36: „Wie das Wissen speculativ wird durch
  die Anschauung der Universalität, so wird die Speculation wissenschaftlich durch die
  Anschauung der Individualität." **No Latin `\textit` in this batch.** The two
  transliterated-Greek terms „Dikaiosyne"/„Nemesis" (§18 Anm.6, p.71) are set in Fraktur
  in the source → left plain (not antiqua, so no `\textit`).
- **No leaf errata in this range** (pp.66–70). All Anm.\ petit as usual.
- **Boundary:** §18's Anm.6 spills onto p.71 and completes there („…en Livets
  Dikaiosyne, en Livets Nemesis."), immediately before the § 19 heading — batch extends
  to that point for a clean cut.

**Batch 9 DONE (2026-07-19):** **§ 19** (printed pp. 71–80 = PDF 82–91),
*Philosophiens Udtræden i c) et philosophiskt System* — image-verified page by page.
Structure: one full-size body paragraph (p.71) + **Anm.~1–7**, ALL petit (verified at
400 dpi — Anm.6's long forudsætningsløs/Hegel-Logik discussion on pp.76–79 is petit,
smaller than the p.71 body). Ends the *Philosophiens Grundlag og dens Værk* group with
a section-break rule. Verified sandbox compile: **55 pp., 0 errors, 0 char-warnings;
whole-file 87 `\emph{}`, 79 `\textit{}`.**
- **NO bold-Fett Danish emphasis in §19** (checked every page at 400 dpi). The 7 new
  `\emph` are all the Anm.~1–7 run-in labels.
- **Latin `\textit` (2 new):** `Totum est parte sua prius` (Anm.2, p.73, antiqua) and
  `a priori` (Anm.6, p.77). **German → plain (Fraktur), „…" kept:** Kant's *Kritik der
  reinen Vernunft* (Anm.2) and „Erkenntnißlehre" (Anm.4); Sibbern's own „Bemærkn.\ og
  Undersøg.\ betreffende Hegels Philosophie" (Anm.6); the *Theologische Zeitschrift*
  (Schleiermacher/de Wette/Lücke) reference (Anm.7). Schmidten's „om Mathematikens
  Væsen" is Danish in „…".
- **Errata applied (both non-NB):** p.75 l.15 Tilværelsesphære→**Tilværelsessphære**
  (Anm.4); p.80 l.13 „Philosoohiens"→**Philosophiens** (Anm.7, the print drops the
  *p* in the 2nd occurrence, before „Forhold til Aabenbaringen"). Each carries a
  % Rettelse note.
- **Numbering caught:** the OCR read the p.75 „Anm. 5." (Methode) as „Anm. 6." — the
  print is Anm.5 then Anm.6; transcribed correctly as 5/6.

**Batch 10 DONE (2026-07-19) — ★ DANISH TRANSCRIPTION COMPLETE.** **§ 20 + § 21 +
the verbatim Rettelser leaf** (printed pp. 81–86 = PDF 92–97, + errata leaf PDF 11),
image-verified page by page. §20 (Endelig Definition; the definiendum
`\emph{Philosophie}` is bold-Fett, and „egentlig speculativ Philosophie … tages
\textit{sensu eminenti}"), §21 (Philosophie paa lige Linie med det Empiriske og det
Suprarationale — body + Anm.1–4, then the book's full-size finale „Men tænke vi os nu
… det høieste Formaal."). Then the full **Rettelser** table (all 21 items + the two
author tail-notes: the double-§13 slip and the *Psychologie, ny Udarb.* p.133
umiddelbare→middelbare self-correction), transcribed from the leaf at 220–300 dpi.
**Final full sandbox compile (Computer-Modern substitute): 59 pp., 0 errors, 0
char-warnings, 0 markers; whole-file 93 `\emph{}`, 80 `\textit{}`.**
- **Bold-Fett in this batch:** only `\emph{Philosophie}` (§20 definiendum). §21 has
  NO bold — the climactic „Rige" terms (Skjønhedens/Poesiens/Godes/Kjærlighedens og
  Hellighedens Rige) are all normal weight (checked at 400 dpi). New `\textit`:
  `sensu eminenti`.
- **§21 structure (400-dpi size checks):** body (pp.82–83, full) → Anm.1–4 (petit) →
  body RESUMES (full) for the finale pp.85–86. Anm.4 is the short petit Hegel-Suprematie
  remark; the „Men tænke vi os nu…" finale is full-size body.
- **Rettelser** rendered as a tabular (NB | Pag. | Lin. | correction); the leaf's ditto
  dashes for repeated page numbers are written out explicitly (noted in a % comment).
- `catalog.yaml` note updated to reflect the completed transcription (section left
  `in-progress` — the English translation is Phase 2, not yet begun).

============================================================
## ★ STATUS: Danish transcription COMPLETE. Next = Phase 2 (English translation).
============================================================
`grep -c "text to be added" transcription.tex` → **0**. The whole book (Fortale +
§§1–21 + Rettelser) is transcribed, image-verified, all NB/non-NB errata folded in
with % Rettelse notes, verified compile 59 pp. 0/0.

**Still OWED (minor backfill, does not block Phase 2):** the 400-dpi emphasis-parity
pass over **pp. 1–6 (§§ 1–2, batch 1)** — batch 1 marked `\emph` conservatively from
200-dpi images before we'd confirmed this book's emphasis is BOLD Fraktur (Fett); a
few batch-1 `\emph` (e.g. „Videnskab"/„Maade") may be over-marked and should be
re-checked bold-vs-normal against the scan.

**Phase 2 — English translation** (`translation.tex`, NOT yet started): follow
`../../../TRANSLATION-PLAYBOOK.md`. Translate FROM this `transcription.tex` (source of
truth). Reuse the *erkjendelse* / *brøchner* conventions. Book-specific notes for the
translator: emphasis is bold-Fett rendered as `\emph{}` (→ italic in translation, same
convention); Latin already in `\textit{}` (keep, incl. the long Wolff §13,a Anm.3
quotations and the *scimus, qvia…* series — translate surrounding prose, keep Latin);
German block-quotes (Steffens ×3, Hegel, Fichte, Kant titles) are plain Fraktur in the
source — decide per playbook whether to italicize titles in English; no real Greek in
this book (only transliterated „Dikaiosyne"/„Nemesis", Fraktur).

The user compiles/commits/pushes — never commit from the session.
