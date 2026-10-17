# ebook-method/ — the scripts and the readings behind the e-book-method transcriptions

The Danish transcriptions of these books were made by the **e-book method**
(TRANSCRIPTION-PLAYBOOK.md §00, point 0): no one typed the text. A script aligns
the text of a modern e-book of the same edition with the text layer of the scan,
letter by letter, takes every page turn from the scan, and lists every place the
two disagree. Each listed place was looked at in a crop of the scan, and the
reading of the print was written down in `decisions.tsv` (or, for edits that are
not a single word, `patches.tsv`). The print governs; misprints are kept.

So each folder here holds the complete, rerunnable record of one transcription:

| file | what it is |
|---|---|
| `build.py` | aligns, classifies, applies the decisions, writes `texts/hoeffding/<book>/transcription.tex` |
| `template.tex` | the transcription's header comment, preamble, front matter (and any hand-read pages) |
| `decisions.tsv` | one line per disagreement: key, the reading at the image (`E` = the e-book stands), note |
| `patches.tsv` | edits that are not a single word (an omission in the e-book, a subscript, a `% PRINTED AS IS`) |
| `sheets.py` | crops the scan for every disagreement not yet in `decisions.tsv` (`--todo`) |
| `pagemap.py` | printed page -> PDF page of the scan |
| `pagemarks-en.py`, `anchors-en.txt` | the page numbers in the English translation (see below) |

Folders: `filosofiske-problemer/` (1902), `danske-filosoffer/` (1909),
`erkendelsesteori-livsopfattelse/` (1925, pp. 63-123 only; its `out.texfrag` was
spliced into the transcription by hand, and its translation markers were applied
from `anchors-en.txt` with a script that was not kept -- use another folder's
`pagemarks-en.py` as the model), `religionsfilosofi/` (only `notes-check.py`,
the 2026-10-02 check of the Noter), `vort-hjem/` (1903; no e-book: `check.py`
collates the existing transcription against the layer, letter-wise and with
`--words` word-wise with punctuation; the layer's word order is scrambled and the
pages skewed and curved, so it rebuilds reading order from the word boxes after a
skew+curvature fit; `--italics` finds italic words by stroke slant; `--mark` sets
the exact `\opage` markers; `pagemarks-en.py` is the short form for a text whose
sections and paragraphs match the translation one to one).

`humane-ethik/` (1876; 2026-10-05): no e-book, two scans of two copies.  draft.py (Google's layer), check.py against
tesseract on the KB copy, rules.py (KB's own layer as third witness), sheets.py + reads.py (BLIND crop reading),
notesheets.py + notescmp.py (every footnote read in full), spacedsheets.py + spaced.tsv (letterspacing).  New check.py
settings it introduced: SPACING 'strict', QUOTES 'strict', WMARKS True, and the option --unapplied.

`mindre-arbejder/` (1899; started 2026-10-05): no e-book; the draft is Danish Wikisource's page-by-page "Valideret"
text (wikisource.py caches it; draft.py expands its templates and keeps the print where Wikisource silently corrected
a misprint), collated against the KB scan's layer by collate/check.py, with tesseract on the KB images as third
witness (ocr.py, rules.py).  Wikisource is not diplomatic (lower-cased nouns, at/af ...): every word is collated.

`om-aandsdannelse/` (Nielsen, 1877; 2026-10-06): the den-store-humor pipeline on a KB antiqua scan with no notes --
draft.py (KB layer; pagemap NO_NOTES, INDENT_MAX), ocr.py (tesseract witness), rules.py (Humor's note rules switched off;
'guillemet' and 'layerfault' added), sheets.py + reads.py (blind crops, from humane-ethik), spacedsheets.py + spaced.tsv
(letterspacing, applied by draft.py --post), patches.py (PATCHES and POST).  First book outside texts/hoeffding/:
pagemap.py `AUTHOR` sets the folder for collate/check.py, sheets.py and pagemarks.py.

`udvalgte-stykker/` (Høffding ed., 1910, antiqua anthology, 306 pp.; whole-book pipeline set up 2026-10-11, pilot pp. 1-44):
om-aandsdannelse's pipeline on Internet Archive's ABBYY layer.  pagemap `UDV=pilot|all|A-B` picks the pages and
`TEXFILE` the output (the pilot goes to .parts/pilot/; collate/check.py honours TEXFILE).  draft.py adds: running heads
by HEAD regex, section openers (\anthsection), excerpt headings in capitals (\excerpthead), Høffding's small-type
introductions by layer box height (\begin{intro}), \textsc for the § head names, letterspaced words the layer gives as
single letters joined and divided by corpus word frequency, short rules found in the render (\sectionrule), footnotes only
on NOTE_PAGES.  Blind sheets: sheets.py words/italic (two seeded controls a sheet), spacedsheets.py, miscsheets.py
(structure), reads.py (b/i/l/m kinds, controls scored), READER-BRIEF.md; zoom.py (tight high-dpi crops for the main
session), prescreen.py (words per page, misplaced one-letter words, specks, doubles), pagecheck.py + PAGECHECK-BRIEF.md
(sampled page check, from speculative-logik, with a selftest).

`speculative-logik/` (Nielsen, 1841-42, Fraktur; 2026-10-07): the martensens-oplysninger pipeline with a fourth reading
(frak2021), book-specific rules (tokens, vote34, consensus, IJ, pair, WNORM), sfix.py (layer s = ø), crops.py (blind
sheets, union boxes, controls, AUDIT of rule decisions; audit.py scores them), readsbox2.py, structsheets.py (notes,
marks, headings, front matter), emphsheets.py (bold by stroke width, spacing), sweep2.py, lint.py, and finish.py.

`skjaebne-og-forsyn/` (Nielsen, 1853, Fraktur; set up 2026-10-07): speculative-logik's pipeline on a Google Books scan
(BL copy, 600 ppi, Google's OCR layer).  draft.py adds mathematik-og-dialektik's long-s mapping; rules.py unchanged (its
fault lists were counted on KB's layer: audit before trusting).  Google's layer gave 13 disagreements a page against
tesseract, KB's ABBYY layer on speculative-logik 46.  finish.py not yet written.

`brandes-universitetsfilosofien/` (Rubow, Danske Studier 1928, 18 pp. antiqua, footnotes several to a line; 2026-10-09):
a NEW route for short texts.  The text of record is a BLIND whole-page reading by two Sonnet readers
(pagecheck.py sheets + PAGECHECK-BRIEF.md: paragraphs, centred lines, small-type quotations, footnotes as NOTE lines,
marks as ^n, italics *x*), and vote.py checks every reader word against the ABBYY layer AND tesseract: a word stands
when either machine agrees, the rest are cropped; it also lists words both machines have that the readers lack.
vote-fixes.tsv holds the corrections; fromreads.py writes transcription.tex (template.tex for header and preamble;
MISPRINTS and POST inside).  draft.py / check.py / pagereads.py from om-aandsdannelse were run as a cross-check only
(draft.py now writes .parts/draft-from-layer.tex, never the transcription).  Rebuild: `vote.py && fromreads.py --write`.

`staerkeres-ret/` (Nielsen, 1863, Fraktur; 2026-10-08): skjaebne-og-forsyn's pipeline on a 13-page Google Books scan
(BL copy), finished by a FULL blind page check (pagecheck.py, every page) instead of a sample; adjcrops.py crops the
page check's differences; finish.py is new (drop capital, a dash, the rule on p. 14, PRINTED AS IS marks).  Rebuild:
`draft.py --emit --force && ../collate/check.py staerkeres-ret --witness ocr --apply && oepass.py --apply && finish.py --apply`.

`begrebet-noiagtighed/` (Nielsen, 1860, Fraktur with formulas; 2026-10-10): the staerkeres-ret pipeline as machine witness
(draft.py, ocr.py, check.py, rules.py, vote.py), then the brandes route: the blind page reading (pagecheck.py, six readers)
is the text of record, voted word by word (vote2.py) against layer, tesseract and the collated draft; cropsv.py (blind crops
with controls), lines.py + formcmp.py (second blind reading of every formula/Greek line), spot.py (600-dpi line crops),
turned.py (turned-sort misprints only tesseract keeps), finalcheck.py (the finished text against both machines), mkfix.py
-> vote-fixes.tsv, fromreads.py -> transcription.tex.  Rebuild: `fromreads.py --write`; translation `tr_build.py --write`.

`propaedeutik-1868/` (Nielsen, 1868, Fraktur, Google layer; 2026-10-13): a Cursus volume made of earlier books' sheets.
map1868.py (content), concord.py (page for page), setting.py (same setting? line ends of two layers), changes.py
(three-way word diff on the shared pages), concordance.py -> concordance.tsv (SAME / PART / NEW for every PDF page).
Only the NEW pages are transcribed: staerkeres-ret's pipeline (draft.py, ocr.py x3 models, rules.py, crops.py with
controls + rule audit, readsbox.py, oepass.py, pagecheck.py for EVERY page, adjcrops.py) with page keys that are not
consecutive (pagemap.PAGES; ocr.py and pagecheck.py read that list); patches.py takes GL II's transcription as the draft
where the 1868 page is GL II's type (Greek, an interleaved note); finish.py adds HEADS, POST, PARAS/JOINS (paragraphs
from the page reader), ANTIQUA, EMPH, BOLD.  Rebuild: `draft.py --emit --force && ../collate/check.py propaedeutik-1868
--witness ocr --apply && oepass.py --apply && finish.py --apply`.  Translation hand-made (GLOSSARY.md).

`logik-og-psychologie-1871/` (Nielsen, 1871, 8 pp., Fraktur, NO layer; 2026-10-13): scharling-apologie's pipeline (ocr.py
MODEL=layer/deu_latf/dan, rules.py, batchsheets.py + readsbox.py, oepass.py) with `LAYER_PDFS` (the KB PDF holds another
book too), NO_NOTES, staerkeres-ret's pagecheck.py for a FULL blind page reading (line boxes from the tesseract layer;
title page as p. 0), and a new finish.py (HEADS, POST, ANTIQUA, EMPH, MISPRINTS, each find exactly once).  Rebuild:
`draft.py --emit --force && ../collate/check.py logik-og-psychologie-1871 --witness ocr --apply && oepass.py --apply &&
finish.py --apply`.  Translation hand-made in the main session (GLOSSARY.md).

`erindringer/` (Høffding, 1928; 2026-10-07): the den-store-humor pipeline on the Slægtsforskernes Bibliotek scan (ABBYY
layer) with the Lindhardt og Ringhof e-book of the same text as a third reading: draft.py (layer; old-style folios;
white lines from line gaps, `WHITE_GAP`), ocr.py (tesseract witness), rules.py (etik's e-book vote), sheets.py + reads.py
(blind crops, controls.tsv), ebookdiff.py -> qsheets.py -> qresolve.py -> efix.py (every difference between the
finished text and the e-book read at the image; efix.tsv), pagepass.py + pagepass.tsv (89 pages read whole), and
patches.POST (where the 41 pages read on 23 Sep 2026 govern).  Rebuild:
`draft.py --emit --force && ../collate/check.py erindringer --apply && efix.py && draft.py --post` (from the repo root,
with `ebook-method/erindringer/` prefixed).

`tydskland-efter-hegel/` (Høffding, 1872; pilot pp. 1-16 on 2026-10-09): the humane-ethik pipeline on an Internet Archive
Google scan whose layer is the Archive's ABBYY OCR (abbyy_scan.py binds TIFFs + ABBYY into the PDF).  draft.py (humane-ethik's,
+ ABBYY TeX-special rules), ocr.py + rules.py (om-aandsdannelse's), sheets.py (erindringer's, controls from rule decisions),
reads.py, pagediff.py (a whole-page reading vs transcription and tesseract), patches.PAGESET (pages set whole), sweep.py
(unattested words), spaced.tsv.  Rebuild: `draft.py --emit --force && PILOT=1 ../collate/check.py tydskland-efter-hegel --apply
&& PILOT=1 draft.py --post`.

`psykologiske-undersoegelser/` (Høffding, 1889; transcription and translation built 2026-10-09): danske-filosoffer's build.py on a
Google scan of an Academy volume (Stanford copy) with the Lindhardt og Ringhof e-book of the same text.  Changed: the
body/footnote split is by baseline PITCH (notes 10-12 pt, body 13-16), because Google's tight word boxes make type
size unreadable from box height; SIG matches the series line „Vidensk. Selsk. Skr.“ only.  Letterspacing is measured
from box WIDTH (per-character widths fitted by least squares; calibration in the book's RESUME-NOTES); the stacked
formulas are patches.  Rebuild: `build.py --emit`; `sheets.py --todo` crops anything undecided.  Needs numpy (the width fit) as well as Pillow.
Translation: tydskland-efter-hegel's tools (GLOSSARY.md, TRANSLATOR-BRIEF.md, tr_parts.py, tr_template.tex); rebuild
the English with `tr_parts.py build --write`.

`betingelserne-villie/` (Nielsen, 1874, antiqua, 83 pp.; transcription and translation 2026-10-12): om-aandsdannelse's pipeline
(draft.py on Google's layer, ocr.py, rules.py with book rules grounded in its own crops) + udvalgte-stykker's sheets.py /
reads.py / pagecheck.py (blind crops with controls, sampled page check); diff84.py (word diff against the 1884 resetting's
ABBYY layer, a FINDING aid only) and zoom.py (main-session line crops; zoom84-items.tsv records the 113 spots read).
Translation: four translators (GLOSSARY.md, TRANSLATOR-BRIEF.md, tr_extract.py, tr_build.py, tr_template.tex, parts in tr/).
Rebuild: `draft.py --emit --force && ../collate/check.py betingelserne-villie --italics --apply && draft.py --post`
(prefix `ebook-method/betingelserne-villie/`); translation `tr_build.py --write`.

`phantasiens-magt/` (Nielsen, 1876, antiqua, 91 pp.; transcription and translation 2026-10-12): betingelserne-villie's
pipeline on a KB scan (ABBYY layer) of a pencil-marked copy; rules.py gains candidate rules measured on a blind pilot
(`candrule`, ON list); sheets.py gains --keys/--skip; prescreen.py (from speculative-logik).  Sweeps after OPEN 0 (run from the
book directory): splitsweep.py, linecheck.py, parcheck.py, unknown.py.  Rebuild:
`draft.py --emit --force && ../collate/check.py phantasiens-magt --italics --apply && draft.py --post`
(prefix `ebook-method/phantasiens-magt/`); translation `tr_build.py --write`.

`gamle-nye-profeter/` (Nielsen, 1878, antiqua, 112 pp.; transcription and translation 2026-10-12): phantasiens-magt's
pipeline (rules re-measured on a blind pilot) + LAYER_SPLITS, a V-for-backslash map in draft.py, spacedwidth.py
(letterspacing candidates by box width), six translators.  Rebuild:
`draft.py --emit --force && ../collate/check.py gamle-nye-profeter --italics --apply && draft.py --post`
(prefix `ebook-method/gamle-nye-profeter/`); translation `tr_build.py --write`.

`liv-og-haab/` (Nielsen, 1875, antiqua, 103 pp.; transcription and translation 2026-10-12): gamle-nye-profeter's pipeline
on a Google scan (600 ppi bitonal, Google layer) + abbyy.py (the Internet Archive's ABBYY OCR of the same scan, a third
reading that only narrows rules), spacedlines.py (letterspacing by the gap measure), a guard in reads.py (marks the draft
lacks), six translators.  Rebuild:
`draft.py --emit --force && ../collate/check.py liv-og-haab --italics --apply && draft.py --post`
(prefix `ebook-method/liv-og-haab/`); translation `tr_build.py --write`.

`om-samfundets-vilkaar/` (Nielsen, 1877, antiqua, 103 pp.; transcription and translation 2026-10-12): liv-og-haab's
pipeline on a Google/Harvard scan + page-end hyphens taken from tesseract (draft.py), `rules.py --classify` (a pilot
sampled by candidate rule), three footnotes moved to their marks by POST.  Rebuild:
`draft.py --emit --force && ../collate/check.py om-samfundets-vilkaar --italics --apply && ../collate/check.py
om-samfundets-vilkaar --apply && draft.py --post` (prefix `ebook-method/om-samfundets-vilkaar/`); translation
`tr_build.py --write`.

`folkelige-foredrag/` (Nielsen, 1875, antiqua, 164 pp.; transcription and translation 2026-10-12/13): om-samfundets-vilkaar's
pipeline on a MICROFILM with two book pages a frame.  `split.py` derives `.parts/split.pdf` (each frame cut at its gutter,
MediaBox = CropBox = one half) and pagemap.scan_path() returns it, so nothing else changes; `pagemap.PMAP` maps printed
pages from the layer's folios (the film repeats pp. 130-131).  The layer is the Internet Archive's ABBYY (no third
reading); rules.py adds caret, bang, layerfault3, joinW, aposW, splitW; letterspacing candidates by width (spacedwidth.py
-> spacedlines.py); `heads.py` cuts the structure reader's crops.  Rebuild: split.py once, then
`draft.py --emit --force && ../collate/check.py folkelige-foredrag --italics --apply && ../collate/check.py
folkelige-foredrag --apply && draft.py --post` (prefix `ebook-method/folkelige-foredrag/`); translation `tr_build.py --write`.

`for-idee-1869/` (Nielsen, five essays in *For Ide og Virkelighed*, Aargang 1869, 189 pp. antiqua; transcriptions and
translations 2026-10-13): folkelige-foredrag's pipeline for SEVERAL WORKS IN ONE VOLUME -- pagemap.RANGES/ESSAYS, a combined
working file (pagemap.TEXFILE, `.parts/combined.tex`), one collation, `split5.py` cutting the five transcription.tex files,
patches.NOTES (notes moved to their marks by draft.py --post), tr_extract.py/tr_build.py over five essays; pagemap.OWN keeps
the cut files out of the attesting vocabulary (check.py, rules.py, sweeps).  Rebuild: `sh ebook-method/for-idee-1869/rebuild.sh`.

`for-idee-1870-73/` (Nielsen, eight essays in *For Idee og Virkelighed* 1870-1873, SIX volumes, 231 pp. antiqua; 2026-10-13/14,
done): Nasjonalbiblioteket scans with NO text layer.  `nbalto.py` fetches NB's ALTO for
the pages; `combine.py` binds the 231 pages of the six volumes into ONE working PDF (.parts/scan.pdf) with the ALTO laid over
as invisible text (etik/nb_scan.py's method), so draft.py and check.py run unchanged; pages are VIRTUAL (V = 1000 x Bind +
page: the volumes' page numbers collide).  `ocr.py` (tesseract dan witness; renders by pdfimages).  `calibrate.py`: the same
pipeline with FIV_CAL=1 on Et Synspunkt for Darwinismen (same volume, already page-read) scores every candidate rule
against a known text by script, before any pilot.  rules.py --pilot-on: dry run of the calibrated candidates.  Then: blind crops (sheets.py, reads.py, zoom.py), letterspacing
(spaced.py), structure and notes (structsheets.py, notecmp.py), the sampled page check (pagecheck.py); `rebuild.sh` runs the
whole pipeline and `split7.py` writes the seven transcription.tex files (Aandsvirkelighed: one file, two parts).  Translation:
GLOSSARY.md, TRANSLATOR-BRIEF.md, `tr_extract.py` (15 parts), `tr_build.py --write` (checks the parts, writes the seven
translation.tex files from tr_template.tex and the fragments in tr/).

`moderne-filosoffer/` (Høffding, *Moderne Filosofer*, 1904, X + 157 pp.; transcription and translation 2026-10-14):
erindringer's pipeline on an Internet Archive Google scan (Google's layer, betingelserne-villie's settings) with the SAGA
e-book of the same 1904 text as the third witness (rules.py: etik's vote + dash/mark/spacing/label votes; the seam rule
OFF -- it settled digits blind).  draft.py: running heads to `% running head:` comments, endnote marks placed by NOTEPAGES,
lone > < to guillemets (they break check.py's keys) except MATHPAGES.  sheets.py/reads.py (blind crops, 2 controls a
sheet), ebookdiff.py + ebextra.py/xresolve.py, parcmp.py (paragraph starts vs the e-book), emarks.py (e-book italics ->
italics.tsv; its underline spans proved NOT letterspacing), spacecmp.py + lsheets.py (letterspacing measured, Noter only),
frontsheets.py (front matter read whole), pagecheck.py (sampled page check), then draft.py --post (POST, efix, pagepass.tsv,
italics*.tsv, spaced.tsv, Iagttag rule, small capitals, last.tsv).  Rebuild: `sh ebook-method/moderne-filosoffer/rebuild.sh`.
Translation: GLOSSARY.md, TRANSLATOR-BRIEF.md, `tr_parts.py` (6 parts; `build --write` checks marks/paragraphs per page).

`oplevelse-og-tydning/` (Høffding, *Oplevelse og Tydning*, 1918, 238 pp.; transcription and translation 2026-10-14):
a Nasjonalbiblioteket scan with NO text layer, the SAGA e-book of the 1918 text as a third, voting witness.  `nbalto.py` +
`nb_scan.py` (etik's method; each line set on its words' MEDIAN bottom, so a two-line initial does not merge two lines)
build the working PDF with NB's ALTO as an invisible layer (~/bibliotek, SCANS.tsv); `ocr.py` (tesseract witness).
draft.py (etik's, with footnotes): star marks *) **) and daggers, notes grouped by their hanging indent (12 pt).
pagemap.NOTE_SPACE asks check.py for a space either side of a note moved to the page foot.  rules.py was scored by
script on Etik's decided checks first (OOT_CAL).  Then sheets.py/reads.py (blind crops, 2 controls a sheet, `--extra`
spots), notesheets.py/notereads.py/notefix.py (the footnotes read whole -> postfix.tsv), notecmp.py (141 notes = the
e-book's 141), ebookdiff.py, pagecheck.py, wordcrop.py (a few words at 600 dpi), then draft.py --post (patches.POST,
postfix.tsv).  Rebuild: `sh ebook-method/oplevelse-og-tydning/rebuild.sh` (draft --emit, check --apply ONCE, draft --post).
Translation: GLOSSARY.md, TRANSLATOR-BRIEF.md, `tr_parts.py` (9 parts; `build --write`); the translators' odd spots
(tr/odd-*.tsv) went back to the image as extra-b3.tsv.

`rydberg-anmeldelse-1882/` (Høffding's review of Viktor Rydberg, *Ude og Hjemme* 5, Nr. 224, 15 January 1882, pp. 196-197;
transcription and translation 2026-10-17): a small self-contained pipeline for two printed pages in two columns.
fetch.sh (two JP2 leaves and the Archive's hOCR), pagemap.py (REGIONS: head, columns, note as pixel boxes), readings.py
(our tesseract per region + the hOCR aligned line by line -> .parts/lines.tsv), sheets.py (every line as a crop, read in
the main session), reads.tsv (the lines as printed where they differ from the draft), build.py (transcription.tex),
extract.py (the bibliotek extract with the hOCR as text layer), tr/RY.texfrag + tr_build.py (translation.tex, with checks).

`kort-oversigt/` (Høffding, *Kort Oversigt over den nyere Filosofis Historie*, 4th ed. 1910, 95 pp.; transcription and
translation 2026-10-17): religioese-tanketyper's pipeline on an NB scan with no layer; the SAGA e-book is a LATER edition
and votes only where it agrees with an OCR; rules2.py (e-book capitals → small capitals, NB å for a, ü).  st1.py/st2.py
(structure, one question per crop), q3.py (the quote sheet), oddlines.py (the printed line behind any transcription line,
for main-session reading), pagecheck.py.  draft.py keeps a first line that ends in a hyphen (HEADSKIP/HEADKEEP in its
log).  Rebuild: `sh ebook-method/kort-oversigt/rebuild.sh`.  Translation: GLOSSARY.md (+ the big book's, bound in full),
TRANSLATOR-BRIEF.md, `tr_parts.py` (6 parts cut at chapter heads by anchor; `build --write`).

`religioese-tanketyper/` (Høffding, *Religiøse Tanketyper*, 1927, 165 pp.; transcription and translation 2026-10-17):
oplevelse-og-tydning's pipeline on an NB scan with no layer (nb_scan.py fetch/build/notes/italics; draft.py with notes whose
FIRST line is indented, notes only on the pages nb_scan.py notes lists; ~ and « mapped to „), tesseract witness (ocr.py),
the SAGA e-book voting (rules.py).  b1.py: blind crops of open checks, e-book differences, an audit of rule/hand decisions
(collate/check.py now writes `.parts/collate/checks-all.tsv`, every check with its box) and LINE crops for emphasis;
st1.py: structure and the notes read whole, with a question per crop (S1-READER-BRIEF.md); pagecheck.py; oddcrops.py
(the translators' odd spots as 400-dpi line crops, read in the main session).  Pp. 27-28 are missing from the scan: set
from the e-book by patches.INSERT (pp27-28-ebook.texfrag), flagged.  Rebuild: `sh ebook-method/religioese-tanketyper/rebuild.sh`.
Translation: GLOSSARY.md, TRANSLATOR-BRIEF.md, `tr_parts.py` (7 parts; `build --write`).

`engelske-philosophi/` (Høffding, *Den engelske Philosophi i vor Tid*, 1874, [IV] + 190 pp.; transcription and translation
2026-10-15): tydskland-efter-hegel's pipeline on two Internet Archive copies of the one edition.  The Toronto copy (the
Archive's own PDF, its layer = ABBYY) is the draft and the working scan; tesseract on its images is check.py's witness
(WITNESS 'ocr'); the Oxford copy (Google's scan bound with its ABBYY by abbyy_scan.py) is read twice, by its layer and by
tesseract (`oxocr.py`), and votes: rules.py umn-*, `vote2.py` ox2-* (both Oxford readings), `oxsweep.py` (both Oxford
readings agree against an unopened word).  draft.py clusters lines by their MEAN centre (descenders made false centred
heads); post steps for daggers/thin spaces, nouns with a capital Ø (both ABBYY layers set ø) and NOTEFIX.  rules.py adds
qdir/qspace (the print closes quotations both ways), thinspace, oe/oe-dash (oefix list + OE_BOOK), markplaced.  Then
sheets.py/reads.py (blind crops, 2 controls a sheet, a rule audit mixed in), notesheets.py + NOTE-READER-BRIEF.md (notes
read whole -> notes-read.txt -> patches.NOTESET), spacedsheets.py (letterspacing by gaps) and widthsheets.py (by word
width against per-character widths fitted over the book), frontsheets.py, pagecheck.py, b3fixes.py/spotcrops.py (the
translators' odd spots read blind -> patches.POST2/POSTMIS).  Rebuild: `sh ebook-method/engelske-philosophi/rebuild.sh`
(draft --emit --force, check --apply, draft --post).  Translation: GLOSSARY.md, TRANSLATOR-BRIEF.md, `tr_parts.py` (8
parts; `build --write` joins parts with no blank line where the Danish has none).

`tilskueren-1886-90/` (Høffding's four pieces in *Tilskueren*: *Om Religionsfrihed*, 1886, and his three contributions to the
Nietzsche debate with Brandes, *Demokratisk Radikalisme*, *Gensvar*, *Epilog*, 1889-90; 76 pp.; 2026-10-15, HOEFFDING-QUEUE #2):
for-idee-1870-73's virtual pages (V = 1000 x Aargang + page) with engelske-philosophi's ABBYY-draft method.  `ia_extract.py`
fetches single JP2 leaves out of the Archive's _jp2.zip (no 1.3 GB download) and binds per-volume extracts with the ABBYY
layer (~/bibliotek, SCANS.tsv); `combine.py` binds the working PDF.  Witnesses: tesseract (ocr.py) for check.py, Project
Runeberg's OCR of the same Google images (`runeberg.py`) as a guarded voter in rules.py (it never makes a non-word: it
shares faults with ABBYY), henrikpontoppidan.dk's e-texts as a finding aid only (`pontoppidan.py`, `mkextra.py` X-pp).
Blind crops (sheets.py/reads.py, `triage.py` sorts the by-hand list), `zoom.py` (main-session zooms), notes read whole
(notesheets.py, `noteset.py` with figure labels), structure (`structsheets.py`), LETTERSPACING MEASURED, not read:
`spacemeasure.py` (white runs between letters in tesseract's boxes, bimodal, 5 px) -> `spaceapply.py` (after the
collation, letters-only matching, SPACEFIX) -- `spacing.py`/`l2sheets.py`/`spacecmp.py` record the two blind line rounds
that were too inconsistent to use; `pagecheck.py` (6 pp.); `split.py` + `template-piece.tex` write the four
transcription.tex files.  Rebuild: `sh ebook-method/tilskueren-1886-90/rebuild.sh`.  Translation (Om Religionsfrihed
only): GLOSSARY.md, TRANSLATOR-BRIEF.md, `tr_parts.py` (2 parts, `build --write`), tr_template.tex.


`hoeffding-1875-76/` (Høffding's four pieces of 1875-76: *Herbert Spencers Filosofi*, the review of Wilkens's *Erkendelsens
Problem*, *Montaignes Betydning i Etikens Historie* (Det nittende Aarhundrede) and *Benedikt Spinoza* (Nær og Fjern, Fraktur);
~17,100 words; 2026-10-15, HOEFFDING-QUEUE #3): tilskueren-1886-90's virtual pages, with the ROLES SWAPPED: the Archive's
Scribe scans carry only a tesseract layer, measured worse than ours, so `layer.py` lays OUR tesseract (ocr.py, .parts/collate/
best/) over the working PDF as the draft and writes the Archive's OCR as check.py's witness.  `ia_extract.py` (hOCR over the
JP2 leaves; the Harvard copy's ABBYY kept beside the extracts), `combine.py` (Nær og Fjern: one virtual page per COLUMN, cut
by MediaBox/CropBox, pagemap.COLS), `rules.py` (+ the Archive's å-for-a and long-s faults; Harvard ABBYY votes, never on
figures), `vote2.py` (Harvard votes by word alignment), `sheets.py --audit`/`reads.py` (blind crops, audit of rule/vote
decisions), `notesheets.py` + `noteset.py`, `structsheets.py` (title pages, heads, endings, verse, and the measured
letterspacing runs judged at the image -> `spaced-final.tsv`), `PROOF-BRIEF.md` + `proofapply.py` (Fraktur columns
proofread whole; `proof-fixes.tsv`; `final-fixes.tsv` applied with --final after `quotes.py`, the „...“ class rule),
`specksweep.py` (marks the Harvard copy lacks mid-sentence), `pagecheck.py` (3 pp.), `split.py` + `template-piece.tex`.
Rebuild: `sh ebook-method/hoeffding-1875-76/rebuild.sh`.  Translation: GLOSSARY.md, TRANSLATOR-BRIEF.md, `tr_parts.py build
SLUG --write` (6 parts in tr/).

`hoeffding-1879-82/` (Høffding's three pieces of 1879-82: *Filosofien i Sverig* (Nordisk tidskrift 1879, pp. 30-73), *Om
Pessimismen* (Vor Ungdom 1879, pp. 69-90) and the review of Martensen's *Jacob Böhme* (Ude og Hjemme 1882, Nr. 238,
pp. 365-366, two columns); ~28,100 words; 2026-10-15, HOEFFDING-QUEUE #4): hoeffding-1875-76's virtual pages and roles.
`extract.py` builds the extracts from NB's IIIF images + ALTO and from single Archive JP2 leaves + hOCR (SCANS.tsv);
`measure.py` chose the draft (our tesseract; dan+swe for Nordisk tidskrift, which sets Danish ö beside ø and quotes
Swedish); `layer.py` swaps the roles (NB's ALTO / the Archive's tesseract = witness); `runeberg.py` = a third reading of
the SAME NB images -- its votes (rules.py harv-*, vote2.py) were WITHDRAWN after the audit (5 of 30 wrong); `rules.py`
umlaut-R/R2 (ALTO drops umlauts and reads ö as b/d), alto-ae, alto-q; pagemap FAULT_OFF (new hook in collate/check.py)
keeps check.py from settling ø/o as a glyph fault; `umlautsweep.py`, `sweep.py`, `specksweep.py`; blind crops
(`sheets.py`, `reads.py`, `handreads.py` for the reads to decide by hand); `noteplace.py` sets every footnote from the
reading at its mark (patches.NOTEMARKS) and drops the draft's notes; Ude og Hjemme proofread whole (`prooftext.py`,
PROOF-BRIEF.md, `proofapply.py`); `quotes.py` (Nordisk ”...”, Vor Ungdom „...“); `split.py` + `template-piece.tex`.
Rebuild: `sh ebook-method/hoeffding-1879-82/rebuild.sh`.  Translation (Om Pessimismen and the review only): GLOSSARY.md,
TRANSLATOR-BRIEF.md, `tr_parts.py build SLUG --write`.

`mindre-arbejder-2/` (Høffding, *Mindre Arbejder. Anden Række*, 1905, 237 pp., 17 pieces of 1891-1905, incl. the Analogi
essay pp. 33-46 = HOEFFDING-QUEUE #5; ~75,500 words; 2026-10-15/16, #11): ONE book.  Scan: IA mindrearbejder01hfgoog
(Google/NYPL bitonal TIFFs bound with the Archive ABBYY by tydskland-efter-hegel/abbyy_scan.py); `measure.py`/`layer.py`
made our tesseract the layer, ABBYY the witness.  `draft.py`: running heads by key phrase + folio (pagemap HEAD/HEADT),
skew-fitted margins, indent runs; `rules.py` caret/witfault/witfreq/witjunk/l-I; COMPACT blind crop sheets (`sheets.py`,
3 columns, ~46 crops, 2 controls a sheet) with an audit sample of every rule and voter class (`items.py`, `reads.py`);
edge sweep for the cut gutter margin (`edgesweep.py`, `marginsweep.py`, `edgeadj.py`); damaged pages found by tesseract's
confidence on line-edge words and proofread whole (`pageproof.py`, `proofapply.py`); `noteplace.py`, `structure.py`,
`itapply.py`, `parapply.py`, `joinsweep.py`; and, after the translation, the translators' odd spots sent back to the image
(`oddsheets.py`, ODD-BRIEF.md) and applied last (`oddapply.py`, odd-fixes.tsv).  Rebuild: `sh
ebook-method/mindre-arbejder-2/rebuild.sh`.  Translation: GLOSSARY.md (terms anchored on Høffding's own English, St Louis 1904
and Mind 1905), TRANSLATOR-BRIEF.md, parts in tr/, `tr_parts.py build mindre-arbejder-2 --write`.

`etiske-undersoegelser/` (Høffding, *Etiske Undersøgelser*, 1891, [VI] + 83 pp., three treatises, ~22,650 words; 2026-10-16,
HOEFFDING-QUEUE #6): mindre-arbejder-2's pipeline on a clean Google scan (IA etiskeundersgel00hfgoog, Wisconsin; the item has
JP2s only: converted losslessly to G4 TIFF, then abbyy_scan.py build).  `layer.py` keeps a form that holds the page IMAGE (the
copied one stripped every form and blanked the scan).  `damage.py` (low-confidence edge words per side, gutter white: no damage
here); `strokesweep.py` (ø / umlaut forms 10x rarer than the stroked form); `manualdec.py` (hand decisions by CROP id, keys
never retyped); `roundtwo.py` (z whole-line crops, l letterspacing sample, n note pages, s structure pages); `noteplace.py`
(notes from the readers' reading, placed at their MARK words; patches.NOTECUT / NOTEREAD / NOTEMARKS) with `notesdiff.py`
(reading against the collated draft); `spaceapply.py` after the collation (runs merged across line-end hyphens); `pagecheck.py`
stratified by damage (page lists from damage.tsv).  Translation: GLOSSARY.md (anchored on IJE 1890 and The Monist 1891, and on
the *Etik* translation), four parts in tr/, `tr_parts.py build etiske-undersoegelser --write` (tr/front.texfrag = the
Preface).  The translators' odd spots were read in 600 ppi line crops and mended in fixes1.tsv / patches.MISPRINTS.  Rebuild:
`sh ebook-method/etiske-undersoegelser/rebuild.sh`.

## What a run needs (not in this repo)

- the scan, found by `pagemap.py` under `~/bibliotek/Høffding, Harald/` (SCANS.tsv
  gives its sha256);
- the e-book (`*.epub`, privately owned, git-ignored) in `texts/hoeffding/<book>/`;
- `pdftotext` / `pdftoppm` (poppler), Python 3 with Pillow.

Scratch output (alignment lists, crop sheets) goes to the book's `.parts/` and
`.render/`, which are git-ignored.

## Rebuilding a transcription

    python3 ebook-method/<book>/build.py            # align; report anything undecided
    python3 ebook-method/<book>/build.py --emit     # also write transcription.tex

`--emit` refuses while a disagreement is undecided. If the repo's other
transcriptions have changed since the last run, a rerun can list a few new ones
(the rules consult the words attested elsewhere in the repo): crop them with
`python3 ebook-method/<book>/sheets.py --todo`, look at the sheets in
`texts/hoeffding/<book>/.render/`, and add a line per case to `decisions.tsv`.
On 2026-10-02 the moved scripts rebuilt `filosofiske-problemer` and
`danske-filosoffer` byte for byte.

Backups (`BAKDIR` in a book's `pagemap.py`) belong in
`os.path.join(tempfile.gettempdir(), '<book>-bak')`, not a fixed `/tmp/...` path: a
`/tmp` folder made by one sandbox session is not writable by the next, and
`check.py --apply` then dies after `draft.py --emit` has already overwritten
`transcription.tex` (mindre-arbejder-2, 2026-10-16; rerun the whole chain once the
path is fixed).  Still fixed paths: etiske-undersoegelser, hoeffding-1875-76,
hoeffding-1879-82, tilskueren-1886-90.  Before a rebuild meant to change one
thing, copy `transcription.tex` aside and `diff` afterwards: the diff should be
that one thing.

## Page numbers in the translation

    python3 ebook-method/<book>/pagemarks-en.py --turns   # Danish/English windows -> .parts/turns-en.md
    python3 ebook-method/<book>/pagemarks-en.py --apply   # insert \opage{N} before each anchor

`anchors-en.txt` has one line per printed page, `N|first words of the English for
page N`, copied verbatim from the translation. `--apply` checks that every anchor
occurs exactly once and that the pages run in order. Run it on a translation that
has no markers yet (set `TRANSLATION=<path>` to try it on a copy).

## Checking an existing transcription: `collate/check.py`

For a transcription that already exists (no e-book needed). It compares the transcription word by
word, punctuation included, with an independent reading of the scan -- the scan's text layer, or a
fresh tesseract OCR -- and lists what must be decided at the image.

    python3 ebook-method/collate/check.py BOOK                summary + open checks (.parts/collate/checks.tsv)
    python3 ebook-method/collate/check.py BOOK --sheets       crops of the open checks, witness word boxed in red
    python3 ebook-method/collate/check.py BOOK --italics      italics by stroke slant vs the transcription's \emph
    python3 ebook-method/collate/check.py BOOK --pages        how far each page marker is from the true page turn
    python3 ebook-method/collate/check.py BOOK --apply        apply the W / P / =text decisions (backup first)
    python3 ebook-method/collate/check.py BOOK --mark         markers at the exact turns: dry run; add --write
    python3 ebook-method/collate/check.py BOOK --witness ocr  tesseract instead of the layer

Settings live in `ebook-method/BOOK/pagemap.py` (page range, scan path, and optionally FIRST_FROM /
LAST_UPTO where the essay shares its first or last page with another text, HEAD / FOOT for unusual page
furniture, WITNESS, LANG); decisions in `ebook-method/BOOK/decisions.tsv`, one line per key as the
tool prints it: `T` (transcription right), `W` (witness right), `P` (misprint: take it, mark PRINTED AS
IS), `=text`, `?`.  The docstring at the top of the script has the details.

How it works, so that its silences can be judged:
- Witness lines are rebuilt from the word boxes (skew and page curvature fitted), because a layer's
  content-stream order can be scrambled; running heads, folios and signature marks are dropped.
- Footnotes are moved, in the transcription's stream, to the foot of their page, where the witness reads
  them, so no type-size measurement is needed.
- A difference is settled by rule only if it is a known glyph confusion AND the transcription's word is
  attested in the corpus's other transcriptions AND the witness's word is not (so „til“/„fil“, „Bud“/„Hud“,
  „det“/„dét“ go to the image); also: the same words dropped and added nearby (witness line order), and
  stray marks.  Case-only and one-letter differences are never settled by rule.
- Italics: each witness word's image is sheared; italic strokes line up better slanted (score ≥ 1.07 on
  the books calibrated so far; the run prints the score distribution).  Letterspacing is not detected.
- **The witness must be independent of the transcription's source.**  If a transcription was made from
  the scan's own text layer (RESUME-NOTES say so), errors it copied are invisible against that layer: use
  `--witness ocr`.
- OCR needs tesseract with the Danish (and, for French texts, French) models: on a Mac
  `brew install tesseract tesseract-lang`; elsewhere set TESSDATA_PREFIX to a folder holding
  dan.traineddata (tessdata_best).  About 8 s a page; results are cached in `.parts/collate/ocr/`.
Witness quirks met so far (handled): line-end soft hyphens (U+00AD) in KB layers; pencil letters in a
column beside the text (dropped when a wide gap cuts them off the line); tesseract's French model gives
words with apostrophes very low confidence (so only short low-confidence tokens are dropped); tesseract
splits a running head into fragments (so OCR words are re-clustered into lines like layer words).
Running heads with lowercase words need a HEAD pattern in pagemap.py (see the Hoeffding pagemaps).
Tested on Vort Hjem (2026-10-03): with the layer it reproduces the hand-built check of 2026-10-02
(all readings decided, italics none open, 10 of 10 markers exact, `--mark` a no-op); with OCR it also
puts all 10 markers exact, at about 2.5 crops a page.

## Page numbers in a translation: `collate/pagemarks.py`

    python3 ebook-method/collate/pagemarks.py BOOK --turns    -> ebook-method/BOOK/turns-en.txt
    (write ebook-method/BOOK/anchors-en.txt: "N|English words where page N begins", verbatim)
    python3 ebook-method/collate/pagemarks.py BOOK --apply    -> \opage{N} in translation.tex (backup first)

The Danish markers must be exact first (`check.py BOOK --pages`). Paragraphs of both texts are aligned by
length (Gale-Church); for each page turn the tool prints the Danish words around it and the English
passage at the same relative point, so that the anchor can be picked by reading a few lines, not the book.
Turns at the head of a one-to-one paragraph are answered automatically. `--apply` refuses an anchor that
occurs more or less than once, or out of page order. Done this way 2026-10-03: Realisme, Religion og
Videnskab, Religionsfilosofiens Opgave, Udvalgte Stykker, Pascal og Kierkegaard (117 turns); then Kants
Udvikling, Relation som Kategori and Den menneskelige Tanke (552). An anchor that recurs takes `@k` (its k-th
occurrence). Heading blocks are skipped: their page turn goes to the first text under them.

Two limits (2026-10-03, Den nyere Filosofis Historie): it reads arabic page numbers only, so roman
front-matter pages (XI-XV) are placed by hand; and when the print sets its notes as endnotes but the
English has them as footnotes, the endnote pages fall out of order -- mark them by hand inside the
footnotes that carry those notes, and list them as comments in anchors-en.txt.

## Is the English still right? `collate/xcheck.py`

    python3 ebook-method/collate/xcheck.py --all --measure          one line per book (sources: collate/xcheck-sources.tsv)
    python3 ebook-method/collate/xcheck.py BOOK --review            -> .parts/xcheck/BOOK/review.txt
    python3 ebook-method/collate/xcheck.py BOOK --apply FIXES.txt [--write]

A translation is only as good as the Danish it was made from. When that Danish was an e-book, or an
earlier state of transcription.tex, every place where it differs from the present transcription of the
print is a place where the English may be wrong. `xcheck-sources.tsv` records, per book, what the English
was made from: a git commit (found by diffing the English prose of successive commits) or an .epub
(relative paths start at the repo root, so `../bibliotek/...` is the library beside it). The tool compares
that source with transcription.tex word by word, ignoring what cannot matter to a translator (case, aa/å,
é, x/ks, the e-books' modern verb forms opstaar/er/kan), and sorts the rest into wording, markup (italics)
and punctuation; footnotes are compared as their own stream, and e-book endnotes are set against the
print's endnote section when the print has no footnotes. `--review` prints each difference with the
English from the same printed page, at the same relative point (between the `\opage` markers), so a
decision takes one reading. `--apply` takes "old|new" lines and refuses any old string that does not
occur exactly once; `--write` keeps a backup. Den menneskelige Tanke was repaired this way 2026-10-03
(89 wording fixes, see TRANSLATION-PLAYBOOK.md §6a); its 288 wording differences are all in the tool's
list, which is how the tool was checked. A count of 0 for a book with a git source means only that the
transcription has not changed since the English was last revised, not that the English is right.

When the transcription covers only a SELECTION of the e-book, give the source as
`PATH.epub::FILE-REGEX[::NOTES=first-last]` -- the e-book files to keep and the range of its endnotes --
or the whole book is compared against the selection (Den nyere Filosofis Historie:
`...Den_nyere_filosofis_historie.epub::s004-|s015-::NOTES=218-236`). Roman page markers (`\opage{XI}`)
are pages like any other. When the English has no `\opage` markers, `--review`'s English window is
not the right place; grep the English for the Danish context instead.

## Starting a new book

Copy the folder of the nearest model -- `filosofiske-problemer/` for endnotes,
`danske-filosoffer/` for footnotes at the page foot -- set the book's page map,
e-book file names and front matter, start an empty `decisions.tsv`, and follow
TRANSCRIPTION-PLAYBOOK.md §00.

**A book with no e-book and no earlier transcription** (model:
`spinozas-liv-og-laere/`, 2026-10-03): `draft.py --emit` builds a draft
transcription.tex from the scan's text layer by rule (lines rebuilt from the word
boxes, hyphens joined, paragraphs from indents, footnotes from their smaller line
pitch, exact page markers, "% CHECK" at every guess); `pagemap.py` sets
`WITNESS = 'ocr'`, so `collate/check.py BOOK` collates the draft against an
independent tesseract reading, never against the layer it was made from. On the
device, tesseract must run single-threaded in parallel (`OMP_THREAD_LIMIT=1`,
four workers) and in calls under the time limit: a background job does not
survive the call.
Rebuild with `draft.py --emit --force && collate/check.py BOOK --apply` (chained: a failed patch
leaves the file unwritten). `check.py BOOK --moved` and `--splits` list the two kinds of rule-settled
disagreement that can hide a real error (a word out of place; a space the witness lacks): read them.
Second model, `den-store-humor/` (2026-10-04): three steps, `draft.py --emit --force &&
collate/check.py BOOK --italics --apply && draft.py --post`; the last applies `patches.POST`,
corrections written against the collated text (the footnotes, read at the image, and specks), since
check.py rewrites words and italics after the draft patches. `collate/spaced.py` (letterspacing by
letter gaps in the tesseract boxes) is EXPERIMENTAL: noisy on bitonal scans, not used for the result.
Third, `spinozas-ethica/` (2026-10-04): the Humor pipeline on a Google scan of an Academy volume (two folios
in the head, small-capital names, superscript note marks, tight word boxes); see TRANSCRIPTION-PLAYBOOK.md §00.
Fourth, `etik/` (2026-10-04): the same pipeline on a scan from the National Library of Norway (nb.no), Etik 4th ed.
(1913, 606 pp.).  nb.no gives page images and its own OCR as ALTO files, not a PDF with a text layer: `etik/nb_scan.py`
fetches both by IIIF and binds them into a PDF with the ALTO words as invisible text, each word on its ALTO line's
baseline and NB's superscripts (note marks) as superscript digits, and the line-end hyphen, which ALTO keeps apart as
<HYP>, put back on its word, so that draft.py and check.py read it unchanged.  nb_scan.py also writes, once, the
files draft.py and check.py read beside pagemap.py: notetops.tsv (where each page's notes begin: the printed rule
found in the page image, else a line that starts with a note's number), italics.tsv (the words NB's OCR set in
italics, for check.py --italics) and spaced.tsv (letterspaced words, for draft.py --post).  notemarks.tsv and
postfix.tsv hold what was read at the image (lost note marks, garbled notes; corrections inside markup).

`martensens-oplysninger/` (Nielsen, 1850; 2026-10-06): the first FRAKTUR book.  draft.py (KB's ABBYY layer), ocr.py
(tesseract script/Fraktur as witness; MODEL=deu_latf as a third reading), rules.py (Fraktur glyph-fault rules: frak,
frak-lit, vote3, oefix), batchsheets.py + readsbox.py (blind crops decided by crop id and boxed word), oepass.py (the ø
pass: lexicon + context-free word crops, oe-reads.tsv; and word-fixes.tsv from sweepsheets.py, the unattested-word sweep),
finish.py (footnotes rebuilt, POST corrections, Latin \textit, \emph, PRINTED AS IS).  Rebuild: see the transcription's header.

`scharling-apologie/` (Nielsen, 1850; 2026-10-06): a Fraktur book with NO text layer, copied from martensens-oplysninger.
ocr.py builds all three readings: MODEL=layer (tesseract script/Fraktur set as a text-only PDF layer,
.parts/layer-Fraktur.pdf, which draft.py reads through pagemap.layer_path()), MODEL=deu_latf (the witness) and MODEL=dan
(the third reading; it alone often sees ø).  rules.py: fault lists re-derived for the two tesseract models, the
two-attested-words guard with a frequency exception (frak-freq), rule2 (line-end = hyphens and spaces before stops),
skal.  finish.py rewritten (NOTES, POST, GLOBAL shared faults, EMPH, MISPRINTS).  The scan's MediaBox is four times its
CropBox: renders are the MediaBox, the page is their lower left (batchsheets.py/sweepsheets.py crop to it).

`mathematik-og-dialektik/` (Nielsen, 1859; 2026-10-06): a Fraktur book FULL OF FORMULAS, with Google's OCR layer (good on
the Fraktur, garbled in the math).  Copied from martensens-oplysninger.  Crop sheets were replaced by COMBINED PAGE
READERS (workgen.py: whole pages per reader, with the open words listed by context; each reader writes WORD, MATH in
LaTeX with anchor words, NOTE whole, SPACED, ANTIQUA, HEAD, PARA, ODD lines -> page-reads.tsv; wordapply.py decides the
words).  pagemap NO_NOTES: notes come from the readers, not the layer.  finish.py sets notes, formulas, headings, spacing,
paragraphs, then PAGEFIX: pagefix/pN.tex (pages rewritten whole by agents, text-only from the readers' lines, then at the
image for the doubtful ones) replaces a page only while the page from the earlier steps equals pagefix/base/pN.tex
(else PAGEFIX STALE with the diff); pagefix/CHANGES.tsv lists every word change.  Then WORDFIX (OCR faults from an
unattested-word sweep), POST, MISPRINTS (the book's own Rettelser).  losscheck.py: witness word runs the text lacks.
Front and back matter (title, motto, Forord, Indhold, Rettelser) are static in template.tex; pagemap END stops check.py
before the back matter.
Translation (2026-10-06): tr_extract.py (FIRST LAST | front | back), tr_build.py (ten parts; joins two parts with a blank
line only where the Danish has a paragraph break at that page turn; checks pages, notes per page, glued %, and emph,
textit, $ and paragraph counts per part), tr_template.tex, TRANSLATOR-BRIEF.md; nine Sonnet translators (1.06M tokens).
Their odd spots: trspots.tsv (screened by hand) -> spotsheets.py (crops round the tesseract box at 300 dpi, sheets
.render/...-tr-NN.png, -tr2-NN.png) -> ODD (literal, exactly once) and new MISPRINTS in finish.py, then the same changes
by hand in the English parts.  finish.py also: pagefix pages are spliced with '\n', not '\n\n' (a page turn is no
paragraph), then FALSE PARAGRAPH BREAKS and LINE-END HYPHENS passes for what the page-fix agents copied from the print.
Formula proof (2026-10-07): formulacheck.py (letters/digits of each formula against the layer and tesseract at its
anchors; flags what neither vouches for) -> proofsheets.py (scan crop over the typeset formula; --pages for whole-page
views of the items whose crop missed) -> readers' DIFFERS checked at the image -> FX in finish.py.
