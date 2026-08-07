# R. Nielsen, *Om personlig Sandhed og sand Personlighed* (1854) — resume notes

Twelve popular lectures ("for dannede Tilhørere af begge Kjøn", i.e. for an educated
mixed audience), delivered at the University in the winter of 1854. Gyldendalske
Boghandling (F. Hegel), 1854. [1] + 144 pp., Fraktur. Same author and genre as
*Evangelietroen og Theologien* (1850), which is the reference implementation for the
whole method used here (pagemap.py / ocr.sh / spacing.py / check.py / splice.py /
BATCH-AGENT.md) — see `../evangelietroen-theologien/` for the fully worked example.

**Status: printed pp. 1–117 transcribed and spliced (Lectures I–X complete, ~81% of
the book). 27 pages remain, starting at printed p. 118 (Lecture XI).** Read
`../../../TRANSCRIPTION-PLAYBOOK.md` before continuing.

## Files
- Scan: `bibliotek/Nielsen, Rasmus/om-personlig-sandhed.pdf` (157 PDF pp., 33.5 MB,
  PyPDF2-produced, KB digitisation). KB metadata: physical extent "[1], 144 s."
- Transcription: `transcription.tex` (skeleton only — 13 markers: Forord + 12 lectures,
  no body text yet). Translation: not begun (separate later job).
- Catalog entry: `catalog.yaml`, author `nielsen`, id `om-personlig-sandhed`.

## ✅ PAGE MAP — VERIFIED UNIFORM, no offset change anywhere

    printed   1--144   ->   PDF = printed + 9      (PDF  10--153)

**How this was verified** (read directly off the page image, never off the embedded
text layer — see the warning below): rendered PDF 1–12, 21, 41–44, 64, 102, 141,
148–157 at 150 dpi and read the printed numeral by eye at each of the following
checkpoints, spaced across the full 157-page scan:

| printed | PDF | what's on the page |
|---|---|---|
| — | 1–5 | KB scan-metadata / barcode leaves (not part of the book) |
| — | 6 | title page (unnumbered) |
| — | 7 | blank verso |
| — | 8 | **Forord** — ONE page, unfoliated, dated "Kjøbenhavn, d. 1. Mai 1854", signed "R. Nielsen." |
| — | 9 | blank verso |
| 1 | 10 | "I. Indledning: en Phantasie." (chapter-opening page; no folio printed on p.1 itself) |
| 12 | 21 | "II. Æsthetisk og religiøs Phantasie..." (folio "12" printed at top) |
| 33 | 42 | "IV. Personlig Hjælp." (folio "33" printed at top, directly above the heading) |
| 55 | 64 | "VI. Store Mænd: personlig Overlegenhed." (folio "55" at top) |
| 93 | 102 | "IX. Skyld i Skrøbelighed." (folio "93" at top) |
| 132 | 141 | "XII. Personlig Stræben: en Slutning." (folio "132" at top) |
| 144 | 153 | last page of the book — ends mid-argument ("...og til denne Indledning vende vi nu tilbage...", the Slutning's closing testimony); no Indhold follows |
| — | 154 | blank |
| — | 155–156 | pastedowns / endpapers |
| — | 157 | back cover |

No jump anywhere in this range — every chapter-opening page's own folio (read at the
checkpoints above) agrees exactly with 9-plus-printed. This is unlike
evangelietroen-theologien, where a double-scanned leaf shifted the offset by +2
partway through; nothing analogous happens here. **Confidence: high** — six
independent checkpoints across the full body, plus both endpoints, all agree with a
single constant offset.

### The Forord has NO printed folio at all
Unlike evangelietroen's Forord (paginated III–VIII in roman numerals), this book's
Forord is a **single unfoliated leaf** — no numeral anywhere on the page, front or
back. Since `splice.py`'s batch-marker filename convention requires two plain arabic
integers (`pp<FIRST>-<LAST>.texfrag`), and there is no real printed number to use, the
skeleton keys the Forord's batch marker as the **synthetic pair `0--0`**:

    % [text to be added: pp. 0--0]      ->  fragment file .parts/pp0-0.texfrag

`0` was chosen because it can never collide with a real printed page (the body starts
at 1) and is self-evidently synthetic. When that batch is eventually written, use the
**non-digit** in-text page marker `% --- p. [Forord] ---` rather than `% --- p. 0 ---`
— `check.py`'s page-gap regex is arabic-only (`\d+`) and will silently ignore a
non-digit marker, exactly the mechanism evangelietroen relies on to ignore its roman
Forord markers. Do NOT use `% --- p. 0 ---`: that WOULD be picked up by the regex and
would corrupt the gap/dupe report for the real body pages.

### No Indhold anywhere in this scan
Checked the back of the book (PDF 154–157) directly on the image: blank page, then
pastedowns/endpapers, then the back cover — no table of contents. The front matter
(PDF 1–9) has none either. **This book's scan simply has no Indhold to transcribe or
to cross-check the lecture heads against** — unlike evangelietroen, where the Indhold
at the back caught two genuine OCR errors and two genuine printer variants. Here, the
titles and page ranges baked into the skeleton were read directly off each lecture's
own opening-page image, with no second witness to check them against. Flag anything
that looks off rather than trusting these entries blindly on the first pass through
each lecture.

## ⚠ TEXT LAYER WARNING
The embedded (PyPDF2/KB) text layer in this PDF is a **garbled OCR**, not a clean
witness — do not trust it for anything beyond the roughest structure-finding (e.g.
locating where a roman-numeral heading falls). Examples of its systematic corruption,
seen while locating the lecture heads via `pdftotext -layout`:

- `Æsthetisk` → `Msthetisk`; `religiøs` → `religiös`
- `Spørgsmaal` → `Sporgsmaal`; `være` → `vcrre`; `Sjælen` → `Sjcelen`
- `personlig Sandhed` renders fine, but `sand Personlighed` on the title page came out
  as `sand Personsighed`
- general æ→"cr" and ø→"o" substitution throughout

The scan itself, by contrast, looks like a clean, crisp Fraktur print in good
condition — similar to evangelietroen's. **Expectation, not yet confirmed:** a fresh
Fraktur tesseract pass (`ocr.sh`) should do much better than this embedded layer, the
same way it did on evangelietroen. Confirm this on the very first transcription batch
before trusting the OCR-first pipeline; if the Fraktur model struggles here the way it
did on Religionsphilosophie, switch to an eyeball-first pipeline instead (see playbook
§2).

## Footnote convention
Surveyed for footnote marks while locating the chapter heads; found exactly **one**
occurrence in the whole book, on printed p. 49 (inside Lecture V, "Selskab i
Eensomhed"): `...den personlige Sandhed.*)` with the note beginning `*) At den
Tænker, der i vor Tid sigtede...`. Set `\thefootnote` to the constant `*)` in the
preamble, matching evangelietroen's convention (same publisher-era house style).
**This has only been confirmed on one page** — if later batches turn up footnotes
marked differently, stop and reconsider rather than silently forcing them into `*)`.

## Structure: the twelve lectures (from the images — no Indhold to cross-check against)

| # | Printed title (verbatim) | Printed pp. | PDF pp. |
|---|---|---|---|
| I | Indledning: en Phantasie. | 1–11 | 10–20 |
| II | Æsthetisk og religiøs Phantasie: en personlig Forskjel. | 12–22 | 21–31 |
| III | Det evige Liv: en personlig Trang. | 23–32 | 32–41 |
| IV | Personlig Hjælp. | 33–42 | 42–51 |
| V | Selskab i Eensomhed: en personlig Opgave. | 43–54 | 52–63 |
| VI | Store Mænd: personlig Overlegenhed. | 55–67 | 64–76 |
| VII | Ubetydelige Mennesker. | 68–79 | 77–88 |
| VIII | En Timelærer. | 80–92 | 89–101 |
| IX | Skyld i Skrøbelighed. | 93–104 | 102–113 |
| X | Den Stærke og den Skrøbelige: et personligt Mellemværende. | 105–117 | 114–126 |
| XI | Personlighedens Vilkaar. | 118–131 | 127–140 |
| XII | Personlig Stræben: en Slutning. | 132–144 | 141–153 |

Total: 144 printed pages, matching KB's "144 s." exactly. Each lecture is headed by a
bare roman numeral ("I.", "II." …) plus its printed title — **not** the ordinal-word
style ("Første Forelæsning") used in evangelietroen. Each opens directly with a
drop-cap paragraph; **no italic "argument" summary** under the heading (unlike
evangelietroen, which prints one both at the chapter head and in its Indhold — moot
here anyway, since there is no Indhold).

## Batches done so far

| Batch | Pages | Lecture | Notes |
|---|---|---|---|
| pp1-11 | 11 | I, Indledning: en Phantasie | 1 `\emph{}` (Sperrsatz, p.11, confirmed); 0 footnotes; 0 `\textit{}`; 2 cross-page hyphenations silently rejoined |
| pp12-22 | 11 | II, Æsthetisk og religiøs Phantasie | 3 `\emph{}` (all confirmed Sperrsatz); p.12 "Forskiel" vs heading's "Forskjel" — genuine printer's variant, kept as printed; p.16 stray period logged; p.19 doubled full stop logged; 0 footnotes |
| pp23-32 | 10 | III (opening), Det evige Liv | 1 `\emph{}` (the Beatitude, p.32, confirmed); possible systematic Ø/D Fraktur confusion noted (p.24, "Øiekast") — worth adding to `ocr.sh`'s sed table if it recurs; 0 footnotes |

| pp33-42 | 10 | IV, Personlig Hjælp | 3 `\emph{}` (Scripture citations, confirmed Sperrsatz); **Ø/D Fraktur confusion recurs** ("Øiemed"→"Diemed", "Øieblik"→"Dieblik/Djeblik", "Øiekast"→"Diekast" — now confirmed at 3+ pages across two batches; NOT safe to blanket sed-fix since "Diadem" is a genuine word with the same opening); 0 footnotes |
| pp43-54 | 12 | V, Selskab i Eensomhed | 6 `\emph{}` (Scripture quotations, all confirmed); **1 footnote** (p.49, `*)`, confirmed as the mark — content transcribed in full); quote imbalance „18/“17 (+1) from a logged unclosed quote after "Sandheden." on p.48 — a genuine printer's defect, not a transcription slip; several stray ink marks logged, not transcribed as characters |
| pp55-67 | 13 | VI, Store Mænd | 0 `\emph{}`/`\textit{}` (Machiavelli's „Fyrste" stays in Fraktur, not antiqua); **Ø/D confusion recurs again** (pp.56,57,59,63,64) — now confirmed across 3 batches, still no safe blanket fix; quote imbalance „63/“64 (−1) from a logged missing opening „ on p.59 (continues a first-person quotation); doubtful "Admindelse" (likely printer's slip for "Aamindelse") kept as printed |

Fresh Fraktur OCR via `ocr.sh` confirmed usable (as hoped, matching evangelietroen) —
the OCR-first pipeline stands; no need to switch to eyeball-first.

**Quote-balance bookkeeping:** the two logged defects above (+1 from pp43-54, −1 from
pp55-67) happen to cancel in the whole-file count, so `check.py` currently reports
`balance=0`. **This is a coincidence, not a clean bill of health** — both defects are
real, logged in-line at their sites, and must stay in RESUME-NOTES so a future pass
doesn't mistake the net-zero for "nothing to review."

**Ø/D Fraktur confusion — now a confirmed recurring pattern** (pp.24, 33, 40, 41, 56,
57, 59, 63, 64, all words beginning "Øie-"). Systematic enough to consider a *scoped*
sed rule in `ocr.sh` (e.g. only at word-start followed by specific letter patterns from
"Øie-"), but "Diadem" (p.40) shows a blanket `D→Ø` substitution would corrupt a real
word — any fix needs to be narrow. Left unfixed in `ocr.sh` for now; continues to be
caught by eye every batch.

`check.py` after splicing pp.1–67:

    pages: 1..67  n=67  gaps=none  dupes=none
    progress: 67/144 = 46.5%   next page to transcribe: 68
    braces balanced: True (145 open / 145 close)
    markers remaining (text to be added): 7
    footnotes: 1 | emph: 14 | textit: 2
    quotes: „=149 “=149  balance=0 (coincidental — see above)
    suspect readings: 0

Sandbox compile test (libertinus → lmodern, libertinust1math/textalpha stripped, babel
stripped) succeeds: 69 pages, 0 `!`-errors.

| pp68-79 | 12 | VII, Ubetydelige Mennesker | **First confirmed `\textit{}` instances in this book**: "Eau de Lavande" and "Ecce homo" (both antiqua-in-Fraktur, p.75/p.78); 0 `\emph{}`; **Ø/D confusion now confirmed beyond "Øie-"**: also hits "Ømhed" (pp.71,78), plus continuing "Øine"/"Øieblik"; f/k and dropped-sk OCR errors fixed by hand (see below); 3 NEW logged quote defects (pp.71,73,73) — this batch's imbalance does NOT cancel against earlier ones, net file balance is now +1, not 0 |

**Quote-balance is no longer a coincidental zero.** After pp.68-79: „=199 “=198,
balance **+1**. This is the honest, expected running total per the playbook (printer's
defects are supposed to drift the balance away from zero) — do not "fix" it. Defects on
record so far, in order: p.48 unclosed „ (+1), p.59 missing opening „ (−1, cancelled the
first), p.71 "Hendes Formue?" unopened (+1), p.73 two nested opens sharing one close
(+1... actually reduces available closes, net effect included in the +1 above), p.73
unclosed quote running past the batch boundary. See the pp68-79 fragment's own `%`
comments for exact wording and line numbers; do not re-derive this from the totals
alone.

**New OCR error types seen for the first time in pp.68-79** (added to running list, not
yet added to `ocr.sh`'s sed table — still being caught by eye each batch): f/k confusion
("fun"→"kun", "funde"→"kunde"); dropped "sk" before j/k ("jule"→"skjule",
"fal"/"sal"→"skal", "ffulde"→"skulde"); "Zürlige"→"Ziirlige"; dropped ø in "Fro"→"Frø".

| pp80-92 | 13 | VIII, En Timelærer | 1 `\emph{}` (Sperrsatz, p.82, confirmed); **3 more `\textit{}`** ("Prima Donna" ×2 p.83, "con amore" p.84 — antiqua-in-Fraktur confirmed by zoom; "Renommée" p.84 checked and rejected, stays Fraktur); **Ø/D confusion still recurring, new words hit**: Øiemed, Øieblik, Øine, Ønske, Øvelse, and newly **Øret** (p.91) — every instance now resolved by cross-checking against a real "D" on the same page; 0 footnotes; 0 new quote defects — batch is internally balanced (29/29), so the running total is unchanged |

Running quote-balance total after pp.1-92: **+1**, unchanged since pp.68-79 (no new
defects in pp.80-92).

| pp93-104 | 12 | IX, Skyld i Skrøbelighed | 5 `\emph{}` (a recurring refrain letterspaced only at its first/last appearance — each of ~9 occurrences checked individually by zoom, not assumed uniform); **1 new `\textit{}`**: "camera obscura" (p.101); **Ø/D confusion continues** (Øiemed, Øieblik ×several, Øine) — **new printer's-spelling-variant finding**: p.102 has one genuine "Øjeblik" (with j) alongside two "Øieblik" (ie) on the same page, a real variant like Forskiel/Forskjel, not an OCR error; 0 footnotes; 0 new quote defects (batch internally balanced 22/22, running total unchanged) |

Running quote-balance total after pp.1-104: **+1**, unchanged since pp.68-79.

| pp105-117 | 13 | X, Den Stærke og den Skrøbelige | 1 `\emph{}` ("Jeg er Sandheden", p.106, confirmed); **1 new `\textit{}`**: "par renommée" (p.111); a refrain ("...personlig i den sidste Time", ~7× pp.113-117) checked individually and found NOT letterspaced anywhere, unlike the pp.93-104 refrain — confirms these must be checked case by case, no general rule; Ø/D confusion recurred again (pp.106,109,112,114×3,115,117); **1 NEW quote defect**: p.106 „Gaa af Veien!...bleven myndig!" opens but never closes (confirmed re-checking both p.106 foot and p.107 head) — balance moves +1→+2; other notes: p.109 stray hyphen wrongly joining "under-de", p.112 has later-reader ink underline (not print emphasis) causing spacing.py false positives, p.107 "Punker" (missing t) kept as printed despite correct "Punkt" elsewhere on p.115; 0 footnotes |

Running quote-balance total after pp.1-117: **+2** (new defect at p.106, on top of the
prior +1 from pp.48/59/71/73).

## Open items for a future review pass
- p.12 "Forskiel"/"Forskjel" printer's variant — confirm it isn't a transcription slip
  when doing the end-of-book review (playbook §6).
- p.16 and p.19 punctuation oddities — logged in-line as printer's defects, not yet
  independently re-verified.
- p.48 unclosed „ and p.59 missing opening „ — the two defects behind the (coincidental)
  net-zero quote balance; see above. Re-verify both against the image in the final pass.
- **Ø/D Fraktur confusion — recurring, unresolved in tooling.** Confirmed at pp.24, 33,
  40, 41, 56, 57, 59, 63, 64, always words beginning "Øie-". No blanket sed rule added
  because "Diadem" (p.40) would be corrupted by one. Needs a scoped fix or continued
  by-eye catching.
- Several stray ink marks logged across pp.43-67 (not transcribed as characters) —
  spot-check these are truly page defects and not lost punctuation, in the final pass.
- The Forord (synthetic marker `pp. 0--0`, ~1 page) is still untranscribed — independent
  of the rest, do whenever convenient.

## CURRENT RESUME POINT
**Printed pp. 1–117 done (Lectures I–X).** Next: printed p. 118, start of Lecture XI
("Personlighedens Vilkaar", pp. 118–131), marker `% [text to be added: pp. 118--131]`.
The Forord (`% [text to be added: pp. 0--0]`) also still needs doing, independently,
whenever convenient. Running quote-balance total: **+2** (four real logged defects at
pp.48, 59, 71, 73, 106 — see above; do not silently correct this).

## Printer's-spelling variants confirmed so far (record both readings, do not normalise)
- p.12: "Forskiel" (heading has "Forskjel")
- p.102: "Øjeblik" (elsewhere consistently "Øieblik")
- p.107: "Punker" (missing t; correct "Punkt" appears twice on p.115)

## Standing method
See `../../../TRANSCRIPTION-PLAYBOOK.md` for the batch-dispatch protocol, and
`../evangelietroen-theologien/RESUME-NOTES.md` for the fully worked example of the
same author, genre and era (including how its one real offset change was tracked, and
how its Indhold pass caught two printer variants — for contrast with this book, which
has no Indhold at all).
