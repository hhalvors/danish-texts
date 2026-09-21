# Brøchner — *Problemet om Tro og Viden* (1868): transcription resume notes

Hand-off for continuing in a **fresh session** (to avoid re-billing a long thread).
Work in batches of ~10 pages, then compile + give a short report. Don't pause per page.

## Goal
Faithful LaTeX transcription (Danish) of the full book, then an English translation.
Files live in `texts/brochner/problemet-tro-viden/`:
- `transcription.tex` — the active Danish file (book class).
- `translation.tex` — English translation, PARTLY DONE (Phase 2 underway; see handoff below).
- Source scan: `~/bibliotek/Brøchner, Hans/1868-problemet-tro-viden.pdf` (241 PDF pages).
- Garbled OCR crib (unreliable): same dir `/ocr/1868-problemet-tro-viden.txt`.
- Catalog entry: `~/danish-texts/catalog.yaml`, id `problemet-tro-viden`, status in-progress.

## CURRENT RESUME POINT
**★ DANISH TRANSCRIPTION COMPLETE — ALL `text to be added` MARKERS FILLED (0 remaining).**
Block D (Ch. IV, pp.161–224) and Block E (*Slutning*, pp.225–226) are now done, through the
book's last sentence ("…det negative Resultat af det foreliggende finde sit positive
Supplement."). Final marker batch: *Endeligt Resultat* (p.224, one closing paragraph) +
*Slutning* (pp.225–226; „Aabenbaringstro“, „det Religiøse i Religionerne“, emph
`Vidensbestemmelse`). Verified full compile (lmodern substitute): **176 pp., 0 char-warnings,
0 LaTeX errors, 0 markers.**

**pp.135–150 `\emph{}` letterspacing pass + source-check: DONE.** Went page by page
(PDF 144–159), viewed each at 400 dpi, added `\emph{}` to every letterspaced span in the
existing prose (e.g. p.136 "Lidenskab"/"Væsensyttring"/"det subjective Væsen virksomt efter sin
Heelhed…"; p.146 the four "praktisk Tænkning"/"praktisk Erkjendelse"; p.147 "Tænkningens
Form"/"combinerende Tænkning"; p.149 "Afspeiledes absolute Uensartethed", "virkelig
Lighed"/"virkelig Tilsvaren", "absolute Formforskjellighed"). Latin already in `\textit{}`
(differentia specifica, ratio sufficiens, per impossibile, idea corporis). **Source-check catch:
the id-est mark had been mistyped as plain "o:" in 5 places (lines ~3963/3989/4062/4270/4398) —
all corrected to "ɔ:".** Proper names (Spinozas, Hume, Strauß…) left un-letterspaced per the
print. Verified compile: 176 pp., 0 char-warnings, 564 `\emph{}` total. pp.151–226 already had
their emphasis pass during transcription, so the WHOLE book now has the letterspacing pass.

**pp.118–134 fuller source-check: DONE.** Went page by page (PDF 127–143) at 400 dpi.
Footnotes: all present — only p.126 and p.132 carry notes in this stretch, both already in the
file; NO dropped footnotes. Glyphs/quotes/escapes: clean (no stray escapes, „…" and ɔ: all
correct). Section-break rule: restored one missing `\begin{center}---\end{center}` after
„Guden i Tiden“ (p.122). Emphasis pass: pp.118–126 had been left with ZERO `\emph{}` — added
the full letterspacing pass (p.119 "subjective"/"Hvorledes"; p.121; p.122; p.125
"subjectivt"/"praktisk"; p.126 "de absolut uensartede Principer…"); also p.134 ("Modsætning",
"absolut Uensartethed mellem de to Aandsvirksomheder med Hensyn til Indhold, Maal og Ideal").
pp.127–133 already had their 27 emphases from the fresh transcription (spot-verified p.133:
"den subjective Sandhed…", "Villie og Erkjendelse", "Grundideernes Modsætning"). Verified
compile: **176 pp., 0 char-warnings, 0 LaTeX errors.** The WHOLE Danish text (pp.80–226) has now
had both the footnote/source check and the `\emph{}` letterspacing pass.

============================================================
## ★ PHASE 2 — ENGLISH TRANSLATION (`translation.tex`): HANDOFF
============================================================
The Danish `transcription.tex` is the **source of truth** and is COMPLETE + checked.
`translation.tex` already exists, compiles clean (35 pp., 0 warnings/errors via the lmodern
substitution), and is **~30% translated**. Work in a fresh session, in ~10-page batches, then
compile + short report. Translate FROM `transcription.tex` (the Danish), not from the PDF.

**DONE so far (do not redo):**
- Front matter + Preface (Forord, pp.1--7) — full.
- Ch. I §1 "The Preparation of the Problem in Antiquity" (pp.8--14) — full.
- Ch. IV intro + §"Main Features of S. Kierkegaard's Theory" (pp.118--126),
  §"Its Relation to Other Contemporary Conceptions", §"Main Features of Prof. R. Nielsen's
  Theory", §"Critique of Nielsen's Theory" intro + start of §§"Psychological Opposition"
  through ~p.133.

**REMAINING markers** (32 `% [text to be added: pp. X--Y]` + 3 continuation notes):
grep -n "text to be added" translation.tex. In reading order: Ch. I §2 NT/Patristic/
Scholasticism (pp.15--21) + §3 Modern (pp.21--31); all of Ch. II (pp.31--43); all of Ch. III
(pp.43--118, ~17 subsection markers); Ch. IV from "psych opposition continues p.133" onward
(pp.133--224) + Conclusion (pp.225--226). The 3 continuation notes (lines ~826, ~964, ~1208)
mark mid-section seams where translated text resumes — fill the gap, don't restructure.

**TRANSLATION CONVENTIONS already established in the file (keep consistent):**
- Quotes: Danish „…" / «…» → English curly double quotes via LaTeX ``…''.
- Emphasis: Danish `\emph{}` (letterspacing) → keep as `\emph{}` (renders italic).
- Latin phrases: `\textit{}` (e.g. `\textit{ipse dixit}`).
- Greek: MATCH THE DANISH TERM-BY-TERM (parity). Brøchner's own practice is mixed: in the
  Antiquity section he transliterates (`\textit{nous}`, `\textit{phronesis}`,
  `\textit{noesis noeseos}`, `\textit{nous poietikos}`, `\textit{pistis}`, `\textit{doxa}` —
  transcription.tex lines 407--457), so the translation keeps those transliterated. Everywhere
  else he sets real Greek glyphs (τέλος, πίστις, γνῶσις, ἐπιστήμη, Κόσμος, Νοῦς, κοινὸς λόγος,
  μὴ ὄν, οὐκ ἀγαθὸν πολυκοιρανίη…) — translate the surrounding text but copy the Greek glyph
  verbatim from transcription.tex. `\usepackage{textalpha}` is now in the preamble for this.
  (Already done in the translated range: `telos`→τέλος at the Feuerbach/Kierkegaard parallels.)
  The ɔ: id-est mark is still rendered "i.e." in English (no ɔ glyph / no graphicx needed).
- id-est mark ɔ: → "i.e."; em-dash `---`.
- Footnotes: translate the note content, keep `\footnote{}` at the same anchor. (NB: Danish
  footnotes are sparse — check each page's Danish for any `\footnote` and carry it over.)
- Register: scholarly, moderately literal but readable English (matches the done sections).
  Proper names unchanged. Section/chapter labels (`\label{...}`) kept English, structure
  mirrors transcription.tex 1:1 — verify each heading against the FINAL transcription.tex
  before filling, since some translation headings were drafted against an earlier state.

**Final steps after translation done:** compile both PDFs on the user's machine
(libertinus+libertinust1math for the Danish; lmodern fine for English), then in catalog.yaml
set id `problemet-tro-viden` section status to `complete` and confirm both Transcription +
Translation links resolve. (User commits/pushes; do not.)

----

**Block C (Ch. III) is COMPLETE through printed p. 118** (PDF 127): all of *Kritik af
Videnskabsbegrebet* (Troesvidenskabens Methode, Dens Resultater, Det for Theologien
Typiske…) and *Endeligt Resultat* (117–118) incl. the bridge paragraph "Fra Kritiken af
Theologiens uigjennemførlige Foreningsforsøg…" (moved from after the Ch. IV heading into
*Endeligt Resultat*, where the print has it). Ch. III now has NO remaining `text to be
added` markers. Verified compile: 119 pp., 0 char-warnings.

**Block D progress: pp.161–171 DONE** (subsection "Det Ethiske og det Religiøse i Forhold
til Erkjendelsen", PDF 170–180). Transcribed from source with full `\emph{}` letterspacing
pass, „…" quotes, --- em-dashes, ɔ marks, and Latin in `\textit{}` (libera necessitas, modus
cognoscendi colendique Deum, cognitio, eo ipso). One in-text section-break rule
`\begin{center}---\end{center}` inserted at the p.162→163 break (Nielsen's view → "For denne
Opfattelse… ligger der et Correctiv"). NO footnotes on pp.161–171 (verified each page's
bottom strip). NOTE on heading convention: the print has its own numbered headings ("2. Det
Ethiskes og det Religiøses Forhold…", "3. De psychologiske Bestemmelsers Forudsætninger…");
the editorial `\subsection{}` stands in for these — do NOT transcribe the number/heading text
separately, and do NOT add a rule before a `\subsection` (the heading is the break). The
batch stopped at the end of subsection 2 ("…Supplementet til dette."); p.171 from the "3."
heading onward (PDF 180 lower half, "Modsætningen i det Psychologiske mellem Erkjendelse og
Villie viste…") is the START of the next marker (pp.171–178) and was NOT yet transcribed.
Verified compile: 137 pp., 0 char-warnings.

**Block D progress: pp.171–178 DONE** (subsection "De psychologiske Bestemmelsers
Forudsætninger i det Metaphysiske", PDF 180–187). Footnotes placed: p.173 ("jfr. Gr. L. I,
190: det Antilogiske „afgiver en Reflex“…", anchor "svarer en logisk Vidensbestemmelse*)"),
p.174 (long, "Var „Afspeilingen“ en væsentlig Bestemmelse…", anchor "Spaltning i
Vidensindholdet*)"), and TWO on p.175 (anchor "denne Mulighed fører*)" = the long Miraklet/
Skabelse note; anchor "andre bestemte Udsagn**)" = "F. Ex. Gr. L. II, 190. „En Almagt, der
ubetinget skaber --- --- af Intet…"). Numbered points "1." and "2." rendered inline as
`1.~`/`2.~`. One in-text rule at the p.177 break before the bridge paragraph. The batch ends
with the lead-in "Paa Grundlaget af de foregaaende Udviklinger… i psychologisk, ethisk og
religiøs Henseende." (p.177→178), placed just before the existing `\section{Theoriens
Consequentser}` heading. NOTE: the print's heading on p.178 is "1. Theoriens Consequentser
med Hensyn til det Psychologiske." — i.e. the print combines the section title with the
"med Hensyn til det Psychologiske" subhead; our skeleton splits them into `\section{Theoriens
Consequentser}` + `\subsection{Med Hensyn til det Psychologiske}` (editorial). Verified
compile: 141 pp., 0 char-warnings.

**Block D progress: pp.178–195 DONE** (subsection "Med Hensyn til det Psychologiske",
Theoriens Consequentser, PDF 187–204). Big quote-heavy section (long Nielsen citations from
*Om den gode Villie* and *Grundideernes Logik*). Footnotes placed: p.179 (×2: "Nielsen: Om
den gode Villie. S. 28 ff." and the Stridsskrift-mod-Martensen note), p.181–182 (the long
"det absolute Mysterium"/Incarnation note spanning two pages), p.187 (long
"mathematiske Venner" note), p.188 (×2), p.190 ("Den gode Villie S. 62--64"), p.193 (×2:
"4. Moseb. XX, 11…" + the Fordring note), p.194 (the psych/metaph Synspunkt note). Latin in
`\textit{}`: non liquet, credo quia absurdum, libera necessitas, necessaria libertas. Foreign
words in guillemets kept as printed: «plus ultra», «lazzi» (compile-clean under lmodern, so
fine under libertinus). Two `«…»`-style and many „…" quotes. The batch ends at "…gjør sig
gjældende i al Bevidsthed." (end of the Psychologiske subsection on p.195), just before the
print's "2. Theoriens Consequentser med Hensyn til det Ethiske." heading = the editorial
`\subsection{Med Hensyn til det Ethiske}`. Verified compile: 153 pp., 0 char-warnings.

**Block D progress: pp.195–199 DONE** (subsection "Med Hensyn til det Ethiske", PDF 204–208).
Footnotes placed: p.196 (the long Kierkegaard/Valget note, anchor "om i sin absolute
Modsætning*)"), and FOUR on p.198 (anchors "rationel Ethik“*)" = Gr. L. I. XXVII note;
"Antirationelt**)" = Heegaard S. 444; "antirationel Ethik***)" = the "brugte iflæng" note;
"uundgaaelig bort****)" = Heegaard S. 442 ff.). Strong letterspaced thesis on p.197 carried as
`\emph{}`: "Den antirationelle Ethik er det Ethiskes Forvanskning; al sand Ethik maa være
rationel Ethik…". Latin in `\textit{}` only where italic; ɔ marks and „…" quotes throughout.
Batch ends at "…en „Troesvidenskab“, en Theologie." (end of the Ethiske subsection on p.199),
just before the print's "3. Theoriens Consequentser med Hensyn til det Religiøse." heading =
editorial `\subsection{Med Hensyn til det Religiøse}`. Verified compile: 155 pp., 0
char-warnings.

**Block D progress: pp.199–210 DONE** (subsection "Med Hensyn til det Religiøse", PDF
208–219, 12 pp.). Many footnotes placed (p.199 praktisk-Tænkning note; p.200 footnotes;
p.201 ×2 incl. Om theor.&prakt.Erkj. S.74 + the subjective-Trang note; p.202 ×2 incl. the
hedenske-Religioner note; p.203 the long Rom. XI / «bonum est quia Deus vult» note; p.206
Heegaard-Sophisme note; p.208 "Nielsen: paa anf. St. S. 118."; p.209 Cornelius-Agrippa
"Guldmagerne" note). Foreign Latin in guillemets kept as printed: «bonum est quia Deus vult»
(p.200) and (bonum est quia Deus vult) (p.203 footnote, parens); `\textit{in abstracto}`.
Heavy `\emph{}` letterspacing throughout (Religionsphilosophien-as-"Grændsevidenskab"
critique). Batch ends at the lead-in "Vi kunne nu uddrage det positive Resultat af Kritiken af
den Nielsenske Theorie. Det kan sammenfattes i følgende Bestemmelser:" (after a
`\begin{center}---\end{center}` rule at the p.210 break), placed just before the existing
`\section{Resultat af Kritiken af Nielsens Theorie}` heading. NOTE: that section's body on
p.210 is the print's numbered summary "1. Med Hensyn til det Psychologiske: …" — START of the
next marker. Verified compile: 163 pp., 0 char-warnings.

**Block D progress: pp.210–212 DONE** (`\section{Resultat af Kritiken af Nielsens Theorie}`,
PDF 219–221). The 3-point summary rendered inline with letterspaced run-in heads:
`1.~\emph{Med Hensyn til det Psychologiske:}`, `2.~\emph{Med Hensyn til det Ethiske:}`,
`3.~\emph{Med Hensyn til det Religiøse:}`. Batch ends with the lead-in "Efterat saaledes den
Nielsenske Theorie er kritisk undersøgt og dens Consequentser belyste[fn]… faaer Gyldighed for
begge." (after a `\begin{center}---\end{center}` rule at the p.212 break), placed just before
the existing `\section{Det for Kierkegaard og Nielsen Fælles…}`. Footnote on p.212: the
Christiania-Forelæsninger note. Verified compile: 165 pp., 0 char-warnings. (Sandbox reset
mid-batch wiped /tmp/tessdata — rebuilt Fraktur model via the OCR-pipeline wget.)

**Block D progress: pp.212–216 DONE** (`\section{Det for Kierkegaard og Nielsen Fælles og det
for hver af dem Ejendommelige}`, PDF 221–225). Three numbered points with letterspaced run-in
heads: `1.~\emph{Det for begge Theorier Fælleds}`, `2.~\emph{Det for Nielsen Eiendommelige}`,
`3.~\emph{Det for Kierkegaard Eiendommelige}`. Point 2 contains a list of ~11 short
contradiction-paragraphs ("Der statueres… og dog…"), each its own indented paragraph (verified
via left-margin strip). One footnote on p.213 (the "Modsigelser"-definition note). Caught
"strax slap Theorien \emph{som Theorie}" (NOT "om Theorie"). Batch ends with the lead-in "Med
Hensyn til dette Støttepunkt for Theorien… særligt til det Christelige." (no rule — the print
runs straight into the next section heading), just before the existing `\section{Kritik af de
for Kierkegaard ejendommelige Bestemmelser}`. Verified compile: 169 pp., 0 char-warnings.

**Block D progress: pp.216–224 DONE** (`\section{Kritik af de for Kierkegaard ejendommelige
Bestemmelser}`, PDF 225–233, 9 pp.). Three numbered sub-points with letterspaced run-in heads
`1)~\emph{Opfattelsen af det Eviges Begreb.}`, `2)~\emph{Consequentserne af Videns Begrændsning
ved Paradoxet.}`, `3)~\emph{Consequentserne af Opfattelsen af det Evige med Hensyn til det
Ethiske og særlig til dets Forhold til det Religiøse.}` plus emphasized `\emph{Paradoxet er
Underet i Tankens Verden}`. Greek typed directly: μὴ ὄν (p.217, p.218) and τέλος (p.221, p.222,
×4). One footnote (p.217, "Jfr. Kierkegaard: Afsluttende Efterskrift."). Notable readings:
"det sorgfulde Spørgsmaal" (p.224), "Religiositeten A" (Kierkegaard's Religiousness A). A reader's
pencil margin note "Ikke hos Kierkegaard" (p.219) is NOT part of the text — ignored. Batch ends
at "…som løsende Bevidsthedens Splid." (end of the Kierkegaard critique on p.224), just before
the existing `\section{Endeligt Resultat}` (no rule added — the editorial heading represents the
print's section-break rule). Verified compile: 175 pp., 0 char-warnings.

**Next work = finish the book**: marker `p.224` (`\section{Endeligt Resultat}`; body starts PDF
233 lower half, after a centered rule: "Det endelige Resultat med Hensyn til den Kierkegaardske
Theorie er anticiperet i de foregaaende Udviklinger…" — a short closing paragraph, ~½ page,
ending PDF 233/234). Then Block E *Slutning* `pp.225--226` (the final `\chapter*{Slutning}`,
PDF 234–235). Also the two Ch. IV backfill items still open: the `\emph{}` pass over pp.135–150
(16 pp.), and dropped-footnote backfill in the pp.118–161 done region. `grep -n "text to be
added" transcription.tex` → 2 markers remain (p.224 Endeligt Resultat; pp.225–226 Slutning).
NOTE: editorial subsection page-ranges run ~1 page late vs. the print; place text by the
actual section breaks (centered rules) and topic, not strictly by the marker numbers.

To find all remaining work: `grep -n "text to be added" transcription.tex`.

## Page-offset (verified)
**PDF page = printed page + 9.** (printed p.80 = PDF 89.) Verify via printed headers,
NOT the OCR `[side N]` markers (those are off by ~6).

## OCR pipeline (rebuild each session; models don't persist)
```bash
cd /tmp && mkdir -p tessdata && cd tessdata
wget -q https://github.com/tesseract-ocr/tessdata_best/raw/main/dan.traineddata -O dan.traineddata
wget -q https://github.com/tesseract-ocr/tessdata_best/raw/main/script/Fraktur.traineddata -O Fraktur.traineddata
# per page P (PDF page number):
export TESSDATA_PREFIX=/tmp/tessdata
SRC="/sessions/<id>/mnt/bibliotek/Brøchner, Hans/1868-problemet-tro-viden.pdf"
pdftoppm -f P -l P -r 300 -png "$SRC" /tmp/ro >/dev/null 2>&1
tesseract /tmp/ro-0P.png stdout -l Fraktur --psm 6 2>/dev/null \
  | sed -e 's/ſ/s/g' -e 's/œæ/æ/g' -e 's/œ/æ/g' | tr -s ' '
```
The `Fraktur` script model is ~98% at word level. Tesseract LSTM is slow (~20s/page)
and the sandbox times out at 45s, so OCR ONE page per bash call.

**Hybrid method (chosen):** read words from OCR text, then read ONE verification image
per page (300 dpi, 3 band crops if needed) to (a) catch letterspaced emphasis → `\emph{}`
[OCR cannot see letterspacing], (b) fix OCR's plausible errors (k↔f e.g. "iffe"→ikke,
"fan"→kan; dropped ø e.g. "gjor"→gjør, "hoiere"→høiere; "cæ/scæ"→æ), (c) place footnotes.

## Conventions (preserve 19th-c. orthography exactly)
- Spellings: Philosophie, Christendommen, Existents, Erkjenden, gjennem, Eiendommelighed,
  capitalized nouns, ø/aa, double-vowel (Heelhed, Viisdom), `f.\ Ex.`, `d.\ v.\ s.`
- Quotes: Danish „...“ (low-high) as printed; guillemets »...« where the book uses them.
- Em-dashes: `---`. Section breaks the book marks with a short rule → `\begin{center}---\end{center}`.
- Latin in italics: `\textit{credo ut intelligam}`, `natura naturans`, `libera necessitas`,
  `bonum est quia deus vult`, `duæ veritates`, `eo ipso`, `ens universalissimum`, `a priori`,
  `prius`, `Conditio sine qua non`, `Ita`/`Quare`, `natura`/`creatura`.
- Greek typed directly (textalpha handles it): e.g. Νοῦς, the Iliad tag
  `οὐκ ἀγαθὸν πολυκοιρανίη, εἷς κοίρανος ἔστω`. Verify accents with a zoomed crop.
- Letterspaced emphasis → `\emph{...}` (the most common thing OCR misses).
- Footnotes → `\footnote{...}` inline at the anchor. The earlier-done sections had dropped
  all footnotes; those are now backfilled. KEEP backfilling for every new page.
- The old Danish "id est" mark ɔ: type the literal `ɔ` — preamble already maps it
  (`\DeclareUnicodeCharacter{0254}{\reflectbox{c}}`, needs `graphicx`, both already added).
- Section/subsection headings in the skeleton are editorial aids; the original is continuous
  prose. Place transcribed text under the heading whose page-range it falls in.

## Verification compile (sandbox lacks libertinus; substitute, keep ɔ to catch mapping bugs)
```bash
cd /tmp && mkdir -p verify && cd verify
SRC="/sessions/<id>/mnt/danish-texts/texts/brochner/problemet-tro-viden/transcription.tex"
sed -e 's/\\usepackage{libertinus}/\\usepackage{lmodern}/' -e '/libertinust1math/d' \
    -e '/textalpha/d' -e 's/\\usepackage\[danish\]{babel}/\\usepackage{babel}/' "$SRC" > t.tex
python3 - <<'PY'
import re; s=open('t.tex',encoding='utf-8').read()
s=re.sub(r'[Ͱ-Ͽἀ-῿]+','[Gr]',s)   # Greek replaced only because sandbox has no textalpha
open('t.tex','w',encoding='utf-8').write(s)
PY
pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1; pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1
grep -o 'Output written.*' l.txt; grep -ic 'not set up\|missing.*character' l.txt
```
Expect 0 char-warnings. (On the user's real machine libertinus + textalpha handle the
real glyphs; do NOT add the Greek/ɔ substitutions to the actual file.)

## Remaining work
Block C (Ch. III) pp. 80–118: **DONE** (Underet→Endeligt Resultat, verified compile).
Block D (Ch. IV) pp. 161–224: subsections per the 8 markers at file lines ~4385–4430.
Block E *Slutning* pp. 225–226 (marker ~4440).

### Ch. IV pp. 118–161 "done" region is NOT actually complete — it needs real transcription
On inspection the pp. 118–161 region is patchy, not just missing footnotes. Concretely:
- **Escape-encoded block, file lines ~3554–3667 (printed pp. ~123–126):** real text is
  present but uses LaTeX escapes (`\ae `, `\o `, `\O `) instead of the project's direct
  Unicode æ/ø, and has NO `\emph{}` letterspacing and NO footnotes. Needs a clean pass.
- **The "CONTENT GAPS" are MOSTLY NOT missing text — they are STALE placeholder comments.**
  Discovered while doing pp. 127–130: the body text was actually present right after the
  `% [...]` comment; the comment was leftover. The real defects at each seam are: (a) the
  stale comment, (b) a `\noindent` artifact + a dropped connecting word at the page seam
  (e.g. p.126→127 had lost ", og denne"), (c) Transkribus quote style `,,…''` instead of
  „…“, and (d) missing `\emph{}` letterspacing (+ footnotes). So this is a CLEANING pass,
  not re-transcription. Verify each seam's continuity against the source though.
  - `% [Nielsen's theory continues pp. 127--130]` → **DONE** (pp.127–130 cleaned: seam
    fixed with ", og denne", emphasis added, `,,''`→„“; verified vs source). No footnotes
    on pp.127–130.
  - `% [pp. 131--133: …]` → **DONE.** This one was a REAL gap: the file had truncated at
    an erroneous "i Betydningen af Villiesbestemthed." (should be "Villiesværen,
    („Existentsen er praktisk“)") and pp.130b–133 body was missing. Transcribed it from
    source (PDF 139–142) with emphasis + the p.132 footnote (Nielsen: Philosophisk
    Propædeutik, p. anf. St.). Also MOVED the `\subsection{Den psychologiske Modsætning
    mellem Villie og Viden}` heading to its correct spot (it had been placed before the
    section intro; in the print "1. Den psychologiske Modsætning…" comes on p.133 after the
    Existents/Subjectivitet analysis, right before "Hvad der med Rette urgeres af Nielsen").
  - `% [pp. 135--150: …]` → **mostly DONE.** Body was present; fixed the p.134→135 seam
    (file had dropped ": en Subordination, der under Theoriens Udvikling træder frem i mange
    Former."), removed the stale comment, and placed both footnotes — p.141 ("Andensteds
    udtrykker Nielsen sig ubestemtere: „den virkelige Praxis kan ikke ligefrem afledes af
    Theorien“. Om theor. og pr. Erkj. S. 66 …", anchor "det virkelige Mod*)") and p.147
    ("Af Troens Gud skal der saaledes kun gives en praktisk Erkjendelse, jfr. Afhandl. om
    theor. og prakt. Erkjendelse. S. 72.", anchor "…ved den theoretiske Erkjendelse*)").
    STILL TO DO: the `\emph{}` letterspacing pass over pp.135–150 (16 pp.), and a per-page
    source check for other dropped seam-clauses.
  - `% [text continues on p. 151]` → this is a **REAL ~10-page content gap** (pp.151–160
    body was never transcribed). **p.151 now DONE** (transcribed from PDF 160, joined to the
    "3.~Ved Siden af de Beviser…" paragraph: "…postulerede Uensartethed. Der kunde saa
    siges: Det Skjønne og det Sande ere absolut uensartede…"; emphasis: "active Frembringen
    af det Skjønne", "receptive Tilegnelse"). Ends mid-sentence "…i hvilket det Aandelige
    gaaer". **pp.152–160 now DONE** (transcribed from PDF 161–169, joined at the seam
    "…i hvilket det Aandelige gaaer i umiddelbar Enhed med Naturbestemtheden…"). Full
    `\emph{}` letterspacing pass done per page; p.153 footnote placed
    ("jfr. Nielsen: Om theor. og praktisk Erkj. S. 68.", anchor "…blive for os absolut
    uensartede*)"). NOTE: p.152 has NO footnote (verified bottom strip — page ends
    "…den absolute Uensartethed hævdes." with no rule); the resume note's "p.152
    kunstnerisk Phantasie footnote" was a false lead. Section-break rule
    `\begin{center}---\end{center}` inserted at p.160→161 break (matches the centered
    rule in the print) just before `\subsection{Det Ethiske og det Religiøse…}`. The
    region ends with the p.160 lead-in paragraph "Inden vi gaae over til at paavise
    Consequentserne…der gives af dette Forhold." Verified compile: 129 pp., 0
    char-warnings. **The pp.151–160 content gap is now fully closed.**
    The `\subsection{Det Ethiske og det Religiøse i Forhold til Erkjendelsen}` heading +
    its `pp.161--171` marker belong to Block D (next work).
  - **ALL `,,…''` Transkribus quotes converted to „…“ DOCUMENT-WIDE** (global, safe:
    `\begin{document}` is line 46, no `,,` in preamble; also fixed stray quotes in Block A/B).
  Method per page: render PDF (printed+9) at 400 dpi, OCR + view top/bottom crops, verify
  the file text matches (fix any real gaps), convert `,,…''`→„…“, add `\emph{}`, insert
  footnotes from the inventory below.
  - **Escape block pp.123–126 → DONE:** all `\ae`/`\o`/`\O` converted to æ/ø/Ø (global,
    they existed nowhere else), p.122→123 seam rejoined ("udfolde de Bestemmelser"),
    Feuerbach `,,…''` quote → „…“, and "Telos"→Greek "τέλος" (line ~3655). Verified vs
    source pp.123–126: this region has NO letterspaced emphasis (Kierkegaard exposition +
    Feuerbach parallels) and no footnotes — so nothing further to add there.
  - pp.151–160 seam + `\emph{}` pass: **DONE** (p.153 footnote placed; p.152 has none).
    Still to clean: the `\emph{}` pass over pp.135–150 (16 pp.). Quotes all done;
    footnotes pp.126,132,141,147,153 are placed.
- **Footnotes dropped throughout pp. 118–161** (0 footnotes currently in lines 3400–4382).
  Full Ch. IV footnote inventory (from the OCR crib, printed-page = crib `[side N]` − 8;
  verify exact text/page-nums against the source image bottom-strip before inserting):
  - p.126 ✓ DONE: "Ved Fremstillingen af Nielsens Theorie er der, foruden til Nielsens egne
    Skrifter, kun taget Hensyn til den authentiske Fremstilling af Theorien i Dr. Heegaards
    Indledning til den rationelle Ethik." (anchor "Idet Nielsen*)").
  - p.132: "Nielsen: Philosophisk Propædeutik, p. anf. St." (anchor "Subjectivitetens
    Hovedstadier udvikles*)") — BLOCKED: body in the pp.131–133 gap.
  - p.141: "Andensteds udtrykker Nielsen sig ubestemtere: „den virkelige Praxis …"" — gap.
  - p.147: "Af Troens Gud skal der saaledes kun gives en praktisk Erkjendelse, jfr. Afhandl.
    om theor. og prakt. Erkjendelse. S. 72." — gap.
  - p.152: footnote re kunstnerisk Phantasie — verify page; near/after p.151 gap.
  - p.153: "jfr. Nielsen: Om theor. og praktisk Erkj. S. 68." — verify; near p.151 gap.
  Most Ch.IV footnotes only become placeable once the gap pages are transcribed. The
  footnotes on **p.173+** belong to Block D, not this region.
Phase 2: translate the whole book into `translation.tex`, front-to-back, block by block.
Final: compile both PDFs, set catalog.yaml status to complete. (User commits/pushes; do not.)

============================================================
# Repair programme — full collation (REPAIR-PLAYBOOK.md §5C), started 2026-09-21
============================================================

**Ground truth, established 2026-09-21 before any dispatch.** Scan
`~/bibliotek/Brøchner, Hans/1868-problemet-tro-viden.pdf`, sha256
`dfb663931ed9f23fcd7f97d598437ac7b614bf4487e8b0d44ac8b87ca622040c` — hash confirmed by
hand on the device and again on the staged copy; 241 pp., ABBYY layer. **PDF = printed + 9,
uniform**: all 202 folios readable in the text layer give +9 (spot rows: Forord p.2=PDF 11,
ch. I p.9=PDF 18, ch. III p.51=PDF 60 and p.91=PDF 100, ch. IV p.121=PDF 130, p.141=PDF 150,
p.191=PDF 200, Slutning p.225=PDF 234, p.226=PDF 235); each agent re-reads the folio at the
image. PDF 8–9 = *Indhold* (not transcribed in this file).

**Witness: the embedded ABBYY layer.** The `ocr/` crib in bibliotek scores 55% of ≥3-letter
tokens in-vocabulary vs 72–82% for the layer; not used.

**Method: full collation**, 10 printed pages per agent, 23 agents in 4 waves
(1: pp.1–60, 2: 61–120, 3: 121–180, 4: 181–226). Brief = `pgtools/COLLATE-BRIEF.md`
(rebuilt 2026-09-21 — it did not exist) + `BATCH-AGENT.md` (new). One `OCRDIFF:` line per
wave below (per-agent breakdown underneath it). `.bak` per wave:
`transcription.tex.bak.collate-waveN`.

## Waves

### Wave 1 — pp. 1–60, 2026-09-21. 6 agents × 10 pp. SPLICED + VERIFIED.
OCRDIFF: embedded ABBYY | pp.1-60 | 228 candidates | 17 real | 211 witness's fault | 0 unresolved
  (per agent: 1-10 36/6/30/0 · 11-20 34/3/31/0 · 21-30 42/4/38/0 · 31-40 34/1/33/0 · 41-50 38/0/38/0 ·
   51-60 44/2/41/1 — the 1 unresolved, p.57 "sattes", settled by the blind reader as printed)
Found by reading: 123 FIX claimed (Forord pp.1–7 alone 45 — derived/modernised text: skarp→klar,
gode→klare, "man maa therefore"→"maa derfor", Konseqvents→Conse-, andetsteds→andensteds …),
157 EMPH, 6 PRN/turned sorts. Blind second reader on 53 items: 51 agree; 2 collator claims REFUTED
and not applied (p.50 Conseqventser, p.55 Conseqvents — page reads Consequ-). Applied: 276 edits
+ 10 manual; 60 markers placed as \opage (53, 57 restored). Word diff vs .bak: 356 hunks, all inside
pp.1–60, file tail after \apage{61} byte-identical. Sandbox compile (mathptmx substitute, Greek
mapped): 168 pp., 0 errors, 0 missing chars — same as the pre-wave file. .bak =
transcription.tex.bak.collate-wave1.

### Wave 2 — pp. 61–120, 2026-09-21. 6 agents × 10 pp. SPLICED + VERIFIED.
OCRDIFF: embedded ABBYY | pp.61-120 | 183 candidates | 2 real | 181 witness's fault | 0 unresolved
  (per agent: 61-70 47/1/46/0 · 71-80 30/0/30/0 · 81-90 23/1/22/0 · 91-100 23/0/23/0 · 101-110 30/0/30/0 ·
   111-120 30/0/30/0)
Found by reading: 29 FIX (hæver→hævder ×2, ophævede→uophævede, gjorte→givne, see→skee ×2, for→før,
lost run-in head "S. Kierkegaard. —" p.118, a dropped "et" p.75, "det er"/"der i" p.79 …), 469 EMPH,
8 printer's readings restored (liberium, Bevidstbed, λὸγος, Autorttet, Uuderet, nn, Anrendelsen, man).
Blind second reader on 70 items (incl. the 4 Forord Conseq- variants): all agree with the collators.
3 spurious paragraph breaks removed (pp.63, 65, 81). 60 markers → \opage (112 restored).
Applied with tools/apply2.py (sequential; the first applier corrupted overlapping edits in this
wave — caught by the brace/duplication checks before anything was written — and was retired;
wave 1 re-derived with apply2 matches what was committed). Word diff vs wave-1 file: 856 hunks,
all in pp.61–120; head and tail byte-identical; no new repeated n-grams; sandbox compile 168 pp.,
0 errors, 0 missing chars. .bak = transcription.tex.bak.collate-wave2.

### Wave 3 — pp. 121–180, 2026-09-21. 6 agents × 10 pp. SPLICED + VERIFIED.
OCRDIFF: embedded ABBYY | pp.121-180 | 237 candidates | 2 real | 235 witness's fault | 0 unresolved
  (per agent: 121-130 49/0/49/0 · 131-140 42/0/42/0 · 141-150 31/2/29/0 · 151-160 39/0/39/0 ·
   161-170 37/0/37/0 · 171-180 39/0/39/0)
Found by reading: 19 FIX (lost run-in head "R. Nielsen. —" p.126; dropped "i" pp.136, 175; added "i"
p.173; Erkjanden→Erkjenden ×2; Fordobling→Fordobbling ×2; Gyldigshed→Gyldighed p.148 (collator
called it a printer's reading; two blind readers read Gyldighed); dashes/commas), ~300 EMPH,
8 printer's readings restored (Indivirer, Tlifælde, "den,", Villle, Modsætniugen, "er er",
ikkeheller; Gjenstaud-type). 2 spurious paragraph breaks removed (145, 161); rule added p.160.
Blind reader on 49 items: 3 disagreements settled by a third reading (p.126 run-in spaced;
p.148 Gyldighed; p.162 Villle). 60 markers → \opage (137, 164, 178 restored).
Verify: 524 word hunks all in pp.121–180, head/tail byte-identical, braces 0, no new repeats,
compile 168 pp. 0 errors 0 missing. .bak = transcription.tex.bak.collate-wave3.

RESUME POINT (if the session stops here): waves 1–3 spliced (pp.1–180). Wave 4 (pp.181–226)
is COLLATED and blind-checked but NOT yet spliced — its results were in the session scratch and
would have to be re-collated if lost. Then: header, ledger → repaired, repair-queue.py,
6-page |post re-sample, essay-quotation check.

### Wave 4 — pp. 181–226, 2026-09-21. 5 agents. SPLICED + VERIFIED.
OCRDIFF: embedded ABBYY | pp.181-226 | 164 candidates | 0 real | 164 witness's fault | 0 unresolved
  (per agent: 181-190 36/0/36/0 · 191-200 33/0/33/0 · 201-210 31/0/31/0 · 211-220 39/0/39/0 ·
   221-226 25/0/25/0)
Found by reading: 14 FIX + 5 ø restored (Kløften, Kløft p.214; Religiøsitet- pp.222–223, both
readers), ~175 EMPH, 6 printer's readings (dogmatkske, Nyttte, Forudsætsætninger, nundgaaelig,
Overlegeuhed …). Refuted by the blind reader, NOT applied: p.199 "kages" (page: tages).
p.212 suspect settled: page prints "belyste*)". Paragraphs: +2 (182, 226), −3 (191, 218, 220).
Markers: all 226 now \opage (205 restored), 0 \apage left. Compile 168 pp., 0 errors, 0 missing.
.bak = transcription.tex.bak.collate-wave4.

## COLLATION COMPLETE — 4 waves, 4 OCRDIFF lines. Ledger: repaired (2026-09-21).
(The "RESUME POINT" note after wave 3 is superseded.) Post-repair re-sample, seed |post,
pp.48, 75, 103, 106, 149, 217: 0 word errors; 8 emphasis-extent disagreements (pp.103, 106),
not applied. Open items are listed in the transcription.tex header ("STILL OPEN").
NOTE for the translation: the RESUME-NOTES claim above that Brøchner transliterates Greek in the
Antiquity section is WRONG — the page prints Greek type (Νοῦς, φρόνησις, νόησις τῆς νοήσεως,
νοῦς ποιητικός, πίστις, εἰκασία). translation.tex follows the false claim.

### translation.tex — Greek brought into line with the print (2026-09-21)
The transliteration convention in the Phase-2 handoff above is withdrawn: Brøchner prints Greek type
throughout. Changed in translation.tex (backup translation.tex.bak.greek-20260921): ipse dixit →
αὐτὸς ἔφα (p.4); nous/phronesis → Νοῦς/φρόνησις, nous → Νοῦς, noesis noeseos → νόησις τῆς νοήσεως,
nous poietikos → νοῦς ποιητικός (p.12); "faith" → "faith, πίστις", pistis → πίστις, doxa → εἰκασία
(a content correction: the page prints εἰκασία), pistis (Rhetoric) → πίστεις (p.13); sentence-initial
γνῶσις → Γνῶσις (p.16). Κόσμος (p.18) and λόγος (p.90) stay in their correct forms in English; the
Danish keeps the printer's Κόςμος / λὸγος with comments. Sandbox compile: 172 pp., 0 errors,
0 missing, same as before.

### translation.tex synced to the collated transcription (2026-09-21)
Whole book split by \chapter/\section/\subsection (49 units, 1:1 with the Danish), each unit
revised against the repaired Danish by minimal edit: ~50 sense-changing word corrections carried
over, emphasis rebuilt run-for-run (\emph/\textit counts now equal the Danish in every unit;
1,707 \emph each), 3 omitted footnotes translated (pp.13, 126, 132; footnotes now 69 = 69),
run-in heads pp.118/126, rules pp.122/160, paragraphing matched. Only paragraph mismatch: p.153,
where the repaired Danish runs point "4." on with no break (PRN on the Danish side — check the
image; the English keeps 4 as its own \medskip'd point). Other PRN (English unchanged): p.132
"objective evil" for "objective Ydre"; p.122 "altsaa" untranslated; p.119 typo "overloking" (since fixed);
p.125 book-title italics on "Concluding Unscientific Postscript" removed to mirror the Danish.
Compile (lmodern recipe): 182 pp., 0 errors, 0 char-warnings. Backup translation.tex.bak.sync-20260921.
