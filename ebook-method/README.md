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

## Starting a new book

Copy the folder of the nearest model -- `filosofiske-problemer/` for endnotes,
`danske-filosoffer/` for footnotes at the page foot -- set the book's page map,
e-book file names and front matter, start an empty `decisions.tsv`, and follow
TRANSCRIPTION-PLAYBOOK.md §00.
