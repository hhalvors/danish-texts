# Rasmus Nielsen — *Grundideernes Logik. I* (1864): transcription resume notes

This is a **TRANSCRIPTION** job (Fraktur Danish, scan → LaTeX), Phase 1. A later
English translation is Phase 2 (separate job, per ../../../TRANSLATION-PLAYBOOK.md).
Work in ~10-page batches; after each, compile, give a short report, hand back.
**Hans commits and pushes — the assistant never does.**

Book: *Grundideernes Logik. I.* Af R. Nielsen. Kjøbenhavn: Forlagt af den
Gyldendalske Boghandel (F. Hegel); Trykt hos J. H. Schultz, 1864.

## Scan & offset (VERIFIED)
- Scan: `~/bibliotek/Nielsen, Rasmus/1864-grundideernes-logik.pdf` (494 PDF pp.,
  Google Books, clean high-contrast).
- **Two page-number sequences:**
  - Front matter, ROMAN folios: **PDF = printed_roman + 2.**
    Indledning "VII" = PDF 9; "VIII" = PDF 10; errata "Trykfeil og Rettelser" = PDF 37.
  - Main body, ARABIC folios: **PDF = printed + 38.**
    printed p.1 (Første Deel) = PDF 39; last text p.456 = PDF 494.
- Title page = PDF 3; Forord = PDF 5; Indhold (table of contents) = PDF 7–8.

## Size & scope — READ THIS
- LARGE work: front matter (roman) + main body **printed pp. 1–456** (PDF 39–494).
- By the Forord it is "barely two-thirds of the first ninth of the whole Logic";
  it develops only the FIRST Grundidee, **Videns Idee** (the Idea of Knowledge).
- Deep hierarchy (see the original Indhold, PDF 7–8):
  **Deel > Afsnit > Kapitel > A./B./C. > a)/b)/c) > α)/β)/γ) > 1)/2)/3).**
  Første Deel = "Videns Idee"; Første Afsnit = "Den subjective Viden";
  Første Kapitel = "Viden og den Vidende: Subjectivitetens Logik".

## Typography — READ THIS
- **Type is FRAKTUR** (Danish body). Greek/Latin technical terms in antiqua.
- **Emphasis = letterspacing (Sperrsatz).** OCR CANNOT see it → image-verify
  every page and wrap each letterspaced span in `\emph{}`. Seen so far (p.VIII):
  the three Hovedpunkter terms `\emph{aprioriske Grundlag, af dens empiriske
  Grundlag}` and `\emph{Maal}`, and the run-in heading `\emph{Philosophiens
  aprioriske Grundlag.}`.
- **Quotes:** Danish „…" (low-high). Use „ (U+201E) … " (U+201D), matching the
  other transcriptions in this repo.
- **Footnotes** marked `*)` in the print → `\footnote{}` at the anchor word.
  The Indledning's notes cite Nielsen's own works (Forelæsninger over
  „Philosophisk Propædeutik" 1860–61; Philosophisk Propædeutik i Grundtræk 1857) —
  keep Danish work-titles in Danish.
- **Greek** typed directly (textalpha in preamble): p.VIII γνῶθι σεαυτόν. Copy
  glyphs verbatim; the sandbox cannot render Greek, so confirm on a local compile.

## OCR pipeline (rebuild each session; models don't persist)
```bash
TD=/tmp/gl_ocr && mkdir -p "$TD" && cd "$TD"
wget -q https://github.com/tesseract-ocr/tessdata_best/raw/main/script/Fraktur.traineddata -O Fraktur.traineddata
export TESSDATA_PREFIX="$TD"
SRC="/sessions/<id>/mnt/bibliotek/Nielsen, Rasmus/1864-grundideernes-logik.pdf"
# printed roman page P: PDF = P + 2 ; printed arabic page P: PDF = P + 38
pdftoppm -f $PDFP -l $PDFP -r 300 -png "$SRC" "$TD/ro" >/dev/null 2>&1   # NB output is ro-0NN.png (3-digit pad)
tesseract "$TD"/ro-*.png stdout -l Fraktur --psm 6 2>/dev/null | sed -e 's/ſ/s/g' -e 's/œ/æ/g' | tr -s ' '
```
`Fraktur` model is ~97%+ at word level on this clean scan. **Hybrid method:** take
OCR words as a base, then render ONE verification image per page (200–300 dpi;
copy PNG into the outputs dir and open with the Read tool) to catch letterspacing,
fix OCR slips, and place footnotes/quotes.
**Predictable OCR slips on this scan:** ø read as o (forste→første, gjore→gjøre,
horer→hører, provet→prøvet); doubled-æ artifacts (Vææren→Væren, Tææukning→Tænkning);
"st" ligature read as ﬅ/ﬀ (d.v.ﬅ→d.v.s., sﬀulde→skulde); sk read as }/ff
(}ulde→skulde); ikle→ikke; leading Fraktur N read as V (Vielsen→Nielsen);
er read as ex/ez.

## Verification compile (sandbox lacks libertinus + greek-fontenc — substitute; NOT in real file)
```bash
cd /tmp && D=verGL_$(date +%s) && mkdir -p "$D" && cd "$D"
SRC="/sessions/<id>/mnt/danish-texts/texts/nielsen/grundideernes-logik/transcription.tex"
sed -e 's/\\usepackage{libertinus}/\\usepackage{lmodern}/' -e '/libertinust1math/d' \
    -e '/textalpha/d' -e 's/\\usepackage\[danish\]{babel}/\\usepackage{babel}/' "$SRC" > t.tex
python3 -c "import re;s=open('t.tex',encoding='utf-8').read();open('t.tex','w',encoding='utf-8').write(re.sub(r'[Ͱ-Ͽἀ-῿]+','[Gr]',s))"
pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1; pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1
grep -o 'Output written.*' l.txt; echo -n 'char-warnings: '; grep -ic 'not set up\|missing.*character' l.txt
echo -n 'markers left: '; grep -c 'text to be added' "$SRC"
```
Expect 0 char-warnings, 0 errors.

## STATE — what's done vs. to-do
**Session 1 (2026-07-04): scaffolded + ENTIRE FRONT MATTER done.** Preamble (book
class, matching `../videnskabslaere`), title/Forord, offsets verified, OCR pipeline
proven. **Done & image-verified:** Forord + the whole Indledning, printed pp.
**VII–XXXIV** (28 pp). That covers: the opening Propædeutik-lecture quote; the
"Almindelig Indledning" with its three run-in Hovedpunkter — `\emph{Philosophiens
aprioriske Grundlag.}` (VIII), `\emph{... empiriske Grundlag.}` (XIII),
`\emph{Philosophiens Formaal.}` (XVIII); long block-quotes from J. L. Heiberg and
from Nielsen's own Philosophisk Propædeutik (footnotes cite "Phil. Propæd. S. NN"
etc. — Danish work-titles kept in Danish); the Tro/Viden + Kierkegaard
"Subjectiviteten er Sandheden" passage; the section heading `\section*{Indledning
til Logiken.}` (XXVII); the Hegel-systematics pages with many letterspaced
technical terms (`\emph{Logik, Physik og Ethik}`, `\emph{Mechanik}`, `\emph{Det
Uorganiskes Physik}`, `\emph{Videns Idee}`/`\emph{Magtens Idee}`/`\emph{Sandhedens
Idee}`, etc. — all image-verified); the two GERMAN Hegel quotations (XXXI–XXXII,
Bewußtseyn/Wissenschaft der Logik — image-verified incl. Hegel's own emphases
`\emph{Gegenstandes}`, `\emph{seiner selbst}`, and the „I/II/III Die Logik des …"
display list); Greek γνῶθι σεαυτόν (VIII). Every front-matter page (PDF 9–36) was
rendered and eyeballed for letterspacing. Sandbox compile clean: 27 pp., 0 errors,
0 char-warnings, 1 marker (the body marker). The **errata page** (Trykfeil og
Rettelser, PDF 37) is recorded as a comment block with 8 corrections to APPLY when
transcribing the body (do not reproduce the errata page as text).

## Body batch 1 (2026-07-04): printed pp. 1–14 done & image-verified.
Første Deel "Videns Idee" / Første Afsnit "Den subjective Viden" / Første Kapitel
"Viden og den Vidende: Subjectivitetens Logik" (the opening argument that philosophy
must begin with *Viden*, not Hegel's *rene Væren*), through the start of subsection
**A. Den umiddelbare Subjectivitet**. Rendering choices locked in:
 - Deel/Afsnit/Kapitel opening = a centered heading block with two centred rules
   (matches p.1 exactly); \addcontentsline for part+section; \markboth for header.
 - Sub-levels A./a)/α) etc. are rendered as centred bold heading blocks (NOT deep
   \subsection nesting), because LaTeX sectioning isn't deep enough for the full
   Deel>Afsnit>Kapitel>A/B/C>a/b/c>α/β/γ>1/2/3 hierarchy. Use \addcontentsline to
   keep them in the TOC. Subsection "A." done this way on p.12.
 - Greek verified glyph-for-glyph: p.6 ἀρχή; p.7 τὸ πρῶτον κινοῦν ἀκίνητον ὄν.
 - Latin inline: cogito ergo sum / cogitat ergo est / est ergo cogitat (p.4) — plain roman.
 - German quotations verified: p.9 footnote (Schelling "Vom Ich als Princip…" +
   Fichte-influenced "System des transcendentalen Idealismus": Bewußtseyn-era spelling,
   ß/ü, „…" quotes, \dots for the printed ellipses between quoted fragments); p.10
   „ein unvordenkliches Sein".
 - Letterspacing (\emph) verified per page: p.6 „Princip"/„Begyndelse" in one sentence;
   p.11 the three forms of Subjectivity — „umiddelbar", „reflecterende",
   „begribende Subjectivitet", „psychologiske". Quote-heavy pages otherwise clean.
 - Long footnotes that span two printed pages (p.10→11) are placed whole at the
   anchor; LaTeX flows them.
Sandbox compile clean: 37 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 2 (2026-07-04): printed pp. 15–24 done & image-verified.
Rest of subsection A (the Anskuelse/Tænken/Væren dialectic, the Eleatics/Zeno &
Herbart critique of change, the Differential/mathematical-element argument), the
close of A naming the two extremes (Sensualisme, subjective Idealisme), and the
start of sub-subsection **a) Sensualistisk Subjectivitet** (Locke, tabula rasa).
Verified specifics:
 - Math (amsmath): footnote on p.16–17 uses $A_0$,$A_1$,$A_2$, $A=A$, $A_0=A_0$;
   footnote on p.23 uses $0$ and $\infty$. Render in math mode.
 - Greek: p.21 (δόξα).
 - Latin inline: naturam expellas furca (p.18), tabula rasa (p.24) — plain roman.
 - German: „Ding an sich" (p.16–17 fn). Herbart is quoted in DANISH translation
   (p.19–20 fn), not German; with internal \emph{samværende}, \emph{mellem}.
 - Cross-page footnotes (p.16→17, p.19→20) placed whole at the anchor; LaTeX flows them.
 - Sub-subsection heading a) rendered as a centred bold line + \addcontentsline{toc}{subsubsection}.
 - Letterspacing verified per page: p.16/17 \emph{Forandringen}; p.19 \emph{ud fra, udenfor},
   \emph{Tankerum}; p.24 \emph{Sensualisme}, \emph{subjective Idealisme}, and the two-clause
   Sensualisme definition. Other pages clean.
Sandbox compile clean: 44 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 3 (2026-07-04): printed pp. 25–35 done & image-verified.
Rest of **a) Sensualistisk Subjectivitet** (Locke; Baco/Hobbes/Gassendi; Condillac's
transformation des sensations; Berkeley), and all of **b) Idealistisk Subjectivitet**
(Kant/Hume; Fichte's Wissenschaftslehre — A=A, Jeg=Jeg, the Non-A/X derivation; the
three-fold critique of "det fichteske Jeg"), up to the end of b) (before the c)
heading). Verified specifics:
 - German: p.30 fn („Ding an sich"; „der Zuchtmeister des dogmatischen Vernünftlers");
   p.34–35 fn = a LONG Fichte quote (Grundlage der Wissenschaftslehre) with letterspaced
   \emph{realistisch}, \emph{transcendental}; Bewußtseyn-era spelling, ß/ü, \dots for ellipsis.
 - Latin: nihil est in intellectu, quod non antea fuerit in sensu (p.31); a posteriori;
   tabula rasa. English titles/parentheticals kept as printed (Essay concerning human
   understanding; (immediatly); (combination of sensible qualities)); French: Traité des
   sensations; (transformation des sensations).
 - Fichte notation rendered as plain text: "A = A", "Jeg = Jeg", "Non-A ikke = A", "et X".
 - Sub-subsection headings a)/b) as centred bold lines + \addcontentsline{subsubsection}.
 - Letterspacing verified per page: p.31 \emph{for sig} (×2), \emph{Dogmatismen},
   \emph{Idealismen}. Other pages clean (names Locke/Hume/Kant/Fichte NOT letterspaced here).
 - Two long footnotes (p.30, p.34) span pages; placed whole at the anchor.
Sandbox compile clean: 52 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 4 (2026-07-04): printed pp. 35–46 done & image-verified.
Heading **c) Subjectivitetsproblemet** + its text: the psychological vs.
abstract-logical subjectivity contrast; critique of Hegel's Panlogisme; the long
Heiberg quotation (pp.37–39, „Subjectets Bestemmelse som Object…"); the
three-subjects analysis of „den speculative Logik"; the theocentric-standpoint
raisonnement and its critique via `via negationis` / `via eminentiæ`. Verified
specifics:
 - Heiberg footnote p.37 (Forelæsninger over Philosophiens Phil.… 1831--32).
 - **Leibnitz** (tz) ×3 preserved verbatim (print reads Leibnitz, not Leibniz).
 - Letterspacing p.38: \emph{Forestillings-Evnens forskjellige Grader},
   \emph{Monadernes Monade}, \emph{forudbestemte Harmonie}. Other pages clean.
 - Greek (p.44): τὸ ἄπειρον … ἄλογον (typed direct as Unicode, textalpha).
 - Latin in antiqua, plain roman (NOT letterspaced/italic): via negationis,
   via eminentiæ, testimonium spiritus sancti.
 - Dante footnote p.45: Italian verse (Paradiso 31) in \begin{verse}…\end{verse},
   attached to „Nærhed"; intro \emph{nel terzo giro dal sommo grado}.
 - „christelige" (ch) throughout the closing paragraph.
Sandbox compile clean: 61 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 5 (2026-07-04): printed pp. 46–57 done & image-verified.
Rest of A. (pp.46–53): the critique of the „speculative Dogmatik" and its
`testimonium spiritus sancti`; Alvidenhed vs. sandselige Modsætninger; the
Kampesteen example; close of A at „her udkræves høiere Former." Then the new
subsection heading **B. Den reflecterende Subjectivitet** (p.54) and its opening
(pp.54–57): Reflexion vs. Tænkning; the optics/logic sense of „Reflexion"; the
Hegel/Heiberg discussion of Vorden as Reflexionens Plads. Verified specifics:
 - Long **Kierkegaard footnote** (Afsluttende uvidenskabelig Efterskrift, S.126--127)
   placed whole at anchor „Eftertryk" on p.47; spans pp.47--48; letterspacing
   \emph{jeg} ×2 („bliver jeg eller er jeg udødelig?").
 - Letterspacing p.50: \emph{har} ×3 (Gud „har" ikke et Øie … men er Øie).
 - Letterspacing p.56: \emph{urolige} (Hegel's „urolige Eenhed").
 - Heiberg footnote p.55 (Perseus Nr.~2, S.~44; Prosaiske Skrifter 2det Bind 1861).
 - Latin in antiqua, plain roman: testimonium spiritus sancti, testimonium
   paupertatis, caput mortuum, in concreto.
 - B. heading rendered like A.: centered {\bfseries B.}\\ + {\large\bfseries …}
   + \addcontentsline{subsection}.
Sandbox compile clean: 68 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 6 (2026-07-04): printed pp. 57–68 done & image-verified.
Rest of B.'s opening (pp.57–59): Reflexion vs. Tænkning, Hegel's Encyclopædie/Logik
quotes, the Plato Parmenides problem; then subsubsection **d) Forstandsreflexion**
(p.60) and its nested paragraphs **α) Sættende og forudsættende Reflexion** (p.62)
and **β) Modsættende og eenhedsættende Reflexion** (p.66). Verified specifics:
 - Greek (typed direct, textalpha): Plato Parmenides p.58 „(νοήματα)" and the long
   „(ἀνάγκη, εἰ τἆλλα φῂς τῶν εἰδῶν μετέχειν, ἢ δοκεῖν σοι ἐκ νοημάτων ἕκαστον
   εἶναι καὶ πάντα νοεῖν, ἢ νοήματα ὄντα ἀνόητα εἶναι)"; Aristotle p.63 „de Gamles
   νοῦς", „αὐτὸν ἄρα νοεῖ, εἴπερ ἐστὶ τὸ κράτιστον, καὶ ἔστιν ἡ νόησις νοήσεως
   νόησις", „den evige νοῦς som ἡ νοήσεως νόησις"; p.66 inline „(τὸ ἕτερον)".
   Greek verified by cropping+upscaling the scan (gl_b6_096_greek*, _101_gr*).
 - German (Hegel Encyclopædie/Logik, Fichte): letterspacing \emph{Gedanken} (p.58,
   ×2), \emph{reflectirt} (p.59, in the Logik „Existenz" quote). Footnotes: Hegels
   Werke 6ter Bd Berlin 1840 S.45 (p.57), S.34 (p.64); Fichte Wissenschaftslehre
   Leipzig 1794 S.25 (p.68). NB German quote reads „ist er daher" first, „ist es
   daher" second — both preserved as printed.
 - Danish footnote p.59 letterspacing \emph{Tænkning} (anchor „Tænkningen").
 - Hierarchy note: lettering a)…d) runs continuously across the Kapitel (d) is
   under B, subsubsection level); nested under d) the print uses GREEK α)/β)
   (paragraph level, \addcontentsline{toc}{paragraph}).
 - Logical formulae A=A, Jeg=Jeg, Non-A rendered as math/plain text (not emph).
Sandbox compile clean: 77 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 7 (2026-07-04): printed pp. 68–79 done & image-verified.
Rest of β)/into γ): Fichte's "Die Gegensätze" fn (p.69), then paragraph
**γ) Iboende og oversvævende Reflexion** (p.70); then subsubsection
**b) Væsensreflexion** (p.76) and its nested paragraph **α) Den phænomenale
Reflexion** (p.77). Verified specifics:
 - Letterspacing \emph{}: p.69 „eenhedsættende", „modsættende"; p.77 „phænomenal,
   som grundende og som begrundende" (before the α heading).
 - Latin (Herbart, antiqua→plain roman): p.71–72 „Posito A, nulla ponitur relatio…
   cui relationis aliquid affingi debeat vel possit"; fn "De principio logico
   exclusi medii… Kl. phil. Schr. II. P.724. Jvfr. P.S.V. Heegaard… Kbhvn. 1861,
   S.4 flgd." Also inline "cognoscendi genus", "harmonia præstabilita",
   "in concreto"/"in abstracto", „zufällige Ansichten", „Ding an sich".
 - Math (p.73–74): $\frac{y}{x}=c$; $y=f(x)=cx$; $\frac{dy}{dx}=\frac{0}{0}=c$;
   $A=A,B=B,C=C,D=D$; $\frac{A}{B}=\frac{C}{D}$; $a=b,b=c,a=c$.
 - German Kant fn (p.78–79): „Dies war das Resultat der ganzen transcendentalen
   Aesthetik… ein von der Sinnlichkeit unabhängiger Gegenstand sein muß". Kritik
   der reinen Vernunft, Leipzig 1838, S.247–48 Anm. Fichte fn p.69 „…im Bewußtseyn
   seyn." Anfr. Skr. S.26 (abbrev is "Anfr.", verified by crop).
 - PRINT ODDITIES preserved faithfully (not corrected): p.68 dittography „og og"
   (% flagged); heading letter-sequence jump — p.60 was „d) Forstandsreflexion",
   p.76 restarts „b) Væsensreflexion" (% flagged); Kant fn spells „Erscheinigung".
Sandbox compile clean: 85 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 8 (2026-07-04): printed pp. 79–90 done & image-verified.
Rest of α) Den phænomenale Reflexion (pp.80–85: Fichte's Ikke-Jeg critique, „huult i
Ryggen"), then paragraph **β) Den grundende Reflexion** (p.85) through p.90 (Grund
og Følge, Herbart on Følgen). Verified specifics:
 - Letterspacing \emph{}: p.85 „grundende" (first occurrence in „udvikler sig i den
   grundende Reflexion", verified by crop) — only one in the batch.
 - German (antiqua→plain roman): Fichte fn p.80 „Kant geht in der Kritik d. r. Vst.
   von dem Reflexionspunkte aus… in dem Ich vorhanden." Wissenschaftslehre 2te
   Lieferung S.108. Schluß-Anmerkung; Herbart p.83 „wieviel Schein soviel Hindeutung
   auf Seyn"; Herbart p.88 „Følgen… skal ligge i Grunden… en Følge af samme." and
   „en Gjentagelse i en afsondret Tanke". Danish fn p.87–88 (Nielsen's own),
   „Da Functionsbegreb…" ending "Mathematik og Dialektik S. 7–8."
 - Math (inline, p.81): „aprioriske Syntheser" af $X$ og $Y$, af $A+B$ ved $a$ og $b$.
 - Quoted phrases kept in „…": „den rene Fornufts Kritik", „Tingenes Grund/Væsen/
   Grunde", „Ugrund", „Urgrund", „de Underjordiske".
 - PRINT ODDITY preserved (not corrected): p.83 „Phænomerne" (trykfejl for
   „Phænomenerne"), % flagged.
Sandbox compile clean: 93 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 9 (2026-07-04): printed pp. 90–101 done & image-verified.
Rest of β) Den grundende Reflexion (pp.90–92: Grund vs Princip/Begyndelse, ἀρχή),
then paragraph **γ) Den begrundende Reflexion** (p.92) through p.101 — the three
theses (Eet / forskjelligt / tilstrækkelig Grund), Eleatics + Plato, Gnostics/
Valentinians, Anaxagoras/atomists, Leibnitz on sufficient reason. Verified specifics:
 - Letterspacing \emph{}: the three theses, both in the enumerated list (p.93) and as
   run-in lead-ins — 1) „Alt er i Grunden Eet" (p.93), 2) „Alt er i Grunden
   forskjelligt" (p.96), 3) „Alt maa have sin tilstrækkelige Grund" (p.99). No other
   letterspacing in the batch (verified full-page scans pp.91–101).
 - Greek (typed direct, textalpha), all crop-verified: p.91 ἀρχή; p.93 τὸ ἕν, τὸ ὄν,
   τὸ ὄντως ὄν, Plato „(ὄντος δέ γε ψεύδους ἔστιν ἀπάτη)"; p.94 „(κινδυνεύει τοιαύτην
   τινὰ πεπλέχθαι συμπλοκὴν τὸ μὴ ὄν τῷ ὄντι)", „Mening" (δόξα); p.95 Valentinian set
   βυθός/προπάτωρ, ἔννοια, σιγή, νοῦς/ἀλήθεια, λόγος/ζωή, ἄνθρωπος/ἐκκλησία, σύζυγοι,
   πλήρωμα, κένωμα.
 - Latin (antiqua→plain roman): principium rationis sufficientis, principium exclusi
   medii, principium inclusi medii, in concreto, creat sibi/creat nobis/creat omnibus.
 - Math (inline logical letters): p.100–101 $A$ er $A$; $A$ er ikke $A$, men $B$; …;
   $A$ er enten $B$ eller $C$; $A$ er baade $B$ og $C$.
 - Footnotes: Poul Møller (Efterl. Skr. 4de Bind S.59) p.94; Nielsen's own
   „Phil. Propæd." lectures p.97 & p.99. „Leibnitz" spelling preserved.
Sandbox compile clean: 102 pp., 0 errors, 0 char-warnings, 1 marker (Greek shown as
[Gr] in the sandbox substitution; real Greek is in the source).

## Body batch 10 (2026-07-04): printed pp. 101–112 done & image-verified.
End of γ) Den begrundende Reflexion (pp.101–105: Leibnitz/sufficient reason,
crystallisation example, ratio finalis), then subsubsection **c) Virkelighedsreflexion**
(p.105) and its paragraph **α) Den substantielle Reflexion** (p.106) through p.112
(substance, Heraclitus, Spinoza). Verified specifics:
 - Letterspacing \emph{}: p.110 „aflede" and „udvikle" (the contrasting pair „At
   aflede Subjectiviteten…" vs „at udvikle Subjectiviteten…"), both crop-verified.
   No other letterspacing in the batch (full-page scans pp.102–112).
 - Greek (typed direct, crop-verified), Heraclitus p.109: „evig levende Ild"
   (πῦρ ἀεὶ ζῷον), udslukker Maal (ἀποσβεννύμενον μέτρα), antænder Maal
   (ἁπτόμενον μέτρα).
 - Latin (antiqua→plain roman): harmonia præstabilita, ratio finalis, eo ipso,
   principium exclusi/inclusi medii already earlier; Spinoza p.111 (id quod in se est
   et per se concipitur), (cujus essentia involvit existentiam), (modi, modificationes).
 - Math (inline logical letters): p.102 „Grunden til, at $A$ er bleven drikfældig".
 - Footnotes: Hegel Werke 3ter Bd 1833 S.76 (German, p.102); Nielsen's own Affinitet
   note (p.103) & „Phil. Propæd." lectures S.167–177 (p.106); Heiberg „Det logiske
   System" / Perseus Nr.2 S.38 (p.107, with nested „En"/„Et"/„en Skov"/„et Huus").
 - Spellings preserved as printed: „Leibnitz", „Arogonit" (for Aragonit), „Zittren".
Sandbox compile clean: 110 pp., 0 errors, 0 char-warnings, 1 marker (Greek shown as
[Gr] in the sandbox substitution; real Greek is in the source).

## Body batch 11 (2026-07-04): printed pp. 112–123 done & image-verified.
Rest of α) Den substantielle Reflexion (pp.112–113: the substantial contradiction,
Magt/Selvmagt, „Viden er Magt"), then paragraph **β) Den causale Reflexion** (p.114)
through p.123 (Aristotle's aporia on number/body/surface/point; Plato's Ideas &
τραπεζότης; Concrete/Abstract & Hegel; Kant's Tidsfølge Grundsætning; Heiberg on
Grund vs Aarsag; Stød/Vexelvirkning; Kant's Thesis/Antithesis on transcendental
Frihed; the A/B/C causal Kredsløb; close of β at „…existerende Ting i en virkelig
Tingenes Orden."). Verified specifics:
 - Letterspacing \emph{}: NONE in the batch. Every full-page scan pp.113–123 was
   crop-checked; the only letterspacing is on the β)/γ) run-in headings themselves
   (rendered bold, as usual). Body is quote-heavy but not letterspaced.
 - Greek (typed direct, textalpha), all crop-verified — Aristotle Metaphys. III.5
   (p.114): (οὐσίαι τινές), (πάθη, Affectioner), (ὡς ὄν τι καὶ οὐσία τις οὖσα),
   (διαιρέσεις ὄντα τοῦ σώματος); Plato's Ideas (p.115): (ἡ τραπεζότης ἐν τῇ τραπέζῃ),
   (ἡ πρώτη οὐσία), (τόδε τι).
 - Latin (antiqua→plain roman): sui causa, sui compos (p.112); pro et contra (p.118).
 - Math (inline logical letters): p.112–113 $A$/$B$ (the Magt-over-$B$ argument);
   p.120 fn $A$/$B$; p.121 $A$ af $B$, $B$ af $C$, $C$ af $D$; p.122 the $A$/$B$/$C$
   Kredsløb (incl. $A$'s).
 - Footnotes: Nielsen's own propæd. Logik (Kbhvn. 1845 S.166–67, p.113); Metaphys.
   III.5 (p.114); „Phil. Propæd." lectures (1860–61 S.84, p.115; 1861–62 S.139–43,
   p.121); GERMAN Kant Kritik der reinen Vernft. (Leipzig 1838 S.196–97, p.117);
   two long footnotes on p.118 (Nielsen „Phil. Propæd." 1860–61 S.165–66; Heiberg's
   Logik Anfr. Skr. S.47 & S.75, the second continuing onto p.119 in the print but
   placed whole at its anchor).
 - PRINT NOTE (not an error): the book uses BOTH „t. Ex." (= til Exempel, pp.112 &
   118) and „f. Ex." (pp.114–116) — reproduced faithfully, % noted. German „Vernft."
   abbreviation for Vernunft preserved as printed, % noted.
Sandbox compile clean: 118 pp., 0 errors, 0 char-warnings, 1 marker (Greek shown as
[Gr] in the sandbox substitution; real Greek is in the source).

## Body batch 12 (2026-07-04): printed pp. 123–133 done & image-verified.
Paragraph **γ) Den totaliserende Reflexion** (p.123) through p.133 — the totalising
reflection, indre/ydre Totalitet & Principet, Selvheds-/Andethedstotalitet, the
mechanical vs. organic whole (Uhr example, crystal, chemical vs. mechanical union,
geological/organic totality), up to the psychological subjectivity & Fornemmelse; then
the close of subsection **B** at „…belyses fra et høiere Synspunkt." Ended exactly at
the B/C boundary. Verified specifics:
 - Letterspacing \emph{}: p.125 body „totaliserende" (Reflexionen er totaliserende).
   Inside footnotes (Heiberg's own emphases): p.124 fn „har" (har det første Led) &
   „har været" (Grunden har været); p.125 fn (cont.) „have været" & „har været";
   p.128 fn „Realitet" & „Eenhed af Væsen" (the parenthetical „Eenhed af Væren" is NOT
   spaced — verified by crop); p.129 fn „det Hele", „Delene", „falde udenfor det Hele".
   All body pages otherwise clean (crop-checked pp.124–133).
 - TWO long Heiberg footnotes: (1) p.124→125, „i følgende Kategorier… es ist gewesen"
   (Logik, Anfr. Skr. S. 36), with a German phrase „es ist gewesen"; (2) p.128→129,
   the „Totalitet" note (Anfr. Skr. S. 49; S. 63–64; S. 64 / Prosaiske Skrifter 1ste
   Bind S. 241), which contains a BRACKET DIAGRAM. Both placed whole at their anchors.
 - DIAGRAM (p.129 fn) reproduced as a centred `tabular` inside the footnote: row $C$
   spanning all (\hline), row $A$ over cols 1–3 and $B$ over cols 5–7 (\cline{1-3}\cline{5-7},
   col 4 left open — matching „Delen 4 falder udenfor"), then 1.\,2.\,3.\,4.\,5.\,6.\,7.
   Rendered check confirmed it matches the print. Ting/Heelt labels $A$/$B$/$C$ set as
   math; part-numbers as plain text.
 - No Greek in this batch. No Latin phrases. „Materien"/„er villieløs"/„Et Uhr" etc.
   quoted normally.
Sandbox compile clean: 125 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 13 (2026-07-04): printed pp. 133–143 done & image-verified.
Subsection **C. Den begribende Subjectivitet** (p.133) and its long introduction through
p.143 — the critique of Hegel's „objective Logik" as either Væsensphilosophie or mere
„dialektisk Synonymik", worked through the three Kategorier **Grunden / Substansen /
Causaliteten** (run-in headings), the Fichte/Hegel Videnskab contrast, and the imaginary
objector's „Men…" speech; ended at the run-in phases list „Begriben og Begreb,
Begribningens Phaser, Begriben og Viden" — right before subsubsection a). Verified:
 - Run-in topic headings letterspaced \emph{}: \emph{Grunden.}, \emph{Substansen.},
   \emph{Causaliteten.}; and the list \emph{Grunden}, \emph{Substansen} og
   \emph{Causaliteten} (p.134).
 - Letterspacing \emph{} (mostly Heiberg's/Hegel's own emphases in quotes): p.135
   \emph{Væsen}/\emph{Phænomen}/\emph{Nødvendighed} (the 1)2)3) predicate terms),
   \emph{Ting} (Existerende: Ting!), \emph{Ting og Egenskab}; p.139 \emph{Aarsag},
   \emph{Virkning} og \emph{Vexelvirkning}, \emph{Virkelighed til Begreb},
   \emph{Causalitet til Subjectivitet}; p.140 (Heiberg) \emph{Subjectivitet},
   \emph{Frihed}, \emph{Tilværen}, \emph{Subjectet}, \emph{Friheden}, \emph{Jeg};
   p.143 \emph{begribende Subjectivitet} + the phases list \emph{Begriben og Begreb},
   \emph{Begribningens Phaser}, \emph{Begriben og Viden}.
 - GERMAN quotes (Hegel, image-verified glyph-for-glyph): p.138 „Die Kausalität ist
   bedingt und bedingend… zum Begriffe selbst gekommen." with emphases \emph{hat} and
   \emph{absoluten Begriffe}; p.140–141 „Die Gestalt des \emph{unmittelbaren} Begriffes…
   den formellen Begriff aus." (ß, ä/ö/ü preserved).
 - Math: p.135 „et mellem $+$ og $-$ svævende Raisonnement".
 - Footnotes: Heiberg Ledetraad 1831–32 (p.135), Anfr. Skr. S.77–78 (p.136), S.80
   ×2 (p.140, p.141); Hegel Wiss. der Logik & philos. Propædeutik Berlin 1840 (pp.137–139).
 - PRINT ODDITIES preserved (% flagged): footnote „Wissenschaft der Logik… Berlin 183."
   (truncated year, for 1834); and the print gives NO closing quote after
   „Subjectivitetsproblemet" on p.140 — the objector's „det Problem…" speech is left
   unclosed in the original (reproduced as printed).
Sandbox compile clean: 132 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 14 (2026-07-04): printed pp. 143–154 done & image-verified.
Subsubsection **a) Begriben og Begreb: logisk Ideebevægelse** (p.143) and its text
through p.154 — Begriben/Begreb/Reflexion distinction, Reflexionens vs. Begrebets Sphære,
Panlogisme critique; then paragraph **α) Negationsbestemmelser: Begrebet i logisk Form**
(p.146) — Herbart on Negation as subjective, Hegel's „immanente Negation"/„Negationens
Negation", the Speil/Bord/Elephant reductio, the Væren=Intet=Vorden trilogy and its
subjectivity, „Det Enkelte er det Almene"; ended mid-p.154 at the letterspaced set-off
sentence „…saaledes gribes og begribes et antilogisk Indhold i logisk Form." (end of that
paragraph, before „Skal det Antilogiske derimod…"). Verified specifics:
 - a) rendered as centred bold subsubsection + \addcontentsline{toc}{subsubsection};
   α) as centred bold paragraph-level + \addcontentsline{toc}{paragraph}.
 - Letterspacing \emph{} (all crop-verified): p.143 \emph{begribende Subjectivitet}
   (already in batch 13's tail); p.145 det \emph{Antilogiske} („betegne vi den negativt
   ved Kategorien det Antilogiske" — only „Antilogiske" spaced, not „det"); p.151
   \emph{Almene}/\emph{Enkelte} (Forhold mellem…), and inside the long Hegel-Danish quote
   \emph{absolute Identitet med sig}, \emph{Almeenhed}, \emph{Almenes}; p.152 (Hegel quote
   cont.) \emph{Almene}, \emph{Eenfolde}, and the trilogy \emph{Væren, Intet, bestemt Væren
   eller Tilværen} („eller" is NOT spaced but kept inside the emph span); p.153
   \emph{Enkelte} („hvad det Enkelte særlig angaaer"); p.154 the whole set-off sentence
   \emph{saaledes gribes og begribes et antilogisk Indhold i logisk Form.} All other body
   pages crop-checked clean (144, 146–150 body, 153 quote „Det Enkelte…siger Hegel…" plain).
 - Math (inline logical letters): p.147 $A$ er ikke Ikke-$A$; p.148 $A$ er ikke, hvad $A$
   ikke er; p.150–151 the trilogy 1) Væren $=$ $A$, 2) Intet $=$ Ikke-$A$, 3) Væren $=$
   Ikke-Ikke-$A$; p.152 Ikke-Væren $=$ Intet. Compound nouns (Ikke-Bord, Ikke-Speil,
   Ikke-Værende, Ikke-Væren) kept plain with hyphen (NOT math — Bord/Speil/Væren are words).
 - Two footnotes: p.147 the long Nielsen quote „Man hører ikke sjældent…end Dogmatismen."
   (Phil. Propæd. i Grundtræk. Kjøbenhavn 1857, S.152–153); p.151 Hegel, Wissenschaft der
   Logik, 2ter Theil, Berlin 1834, S.36 flgd. Both placed whole at their anchors.
 - Herbart quote (Danish, plain): „Negationerne", siger Herbart, „ere kun i dens
   Forestilling…Manglen selv er Intet." (p.146). „Det Enkelte" — siger Hegel — „er det
   Almene." with em-dashes → --- (p.153).
 - PRINT ODDITIES preserved (% flagged): p.144 dittography „nok at at gjennemføre";
   p.145 dittography „hvad er er vel dette". Also faithful: „negte" (p.146, not nægte);
   „afsondret" set as afſondret; p.153 comma after „og" („subjectivt og, dog Altsammen").
Sandbox compile clean: 140 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 15 (2026-07-04): printed pp. 154–164 done & image-verified.
Rest of α) Negationsbestemmelser (pp.154–155: the uendelige Negativitet as the form where
det Enkelte = det Almene; the Hegel „Das Allgemeine…freie Macht" quote); then paragraph
**β) Positionsbestemmelser: Begrebet i antilogisk Form** (p.155) through p.164 — A er A in
both directions; Stilpon's „Menneske er Menneske"/Kaal quote; the Eleatic „Ene" and Plato's
Parmenides (Greek); atoms/herbartske Realer; Hegel's sandsende Bevidsthed (Nu/Her indexicals)
vs. Feuerbach's „Unsagbares"; the positive/negative/antilogical Domme; Abstractions- vs.
Constructionsbegreb; ended at end of p.164 „…kan det ikke hjælpe at beraabe sig paa den."
Verified specifics:
 - β) rendered as centred bold paragraph-level + \addcontentsline{toc}{paragraph} (mirrors α)).
 - Letterspacing \emph{} (all crop-verified): the logical Domme wherever set off — p.155
   \emph{det Enkelte er det Almene}; p.156 \emph{det Almindelige er det Almindelige},
   \emph{det Enkelte er det Enkelte}, \emph{Dette er Dette}, \emph{det Almene er det Almene};
   p.157 \emph{det Almene er det Almene}, \emph{det Enkelte er det Enkelte}; p.160
   \emph{det Almene er det Almene}, \emph{det Enkelte er det Enkelte}, \emph{det Enkelte er
   det Almene}, \emph{det Almene er det Enkelte}; p.161 \emph{det Enkelte er det Almene},
   \emph{det Enkelte er ikke det Almene}, \emph{det Almene er det Enkelte}; p.163 \emph{det
   Enkelte er det Almene}; p.164 \emph{det Almene er dette Enkelte}. (NB the running-prose
   „Det Almene er dette Enkelte." on p.160 is NOT spaced — verified.)
 - German own-emphases (Sperrsatz, crop-verified): Hegel p.155 \emph{freie Macht},
   \emph{sich selbst} (×3), \emph{freie}; Hegel sandsende-Bevidsthed pp.158–159
   \emph{udvortes}, \emph{denne}, \emph{nu}, \emph{her}, \emph{Nu} (×2), \emph{Her} (×2),
   \emph{nu her, nu her, nu her}; Feuerbach p.159 \emph{dieses Haus mein} (in „…mein Weib,
   dieses Haus mein Haus"), p.160 \emph{dieses} (Weib); p.162 the whole \emph{„Dieses Weib
   ist mein Weib, dieses Haus mein Haus"} is spaced; p.164 fn \emph{objektive},
   \emph{subjektiven}. Kant p.162 („Et Begreb mister ikke…") NOT spaced.
 - Greek (typed direct, textalpha), Plato Parmenides p.157, crop-verified: (εἰ ἔν ἔστιν),
   (ἀρχή), (τελευτή), (μέσον), (πέρας), (ἄπειρον), (ἄνευ σχήματος).
 - Math (inline logical letters): $A$ er $A$ (p.155, p.156). Compound „Ikke-Værende" kept
   plain with hyphen (word, not logical letter).
 - § sign rendered \S~: fn p.159 „Grundsätze…\S~26 flgd."; body (\S~28); fn p.164 „…S.~215".
   Abbrev spacing: f.\ Ex., d.\ v.\ s., z.\ B.; S.~39, S.~131 flgd., S.~37.
 - Footnotes placed whole at anchor: Hegel Anfr. Skr. S.39 (p.155); Phil. Propæd. S.131 flgd.
   (p.157); Jvfr. Philos. Propæd. S.37 (p.158); Feuerbach Grundsätze…\S~26 (p.159); Zoologien
   note (p.163); the long „Es ist"—Hegel fn anchored at „Teleologien" on p.164 which CONTINUES
   at the bottom of p.165 (German „auf diesem ganzen Standpunkte…werden sollen" + Danish tail
   „Men hvad er „an und für sich Wahrheit"…") — placed whole at the p.164 anchor.
 - Mid-word page-break hyphens (file convention „Totali-\n% p.\nteten"): p.157/158 „Dette-\n
   værende"; p.163/164 „Con-\nstructionen".
 - Feuerbach spelling „Wiederspruch" (for Widerspruch) and „vindicirt" preserved as printed.
Sandbox compile clean: 149 pp., 0 errors, 0 char-warnings, 1 marker (Greek shown as [Gr] in
the sandbox substitution; real Greek is in the source).

## Body batch 16 (2026-07-05): printed pp. 165–177 done & image-verified.
End of β)/into ch. 1: p.165 Hegel „Es sind…mehrere Formen der Unmittelbarkeit" quote (the
Umiddelbarhedernes Skala); p.166 the Sommernatsdrøm/Skuespiller simile, then paragraph heading
**γ) Begrebets Realitet: den fuldkomne Begriben** (centred bold + \addcontentsline paragraph);
pp.166–171 Viden/Magt, Abstractions-/Constructionsbegreb, det logiske Kredsløb, den logiske
Erindren, ontologisk vs. psychologisk Subjectivitet; pp.172–177 the three run-in problems
(Bevægelses-, Forandrings-, Mulighedsproblemet) with Zeno's flying arrow, Diodoros Kronos, and
Leibniz. Ended at end of p.177 „…er Eet med den fuldkomne Begriben." (right before the b) heading).
Verified specifics:
 - γ) rendered as centred bold paragraph-level + \addcontentsline{toc}{paragraph} (mirrors α)/β)).
 - Run-in topic headings letterspaced \emph{} (crop-verified): p.172 \emph{Bevægelsesproblemet.},
   p.174 \emph{Forandringsproblemet.}, p.175 \emph{Mulighedsproblemet.} — but the same three
   words in the intro list on p.172 („til de tre særskilte: …") are NOT spaced.
 - Other letterspacing \emph{} (crop-verified): p.167 „en Steen kan \emph{ligge} stille, en
   Muur kan \emph{staae} stille" (later at ligge/gaae/staae NOT spaced); p.169 \emph{logiske
   Erindren} at term intro (later occurrences incl. the p.169/170 break-word NOT spaced);
   p.171 the whole \emph{uendelig Vexelbestemmelse af Erindren og Frembringen}.
 - German own-emphases (Sperrsatz, crop-verified) in the p.165 Hegel quote: \emph{erste},
   \emph{Daseyn}, \emph{Existenz}, \emph{Grunde}, \emph{Wirklichkeit}, \emph{Substantialität},
   \emph{Objektivität}. Schelling p.170 („Ueber die Natur…schaffen") NOT spaced.
 - Greek (typed direct, textalpha), crop-verified: p.173 (ἐν τῷ νῦν κατὰ τὸ ἴσον); p.175
   Diodoros (ὅταν ἐνεργῇ, μόνον δύνασθαι, ὅταν δὲ μὴ ἐνεργῇ, μὴ δύνασθαι).
 - French p.177 „Le présent est gros de l'avenir, siger Leibniß" — Antiqua, NO quote marks,
   not spaced (rendered plain).
 - Math (logical letters, crop-verified p.174): $A$ forandrer sig … $A_0$, $A_1$, $A_2$;
   $A = A$. But the lowercase hypothetical case-labels a, b on p.176 are set in Fraktur →
   kept PLAIN (not math).
 - Footnotes placed whole at anchor: p.167 „Phil. Propæd." 1860--61 S.24--30; p.172 Phil.
   Propæd. S.41 (at „…den Ene, som den Anden."); p.173 Jvfr. Mathm. og Dialekt. S.137 flgd.
   (at „…hvilket er en Modsigelse."); p.176 Forelæsn. ov. „Phil. Propæd." 1860--61 S.98--100
   (at „…thi saa er den Virkelighed").
 - Print oddities preserved + flagged: p.173 „Aristoteless" (double-s genitive); p.174
   „factisk" (med c) vs. „faktisk" (med k) — both preserved, flagged with a % comment.
 - Mid-word page-break hyphens (file convention): p.168/169 „anti-\n% p.\nlogisk"; p.169/170
   „Erin-\n% p.\ndren".
Sandbox compile clean: 158 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 17 (2026-07-05): printed pp. 177–189 done & image-verified.
Subsubsection **b) Begreb og Idee: Begribningens Phaser** (p.177) with the Hegel „Ideen"/„Die
Idee" quotes; the three Phaser announced; then paragraph **α) Videns Oprindelighed: universalia
ante rem** (p.178). Long critique of Platonic vs. Hegelian idealism: Poul Møller on Plato's
Ideas (p.180), the three Fordringer on det Almene (pp.181–82), the big Plato-quotation block
(Parmenides/Philebus/Timaeus/Sophist Greek, pp.182–83), Aristotle's critique (pp.184–85), Hegel's
Naturphilosophie mocked (p.188). Ended mid-p.189 at „…dernæst fra det ontologiske Standpunkt."
(before the psychologisk-Standpunkt paragraph „Hvad Magtmomentet gjælder…").
This batch is exceptionally Greek-dense; every Greek run was crop-verified at 1.5–3× zoom.
Verified specifics:
 - b) rendered as centred bold \subsubsection + \addcontentsline; α) as centred bold paragraph.
 - Greek (typed direct, textalpha), all crop-verified:
   p.182 (ὁ ὄγκος αὐτῶν ἄπειρός ἐστι πλήθει), (ὥσπερ ὄναρ ἐν ὕπνῳ);
   p.183 (πέρας), (ἄπειρον), (τὸ ἐξ ἀμφοῖν τούτοιν τι συμμισγόμενον), (αἰτία),
   (τὸ ὂν ἀεί, γένεσιν δὲ οὐκ ἔχον, καὶ τὸ γιγνόμενον μὲν ἀεί, ὂν δὲ οὐδέποτε),
   (πάσης γενέσεως τιθήνη), (ἀόρατον εἶδός τι καὶ ἄμορφον, πανδεχές, μεταλαμβάνον δὲ ἀπορώτατά πῃ
   τοῦ νοητοῦ), (ἐκμαγεῖον), (μετ' ἀναισθησίας ἁπτὸν λογισμῷ τινι νόθῳ),
   (ἕτερον δέ γέ ποί φαμεν τὸ ἕτερον εἶναι ἑτέρου, καὶ τὸ ἄλλο δὴ ἄλλο εἶναι ἄλλου);
   p.184 (ἑνάδες, μονάδες), (τό ἐπὶ πᾶσι κοινόν), (χωρὶς ἐστί);
   p.185 (ἄπειρον), (αὐτὸ ἄνθρωπόν φασιν εἶναι καὶ ἵππον καὶ ὑγίειαν);
   p.186 (εἰ ἓν ἔστι), (εἰ ἓν μὴ ἔστι); p.187 (ἔκγονος).
   (NB p.183 „ποί φαμεν": the print shows ποί with acute-iota where Sophist std. is πού —
   reproduced as printed.)
 - Letterspacing \emph{} (crop-verified): p.181 item 1) \emph{Selveenhed} (first occ. only);
   p.182 item 2) \emph{absolute Identitet} (item 3) has none); p.189 Hegel quote \emph{uopløste
   Modsigelse}. The German „Es sind…"-style quotes on p.188 (Hegel Naturphil., set in Fraktur
   here) have NO letterspacing.
 - Latin set-off terms (universalia ante rem, res, non-ens, universalia sunt ante rem, in
   abstracto etc.) kept PLAIN (Antiqua in print; no italics in our roman transcription).
 - Footnotes placed whole at anchor: p.180 Poul Møller „Phil. Hist. S. 161--62" (at „Poul
   Møller"); p.183 „Phil. Propæd. S. 133--134" (end of the big Plato quote); p.184 „Jvfr. Phil.
   Propæd. S. 137--138" (at „bemærket"); p.187 „Phil. Propæd. S. 157" (end of Hegel quote);
   p.188 „Forelæsn. over „Phil. Propæd." 1861--62 S. 71" (end of Naturphil. quote).
 - Print oddities preserved + flagged: p.189 „phychologiske" (for psychologiske) — flagged with
   a % comment. (OCR-dropped h's corrected against image: „scholastiske" ×2 on p.179.)
 - Mid-word page-break hyphen: p.177/178 „Concre-\n% p.\ntioner".
Sandbox compile clean: 167 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 18 (2026-07-05): printed pp. 189–200 done & image-verified.
Rest of α) Videns Oprindelighed (the psychologisk-Standpunkt tail, pp.189–193): the antilogiske
Umiddelbarhed of Sandsning/Fornemmelse, the Kredsbevægelse Selvhed→Andethed→Selvhed, Gjentagelse
as uendelig Fornyelse, the Lessing „venstre Haand" saying; then paragraph **β) Magtens
Oprindelighed: universalia post rem** (p.193) through p.200 — Nominalisme (universalia post rem,
res ipsæ, nomina/flatus vocis) → Empirisme → Realisme, „Viden er Magt", Billede/Beskrivelse/
Charakteristik/Begreb, the Exemplar/Exempel/Begreb relativity, Liebig on Sukkeratom's atoms,
Facticitetsbegreber, Videns Opgaaen i Magten, and the opening of the „Sagbevægelse" self-quote.
Ended mid-p.200 at „…Skal nu Eenheden af den tænkte Væren og det Værende selv" — batch stops
INSIDE the open „Mystificationen…"-quotation (it closes on a later page; the „ is intentionally
left unbalanced at batch end, matching the print). Verified specifics:
 - β) rendered as centred bold paragraph-level + \addcontentsline{toc}{paragraph} (mirrors α)).
 - Letterspacing \emph{} (crop-verified): p.197 \emph{det Almene er det Enkelte} (the antilogiske
   Dom, set off — crop gl_b18_197_dom3); p.200 \emph{Detteværende} ONLY in „Af Udtrykket
   Detteværende sees" (crop gl_b18_200_a — the two earlier „et Detteværende" are NOT spaced).
   Nothing else letterspaced in the batch: p.189 „Nu og Her" and p.199 „Videns Opgaaen i Magten"
   crop-checked PLAIN; full-page scans pp.189–196, 198 clean.
 - Latin set-off terms all PLAIN (antiqua→roman, no italics): universalia (ante/post) rem, res,
   res ipsæ, realia, nomina, flatus vocis. „universalia post rem" in the β heading is letterspaced
   in print → rendered bold as part of the heading.
 - Two footnotes placed whole at anchor: p.192 Heiberg (at „Begyndelsespunkt") „Det astronomiske
   Aar", Prosaiske Skr. 9de Bd. S.79 flgd. — a long Heiberg quote on „Gjentagelsens Dialektik"
   with an internal \dots (og oplives ved begge … Men hvad); p.197 Forelæsn. over „Phil. Propæd."
   1861--62 S.41 (at end of the „…Exempeludvikling."-quote).
 - Danish-translation quotes (plain „…"): Lessing p.191; Naturforsker „Vi lære…" p.196; Liebig
   p.198 (with internal \dots); Nielsen's own „Sagbevægelse" self-quote p.200 (nested „…").
 - No Greek and no math in this batch.
 - Print spellings preserved: „Göthe" (fn p.192), „Vexelbestemmen" (×2, p.191, not -bestemmelse),
   „factisk" (med c, p.199 — cf. batch 16 p.174), „chemiske"/„chemiske", „begrebløs".
Sandbox compile clean: 176 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 19 (2026-07-05): printed pp. 201–211 done & image-verified.
Close of β) Magtens Oprindelighed (pp.201–207): the „Mystificationen…"-self-quote closes on p.201;
the Værens-/Chemien-Vorden contrast; the realistisk fuldkommen Begriben in 3 points (Tingen med
Egenskaber; ydre/indre Relationer; Hvile/Bevægelse); Sølv/Mineralogi as the running example
(Glands, chemisk Tiltrækning); Lovene as Mellembestemmelser; the Vand/Ilt+Brint reflection quote.
Then paragraph **γ) Magtens og Videns oprindelige Eenhed: universalia in re** (p.207) through p.211
— universalia ante/post/in re, the Ørsted „Naturtanker"/„Naturhandlinger rette sig efter
Tankehandlinger" thesis, the Skraaplan-fald example. Ended mid-p.211 „…thi Experimentet faaer just
sin Betydning derved, at der i" (within γ). Verified specifics:
 - γ) rendered as centred bold paragraph-level + \addcontentsline{toc}{paragraph} (mirrors α)/β)).
 - Letterspacing \emph{} (all crop-verified): p.201 \emph{Vorden} (first occ., „Den Vorden, hvorom
   Logiken handler" — the second „den Vorden…Chemien" NOT spaced); p.203 \emph{fra det Enkelte til
   det Almene, gjennem det Enkelte til det concret Almene}, and the two Domme \emph{det Enkelte er
   det Almene} / \emph{det Almene er det Enkelte, ja dette Enkelte}; p.204 \emph{denne Tiltrækning},
   \emph{denne Glands af denne Tiltræknig}, \emph{denne Tiltrækning af denne Glands}, and
   \emph{at objectivere, at gribe, at magte}; p.205 \emph{udvortes} / \emph{indvortes}; p.208 the
   whole set-off sentence \emph{I den evige Fornuft er Viden og Magt oprindelig Eet.}
 - Heiberg footnote (Anfr. Skrft. S.72) inside the Kraft/Magt note on p.209→210: Heiberg's own
   emphases \emph{Betingelsen}, \emph{Existens}, \emph{Nødvendigheden} (first occ. of each only;
   later Betingelsen/Existens/Virksomhed NOT spaced) — crop-verified.
 - Latin set-off terms PLAIN (antiqua→roman): universalia ante rem / post rem / in re, universalia
   sunt in re, in mente, res. NB the γ heading's „universalia in re" is spaced in print → bold heading.
 - MATH footnote p.211 (H. C. Ørsted, Skraaplan): rendered with \[…\] display math inside the
   footnote (compiles clean, verified visually) — $g\frac{a}{l}$; $h=\frac{gat}{l}$,
   $r=\frac{ga}{2l}t^2$; $t_1=l\sqrt{\frac{2}{ga}}$; $t_2=\sqrt{\frac{2a}{g}}$; $\frac{t_1}{t_2}=\frac{l}{a}$.
 - Footnotes placed whole at anchor: p.201 Phil. Propæd. 1861--62 S.55--56; p.204 the „forklare den
   ene Egenskab" note; p.207 Phil. Propæd. 1860--61 S.173--74; p.209 Ørsted Naturl. mech. Deel 1844
   + the long Heiberg/Kraft note; p.210 Ørsted Anfr. Skr. S.202.
 - ERRATA POLICY: transcribe faithfully as printed and flag the errata with a % comment (matches the
   batch-8 precedent, „Functionsbegreb" kept as printed). p.202 „nævne" kept as printed (errata wants
   „nævne:") — flagged. (Remaining in-range errata to flag likewise: S.290 „sind, außer"; S.308 „x + 7".)
 - Print oddity preserved + flagged: p.204 „Tiltræknig" (for Tiltrækning).
Sandbox compile clean: 184 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 20 (2026-07-05): printed pp. 212–222 done & image-verified.
Continuation of γ) universalia in re: the Tankehandling/Naturhandling non-congruence, in mente
humana/divina; the long Heiberg „Slutningen"-quotes on the syllogism E/A/S and „Systemet af de tre
Slutninger"; then the two run-in systems **1) Idealsystemet** (p.216, E---A) and **2) Realsystemet**
(p.220, A---E) with their Domme. Ended mid-p.222 „…er Tankehandlingen iboende; det vil sige: den er
ikke" (still within γ). Verified specifics:
 - Syllogism formulae rendered PLAIN roman capitals + spaced em-dashes (the print sets E/A/S upright
   in antiqua, not italic): E---A, E---S---A, S---E---A, E---A---S, A---E, E---S, S---A, A---S, S---E.
 - Run-in system headings letterspaced: \emph{Idealsystemet} (p.216), \emph{Realsystemet} (p.220) —
   the Domme after them („Det Enkelte er det Almene" etc.) are NOT spaced.
 - Other letterspacing \emph{} (crop-verified): p.213 \emph{Midler}; p.214 \emph{Individ, Art og
   Slægt} (in the Heiberg quote; the body „det Enkelte, det Særskilte og det Almindelige" NOT
   spaced); p.218 \emph{Individ, Art og Slægt}, \emph{Art} (Kategorien Art), \emph{Slægten} (last
   word); p.219 \emph{Slægt}/\emph{Art}/\emph{Art}/\emph{Familien} (the Slægt>Art>Familien contrast;
   „eo ipso" plain, later „en Slægt af høiere Orden" NOT spaced); p.221 \emph{denne}+\emph{disse}×4
   („just er denne Eenhed under disse, just disse Omstændigheder, paa disse, just disse Betingelser"),
   then \emph{Almene}, \emph{særlige Sammenvoxen}, and in the parenthesis \emph{denne}/\emph{disse}
   (×2 each). NB „gjennem Magtbestemmelsernes" between Almene and særlige is NOT spaced.
 - Latin set-off terms PLAIN: in mente, in mente humana/divina, universalia ante/post/in re,
   universalia sunt in re, eo ipso, in concreto, media, res.
 - Footnotes placed whole at anchor: p.213 Heiberg Specul. Log. (Anfr. Skr. S.93 flgd. / Pros. Skr.
   1, S.303--304); p.214 two (Anfr. Skr. S.93; S.97--98); p.215 the long Heiberg Anmærkning with the
   three syllogisms; p.219 two (Forelæsn. Phil. Propæd. 1860--61 S.324--25 and S.325).
 - Print oddity preserved + flagged: p.212 „parrallelt" (for parallelt).
Sandbox compile clean: 192 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 21 (2026-07-05): printed pp. 223–233 done & image-verified.
Finishes γ) (the Tankehandling/reell-Frembringelse argument; the run-in **3) Ideal- og Realsystemets
teleologiske Eenhed** on p.224, letterspaced title \emph{}); the long Heiberg/Hegel „teleologiske
Virksomhed"-quote (pp.224–225, Øiemed/Midlet syllogism E---S---A etc.); Nielsen's critique of the
personified Begreb; then opens the new subsubsection **c) Det logiske Ideal: Begriben og Viden**
(p.230). Verified specifics:
 - Run-in numbered heading: `3) \emph{Ideal- og Realsystemets teleologiske Eenhed}.` (period outside
   emph, matching the 1)/2) pattern).
 - Subsubsection heading c) normalized to the file convention (centered \bfseries + addcontentsline),
   NOT the print's indented-letterspaced form. CONFIRMED by re-rendering the parallel b) heading
   (printed p.177): print sets a)/b)/c) indented+letterspaced, but the transcription renders all three
   as centered bold. Keep this convention for the remaining a/b/c-series headings.
 - Letterspacing \emph{} (crop-verified): p.225 \emph{subjectivt Øiemed}, \emph{Midlet},
   \emph{Øiemedet som objectivt}; p.229 \emph{teleologisk} (only the „og omvendt, er teleologisk"
   instance; the later „teleologisk gjennemsigtige" NOT spaced).
 - German Hegel footnote on p.226 (Wissenschaft d. Logik) emphases (Sperrsatz→\emph): \emph{objektiven
   Gleichgültigkeit und Aeußerlichkeit}, \emph{Aeußerlichkeit}, \emph{Einfachheit}, \emph{Entschluß},
   \emph{ausschließende Einzelnheit}, \emph{Ausschließen}, \emph{entschließt}, \emph{Selbstbestimmen},
   \emph{Setzen seiner selbst}. (The 2nd „objektiver Gleichgültigkeit" NOT spaced.)
 - Syllogism formulae plain roman + spaced em-dashes: E---S---A, S---E---A, E---A---S.
 - Math on p.230 rendered inline: `$0 \cdot \infty$` and `$\infty - \infty$` (indeterminate forms;
   the print's low dot = multiplication).
 - Latin plain: universalia post rem, mirabile dictu.
 - Footnotes placed whole at anchor: p.223 Jvfr. Forelæsn. Phil. Propæd. 1860--61 S.250; p.224 two
   (Taabelige/Forvirrede note; Heiberg Specul. Logik Anfr. Skr. S.107 / Pros. Skr. 1 S.333); p.226 the
   German Hegel quote; p.231 the Poul-Møller „Kjære Jensen!" note.
 - Print oddity preserved + flagged: p.228 „Vexebestemmelse" (for Vexelbestemmelse; cf. p.229
   „Vexelbestemmelsen", spelled with the l).
Sandbox compile clean: 201 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 22 (2026-07-05): printed pp. 234–244 done & image-verified.
Closes the Schelling „Speculation er Alt"-quote (p.234); opens the two Greek paragraph headings under
c): **α) Den intuitive Viden** (p.234) and **β) Den discursive Viden** (p.243). Content: Nielsen's
critique of the 17th-c. Dogmatik's account of Guds Alvidenhed (the Hutterus Redivivus scheme of
divine knowledge), then the Sensualisme/discursive-Viden discussion (opens a block-quote on p.244
that runs past the batch). Verified specifics:
 - Greek paragraph headings normalized to file convention (same as α/β/γ elsewhere):
   `\begin{center}{\bfseries α)\quad Den intuitive Viden.}\end{center}` + addcontentsline paragraph;
   likewise β). (Print sets them indented+letterspaced; we render centered bold — established.)
 - Letterspacing \emph{}: p.234 \emph{den intuitive og den discursive Viden}; the Hutterus scheme
   items p.234–235 \emph{en nødvendig}/\emph{en fri}/\emph{en betinget} (the repeated „Viden" NOT
   spaced) and \emph{intuitiv}/\emph{simultan}/\emph{tydelig}/\emph{fuldkommen sand}; p.235
   \emph{den frie} („Men hvad betyder nu den frie Viden?"); p.236 \emph{nødvendige} („den nødvendige
   Viden"); p.242 „\emph{har}" and „\emph{ikke har}" (Gud „har"/„ikke har", inside the low-high
   quotes).
 - Latin/technical set-off terms PLAIN roman throughout: testimonium spiritus (sancti/stupiditatis),
   scientia necessaria/libera/media/simultanea/distinctissima, qua Deus … perspicit/novit,
   repræsentatio visionis s. intuitionis, pura/immediata, sine sensu/imaginibus/abstractione/discursu/
   ratiocinio, omnium rerum necessitatem, res præter ipsum vere existentes, libertas, reminiscentia,
   visio, præscientia, ad extra, verissima, testimonia, Opinion. æ-ligatures kept (quæ, intelligentiæ,
   repræsentatio, præter, præscientia).
 - Greek Unicode: δόξα (p.240, in „Herlighedens Rige (δόξα)").
 - Numbered lists: letterspaced in the Hutterus quote (see above); the β)-list on p.243 „1)…2)…3)"
   and the run-in „1)" on p.244 are PLAIN (not spaced).
 - Footnotes placed whole at anchor: p.234 Hutterus Redivivus. Leipzig 1836. S.~138--139; p.243 the
   Poul-Møller „Klogskabsregel"/„Den, der vil gjøre Lykke…" note.
 - Open quote left dangling across the marker: the Sensualisme block-quote „Hvad en Fornemmelse er…"
   (p.244) has no visible closing " on p.244 — it continues onto p.245 (next batch closes it).
Sandbox compile clean: 209 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 23 (2026-07-05): printed pp. 245–255 done & image-verified.
Finishes β) Den discursive Viden (the Sensualisme block-quote closes on p.245 „…af høiere Orden end
den psychologiske."; then the intuitiv/discursiv Punkter 2) and 3) with long block-quotes and two
big German footnotes) and opens **γ) Vidensidealet** (p.253). Verified specifics:
 - γ) heading rendered per file convention: `\begin{center}{\bfseries γ)\quad Vidensidealet.}\end{center}`
   + addcontentsline paragraph.
 - Letterspacing \emph{} (crop-verified on p.250): the stage-name triad „den \emph{umiddelbare}, den
   \emph{reflecterende} og den \emph{begribende} Subjectivitet" (the noun „Subjectivitet" NOT spaced
   in that first triad); „Medens den \emph{umiddelbare} Subjectivitet"; „indsaae den
   \emph{reflecterende} klart"; „for den \emph{begribende Subjectivitet} udtrykkelig" (here BOTH
   words spaced); „\emph{Forstandsreflexionen} … \emph{Væsensreflexion}". No letterspacing on any
   other page of the batch (245–249, 251–255 bodies are plain).
 - Two large German footnotes placed WHOLE at their anchors (each spans two printed pages in the
   original but is one logical note): p.246 Kant (Jäsche Logik / Hartenstein 1838) — Sperrsatz→\emph:
   \emph{logische}, \emph{intuitiven und discursiven}, \emph{ästhetischen und der logischen},
   \emph{allgemeingültigen} (only the FIRST „allgemeingültigen"; the later „objectiv- und
   allgemeingültigen" NOT spaced); p.251 Hegel Phänomenologie (Werke 2te Bd. Berlin 1832) — \emph:
   \emph{Wissenschaft}, \emph{Bestimmtheit}. Third footnote p.254: „Philosophie og Mathematik.
   Kjøbenhavn 1857 S.~41."
 - Latin set-off terms PLAIN: sine abstractione/discursu/ratiocinio, a priori (in the German
   quotes). Danish „a er, saa er b" n/a here.
 - Print oddity kept as-is (faithful): in the Kant footnote „Vollkommennheit" (double-n; printer's
   error for „Vollkommenheit").
 - Numbers kept as digits: „477 Billioner Svingninger".
Sandbox compile clean: 217 pp., 0 errors, 0 char-warnings, 1 marker.

## Body batch 24 (2026-07-05): printed pp. 256–266 done & image-verified.
Finishes **γ) Vidensidealet** (the ontological account of Sandsning, Idealsystem/Realsystem
Vexelbestemmelse, discursiv/intuitiv Viden) which CLOSES the chapter on p.263 with a centered rule;
then opens the new **Andet Kapitel: Functioner af subjectiv Viden: Objectivitetens Logik** on p.264
(distinction Objectivitetens vs. Objecternes Logik). Verified specifics:
 - New chapter heading rendered per file convention (mirrors Første Kapitel): centered
   `{\large\bfseries Andet Kapitel.}\\[3pt]{\Large\bfseries Functioner af subjectiv Viden:
   Objectivitetens Logik.}` + `\addcontentsline{toc}{section}{…}` + `\markboth{Videns Idee}{Objectivitetens Logik}`.
   Preceded by `\begin{center}---\end{center}` (the printed end-of-chapter rule on p.263).
 - Letterspacing \emph{} (all crop-verified): p.257 German Hegel quote „…der sich \emph{selbst}
   wissende … zum \emph{Gegenstande habende} Begriff …" (the later „die er selbst ist" NOT spaced);
   p.260 „svarende til \emph{Idealsystemet} … svarende til \emph{Realsystemet}" (the later
   „Anderledes, naar vi see paa Realsystemet" NOT spaced); p.263 „den \emph{discursive} Videns"
   (single word; the later „intuitiv og discursiv Viden" NOT spaced) and „…antager Charakteer af
   \emph{intuitiv Viden}"; p.265 „Forskjel imellem \emph{Objectivitetens} og \emph{Objecternes} Logik"
   (the many later „Objecternes/Objectivitetens Logik" NOT spaced); p.266 „berige Begrebet
   \emph{Object} med nye" (concept-word spaced across a line break; written as one \emph, no literal
   hyphen since it is a within-page break not a page break). No other letterspacing in the batch.
 - One footnote placed whole at anchor: p.256 Hegel, at „…ist alle Wahrheit": `\footnote{Hegel Die
   subjektive Logik.\ Werke 5te Band.\ Berlin 1834 S.~238.}` (note „subjektive" with k, faithful).
 - German quote spans p.256→257 („…und ist alle Wahrheit…"; fremdeles „Die | Methode ist daraus…");
   Danish „…" quotes throughout (Affectioner, Functioner, den vidende Sandhed, nøgne Monader, Men…).
 - French/Latin set-off terms PLAIN roman: (perceptions petites) p.259, adæqvate, a priori n/a.
 - Abbrev spacing applied: „o.\ s.\ v." (p.258, p.264), „f.\ Ex." (p.262, p.264), „S.~238".
 - All page breaks in this batch are between-word (no mid-word splits); each marked `% p. NNN`.
Sandbox verify compile (portable preamble — libertinus/babel-danish absent in fresh sandbox, swapped
to fontspec/Latin Modern for the check): full document built, 0 fatal errors, braces balanced 22/22,
9 \emph + 1 \footnote + 1 chapter heading as intended; chapter heading + emphases spot-checked in the
rendered PDF. (Real compile with libertinus+textalpha is Hans's; Greek/microtype warnings in the
verify run are font-substitution artifacts only.)

## Body batch 25 (2026-07-05): printed pp. 267–277 done & image-verified.
Continues **Andet Kapitel (Objectivitetens Logik)**: closes the Objecternes-vs-Objectivitetens-Logik
discussion, the ontological Objectivering (Grund/Existens Fordobling), the Function-category
argument, and OPENS subsection **A. Functionernes Logik** (p.274). Verified specifics:
 - New subsection heading rendered per file convention (mirrors A./B./C. of Kap. 1): centered
   `{\bfseries A.}\\[2pt]{\large\bfseries Functionernes Logik.}` + `\addcontentsline{toc}{subsection}{A. Functionernes Logik}`.
 - Letterspacing \emph{} (all crop-verified): p.270 „…baade Grund og Existens: \emph{Existens},
   forsaavidt … sin Grund; \emph{Grund}, forsaavidt" (the earlier „baade Grund og Existens" NOT
   spaced — only the two definitional terms after the colon); p.273 „ved Kategorien \emph{Function}",
   „d.\ v.\ s. til en \emph{Functionernes Logik}" (earlier „Functionernes Væsen" NOT spaced), „af de
   i egentlig Forstand \emph{logiske Functioner}", „i \emph{Functionernes Systematik}", „Hvad
   \emph{Functionernes Logik} angaaer"; p.274 „Hvad \emph{de logiske Functioner} angaaer", „Hvad
   endelig \emph{Functionernes Systematik} angaaer"; p.276 „…betegnende Udtryk: \emph{Function}."
   (the later „Kategorien Function er" NOT spaced) and in the p.276 footnote „Ordet \emph{Function}
   forekommer" (later „Function" occurrences in that footnote NOT spaced). No other Sperrsatz in the
   batch (pp.267–269, 271–272, 275, 277 bodies plain; „det Mathematiske/Mineralogiske angaaer" on
   p.267 NOT spaced).
 - Three footnotes, each placed WHOLE at its anchor: p.267 (spans 267→268) the long Hegel/centrifugal
   note — quotes „Naar Forstanden…", „Phil.\ Propæd.“, and a German „…„ein plötzliches Umschlagen“…"
   with em-dashes, refs 1861--62 S.~29--34, (Anfr.\ Str.~95--98), (Anfr.\ Str.\ S.~64--65); p.275
   „Den propæd.\ Logik.\ S.~182."; p.276 (spans 276→277) the „Ordet Function…" note ending „Phil.\ og
   Mathem.\ S.~5--6." — contains INLINE MATH (rendered & spot-checked): $x$, Addend $(a + x)$, Factor
   $(ax)$, Potensexponent $(a^{x})$, and the Ramus formula $y = f(x, z, t, u \ldots)$; ellipses as
   `\ldots`.
 - Mid-word page-break splits (literal hyphen + `% p. NNN` + continuation, per file convention):
   p.271→272 „det Vir-|kelige", p.273→274 „hvis Vidt-|løftighed". All other breaks between-word.
 - Latin set-off „in concreto" (p.277) PLAIN roman.
Sandbox verify compile (portable preamble): full document built (235 pp.), 0 fatal errors, braces
balanced 23/23, 22 math-$ (balanced), 11 \emph + 3 \footnote + 1 subsection heading as intended;
A. heading, „Udtryk: Function." emphasis, nested example-quotes, and the math footnote all
spot-checked in the rendered PDF.

## Body batch 26 (2026-07-05): printed pp. 278–288 done & image-verified.
Continues **A. Functionernes Logik** (Function = lovbestemt Afhængighed; math & physiology critique;
Function's mathematical vs. real meaning), then OPENS subsubsection **a) Functioner af Grunden**
(p.286) and paragraph **α) Functioner af den formelle Grund** (p.287). Verified specifics:
 - Two headings per file convention: `\begin{center}{\bfseries a)\quad Functioner af Grunden.}\end{center}`
   + subsubsection addcontentsline; `\begin{center}{\bfseries α)\quad Functioner af den formelle
   Grund.}\end{center}` + paragraph addcontentsline.
 - Letterspacing \emph{} (all crop-verified): p.278 „er Afhængigheden, \emph{den lovbestemte
   Afhængighed}", „Begrebet \emph{Function} staaer med Begrebet \emph{Afhængighed, lovbestemt
   Afhængighed}", „Eenhedsudtrykket, \emph{lovbestemt Afhængighed}"; p.284 „er \emph{Grund}, og at
   Grunden" (Grunden NOT spaced); p.285 „som \emph{Functioner af Grunden}", „som \emph{Functioner af
   Aarsagen}", „altsaa: en \emph{Grundaarsag}" (later „Som Grundaarsag" NOT spaced), „et
   eiendommeligt \emph{Anlæg}" (later „som Anlæg" NOT spaced); p.286 „som \emph{Functioner af
   Grundaarsagen}", „charakteriserer \emph{Functionerne af den formelle Grund}" (later „reelle Grund"
   NOT spaced), „skulle kjende \emph{Functionerne af den reelle Grund}"; p.287 „Særkjendet for
   \emph{Functionerne af den blandede Grund}"; p.288 „der handler om \emph{Qvaliteten}" (later
   „Qvalitet" NOT spaced), „i det Sandselige \emph{dette Sandselige}" (later „dette Sandselige" NOT
   spaced). No other Sperrsatz in the batch bodies (pp.279–283 plain).
 - INLINE MATH (rendered & spot-checked): p.278 the Mathematik quote — $2 = 3^{2} - 7$, $= 3 - 1$,
   $= 3^{3} - 25$, $y = x^{2} - 7$, $y = 2$, $x = 3$, and $f(x)=y$, $f(x)=ax$, $f(x)=x^{2}$,
   $f(x)=a^{x}$; p.282 $y = f(\varphi(x))$.
 - Four footnotes, each placed WHOLE at anchor: p.278 „Om „Functionsbegrebet“ jvfr.\ Mathem.\ og
   Dialekt.\ S.~4--27." (Functionsbegrebet NOT spaced); p.281 „Jvfr Forelæsn.\ over „Phil.\ Propæd.“
   Universitetsaar 1860--61, S.~367 flgd."; p.283 „Mathem.\ og Dialekt.\ S.~25."; p.287 (spans
   287→288) the LONG German Hegel quote (Allgemeiner Begriff der Logik, Anfr.\ Udgv.\ S.~35) with
   extensive Sperrsatz — image-verified best-effort: \emph on Wahrheit (×2), Gegenstandes, „Gewißheit
   seiner selbst", Gedanken, „eben so sehr die Sache an sich selbst", „Sache an sich selbst", „ebenso
   sehr der reine Gedanke", „an und für sich seyende" (×2), Inhalt, Dieses, „an und für sich selbst",
   „in seinem ewigen Wesen vor der Erschaffung der Natur und eines endlichen Geistes", and (Danish
   tail) Idealsystemet; ellipses in the quote as `\ldots`. [A couple of short-word run boundaries in
   this footnote are pixel-ambiguous; erred toward the contiguous spaced runs.]
 - Latin set-off „Non datur metaphysica in mathesin via." (p.283) PLAIN roman; „in concreto" n/a here.
 - Mid-word page-break splits (literal hyphen + `% p. NNN` + continuation): p.278→279 „at be-|stemme",
   p.279→280 „Trods alle For-|sikkringer", p.283→284 „dens betin-|gede", p.285→286 „eiendommelige
   Virke-|maader". All other breaks between-word.
Sandbox verify compile (portable preamble): full document built (244 pp.), 0 fatal errors, braces
balanced 52/52, 42 math-$ (balanced), 30 \emph + 4 \footnote + 2 headings as intended; a) heading,
the full German footnote emphases, and „om Qvaliteten" spot-checked in the rendered PDF. (α renders as
a substitution glyph in the verify run only — libertinus+textalpha handle it in Hans's real compile.)

## Body batch 27 (2026-07-05): printed pp. 289–299 done & image-verified.
Continues **a) Functioner af Grunden** (Qvalitet vs. Qvantitet as Function-spheres; the two Heiberg
category-schemata; the constant/variable Størrelse analysis). VERY letterspacing-dense batch (Heiberg
quote-schemata on pp.290, 293–294). Verified specifics:
 - Two Heiberg schemata rendered inline with \emph on the spaced category names: p.290 „1) \emph{Absolut
   Væren}: a) … 2) \emph{Tilværen}: a) … 3) \emph{Eenhed af Væren}: a) …"; p.293 „1) \emph{Absolut
   Qvantitet}, 2) \emph{Qvantitativ Tilværen}, 3) \emph{Eenhed af qvantitativ Væren}" then the numbered
   run-in exposition 1./2./3. with \emph on each spaced technical term.
 - Letterspacing \emph{} (all crop-verified): p.292 „resulterende \emph{Eenhed af Væren}" (Heiberg);
   p.293 1a \emph{Discretion}; 1b \emph{Vorden}, \emph{Qvantum}, \emph{Størrelse}, c „det \emph{bestemte
   Qvantum eller den bestemte Størrelse}"; 2a \emph{qvantitativ Eenhed}; 2b \emph{Antal}; 2c \emph{Tal};
   3a \emph{Sum}, \emph{numerere eller tælle}, \emph{addere}; p.294 3b \emph{multiplicere},
   \emph{Eenhed}; 3c \emph{Qvadratet}, \emph{qvadrere}; body „at \emph{tælle}, at \emph{multiplicere},
   at \emph{qvadrere}"; p.296 „i \emph{Fleerheden}"; p.297 „et Blik paa \emph{Functionsbegrebet}";
   p.298 „den \emph{constante Størrelse}", „Størrelsen \emph{variabel}", „At Bestemmelsen: \emph{variabel}
   … som Bestemmelsen \emph{constant}". German-quote Sperrsatz: p.294 „das \emph{Daseyn} … \emph{zugleich}",
   p.295 „\emph{zugleich} … überhaupt \emph{außer sich}, ein sich schlechthin \emph{Aeußerliches}". Many
   parallel occurrences of the same words were NOT spaced and left plain (crop-checked each).
 - INLINE MATH (rendered & spot-checked): p.297 fn $y=f(x,z,t,u \ldots)$; p.298 „$f(x)=ax$", „$f(a)=ax$",
   „$a=a$"; p.299 „$x=x$", „$f(x)=ax=f(x)$", „$f(x)=y=ax$" plus single-letter vars $a,x,y$.
 - Seven footnotes placed WHOLE at anchor: p.290 German Hegel (Seyn/Nichts; Anfr.\ Str.\ S.~82) —
   NO Sperrsatz; p.292 „Heiberg.\ Anfr.\ Str.\ S.~17. (Prof.\ Str.\ 1ste Bind S.~138.)"; p.295 „Anfr.\
   Str.\ S.~209" and „Anfr.\ Str.\ S.~249"; p.297 „Jvfr.\ Mathematik og Dialektik…1859" and the math fn;
   p.299 „Mathem.\ og Dialekt.\ S.~5--7".
 - ERRATA (Trykfeil) S.290: kept as printed „so sind außer, dem Werden selbst" (source-errata corrects
   to „sind, außer dem Werden") — flagged with a % comment in situ.
 - Print oddity: p.293 3a) the opening „ before „Tallet" is MISSING in the original (1a/2a have it);
   supplied for quote-balance and flagged with a % comment.
 - Faithful spellings kept: „hume'ske" (p.289), „Bibestemmelse" (p.296), „Qvalität"/„Etwas von Grenze"
   in the p.290 German quote.
 - Mid-word page-break splits (literal hyphen + `% p. NNN`): p.290→291 „et-|hvert", p.292→293
   „umiddel-|bare". Other breaks between-word; p.297→298 is a same-paragraph continuation (no indent).
Sandbox verify compile (portable preamble): full document built (252 pp.), 0 fatal errors, braces
balanced 47/47, 44 math-$ (balanced), 39 \emph + 7 \footnote as intended; both Heiberg schemata, the
math, „Functionsbegrebet", and the two spacing fixes (after „Sum." and after the p.290 footnote)
spot-checked in the rendered PDF.

## Body batch 28 (2026-07-05): printed pp. 300–310 done & image-verified.
Continues **a) Functioner af Grunden** into paragraph **β) Functioner af den reelle Grund** (opens
p.301): the Qvalitet→Qvantitet→Modalitet (Maal) transition, Heiberg's Qvadrat/Potens critique, the
intensive/extensive (Grad, Varmegrad) analysis. Math-dense (Potenser, fractions). Verified specifics:
 - Heading β) per file convention (centered bold + paragraph addcontentsline).
 - Letterspacing \emph{} (all crop-verified): p.302 „eller \emph{Modalitet}" (end of Heiberg quote)
   and „ved \emph{Modalitet} eller \emph{Maaden} af Tilværen"; p.303 „Kategorien \emph{Produkt} …
   Kategorien \emph{Qvadrat}"; p.308 „ved Functionen \emph{Qvotient}"; p.309 „Kategorien \emph{Grad}"
   and „Forhold er \emph{Grad}" (the two „en Grad af…" instances NOT spaced); p.310 „Qvaliteten
   „\emph{extensiv}"". German-quote Sperrsatz only in the p.304 fn („ist \emph{das Qvadrat}: die Größe
   außer sich \emph{kommend} … aber \emph{nach keiner andern als ihrer eignen Bestimmtheit}" — spans
   304→305, best-effort). Main German quotes on pp.304, 306 had NO Sperrsatz (crop-checked).
 - INLINE MATH (rendered & spot-checked): p.300 $F(x,y,z)=0$; p.303 „Eet $=$ Eet"; p.305 $f(x+y)=f(x)f(y)$,
   $f(x+y)=f(x)+f(y)$; p.306 $n,n^{2},n^{3},n^{4},n^{5}\ldots$, $n^{n}$, $n:n=1$; p.307 $=1$, $1:1$/$2:2$/$3:3$,
   $2:4$/$3:6$/$4:8$, $27$, $3^{3}$, $3,3^{2},3^{3},3^{4}$, $3^{n}$; p.308 FRACTIONS $\varphi(\psi(x))=x$,
   $\psi(x)=\frac{x}{a}$, $\varphi(x)=ax$, $\frac{x}{x}$, $1=f(x)$, $a=\frac{x}{y}$, $a=F(x,y)$, $a=\pm x y$.
 - Nine footnotes placed WHOLE at anchor: p.300 (Mathm.\ og Dialekt.\ S.~20); p.301 (Anfr.\ Str.\ S.~147;
   Anfr.\ Str.\ S.~148); p.302 (Anfr.\ Str.\ S.~22 …S.~150); p.304 (Logik 1ster Theil …S.~391--92; German
   „Die der Einheit…" spanning 304→305); p.305 (Heiberg …S.~24 …S.~153); p.307 (Heiberg …S.~24--26 …S.~156--57);
   p.309 (Heiberg …S.~26 …S.~157).
 - ERRATA (Trykfeil S.308 Lin.3 f.n.): printed formula „a = ± x y" KEPT as printed and flagged with a %
   comment (the registered correction „+x5"→„x + 7" is itself garbled/uncertain; the page clearly prints
   „a = ± x y").
 - Faithful: „Mathm." (p.300 fn, not „Mathem."), „das Maaß"/„Qvalität"/„Etwas von Grenze" spellings.
 - Mid-word page-break splits: p.299→300 „Subjectivi-|teten", p.300→301 „Qvantitetskate-|goriernes",
   p.301→302 „qvanti-|tative", p.303→304 „Moda-|litetens". Other breaks between-word; p.305 & p.310
   openings are same-paragraph continuations / new paragraphs verified by first-line indent.
Sandbox verify compile (portable preamble): full document built (260 pp.), 0 fatal errors, braces
balanced 48/48, 72 math-$ (balanced) + 3 \frac, 12 \emph + 9 \footnote as intended; the exponents,
ratios, and inline fractions, plus „Qvotient"/„Grad"/„extensiv", spot-checked in the rendered PDF.

## Body batch 29 (2026-07-05): printed pp. 311–320 done & image-verified. **>=70% MILESTONE REACHED.**
Finishes the Grad/Maal (measure) analysis, the reelle-Grund Functions (Newton's law worked example),
and OPENS paragraph **γ) Functioner af den blandede Grund** (p.316). Verified specifics:
 - Heading γ) per file convention (centered bold + paragraph addcontentsline).
 - Letterspacing \emph{} (all crop-verified): p.311 „Kategorierne \emph{Grad og Grund} staae" and
   „er \emph{Maal}, som altsaa bestaaer"; p.317 „saa have vi her en \emph{Function af den blandede
   Grund}"; p.320 German fn „so ist die \emph{Temperatur} eine Qvalität" (only that one word spaced —
   rest of the long Hegel fn crop-checked and tight). Recurring terms constant/variabel (p.313),
   Maal og Maalestok / Grad og Intensitet (p.315), Grad/Varmegrad (throughout) all crop-checked and
   NOT spaced. The p.317→318 German quote „…hat ein Maaß…zu Grunde ginge" has NO Sperrsatz.
 - INLINE MATH incl. DISPLAYED FRACTIONS (rendered & spot-checked): p.312 $2:4$/$2:6$/$2:8$,
   $1:1$/$2:2$/$3:3$, $=1$; p.313 $T=F(x)=\frac{a}{x^{2}}$, vars $a,T$; p.314 $x=1$, $a=T$, $\frac{a}{x^{2}}$,
   $\frac{1}{x^{2}}$; p.315 $\frac{1}{x^{2}}$, $\frac{a}{x^{2}}=F(x)=T$, vars $x,T,F(x)$; p.318 $y=f(x)$,
   $dx$, $dy$; p.319 $0$/$1$ + Greek μέτρον (unicode; renders via textalpha in real compile).
 - Three footnotes placed WHOLE at anchor: p.312 (Heiberg …S.~27 …S.~159); p.317 (Logik 1ster Theil
   …S.~403--404); p.320 the long German „Um ein Beispiel…" (Hegel Logik.\ 1ster Theil S.~410--411).
 - All page breaks between-word except p.312→313 (paragraph break, new „Det for Graden") — no mid-word
   splits this batch.
Sandbox verify compile (portable preamble): full document built (268 pp.), 0 fatal errors, braces
balanced 35/35, 86 math-$ (balanced) + 7 \frac, 4 \emph + 3 \footnote + 1 heading as intended; the γ
heading, the „Grad og Grund"/„Maal"/„Temperatur" emphases, and the inline fractions spot-checked in the
rendered PDF (γ renders as a substitution glyph in the verify only — libertinus+textalpha handle it in
Hans's real compile).

### Batch 30 (printed pp. 321–331, PDF 359–369) — DONE & image-verified
 - Ends a) Functioner af Grunden, γ) blandede Grund (Cohæsion/Smeltning/Svovl example, chemical
   proportions) and opens **b) Functioner af Aarsagen** (subsubsection heading on p.329, mechanisk/
   dynamisk Virksomhed, the Hegel „Chemisme" quote).
 - **Berzelius manganese-oxide notation** (p.323 formula line + p.324 named list, both identical,
   each symbol zoom-verified): 5 oxides as over-dotted M — Forilte $\dot{\mathrm M}$n (1 dot),
   Tveilte $\dddot{\mathrm M}$n₂ (3), Overilte $\ddot{\mathrm M}$n (2), Syre $\dddot{\mathrm M}$n (3),
   Oversyre $\ddddot{\mathrm M}$n₂ (4). Rendered with amsmath \dot/\ddot/\dddot/\ddddot + flag comment;
   renders correctly in verify PDF. Berzelius sulphur $\ddot{\mathrm S}$ (2 dots) in the p.328
   thermochem formulas (R,O,S̈ Aq) etc.
 - Temperatures as $NNN^{\circ}$ (111/160/200/400; 350/1410/2230/4340/4690). Three display formulas
   on p.328, one W=f(i,i',i''…) formula on p.329 (footnote *) attached).
 - Footnotes (all whole at anchor): p.323 „Phil. Præpæd." 1860–61; p.327 Tidsskrift for Physik og
   Chemie 1862; p.329 J. Thomsen, Bidrag til et thermochemisk System 1853.
 - Letterspacing (\emph): p.321 en blandet Grund, udefter, indefter; p.325 blandede Grund; p.327 the
   whole letterspaced Spørgsmaal „Hvilke Metaller…Brintudvikling?"; p.329 var vistnok…Methode.;
   p.330 mechaniske/dynamiske, Stød, meddeles, Indifferens, Kraft, Bevægelse, Hvile, Centralitet,
   Differens, dynamisk; p.331 Affinitet, meddeles. All crop-verified; parallel plain occurrences left plain.
 - Mid-word page breaks: Func\-/tionsbegrebet (323→324), Mangan\-/foriltesaltene (325→326),
   Aarsags\-/forhold (329→330), For\-/ening (330→331). Others between-word.
 - FLAG: p.328 closing quote after „2230°" has no matching opening on the page (likely printer's
   omission) — transcribed as printed, % comment in situ.
 - Verify compile (portable preamble): 276 pp., only the expected microtype/xetex artifact, braces
   997/997, math-$ balanced, 4 display formulas balanced; oxide dot-accents + emphasis spot-checked
   in rendered PDF (p.271 of verify).

### Batch 31 (printed pp. 332–342, PDF 370–380) — DONE & image-verified
 - Within b) Functioner af Aarsagen; opens **α) Mechaniske Functioner** (paragraph heading on p.334,
   centered bold + \addcontentsline paragraph). Mechanisk/dynamisk, Schelling, Inertie/Kraft, the
   thermochem-free mechanics of jevn Bevægelse (Taylor series).
 - **Schelling Potenz notation** (p.333–334): $A=A$, $\overset{+}{A}=B$, $A=\overset{+}{B}$ (+ over the
   letter, crop-verified); $A^{2}$, $A^{3}$; "(E — S — A)" kept as printed em-dashed letters.
 - **Big two-page footnote (p.339–340)** anchored on p.339: whole quote „Forsaavidt s er…Uendelige."
   with a single Taylor-series display eqn + a 3-line aligned system ($f(t+h)=…$, $=\ldots+v…$,
   $=\ldots+\ldots+\varphi…$). Rendered with `\[\begin{aligned}…\end{aligned}\]` INSIDE `\footnote{}` —
   verified to compile & render (verify p.282). φ = \varphi; "1·2·3" = `1\cdot 2\cdot 3`.
 - Other math: p.336 $v=\frac{s}{t}$, $v=\frac{ds}{dt}$; p.339 $\frac{ds}{dt}=a$, $\frac{d^{2}s}{dt^{2}}=0$;
   p.341 $\frac{ds}{dt}=C$, $C=0$; p.342 $\frac{dv}{dt}=\frac{d.\,\frac{ds}{dt}}{dt}=\frac{d^{2}s}{dt^{2}}$.
 - Footnotes (all whole at anchor): p.332 Phil. Propæd. 1857 S.52; p.334 Jvfr. Philos. Propæd. 1857
   S.50–51; p.336 Mathem. og Dialektik S.23–25; p.339–340 the big Taylor one (…Dialktk. S.78–88);
   p.341 „En foraarsaget Hvile…". NB source spells the title „Phil. Præpæd." on p.323 but „Phil.
   Propæd."/„Philos. Propæd." on pp.332/334 — transcribed faithfully as printed (source inconsistency).
 - Letterspacing (\emph): p.333 Selv, Lyset, Stjernen, Solen; p.336 Hastighed, Inertie, Kraft,
   bevægende Kraft, levende Kraft; p.340 footnote Bevægelse, Hastighed, Kraft, Forandring i Kraft.
   All crop-verified; parallel plain occurrences left plain.
 - Latin antiqua rendered plain roman: "vere scire est per causas scire", "res iners", "vis inertiæ",
   "lex inertiæ", "posse etiam rudes mechanice totam logicam doceri, ut pueri mathematicam docentur".
   German quotes with umlauts/ß: „die für die Erkenntniß des Lichts nichts nutzen", „Trägheit",
   „Es bewegt sich…der Verrücktheit."
 - ERRATUM (in situ flag): p.337 "at at" dittography at the line break ("saa langt fra at / at være
   adæqvat") — transcribed faithfully, % comment.
 - Mid-word page breaks: Indiffe\-/rensen (336→337), „den en\-/kelte (337→338). Others between-word.
 - Verify compile: 284 pp., only the expected microtype/xetex artifact; braces 1133/1133, inline-$
   even, aligned 1/1; Potenz notation, the footnote equations, and all emphasis spot-checked in
   rendered PDF (verify pp. 279–282). α heading renders as substitution glyph in verify only
   (libertinus+textalpha handle it in Hans's real compile).

### Batch 32 (printed pp. 343–353, PDF 381–391) — DONE & image-verified
 - Still within b) Functioner af Aarsagen, α) Mechaniske Functioner. Kræfternes Udmaaling (Ramus),
   accelererende/bevægende Kraft, Rum/Tid/Materie, mechaniske Produkter (gt, mv, mgs), Arbeidskraft
   og levende Kraft.
 - Math: p.343 $P=Q$, $Q=R$, $P=R$, $P=P'$, $Q=Q'$, $P+Q=P'+Q'$; p.344 display
   $\psi=\frac{d\varphi}{dt}=\frac{d^{2}v}{dt^{2}}=\frac{d^{3}s}{dt^{3}}$, φ/ψ/ω = \varphi/\psi/\omega,
   $v=\varphi t$, $\varphi=f(t)=\psi t$; p.345 $\mathrm{MA}_1,\mathrm{MA}_2,\mathrm{MA}_3\ldots$;
   p.348 display $\left(\frac{d^{2}x}{dt^{2}}\right)^{2}+\dots\div p^{2}=0$ (÷ = \div); p.349 $\frac{s}{t}=v$,
   $g=v$, $v=f(t)=gt$; p.350 $v=gt$→$mv=mgt$; p.351 $g=g$, $g,2g,3g,4g$, $v=f(g)=tg$, $g\,dt$, $dv$;
   p.352 $\frac{ds}{dt}=v$, $dt=\frac{ds}{v}$, $mg\frac{ds}{v}=mdv$; p.353 $mgds=mvdv$,
   $mgs=\frac{mv^{2}}{2}$, $mv^{2}$, $2mgs$. All display eqns render (verify p.289).
 - Footnotes (whole at anchor): p.343 Ramus. Analytisk Mechanik. Kbhvn. 1852 S.4; p.345 C. Ramus,
   Analyt. Mechan. S.4.
 - Letterspacing (\emph): p.343 "mechaniske Kræfters gjensidige Uafhængighed af hinanden"; p.345
   "Kraften er ligestor med Linien"; p.349 paa, "en bevægende Kraft"; p.350 "mechaniske Produkter og
   mechaniske Begreber"; p.351 Bevægelsesmængde; p.353 Arbeidskraften, "levende Kraft". All crop-verified.
 - French antiqua rendered plain roman: "force accélératrice", "force motrice", "force vive",
   "points d'applications".
 - Mid-word page breaks: va\-/riabel (343→344), Begyn\-/delsen (345→346), vir\-/kende (349→350).
   Others between-word.
 - Verify compile: 293 pp., only the expected microtype/xetex artifact; braces 1199/1199, inline-$ even;
   coordinate & Taylor display eqns and all emphasis spot-checked in rendered PDF (verify p.289).

### Batch 33 (printed pp. 354–364, PDF 392–402) — DONE & image-verified
 - Opens **β) Dynamiske Functioner** (paragraph heading on p.354). Critique of Hegel/Schelling
   Naturphilosophie; long German quotations (Bayrhoffer, Hegel Encyclopädie/Vorlesungen); the
   Continuity/Discretion calculus (Continuitet af 1./2./3./nte Orden) ending in a triple integral.
 - **Very heavy German Sperrsatz** on pp.357–359 (Bayrhoffer/Hegel quotes) — every letterspaced word
   crop-verified band-by-band and set as \emph: e.g. Hegels, Begriff, Phantasie, Grund; dynamische,
   die Wiederholung, der Besonderung, physikalischen Bestimmtheit, tellurische, Schwere, physikalischen,
   freien Gestalt, Magnetismus, engegengesetztes, Einen Körper, Cohäsion, Klang, specificirt, frei,
   Electrismus, polarisirtes, Differenz, reellen, Farbe, Wärme und Feuer, realisirt, Galvanismus, fort,
   deren, solare, einfach, bestimmt, Sauerstoffs, allgemein in sich reflectirte, dynamischen, Seele,
   selbst, reflectirte Insichsein, Sensibilität, Empfindung, Anderes, Irritabilität, Reproduction.
   Danish Sperrsatz: p.361 dynamisk; p.362 Continuiteten af første Orden, umiddelbart, Continuitet af
   anden Orden; p.363 Continuiteten er af tredie Orden.
 - Math: p.362 $s=f(t)=vt$, $v=a=\frac{ds}{dt}$, $v_{1},v_{2},\ldots v_{n}$, $v_{p}-v_{p-1}=dv$,
   $ds_{1}\ldots ds_{n}$, the stacked "> over <" relation (printed ≷) rendered
   `\mathrel{\substack{\textstyle> \\ \textstyle<}}` (amsmath-only, NOT \gtrless — that needs
   amssymb/libertinust1math), $dv\,dt=d^{2}s$, $s=at^{2}$; p.363 $s=at^{3}$, $d^{3}s$,
   $\frac{d^{n}s}{dt^{n}}=C$, $n^{\mathrm{te}}$, $n=\infty$, $s=\cos t$; p.364 $\varrho v=M$, polar
   $dP=p\,r^{2}\,dr\,\sin\alpha\,d\alpha\,d\theta$, and a stacked triple-integral display
   ($P=p\iiint\ldots=\tfrac{4}{3}p\pi a^{3}$) in `\[\begin{aligned}…\end{aligned}\]`. All render (verify p.301).
 - Footnotes (whole at anchor): p.355 two (Phil. Propæd. 1860–61 S.177–200; 1861–62 S.57–66); p.356
   two (Phil. Propæd. 1861–62 S.73–74; Hegel Vorlesung. üb. d. Naturphil. Werke 7ter Bd. 1. Abtheil.
   Berl. 1842 S.97); p.357 two (Beiträge zur Naturphilosophie. Leipzig 1839; Anfr.-Skr. Indledning
   S.14); p.358 Anfr. Skrift. S.92–94; p.359 Anfr. Skr. S.129; p.363 Phil. Propæd. 1860–61 S.77–79.
 - ERRATA (in-situ % flags): p.363 S.363 "cos.t,"→"cost," (transcribed as printed, $s=\cos t$). ALSO
   retro-added the two Batch-31 errata flags I'd missed: S.335 "det i Mechaniske"→"i det Mechaniske,"
   and S.337 "Inertie, ved Stød og Bevægelse,"→"Inertie og Bevægelse ved Stød,".
 - Mid-word page breaks: speci\-/ficirt (357→358), zur Seele re\-/flectirt (358→359), intellectuel
   An\-/skuelse (359→360), Functionslæren og da til\-/lige (361→362), Materien alt\-/[saa] (364→365).
   Others between-word.
 - Verify compile: 301 pp., only the expected microtype/xetex artifact + textalpha-Greek substitution
   (β heading, plus the Indledning motto); 0 undefined control seqs; braces 1316/1316. German Sperrsatz,
   ≷ relation, triple integral spot-checked (verify pp.296, 299, 301).

### Batch 34 (printed pp. 365–375, PDF 403–413) — DONE & image-verified
 - Finishes β) Dynamiske Functioner (Discretion→Continuity limit; Cartesius/Gassendi; isomerism/
   chemical formulas) and opens **γ) Æsthetophysiske Functioner** (paragraph heading on p.369; the
   Hegel Klang/Licht critique with long German quotations).
 - Math: p.365 $M,dM,P,dP$; p.366 $\mu,\sigma$, $\sigma=q\mu$, $\frac{\sigma}{\mu}=q$; p.367
   $\frac{d\sigma}{d\mu}=q$, $d\sigma=q\,d\mu$, $d\mu$; **chemical formulas** p.368–369 rendered
   $\mathrm{C}_{4}\,\mathrm{H}_{6}\,\mathrm{O}_{3}+\mathrm{C}_{2}\,\mathrm{H}_{6}\,\mathrm{O}$ etc.
   (subscripts verified: 4-6-3, 2-6, 2-2-3, 4-10; also C₆H₁₂O₄, and $\mathrm{C}=\mathrm{C}$,
   $\mathrm{H}=\mathrm{H}$, $\mathrm{O}=\mathrm{O}$). All render (verify p.304).
 - Footnotes (whole at anchor): p.365 Mathm. og Dialekt. S.127–129; p.368 Phil. Propæd. 1860–61
   S.155–156; p.370 Naturphil. S.207; p.372 two (Hegel. Anfr. Skr. S.208; Sammesteds); p.373 Anfr.
   Skr. S.209; p.374 Anfr. Skr. S.130–131.
 - Letterspacing — Danish (\emph): p.365 dynamiske, materialistiske; p.366 Bevægelse, Fortynding,
   Fortætning; p.367 Forandring, Forvandling; p.375 imod, for, Emissions-, Corpusculartheorie.
   German Sperrsatz inside Hegel/Bayrhoffer quotes (\emph): p.372 von, uns, Wirkende. Other long
   German quotes on pp.370–374 are NOT Sperrsatz (plain). All crop-verified.
 - Greek enum labels α)/β) inside a German quote (p.373) typed as Unicode (textalpha). French antiqua
   plain: mécanique céleste. Latin plain: vacuum disseminatum, vacuum coacervatum.
 - Mid-word page breaks: physicalische Aeuße\-/rung (371→372). 364→365 was Materien alt\-/saa (from
   Batch 33). 373→374 paragraph break (after Geräusch. footnote). Others between-word.
 - Verify compile: 310 pp., only microtype + textalpha-Greek substitution artifacts; 0 undefined
   control seqs; braces 1451/1451. Chemical formulas + German quotes spot-checked (verify p.304).

### Batch 35 (printed pp. 376–386, PDF 414–424) — DONE & image-verified
 - Still within γ) Æsthetophysiske Functioner: Newton (Emissionsth.) vs Huyghens (Undulationsth.);
   Hegel's critique of both; then the mechanical/dynamical Dualisme of Lyd/Lys and the æsthetic side.
 - **Two long math-heavy footnotes** (each rendered `\[...\]` inside `\footnote{}`, all verified):
   p.379–380 (anchor on p.379): Holten wave-intensity derivation — $n\,mh^{2}=n_{1}\,mh_{1}^{2}$,
   $\frac{n_{1}}{n}=\frac{r_{1}^{2}}{r^{2}}$, $\frac{mh^{2}}{mh_{1}^{2}}=\frac{r_{1}^{2}}{r^{2}}$;
   p.381: Snell/attraction derivation — $\frac{\sin i}{\sin b}=\frac{h_{1}}{h}$,
   $h_{1}^{2}-h^{2}=\int_{0}^{y_{0}}Y\,dy$, $h_{1}\sin b=h\sin i$. Render correctly (verify pp.313–314).
 - Other math: p.376 $\frac{1}{2000000000}$ (2 followed by 9 zeros, zoom-counted); p.377 & p.382
   $\frac{4}{3}$; p.382 fn $1\tfrac{1}{2}$ Pund; big numbers as 40{,}000 / 41{,}500 / 919{,}000 /
   845{,}000 / 477 & 733 Billioner (plain text with `{,}`).
 - Footnotes (whole at anchor): p.376 Holten Lysets Naturlære 1861; p.377 two (Holten Anfr. Skr.
   S.164; 166–167); p.378 two (Hegel Naturphil. S.140; Anfr. Skr. S.138–39); p.379–380 the wave one;
   p.381 the Snell one; p.382 Holten Lysets Naturl. S.167; p.384 H. C. Ørsted, Naturlærens mech.
   Deel, 3. Udg. ved Holten 1859 S.294; p.385 Holten Lysets Naturl. S.170.
 - Letterspacing — Danish (\emph): p.376 Lysstraaler; p.382 Vandet, Luften, Ætheren; p.384 høiere,
   dybere, Styrke; p.381 fn Frastødningen, Tiltrækningen, efter. German Sperrsatz (\emph): p.378
   jedem Punkte, nach allen Richtungen, materielle Halbkugel, durchdrängen; p.379 Vermittlungen.
   All crop-verified.
 - Mid-word page breaks: maae vi ind\-/rømme (376→377), Undulations- som Emis\-/sionstheorien
   (378→379), mechaniske Aar\-/sager (382→383). 377→378 & 381→382 paragraph breaks (after footnote-
   anchored sentences). Others between-word. The p.379–380 footnote spans two printed pages (anchored
   whole on p.379; p.380 body is a fresh paragraph above the footnote continuation).
 - Verify compile: 318 pp., only microtype + textalpha-Greek substitution artifacts; 0 undefined
   control seqs; braces 1533/1533. Both math footnotes + emphasis spot-checked (verify pp.313–314).

### Batch 36 (printed pp. 387–397, PDF 425–435) — DONE & image-verified
 - Closes γ) Æsthetophysiske Functioner, then opens **c) Functioner af Grundaarsagen** (subsubsection
   heading on p.387) and within it **α) Organiske Functioner** (paragraph heading on p.394). Mostly
   prose (Magt/Viden, Sandsning/Tænkning, materiality/ideality); one footnote (p.395).
 - Prose-heavy — NO math this batch. Only footnote: p.395 Forelæsn. over „Phil. Propæd." 1860–61 S.200.
 - Letterspacing (\emph), all crop-verified: p.387 formel Objectivitet; p.388 væsentlig, reel
   Objectivitet; p.389 virkelig Objectivitet, Functioner af Grundaarsagen; p.394 organiske, Aandens
   Mechanik, Energie; p.395 anlægge, ordne, constituere, articulere, organisere, Fornuft; p.396
   Organiseringens, Organiseren, organiseres.
 - Latin antiqua plain: in concreto, Absolutum. No German this batch.
 - Mid-word page breaks: det Sandse\-/lige (391→392), discursive For\-/udsætninger (392→393),
   den articu\-/lerende (396→397). 389→390 paragraph break. Others between-word.
 - Verify compile: 326 pp., only microtype + textalpha-Greek (α heading) substitution artifacts;
   0 undefined control seqs; braces 1562/1562, emph 512. Headings + emphasis spot-checked (verify p.324).

### Batch 37 (printed pp. 398–408, PDF 436–446) — DONE & image-verified
 - All within c) Functioner af Grundaarsagen, α) Organiske Functioner: relative vs absolute
   totalities, mechanical/elementary/organic Selvhed, the organic function as apriorisk+empirisk,
   Hegel's Idee/Begriff, Philosophy vs Physiology. Prose + five (mostly long) quote-footnotes.
 - NO display math. Five footnotes (whole at anchor): p.399 „Fordi en blot mechanisk…" (Forelæsn.
   Phil. Propæd. 1861–62 S.91); p.400 „Ved at tydeliggjøre…" (1861–62 S.91–93); p.403 „I det
   astronomiske Hele…" (1860–61 S.208–209); p.405 the cell/Kimen quote (1860–61 S.345–46); p.406
   „Die Bestimmungen des Gegensatzes" (Die subjektive Logik S.249).
 - Letterspacing (\emph), all crop-verified — Danish: p.399 organiske Functioner, mechaniske
   Functioner; p.401 elementære; p.403 magte, assimilere; p.405 FOOTNOTE animale, dyriske,
   vegetative, Sliimbladet, Karbladet, animale, vegetative. German Sperrsatz (p.406 Hegel quote):
   Bestimmungen des Begriffs, Erfüllung, die Idee, Einheit, die Idee, unmittelbare, die
   Objektivität, Inneres, äußerliche, Negatives.
 - Mid-word page breaks: Elementær\-/function (401→402), sig legemliggjørende Selv\-/hed (403→404).
   397→398, 400→401, 402→403 paragraph breaks; 399→400 continuation after a colon. Others between-word.
 - Verify compile: 334 pp., only microtype + textalpha-Greek substitution artifacts; 0 undefined
   control seqs; braces 1589/1589, emph 534. Hegel German Sperrsatz + cell footnote emphasis
   spot-checked (verify pp.331–332).

### Batch 38 (printed pp. 409–419, PDF 447–457) — DONE & image-verified
 - Closes α) Organiske Functioner (pp.409–412) and opens β) Functioner af Aandens Mechanik (heading
   on p.412) through p.419. Chemical/morphological analysis of the organism, Fechner's psychophysics
   (weberske Lov), Herbart's Aandsmechanik and its critique.
 - Display math: three Fechner-law equations on p.415 — dγ = k dβ/β; γ = k(log β − log b);
   γ = k log(β/b) — plus Herbart's proportion on p.418: m/a : m/b = 1/a : 1/b. Inline β,γ,b,k,m,a.
 - Footnotes (8, whole at anchor): p.409 S.209; p.410 S.219 & S.220 (Anfr. Skr.); p.411 S.231–32;
   p.414 S.446 & Heiberg Specul. Logik (Pros. Skr. 1 Bd. S.338); p.415 S.444–153 [ERRATUM: prob.
   453]; p.417 Forelæsn. Phil. Propæd. 1860–61 S.454–55.
 - Letterspacing (\emph), all crop-verified: p.409 Analyse; p.411 „to Organismer i een Organisme";
   p.412 heading + „Functioner af Aandens Mechanik"; p.413 ydre Psychophysik, Aandsmechanik;
   p.415 (inside quotes) Fundamentalformel, Maalformel, Incitamentets Fundamentalværdie. Pages
   416–419 have NO Sperrsatz (dense Herbart quotation) — scanned/confirmed.
 - Errata flagged in situ: p.415 footnote page range „444--153" (misprint for 453); p.418 „Förholdet"
   printed with umlaut (std „Forholdet"); p.418 stray dot over final „1" in the proportion (rendered
   plain 1/b). Quote „Sjælen er kun een…" spans p.416→417; „At det nødvendigviis…" spans p.413→414.
 - Mid-word page breaks: sandse\-/lige (415→416), saa\-/kaldte (417→418) — page comment appended to
   the `\-` line (`sandse\-% p. 416`) so the newline is swallowed and the word joins. Others
   between-word; 412 (before β heading) and 412→413 paragraph breaks.
 - Verify compile: 343 pp., only microtype + textalpha-Greek substitution artifacts; 0 undefined
   control seqs, 0 runaway; braces 1637/1637, display \[/\] 24/24, emph 542, footnote 184.
   Fechner eqns (verify p.339), Herbart proportion + „Förholdet" (verify p.341), „sandselige" join
   (verify p.340) all spot-checked.

### Batch 39 (printed pp. 420–430, PDF 458–468) — DONE & image-verified
 - Within β) Functioner af Aandens Mechanik, then opens γ) Functionernes Energie (heading p.427).
   Herbart's calculations (attention/forgetting/recall as approaches to an unattainable limit), the
   psychological-vs-ontological analogy critique, and the Functions' Energy / hegelian syllogism
   critique. VERY math-heavy — all equations sit in long footnotes.
 - Display math: p.420 fn dz/dt = βφe^{-βt}; p.421 fn ϱr/Π·(ϱ-ω)/ϱ dt = dω and ω = ϱ(1-e^{-rt/Π});
   p.422 fn d²σ/dt² = h(S-σ) - k dσ/dt; p.423 fn σ = S[1 - e^{-kt/2}(cos qt + k/2q sin qt)], idet
   k²/4 - h = -q². Inline: y=f(x)=e^{-x} (p.420 main); z=φ(1-e^{-βt}); S-σ=Se^{-t}; p=P(1-e^{-t});
   =0 and rene 0 (p.422); r ϱ/Π; β,φ,σ,ϱ,ω,Π,k,q,h,p,z,P,S. Used \varrho for ρ, \Pi, \varphi.
 - Footnotes (3, whole at anchor, all spanning two printed pp.): p.420→421 the giant Herbart-
   calculations note (three sub-parts w/ letterspaced run-in headings Opmærksomheden.,
   Forestillingernes Bevægelse., Forestillingernes Gjenopvækkelse.; refs S.376, S.462-63, S.466-67);
   p.422→423 the 2nd-differential-coefficient note (S.—); p.430→431 German Hegel note „Die sich auf
   sich selbst beziehende Bestimmtheit… ist die Einzelnheit…" (Hegel, Subj. Logik S.51) — Einzelnheit
   letterspaced ×2.
 - Letterspacing (\emph), crop-verified: fn pludselig, aldrig (×2 each in p.420-421 fn); „pludselig
   Opnaaelse af et dog Uopnaaeligt" (p.421 fn, 1st only — 2nd occurrence plain); γ) heading;
   p.429 Functionsenergien, „System af Slutninger", „teleologiske Slutninger"; p.430 „Modsætningen",
   „Functionernes Energie" (the emphasised restatement of point 1). Pages 424-426, 428 no Sperrsatz.
 - Mid-word page breaks (page comment appended to the `\-` line): Forstands\-/kritiken (423→424),
   Func\-/tioner (428→429). Note „e." stray dot in p.420 fn eq dropped (rendered βφe^{-βt}, flagged).
   Two inline „1)…2)…" lists on p.429-430 (NOT letterspaced) vs the letterspaced „1)" restatement.
 - Verify compile: 351 pp., only microtype + textalpha artifacts; 0 undefined, 0 runaway; braces
   1699/1699, display \[/\] 29/29, emph 557, footnote 187. Herbart calc footnote + all five eqn
   blocks + „Forstandskritiken" join spot-checked (verify pp.343–345).

### Batch 40 (printed pp. 431–441, PDF 469–479) — DONE & image-verified
 - Still in γ) Functionernes Energie; introduces a NEW deeper heading level — αα)/ββ)/γγ) — for the
   three Grundtotaliteter (abstract-mechanical p.435, mechanical-dynamical p.437, organic-living
   p.441). Rendered as `\begin{center}{\bfseries αα)…}` + `\addcontentsline{toc}{subparagraph}`.
 - Syllogism/symbol math: bare terms E, S, A, O kept as PLAIN TEXT on pp.431–434 (matching Batch 39
   Schema style), but as inline math $S$,$O$,$A$ from p.435 on (where subscripts appear). Greek
   lowercase p.433 „ε — σ — α" = $\varepsilon$ — $\sigma$ — $\alpha$ (text em-dashes). Subscripts:
   $A_{\varkappa}$,$O_{\varkappa}$ (kosmisk Index), $A_\gamma$,$O_\gamma$ (geologisk), $O_o$ (organism).
   Display: \[ S - A_{\varkappa} - O_{\varkappa} \] (p.436), \[ S - A_\gamma - O_\gamma, \] (p.439).
   **NB \varkappa needs libertinust1math (Hans's build has it); portable verify adds
   `\providecommand{\varkappa}{\kappa}` in place of the libertinust1math line.**
 - Footnotes (8, whole at anchor): p.431 Heiberg Specul.Logik Pros.Skr.1 Bd.S.321-22 & Heiberg
   Anfr.Skr.S.327; p.433 „de logiske Functioner" note & Heiberg Anfr.Skr.S.(Pros.Skr.1 Bind,S.315);
   p.437 Hegel Subj.Logik S.200-201; p.438 the long German „Die drei Schlüsse…" note (whole on
   p.438); p.439 Hegel Anfr.Skr.207; p.440 the „geologisk Totalitet" note.
 - Letterspacing (\emph), crop-verified. Danish: p.431 Object, Grunden; p.432 Object, Subject,
   „dens Idee er Viden", „dens Idee er Magten"; p.433 „dens Idee er Sandheden", de logiske Functioner;
   p.434 Fremgang, „Tilbagegang eller Cirkel", the letterspaced „2) Totaliteternes System…Energie";
   p.436/437 the two „Totalitetens Functioner ere …-functioner og virke med …-el Energie" statements;
   p.437 Differensen, Indifferensen; p.439 Differens. German (Hegel quotes): p.437 Bestimmtheit,
   „auf Anderes"; p.438 „fallen diese Schlüsse", auseinander, „äußerlich hinzukommenden Bedingungen",
   Trennung; p.439 „zwei verschiedene Seiten aus". Pages 435 (body), 440, 441 (body) largely no ls
   beyond the symbol emphasis noted.
 - Mid-word page breaks (comment on the `\-` line): op\-/rindelig (434→435). „Øiemedet" (=Øiemed)
   confirmed on p.431. Between-word elsewhere.
 - Verify compile: 359 pp., only microtype + textalpha artifacts; 0 undefined, 0 runaway; braces
   1758/1758, display \[/\] 31/31, emph 580, footnote 195, \varkappa ×11. Headings αα/ββ/γγ,
   ε—σ—α, S—Aϰ—Oϰ, Hegel German footnotes spot-checked (verify pp.351–354).

### Batch 41 (printed pp. 442–452, PDF 480–490) — DONE & image-verified
 - Still γ) Functionernes Energie (γγ) organic-living continues, then the „3)" point). Grounding of
   the three syllogisms, Life's origin (Liebig), the Absolute & Aristotle, Hegel's method, the three
   Idee-Systemer (cosmological/geological/biological), Aandens/Naturens Idee, Sandhedsideen,
   Spiritualisme vs Naturalisme.
 - Symbol math (inline $S$,$A$,$O$ + subscripts $A_{\varkappa}$,$O_{\varkappa}$,$A_\gamma$,$O_\gamma$,
   $A_o$,$O_o$; \varkappa via libertinust1math, verify providecommand). Displays: \[ S - A_o - O_o. \]
   (p.443) and the three on p.449 (S−Aϰ−Oϰ, S−Aγ−Oγ, S−Ao−Oo).
 - GREEK (p.447, Aristotle) typed directly as polytonic Unicode (same convention as the ~129 existing
   Greek lines): (θεοῦ ἐνέργεια ἀθανασία, τοῦτό δ'ἐστι ζωὴ ἀΐδιος), (τὸ δυνάμει ὄν), (τὸ ἐνεργείᾳ ὄν),
   (καὶ γὰρ ἔστιν ἡ κίνησις ἐνέργειά τις ἀτελὴς μέντοι). In portable verify these show blank (LM font
   lacks polytonic Greek) — correct in Hans's libertinus+textalpha build.
 - Footnotes (5, whole at anchor): p.443→444 Liebig „Paa Elementernes Sammentræden…" (Phil.Propæd.
   1860-61 S.189 flgd); p.445 S.219; p.446 S.281-82; p.448 two Hegel notes (Subjkt.Logik S.349 &
   S.351-52, Werke 5ter Bd).
 - Letterspacing (\emph). Danish: p.446 „3) I Functionernes Energie er Grundideernes Energie
   reflecteret"; p.447 „Energie skal være Ideens høieste Udtryk"; p.450 „Aandens Idee", „Naturens
   Idee"; p.452 „Naturen og Aanden ere i Sandhed Eet". German (Hegel, p.448): Nothwendigkeit,
   Außersichgehens, „weitern Bestimmung", Ausdehnung, „höhere Intensität", „Konkreteste und
   Subjektivste", „reine Persönlichkeit", „Alles in sich befaßt und hält", „einfachen Einheit",
   „reine Unmittelbarkeit des Seyns" (NB „ein In-sich-gehen" is NOT spaced — zoom-checked).
 - Mid-word page breaks (comment on `\-` line): orga\-/niske (443→444), Følge\-/sætningen (444→445),
   Mang\-/foldige (446→447). Three ink-blot spots flagged with % NOTE: p.443 blot over „en", p.447
   blot between „være"/„en", p.448 blot between „er"/„det" — text complete in each, blots are scan
   defects.
 - Verify compile: 368 pp., only microtype + textalpha/Greek „Missing character" substitutions;
   0 undefined, 0 runaway; braces 1789/1789, display \[/\] 35/35, emph 595, footnote 200, \varkappa
   ×22. Subscript syllogisms (verify p.361), Greek page + „3)" emphasis (verify p.363) spot-checked.

### Batch 42 (printed pp. 453–456, PDF 491–494) — DONE & image-verified — **FINAL BATCH**
 - Closes γ) Functionernes Energie and the whole book: the consequent Spiritualism vs Naturalism
   argument, the two Riger united in Sandhedens Idee, ending „…Functionerne af den almindelige
   Objectivitet ere alle Functioner af subjectiv Viden." (p.456 = last line of the body).
 - No display math, no Greek. One long footnote p.453 „Grundspørgsmaalet bliver altsaa dette…"
   (Forelæsn. Phil. Propæd. 1861--62 S.138-39). No Sperrsatz on these four pages.
 - Mid-word page break (comment on `\-` line): Natur\-/riget (455→456). p.454→455 between-word.
 - The scan's last page (PDF 494 = p.456) ends the body; below the text is only a library
   date-stamp „15 JU 66" — NOT transcribed (scan artifact). No back-matter/TOC in this scan.
 - Verify compile: **371 pp.**, only microtype + textalpha/Greek substitution artifacts; 0 undefined,
   0 runaway; braces 1790/1790, display \[/\] 35/35, emph 595, footnote 201, **0 „text to be added"
   markers left**. Final page (verify p.371) spot-checked — ends correctly.

## ✅ TRANSCRIPTION COMPLETE — body pp. 1–456 fully transcribed & image-verified.
The whole book body is done. `grep -c 'text to be added' transcription.tex` = 0; portable verify
compile is clean (371 pp., 0 undefined / 0 runaway). Remaining per the Finishing checklist below:
Hans compiles locally with the real fonts (libertinus + libertinust1math + textalpha — note the file
uses `\varkappa` and polytonic Greek, both of which need that real toolchain), then optional Phase 2
(translation). Hans commits & pushes — the assistant never does.

(Historical resume pointer, now moot: reached printed p. 456 (PDF 494), end of body.)
NB own footnotes incl. math (errata: S.308 "x + 7", S.363 "cost"). Rendered PNGs
live in the outputs dir as gl_body_NN.png / gl_b2_NN.png / gl_b3_NN.png during a session.

## Finishing (per TRANSLATION-PLAYBOOK.md §6, adapted for a transcription)
When `grep -c 'text to be added'` = 0 and compile is 0/0:
1. Final sandbox compile → confirm page count, 0/0.
2. `catalog.yaml`, id `grundideernes-logik`: status skeleton → in-progress → complete
   as work proceeds; add a Transcription link.
3. Tell Hans to compile locally with the real fonts (libertinus + textalpha).
4. Phase 2 (separate job): translation per ../../../TRANSLATION-PLAYBOOK.md.
5. Hans commits & pushes — the assistant never does.

## Standing method
See `../../../TRANSLATION-PLAYBOOK.md` and, for the Fraktur OCR/letterspacing/
footnote discipline, the precedents in `../theologiens-naturbegreb/RESUME-NOTES.md`
and `../../brochner/problemet-tro-viden/RESUME-NOTES.md` (both Fraktur). For the
book-class preamble and deep sectioning, see `../videnskabslaere/transcription.tex`.
