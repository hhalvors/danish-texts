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
