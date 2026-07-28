# Rasmus Nielsen — *Philosophiske Grundproblemer* (1879): transcription resume notes

Hand-off for a **fresh session**. This is a **TRANSCRIPTION** job (Danish, from scan → LaTeX),
to be followed later by an English translation. Work in ~10-page batches; after each, compile,
give a short report, and hand back. **Hans commits and pushes — the assistant never does.**

Book: *Philosophiske Grundproblemer, fremstillede af R. Nielsen* — Festskrift i Anledning af
Universitetets Firehundredaarsfest, Juni 1879. Kjøbenhavn: Gyldendalske Boghandel (Schultz), 1879.
**77 printed pages.**

Files live in `texts/nielsen/philosophiske-grundproblemer/`:
- `transcription.tex` — the active Danish file. **`article` class** (NOT `book`). Preamble already
  set up (libertinus + libertinust1math + danish babel + hyperref + fancyhdr). Structure scaffold
  is in place with English content-summary comments per section (accurate — they match the scan).
- Catalog entry: `catalog.yaml`, id `philosophiske-grundproblemer`, status currently **skeleton**.
- No `translation.tex` yet (create it only in Phase 2, after transcription is complete).

## Scans (in the bibliotek folder Hans mounts)
`bibliotek/Nielsen, Rasmus/`:
- **`philosophiske-grundproblemer-color.pdf`** — 91 pp, color, clean and very legible. **Use this.**
- `philosophiske_grundproblemer.pdf` — 91 pp, alternate (B/W) copy; fallback / cross-check.
- Neither PDF has an embedded text layer (`pdftotext` returns nothing) → **OCR is required.**

## Page-offset (VERIFIED)
**PDF page = printed page + 9.**  (printed p.1 = PDF 10 [drop-title]; printed p.5 = PDF 14.)
Verify against the printed running header ("Philosophiske Grundproblemer" verso / page-number recto),
not by counting — the color scan has ~9 pp of endpapers/flyleaves/title up front.

## Typography — READ THIS (differs from the Brøchner job)
- **Type is ANTIQUA / roman, NOT Fraktur.** So OCR with **`-l dan`** (Danish), *not* the Fraktur
  model. (Contrast Brøchner 1868, which was Fraktur.)
- **Emphasis = letterspacing** (e.g. `K r i t i k   d e r   r e i n e n   V e r n u n f t`,
  `Rum og Tid`, `Erfaringens Mulighed`). OCR CANNOT see letterspacing → image-verify every page and
  wrap each letterspaced span in `\emph{}`. This is the single most-missed thing.
- **Latin phrases are true italics** → `\textit{}` (e.g. `\textit{a priori}`). Match the print.
- **Quotes:** Danish „…" (low-high), incl. around German titles („Kritik der reinen Vernunft").
  Convert any Transkribus/OCR `,,…''` to „…".
- **Greek** (if any appears — likely sparse): copy glyphs verbatim; `textalpha` is available.
- **Em-dash** `---`; section-break rules the print marks with a short centered rule →
  `\begin{center}---\end{center}`.
- **id-est mark** `ɔ:` if present → type the literal `ɔ` (add the `\DeclareUnicodeCharacter`
  mapping + `graphicx` to the preamble if it turns up, as in Brøchner).

## Orthography — preserve 1879 spelling exactly
Philosophie, Erkjendelse, Erkjenden, Sandsning, Gjenstand, gjøre, Tænkere, øse, Forudsætninger,
Existents, Villie, Aand/Aands-, Eiendommelighed, capitalized nouns, ø/aa (not å), double vowels
(Heelhed, Viisdom), `f.\ Ex.`, `d.\ v.\ s.`. When in doubt, match the image glyph-for-glyph.

## STATE — what's done vs. to-do
**DONE:** the **Indledning** (drop-title + intro, printed pp. 1–2) is transcribed in
`transcription.tex` (lines ~62–121). Leave it; spot-verify against PDF 10–11 and add any missed
`\emph{}`.

**TO DO — four sections, each currently just a `% [text to be added]` placeholder** (with an
accurate English summary comment above it). `grep -n "text to be added" transcription.tex` → 4 markers:
1. **I. Erkjendelsesproblemet** — printed pp. 3–26 (PDF 12–35). Kant's conditions/limits of
   knowledge; pure intuitions (Rum og Tid); categories; the thing-in-itself (X) and its critique;
   Fichte; Hegel; Nielsen's *Objektiveringslov*; the multiple-sensory-system argument (pp. 24–26).
2. **II. Realitetsproblemet** — printed pp. 27–~52 (PDF 36–~61). Positivism (Comte) vs. absolute
   Idealism (Hegel); thing vs. concept; the *Objektiveringslov* applied to reality; teleology vs.
   causality; *Selvhedsbegreb* vs. *Stofbegreb*; into the soul–body problem.
3. **[III. Frihed, Sjæl og Legeme]** — ~pp. 53–69. ⚠️ **HEADING UNCONFIRMED** — reconstructed from
   content. Freedom as *selvbevidst, betinget Selvvirken*; Motiv og Villie; the ideal–real
   opposition in ethics.
4. **Tro og Viden** — ~pp. 70–77 (through p. 77). The absolute heterogeneity of the principles of
   faith and knowledge; miracle-critique (Troeskritik vs. Videnskritik); *Aandsvirkelighed*. Key
   p.72 line and the closing p.77 statement are quoted in the skeleton comment — verify them verbatim.

### Structural verification (do this FIRST, before transcribing bulk text)
Render the section-boundary pages and confirm the ACTUAL printed headings and their page numbers:
- Confirm **I** and **II** heading wording/pages (pp. 3, 27).
- **Resolve section III**: find the real heading on ~p. 53 (is it "III. …"? what exact title?),
  and whether **Tro og Viden** is "IV." or an unnumbered final part. Fix the `\section*{}` headings
  and the `% pp. X--Y` comments to match. The scaffold's `[III. Frihed, Sjæl og Legeme]` is a guess.
- Check whether the print has a table of contents (Indhold) page; a 77-pp festskrift may not.

## OCR pipeline (rebuild each session — models don't persist; run ONE page per bash call)
```bash
cd /tmp && mkdir -p tessdata && cd tessdata
wget -q https://github.com/tesseract-ocr/tessdata_best/raw/main/dan.traineddata -O dan.traineddata
# per printed page P:  PDF = P + 9
export TESSDATA_PREFIX=/tmp/tessdata
SRC="/sessions/<id>/mnt/bibliotek/Nielsen, Rasmus/philosophiske-grundproblemer-color.pdf"
PDFP=$((P+9))
pdftoppm -f $PDFP -l $PDFP -r 300 -png "$SRC" /tmp/ro >/dev/null 2>&1
tesseract /tmp/ro-*.png stdout -l dan --psm 6 2>/dev/null | tr -s ' '
```
(`-l dan`, NOT Fraktur — this book is roman type. Tesseract LSTM is slow; the sandbox times out at
45 s, so OCR one page per call.) Find the live `/sessions/<id>/mnt/…` path with `ls /sessions/*/mnt/`.

**Hybrid method (recommended, same as the Brøchner/Høffding jobs):** take the OCR words as a base,
then render ONE verification image per page at 300–400 dpi (copy the PNG into the outputs dir and
open it with the Read tool) to (a) catch letterspaced emphasis → `\emph{}`, (b) fix OCR slips,
(c) place footnotes, (d) confirm „…" quotes and italic Latin. Nielsen's footnotes cite his own
works (Grundideernes Logik = "Gr. L.", Om theoretisk og praktisk Erkjendelse, etc.) — carry each
`\footnote{}` at its anchor.

## Verification compile (sandbox lacks libertinus — substitute; do NOT put substitutions in the real file)
```bash
cd /tmp && mkdir -p verify && cd verify
SRC="/sessions/<id>/mnt/danish-texts/texts/nielsen/philosophiske-grundproblemer/transcription.tex"
sed -e 's/\\usepackage{libertinus}/\\usepackage{lmodern}/' -e '/libertinust1math/d' \
    -e '/textalpha/d' -e 's/\\usepackage\[danish\]{babel}/\\usepackage{babel}/' "$SRC" > t.tex
python3 - <<'PY'
import re; s=open('t.tex',encoding='utf-8').read()
s=re.sub(r'[Ͱ-Ͽἀ-῿]+','[Gr]',s)   # Greek → [Gr] only because sandbox has no textalpha
open('t.tex','w',encoding='utf-8').write(s)
PY
pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1; pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1
grep -o 'Output written.*' l.txt; echo -n 'char-warnings: '; grep -ic 'not set up\|missing.*character' l.txt
echo -n 'markers left: '; grep -c 'text to be added' "$SRC"
```
Expect 0 char-warnings, 0 errors. (`textalpha` is only needed on Hans's machine for real Greek, if any.)

## Finishing (per TRANSLATION-PLAYBOOK.md §6, adapted for a transcription)
When `grep -c 'text to be added'` = 0 and compile is 0/0:
1. Final sandbox compile → confirm page count, 0/0.
2. In `catalog.yaml`, set id `philosophiske-grundproblemer` section status **skeleton → in-progress**
   (transcription complete but no translation yet), and update the `note`.
3. Tell Hans to compile the PDF locally with the real fonts and confirm the Transcription link resolves.
4. **Phase 2 (separate job):** create `translation.tex` and translate front-to-back per
   `../../../TRANSLATION-PLAYBOOK.md`. Only then does the section status go to `complete`.
5. Hans commits & pushes — the assistant never does.

## Standing method
See `../../../TRANSLATION-PLAYBOOK.md` (general workflow) and, for the OCR/transcription mechanics
and the letterspacing/footnote discipline, the fuller precedent in
`../../brochner/problemet-tro-viden/RESUME-NOTES.md` (that one is Fraktur — here use `-l dan`).
