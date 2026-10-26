# Høffding (ed.), *Udvalgte Stykker af dansk filosofisk Litteratur* (1910) — resume notes

## 2026-10-11: WHOLE-BOOK TRANSCRIPTION -- pipeline set up, PILOT run (front matter + Indledning + section I, pp. 1-44)

Hans approved transcribing the whole anthology (incl. Treschow's excerpt A, pp. 99-108, as the anthology prints it).
**Method: om-aandsdannelse's (antiqua, no e-book): the layer by rule, tesseract as independent witness, blind crops.**
Tools, all tracked in `ebook-method/udvalgte-stykker/` (copied from om-aandsdannelse and adapted; see their docstrings):
pagemap.py (whole book; `UDV=pilot|all|A-B` picks the run; `TEXFILE` the output), ocr.py, draft.py, patches.py,
template.tex, indhold.texfrag, rules.py, sheets.py (words / italic, with 2 controls a sheet), spacedsheets.py,
miscsheets.py (front matter, Indhold, headings, rules, paragraph starts, small caps, Greek), reads.py, READER-BRIEF.md.
`ebook-method/collate/check.py` got one optional setting, pagemap `TEXFILE` (backup check.py.bak.20261011-udv), and
now writes `.parts/collate/italics.tsv` (the open italics with boxes) on --italics.

**Edition check.** No e-book, no Wikisource text, no earlier transcription of the whole (only the hand-made section IV
file below). Scan (SCANS.tsv; the file once called mindesmaerkerafd03ande.pdf):
`~/bibliotek/Høffding, Harald/1910-udvalgte-stykker-dansk-filosofisk-litteratur.pdf`, IA, 400 ppi, clean ABBYY layer.
PDF = printed + 8 (pp. 1-306 = PDF 9-314); PDF 5 half-title, 6 series title, 7 title, 8 printer, 315-316 Indhold.

**Recon findings (2026-10-11, ~5 page images).**
- Høffding's text (Indledning, the numbered introductions "1. LUDVIG HOLBERG (1684—1754), ...", Anmærkninger) is in a
  SMALLER type than the excerpts: layer box height 12-13 pt vs 14-15 on every pilot page -> draft.py `\begin{intro}`.
- Names in Høffding's text are in SMALL CAPITALS at first mention (Indledning: HOLBERG, SNEEDORFF, TRESCHOW, STEFFENS,
  SIBBERN, KIERKEGAARD, NIELSEN, BRØCHNER; each § head name). The layer gives them in mixed case; tesseract in capitals:
  each is a case-only check -> readers mark `<sc>` -> decision SC.
- Excerpts: emphasis by LETTERSPACING (\emph; the layer sets spaced words as single letters, draft.py joins them and
  divides runs into words by corpus frequency) AND ITALICS for foreign words/names (very frequent in Holberg).
- Headings: opener = numeral + title in capitals + short rule (\anthsection); excerpt heading in capitals + source in
  parentheses (\excerpthead); a short rule between excerpts/authors (\sectionrule, found in the render). p. 1 opens
  with a large initial I (not reproduced). Footnotes (*) **)) only on 16 pages, none in the pilot (pagemap NOTE_PAGES).
  Running heads "AUTHOR : TITLE" in small caps + folio; signatures "Dansk filosofisk Litteratur N" and "3*" dropped.
- Greek on pp. 13-14 (both OCRs garbage; needs `\usepackage{textalpha}` after patching), English verse p. 40.

**Rebuild (pilot):**

    python3 ebook-method/udvalgte-stykker/ocr.py              # tesseract witness; rerun until "done" (~5 s/page)
    python3 ebook-method/udvalgte-stykker/draft.py --emit --force \
      && python3 ebook-method/collate/check.py udvalgte-stykker --italics --apply \
      && python3 ebook-method/udvalgte-stykker/draft.py --post
    python3 ebook-method/udvalgte-stykker/rules.py [--write]  # before --apply, on a fresh checks.tsv
    python3 ebook-method/udvalgte-stykker/sheets.py words; sheets.py italic; spacedsheets.py; miscsheets.py
    python3 ebook-method/udvalgte-stykker/reads.py [--write]  # after the readers

**Output: `.parts/pilot/transcription.tex`** (pagemap TEXFILE). The tracked transcription.tex (the hand-made section IV
file, catalogued and linked) is UNTOUCHED (backup anyway: transcription.tex.bak.20261011-prepilot). When the whole book
is built, set `UDV=all` (TEXFILE becomes transcription.tex); pp. 99-113 then come from the pipeline, and the old
decisions in decisions.tsv (section IV, 2026-10-03, kept at the top) apply where their keys still match; read the old
file's header notes into the new header. ocr.py has read ALL 306 pages (2026-10-11; .parts/collate/ocr/, renders in .render/); pp. 99, 108-113 are from the
2026-10-03 run (system tessdata, not the repo's tessdata_best): rerun those seven (move them aside) before collating section IV.

**Pilot state (2026-10-11).** 44 pp., 14 264 words (tesseract 14 283; every page within 85-115 %). 176 disagreements:
22 settled by check.py (glyph 2, split/noise 16 [--splits: 2 listed, harmless], noise 4), 47 by rules.py (punctspace
28 [space before ; : ? ! not transcribed], accent 8 [tesseract Å for A], layerfault 6, compound 5 [line-end hyphen of a
capitalised compound]); 1 layerfault withdrawn by hand (37|hånd>hand, rules.NEVER). OPEN 107 -> sheets b1-01..11 (107
crops + 22 controls). Italics: 155 open runs at ITAL 1.03 (99th pct 1.11) -> sheets i1-01..13 (+26 controls).
Letterspacing: 80 candidate lines (gap >= 0.15, calibrated; 16 draft \emph to confirm; 20 tesseract run-ons) -> l1-01..06.
Structure: 46 items -> m1-01..07 (front matter grid, Indhold 2 pp., 8 headings, 7 rules, 15 paragraph-start
disagreements, 4 small-caps names, Greek x3, verse, p. 35 lines the layer mixed).
Sheets: `.render/udvalgte-stykker-{b1,i1,l1,m1}-NN.png`; index and controls in `.parts/reads/sheets-*.tsv`,
`controls-*.tsv` (never shown to readers). Old/stale sheets moved to `.render/stale/`. reads.py self-tested on fake
readings (moved to .parts/reads/selftest/; controls 1 of 2 caught as designed).

**RESUME POINT.** Dispatch 4 blind readers with READER-BRIEF.md: A b1-01..10; B i1-01..09; C i1-10..13 + l1-01..06;
D m1-01..07 + b1-11 (every reader then has >= 2 controls). Then reads.py --write; decide the hand list; m1 answers ->
patches.py (headings, Greek with textalpha, p. 35 mixed lines, front matter/Indhold fixes in template.tex and
indhold.texfrag); spaced.tsv; rebuild chained to OPEN 0 (words and italics); then the house's last passes: --moved,
--splits, --unapplied, prescreen greps, two spot pages read in full with planted errors, and only then the pilot
verdict (errors per page) and the decision on running the rest of the book.

**2026-10-11 (later): readers' results applied -- pilot at OPEN 0.**
Readers A (b1-01..10), B (i1-01..09), C (i1-10..13, l1-01..06), D (m1-01..07, b1-11): files .parts/reads/r-*.tsv.
Controls 48 of 48 right (b1 22, i1 26). reads.py --write: 206 decisions + 52 spaced spans; 132 items decided by hand
(decisions.tsv "# by hand 2026-10-11"), doubtful ones at the image by the main session with zoom.py (tracked; crops
.render/udvalgte-stykker-z1..z5-NN.png): Skue-Spil, Latter, alt,, (PRINTED AS IS), Philosophiske, Grundvold (no stop),
fodre (PRINTED AS IS), puure, pœna, Svift, „— —“ pp. 43-44, Creta/Lacedæmon, the Greek of pp. 13-14 at 900 dpi,
Tyndal/Morgan/Chub, Occam/Svarez, Præexistence, Indhold (I. S. SNEEDORFF, Væxt, INDHOLD:), the p. 29 source „47).“
(reader D's „47.)“ was wrong), the letterspacing of pp. 17-20, 38-41. Reader C left short words outside multi-line
letterspaced passages; at the image they are spaced too: those passages are set whole by patches.POST. One blind-read W
overridden (41|Er>E r: one letterspaced word), one rule-free W kept as T (moralske: only the stem italic).
Patches: 11 PATCHES (Greek x3, p. 36 source line, p. 15 heading, the layer's line-initial „i“ set after the first word
on pp. 30/31/32/35 -- a systematic IA-layer fault, see prescreen.py 'lone' --, Ac-tion over the page turn, the p. 20
spaceless line), 31 POST (italics, letterspaced passages, misprint marks, œ). spaced.tsv: 24 wrapped.
Chain: draft OPEN 0 (words, italics); the collated file itself also OPEN 0 (the post-state keys decided T "as it
stands"); --unapplied empty; --splits 1 (er barmhiertig, right). prescreen.py: words per page all within 85-115 %,
lone 21 (reviewed: the four real ones mended, the rest line-break noise), speck 1 (Sneedorff's, right), double 1
(Troe! Troe!, right), marks 0. Sandbox compile (§5 recipe on the device, Greek as placeholder): 0 errors, 0 missing
characters, 43 pp. Front matter (template.tex) and Indhold (indhold.texfrag) now as read at the image.
OCRDIFF: tesseract (repo tessdata_best, dan) | 175 candidates | 61 corrected | 114 witness's fault | 0 unresolved
(+ italics 156 runs, 134 set; letterspacing 80 lines). Second-reading sheet: none needed (all doubts settled at the image).

**Sampled page check -- PREPARED, NOT READ.** `ebook-method/udvalgte-stykker/pagecheck.py` (from speculative-logik) +
`PAGECHECK-BRIEF.md`. Sample (seed 20261011): pp. 12, 16, 33, 38 + the title page (page 0 = PDF 7); 18 strips on
`.render/udvalgte-stykker-pc-01..09.png`; selftest PASSED (read-back 0 differences on all five; 5 injected faults -- a
letter, a word, a comma, an italic, a letterspacing -- all found). Reader writes .parts/pagecheck/reading-1.tsv; then
`pagecheck.py compare .../reading-1.tsv`, decide diffs.tsv, `pagecheck.py rate`.

**RESUME POINT (now).** Dispatch ONE reader for the page check; adjudicate; then the pilot verdict and Hans's decision
on the rest of the book (UDV=45-98 etc.; rerun ocr for pp. 99, 108-113 first).

**2026-10-11 (last): page check read, translator's odd spots settled -- PILOT DONE (pending Hans).**
Page check (reading-1.tsv, one blind reader; `pagecheck.py compare` + rate; decided rows in .parts/pagecheck/run1-diffs.tsv):
pp. 12, 16, 33, 38 + title, 1343 words, 12 differences: 8 the reader's (Argu-menter division; interessered, Umueligheder,
blant as printed, z6; title-page descriptions/dots), 0 word errors, 0 punctuation (95 % upper 2.2/1000), 2 markup faults
= 4 words (B. S. italic p. 12; og spaced in the p. 38 passage), mended by POST (the p. 38 spaced.tsv entries replaced).
Translator's odd spots (.parts/pilot/tr-odd.tsv), at the image (zoom.py z6-z8, 450-900 dpi): mended p. 5 à priori, p. 6
Hexerie, (faint comma), p. 32 han er; PRINTED AS IS p. 18 føend + døde (probably døbe), p. 20 taelt; as printed p. 31
endelige, p. 41 elliptic „enten ikke det Gode“. translation.tex (pilot) updated at à priori, B. S. (italic), the p. 38
spaced passage, a note at „baptized“; backup translation.tex.bak.20261011-oddspots; \opage 44/44; sandbox compile 43 pp.
Final: chain OPEN 0 (words, italics), the collated file itself OPEN 0, --unapplied empty, prescreen clean, transcription
compiles (0 errors, 0 missing characters, 43 pp.). Header of the pilot carries the page-check rate and the odd spots.
The VM's /sessions disk is nearly full (other sessions): zoom.py now deletes each page render after cropping.
NEXT: Hans decides on the rest of the book (UDV ranges; rerun ocr.py for pp. 99, 108-113 first).

**Hans's decisions (2026-10-11, after the pilot).** (1) The Indledning and Høffding's §§ stay at NORMAL size, marked as
introductions: `intro` is now `{\par}{\par}` (no \small) and the whole Indledning pp. 1-3 is in it (pagemap.NO_INTRO = the
Anmærkninger only; PATCHES[0..1] put its first paragraph, with the large initial, inside). (2) p. 8 „alt,,“ stays two
commas (PRINTED AS IS). (3) Small caps set where the readers mark them (\textsc), not normalised. All three are in the
template header. (Still standing: the excerpts are transcribed as Høffding printed them, his redaction.)

## 2026-10-11: ROUND 1 -- sections II-III, pp. 45-98: built, collated, sheets cut (READERS NOT YET DISPATCHED)

**Build.** pagemap `UDV=build` (now the default): pp. 1-BUILD_TO (98) -> `.parts/pilot/transcription.tex` (folder name
kept); `UDV=pilot` now writes pp. 1-44 to .parts/pilot44/, never the build. Backups `*.bak.20261011-prebuild98` (build
file in .parts/pilot/, the scripts, decisions, spaced, template, this file in .parts/). Rebuild = the pilot chain
unchanged (draft --emit --force && check.py --italics --apply && draft --post). pp. 1-44: identical to the settled pilot
text except the two `intro` lines round the Indledning (Hans's decision); still OPEN 0 there.

**Recon (3 page images: pp. 45, 68, 84; sheet m2-03 checked).**
- From p. 45 IA's layer gives ONE box height per page block (p. 45: 13 pt for § and excerpt alike), so SMALL_H fails.
  From pagemap.SMALL_OCR_FROM = 45 the type size comes from TESSERACT's boxes (draft.ocr_class): median height of a
  line's words with an ascender and no descender, px at 300 dpi -- excerpts ~41-42, §§ ~36-38, note type ~28-30
  (ASC_SMALL 39.5, ASC_QUOTE 33; x-height words as fallback). A change of type starts a paragraph.
- NEW element: quotations inside an excerpt set in note type (p. 68 Mynster's objection; pp. 77-78) ->
  `\begin{smallquote}` (template: an indented quote, normal size).
- Running heads pp. 64-76 („68 H. c. ørsted: videnskab og religion“): the layer reads the small caps in lower case ->
  pagemap.HEAD_LC (draft.py, first line of a page only).
- Footnotes: 5, one *) each (pp. 65, 66, 82, 84, 93; NOTE_PAGES also lists later pages). draft.py split a note at a
  line after a hyphen (pp. 65, 84) -> fixed (a line after „-“ continues the note). The notes have letterspaced names
  (Eilschov, Risbrigh, Skabelunde ...). p. 66 note „hvorlunde ogenlunde o. s. v.“ (n lost? misprint?) -> m2 note + b2.
- Steffens marks emphasis by ITALICS (Kundskabens, Interessens, p. 45); the Ørsted dialogue's speaker names are
  letterspaced (Alfred., Sophie., Herman.); p. 68 a letterspaced passage over 4 lines. German only in the notes (Kant
  titles, p. 82, 93); Latin „qvod dubitas, ne facias“ p. 93; no Greek or verse; centred sub-headings pp. 54, 58.
- rules.py: 'mark' (tesseract's ') %) +) ?) for *)) switched on for NOTE_PAGES only.

**Counts, pp. 45-98.** 54 pp., 16 102 words (tesseract 16 156). WORDS PER PAGE vs tesseract (its running head dropped,
line-end hyphens joined): 99-102 % on every page (pilot 96-104 %) -- no missing text. 152 disagreements: 11 settled by
check.py (glyph/split), 57 by rules.py (punctspace 38, layerfault 8 [aliene>allene, oploser>opløser (ø rule), ængsdige,
samdige, Viddøftighed, egendige, innerlialb, biossen], mark 8, accent 2, guillemet 1), OPEN 84 -> image.
Italics: 21 open runs. Letterspacing: 79 candidate words on 55 lines (running heads, capitals, line-end halves and every
lone „i“ excluded); 33 more lines of „Alfred.“/„Sophie.“ not cropped -> `.parts/reads/repeat-l2.tsv` (set by pattern
once the first two of each are read). Structure: 43 items (13 head, 8 rule, 2 sc, 5 note read whole, 11 par, 4 extra:
p. 64 Venus/Minerva/Apol- line, p. 66 Bestanddele, p. 68 and p. 78 the small-type quotations).

**Sheets (round 1, CONTROLS ON EVERY KIND now, 2 a sheet):** `.render/udvalgte-stykker-{b2,i2,l2,m2}-NN.png`, index
`.parts/reads/sheets-*.tsv`, controls `controls-*.tsv`. b2-01..07 (84 + 14 controls, 12 a sheet), i2-01..02 (21 + 4),
l2-01..03 (55 + 6; controls: an Indledning line = 'roman', a word the pilot settled as letterspaced = 'sp:word'),
m2-01..08 (43 + 16; controls: settled pilot rule/par items, yes and no). Commands:
    python3 ebook-method/udvalgte-stykker/sheets.py words --tag b2 --per 12 --pages 45-98
    python3 ebook-method/udvalgte-stykker/sheets.py italic --tag i2 --per 11 --pages 45-98
    python3 ebook-method/udvalgte-stykker/spacedsheets.py --tag l2 --pages 45-98 --per 21
    python3 ebook-method/udvalgte-stykker/miscsheets.py --tag m2 --pages 45-98 --maxh 2050
reads.py: `--tags b2,i2,l2,m2` (else the pilot's reader files are re-read) and scores l/m controls too; selftest with
fake readings in .parts/reads/selftest/round1/ (40 controls, the 2 planted misses caught). READER-BRIEF.md: round-1
tags, the `note` kind, <sp> in transcribed m-answers. Superseded sheets in .render/stale/.

**RESUME POINT.** Dispatch three blind readers (READER-BRIEF.md): E b2-01..07; F i2-01 i2-02 l2-01 l2-02 l2-03 m2-01
m2-02; G m2-03..08. Then `reads.py --tags b2,i2,l2,m2` (dry) and --write; hand list; m2 answers -> patches (headings
and sources, notes, centred sub-heads, p. 64/66 lines); spaced.tsv + repeat-l2.tsv; rebuild to OPEN 0; the house's last
passes (--moved, --splits, --unapplied, prescreen, a page check); then BUILD_TO for the next round (pp. 99 ff.: rerun
ocr.py for pp. 99, 108-113 first).


**2026-10-11 (later): ROUND 1 READ AND APPLIED -- pp. 1-98 at OPEN 0.**
Readers E (b2-01..07), F (i2, l2, m2-01..02), G (m2-03..08): .parts/reads/r-{b2-E,i2-F,l2-F,m2-F,m2-G}.tsv.
Controls 39 of 40 (b2 14/14, i2 4/4, m2 16/16, l2 5/6): the miss l2-03-11 „sp:franske“ is a FAULTY CONTROL -- p. 18 has
„franske“ also unspaced („Den franske Konge“) and the crop took that one; spacedsheets.py's spaced controls should use
words that occur once on their page (to do before the next round).
`reads.py --tags b2,i2,l2,m2 --write`: 70 decisions (54 words, 16 italics) + 60 spaced spans. reads.py bug fixed: a
case-only check inside a longer <sc> span („<sc>Hans Christian</sc>“) is now SC (60|Hans, 60|Christian set SC by hand).
By hand (decisions.tsv „# by hand 2026-10-11 (round 1“): 29 words, 5 italics; amended: 67|v,at T (the W would have deleted
the p. 66 note's „v.“), 84|Fuldkommenhed. T (the „*)“ is the \footnote mark); 6 post-state keys T; rules.py 1 more.
At the image (main session, zoom.py y1 at 600 dpi, y2 at 1200 dpi, y3 at 500 dpi; crops .render/udvalgte-stykker-y1..y3):
p. 66 note „o. s. v.“ -- the marks after s and v sit ON the baseline, no descender, the same as after o: worn stops, not
commas (the converse of TRANSLATION-PLAYBOOK §6k); p. 66 „ogenlunde“ PRINTED AS IS (probably nogenlunde); p. 60 „III“
without a stop PRINTED AS IS (pagemap.OPENERS[60] = 'III'); p. 93 note „Vernuft“ PRINTED AS IS (reader G normalised it to
Vernunft); p. 73 Virkningslovene (an ink blot under the v; both readers saw it); p. 69 „d e t“ letterspaced; p. 69
„Forandringer: Loven“ (the layer moved the colon: PATCH); p. 81 nødvendigviis, p. 93 Overbeviisning (the second halves of
broken words); p. 54 the first „og“ not spaced (F's doubt); p. 68 „men“ not spaced, „naar Grundsætningen ...“ spaced (F
had read „men naar“); p. 80 NO rule above § 2 (G; PATCH removes the draft's \sectionrule); p. 84 note ends
„Rettigheder.“; p. 85 „altsaa“ (layer „ahsaa“); p. 87 „fjærner“ (the layer split it: --splits; PATCH).
Speaker names: patches.POST_ALL (new in draft.py --post: a regex applied to every match, the count must be exact): 38 +
1 „Alfred.“/„Sophie.“/„Herman.“ letterspaced, pp. 60-67; three that the draft ran on into the paragraph before get their
break (m2-07-01/11 par yes); y1 Y11-Y13 (pp. 63, 64, 66) checked at 600 dpi.  spaced.tsv: 42 spans from F; 18 proposals
that cross a line-end hyphen or run over lines replaced by POST passages (pp. 54, 59, 64, 66, 68, 81, 83, 92).
m2 answers set by patch: the centred sub-headings pp. 54, 58 letterspaced; p. 60 source „\textit{(Brudstykke af en
Samtale)}.“; p. 60 \textsc{Hans Christian} \textsc{Ørsted}; p. 64 „i \emph{Apol}“, „\emph{Minerva}“ (the layer's
„Minerv a“); p. 83 „\emph{Kant} og \emph{Fichte}“ (layer „KantogFichte“), \emph{Spinoza}; the p. 93 note's Kants.
Reader doubts about the italics of punctuation after an italic word (F: i2-01-01/03/08/13, i2-02-07/11/12) left as the
slant check set them (as in the pilot: NOT ESTABLISHED, in the header). No second-reading sheet needed.
READER-BRIEF.md: an ANSWER FORMAT for `extra` (the m2 labels showed no question; miscsheets.py now prints the question on
the label's second line for extra items).
Final: chain OPEN 0 (words, italics); the collated file itself OPEN 0; --unapplied empty; --splits 1 (p. 28 er
barmhiertig, the pilot's, right); words per page vs tesseract (head dropped, hyphens joined) pp. 45-98 99-102 %,
pp. 1-44 96-104 %; prescreen words 0, lone 52 (the 19 on pp. 45-98 each checked against tesseract: all right), speck 1,
double 1 (both the pilot's, right), marks 0; sandbox compile (§5 recipe, Greek as placeholder): 0 errors, 0 missing
characters, 85 pp.
OCRDIFF: tesseract (repo tessdata_best, dan) | 152 candidates | 47 corrected | 94 witness's fault | 0 unresolved
(+ 11 settled by check.py as glyph/split; italics 21 runs, all set; letterspacing 55 lines read + 33 by pattern).
**Page check round 1 -- PREPARED, NOT READ.** pagecheck.py now takes PCRUN=2 (pp. 45-98, no title page; files *-2.tsv;
footnotes compared as mark + note at the page foot). Sample (seed 202610112): pp. 61, 65, 96; 12 strips on
`.render/udvalgte-stykker-pc2-01..06.png`; selftest PASSED (read-back 0 differences on all three, incl. the p. 65 note;
4 injected faults found -- no italic on p. 61 to inject). PAGECHECK-BRIEF.md: a „Which round“ section and footnotes.
RESUME POINT: dispatch ONE page-check reader: „Follow ebook-method/udvalgte-stykker/PAGECHECK-BRIEF.md in ~/mnt/danish-texts.
Round 1: sheets pc2-01 … pc2-06, write .parts/pagecheck/reading-2.tsv.“ Then `PCRUN=2 pagecheck.py compare
.../reading-2.tsv`, decide diffs-2.tsv, `PCRUN=2 pagecheck.py rate`; header; then BUILD_TO for round 2 (pp. 99 ff.;
rerun ocr.py for pp. 99, 108-113 first).

**2026-10-11 (last): ROUND 1 DONE -- page check read, translator's odd spots settled. pp. 1-98 at OPEN 0.**
Page check (reading-2.tsv; `PCRUN=2 pagecheck.py compare` + rate; decided rows .parts/pagecheck/run2-diffs.tsv = diffs-2.tsv):
pp. 61, 65, 96, 956 words, 3 differences: 2 the reader's (p. 96 „Mueligheden“ is printed, y4 O16; the „=“ at the p. 96
foot), 0 word errors, 0 punctuation (95 % upper 3.1/1000), 1 markup fault (p. 65 „d e n“ letterspaced, missed by l2: a
short word; mended by POST). Reader's „Naturgrandskerne“ and the NATURLOVE head as printed: right.
Translator's odd spots: 23 rows in .parts/pilot/tr-odd.tsv; outcomes in .parts/pilot/tr-odd-round1-decided.tsv:
6 MENDED (p. 68 „Dyr- og“ -- the draft's hyphen join; p. 70 „i Banens“ and, found with it, p. 84 „i Grunden“ -- the
layer's line-initial „i“ after the first word, which reads.py had then DELETED by a W: 70|i>, 84|i> now T + PATCH;
p. 71 „Iagttagelseskunst“, p. 72 „Iis“ x2, p. 88 „Individualitetens“ -- capital I both OCRs read as l; p. 83 a nested
\emph), 3 PRINTED AS IS (p. 52 „den den“, p. 81 „brad“, p. 88 „til aflede“), 15 as printed. Also p. 52 „et“ italic.
LESSONS for round 2: (1) a b-sheet W that DELETES a lone „i“ (key „N|i>“) is the layer's moved „i“ -- never a W
without the moved word put back (pilot pp. 30-35 had the same; prescreen 'lone' does not catch a deleted one);
(2) draft.py joins „Dyr-|og“: a suspended hyphen before og/eller (check prescreen for „-og“ joins); (3) capital I
read as l by both OCRs (lis, lagttag-): grep the build for r'\bl[agt]' style non-words; (4) spaced.tsv proposals
inside a POST passage nested \emph -- draft.py --post now skips a span inside an \emph (_inside()).
translation.tex (pilot folder, now pp. 1-98): the matching spots only -- pp. 54, 68, 83 the nested \emph undone, p. 52
\textit{a}, p. 65 \emph{he}, p. 84 „he is at bottom working to uproot“, the Indledning in intro (pp. 1-3) and intro at
normal size; backup translation.tex.bak.20261011-round1odd. tr_check.py now counts environments over the WHOLE file
(intro opens p. 1, closes p. 3) and checks they balance: all OK, \opage 98/98.
Final: chain OPEN 0 (words, italics), the collated file OPEN 0, --unapplied empty, prescreen clean, sandbox compile of
BOTH files: 0 errors, 0 missing characters, 85 pp. each.

**RESUME POINT -- ROUND 2: pp. 99-161 (IV TRESCHOW pp. 99-146, V pp. 147-161).**
1. Tesseract: rerun ocr.py for pp. 99 and 108-113 (made 2026-10-03 with the system tessdata, not tessdata_best): move
   .parts/collate/ocr/p{99,108..113}.tsv aside (no rm: .parts/collate/ocr/stale-20261003/), then
   `python3 ebook-method/udvalgte-stykker/ocr.py 99 113`.
2. pagemap.BUILD_TO = 161; back up the build file; rebuild; pp. 1-98 must stay identical (diff the body as /tmp/udvchain.sh
   did: the TEXT part up to „% --- p. 99 ---“ against the backup) and OPEN 0.
3. SECTION IV DECISIONS (decisions.tsv top, „2026-10-03“, 12 keys pp. 99-113, against the old hand-made file and the old
   witness): they apply only where their key still matches; after the rebuild run `check.py --unapplied` and read every
   one of them against the new open list -- a stale key is harmless but must not be trusted as a reading; the old
   „E113|Pallas's>roman“ (letterspaced, not italic) and the small-caps notes still hold as image facts. The old tracked
   transcription.tex (section IV, hand-made 2026-10-03, catalogued and linked) stays UNTOUCHED until UDV=all; read its
   header notes into template.tex when the section is done.
4. TRESCHOW A (pp. 99-108, „Gives der noget Begreb ... om eenslige Ting“): transcribed AS THE ANTHOLOGY PRINTS IT
   (Hans: Høffding's redaction, cuts and spelling as printed). texts/treschow/enslige-ting/ holds the complete essay from
   the 1810 original: use it only as a THIRD WITNESS by script (word diff against the draft) to find shared OCR errors;
   where 1810 and 1910 differ, the 1910 print governs (read at the image), never the original. Record the differences
   found (cuts, spelling) in RESUME-NOTES, not in the text.
5. Recon (<= 3 page images: the p. 99 opener, a NOTE_PAGES page 110/124/144, the p. 147 opener); then rules.py, blind
   sheets with tags b3/i3/l3/m3 (spaced controls: words that occur once on their page -- the round-1 faulty control),
   three readers, reads.py --tags b3,i3,l3,m3, hand list at the image, page check PCRUN=3 (add a stratum in pagecheck.py),
   translator's odd spots, OCRDIFF line.


= *Mindesmærker af Danmarks Nationallitteratur* III, ed. Vilhelm Andersen.
Kjøbenhavn: Gyldendal 1910, 306 pp. Høffding supplied the introductions.

**Why this file exists.** Not to re-transcribe the anthology's excerpts — the
1810 Treschow essay is already transcribed and translated *complete, from the
original printing*, at `../../treschow/enslige-ting/`. What matters here is the
**transmission document**: Høffding's own framing of Treschow, and the shape of
the selection he passed on to his readers (Bohr's milieu among them).

## Scan & offset
- `~/bibliotek/Høffding, Harald/mindesmaerkerafd03ande.pdf` — Internet Archive,
  320 PDF pp., **clean OCR — use this**.
- `~/bibliotek/Høffding, Harald/udvalgte-stykker.pdf` — HathiTrust (Wisconsin,
  Google-digitized), 321 pp., **badly jumbled OCR** (column order scrambled);
  useful only as a second set of page images.
- **Offset: renderer page = printed + 8.** Section IV opens printed p. 99
  (unnumbered section opener, signature "7*" at foot) = render p. 107.
- ⚠ `pdftotext`'s form-feed indexing differs from `pdftoppm`'s by ~3 on this
  file. Trust the renderer offset when pulling images; recalibrate if in doubt.
- Type is **antiqua**; proper names in small caps; Danish low–high quotes „…".

## Structure of section IV, "Den psykologiske Skole (Treschow, Sibbern, Howitz)"

| Anthology pp. | Content |
|---|---|
| 99 | Section heading + Høffding's § 1 (introduction to Treschow) |
| 99–108 | **A. Det Individuelles Uudtømmelighed** — from the 1810 essay |
| 108–113 | **B. Udviklingslære** — from another work (see below) |
| 114 | § 2 introduces F. C. Sibbern (then § 3, presumably Howitz) |

Høffding's editorial notes are **distributed**, one before each author, not
gathered at the head of the section.

## What Høffding kept from the 1810 essay (excerpt A)

Collated mechanically against the complete transcription (12 evenly spaced
30-character probes per printed page):

| Original printed pp. | In excerpt A |
|---|---|
| 225–229 | kept (full) |
| 230 | partial |
| **231–234** | **cut** |
| 235–240 | kept (full) |
| 241 | first line only (completes the sentence begun on 240) |
| **242–254** | **cut** |

The excerpt therefore **ends on the "Hielpemidler til Oversyn" passage**, with
its closing words "...rigtigen er det alligevel at giøre Forskiel paa denne
abstrakte Forestilling om det Enslige og den concrete." **The omissions are
silent** — no ellipses, no rules, no editorial note marks the cuts.

What this means: Høffding transmitted the *epistemological* Treschow (the limits
of general concepts, dissolving species boundaries, individuality as nature's
aim) and dropped the metaphysics — the rights-and-personality argument, the
circle/sphere and Godhead-as-perfect-individuality, and the whole second half:
the identity-system, Plotinus/Spinoza/Fichte/Schelling, the thesis restatement at
p. 247 that the concept of singular things has objective validity and reality,
Democritus, germs and preformation, and the closing. See
`../../treschow/enslige-ting/RESUME-NOTES.md` for the full discussion.

## Three points worth exploiting

1. **Høffding's own title.** The excerpt is headed *Det Individuelles
   Uudtømmelighed* — "The Inexhaustibility of the Individual." That is
   Høffding's phrase, not Treschow's, and it names an epistemic thesis (the
   individual outruns any concept) rather than the metaphysical one Treschow
   actually argues for.
2. **A shifted framing.** In *Danske Filosofer* (1909) Høffding calls the essay
   "directed against Schelling"; here in § 1 the opposition is broadened to
   "den tyske Filosofis Opgaaen i almene og abstrakte Begreber" — German
   philosophy's absorption into general and abstract concepts. Note that the
   anthology cuts *both* Schelling passages (original pp. 231 and 246).
3. **Høffding's dating.** § 1 cites the essay as *Videnskabernes Selskabs
   Skrifter* **1807** — the signed date carried in the volume's footline —
   though the volume was published 1810. Cite with care.

## Excerpt B, *Udviklingslære* — source VERIFIED

Høffding prints no source at the excerpt. His § 1 points to *Elementer til
Historiens Filosofi* (1811), and that attribution is **confirmed**:

- Searching nb.no's full-text index across Treschow's works, the distinctive
  tokens **"Thibetanerne"** and **"Evolutions"** occur **only** in *Elementer til
  Historiens Philosophie* (1811) — zero hits in *Om Gud* I, *Philosophiske
  Forsøg* (1805), *Om Philosophiens Natur og Dele* (1811), *Om den menneskelige
  Natur* (1812).
- Anthology pp. 111–112 are word-for-word identical with *Elementer*, **printed
  p. 80 = scan p. 92** (image-verified against
  `~/bibliotek/Treschow, Niels/elementer-til-historiens-philosophie-1811.pdf`).
  The relevant region of *Elementer* is roughly scan pp. 87–95.
- ⚠ **Orthography differs.** The 1811 original is Fraktur and uses **ø**;
  Høffding's anthology normalizes (and drifts — e.g. "Øjet" beside "Øiekast").
  The anthology is Høffding's redaction. **Cite the 1811 original**, and
  transcribe from it if the passage is quoted at length.
- Extent within *Elementer* has **not** been collated end-to-end; only the
  identity of the source and the p. 80 anchor are established. Whether Høffding
  cut silently here too, as he did in excerpt A, is still open.

## STATE
- **DONE:** Høffding's editorial matter for Treschow — section heading, § 1, and
  both excerpt headings — plus **excerpt B in full** (anthology pp. 108–113),
  transcribed, **every page image-verified**, and translated. Both files compile
  0 errors / 0 char-warnings, 5 pp. each, with structural parity (8 page markers,
  5 `\emph{}` spans, 1 footnote on each side).
- Excerpt A is deliberately **not** re-transcribed here: the 1810 essay exists
  complete and from the original printing at `../../treschow/enslige-ting/`.
- **TODO (optional, in rough value order):**
  1. § 2 on Sibbern (p. 114) and § 3 on Howitz — relevant to the
     Treschow→Sibbern→Kierkegaard question.
  2. Collate excerpt B against *Elementer* end-to-end, to see whether Høffding
     cut silently here as well.
  3. Høffding's general *Indledning* (pp. 1 ff.) mentions Treschow in passing
     when tracing the Holberg/Sneedorff line forward to Høffding and Kroman.

## 2026-10-03: collated against the scan (ebook-method/collate/check.py)

Run: `python3 ebook-method/collate/check.py udvalgte-stykker [--sheets|--italics|--pages]`; settings in
`ebook-method/udvalgte-stykker/pagemap.py`, every decision in `ebook-method/udvalgte-stykker/decisions.tsv`. The
header of transcription.tex says what changed. Ledger row updated (repaired).


## 2026-10-11: ROUND 2 -- sections IV-V, pp. 99-161: built, collated, sheets cut (READERS NOT YET DISPATCHED)

**Build.** ocr.py rerun for pp. 99, 108-113 (old tsv in .parts/collate/ocr/stale-20261003/). pagemap.BUILD_TO = 161.
Backups `*.bak.20261011-prebuild161` (build file in .parts/pilot/; scripts, decisions, spaced, template, checks.tsv,
this file in .parts/). Chain unchanged (draft --emit --force && check.py --italics --apply && draft --post). pp. 1-98:
body identical to the settled text (diff 0 lines), still OPEN 0; the only header change is template.tex's footnote mark
(\fnsymbol gave a dagger for note 2: now *) **) ***), needed for p. 144).
**Fixes made before collating (layer and tesseract agree; recon images r3-p121, r3-p144, r3-p146):**
- pagemap.OPENERS: section V opens on p. **146** („V / HEIBERG OG POUL MØLLER“, no running head; p. 147 has one), not
  147 as the Indhold says (indhold.texfrag keeps 147 as printed: record both). The numeral looks stopless at the image
  (p. 146 „V“; the old file had „IV“ too): m3 head items decide -> PRINTED AS IS as for p. 60 „III“.
- PATCHES (5 + 1): p. 99 § 1 broken at the title line by the type measure (joined; m3 extra asks italics/type);
  p. 111 the running head „TRESCHOW: UDVIKLINGSLÆRE 111“ read as a heading + a rule (each running head has a rule
  under it: not a \sectionrule); p. 114 „2. Hos \textsc{F. C. Sibbern}“; p. 121 B and p. 126 C excerpt headings (head
  in capitals + source in roman on one line: the capitals rule missed them); p. 144 note **) at „Ubekjendte**)“ (the
  layer read **) as “)).
- rules.py NEVER += opstøde/opstode (both words), Forplanteise (old text differs), Atttraa (p. 121: printed „Atttraa“,
  seen in r3-p121 -> a POST PRINTED AS IS mark is due once b3 confirms).
- Old section-IV decisions (2026-10-03): 8 of 12 keys still match (TRESCHOY, HOVWITZ, („Gives, selv?/ %) note marks,
  forstase, Årter x2: crop-checked then, kept); 4 stale (no effect).
**Counts.** 63 pp.; 19 959 words (tesseract 19 769, running head dropped, hyphens joined); words per page 98.8-102.9 %.
OPEN after check.py 199 (+8 old keys); rules.py 79 (punctspace 47, layerfault 15, accent 11, mark 3, compound 2,
para 1) -> OPEN 120. --moved 0; --splits 4 on these pages (Selvre flection, Indadgaaen i sig, b eængstende, Af
fectation: letterspacing, in l3/b3); --dropped: letterspaced words only. prescreen: lone 0 on pp. 99-161 (but b3 has
four „N|i>“ keys, pp. 115, 117, 118, 160: the round-1 lesson -- a W deleting a lone „i“ needs the moved word put back),
speck 7 (Palla s's p. 113 in b3; the rest apostrophes, right). Italics: 19 open runs (Latin in Sibbern/Howitz, a priori).
**Third witness, Treschow A (pp. 99-108) vs the 1810 original (texts/treschow/enslige-ting):** 136 diffs, of which
~95 Høffding's ö->ø, 1 big cut (orig. pp. 231-234 inside p. 103, and 242-254 after p. 108, silent, as noted above),
and 23 spots where layer and tesseract agree but 1810 differs -> `ebook-method/udvalgte-stykker/extra-b3.tsv` (keys X...,
on b3 sheets via `sheets.py words --extra extra-b3.tsv`; reads.py lists X keys for the hand, never decides): Abstraktion,
Tankekraftens, „de første“, Mennesker., word order „kan man ei derom giøre“, ganske, indsaa, afgjort x3, har, „høieste
og“, allene, / giøre, / derpaa; / tvivlsomt / maa / Værker / kiendeligere / Beskrivelse / „betegne de“ / „endskiøndt de“ /
abstrakte. Whatever the image shows, 1910 governs; differences found go into this file (not the text).
**Old hand-made section IV text (tracked transcription.tex) vs the draft, § 1 + excerpt B:** 6 word differences
(1751—1833 spacing; „Psykologi. I“ vs „Psykologi, i“; p. 109 „til“ vs „ril“ -- BOTH OCRs read „ril“, the old file
„til“: X109 in extra-b3; Forplantelse; Phænomen,,; Pallas's) and 4 markup (\textsc{Niels Treschow}; „a priori“ (i3);
Pallas (l3), Ceder (m3 extra)) -- all on sheets.
**Sheets (2 controls each):** b3-01..12 (144 = 120 checks + 24 extra; per 12), i3-01..02 (19), l3-01..06 (108 lines;
spaced controls now only words that occur ONCE on their page, pp. 4-98; the repeat-line rule only for l2), m3-01..08 (39:
11 head, 9 rule [5 lines above now: the p. 141/155 rules sit ~4 lines above], 4 note, 2 sc, 7 par, 6 extra [sc of
Treschow p. 99, Howitz p. 141, Heiberg p. 146; p. 99 title line; Ceder; p. 161 „(Den vexlende Affectation.)“]).
Commands: `sheets.py words --tag b3 --per 12 --pages 99-161 --extra extra-b3.tsv`; `sheets.py italic --tag i3 --per 11
--pages 99-161`; `spacedsheets.py --tag l3 --pages 99-161 --per 21`; `miscsheets.py --tag m3 --pages 99-161 --maxh 1800`.
reads.py: a SyntaxError from round 1 fixed (`: d = 'SC'` had slipped into a comment); selftest on a fake b3 file
(.parts/reads/selftest/round2/): 3 of 4 controls, the planted miss caught, the X item listed for the hand.
Superseded sheets in .render/stale/.
**Known gaps for the main session:** letterspacing is cropped only on candidate lines (gap/draft/join): short spaced
words on other lines (Sibbern pp. 122-126 is heavily spaced) are not read -- the page check must cover a Sibbern page.

**RESUME POINT.** Dispatch three blind readers (READER-BRIEF.md):
H: b3-01 … b3-09; I: b3-10 b3-11 b3-12 i3-01 i3-02 l3-01 l3-02 l3-03 l3-04; J: l3-05 l3-06 m3-01 … m3-08.
Then `reads.py --tags b3,i3,l3,m3` (dry) and --write; hand list incl. the 24 X items (patches); m3 answers -> patches
(opener numerals IV/V, headings, notes pp. 110/124/144, sc names); spaced.tsv; rebuild to OPEN 0; last passes; page
check PCRUN=3 (add the stratum in pagecheck.py; include a Sibbern page 122-126); translator's odd spots; OCRDIFF line;
header notes of the old section-IV file into template.tex.

**2026-10-11 (later): ROUND 2 READ AND APPLIED -- pp. 1-161 at OPEN 0.**
Readers H (b3-01..09), I (b3-10..12, i3, l3-01..04), J (l3-05..06, m3): .parts/reads/r-{b3-H,b3-I,i3-I,l3-I,l3-J,m3-J}.tsv.
Controls 55 of 56: the miss l3-05-07 „sp:Skaplynne“ (p. 66 note) is the READER's (J marked only „lunde“); the control is
right (x3 Q11 at 500 dpi). `reads.py --tags b3,i3,l3,m3 --write`: 99 decisions (88 words, 11 italics) + 69 spaced spans.
Overridden by hand (BY HAND round 2 in decisions.tsv): the two lone-„i“ deletions 115|i>, 118|i> (W -> T + PATCH, the
layer's line-initial „i“ after the first word -- with 117|i>, 160|i> four such, all put back by PATCH), 143 „Forstemthed i“
(W would have joined it), 133 doX, 155 til værende / nær —, 153 saaledes; (T + POST), E124 folie (i3 read roman; the note
is italic, x3 Q10). By hand: 37 words, 9 italics; 12 post-state keys T. reads.py fix (round 1's SyntaxError) held.
At the image (main session, zoom.py x3 Q01-Q23, x4 R01-R03, x5 S1-S6 at 500 dpi, x6 U1-U5 at 600 dpi): p. 104 „at“, p. 147
dotless „i“, p. 159 „itl“ PRINTED AS IS, p. 121 „Atttraa“ PRINTED AS IS, p. 114 „Forskerperslonighed“ PRINTED AS IS (both
OCRs read it so: found by a corpus-rarity scan), IV and V without stops PRINTED AS IS, p. 144 note ends with a stop,
p. 127 Menneske-Stamme, p. 128 Misfosterdannelser, p. 124 note „\textit{L'irritation et la folie}“, p. 144 „l'alienation“.
SHARED OCR ERRORS (no check: both OCRs agree) found and mended by POST: p. 109 „til“ (both „ril“; b3-12-14 blind + the
2026-10-03 text), p. 144 „l'alienation“ (both „Valienation“), p. 132 Mumieskikkelse („-keise“), p. 134 „Romer- og“ (the
draft joined the suspended hyphen), p. 136 „unterdrükken“ („-driikken“), pp. 122, 134, 135 „Iøvrigt“ („løvrigt“; POST_ALL);
p. 118 „be-|ængstende“ (the draft's „b eængstende“, --splits). ROUND 1 RESIDUE: p. 88 „\textit{a priori}“ (only „priori“
was italic; x6 U5) -- the only change in pp. 1-98 (5 diff lines).
LETTERSPACING: one-letter words next to a spaced word show no spacing and are left roman (pp. 122, 124, 130: „i \emph{denne}“,
„\emph{denne} i“, „i \emph{dem}“, „i al \emph{Leven}“; the draft's runs had taken them in). Partly spaced words: p. 133
„Hetero\emph{doxe}, Ortho\emph{doxe})“, p. 155 „\emph{til}værende og \emph{nær}værende“. 13 words H read as spaced only in
b3 NOTEs (not on l3 candidate lines: os, har, er, havde x2, deres x2, nu, sig selv, derfor, samme, Sandhed, er) added to
spaced.tsv -- the l3 candidate detector misses short spaced words: the page check covers pp. 122 and 130.
Italics: „a priori“ p. 112, „eo ipso“ x3 (POST_ALL), „natura naturans)“ p. 130, „ex opere fidei operato.“ p. 134, „l'homme
physique“ p. 125 set whole by POST. Punctuation after an italic word as the slant check set it (NOT ESTABLISHED, as round 1).
Third witness (1810 Treschow, 23 X spots): the readers confirm the 1910 draft at all 23 -> Høffding's own changes against the
1810 text (Abstraktion, Tankekraftens, „de første“, Mennesker., „kan man ei derom giøre“, ganske, indsaa, afgjort x3, har,
„høieste og“, allene, / giøre, / derpaa; / tvivlsomt / maa / Værker / kiendeligere / Beskrivelse / „betegne de“ /
„endskiøndt de“ / abstrakte) -- or misprints of 1810; the 1910 print governs.
Final: chain OPEN 0 (words, italics); the collated file itself OPEN 0 (402 disagreements, 357 decided); --unapplied empty;
--splits 2 (p. 28 er barmhiertig; p. 116 „Indadgaaen i sig“, right); words per page vs tesseract pp. 99-161 99.1-102.2 %;
prescreen words 0, lone 0 on pp. 99-161, speck 10 (apostrophes and p. 121 „nær,lade“ as printed), double 1 (pilot),
marks 0; sandbox compile (§5 recipe, Greek as placeholder): 0 errors, 0 missing characters, 133 pp.
OCRDIFF: tesseract (repo tessdata_best, dan) | 207 candidates | 77 corrected | 130 witness's fault | 0 unresolved
(+ 8 shared errors outside the collation; italics 19 runs + 6 by hand; letterspacing 108 lines read + 13 from b3 notes;
third witness 23 spots, 0 corrections; round-1 residue 1, p. 88).
**Page check round 2 -- PREPARED, NOT READ.** pagecheck.py PCRUN=3: strata 99-121 (2), 122-126 (1), 127-161 (1); seed
202610113 -> pp. 104, 115, 122, 130 (two Sibbern pages in the heavily letterspaced stretch); 16 strips on
`.render/udvalgte-stykker-pc3-01..08.png`; selftest PASSED (read-back 0 differences on all four; 4 injected faults found --
no italic on p. 104 to inject). PAGECHECK-BRIEF.md: a Round 2 line.
RESUME POINT: dispatch ONE page-check reader: „Follow ebook-method/udvalgte-stykker/PAGECHECK-BRIEF.md in ~/mnt/danish-texts.
Round 2: sheets pc3-01 … pc3-08, write .parts/pagecheck/reading-3.tsv.“ Then `PCRUN=3 pagecheck.py compare
.../reading-3.tsv`, decide diffs-3.tsv, `PCRUN=3 pagecheck.py rate`; translator's odd spots; header notes (incl. the old
section-IV file's) into template.tex; then BUILD_TO for round 3 (pp. 162 ff.).

**2026-10-11 (last): ROUND 2 DONE -- page check read, translator's odd spots settled. pp. 1-161 at OPEN 0.**
Page check (reading-3.tsv, one blind reader; `PCRUN=3 pagecheck.py compare` + rate; decided rows .parts/pagecheck/run3-diffs.tsv =
diffs-3.tsv): pp. 104, 115, 122, 130, 1389 words, 8 differences: 0 word errors, 0 punctuation (95 % upper 2.16/1000),
3 markup = 2.16/1000 (95 % upper 5.58): letterspacing missed on p. 122 „Ene“, p. 130 „Sjæl“, „af“ in „System af Operationer“
(x7 at 500 dpi) -- all in Sibbern's stretch, as feared (short spaced words off the l3 candidate lines); mended (spaced.tsv,
POST). 5 the reader's/tool's: „i denne“, „i dem“ (a one-letter word shows no spacing: left roman, house convention);
„*natura naturans*)“ -- the reader's „*)“ is read by pagecheck.py as a footnote mark (3 rows; tool artifact). The p. 115
signature (cut at the strip edge) is „8*“ (tesseract „8+“), not transcribed.
Translator's odd spots (19 rows, .parts/pilot/tr-odd.tsv; outcomes .parts/pilot/tr-odd-round2-decided.tsv, crops x8):
3 MENDED (p. 100 paragraph -- m3-07-04 „par yes“ had never been applied; p. 105 „Erfarenhed,“ comma, reader H had read a
stop; p. 129 \emph{Nu}), 3 PRINTED AS IS (p. 138 „undre“, p. 144 „lingende“, p. 159 „ta“), 12 as printed, 1 no fault (p. 142
„være“, a display fault on the translator's side). translation.tex (backup translation.tex.bak.20261011-round2odd): the
p. 100 paragraph, \emph{One} p. 122, \emph{Now} p. 129, \emph{system of operations} and \emph{soul} p. 130, and the
„% print:“ site comments for the 8 PRINTED AS IS misprints of pp. 99-161 (IV, V, Forskerperslonighed, Atttraa, undre,
lingende, itl, ta). tr_check.py: all OK, \opage 161/161, markup per page equal.
LESSON: m3 „par yes/no“ answers are not applied by reads.py (only listed) -- read every one against the build (round 2:
p. 100 missed until the translator saw it; pp. 151, 155 were already paragraphs; the „no“ answers pp. 114, 138, 140 agree).
Final: chain OPEN 0 (words, italics), the collated file OPEN 0 (404 disagreements, 359 decided), --unapplied empty;
sandbox compile of BOTH files (§5 recipe, Greek as placeholder): 0 errors, 0 missing characters, 133 pp. each.

**RESUME POINT -- ROUND 3: pp. 162-221 (VI SØREN KIERKEGAARD p. 162, VII RASMUS NIELSEN p. 199 (and Brøchner), to p. 221;
VIII opens p. 222).**
1. pagemap.BUILD_TO = 221; back up the build file and the scripts (`*.bak.<date>-prebuild221`); rebuild with the chain
   (draft --emit --force && check.py --italics --apply && draft --post); pp. 1-161 must stay identical (diff the TEXT part up to
   „% --- p. 162 ---“ against the backup) and OPEN 0. ocr.py has read all pages with tessdata_best (only 99, 108-113 were rerun).
2. Check OPENERS 162/199 against the layer and the image (round 2: V opened on p. 146, not the Indhold's 147); NOTE_PAGES 194,
   206 (footnotes; ** notes now render **) via template.tex). Kierkegaard: expect Latin/Greek and long letterspaced passages.
3. Edition check before drafting: texts/kierkegaard/ (SKS-based e-texts) and any Nielsen/Brøchner transcriptions in the repo are
   THIRD WITNESSES by script (word diff against the draft, `sheets.py --extra`), never the text: Høffding's redaction governs.
4. Recon <= 3 page images; rules.py; blind sheets b4/i4/l4/m4 (2 controls a sheet; l-controls once on their page); after
   reading: apply m4 par answers BY HAND (reads.py only lists them), scan the build for corpus-rare words (shared OCR errors:
   round 2 found 8), check every lone-„i“ key, a page check PCRUN=4 (add a stratum), the translator's odd spots, OCRDIFF line.

## 2026-10-11: ROUND 3 -- sections VI-VII, pp. 162-221: built, collated, sheets cut (READERS NOT YET DISPATCHED)

**Paragraph-start gap (round 2 lesson) closed.** reads.py now APPLIES the m-sheet `par` answers: a yes/no whose quoted
line begins with the boxed words goes to `ebook-method/udvalgte-stykker/pars.tsv` (page, the build line's first words,
yes|no, id) and `draft.py --post` sets/removes the blank line (before the page marker for a page-top line); everything
else is listed for the hand.  The guard matters: AUDIT of all 33 par answers of rounds 0-2 (r-m1-D, r-m2-F/G, r-m3-J)
against the build: 22 answered at the boxed line and agree; 11 crops had the box on ANOTHER line (miscsheets.find cut the
top 9 % of the page for the running head and so lost the page's first line; the fuzzy match boxed a word lower down) and
the readers answered „no“ for that line -- all 11 are page-top paragraphs; 8 read at the image (crop
.render/udvalgte-stykker-w1-01.png, 250 dpi: all indented), 3 are numbered §§. ONE paragraph was wrong: p. 63 page top
„Sophie. De er dristig“ (a new speaker; the build ran it on; the box words „Sophie. De“ start two lines of the page and
the reader answered for the other). Fixed by pars.tsv; pp. 1-161 otherwise identical (diff: that one blank line).
pars.tsv holds 14 reader answers (reads.py --write) + 14 lines by hand; --post: 1 set (p. 63), 27 already right (a regression guard).
miscsheets.py (m4 on): drops only the running head's own line, keeps the tesseract rows a par item was found on, and
counts page-top paragraphs as draft paragraphs (no more page-top par questions where the draft agrees).

**Build.** pagemap.BUILD_TO = 221; backups `*.bak.20261011-prebuild221` (.parts/, build file in .parts/pilot/).
check.py (shared tool; backup check.py.bak.20261011-slantcache): the slant scores are CACHED per word box
(.parts/collate/slant-214.json) -- the --italics pass over 221 pp. outran the 180 s a device call may take, and a
background process does not survive the call.  draft.py: FLAGS_FROM=162 lists the new round's CHECK flags.
PATCHES (round 3, 9): the § type measure broke p. 162 and p. 214 (Iso-|lering) at lines with capitals; p. 199 § 1 is
intro type (tesseract ascender 36-38 vs 41-42) and was not in intro; p. 189 „C. STADIERNES TEORI (Uvidenskabelig
Efterskrift).“ excerpt head; pp. 206-207 note **) at „Beviser**).“ (layer “)) whose French runs on at the foot of p. 207
(the draft had set it as a smallquote in the text, closed on p. 208) -- moved into the note; p. 170 and p. 179 centred
sub-heads „a.“, „b.“ (the layer ran them into lines).  OPENERS 162 VI, 199 VII, 222 VIII confirmed in the layer.

**Recon (3 images r4-cols, r4-notes, r4-p167-175; plus the m4-05 sheet).**
- pp. 183-184: SKS's two parallel columns („Naar der objektivt/subjektivt spørges om Sandheden ...“) are printed ONE
  after the other, full width, LETTERSPACED, 14 lines, through „Usandheden.“ (then „Lad os tage“ on the same line):
  l4 reads the lines; set the passage whole by POST.
- p. 175 Greek „μετάβασις εἰς ἄλλο γένος.“ (m4 extra; textalpha patch after); pp. 170, 172 the item marks are GREEK
  „α.“ „β.“ (draft a./p.; b4 keys), under centred „a.“ (p. 170) and „b.“ (p. 179).
- p. 206 notes: *) „*Auguste Comte et la philosophie positive.* Paris 1877. S. 539 flgd.“; **) all italic, French with
  accents and œ („l'opinion que l'esprit doit être subordonné au cœur“, „IIme“, „régime“); both OCRs garble the French
  (V for l', æ for œ): the m4 note items (p. 206, and the p. 207 foot as extra) give the readings -> patch the note text.
  In the text „(*l'insurrection moderne de l'esprit contre le cœur*)“ -- X keys.
- p. 194 note *) at „Dagligstue*). As-|sessoren“; p. 165 „Men hvad“ IS a new paragraph (the draft runs on: m4 par);
  p. 208 „Mulighed. — —“ printed dashes (not a rule; b4 key).
- p. 167 „essentia involvit existentiam.“ italic; Lessing's German (pp. 167-168) in text type, letterspaced in part;
  German umlauts: rules.NEVER keeps 168 sprache/wahle (tesseract å = a printed umlaut?) and French accents
  (206 regime, 200 etats) off the accent/layerfault rules.
- Small capitals: „SØREN KIERKEGAARD“ p. 162, „RASMUS NIELSEN“ p. 199, „HANS BRØCHNER“ p. 214 (case keys on b4 -> SC).
- LONE „i“ keys (round-1 lesson: a W deleting it needs the moved word put back): 194 „Grundforvir-ring i den“, 197
  „i samme Grad“, 217 „i dets høieste“ -- after b4, PATCH, never a bare W.  Shared OCR errors found by a corpus-rarity
  scan (vocabulary of all repo transcriptions + SKS): 163 „Tii“, „Beysning“, 169 „ogrigtigt“, 171 „ttil“, 178 „y“, 205
  „lis“ (capital I as l), letterspaced run-ons both OCRs share on pp. 210, 212, 218 („muligudenetValg“,
  „DetUsandsynligemaatroes“, „ofteuklartoghalvbevidst“: l4 lines give the words -> POST).

**Third witnesses** (by script, /tmp, not kept): SKS plaintext (`~/bibliotek/Kierkegaard, Søren/SKS-plaintext/Trykte
skrifter/`: Philosophiske Smuler, Afsluttende uvidenskabelig Efterskrift -- NOTE its plaintext EXPANDS abbreviations: ɔ:,
o. s. v., f. Ex., B., S. -- useless for those), texts/nielsen/philosophiske-grundproblemer (1879), texts/brochner/
det-religioese (1869; its file keeps line-end splits). Spots where layer and tesseract agree but a witness differs (no
abbreviation expansions, no obvious editorial rewording) + the rare words: 81 X keys in `extra-b4.tsv` (Øjeblik/Øieblik
x5, fordøjer, højere, højfornemme: Høffding's j or the print's?; Teori, Refleksion, beskjæftiger ...). The 1910 print
governs; record what the readers find here.  SKS also serves the hand list as a third witness on open checks (never to
override the print).

**Counts.** 60 pp.; words per page vs tesseract (running head dropped, hyphens joined) 99.3-105.4 % (p. 167 105 %:
tesseract runs letterspaced German together; pp. 206+207 together 99 %: the note moved). check.py: 809 disagreements in the
whole build, pp. 162-221 OPEN 241 -> rules.py 94 (punctspace 55, layerfault 16 [-2 French to the image], accent 8 [-2
German], compound 7, quote 5, guillemet 4, mark 2, para 1) and 8 by hand (161 Af fectation key changed by the opener,
207 French span x2, 198 running head, 199 VII.; 189/208 „— —“ withdrawn: printed dashes) -> OPEN 140; italics 30 open runs
(Latin, French). prescreen: lone-i 0 moved at line starts; speck/double reviewed (p. 170 „a. a.“ = the centred head).
--unapplied empty; pp. 1-161 OPEN 0.

**Sheets (2 controls each):** b4-01..19 (140 checks + 81 X = 221; per 12), i4-01..03 (30), l4-01..10 (186 lines, 341
candidate words; spaced controls once on their page), m4-01..05 (26: 11 head [incl. centred a./b.], 7 rule, 3 note, 3 par
[165 Men hvad, 170 α. Skal, 172 β. Begyndelsens], 2 extra [p. 175 Greek; p. 207 foot French]; m-controls: the settled
pilot items minus „i den“, which stands three times on p. 1).  Commands:
    python3 ebook-method/udvalgte-stykker/sheets.py words --tag b4 --per 12 --pages 162-221 --extra extra-b4.tsv
    python3 ebook-method/udvalgte-stykker/sheets.py italic --tag i4 --per 11 --pages 162-221
    python3 ebook-method/udvalgte-stykker/spacedsheets.py --tag l4 --pages 162-221 --per 21
    python3 ebook-method/udvalgte-stykker/miscsheets.py --tag m4 --pages 162-221 --maxh 1800
reads.py selftest (fake m4 file, .parts/reads/selftest/round3/): par answers with a Greek item mark accepted, the planted
control miss caught.  READER-BRIEF: round-3 tags; Greek/French/German letters exactly.

**RESUME POINT.** Dispatch three blind readers (READER-BRIEF.md):
K: b4-01 … b4-12; L: b4-13 … b4-19, i4-01 i4-02 i4-03, l4-01 l4-02 l4-03; M: l4-04 … l4-10, m4-01 … m4-05.
Then `reads.py --tags b4,i4,l4,m4` (dry) and --write (pars.tsv now written and applied); hand list incl. the 81 X items
(patches; SKS as third witness), lone-i keys 194/197/217 by PATCH, the French notes from the m4 readings, Greek p. 175
(textalpha), the pp. 183-184 letterspaced passage and the run-on lines pp. 210/212/218 (POST), small caps (SC), opener
numerals VI/VII; rebuild to OPEN 0; last passes; page check PCRUN=4 (add a stratum: a Kierkegaard page and p. 218);
translator's odd spots; OCRDIFF line.

**2026-10-11 (later): ROUND 3 READ AND APPLIED -- pp. 1-221 at OPEN 0.**
Readers K (b4-01..12), L (b4-13..17, i4, l4-01..03; L SKIPPED b4-18/19 = 17 X spots, read by the main session at
400-800 dpi, v1-02/03: all confirm the draft, incl. „cœur“), M (l4-04..10, m4): .parts/reads/r-{b4-K,b4-L,i4-L,l4-L,l4-M,m4-M}.tsv.
Controls 69 of 70: the miss l4-03-12 „sp:Fichtes“ (p. 93 note) is the READER's -- spaced in note type (v1 B093).
`reads.py --tags b4,i4,l4,m4 --write`: 97 decisions (75 words incl. 6 SC, 22 italics), 178 spaced spans, 3 par answers
(pars.tsv; p. 165 „Men hvad“ set). reads.py misparses a note's leading „*)“ as an italic span: i4-03-02/04 overridden (W).
By hand (decisions.tsv „round 3, after readers“): 60 words (ɔ: x10, α. β., German umlauts spräche/wähle/für/Götze, IIIme,
l'esprit, Phædrus 230 A). moved back, „— —“ x2 printed, signatures „11*“ „12*“ read by tesseract ...), 10 italics;
44 post-state keys T. Crops v1-01..04 (main session, 400-800 dpi): letterspaced word division (18 runs), Tii, ogrigtigt,
ttil, op (all PRINTED AS IS), „socratisk.“ with its quote, IIIme (three I; my recon had read IIme), p. 207 note lines
italic throughout with „á la foi“ (PRINTED AS IS).
PATCHES (6, pre-collation): Greek p. 175; lone-i x3 (194 „Grundforvirring / i den“, 197, 217); p. 194 note „Alt.“; p. 197
„\emph{Qvinden kun er} \emph{Øieblikket}“. POST (~45): misprint marks (Beysning, Tii, ogrigtigt, ttil, op, VI, VII, note **)),
γ. p. 178, „(\textit{l'insurrection ... le cœur})“, note **) set whole from M's reading (m4-04-04 + m4-05-08 + l4 French
lines) and note *) „\textit{Auguste Comte et la philosophie positive.}“, 15 word-division fixes in letterspaced runs
(pp. 164-219, witness word division), half-set italics (essentia involvit existentiam, de omnibus dubitandum x3, a tout
prix, trois états, qvalitates occultæ, in actu, in vino veritas), POST_ALL Iis (p. 205), letterspaced passages pp. 207, 216.
draft.py --post: spaced.tsv gets a LETTERS-ONLY fallback (_spfallback: a span crossing a line-end hyphen, or read with lost
word spaces, is found by its letters, disambiguated by the words before -- 20 letters of them; an \emph met at the edge
is absorbed; a word split between two spans is merged, none before p. 162). template.tex: graphicx +
\DeclareUnicodeCharacter{0254}{\reflectbox{c}} for „ɔ:“; a header note on the round-3 conventions.
Small capitals: SØREN KIERKEGAARD (p. 162), RASMUS NIELSEN (p. 199), HANS BRØCHNER (p. 214). Opener numerals VI, VII stopless.
Third witness (81 X): the print confirms the draft at 76 (Øjeblik x5 with j, beskjæftiger, Teori, Refleksion, hielte,
Duplik, bleven, høiest, bagtefter, qua, maaske, Spekulationen, Passager, fordøjer, højere, højfornemme ... = Høffding's
text), corrections at 4 (γ., Iis, l'insurrection, cœur), misprints at 5 (Beysning, Tii, ogrigtigt, ttil, op).
Final: chain OPEN 0 (words, italics); the collated file itself OPEN 0 (decided 736); --unapplied empty; words per page vs
tesseract pp. 162-221 99.1-105.5 % (pp. 167/210/218 > 103: tesseract runs letterspaced words together; 206+207 100.6 %);
prescreen: lone-i at line starts 1 (p. 218 „det i Sandhed“, read), speck 21 (French apostrophes), double/single/dash/marks
0; pp. 1-161 identical to the prebuild221 backup but for the p. 63 paragraph; sandbox compile (§5 recipe, Greek as
placeholder): 0 errors, 0 missing characters, 178 pp.
OCRDIFF: tesseract (repo tessdata_best, dan) | 233 candidates | 68 corrected | 165 witness's fault | 0 unresolved
(+ 20 shared errors outside the collation: 15 letterspaced word divisions, Greek, γ., Iis, the French of note **) and
p. 206 text; third witness 81 spots: 4 corrected, 5 PRINTED AS IS; italics 30 runs + 10 by hand; letterspacing 186 lines,
178 spans + 2 passages by POST).
**Page check round 3 -- PREPARED, NOT READ.** pagecheck.py PCRUN=4: strata 163-181, 182-184 (Kierkegaard's letterspaced
passage), 185-198, 199-221; seed 202610114 -> pp. 180, 184, 185, 207; 16 strips on .render/udvalgte-stykker-pc4-01..08.png;
selftest PASSED (read-back 0 differences on all four; 4 injected faults found). p. 207's foot is the run-on of note **)
(set at its mark on p. 206): compare lists it -- adjudicate it against the note. PAGECHECK-BRIEF.md: a Round 3 line.
RESUME POINT: dispatch ONE page-check reader: „Follow ebook-method/udvalgte-stykker/PAGECHECK-BRIEF.md in ~/mnt/danish-texts.
Round 3: sheets pc4-01 … pc4-08, write .parts/pagecheck/reading-4.tsv.“ Then `PCRUN=4 pagecheck.py compare
.../reading-4.tsv`, decide diffs-4.tsv, `PCRUN=4 pagecheck.py rate`; translator's odd spots; then BUILD_TO for round 4
(pp. 222 ff., VIII).

**2026-10-11 (last): ROUND 3 DONE -- page check read, translator's odd spots settled. pp. 1-221 at OPEN 0.**
Page check (reading-4.tsv, one blind reader; `PCRUN=4 pagecheck.py compare` + rate; decided rows .parts/pagecheck/run4-diffs.tsv =
diffs-4.tsv): pp. 180, 184, 185, 207, 1355 words, 5 differences, all T: 0 word errors, 0 punctuation, 0 markup (95 % upper
2.21/1000 each). The reader's: p. 185 „netop er Inderlighedens“ marked letterspaced (it is not: v2-01 P185). The tool's: p. 184
the page-final divided word „uende=“; p. 207 the foot = the run-on of note **), set at its mark on p. 206 (word for word the
same: 145 tokens, 0 differences). pagecheck.py fix: a letterspaced run the reader closes and reopens at every line (`Sand_=` /
`_heden`) was parsed into ~90 false differences („Sand__heden“: Python's \w matches _) -- now one run, the divided word joined
(backup .parts/pagecheck.py.bak.20261011-round3). A scrap normalised copy is in .parts/_to_delete/ (no delete permission).
Translator's odd spots (10 rows; outcomes .parts/pilot/tr-odd-round3-decided.tsv; crops v2-01/02): 4 MENDED by POST (p. 196
„Fleertals-Majestæt.“ a stop; p. 200 „Videnskabelige;“ -- the W decision had put „; men“ on a line of its own; p. 217
„\emph{Natur}“ (Na-|tur); p. 220 „\emph{Endeligheds}bestemtheden“ -- one word, only its first part spaced; the l4-10-16 spaced.tsv
entry commented out), 1 PRINTED AS IS (p. 195 „Fortabelse. han“ -- a stop where SKS has a comma; `% print:` in translation.tex),
5 as printed (p. 180 „at hans, ja ... at hans“, p. 181 „aflave“, p. 189 „lader ligegyldig“, p. 191 „Pust“ -- all as SKS; p. 219
„Begrebsprincipatet“). translation.tex (backup translation.tex.bak.20261011-round3odd): \emph{finitude} p. 220 and the p. 195
print comment; the translator had already rendered pp. 196, 200, 217 right. tr_check.py: all OK, \opage 221/221.
Final: chain OPEN 0 (words, italics), the collated file itself OPEN 0 (3 more post-state keys T), sandbox compile of BOTH files
(§5 recipe, Greek as placeholder): 0 errors, 0 missing characters; transcription 178 pp., translation 179 pp.

**RESUME POINT -- ROUND 4: pp. 222-306 = VIII DEN SIDSTE MENNESKEALDER (p. 222: 1. S. Heegaard p. 222; 2. H. Høffding pp. 231,
237; 3. K. Kroman p. 247; 4. Cl. Wilkens pp. 259, 267; 5. A. Lehmann pp. 276, 282; 6. L. Feilberg pp. 288, 295) and the
ANMÆRKNINGER pp. 301-306.**
1. pagemap.BUILD_TO = 306 (the last text page); back up build file and scripts (`*.bak.<date>-prebuild306`); chain; pp. 1-221 must
   stay identical (diff up to „% --- p. 222 ---“) and OPEN 0. OPENERS 222 'VIII.' (the layer reads „VIII“: m5 head decides the
   stop, as IV-VII were stopless), 301 '' (Anmærkninger). NOTE_PAGES 232, 243, 250, 272, 274, 276 (footnotes; check the layer
   for more). ocr.py has read all pages; renders for 222-306 at 300 dpi exist.
2. THE ANMÆRKNINGER (pp. 301-306) NEED SPECIAL CARE: endnotes in SMALL TYPE, NO_INTRO, keyed back to the excerpts by page (and
   line?) references -- recon the layout first (two columns? hanging indents? italic or letterspaced lemmata? „S. 31 L. 4“-style
   references and any reference marks in the excerpts that point to them; the pilot already met one: p. 31 „endelige“ is glossed
   there). Decide the markup before drafting (a description list or one paragraph per note, references kept verbatim, page
   numbers checked against the build), give them their own m5 items (head/extra per note block) and a page-check stratum.
   draft.py's small-type measure will see the whole stretch as note type: make sure it is neither smallquote nor footnote.
3. Third witnesses: Høffding's own texts in texts/hoeffding/ (Gentagelsen? Religionsfilosofi), Kroman (texts/kroman/), Heegaard
   (texts/heegaard/) -- word diff by script (the round-3 method: witdiff, X keys in extra-b5.tsv), the 1910 print governs.
4. Round-3 tools to reuse: reads.py (par answers applied; the „*)“ footnote-mark misparse in i-sheets: fix it), draft.py's
   letters-only spaced fallback, miscsheets (page-top par fix), pagecheck PCRUN=5 (add strata), the vocabulary rarity scan for
   shared OCR errors, the lone-i check, the word-division check for letterspaced runs against a witness.
5. Then the whole book: UDV=all (TEXFILE becomes the tracked transcription.tex -- only with Hans's go-ahead; read the old section-IV
   file's header notes in first), front matter and Indhold already done (template.tex, indhold.texfrag).

## 2026-10-11: ROUND 4 -- section VIII pp. 222-299 + ANMÆRKNINGER pp. 301-306: built, collated, sheets cut (READERS NOT YET DISPATCHED)

**Build.** pagemap.BUILD_TO = 306; backups `*.bak.20261011-prebuild306` (.parts/: scripts, decisions, spaced, pars, template,
extra-b4, indhold, READER-BRIEF, check.py, checks.tsv, this file; build file in .parts/pilot/). Chain unchanged. pp. 1-221: body
identical to the prebuild306 backup (diff of the text up to „% --- p. 222 ---“: 0 lines), still OPEN 0 (every open check and
italic run is on pp. >= 222). NOTE_PAGES += 253 (layer „♦)“; draft.STAR and rules.NOTE_PAGES too): 7 footnotes in VIII (232, 243,
250, 253, 272, 274, 276), all placed. p. 300 is BLANK (render grey 199-234, tesseract nothing): `\opage{300}` + comment (PATCH).
check.py --italics: the 214-dpi renders of pp. 222-306 were missing (prerender outran the call); made by a loop (pdftoppm per page).
**Recon (3 images, .render/recon/r5-p222, r5-p301a, r5-p288).** p. 222 „VIII“ printed WITHOUT a stop (as IV-VII; T now, m5 head,
then a POST PRINTED AS IS mark); § 1 in small caps „SOFUS HEEGAARD“. p. 288: Feilberg's § has NO numeral („L. FEILBERG (f. 1849)“).
p. 301: the ANMÆRKNINGER are ONE RUN-ON PARAGRAPH: entries „— **P. 6,** *Physica coelestis*, ...“ -- page references in BOLD (comma
bold too), lemmata in ITALICS, „ɔ:“, an equals sign („*a priori* = uafhængigt“, the layer reads „—“). Markup decided: one paragraph
(pagemap.ONEPAR = 301-306: draft.py sets no paragraph or rule there except after the title), references verbatim, \textbf on every
„P. N,“/„Pag. N,“ that opens the run or follows a dash (draft.py --post, idempotent: 79 set; references inside a note -- „se P. 11“,
„Note til P. 164“ -- stay roman), NO_INTRO, no smallquote/footnote (normal size, as the Indledning: Hans's decision).
**INDHOLD vs the headings (editorial stance: both readings recorded; the Indhold stays as printed in indhold.texfrag):**
(1) author numbers: Indhold „1. S. HEEGAARD … 6. L. FEILBERG“; the §§ print „1. Sofus Heegaard“ (p. 222), „2. Harald Høffding“
(p. 231), „2. Kristian Kroman“ (p. 247: a second 2.), „3. Claudius Wilkens“ (p. 259), „4. Alfred Lehmann“ (p. 276), Feilberg (p. 288)
unnumbered -- layer and tesseract agree; m5 sc/head items read them. (2) Wilkens a. „Det Skønne og Kunsten“: Indhold 259, heading
on p. 260 (§ 3 on p. 259). (3) Lehmann a.: Indhold „vaomotoriske“ (PRINTED AS IS, round 0), heading „VASOMOTORISKE“ (p. 276).
All other VIII pages agree (222, 231, 237, 247, 267, 282, 288, 295; ANMÆRKNINGER 301).
**PATCHES (round 4, 24):** p. 301 layer braces „{ 1 642—1 727)“, „Bayle{\QAl“, p. 303 „P. \ Ab ^“, p. 306 „P. 22\,“ -> tesseract's
readings (checked on the anm strips); p. 231 § 2 into intro + \textsc{Harald Høffding} (draft.py had set \textsc{Erfaring});
\textsc on the § names Kroman, Wilkens, Lehmann, Feilberg; p. 276 and p. 282 headings with their second line / source; p. 274 note
(„Menneskene*).“, note „… S. 607 ff. og 693 ff.“; the layer had „nesken.e* )“); pp. 250-251 a false smallquote removed (tesseract
ascenders 41 on every line; the last p. 250 line took note type from the footnote); LONE-i x6 (pp. 240, 243, 246, 252, 289 „I Kraft“,
298) put back by tesseract's word order (never a bare W). The verse p. 265 (Richardt) IS small type (ascenders 30): smallquote kept.
**Collation.** OPEN 266 words (pp. 222-299: 180, pp. 301-306: 86) after rules.py 127 (punctspace 39, layerfault 26, quote 26,
accent 18, guillemet 10, mark 7, para 1, compound 1; NEVER += 304 Rotscher>Røtscher -- Rötscher? to the image) and 6 by hand
(222 VIII. T; 276/282 two-line headings T; 288 Leve-ABC W (r5-p288); the ANMÆRKNINGER heading and the witness's p. 306 head T).
Italics OPEN 148: 24 on pp. 222-299 (Høffding's own excerpts emphasise by ITALICS), 124 on pp. 301-306 (the lemmata) -- NOT on
i5: the anm strips read every italic. p. 225: the layer reads lower-case „i“ as „I“ throughout (17 case keys on b5: case is never
settled by rule). WORDS PER PAGE vs tesseract (head dropped, hyphens joined): pp. 222-299 99.0-103.6 % (p. 261 103.6: tesseract runs
letterspaced words together), pp. 301-306 99.6-100.3 % -- no missing text. prescreen: lone-i 0 moved on pp. 222-306 after the
patches, double 1 (p. 291 „osv. osv.“), single 1 (p. 256 „m i t“, letterspaced, on b5/l5), marks 2 („^“ in Clovis^, ærgre^ -- open
checks, decided by b5).
**Third witness:** texts/hoeffding/religionsfilosofi (3rd ed. 1924; Høffding revised verbs ere>er, kunne>kan, havt>haft, so only
spots that could be misreadings) for Høffding b. pp. 237-246; psykologi (1882 1st ed.) differs from the 1905 text of a. -- no use;
Heegaard's Om Intolerance, Kroman's Tænke- og Sjælelære, Wilkens, Lehmann, Feilberg are not in the repo. Corpus-rarity scan
(vocabulary of all repo transcriptions + pp. 1-221) for shared OCR errors. -> 22 X keys in `extra-b5.tsv` (Følelsesog -- the draft's
suspended-hyphen join „Følelses-|og“, round-1 lesson --, psykiske, billed-og, „er dem“, Værdiernes, „den anden“, „kunne fremtræde“,
„betragtes irreligiøst“, ud-|udvortes (tesseract „ud- udvortes“: a doubling in the print?), „den nyeste“, „som ufær-“, „den Fordel“,
Vedvaren/„Ved varen“, noges, Blilede, „den ævnede“ (tesseract no word), mér, æsthetisk-|intellektuelle, Millieuet, smlign, lagttagelses-
fejl (capital I), odsl.). Rare words in the Anmærkninger (for the hand, against the anm readings): SimonideSy, „søber“, Ideeı/Ideer,
„omsluttedes at sin“ (at for af? seen on m5-13), Theodice, Troschows (for Treschows?), Wolfenbiittel (ü), statigt, Qyodlilet, Vef,
Häckels (tesseract Håckels), Inimanens-, Sfygmanomefer, Lundhoff's, Aet./Se. (tesseract Act./Sc.), Rotscher/Rötscher.
**ANMÆRKNINGER REFERENCES checked against the build (script; lemma's first word on page N):** all fit except (a) „P. 36, De smukke
Videnskaber“ -- the text is on p. **31** (with „Endelig eller nødvendig Umulighed“, also p. 31; the sequence runs P. 30, P. 36, P. 33,
P. 36 Swift): both OCRs read „36“ -- misprint or shared misreading, the anm strip decides; (b) „P. 286, Kardiograf … Tibialis“ -- the
words are on p. **281** (Kardiografens, Tibialispulsen); the next entry „P. 286, — indrømmes“ fits p. 286; (c) „P. 236, Ved Sætningen
om Værdiens Bestaaen“ -- „Bestaaen“ stands on pp. 237, 239 („Værdiernes Bestaaen“, X239). Record each as PRINTED AS IS with a
% print: comment if the image confirms the number. (Trendelenburg „Pag. 171“ fits: the text spells „Trendlenburg“, as SKS.)
**Sheets (2 controls each):** b5-01..24 (266 checks + 22 X; per 12; b5-16..23 hold the 86 Anmærkninger checks), i5-01..03 (24,
pp. 222-299), l5-01..11 (200 lines, 267 candidate words; spaced controls now from pp. 4-221, once on their page: the pp. 4-98 pool ran
dry), m5-01..21 (100 items: 12 head, 6 sc, 7 note, 7 rule, 15 par, 4 extra [p. 231 rule above § 2?, p. 250 type change?, p. 265 verse,
p. 276 „Metoden.“], 49 ANM STRIPS on m5-13..21: every line of pp. 301-306 (39+52+52+52+52+34 lines, 6 a strip, full width, 0.72 of
300 dpi; the running head and signature dropped; anm strips on sheets of their own; no par items on pp. 300-306)).
Commands:
    python3 ebook-method/udvalgte-stykker/sheets.py words --tag b5 --per 12 --pages 222-306 --extra extra-b5.tsv
    python3 ebook-method/udvalgte-stykker/sheets.py italic --tag i5 --per 11 --pages 222-299   # --pages now also limits the checks
    python3 ebook-method/udvalgte-stykker/spacedsheets.py --tag l5 --pages 222-299 --per 21
    python3 ebook-method/udvalgte-stykker/miscsheets.py --tag m5 --pages 222-306 --maxh 1800    # 'anm' strips (ANM_N = 6)
reads.py: the „*)“ footnote-mark misparse in i-sheets fixed (a mark at a line start or after a space is stripped before the italic
spans are read); 'anm' answers go to the hand list. Selftest (.parts/reads/selftest/round4/: fake m5/i5): planted control miss caught,
„*) Se min *Afhandling*“ parsed right, anm listed. READER-BRIEF: round-4 tags, ɔ:, =, bold <b>..</b>, the `anm` kind (¶ for an indent).
Independence: the b5 Anmærkninger crops (reader O) and the anm strips (P, Q) go to different readers.

**RESUME POINT.** Dispatch FOUR blind readers (READER-BRIEF.md):
N: b5-01 … b5-14; O: b5-15 … b5-24, i5-01 i5-02 i5-03, m5-01 m5-02 m5-03; P: l5-01 … l5-11, m5-13 m5-14 m5-15;
Q: m5-04 … m5-12, m5-16 … m5-21.
Then `reads.py --tags b5,i5,l5,m5` (dry) and --write; hand list incl. the 22 X items; THE ANM STRIPS: diff every strip's reading
word by word against the build (letters, punctuation, bold, italics) -- a script, the strips are the Anmærkninger's second full
reading -- and settle each difference at the image (the 124 anm italic runs and the 79 bold references included); the three
reference anomalies above; „VIII“ PRINTED AS IS; the Indhold discrepancies into template.tex's header; m5 par answers (pars.tsv);
spaced.tsv; rebuild to OPEN 0; last passes (--moved, --splits, --unapplied, prescreen, rarity scan, lone-i, suspended-hyphen joins
„-og“); page check PCRUN=5 (add strata: a Kroman page, a Feilberg page, an Anmærkninger page); translator's odd spots; OCRDIFF line;
then the whole book: UDV=all only with Hans's go-ahead.

**2026-10-12: ROUND 4 READ AND APPLIED -- pp. 1-306 (the whole book) at OPEN 0.**
Readers N (b5-01..14), O (b5-15..24, i5, m5-01..03), P (l5, m5-13..15), Q (m5-04..12, m5-16..21): .parts/reads/r-{b5,i5,l5,m5}-*.tsv.
Controls 118 of 118. `reads.py --tags b5,i5,l5,m5 --write`: 193 decisions (105 W, 85 T, 3 SC), 153 spaced spans, 13 par answers (one,
„(Richardt).“ no, removed: the line after \end{smallquote}). By hand (decisions.tsv „by hand round 4“): ~70 words, 16 ɔ:, 14 italics,
37 post-state T; overrides of reads.py W's that took tesseract's spacing/quotes (sige :, v.", Re fleksibilitet, Vej", „--“).
NEW TOOL `ebook-method/udvalgte-stykker/anmdiff.py` (rerunnable: `python3 … anmdiff.py [--italics [--write]]`): the 49 anm strips
(every line of pp. 301-306) word by word with punctuation, bold, italics against the build. First run (pre-post build) 170
differences, nearly all italics/bold; --italics decided 110 open italic runs from the strips (14 by hand). Real errors found and
mended: „\textit{i vor Tid}“ p. 303 (the layer read the italic i as „/“, draft.py dropped it as a speck), „Kierkegaard.“, Wolfenbüttel,
bold „P. 16,“ after a stop without dash (draft.py's bold rule extended), ~30 lemma italics (POST), Tyndall/Morgan/Chubb. Misprints
PRINTED AS IS: p. 304 high opening quote “Systemet, p. 305 „Snbjektivitet“. Final: 4 differences = 3 strip-reader errors checked at
the image (Q's Götze: print Gøtze; Subjektiv: Subjektivt; principipia: princi-|pia) + the first-line indent.
At the image (zoom.py u5-01/02 at 500 dpi, u6-01 at 600 dpi, main session): Væxt.“ (italic), A/B italic p. 248, p. d. a. S. (N's „e“
wrong), [ɔ: p. 263, For-|skjel, ex-|akte, Br.. rr.., Tids-og (no space), Vedvaren (one word), længer (N's „længere“ wrong),
erkendelsesteoreti-|ske / psykologi-|ske spaced, „svare til“ spaced, „paa disse“/„og“ not, „være os bevidst“ and Udtryksbevægelse
spaced whole, the note p. 272 „størst“ (Q's „største“ wrong), p. 276 note ends with a worn stop, „Enten—Eller“ unspaced,
\textsc{Fr. Nietzsche} p. 232 note. O's „short dashes“ before P. N are worn long dashes, not a sort of their own (---); „P.209,“ and
„P.218,“ set tight, as printed. Reference anomalies (P. 36 for p. 31, P. 286 Kardiograf for p. 281, P. 236 for pp. 237/239): the
strips confirm the printed numbers -- as printed (record a % print: comment in the translation).
X items (22): the print confirms the draft at 15 (Høffding's 1910 text against Religionsfilosofi 1924: psykiske, billed-og, er dem,
Værdiernes, den anden, kunne, irreligiøst, den nyeste, som ufær-, den Fordel; mér, smlign, odsl., „den æv-|nede“, æsthetisk-|);
mended 3 (Følelses- og, Iagttagelsesfejl, \emph{Vedvaren}); PRINTED AS IS 4 (Blilede, noges, Millieuet, ud-|udvortes).
Other shared errors mended by POST: p. 255 „Sansnings\emph{muligheder}“, p. 256 „\emph{mit}“, p. 228 Omraade, p. 261 Dvælen
(--splits), p. 261 „Verdensopfattelse i den“ (the layer moved „den“), p. 255 „sten“ (page turn), p. 265 verse line breaks.
Final: chain OPEN 0 (words, italics) for pp. 1-306; the collated file itself OPEN 0; --unapplied empty; --splits only the settled
old ones + p. 261 „den begærfri“ (right); words per page vs tesseract (head dropped, hyphens joined) pp. 222-299 99.4-103.0 %,
pp. 301-306 99.6-100.3 %; prescreen in VIII: lone 0, single 0, marks 0, double 1 (p. 291 „osv. osv.“, as printed); sandbox compile
(§5 recipe, Greek as placeholder): 0 errors, 0 missing characters, 245 pp.
OCRDIFF: tesseract (repo tessdata_best, dan) | 396 candidates | 154 corrected | 242 witness's fault | 0 unresolved
(+ ~16 shared errors outside the collation, 4 X misprints PRINTED AS IS; italics 148 runs (24 i5, 124 from the anm strips) + ~30 by
POST; letterspacing 200 lines read; Anmærkninger read whole twice (OCR collation + strips), 0 open differences.)
**Page check round 4 -- PREPARED, NOT READ.** pagecheck.py PCRUN=5: strata 222-240, 241-259, 260-278, 279-299, 301-306 (p. 300
blank excluded); seed 202610115 -> pp. 232, 252, 269, 294, 306; 20 strips on .render/udvalgte-stykker-pc5-01..10.png; selftest PASSED
(read-back 0 differences on all five; 5 injected faults found). PAGECHECK-BRIEF.md: a Round 4 line (bold not compared).
RESUME POINT: dispatch ONE page-check reader: „Follow ebook-method/udvalgte-stykker/PAGECHECK-BRIEF.md in ~/mnt/danish-texts.
Round 4: sheets pc5-01 … pc5-10, write .parts/pagecheck/reading-5.tsv.“ Then `PCRUN=5 pagecheck.py compare .../reading-5.tsv`,
decide diffs-5.tsv, `PCRUN=5 pagecheck.py rate`; translator's odd spots; the Indhold discrepancies and round-4 notes into
template.tex's header; then the whole book: UDV=all only with Hans's go-ahead.

## 2026-10-12: ROUND 4 CLOSED -- THE WHOLE BOOK INSTALLED

**Page check round 4 (pc5):** reading-5.tsv, pp. 232, 252, 269, 294, 306, 1660 words, 7 differences (run5-diffs.tsv = diffs-5.tsv):
0 word, 0 punctuation (95 % upper 1.80/1000), 3 markup = 1.81/1000 (95 % upper 4.67): p. 232 note title „\textit{Søren Kierkegaard som
Filosof}“ (only two words were set), p. 294 „\emph{Eks.}“ -- and at the image all four „Eks. 1./2.“ pp. 289-294 are letterspaced (u8;
POST_ALL); 4 the reader's/tool's (p. 252 Hypotese not spaced, p. 306 „bl. Andet“, two line-end divisions written „x =“). The p. 306
running head is printed „ANMÆRKMINGER“ (u7 P05): running heads are not transcribed; recorded at \opage{306} and in the header.
**Translators' odd spots r4 (tr-odd-r4a/b, 25 rows; crops u7 C01-C18, u8):** MENDED 9: p. 223 \emph{dersom} only, p. 230 \emph{er},
p. 256 \emph{Duplicisme} whole, p. 257 \emph{Jeg}opfattelse, p. 260 „i et \emph{Viljesforhold}“, p. 267 \emph{Lysten ved Forskjel,
Forandring}, pp. 293/297 „el. l.“ (letter l). PRINTED AS IS 8: Ævret, „den den“ p. 261, „Kunstens Verdens“ p. 264, delt p. 281, „at sin“
p. 301, Tyndall, Troschows, Qvodlilet. AS PRINTED 6: uberegnelig p. 257 (translation now „incalculable“), Tids-og, Forelementerne,
Modtrykkets, „Sansebilledet B … A“ p. 248, „mod“ p. 301; numbering pp. 247/259 (as printed; header + translation comment).
MISREFERENCES kept with „% print:“ in both files: „P. 36“ (p. 31), „P. 286, Kardiograf“ (p. 281), „P. 236“ (p. 239).
**Translation:** tr/pp222-264 and tr/pp265-306 spliced after p. 221 (backup .parts/pilot/translation.tex.bak.20261012-prer4splice); the
round-4 close changes carried over; Wilkens harmonised across p. 265 (the real-beautiful / the art-beautiful; glossary updated);
tr_check.py all OK, \opage 306/306. Fragments renamed .texfrag (.parts/pilot/tr/); no stray .tex fragment under the book directory.
**INSTALLED:** pagemap.py `UDV=build` now writes the TRACKED texts/hoeffding/udvalgte-stykker/transcription.tex (TEXFILE =
'transcription.tex'); the chain (draft --emit --force && check.py --italics --apply && draft --post) rebuilds it, header from template.tex
(now with the whole-book ACCURACY statement, page checks, Indhold discrepancies, misprint log). translation.tex = .parts/pilot/translation.tex
(backup translation.tex.bak.20261012-prewhole; the old section-IV transcription is transcription.tex.bak.20261011-prepilot). The tracked
file's text is identical to the .parts/pilot build (0 diff lines below „% ===== TEXT“); OPEN 0, --unapplied empty. Sandbox compile: transcription
0 errors, 0 missing, 245 pp.; translation 0 errors, 0 missing, 247 pp. ACCURACY-LEDGER row and catalog.yaml (one section „Complete work“,
status complete, Transcription/Translation/Scan links; validate-catalog.py: 0 problems) updated. No note.md (none created).
**Left for Hans:** read and commit; publish with `~/hhalvors.github.io/publish-danish.sh "Udvalgte Stykker: whole book"`.

## 2026-10-12: Virkelighed in the Kierkegaard excerpts
Hans decided: the noun is `actuality` throughout pp. 162-198 (5 sites: pp. 172, 179, 180, 193, 194), adverb `actually` where it plays against Mulighed (pp. 190 x2, 194 note), `really` for plain intensifiers (pp. 193, 198). Translator's note at p. 172 via the new `\trnote` macro (translation preamble; marked T, outside the footnote counter so the print's notes keep their marks). Backup translation.tex.bak.20261012-virkelighed. Glossary in TRANSLATOR-BRIEF.md updated. Sandbox compile 247 pp., 0 errors.

## 2026-10-12: Anstød in the Smuler excerpt
Hans decided: Anstød = `shock` (pp. 163 x2, 164), støde an = `strike against` (p. 165), with a translator's note (\trnote) at the first occurrence, p. 163. Backup translation.tex.bak.20261012-anstod. Glossary updated.

## 2026-10-26: paragraph-initial long dashes (the mindre-arbejder-3 check, TRANSCRIPTION-PLAYBOOK lesson 13)
Every paragraph-initial `---` read at the scan (ink test + crops): 5 moved back to the end of the line before (the print has them there).  The cases are in
ebook-method/udvalgte-stykker/dashfix.tsv and are applied to transcription.tex by
    python3 ebook-method/collate/dashfix.py udvalgte-stykker --write
which must be run AFTER any rebuild of the transcription (append it to the rebuild line above).  The English mended to
match (the same dashes moved / paragraphs joined in translation.tex).
