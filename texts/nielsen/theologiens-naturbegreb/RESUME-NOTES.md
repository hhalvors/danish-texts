# Rasmus Nielsen — *Om Theologiens Naturbegreb* (1855): transcription resume notes

This is a **TRANSCRIPTION** job (Fraktur Danish, from scan → LaTeX), to be
followed later by an English translation (Phase 2). Work in ~10-page batches;
after each, compile, give a short report, hand back. **Hans commits and
pushes — the assistant never does.**

Book: *Om Theologiens Naturbegreb, med særligt Hensyn til Malebranche:
De la recherche de la vérité* — Indbydelsesskrift til Kjøbenhavns Universitets
Aarsfest, i Anledning af Reformationsfesten 1855. Kjøbenhavn: Schultziske
Officin, 1855.

## Scan & offset (VERIFIED)
- Scan: `~/bibliotek/Nielsen, Rasmus/theologiens_naturbegreb.pdf` (58 PDF pp.,
  Google Books, clean).
- **Offset: PDF = printed + 6.** Title (printed p.1) = PDF 7; body text begins
  **printed p.3 = PDF 9**; last text page **printed p.47 = PDF 53** (ends with
  the formal invitation "…bidrage til Festens Forskjønnelse. / Kjøbenhavn, den
  31te October 1855." then a rule and "Under Universitetets Segl." + the
  university seal engraving). PDF 54–56 blank; 57 = library card; 58 = cover.

## Typography — READ THIS
- **Type is FRAKTUR** (Danish body). French/Latin quotations set in
  roman/antiqua (e.g. the title's "De la recherche de la vérité").
- **Emphasis = letterspacing (Sperrsatz).** OCR CANNOT see it → image-verify
  every page and wrap each letterspaced span in `\emph{}`. Seen so far:
  p.4 `\emph{Natur}` (the key term) and the work-title `\emph{Evangelitroen og
  Theologien}` in the p.4 footnote.
- **Quotes:** Danish „…" (low-high). Use „ (U+201E) … " (U+201D), matching the
  other transcriptions in this repo. (Do NOT use „…''.)
- **Multiplication sign** rendered `$6 \times 6$` (p.3 "6 × 6 Millioner Aar").
- **Footnotes** marked `*)` in the print → `\footnote{}` at the anchor word.

## Orthography — preserve 1855 spelling exactly
Theologien, Naturlæren, Kjendsgjerningernes, Spørgsmaal, Paradiis, Syndefald,
eiendommelige, Vorden, Principløshed, gjøre/gjennemført, iøinefaldende,
Forudsætning, Local-Catastrophe, kj/gj, double vowels (Paradiis), ø/aa.
When in doubt, match the image glyph-for-glyph. (Spot-check fine points like
Vis/Viis and Opfatning/Opfattelse against the image on the verification pass.)

## OCR pipeline (rebuild each session; models don't persist; ONE page per call)
```bash
TD=/tmp/td_$$ && mkdir -p "$TD" && cd "$TD"
wget -q https://github.com/tesseract-ocr/tessdata_best/raw/main/script/Fraktur.traineddata -O Fraktur.traineddata
export TESSDATA_PREFIX="$TD"
SRC="/sessions/<id>/mnt/bibliotek/Nielsen, Rasmus/theologiens_naturbegreb.pdf"
# printed page P: PDF = P + 6
PDFP=$((P+6))
pdftoppm -f $PDFP -l $PDFP -r 300 -png "$SRC" "$TD/ro" >/dev/null 2>&1
tesseract "$TD/ro-$PDFP.png" stdout -l Fraktur --psm 6 2>/dev/null | sed -e 's/ſ/s/g' -e 's/œ/æ/g' | tr -s ' '
```
`Fraktur` model is ~95%+ at word level. **Hybrid method:** take OCR words as a
base, then render ONE verification image per page (300 dpi; copy PNG into the
outputs dir and open with the Read tool) to (a) catch letterspacing → `\emph{}`,
(b) fix predictable OCR slips, (c) place footnotes/quotes.
Predictable OCR errors on this scan: **ø read as o** (folge→følge, Dod→Død,
Sporgsmaal→Spørgsmaal, gjor→gjør) — restore ø everywhere; **sk read as `}` or
`ff`** (`}ulde`→skulde, `Anffuelse`→Anskuelse); **s/k confusion** (modfiger→
modsiger); **n→u** (tæukes→tænkes); doubled æ artifacts (væære→være); leading
Fraktur **I read as J** (Jmellem→Imellem).

## Verification compile (sandbox lacks libertinus — substitute; NOT in real file)
```bash
cd /tmp && D=verT_$$ && mkdir -p $D && cd $D
SRC="/sessions/<id>/mnt/danish-texts/texts/nielsen/theologiens-naturbegreb/transcription.tex"
sed -e 's/\\usepackage{libertinus}/\\usepackage{lmodern}/' -e '/libertinust1math/d' \
    -e 's/\\usepackage\[danish\]{babel}/\\usepackage{babel}/' "$SRC" > t.tex
pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1; pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1
grep -o 'Output written.*' l.txt; echo -n 'char-warnings: '; grep -ic 'not set up\|missing.*character' l.txt
echo -n 'markers left: '; grep -c 'text to be added' "$SRC"
```
Expect 0 char-warnings, 0 errors.

## STATE — what's done vs. to-do
**TRANSCRIPTION COMPLETE.** preamble corrected (title/date match the title page;
Fraktur/offset recorded; **`\usepackage{textalpha}` added** for the Greek on
p.34). **All printed pp. 3–47 transcribed & image-verified**, compiles 0/0
(32 pp. in the sandbox substitute; 0 markers left). pp. 5–20 are heavily footnoted (long French Malebranche citations in
antiqua, plus inline Latin scripture on p.16); each footnote carried verbatim,
tricky French spot-checked by zoom-crop. Letterspaced emphasis found & wrapped
throughout — e.g. p.10 `\emph{Forstanden}`/`\emph{Villien}`; fn p.8
`\emph{Volonté}`/`\emph{Liberté}`; fn p.11 last sentence `La pensée toute
seule…`; p.13 `\emph{hvorledes kommer Sjælen…}`, `\emph{De la nature des idées}`,
`\emph{Materielle Gjenstande…disse Ideer?}`; fn p.14 `\emph{expresses}`; fn p.18
the run of scholastic terms (`genre`, `espece`, `acte`, `puissance`, …); p.20
the whole occasionalist doctrine sentence `at der kun er een sand Aarsag…(des
causes occasionelles)`. p.16 centred maxim → `\begin{center}\textbf{Que nous
voyons toutes choses en Dieu.}\end{center}`. Section-break rule after the p.6
intro → `\begin{center}---\end{center}`.
**Printer's slips kept verbatim:** p.6 fn "rejettetent"; p.15 double paren
"((qu'il est le lieu des esprits)"; p.17 fn "qu, une pure Logique"; p.18 fn
"semblabes". Inline Latin scripture (p.16) left as plain roman, matching the
convention of not italicising the French parentheticals.

**pp. 21–30 (Nielsen's own occasionalism commentary):** dense with inline Latin
technical terms (systema causarum occasionalium, nihil negativum/privativum,
omnipotentia, concursus universalis/specialis/specialissimus, nexus cosmicus,
harmonia præstabilita, etc.) — all left as plain roman (consistent). More
letterspaced emphasis wrapped: p.23 `\emph{Intet og dog virkelig Noget!}`; fn
p.27 `\emph{creando vel annihilando}`; p.29 Psalm 104:24 quote `\emph{Herre,
hvormange ere dine Gjerninger, Du gjorde dem alle viselig.}`; p.30
`\emph{Skabelseslære}`/`\emph{Naturfornegtelse}`. Section-break rules after the
p.22 (") and p.30 opening paragraph → `\begin{center}---\end{center}`.
**Printer's slip kept verbatim:** p.26 fn "Sunt emim" (for "enim"). Footnote
headers vary: "Jvnf." (p.21), "Jfr." (p.6). p.30 ends a complete sentence
(„Sagens Natur".); p.31 continues.

**pp. 31–37 finish the treatise.** The essay proper ENDS on p.37, echoing the
opening line: „Imellem Theologien og Naturlæren er der ingen Forstaaelse…"
(preceded and followed by a centred rule). Emphasis wrapped: p.31 `\emph{at der
er et naturligt Vexelforhold…}`; p.32 `\emph{baade}` ×2 + `\emph{at den
naturlige Forstand…Naturens Love.}`; p.34 `\emph{at Naturriget er et i sig
sammensluttet Hele…}`; p.35 `\emph{baade}` ×2.
**Greek (p.34):** inline `(ὁμοούσιος)`, `(θεία φύσις)` and a footnote Aristotle
quote (Physics; `Τὰ μὲν γὰρ φύσει ὄντα πάντα…κατ' ἀλλοίωσιν.`), all hand-checked
against zoomed scans. Print uses the `-εος` spelling (κινήσεος, στάσεος) — kept
verbatim. NB the sandbox has no greek-fontenc, so the Greek could not be
machine-compiled here; Hans should confirm on a local compile with the real
fonts. p.34 fn also prints "Aristotoles" (slip for "Aristoteles") — kept.

**pp. 38–47 = Indbydelsesskrift appendix (NOT the treatise):** the three new
doctors' autobiographical vitae ("De trende Videnskabsmænd…Levnetsløb"). Style
convention adopted: candidate's OWN name in `\textbf{}` (bold in print), parents'
names in `\emph{}` (letterspaced); numbered heads `\begin{center}\textbf{1.}…`.
Vita 1 = Martin Salomonsen (physician) spells "Kjøbenhavn"; vita 2 = Carl Ludvig
Müller spells "Kiøbenhavn" — each author's spelling preserved. Latin exam grades
(Laudabilis c. encom. publ., Laud. præ cæt.) and Latin/French work-titles (De
resurrectione…, Numismatique d'Alexandre le Grand) left plain roman. Vita 1 =
Martin Salomonsen (physician); vita 2 = Carl Ludvig Müller (numismatist); vita 3
= Nicolaus Ludvig Helweg (theologian). In vitae, notable third parties are
letterspaced on first mention (Christian VIII, Brøndsted, Thomsen, Thorvaldsen);
brother "Adam Müller" and speaker "R. Nielsen" are NOT (image-checked). In the
festival invitation (p.46), every proclaimed name IS letterspaced (J. E. Larsen,
M. Salomonsen, C. L. Müller, N. L. Helweg, J. N. Madvig, C. E. Scharling,
F. T. J. Gram, C. Otto, J. L. Ussing, F. M. Liebmann) — all wrapped `\emph{}`.
Closes p.47: date „Kjøbenhavn, den 31te October 1855.", centred rule,
`\textbf{Under Universitetets Segl.}`, then the seal engraving noted as a comment
`% [University seal engraving …]`.

**CURRENT RESUME POINT: none — BOTH phases complete.**
Transcription.tex complete (0 markers, 0/0). Phase 2 (translation) done 2026-07-04.

## PHASE 2 (translation) — DONE 2026-07-04
`translation.tex` fills all four treatise markers (pp. 3–10, 11–20, 21–30, 31–37),
in reading order. Sandbox compile clean: 26 pp., 0 errors, 0 char-warnings, 0
markers (2 cosmetic overfull hboxes in long French footnotes). Decisions made with
Hans: (1) scope = TREATISE ONLY (pp. 3–37); the appendix (vitae + invitation, pp.
38–47) is left untranslated — its marker was replaced by an "OUT OF SCOPE" comment.
(2) "Leibnitz" → modernised to **Leibniz** throughout the English.
Convention notes: French footnotes and inline French parentheticals carried
verbatim (not translated); Latin phrases/Vulgate quotations kept verbatim; Greek
(p.34 ὁμοούσιος, θεία φύσις, Aristotle Physics quote) copied verbatim — sandbox
cannot render it, so Hans must eyeball it on a local compile with textalpha.
`Aand` translated by sense: "mind" in the Malebranche epistemology (esprit),
"Spirit" in Trinitarian passages (Father/Son/Spirit), "Holy Spirit" for Helligaand.
The essay's opening line and its closing echo are worded identically in English.
catalog.yaml: section retitled "Treatise (pp. 3–37)", status → complete.
STILL FOR HANS: compile both PDFs locally with real fonts (libertinus +
libertinust1math + textalpha), confirm the p.34 Greek renders, and commit/push.

## Finishing (per TRANSLATION-PLAYBOOK.md §6, adapted for a transcription)
When `grep -c 'text to be added'` = 0 and compile is 0/0:
1. Final sandbox compile → confirm page count, 0/0.
2. `catalog.yaml`, id `theologiens-naturbegreb`: status **skeleton → in-progress**
   (transcription complete, translation pending); update note; add a
   Transcription link.
3. Tell Hans to compile locally with the real fonts.
4. **Phase 2 (separate job):** create/fill `translation.tex` per
   `../../../TRANSLATION-PLAYBOOK.md`. Only then does status go to `complete`.
5. Hans commits & pushes — the assistant never does.

## Standing method
See `../../../TRANSLATION-PLAYBOOK.md` and, for the Fraktur OCR/letterspacing/
footnote discipline, the fuller precedent in
`../../brochner/problemet-tro-viden/RESUME-NOTES.md` (also Fraktur).
