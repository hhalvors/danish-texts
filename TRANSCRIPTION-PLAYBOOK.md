# Fraktur/Antiqua → LaTeX transcription playbook

Point a fresh Claude session at this file to transcribe any 19th-century Danish
book in this repo from a page scan into `transcription.tex`. Use it as the
standing method; keep a short per-book **RESUME-NOTES.md** alongside it for
state that changes batch to batch.

**A caution about the word "complete".** This file used to advertise its model
book as "complete (VIII + 174 pp., 0 errors, done in one sitting)". Every term
in that boast is a statement about the *file*: `0 errors` is what LaTeX said,
not what a reader found. The repo said `0 errors` 218 times and had measured
the accuracy of exactly one of its 72 books. Do not describe a book as complete
on the strength of a clean compile. See §0.

For turning a finished transcription into English, see **TRANSLATION-PLAYBOOK.md**.

---

## 00. The current method (2026-09-30) — read this first; it supersedes §3 where they differ

Measured on *Totalitet som Kategori* (78 pp.) and *Erkendelsesteori og
Livsopfattelse* pp. 3–62. Every point below cost real money to learn.

**Before everything below:** **Always look for a cheaper method before reading scans page by page — and ask
Hans before using the expensive one.** Reading page images is the most
token-costly thing in this repo (on 2026-09-30, 29–40k tokens per page). Before
any job that would have agents read whole pages, check for less costly
alternatives and say which ones you checked: an existing transcription or e-book
of the same edition (see the book's RESUME-NOTES, "Edition check"); the scan's
text layer; a script-level diff between two machine texts, with the image
consulted only at the differences; a random sample instead of every page;
pre-cut crops instead of whole pages. **If you conclude that reading every page
at the image is the only way, stop and tell Hans before dispatching anything:**
why the cheaper options will not do, and the estimated cost in tokens. Do not
start a brute-force job on your own judgment.

0. **If a checked e-book of the same edition exists, do not transcribe at all.**
   Five Høffding books have one, with an "Edition check" recorded in their
   RESUME-NOTES (*Danske Filosoffer*, *Erkendelsesteori og Livsopfattelse*,
   *Filosofiske Problemer*, *Religionsfilosofi*, *Totalitet som Kategori*). The
   method there is: the e-book text is the base; a script diffs it against the
   PDF's text layer; the differences — spelling the e-book modernised, OCR noise
   on either side, notes the e-book moved to the end — are settled at the image,
   in batches of crops, with the print governing; page markers come from the
   layer's page boundaries. No agent reads whole pages. Read the book's
   RESUME-NOTES before choosing a method: *Totalitet* and *Erkendelsesteori* were
   transcribed from scratch on 2026-09-30 although both notes said "no
   retranscription needed" — ~5M tokens spent against a recorded decision.
   **The tools live in `ebook-method/<book>/` at the repo root (tracked; see its
   README): scripts, `decisions.tsv`, `patches.tsv`, the page map and the
   translation anchors.** A new book starts from a copy of the nearest model folder.
   **Worked examples:** *Psykologi i Omrids* (1882), 2026-09-28 — two-witness
   script incl. footnotes matched to endnotes and letterspacing measured from the
   gaps between letters (see its transcription.tex header; its scripts were never
   saved in the repo and must be rebuilt — save such tools in the book's
   directory); *Erkendelsesteori og Livsopfattelse* pp. 63–123, 2026-10-01
   (`ebook-method/erkendelsesteori-livsopfattelse/build.py`).
   (Known limit: misprints that both the e-book and the layer normalise, e.g.
   „Sammenbængen“, are invisible to the diff; whether to pay for an image pass
   to catch them is Hans's call per book.)
   *Filosofiske Problemer* (1902), 2026-10-02, whole book incl. endnotes and
   front matter (`ebook-method/filosofiske-problemer/`:
   `build.py` letter-level alignment in 3000-character windows, so the
   layer's split words and page boundaries cause no noise; `sheets.py --todo`
   crops whatever `decisions.tsv` does not yet settle; `patches.tsv` for
   non-word edits; `template.tex` + `build.py --emit` writes transcription.tex;
   `pagemarks-en.py` then places the page numbers in the translation).
   About 230 crops in all, no whole pages. Lessons from it:
   - **A "layer glyph fault" rule (layer h for e-book b, c for e, u for a …)
     may settle a disagreement only when the e-book's word is attested in the
     repo's other transcriptions.** Without that guard the e-book's own OCR
     errors pass as layer faults: „Grandlag“, „suffieiunt“,
     „Wissensehaftslehre“, „Besultat“, „Prineipet“ all did, until a full read
     of one spot page caught them. The e-book's endnotes were far worse than
     its body text.
   - **Never let the book's own output into that vocabulary** (a rebuild
     after writing transcription.tex silently "attested" every e-book error).
   - **Both OCRs read the point after an italic word as a comma** („Efterskrift,
     p. 83“ where the print has „Efterskrift. p. 83“): list every comma that
     closes an italic span, and every note's last mark, for the image.
   - **Read two spot pages in full after the build**, one of them from the
     notes. That is what found the two faults above.
   - Endnote labels can be irregular (here 12b, 31b, 31c, and the Noter print
     „12)“ twice): read them off the Noter pages' layer before mapping notes.
   *Danske Filosofer* (1909), 2026-10-02 (`ebook-method/danske-filosoffer/`),
   the same tools for a book with **footnotes**: the layer is split per page by
   word height into text lines and footnote lines (smaller type, below the last
   text line), each aligned with its own e-book stream (text / notes); text the
   two streams place differently (a note running over a page, a quotation in small
   type) shows as a long deletion in one and a long insertion in the other and is
   paired by content. Lessons:
   - Lines of figures only („1843.“) must not be dropped as page furniture in the
     footnote stream; they are the ends of notes.
   - Letterspacing (the print's emphasis) can be read off the layer, which sets a
     spaced word as single letters -- but short words (Et, af, os, her) split the
     same way unspaced; keep words under four letters only beside a spaced name.
   - The e-book may add commas the print lacks: check the punctuation list, not
     only the letters (27 corrections here).
   - The e-book can lack a whole section (here the Indledning): compare its first
     chapter with the scan's first text page before building.
   *Vort Hjem* (1903), 2026-10-02 (`ebook-method/vort-hjem/check.py`): no e-book,
   so the **existing transcription is the second witness** and the layer the first.
   Lessons:
   - A layer's word order can be scrambled (content-stream order) on a skewed,
     curved page: rebuild reading order from the word boxes (fit skew + curvature
     by the sharpest line histogram, cluster lines, sort by x) before aligning;
     unsorted it gave 798 "disagreements", sorted 41.
   - Letter rules must not settle case-only differences or a lone extra letter:
     they hid „eks.“/„Eks.“, „værd“/„værdt“, „selvfølgelig“/„selvfølgeligt“. Run a
     **word-level pass with punctuation** as well (`check.py --words`); it also
     finds misprints both readers might smooth over.
   - Italics, which the layer cannot show, are found cheaply by **stroke slant**:
     shear each word's image and compare the column profile's sharpness slanted
     vs upright (`check.py --italics`; italic 1.09-1.33, roman 0.77-1.01 here).
     Lone „og“ scores high from the g's tail; confirm runs at the image.
   - Crop the flagged word's own box, never the first text match on the page: a
     text-search crop showed the wrong line and three italics were dismissed; the
     spot-read caught it.
   - The Vort Hjem script is generalized as `ebook-method/collate/check.py BOOK` (README there):
     use it for every existing transcription; it takes the layer or a tesseract OCR as witness.
   - First run (2026-10-03), five texts: Religion og Videnskab normalized the print's adverbial
     „-t“ (egentligt → egentlig) eleven times; Realisme joined „lige som“ and missed 11 italic
     passages; the three made from OCR layers (Religionsfilosofiens Opgave, Udvalgte Stykker,
     Pascal) had no reading errors at all. Page markers were the commonest fault (`\apage`
     placed by eye: Realisme 13 of 14 off). Pagemap settings learnt: HEAD/FOOT patterns for
     running heads with lowercase words; CUTS for excerpts; ITAL per typeface (the Revue's
     italic leans less: 1.00).
   - Page numbers in a translation (`collate/pagemarks.py`, 2026-10-03; 670 markers in eight
     translations): CHECK THE DANISH MARKERS FIRST (`check.py BOOK --pages`). Kants and Den
     menneskelige Tanke had `\apage` markers placed before a word divided across the joint, or a
     line early (88 of 446). Headings: the marker goes on the first words under the heading, never
     inside `\section`. A translation with a contents page needs three LaTeX passes before every
     margin note shows. A translation can lack a page that was added to the transcription later
     (Den menneskelige Tanke p. 134).
   *Spinozas Liv og Lære* (1877), set up 2026-10-03 (`ebook-method/spinozas-liv-og-laere/`): **no e-book and
   no earlier transcription**, so step 1 below is `draft.py` (the layer by rule) and the witness for
   `check.py` is a tesseract reading (`WITNESS = 'ocr'`). Lessons from building the draft (Google's OCR
   layer, via HathiTrust):
   - The layer boxes punctuation apart, off the baseline: merge letter-less fragments into the nearest
     line, but never a folio or a section numeral (both were swallowed into the first text line).
   - Footnote stars are often lost; the notes' smaller type is not (line pitch ~10 vs ~14). Detect notes
     by pitch; pair an unstarred note with an orphan mark by order, and flag it.
   - Lone digits at the foot every 16 pages are signature marks, not text.
   - The OCR puts in Cyrillic look-alikes (р for p) and Lao marks for specks: map or drop them, or LaTeX stops.
   - Rules for the collation (`rules.py`, decisions noted `rule:NAME`, so each can be undone): settle only the
     WITNESS's known faults (tesseract: „ as a comma, “ as % or 4, *) as +) or %)) and what one OCR provably
     drops (Google's layer drops long dashes; tesseract's "—" boxes were all dash-shaped). Two rules that looked
     safe were withdrawn on review: "keep the layer's dash where tesseract has none" (the layer's free-standing
     "-" can be a speck or a split-off hyphen) and "keep the layer's quote mark" (quotation marks did not
     balance where quotations cross pages). A rule that keeps a mark only one witness has needs evidence
     beyond that witness; otherwise send it to the image. An accent rule may only accept accents the witness ADDS:
     printers of the period lacked accented sorts, so a missing accent may be the print's.
   - Word decisions cannot repair words a layer put out of order, notes it ran together, drop capitals read
     twice, or pencil marks in a library copy read as text: keep such fixes in a `patches.py` applied by the
     draft builder (each find must match exactly once), so `draft.py --emit` + `check.py --apply` still rebuild
     the transcription. 429 checks took 327 decisions + 68 patches; ~200k tokens for the whole image pass.
   - The two-OCR diff does catch some misprints: where Google's layer normalised („for“), tesseract read the
     print literally („før“, p. 110). Read such a check at the image before calling either OCR wrong.
   - Signature marks can carry a star (1*, 2*): drop them like the plain ones.
   - Calibrate the italics threshold on words known to be italic: here italics scored 1.01-1.08 (ITAL 1.03),
     far below the default 1.07; and wrap whole phrases by patch -- the detector finds runs in fragments.
   - Letterspacing, when neither OCR keeps it: measure the white gaps between letters in the word boxes
     (gap >= 0.16 x-height between at least 60% of letter pairs); 48 candidates, 33 real.
   - check.py's split/noise rule (same letters, different spacing) hid seven compounds the layer split at
     their hyphen ("dogmatisk -s pekulative", "teologisk -p olitiske"): grep the result for ` -[a-z]`.
     Found only while translating; a translator reading the Danish is a useful last reader.
   - A draft builder must not put a blank line before a page marker: in LaTeX it ends the paragraph, so
     every page turn split one (found only at the image, in the Forord).
   - Chain the rebuild: `draft.py --emit --force && check.py BOOK --apply`. draft.py exits non-zero when a
     patch fails to match, without writing; an unchained `--apply` then runs on the stale or raw file (it
     happened twice on Spinoza, 2026-10-03, and showed as OPEN 77 instead of 0).
   - `check.py BOOK --splits` lists the split/noise settlements where the transcription has a space the
     witness lacks: 23 on Spinoza, 2 real („(I maginationens)“, „(S kinsyge“; both after a parenthesis),
     the rest page-turn splits or Danish word division („i det“). A line-end hyphen that belongs to the
     compound („teologisk- politiske“) is joined away by the draft rule; read every such compound.
   - Both OCRs read a broken comma (dot with a faint tail) as a stop; three on Spinoza (pp. 103, 126, 157),
     one of them already decided "W" at a low-resolution image. Reread doubtful stops at 400 dpi before a W.
   - **Den store Humor (2026-10-04), lessons.** (1) Two OCRs agree on errors in small type: after OPEN 0
     the notes still had ~95 faults (italic spans cut in two or shifted onto the next word, ü read "ii",
     è/ê read "é", a note's last line lost or put mid-note, note numbers read as V, 9, 1, "-:I)"). Read
     every note at the image: crop from the footnote rule (a solid run of 300-1000 px, blank rows above and
     below) to the last line, scale to 1500 px wide, stack ~2400 px per sheet; 108 notes took 20 sheets.
     (2) Fixes that touch the italics or the decided words cannot be draft patches (check.py rewrites
     after them): put them in `patches.POST` and run `draft.py --post` as the LAST step; it refuses on a
     second run. (3) A `%` comment inside a one-line footnote comments out its closing brace: mark a misprint
     in a note by a regex patch that puts `% PRINTED AS IS` at the END of the physical line. (4) Specks read
     as punctuation inside words or between them ("Tænke'ren", "den,tidligere", "at.gaa", "(,,Dyder“)")
     survive the collation when both OCRs see the speck: grep `[[:alpha:]]'[[:alpha:]]` and
     `[[:alpha:]][,.][[:alpha:]]` after OPEN 0. (5) Note numbers are unreliable in both OCRs; find notes by
     indentation and smaller type, pair marks and notes by order on the page, and join a flush first line
     to the previous page's last note. (6) `--italics` must be in the same check.py call as `--apply`, or
     the italics decisions are not applied. (7) Sheet signatures here read "Den store Humor N": drop them
     like the plain ones. (8) A two-column Register: read each column on its own. (9) Greek needs
     `\usepackage{textalpha}` (absent on the device VM; test-compile elsewhere).
   - **Spinoza's Ethica (1918), set up 2026-10-04** (`ebook-method/spinozas-ethica/`, copied from
     den-store-humor; Google's scan of a whole Academy volume, the book at PDF 389-487). Settings that
     differed: (1) Google's word boxes are tight round the letters (median height 5.5 pt at a 13 pt pitch),
     so every threshold measured in box heights was off by half: measure indents and centring against 0.75
     of the line pitch (paragraphs found went from 56 to 312). (2) The running head is two folios, the
     volume's and the book's own ("344 8"): one fragment line, which the fragment merge put INTO the first
     text line until it was allowed as a line of its own. (3) The layer gives most note marks as
     superscripts (¹)): map them to digits; a superscript without its parenthesis is an edition number
     (\textsuperscript). (4) Citations close with a parenthesis, „(Eth. I, Def. 6)“: a digit + ) that
     closes an open parenthesis is not a note mark unless glued to a word („(som KEPLER³) selv ...)“).
     (5) Names in small capitals come as capitals in the layer: set `\textsc{Name}` by rule (check.py
     compares \textsc in capitals). (6) The series line at a sheet's foot, „D. K. D. Vidensk. Selsk. Skr.,
     7. Række ... 45“, and stars on sheet numbers („43*“): drop. (7) Greek capitals inside Latin names
     (SpinoΖΑ) and a Cyrillic т, Arabic digits as specks: map or drop, or LaTeX stops.
     **Collation lessons (same day, OPEN 0):** (8) Small capitals: tesseract reads them in mixed case
     (SpiNoza, HoBBEs); rules `smallcaps`/`smallcaps+`/`name` settle the case differences, and check.py now
     takes the decision `SC` (wrap the span in \textsc). But where BOTH OCRs read a name in lower case the
     collation sees nothing: a full-page read found two on one page, and a sweep found 68 more „Spinoza“.
     After OPEN 0, list every name that is \textsc somewhere and plain elsewhere, and read a sample.
     (9) The paragraph labels: Latin a. b. c. in the Indledning, Greek α. β. γ. δ. in the Books; both OCRs
     read α as a/u/4, γ as r/7/y, β as 3/PA: set by rule per part (draft.py layout()), in italic. (10) The
     layer drops long dashes inside tokens too (»andens“ —«, »Spinoza —«): grep the witness keys with a —
     the transcription lacks, after the rules. (11) Titles are italic in the notes only; in the text they are
     roman (Principia, Ethik, Regulæ): patches.ITALICS applies inside \footnote{} only. (12) Numbered points
     1) 2) 3) in the text and inside notes read as note marks; a note's continuation on the next page, and a
     passage in small type (the Exkurs, p. 18) read as notes: read every page with a note at the image.
     (13) In decisions.tsv a „=text“ with a space must be written with the TAB intact (a space-split broke two).
     (14) A word both OCRs read the same can still be a misprint OR a shared misreading: sweep the words not
     attested anywhere in the corpus and read each at the image (17 misprints found this way, 3 OCR faults).
     (15) The unattested-word sweep cannot see faults in punctuation, spacing and layout, nor misprints that are
     real words (kam for ham, kan for han, en en): translating the book found 15 more misprints and 14 such
     faults (TRANSLATION-PLAYBOOK §6c).  Until a book has had a full reading, OPEN 0 is not "clean".
     (16) Etik (2026-10-04), a scan from nb.no with NB's ALTO as the layer.  NB's OCR has its own systematic faults:
     a ring, umlaut or slash put in (nåar, tåge, übevidst, Førestillingen), o for ø (folger, gore), i for l (seiv,
     siet), words split by a space (Gen nemferelse); its superscript flag finds the note marks (in-text "1)" is an
     enumeration, not a mark); its word confidence is worthless (seiv at 1.00).  ebook-method/etik/rules.py settles
     these by rule (the witness's word attested, the layer's not).  A pilot on 10 pages counted ~7 word
     disagreements a page and guessed ~1 a page would reach the image; after the rules ~4.3 a page stayed open,
     a third of them punctuation only, which the pilot had left out of its count.  Count punctuation in a pilot.
     Stops and commas (29 read at the image): tesseract reads them better than NB, which often reads a stop as a
     comma; where the two disagree, the next word decides -- Danish capitalizes nouns, so only a capitalized
     function word (Men, Der, Naar) proves a sentence end, and only a lowercase word (not p., f.) proves none.
     check.py now writes the text after each check as a 4th column of checks.tsv, for such rules.
     An e-book of a NEIGHBOURING edition is still a strong third witness: SAGA's Etik is the 3rd edition (1905),
     which the 4th changed only in small places.  Where it agrees with one OCR reading against the other (found by
     the words around the check, unique in the e-book), that reading wins (rules.py 'ebook'; 13 of 14 right at the
     image, the 14th a word split at a line end, now excluded): OPEN fell from 2223 to 1097.  Check an e-book's
     edition from its prefaces, not its copyright year (SAGA prints the first edition's year).
     Before reading crops, look for faults of the LAYER BUILD that make hundreds of checks at once.  Here three did:
     NB keeps the line-end hyphen apart from its word (<HYP>, SUBS_TYPE="HypPart1"), so no word was joined over a
     line end ("Indfly delse"); the tight crop let letters of the facing page into the gutter as words before each
     line (";8", "\\", "I"); and a running head whose folio was read in pieces ("5 3" for 553) stayed in the text.
     Fixing those in nb_scan.py / draft.py and re-emitting took OPEN from 1082 to 670 with no image read.  Every
     re-emit must be followed by a fresh check.py --apply (applying onto an applied file makes new checks).
     Image decisions: 1,080 checks over ~110 crop sheets; the commonest NB faults left for the image were Greek,
     German and French accents (ö ü é è), roman numerals read as 11/111, „ read as .., and Men read as Alen.
     The notes are NB's weakest part: a note's continuation lines often land in the body, or a mark is lost;
     the crops show this but a word decision cannot mend it -- leave the mark-junk (*), -), l)) as an anchor
     and mend the notes in a pass of their own.
     The notes pass (2026-10-04): the layer's own guesses at where the notes begin (line pitch, word height,
     ALTO blocks) were each wrong on a few dozen pages; the PRINTED RULE above the notes, found in the page image
     (a short stroke from the text's left edge with white above and below, the scan's tilt allowed for), was
     right on every page checked and settles it (nb_scan.py notes).  A note that runs on from the page before
     stands flush with the text; a new note is indented.  Marks NB lost show as junk glued to the word ("-)",
     ":)", " ')", "*)"); where the junk is exactly as many as the missing marks it is taken as the marks, the
     rest were placed at the image (notemarks.tsv: also notes NB garbled or missed, typed from the image).
     Italics: NB's ALTO flags them (STYLE/FONTSTYLE "italics"); check.py --italics took those and confirmed them
     by its slant test on the scan's own images.  Letterspacing: a word box >=15% wider than Times needs for its
     letters; in a note it is \emph, in the text the same width means small capitals (\textsc).
     Corrections inside markup that a word decision cannot reach go in postfix.tsv (page, find, replace).
   - **Om Grundlaget for den humane Ethik (1876), 2026-10-05** (`ebook-method/humane-ethik/`, RESUME-NOTES has the
     rebuild line): TWO SCANS OF TWO COPIES, both with OCR layers, no e-book. Draft from the cleaner layer (Google's),
     witness = tesseract on the other copy, and the other copy's own layer as a THIRD witness (rules.py: a vote counts
     only if exactly one of draft/tesseract reading, set in 24 characters of context, occurs in the third layer; it
     settled 294 of 714 disagreements).  Lessons:
     (1) **Blind crops.** check.py --sheets prints both readings on each crop; sheets.py here labels only id and page,
     the reader transcribes the boxed line, and reads.py decides by finding one reading in the transcription.  The
     comparison must not match an EMPTY reading on one side of context (it deleted text twice: a whole line and a
     note's last line), and must not use a reading matched by loose context to another spot: after a reads.py run,
     list every W that deletes two or more letters and every decision whose two sides differ greatly in length.
     (2) **Silent non-application.** A W/P/= decision that --apply cannot carry out leaves its check DECIDED, so it
     never reappears as open: 16 such here (quote and dash insertions; the etik rule keeps the transcription's marks
     on a W).  Run `check.py BOOK --unapplied` after every --apply; pagemap `WMARKS = True` makes a W take the
     witness's marks.
     (3) **Never generate sheets, then change the draft before the readings are in**: check ids are renumbered and
     the readings no longer fit them.  reads.py therefore matches readings to checks by page and context.
     (4) check.py's split/noise rule settled every word-division difference unseen, both ways (Google ran
     "brænder i aaben", "har han", "af den" together); pagemap `SPACING = 'strict'` opens them unless one side is
     plainly fragmented (spacing_open).  Both OCRs still ran together some tightly set lines; the unattested-word sweep
     found those.  Glued lowercase+Capital tokens ("iEthiken") are always the layer's: split by rule.
     (5) norm() maps every quote to one mark, so quote KIND and guillemet DIRECTION were never checked; this print uses
     »...«, «...» and „...“ side by side.  `QUOTES = 'strict'` opens them.  Google's layer reads » « as >> < and
     doubles them; collapse doubled marks (found by the spot-read).
     (6) Google's layer drops the hyphen on a page's LAST line: the other copy's layer told which turns break a word,
     and was wrong twice (a pencil mark read as a hyphen) -- the witness's spacing check caught both.
     (7) Letterspacing: tesseract boxes on the 300 dpi KB images, white columns inside the word per letter gap / box
     height: normal 0.03-0.08, spaced 0.11-0.28; threshold 0.105 gave 386 candidates, 113 real (yes/no crops, 30 a
     sheet).  check.py's own spaced.py threshold (any gap between 60% of letter pairs) flags every antiqua word.
     (8) Cost, measured: ~1.0M subagent tokens for 146 pages (blind crops ~520k for 327 checks; all notes ~250k;
     letterspacing ~126k; spot-read ~97k).  A tesseract witness on the device must run in <=170 s chunks
     (background jobs die with the call); OMP_THREAD_LIMIT=1, 4 in parallel, ~3 s a page.
   - **Wikisource as a draft source (Mindre Arbejder I, 2026-10-05; `ebook-method/mindre-arbejder/`).** A page-by-page
     Wikisource text at quality "Valideret" is a cheap, well-paged draft (wikisource.py fetches it through the API, 50
     pages a request; one request per page met HTTP 429 after ~100), but it is NOT diplomatic: nouns lower-cased
     (standpunkt, samvittighed -- tesseract and the KB layer both read capitals), at for af, kuu, Konfiikt; and
     {{rettelse|PRINT|CORRECTED}} records its silent corrections of misprints (keep the PRINT, mark PRINTED AS IS).
     Treat it like an e-book: collate every word against the scan's layer, with tesseract as a third witness.
     Do not measure a witness's error rate against another transcription without the image: the first comparison here
     (Wikisource vs the "repaired" Realisme, ~20 differences) blamed Wikisource for errors that were Realisme's own --
     the print has „Kant's“, „Darwin's“, „Spencer's“ and „Udgangs- og Støttepunkter“ where Realisme has „Kants“ ...
     „Udgangspunkter og“ (checked at the image).  Readings in which a transcription and the layer AGREE are never
     checked by a collation; a second, independent text is what exposes them.
     Crop reading, measured the same day: a Sonnet reader agent costs ~60k tokens before it reads anything, then ~4k
     a sheet of 10 crops; 3 sheets cost 74k, 11 sheets 96k.  Give each reader 8-11 sheets, not 3.  Readers asked to
     transcribe still normalise now and then (Indbildningkraftens -> Indbildningskraftens): decide by comparison
     (reads.py), and read at the image yourself whatever the comparison cannot settle.  reads.py took a run-over
     footnote's text, a note mark and spaced dots for W: list every W that deletes or inserts more than a word.
     Readers normalise most where only they disagree with the machines: in the notes pass a reader gave Göttingen and
     Königsberg for the print's Gøttingen, Kønigsberg, and "Fremskrid" for Fremskridt; a word reader gave Vekselvirkning
     for the print's Vekselvirking.  A reader's reading that would CHANGE a word which both machine witnesses agree on is
     a claim, not a decision: read it at the image yourself before applying it (4 of 4 such claims were the reader's).
   - **Om Aandsdannelse (Nielsen, 1877), 2026-10-06** (`ebook-method/om-aandsdannelse/`, the Humor pipeline on a KB
     antiqua scan with no notes; first non-Høffding book: pagemap `AUTHOR = 'nielsen'` now tells collate/check.py,
     sheets.py and pagemarks.py the folder under texts/).  Lessons: (1) **Indent threshold**: KB's tight boxes (median
     7.6 pt at a 13 pt pitch) put the paragraph indent at ~2.8 box heights, beyond draft.py's 2.5: 25 paragraphs found
     instead of 152 until pagemap `INDENT_MAX` raised it -- measure the indent histogram before emitting.  (2) A book
     with **no notes** must switch off every note rule (pagemap `NO_NOTES`): draft.py turned citations „(24,1)“ into
     \footnotemark and last lines into notes, and rules.py's Humor rules 'seam' and 'mark' kept the layer's run-together
     words („VedSiden“) and took „(24,1)“ for note numbers.  Rules written for one book's note stream are not general.
     (3) **Quote kind**: tesseract read the print's „ as » 39 times; a 2-crop check showed the print sets „…“ only, so a
     rule (rules.py 'guillemet') settled 26 at once -- look at a few before reading them all.  (4) The layer garbles
     letterspaced lines (letters split: „Kul tu rskolen“, „Retfærd ighed..»Syælver“) and tesseract runs their words
     together: neither is a witness there; read every spaced line at the image and set it by patch.  (5) check.py's
     'split/noise' rule settled 22 such layer splits the wrong way (the transcription kept the space): read `--splits`.
     (6) A W decision whose key spans two transcription words and one witness word („Jiestemmes. Yil“>„Vil“) deletes a
     word: list W decisions that delete letters, as humane-ethik says.  (7) A witness-only „2*“, „3*“ is a sheet
     signature the LAYER put into the text: the decision is W, not T.  (8) The unattested-word sweep, narrowed to words
     one edit from an attested word, gave 14 suspects: 8 real misprints (Psysik, hlive, kvis, Siælen ...) and 5 faults
     BOTH OCRs shared (fon for for, Aaabenbaringens) -- cheap and productive.  (9) Letterspacing by letter gaps
     (spacedsheets.py) needs ≥5 letters here (short words score high unspaced); crop the WHOLE line so the reader
     reports short spaced words too; the spot-read still found 2 missed.  (10) check.py --italics prerenders all pages
     in one pdftoppm call and a killed run leaves `BOOK-batchNNN-*.png` unrenamed: rename them (PDF page - offset) and
     rerun.  Cost, measured: ~0.83M subagent tokens for 109 pp. (blind crops 518: ~610k; letterspacing + front matter
     ~123k; spot-read ~89k).
   - **Dr. H. Martensens dogmatiske Oplysninger belyste (Nielsen, 1850), set up 2026-10-06**
     (`ebook-method/martensens-oplysninger/`): the first FRAKTUR book in this pipeline (KB scan, ABBYY layer).
     (1) tesseract needs a Fraktur model: `script/Fraktur` (tessdata_best) as witness, `deu_latf` as a third reading
     (`ocr.py MODEL=deu_latf`); `frk` in tessdata_best is a 404 page, not a model.  Map on writing the cache: œæ/œ->æ (the
     model's reading of the Fraktur æ), ſ->s, ligatures.  tesseract reads Fraktur k as ff/f and I as J.  (2) With two weak
     OCRs ~40 disagreements a page.  Rules that took 2985 to 856 with no image read (rules.py): undo each side's KNOWN
     glyph faults (LAYER_SUBS, WIT_SUBS) and accept the agreement only if the CHEAPEST agreement is a word -- a misprint
     read right by one OCR is nearer the other's reading than the word it resembles, and so goes to the image; accept at
     once where one OCR's literal word is the other's after <=2 of the other's faults (frak-lit); deu_latf found under the
     witness word's box votes (vote3; fold æ/ø, which it lacks).  (3) **Attest only by words in >=2 other books**
     (STRONG): the corpus carries unrepaired OCR junk (knnne, deu) that "attested" wrong readings.  (4) **All three OCRs
     read the print's ø as o** (draft: 7 ø in 73 pp.; Johannes Climacus, same press, ~6 a page): no collation can see
     it.  Every Fraktur book needs an ø pass: lexicon where the o-form is no word, crops where both are words (for/før).
     (5) Decisions are keyed on the raw draft: count OPEN on a fresh `draft.py --emit --force`; check.py run on an
     applied file reports every changed word as a new check.
     (6) Blind crops for this book (pilot 102 + 5 readers x 150, ~1.1k tokens a crop incl. overhead; controls 12/12)
     took OPEN 856 -> 295.  reads.py's context match fails where the draft's context is garbled; readsbox.py decides by
     crop id and the BOXED word instead -- but a box at a line end holds only the word's first part, and a box need not
     line up with a multi-word key: take a reader's new reading ('=b') only for single words wholly inside the box.
     Readers infer ø where the stroke is faint (and say "unsure"): an ø pass on ambiguous pairs must be its own crops.
     (7) The ø pass (`oepass.py`, run after check.py --apply): a lexicon for o-forms that are no words (350 tokens), and for
     pairs that are both words (for/før, bor/bør, tør, føre, løse ...) TIGHT crops of the word alone, no context, 30 a sheet,
     so meaning cannot decide (196 crops, one reader, ~86k tokens, 31 ø).  The print turned out to have "før" twice where
     sense needs "for" (p. 73): context-free crops are what let a real misprint through to be marked.
     (8) A fix to (2): tesseract's x is SOMETIMES the print's (Paradox, strax, Excerpt): a glyph-fault rule must not
     settle a word against the corpus (literal reading unattested, the other attested) -- the spot-read found it.
     (9) Footnotes in a Fraktur KB layer were beyond draft.py (marks lost, a note split per line, run-overs): read
     every note page whole at the image and set the notes by script (`finish.py` NOTES: strip, then place at the
     mark), words from the collation, structure from the reading.  (10) Cost for 75 pp. of Fraktur: ~1.35M agent
     tokens -- about three times an antiqua book of the same length.
     (11) **A dropped line is invisible among hundreds of open glyph checks**: the KB layer lost a whole line (p. 4)
     and three shorter runs, and neither the collation rounds nor the spot-reads saw them; the translator saw only the
     garbled sense.  Run `check.py BOOK --witness ocr --dropped` (witness runs of two or more words the transcription
     lacks) on every book before finishing, and read each hit at the image.  (12) Inline `%` comments inside a
     replacement string in finish.py comment out the rest of the line (a note lost "siger lige det Modsatte;", another
     glued two words): never put a comment inside generated text, only at the end of a physical line by MISPRINTS.
     (13) The translators' odd-spot lists (134 spots, 59 worth a crop) found about 30 more faults and 6 misprints:
     cheap, because the reading is already paid for -- crop the spots and read them blind before building the English.
   - **Et Par Ord i Anledning af Prof. Scharlings Apologie** (Nielsen 1850, 24 pp., Fraktur, NO text layer; 2026-10-06):
     (1) With no layer, make one: tesseract script/Fraktur as a text-only PDF (`-c textonly_pdf=1 -c tessedit_create_pdf=1`;
     TESSDATA_PREFIX needs pdf.ttf) read by the usual draft.py; witness deu_latf; third reading dan.  (2) Two tesseract
     models share faults (k read f, sk read f or st, x read r, Ø read D, ø read o): words both read alike and wrong
     (iffe, fun, fal, theologiste, Loftestang, Parador) pass the collation; the unattested-word sweep and a look at
     every page find them -- set them with a GLOBAL list in finish.py, each checked.  (3) Fault lists must be derived
     from the book's own disagreements (count substitutions where one side's word is attested): the copied lists ran
     backwards (they took tesseract for the witness) and decided falder/kalder the wrong way.  (4) tesseract's Fraktur
     model writes a backslash for some long s (Profes\ſor, \muk), and keeps the line-end double hyphen as = or =-:
     map both before the draft.  (5) Page readers on whole pages miss short letterspaced words (p. 4 „tænker“); the
     main session's own look at all pages, two half-pages side by side at ~750 px a column, took ~40k tokens.
     (6) Cost: transcription ~0.75M agent tokens (3 crop readers 300k, 2 page readers 240k, ø+sweep 80k), translation
     ~125k: 24 pp. of layerless Fraktur cost about as much per page as Martensen's 75 pp. with a layer, x1.6.
   - **Den speculative Logik (Nielsen 1841, 192 pp. Fraktur, KB ABBYY layer), 2026-10-07** (`ebook-method/speculative-logik/`).
     Cost levers that worked, all before any image read: (1) a FOURTH reading, UB Mannheim's `frak2021` tesseract model
     (tessdata_best, in `.tessdata/`; fast, ~80 pp. per device call) beside deu_latf: two independent votes (rules.py
     vote34, consensus).  (2) Count each OCR's faults on the BOOK'S OWN disagreements before copying fault lists (oe>æ,
     Boe>Væ, N>R in the layer; doubled æ „Veæren“, z for ;, JI for the I/J sort in tesseract).  (3) Normalise tesseract's
     doubled æ BEFORE the rules (WNORM), or the substitution search chains it into another word (Vææren > Væren > Varen).
     (4) Join the layer's split words group by group against the witness (tokens()); the splits are letterspacing
     candidates.  (5) Accept a word as attested when it is a compound of two attested words -- but only with both third
     readings agreeing and both OCRs within two known faults (consensus): the book's own terms (Værenseenhed,
     Qvalificationsproces) are otherwise all unattested.  (6) Fraktur I/J is one sort: settle by convention, never at
     the image.  Rule guards learned from a blind AUDIT of rule decisions mixed into the crop sheets (A-ids; do this on
     every book with new rules): a winner must be attested (three tesseracts all read æ as e); two real words (Troe/Træ,
     sattes/sættes, kategorisk/categorisk) always go to the image; frak-lit only for an attested literal reading.
     8792 disagreements -> 2205 open (11/page) with no image read.  Crop sheets: 14 crops cropped to the TEXT BLOCK
     (not the page) at 2/3 of 300 dpi read well; ~430 tokens a crop at ~330 crops a reader.
     **Box the whole check**: the check's box is its first witness word only; a multi-word check (the layer's split and
     garbled words, a word divided at a line end) read from that box cannot be decided.  crops.py now boxes every
     witness word of the check, counted by LETTERS (a divided word is one key word but two OCR boxes).  Not knowing this
     cost a second round on ~600 checks (~340k tokens).
     Emphasis in this print is BOLD Fraktur as well as letterspacing; tell readers to note both.
     Finishing (same day, `finish.py`): (1) **check.py --apply could duplicate whole paragraphs**: a check whose words
     map partly into a footnote placed elsewhere gets an end offset BEFORE its start, and S[:s0]+new+S[s1:] then repeats
     the text between; 12 pages were hit before an 8-word duplicate scan found it.  --apply now drops inverted or
     overlapping edits; run the duplicate scan on every book after --apply.  (2) The split/noise rule kept the draft's
     split words („M odsigelse“) because the draft side was the fragmented one: pagemap `LAYER_SPLITS` makes them checks.
     (3) Footnotes can be in BODY-size type (pp. 34, 38-39): a note-area detector by type size misses them; read the
     marks (M crops of tesseract's '*' tokens) and look where a mark has no note.  (4) Headings: the draft's own
     `quote`/`center` blocks locate them better than fuzzy text search.  (5) Emphasis by stroke width (dark-run length
     across the middle of the word box, over the page median) separates bold Fraktur well (bold 1.5-2.1, plain <= 1.2);
     a blind audit of 60 auto-bold words gave 53 bold.  (6) Never crop a spot-read page by fixed fractions of the image:
     the text block's right edge was cut and the spot-read lost every line end; crop by the OCR's text block.
     (7) Measured cost, whole book: ~2.9M agent tokens for 192 pp. of Fraktur (~15k/page); of that the crop rounds
     ~1.8M, structure/notes/emphasis/ø ~0.6M, residue + sweep ~0.3M.
   - A transcription marked "unassessed" may hide real rewording (here an
     interpolated phrase and normalized grammar: „Inderlighed“ for „Inderligheden“,
     „giver“ for „give“): collate before trusting it.

1. **No agent re-types the text.** A script builds the draft: the scan's text
   layer page by page (line-end hyphens joined, running heads stripped), page
   markers from the layer's own page boundaries, italics from the font tags.
   Where an e-book of the same text exists, a word diff against it flags every
   place the two machine texts disagree. Agents supply **corrections as a
   list**, which a script applies.
   *Why:* transcribers who re-wrote the page from the OCR introduced slips of
   their own (*Erkendelsesteori* p. 15: layer „stans.“, agent „stanser“) and
   silently "corrected" the print's misprints.
2. **One image pass per page, by an agent that did not produce the text.** It
   reads every line of the page against the draft, settles every flag, supplies
   footnotes, paragraphing and faces, and reports corrections.
   *Why:* **both machine texts normalise the print's misprints.** The ABBYY
   layer and the e-book read „for“, „matière“, „Sammenhængen“, „Dommen“,
   „Forholdet“, „det“ where the print has „før“, „matiére“, „Sammenbængen“,
   „Dømmen“, „Forboldet“, „pet“. Seven of the eight real errors found in 138
   pages were of this class. Only the image shows them; ocrdiff cannot.
3. **Two planted control errors per reader** (a one-letter change, a dropped
   short word) in the reader's copy; a batch whose controls are not both
   reported is read again. *Why:* readers without controls returned 0 errors on
   27 pages in 2–3 minutes with no zooms — indistinguishable from not reading.
   With controls: 16 of 16 caught.
4. **Cost discipline inside every agent:** stage a batch's images in at most two
   calls; about 40 tool calls in all; save results to a file page by page;
   **after two failed calls to the device, save and return — never retry in a
   loop.** On 2026-09-30 two readers made 700–900 calls during a connection
   drop and burned ~250k tokens.
5. **Measured cost of the old way** (agent-typed text plus a second full image
   pass): 29–40k tokens per page; *Totalitet* came to ~3.3M for 78 pages. The
   method above aims at roughly half; the *Erkendelsesteori* pp. 63–74 pilot
   measures it.
6. **Guillemets:** LaTeX's `\guillemotleft` is «, `\guillemotright` is ». Danish
   print »…« is coded `\guillemotright…\guillemotleft`. *Relation som Kategori*
   and seven Kroman texts had them reversed until 2026-09-30. Check the image.
7. **Where lessons go:** anything learned that applies beyond one book goes into
   this playbook (and, if it changes the method, CLAUDE.md) **the same day.**
   `RESUME-NOTES.md` and `BATCH-AGENT.md` are gitignored per-book files; a lesson
   left only there is lost to the next book. That is how the "don't re-type"
   lesson, learned in collation work (pgtools/COLLATE-BRIEF.md, COLLATE-WORKFLOW.md),
   never reached new transcriptions.

Working tools (in `texts/hoeffding/erkendelsesteori-livsopfattelse/`, untracked,
copy per book): `sr_prep.py` (page bands + the page's text for a reader),
`.parts/sample/plant.py` (controls; log kept outside the repo),
`.parts/sample/SR2-READER.md` (reader brief), `draft.py` (the script-built draft;
added with the pp. 63–74 pilot).

---

   - **Om Skjæbne og Forsyn (Nielsen 1853, 81 pp. Fraktur, Google Books scan of the BL copy, Google layer), 2026-10-07**
     (`ebook-method/skjaebne-og-forsyn/`, copied from speculative-logik).  (1) Google's Fraktur layer at 600 ppi is far
     better than KB's ABBYY: 13 disagreements a page against tesseract (KB on speculative-logik: 46), 98% of its words
     attested; speculative-logik's rules held unchanged (blind audit 46/46).  Look for a Google copy before ordering KB
     digitisation.  (2) Google's layer reads a Fraktur line-end hyphen as `z` or ` =` („Bez|givenhed“, „re =|ligiøse“):
     the draft does not join them; grep `[a-zæø] ?[z=]$` before finishing.  (3) After any `--apply`, count OPEN only on
     a FRESH draft (`draft.py --emit --force` first): counted on the applied file, OPEN went from 7 to 49.  (4) Cost: three
     blind crop readers for 1066 checks + audit ~261k, one structure reader (title, headings, notes, residue) ~97k.
     (5) The sampled page check found what the collation cannot: faults SHARED by Google's layer and tesseract -- the
     Fraktur Ø read as D (Øie, Øieblik, Øine) and j read as i after g/k (giør for gjør) -- 4 of 5 word errors in 1177
     words.  Before the page check, run a lexicon scan for these two classes (a D-word whose Ø-form is attested; gi/ki
     + vowel whose gj/kj-form is attested) and crop every occurrence: 49 here, all but 2 real.  „Dieblik“ is attested
     in four other Nielsen transcriptions (om-personlig-sandhed 7 lines): the same fault, a repair-queue candidate.
     (6) readsbox2.py's `=b` takes the reader's box, which can stop short of the punctuation: 5 marks lost („?“, „;“,
     „,“, „“"), one found by the page check.  After a round, list `=` decisions whose punctuation differs from the draft's.
     (7) A sheet signature the draft keeps (key `p|1*>`) is decided W, not T (T keeps it in the text).
   - **Erindringer (Høffding 1928, 324 pp. antiqua, ABBYY layer, e-book of the same edition), 2026-10-07**
     (`ebook-method/erindringer/`, from den-store-humor + etik's e-book vote; rebuild line in RESUME-NOTES).  The 41 pages
     already read at the image on 23 Sep served as the CALIBRATION of the whole pipeline (`cmp41`/`cmpstruct`: compare
     the built text with them word by word and in paragraphs/white lines/rules).  Lessons: (1) A same-edition e-book is
     more than a vote: diff the FINISHED text against it (`ebookdiff.py`) and read every difference at the image --
     it caught faults both OCRs shared („cand,“ for „cand.“, split words „Øster rigs“, glued „tilVejle“) that the
     layer/tesseract collation cannot see.  But the e-book is itself an OCR and SHARES some faults (p. 80 „1er“ in layer,
     tesseract and e-book alike): it is not ground truth, and it moves italics (p. 307).  (2) White lines and printed
     rules leave a gap in the layer of ~2.0 or ~3.0 times the line pitch (verse and set-off passages 1.5-1.8): the draft
     can find them (`WHITE_GAP`); neither OCR nor e-book marks a white line, and 6 of them on the 41 pages had been lost.
     Which gap is a rule cannot be told from its size; the e-book's rule positions, read at the image, decide.
     (3) Old-style figures: the folio „111“ reads „III“ and „11“ „II“ -- a folio test that excludes roman numerals
     keeps them as text; compare with the page number.  (4) In an `re.sub` template, `'\1' + '70...'` is group 1 then
     an OCTAL escape (\170 = „x“): write `\g<1>`.  (5) A page reader's „PRINTED AS IS“ correction must go on its own
     line BEFORE the line, never after the word: inside a one-line footnote the `%` comments out the brace (the build
     failed; draft.py --post now moves such notes).  (6) A page reader's LINE outside the boxed word can drop a word
     (control X05): decide on the BOX.  (7) Cost: 2 blind collation readers ~258k, 3 e-book-difference readers ~331k,
     7 page-pass readers (89 pp., 14/14 planted controls found) ~940k; ~1.6M agent tokens for the transcription.
     (8) An e-book of the same edition may be an OCR of the SAME kind as the layer, and share its faults („giede“ for
     „glede“ twice, „religøs“, „Flourney“): its vote FOR the layer and against tesseract is weak evidence.  Audit every
     such T vote off the pages read whole (blind crops; here 155 votes, 5 wrong, ~3%), and treat the e-book diff as a
     list of places, not as truth.  The translators' odd spots then found 7 more faults and 75 unmarked misprints.
   - **Den Stærkeres Ret (Nielsen 1863, 13 pp. Fraktur, Google Books scan of the BL copy, Google layer), 2026-10-08**
     (`ebook-method/staerkeres-ret/`, copied from skjaebne-og-forsyn; RESUME-NOTES has the rebuild line).  (1) For a short
     book, read EVERY page blind (pagecheck.py with all pages in sample.tsv): one Sonnet reader, 33 sheets, ~148k tokens,
     found 16 word errors in 3,857 words that the collation (OPEN 0, audit 21/22, controls 2/2) had passed -- 8 of the two
     shared-fault classes (Ø read as D; gj read as gi), 4 ø read as o that oepass.py's lexicon did NOT list (hoiere, Hoihed
     and Mode are „attested“ elsewhere, so they never reach the lexicon), plus Har/Hær, Glosfer/Glosser, JIllusionen and a
     drop capital the layer read twice („P Paa“).  The differences were settled from ~20 line crops in the main session.
     (2) Rule `frak` turned the layer's RIGHT „gjøre“ into „giøre“ (layer gjøre, tesseract giore): a glyph rule must never
     move a word INTO the gi/ki class; and the audit caught `frak` once more („samler“ -> „famler“).  (3) Google's layer
     can drop a dash inside a sentence and add a space before „!“: the page reader saw both.  (4) A page reader's claim
     against all three OCRs is still a claim: „dristige, driftige“ (p. 13) was read as a doubled „dristige“; a 600 dpi
     crop showed f, not long s.  (5) INDENT_MAX had to be 5.0 here (paragraphs 0 at 3.6): measure before emitting.
     Cost: crop reader ~89k, page reader ~148k, translation inline; ~240k agent tokens for the whole book.
     (6) THE ø RULE (Hans, same day; CLAUDE.md, Editorial stance): an o-form that is no Danish word is ø, without image
     or second reader -- a faded slash or worn sort, not a compositor's non-word.  So the ø lexicon must not drop a word
     because other transcriptions „attest“ it (they still carry hoiere, Hoihed ...); judge the o-form as Danish, not by
     corpus frequency.  `oefix.py` (repo root) applies a reviewed list; logik-og-psychologie, which had transcribed the
     plain o „as printed“, was brought under the rule (217 sites).
   - **Georg Brandes og Universitetsfilosofien (Rubow, Danske Studier 1928, 18 pp. antiqua, ABBYY layer), 2026-10-09**
     (`ebook-method/brandes-universitetsfilosofien/`).  A SHORT text with footnotes several to a line: the layer draft
     placed none of its 35 notes and the two-OCR collation left 208 of 241 disagreements open, many of them notes and
     marks.  Cheaper and better here: the full blind page check FIRST, as the base text, with two machine readings as
     the check (vote.py): a reader's word stands only if the layer or tesseract agrees; 6,411 words left 24 word and 39
     mark disagreements, 9 cropped, 7 reader slips found (Indførere for Indfører, a lost colon and closing quote, a false
     division „tab=ikke“, Greek accents, a doubled italic opener) and 2 misprints the readers had silently corrected
     („Afhængighed at“, „har spiller“).  Also run the reverse search, words both machines read and the reader lacks
     (a dropped word or line): only running heads.  Notes, marks, italics, paragraphs and block quotations come from the
     reading, so no note pass is needed.  Cost ~224k agent tokens (two readers, 52 sheets) -- less than crops for 208
     checks plus a page check.  Limits: a fault a reader shares with ONE machine passes (two of three); faces (italics)
     rest on the reader alone.  Before writing faces, list lines with an odd number of `*`: a reader opened a span twice
     across a line end.  Also: Danske Studier sets a line-end hyphen inside compounds („maskeret-|teologiske“) the same as
     a division -- read each joined compound.
     (Build failure the same day: greek-fontenc/textalpha has NO text-mode ϑ (U+03D1, the curly theta), and the sandbox
     compile test hides it because it maps all Greek to a placeholder.  Set the print's ϑ as θ, and grep body text for
     ϑ and ϱ before handing a book over.)

   - **Om Begrebet Nøiagtighed (Nielsen 1860, 55 pp. Fraktur with many formulas, 17 notes, errata; Google BL scan), 2026-10-10**
     (`ebook-method/begrebet-noiagtighed/`; RESUME-NOTES has the rebuild line).  (1) **Look for every Google copy first**: the
     book was to be done from a DTU scan (300 ppi colour, weak layer); Google Books had the BL copy (2013, 600 ppi, the
     skjaebne-og-forsyn batch) and a Harvard copy (2008).  The edition page's "Other editions" link finds the second copy;
     the PDF downloads in Hans's Chrome (ask first), into ~/Downloads (request access, copy into bibliotek).
     (2) **When the two-OCR collation leaves too much open (here 715 of 1825, mostly formulas and notes), take the
     brandes-universitetsfilosofien route even for Fraktur**: the full blind page reading as the text of record, every
     reader word voted against layer + tesseract + the collated draft (vote2.py), unsupported words cropped blind
     (cropsv.py, controls), every formula and Greek line read a second time blind (lines.py, formcmp.py), and the book
     written from the readings (fromreads.py).  ~0.8M agreed with Hans instead of ~1.1M for crops + page check.
     (3) **Run a check of the FINISHED text against the machines** (finalcheck.py: words both machines read otherwise) and
     the D/Ø lexicon scan after building, not only the vote: the vote's alignment let „besaarsag“ (both machines
     „desaarsag“), „Fællesproblem“ („Fælledsproblem“), „befindet“ („besindet“) and four D-for-Ø words through, and the
     reader had read „Diemed“ just as both OCRs had.  The page reader shares the D/Ø fault and the f/long-s confusion.
     (4) **Turned letters**: „saud“, „Functioneus“, „Synspuukt“, „Differeutialcoefficienterne“, „eud“, „dct“ were read as
     n/e by the reader AND Google's layer; only tesseract kept them.  turned.py lists words where tesseract (or, with
     --layer, the layer) differs from the reading by one turned/wrong sort and is no corpus word: 11 listed, 6 real.
     (5) Readers' format pitfalls for fromreads: a division written `]]=` / `[[…` across an antiqua span, a `[[…` span
     carried over a line end, a line begun with the last line's full stop, a Danish word put inside `[[…]]` („for=|[[uden
     et genus…“), `[stamp]` and date stamps („18 JY 63“).  The Fraktur `=` → `-` rule must never run inside math
     („arc (cos=x)“, „∫_{x=a}“ had become minus signs).  One reader set the antiqua zero as O, another as 0.
     (6) **vote-fixes are literal and applied in order**: make each find unique LITERALLY (mkfix.py extends it), never by
     a word-boundary match alone; the first version silently rewrote the wrong „end“ and „Enheden“.
     (7) Crop sheets for agents must be ≤ ~1560 px on the long side (Read downscales larger images: a 400-dpi sheet 2600
     px high is read at ~240 dpi).  Device background jobs die with the call: run tesseract in ≤170 s chunks.
     (8) A main-session 600-dpi look is not infallible: „og at,“ (p. 36) was a damaged k („og ak,“, cf. p. 48); the
     translator's sense doubt caught it.  Cost: page readers 776k, crop readers 211k, line readers 250k.
   - **Philosophien i Tydskland efter Hegel (1872), pilot pp. 1-16, 2026-10-09** (`ebook-method/tydskland-efter-hegel/`).
     (1) **An Internet Archive Google scan has no text layer in Google's PDF, but the Archive keeps an ABBYY OCR with
     character boxes** (`_abbyy.gz`) and the 600 ppi G4 TIFFs (`_tif.zip`): `abbyy_scan.py build` binds them into a
     layered PDF that draft.py and check.py read like any other.  (2) **Measure the folios from the layer before
     anything else**: the offset jumped by 2 at p. 236 -- a leaf missing from the scan, found only that way.
     (3) ABBYY's TeX specials: `^` is its reading of „ (before a word) or of a comma/point/“ (after one); `''` is a
     quote; `\ { } ~` occur.  Map them in emit_line, or LaTeX and check.py's brace matching break (an IndexError in
     group_end was a stray `{`).  A `^` inside a word is a broken letter (Tilsidesa^ttelse), not a quote.
     (4) ABBYY splits after kj/gj ("Erkj endelsen", "Gj enstand"): check.py's split/noise rule settled all five the
     wrong way; `--splits` found them.  (5) Controls for blind crops can be taken from a rule's own decisions
     (answer = the rule's reading): they measure the reader AND audit the rule at once (6/6 here).
     (6) erindringer's sheets.py trims 6% of each margin: on a Google scan with narrow margins that cut line ends
     off (12 re-crops); set `ox = 0`.  (7) **A page whose impression is heavy and smeared defeats both OCRs** (p. 9:
     the layer lost four lines, both garbled six): read it whole and set it by `patches.PAGESET`, comparing the
     reading with both OCRs (`pagediff.py`) -- never word decisions on garble.  (8) **Spot-reads by comparison are
     weak**: two Sonnet readers given a page and its transcription with two planted errors each caught 1 of 2 each.
     The blind crop controls are the better measure; a spot-read's "no further differences" is not evidence.
     Cost, measured: ~381k agent tokens for 16 pp. + front matter (4 agents, ~60k fixed overhead each).
     (9) **A second Google copy as third witness** (same day, the Minnesota copy from HathiTrust): its layer's LINES are out
     of order (a plain pdftotext gave the context of only 32 of 176 checks): rebuild reading order from the word boxes
     before voting.  Then 58 votes, 58 agreeing with the image, and one image decision shown wrong; checks sent to the
     image fell from 134 to 75.  A leaf missing from one copy is spliced in from the other (`abbyy_scan.py splice`),
     so that the page map stays uniform; the spliced pages must not be voted on by their own copy.
     (10) **Look for clipped page edges** (Chapter 4, p. 219): a scan cut at the left margin loses the first letter of
     every line (ivor, unne, Beligions-); both OCRs then agree on the wrong word and the collation never sees it.  Only
     a second copy catches it (umnsweep.py against the Minnesota layer): run it on every chapter.
     (11) **Order of patch stages matters.**  Notes set from readings (NOTESET/PAGESET) replace text that literal
     patches cannot see beforehand; mends to notes whose marks the draft crossed or lost, and to text that a set note
     makes visible, belong in a last stage on the FINISHED text (patches.POST2).  Likewise a misprint marker for a word
     inside a set note is written into the set text, not left to a line-end rule that runs earlier.
     (12) **A tool added late must not pre-empt older patches**: manual.py (decisions --apply cannot carry out, found
     by a junk-tolerant pattern) at first rewrote spots that POST patches of earlier chapters already handled, and 12
     of those then failed to match.  It now skips any find that overlaps a POST patch on its page.
     (13) **An automatic decision must not drop a word the reader saw** (Chapter 5): reads.py's exact pass, with its
     context shortened to 3 characters, chose a witness reading that lost "Hartmann (f." from a section head.  Any
     T/W decision whose rejected reading has a word present in the reader's line and absent from the chosen one now
     goes to hand.  (14) Clipped pages can be found before reading anything: count the lines whose first word is
     unattested in the corpus; > 8% of a page's lines flagged every clipped page in pp. 117-318.
     (15) **Greek: read it at 600 dpi, in a pass of its own, and tell the reader to give only what is printed.**  Readers
     at 300 dpi had set wrong accents and an \textit; at 600 dpi one reader found every breathing and accent, three
     misprints of the print's own (εῖναι, μόρφη, ἀρχῆ without iota subscript) and one doubt.  Greek of this period is
     set in a cursive face (κ looks like x): that is the face, not emphasis -- do not mark it \textit.
## 0. What the job is

**The job is to transcribe a book _and establish that the transcription is
accurate_. Those are not two jobs. A fragment whose accuracy has not been
established is not finished work.**

This has to be said at the top because for the first half of this corpus it was
never said at all, and the omission was invisible. The pipeline had rigorous
discipline about cost, and rigorous discipline about *structure* — page markers,
paragraphing, emphasis, Greek accents, printer's defects, all of it verified at
the image and logged. What it never had was a discipline about **words**. No
book was ever asked what its error rate was, so no procedure for answering
existed, so books were published `status: complete` with no evidence about the
one thing a transcription is for.

It was concealed by vocabulary. A finished book reported `0 errors`, `0 missing
characters`, `compile clean`, `TRANSCRIPTION COMPLETE`. Every one of those is a
typesetting result. `0 errors` is LaTeX's verdict; `0 missing characters` is a
font-coverage check. They read exactly like accuracy claims and are not. When
*Den menneskelige Tanke* was finally collated it came in at **~0.9 transcription
errors per page** — roughly 350 in one book — having passed every gate the
pipeline had.

### Why this is nearly free during, and ruinous after

**The check is almost free at the moment of transcription and costs a second
transcription afterwards.** This is the whole argument, and it is arithmetic:

The batch agent has already rendered the page. It already has the OCR in its
context. Comparing its own words against that second reading is a diff it is
holding both sides of — ten or so candidates on a thirteen-page batch, each
settled at an image it has *already paid to render*. That is the cheapest review
in this pipeline, and it is the only step that can see a dropped „ikke“.

Deferred, the same check requires rendering and reading all 392 pages again from
cold. *Den menneskelige Tanke*'s repair took forty collation agents over every
page in the book, then five waves of splicing, then a full re-verification — a
second pass comparable in cost to the original transcription, to recover
information that was in the first agent's context window and thrown away.

> **So: the check is not a stage that follows transcription. It is part of
> transcribing.** An agent that returns unchecked words has not done the job
> cheaply; it has deferred the expensive half of it onto someone else, at
> roughly forty times the price.

### The cost constraint, which is real and comes second

Cost discipline is a constraint on *how* the job is done. It never relaxes the
standard above, and confusing the two is what produced this corpus.

The cost of this job is context replay. A batch of twelve pages needs ~30k
tokens of OCR dumps and page images; those stay in the conversation and are
re-sent on every later call, so by batch 15 you are paying to re-transmit batch 1
fourteen times over. The fix is not "start a fresh conversation every batch" —
that works but wastes the user's time. **Dispatch each batch to a subagent.** It
starts cold, burns the OCR and images in its own context window, and returns
~150 words: **~119k–152k tokens inside each agent, a single paragraph in the
calling conversation.** Roughly a hundredfold reduction in what accumulates.

> **In the main conversation, never read a page image and never let OCR output
> land there.** Everything else in this file follows from that.

Both disciplines at once, in one line: *the images are read, and the words are
checked, inside the agent — and only conclusions come back.*

### The mechanism

Every batch is diffed against an independent machine reading of the same pages,
before it is spliced, with no book exempt:

```sh
python3 ocrdiff.py --frag .parts/pp<FIRST>-<LAST>.texfrag
```

Structural checks cannot see a missing „ikke“. Of the errors found in *Den
menneskelige Tanke* without consulting the OCR, **two-thirds were readings the
scan's own text layer had already got right** — the words were not lost by the
OCR, they were lost between the OCR and the file, because an agent handed a page
of OCR does not copy it: it reads it and writes it out again. Nothing compared
the two, so nothing could see it. §3 step 4 is the full rule, §3 step 6 is how
the result is recorded, and `SCANS.tsv` says which witness each book uses.

### No book in this corpus has ever been transcribed under this rule

Measured 13 September 2026 across **all 74 `RESUME-NOTES.md` files in
`texts/`**: the number carrying an `OCRDIFF:` line is **zero**. The only file
that mentions `ocrdiff` at all is *Den menneskelige Tanke*'s, and that is the
collation which produced the tool. The rule postdates the entire corpus.

So this is not a lapse in one book. **Every transcription in `texts/` was made
without its words being compared against a second reading**, and every one then
passed `check.py`, `paginate.py verify` and a clean compile and was published
`status: complete`. *Logik og Psychologie* is simply the one that has since been
measured: 38 batches, no `OCRDIFF:` line, **1.17 errors per page**, with a
clause paraphrased and a whole sentence dropped on p. 405 that the scan's own
text layer had **correct**.

Two consequences, and the second is the one that is easy to get wrong:

- **The presence of an `OCRDIFF:` line is not a triage signal.** It was tried as
  one on 13 September — the hope being that books which had recorded the check
  could be exempted from collation — and it has no discriminating power at all,
  because the value is constant across the corpus. Do not retry it. It belongs
  with the four failed proxies in REPAIR-PLAYBOOK.md §1.

- **Unchecked is not the same as wrong.** All seven books whose rate is now
  known were transcribed without the check, and their measured rates run from
  **0.0 to 1.17 errors per page** — *det religiøse* and *Philosophiens Historie
  I* each returned 0 errors over 12 sampled pages. "Never verified" describes
  all 72 books. "Contains errors" describes an unknown subset, and the only way
  to move a book from the first description to the second is to read it.

From here forward the discipline is a **control, not an exhortation.** Before a
book may be called complete:

- every batch entry in `RESUME-NOTES.md` carries an `OCRDIFF:` line (§3 step 6);
- the count of `OCRDIFF:` lines equals the count of batches;
- a book that cannot show this is not `complete`, whatever `check.py`,
  `paginate.py verify` and the compile say. Those are typesetting results.

Treat a missing `OCRDIFF:` line exactly as REPAIR-PLAYBOOK.md treats a missing
accuracy statement: the book is **unmeasured**, and unmeasured is a status, not
a formality.

### Two things the diff cannot see, so it is necessary and not sufficient

Both were measured on *Logik og Psychologie* on 13 September 2026.

1. **Long divergences never appear at all.** `ocrdiff` anchors on three matching
   words each side. A paraphrased clause followed by a dropped sentence breaks
   the anchor, so it is not merely filtered — it is absent from the output
   *before* any filtering. The p. 405 loss is invisible to the tool. Only a
   reading of the page finds that class.

   A per-page word-count comparison against the OCR was tried as a cheap
   detector for it and **does not work**: on that book p. 405 ranks only 48th of
   481 pages by shortfall, buried in noise from footnote attribution and
   displayed equations (sd ≈ 72 words on ~330-word pages). Do not add it.

2. **Whole-book mode hides systematic faults.** `python3 ocrdiff.py <slug>`
   discards any divergence whose (kind, tex-word, scan-word) triple recurs more
   than twice, on the theory that recurrence means OCR noise. But a systematic
   *transcriber* fault recurs too. That book has a running fault of `ø` losing
   its slash — `forste`/`første`, `hoiere`/`høiere`, `folge`/`følge` — and the
   filter hid **24 of its 28 instances**, keeping 4.

   The per-batch `--frag` path does **not** filter, which is a further reason
   the per-batch discipline is the one that matters. When auditing a finished
   book, re-run with the filter disabled before concluding the tool cannot help
   it — and never estimate the tool's usefulness from a random draw of
   candidates, because the pool is dominated by the near-worthless `DITTO`
   class. That mistake was made on 13 September and recorded a book as
   `ocrdiff precision 0/15` when the tool in fact works on it.

### The sense check: a detector, never an authority

Read the batch back as Danish before splicing, and flag anything that is **not a
word** or that reads as garbled — `hveranbre` for `hverandre`, a mangled proper
name, a citation whose figures cannot be right. Then **go to the image** and
settle it there.

That is the whole of the licence. Sense may tell you *where to look*. It may
never tell you *what to write*, for two reasons, both of which have already
produced damage in this corpus:

- **The errors that matter read perfectly.** The p. 405 error was „at vi skulle
  gjøre store Anstrengelser i denne Retning“ — fluent, idiomatic, entirely
  plausible 19th-century Danish, and not what the page says. So does a dropped
  „kun“, „ikke“ or „ny“; so does a modernised `Regelen`→`Reglen`. Fluency is
  what these errors *are*. A text that reads well is evidence of nothing, and an
  agent asked whether the Danish makes sense will answer yes on exactly the
  pages where it has gone wrong.

- **Correcting toward sense breaks the edition.** These are diplomatic
  transcriptions: a printer's error is transcribed **as printed** and logged in
  a `%` comment at the site (§4). "Making sense of it" is the precise
  description of the wrong action. *Logik og Psychologie*'s own notes already
  warn of this — `check.py` deliberately carries no dropped-`ø` test, because
  that compositor really does set plain `o` for `ø` unsystematically, `hoist`
  beside `høist` on the same page, and "sniffing for it flags correct readings,
  which invites a later hand to make the edition wrong."

So: where the Danish reads oddly, suspect the file and check the page. Where the
Danish reads well, suspect nothing and prove nothing. If a reading is odd **and**
the image confirms it, it is the printer's and it stays, with a comment.

---

## 1. Set-up (once per book)

A book lives in `texts/<author>/<slug>/`. Before batching, it needs:

- `transcription.tex` — preamble (`book` class, 12pt, A4, openany — never
  `article`, even when the pipeline is borrowed from a short text), front matter
  (title page, prefaces, the printed Indhold), and a `\chapter*` skeleton with
  one marker per chapter: `% [text to be added: pp. X--Y]`.  Set the front
  matter first, not last: *Etik* (2026-10-04) was collated without it.
- `pagemap.py` — **the single source of truth for printed page → PDF page.**
  Scans are not uniformly offset: on this book a leaf was scanned twice, so the
  offset changed from +13 to +15 partway through. Never hard-code an offset;
  every script calls `pagemap.py`.
- `ocr.sh` — Fraktur OCR for a page range, with the book's closed set of
  systematic confusions fixed by `sed`.
- `spacing.py` — mechanical letterspacing (Sperrsatz) detection. Fits a
  per-glyph advance width over the page by least squares and flags words that
  come out too wide.
- `check.py` — gap/dupe detection over `% --- p. N ---` markers, brace and quote
  balance, progress.
- `splice.py` — merges batch fragments into `transcription.tex` (see §3).
- `joints.py` — batch-seam paragraph breaks and dangling word-break hyphens, the
  two silent corruptions that survive every other check (see §6).
- `BATCH-AGENT.md` — the prompt body. **It must carry the copy-text discipline
  block from §4**; that block, not the playbook, is what the batch agent
  actually reads, and it is the agent-side half of the fix for the defect in §6.

Copy these from `texts/nielsen/evangelietroen-theologien/` and adjust
`pagemap.py` and the `ocr.sh` sed table for the new scan.

`ocrdiff.py` is **not** per-book: it lives at the repo root beside
`paginate.py`, works on any book with a text-layer scan, and needs no set-up.
§3 step 4 runs it on every fragment.

**None of this harness is tracked in git**, and neither is `BATCH-AGENT.md` or
`RESUME-NOTES.md`. A book directory tracks the **edition only** —
`transcription.tex`, `transcription.pdf`, and later the translation pair. The
root `.gitignore` enforces it; the reasoning is recorded there. In short: the
repo is public, the harness is unrunnable without the scans (which are correctly
not in the repo), and the copies are near-identical from book to book.

So the harness lives on your machine, and **the durable scholarly record goes in
the comment header of `transcription.tex`** — the verified page map, the errata
applied, the emphasis findings, the normalisation conventions, and the log of
printer's defects. Write that header as the thing an outside reader would need in
order to check the edition against the scan, because it is the only thing they
will get. `RESUME-NOTES.md` then carries only volatile state.

**The preamble must define the page macro** before any batch runs, or the
first fragment will not compile:

```latex
\usepackage{marginnote}
\newcommand{\opage}[1]{\marginnote{\footnotesize\textit{[#1]}}}
\newcommand{\apage}[1]{\marginnote{\footnotesize\textit{[#1]}}}
```

**Verify the page map by eye before transcribing a single word.** Read the
printed numeral off every page of the scan and confirm the endpoints. An
undetected offset change silently corrupts the whole book.

---

## 2. Is the OCR usable, or is the image the only witness?

Test this per book; it decides the whole pipeline.

- **Fraktur, clean scan** (this book): the Fraktur tesseract model reads it well.
  OCR carries the *words*; the image only has to carry *structure* — paragraphing,
  footnotes, rules — plus emphasis and doubtful readings.

  **This is the right division of labour and it is what makes a book cheap. But
  read what it commits you to.** If the words come from the OCR and the image is
  not going to be read word by word, then the OCR's words are your copy-text,
  and the only thing that can tell you whether they survived into the file is a
  machine comparing them. That is `ocrdiff.py`, and §3 step 4 makes it
  mandatory. A book transcribed on this premise *without* that comparison has
  nothing whatever checking its prose — which is the state eleven books in this
  repo were in until 2026-09.
- **Antiqua, poor scan** (Nielsen's *Religionsphilosophie*): the text layer was
  rejected outright and every page had to be eyeballed. Much slower.

Keep the PDF's own ABBYY layer (`pdftotext`) as a **second witness**: it fails
differently from tesseract (it tends to lose æ/ø), so where the two agree the
reading is safe, and where they differ, look at the image.

### Find out what the scan can actually resolve, before adjudicating any glyph

**Run `pdfimages -list -f P -l P <scan>` on a body page at the start of every
book.** A KB scan is typically not one image: on *Evangelietroen og den moderne
Bevidsthed* each page is a 96 ppi RGB image **plus a 1-bit mask at 400 ppi**, and
the mask carries all the type. `pdftoppm -r 1200` on such a page is 3× interpolation;
`-r 2400` is 6×. Interpolation preserves the topology of a stroke, so it still
helps you read — but it invents no evidence, and a distinction that lives in one
or two pixels of the mask cannot be settled by rendering bigger.

This matters because Fraktur has pairs that differ by almost nothing: **x/r**
(the x's tail below the baseline), n/u, and long-s/f. On this book an inventory of
some 130 "wrong sorts" — strar for strax, Erempel for Exempel, Tert for Text —
was built up page by page from renders at 1200 and 2400 dpi, defended with
confident measurements, and **had to be withdrawn in its entirety**: calibration
against words the edition already accepted as x showed that four of eleven
certain `strax` carry no visible tail at all, so absence of a tail was never
evidence. Two "control pairs" cited as proof that the compositor mixed the sorts
(a true `strax` twelve lines below a `strar`; a `voxer` above a `vorer`) both
turned out to be the same word twice.

Three rules follow, and they cost fifty hours to learn:

1. **Calibrate on words the edition already reads the other way**, not on your
   sense of what the glyph looks like. Measure the discriminating feature on a
   set of certain instances of each letter and see whether the distributions
   actually separate. If they overlap, the scan cannot decide and no amount of
   zooming will change that.
2. **Only a positive signal counts.** Silence is not evidence for either reading.
3. **Put the burden of proof on the claim of a defect.** Where the printed form
   is not a word in the language, default to the sense-reading unless the glyph
   positively shows otherwise. Errors in the other direction *fabricate* evidence
   about the printing house, which is worse than losing a real datum — and, left
   in a batch brief, they propagate: three consecutive batches here inherited the
   mistake from each other and hardened it into a rule.

Note that this is a departure from strict diplomatic practice, and a deliberate
one. It applies to sort-level distinctions the scan cannot resolve — not to
turned sorts, dropped sorts, broken sorts or punctuation faults, which are
plainly visible and stay logged as printed.

---

## 3. The batch loop (older method — superseded by §00 where they differ)

Batches are independent — each touches exactly one marker — so several can run
at once. **Concurrent agents must never edit `transcription.tex` directly:**
`Edit` is a read-modify-write over the whole file, and two agents finishing at
the same moment can clobber each other. `check.py` would catch a whole missing
batch but not a half-written one.

1. **Dispatch** one subagent per batch, 12–17 printed pages each, using the
   prompt body in the book's `BATCH-AGENT.md`. Give it the page range, the
   lecture/chapter name, and the exact marker line. `BATCH-AGENT.md` must tell
   it to open every page with `\opage{N}` at the word the page begins on (§4);
   if the book's copy predates that rule, add it before dispatching.
2. Each agent writes `.parts/pp<FIRST>-<LAST>.texfrag` — the text that will
   replace the marker, starting with its own `% --- p. FIRST ---`.
   **The extension must be `.texfrag`, never `.tex`** (see §6).
3. **Splice** in the calling conversation: `python3 splice.py`. One process, one
   write, no race. It matches each fragment to its marker by filename, archives
   spliced fragments to `.parts/spliced/`, and refuses to run on `.tex` fragments.
4. **Diff the fragment against the scan's own words** — before splicing, and
   non-negotiable for any book with a usable text layer:

   ```sh
   python3 ocrdiff.py --frag .parts/pp45-57.texfrag
   ```

   It prints every place the fragment's words diverge from the OCR's, with three
   exactly matching words on each side, and labels the classes that have
   actually gone wrong here (`dropped word`, `adverbial -t dropped`, `form
   modernised?`, `likely OCR`). Expect roughly ten items on a thirteen-page
   batch and expect about half to be the scan's fault — settle **each** at the
   image and either correct the fragment or dismiss it. Ten adjudications per
   batch is the cheapest review in this pipeline and it is the only step that
   can see a dropped „ikke“. Do not splice a fragment with unresolved items.

   Nothing here is filtered on suspicion of being OCR; the labels are hints.

   **There is no book to which this does not apply.** The check is against a
   *machine witness* — an independent machine reading of the same page — and
   the embedded layer is only the commonest one. Every book names its witness
   in RESUME-NOTES before its first batch is dispatched, in one of three forms:

   - **`USABLE`** — the scan's embedded layer. `SCANS.tsv` at the repo root gives
     every book its scan, that scan's sha256, and its layer state (55 of 72 are
     `USABLE`). `python3 scans.py path <book>` returns the verified path. This
     is the default and needs no argument.
   - **`NO LAYER`** — the embedded layer is absent or unusable. Four books are
     in this state (`hoeffding/pascal-kierkegaard`, the three Treschows).
     **Build the witness**: run tesseract over the batch's pages with the
     book's own model (`-l dan` for antiqua, the `Fraktur` *script* model for
     Fraktur — see `brochner/svar-nielsen/RECON.md` for the recipe and the
     trap), write it to `.parts/ocr/pp<FIRST>-<LAST>.txt`, and pass it:

     ```sh
     python3 ocrdiff.py --frag .parts/pp45-57.texfrag --ocr .parts/ocr/pp45-57.txt
     ```

     A tesseract witness is noisier than ABBYY, so more of its candidates will
     be the witness's fault. That raises the cost of the step; it does not
     excuse it. The point of a second witness is not that it is right — it is
     that it is *independent*, so anything both readings agree on was not
     invented between them.
   - **`NONE POSSIBLE`** — the book has no page images at all, because it is
     not scan-derived (`hoeffding/erindringer`, from an EPUB;
     `hoeffding/forholdet-tro-viden`, from Wikisource). These are the only
     legitimate exemption, they must be named as such in RESUME-NOTES **and**
     in `catalog.yaml`, and a reader must be able to see that the text has no
     original behind it. A book in this state is not a diplomatic
     transcription and should not be published as though it were.

   The distinction that was missed for eleven books is the one between *the
   check found nothing* and *the check never ran*. Those look identical in a
   finished file and opposite in a resume note, so the note must say which.

5. **Verify** in the calling conversation — cheap, text-only:
   `python3 check.py` (no gaps, no dupes, balanced braces, 0 suspect readings),
   then the compile test in §5. **Also check the page markers**: one `\opage`
   per printed page in the batch, numbers strictly increasing, none inside a
   command name. A batch covering pp. 45–57 must contain `\opage{45}` through
   `\opage{57}` and nothing else:

   ```sh
   grep -o '\\opage{[0-9]*}' .parts/pp45-57.texfrag
   ```

   A missing one means a page was skipped — the fault that lost printed p.134
   of *Den menneskelige Tanke* entirely, undetected until the book was
   paginated years later.

6. **Record that the check ran.** Every batch agent returns one line in a fixed
   form, and the caller copies it into RESUME-NOTES beside the batch entry:

   ```
   OCRDIFF: <witness> | <n> candidates | <n> corrected | <n> witness's fault | <n> unresolved
   ```

   e.g. `OCRDIFF: embedded | 11 candidates | 4 corrected | 7 witness's fault | 0 unresolved`.
   Unresolved must be 0 before the fragment is spliced; if it cannot be, the
   line says why. A batch entry in a RESUME-NOTES with no `OCRDIFF:` line is a
   batch whose words were never compared against anything, and a later reader
   should treat that book's word-accuracy as unestablished. `grep -L OCRDIFF
   texts/*/*/RESUME-NOTES.md` is the corpus-wide version of that question.

   **And when the book is finished, the totals go in the comment header of
   `transcription.tex`.** `.gitignore` excludes `RESUME-NOTES.md` and
   `BATCH-AGENT.md` on purpose — they are working files, and the durable
   scholarly record belongs in the header, "where it travels with the
   edition". A reader a year from now needs to know how this book's words were
   established, and a working file that was never committed cannot tell them.
   One line:

   ```
   % Word-accuracy: every batch diffed against <witness> before splicing
   % (ocrdiff.py). <n> batches, <n> candidates, <n> transcription errors
   % corrected, 0 unresolved. See TRANSCRIPTION-PLAYBOOK.md §3 step 4.
   ```

   A finished book whose header cannot carry that line is a book whose words
   were never checked, and the header should say *that* instead, plainly.
7. **Spot-check one emphasis call per batch** against the scan. This is the only
   step where the main conversation may look at an image, and it is worth it:
   the agents have been right every time so far, but the check is a few thousand
   tokens against a silent corruption risk.

Use the task list (TaskCreate/TaskUpdate) per round; it renders as a progress
widget for the user.

**The user commits and pushes — you never do.** (You almost certainly *cannot*
anyway: the sandbox has no git identity and cannot unlink files, and a half-run
`git commit` leaves a `.git/index.lock` behind that blocks the user's next
command.)

---

## 4. Transcription conventions

- **Mark every page turn, as you transcribe it.** Put `\opage{N}` at the exact
  word where printed page N begins — mid-sentence if that is where it falls,
  and mid-word too: where the original hyphenates *inden-/for* across the turn,
  write `inden\opage{30}for`. `\opage` sets no text, only a marginal *[N]*.

  This is not bookkeeping, it is the edition. A transcription without page
  markers cannot be cited: a hit in it is a paragraph number of ours, useless
  in a footnote, and a reader of the PDF cannot find the passage in the
  original. Møller's volumes have always done it and are the model.

  Do it *now*, while the page image is in front of you and the turn is a fact
  you can see. Recovering it afterwards costs a session per book and can only
  be approximate: of 73 transcriptions, 10 carry visible markers, 28 carry the
  page turns only as comments and still await `paginate.py convert`, and 27
  have no record of the original pagination at all — none of those 27 has a
  scan on disk, so for them the information is simply gone until one is found.

  A comment is a record, not a marker. `% --- p. 110 ---` on its own line is
  good practice and the search index now reads it, but the printed page shows
  nothing, so the PDF cannot be cited from. Write `\opage{110}` as well, in the
  body, at the word where the turn falls.

  Use `\opage` — you read the page. `\apage` is reserved for markers placed
  afterwards by machine alignment (see PAGINATION-PLAYBOOK.md); never write it
  by hand.

- 19th-century orthography **exactly as printed**: `Christendommen`,
  `Videnskaben`, `Theologie`, `høiere`, `aa`, capitalised nouns. Do not modernise.
- Danish quotation marks `„…“` low-high, as printed. Em-dash `---`.
- Letterspaced emphasis → `\emph{}`. Latin/foreign set in antiqua against the
  surrounding Fraktur → `\textit{}`. **Check the image**: a German name may be
  antiqua on one page and Fraktur on another, and each occurrence follows its own
  page.
- Footnotes: plain `\footnote{}`, with the printed mark noted in a `%` comment.
  If the book marks them `*)`, set `\renewcommand{\thefootnote}{*)}` in the
  preamble — **not** `\fnsymbol` (math mode, gives U+2217) and **not**
  `footmisc[perpage]` (resets on the *typeset* page, not the printed one, so a
  second note on your page becomes a dagger).
- Page markers: `% --- p. N ---` on its own line where printed page N begins.
  `check.py` depends on these; every page in the batch needs one.
- **Printer's defects: transcribe as printed**, log a `%` comment at the site,
  and report it. Do not silently correct the compositor. Expect the quote balance
  to drift off zero as a result — that is the *signal*, and the running total
  belongs in RESUME-NOTES so nobody later "fixes" it.
- Doubtful readings: zoom, then transcribe your best reading and flag the
  alternative you rejected. Never silently guess.

---

### Copy-text discipline — paste this into every batch prompt

The agent is not writing Danish; it is moving a fixed string of words from one
place to another. Say so, and say it in the prohibitive form — "be accurate" is
not an instruction an agent can act on, whereas "do not improve anything" is:

> You are copying, not composing. Where the text layer and the page agree, the
> words are already settled and your job is to carry them across unchanged —
> including every word you would have phrased differently, every spelling that
> looks like a mistake, and every short word you might not notice dropping.
>
> The 1910 orthography is data. `egentligt`, `navnligt`, `stadigt`,
> `oprindeligt`, `i Regelen`, `Principet`, `stansede` are correct as they stand;
> do not modernise a trailing *t* or a doubled consonant, and do not assume an
> archaic form is OCR noise.
>
> If the PAGE is wrong — a broken letter, a transposed pair, a misspelt name —
> transcribe the error **as printed** and log it in a `%` comment at the spot.
> Never silently correct the print. If you find yourself about to fix
> something, that is the moment to write a comment instead.
>
> When you are unsure between two readings, do not pick the one that reads
> better. Render the page and look.

---

## 5. The sandbox compile test

```bash
cp transcription.tex /tmp/t.tex
sed -i -e 's/\\usepackage{libertinus}/\\usepackage{lmodern}/' \
       -e 's/\\usepackage{libertinust1math}//' \
       -e 's/\\usepackage{textalpha}.*//' \
       -e 's/\\usepackage\[danish\]{babel}//' /tmp/t.tex
pdflatex -interaction=nonstopmode /tmp/t.tex
```

Expect **0 errors, 0 missing-character warnings**. Three false alarms this
produces, none of them defects in the file:

1. **Garbled `æ ø å` in the terminal log** — the terminal's encoding.
2. **`Unicode character … not set up for use with LaTeX` for every Greek letter**
   — caused by the `sed` stripping `textalpha`, which the real preamble loads.
   Confirm with `grep '^!' log | grep -v 'Unicode character'` (must be empty),
   and to test the rest of the file map Greek to a placeholder:
   `re.sub(r'[Ͱ-Ͽἀ-῿]', 'G', s)`. **Never delete Greek from the source.**
3. **`make` fails with `libertinus.sty not found`** — that package isn't in the
   sandbox. It is not a problem with the document; an untouched file in the repo
   fails identically. Real builds happen on the user's machine.
4. **`Undefined control sequence` for a math command** — `\varkappa`,
   `\underset`, `\overset`, `\angle`, `\wedge`, `\to`. The `sed` strips
   `libertinust1math`, which is what supplies them. *Grundideernes Logik* shows
   22 of these and *Den menneskelige Tanke* 49; both are clean on the real
   machine. Confirm by building the file's own backup the same way and
   comparing — **never compare a bare error count across the recipe**, only a
   file against its own untouched backup built identically.

### latexmk caches a failure and will not retry

`make` on the whole tree can end with

```
Latexmk: Nothing to do for 'transcription.tex'.
Collected error summary (may duplicate other messages):
  pdflatex: gave an error in previous invocation of latexmk.
```

and name no book, because the book it is talking about is the one it just
skipped. latexmk records the failed run in `.fdb_latexmk`; if the `.tex` has not
changed since, it reports the old failure instead of rebuilding — so a file that
was *repaired by reverting to a backup* keeps reporting an error it no longer
has. To find which book, look for the logs rather than the make output:

```bash
for f in $(find texts -name transcription.log); do
  n=$(grep -c '^!' "$f"); [ "$n" -gt 0 ] && echo "$n  $f"
done
```

Then check whether the error is still present in the current `.tex` before
fixing anything. Force the rebuild with `latexmk -g` or `make -B`.

---

## 6. Traps that have actually caused damage

- **`glob('/tmp/pg*.png')[0]` returns a stale page.** `/tmp` is shared between
  agents and `009` sorts before `068`, so a verification can confidently examine
  entirely the wrong page. This happened. Always
  `mktemp -d` + `pdftoppm -singlefile`.
- **Fragments named `.tex` break `make`.** The Makefile discovers targets with
  `find texts -name '*.tex'` and a preamble-less fragment dies with
  `Missing \begin{document}`. Hence `.texfrag`, plus `**/.parts/` in `.gitignore`.
- **Never write scratch renders inside the repo.** One agent wrote 26 PNGs
  (25 MB) into the book directory; they were committed and pushed, and the blobs
  are in history permanently. Render to `mktemp -d`. `.scratch-*/` and `*.png`
  are now gitignored, because the ignore rules don't depend on an agent complying.
- **A word the compositor broke across a line becomes `Cau- salitetsforholdet`.**
  A transcription reflows, so the printed line-break hyphen has to be resolved —
  but an agent writing out a page naturally copies the hyphen and starts the next
  source line with the rest of the word, and TeX turns that newline into a space.
  Nothing catches it: braces balance, quotes balance, `check.py` is happy, the
  file compiles with zero errors, and the defect is invisible until you read the
  PDF. Nine such words were in one book's first 147 pages, and eight more hid
  behind an `\emph{}` or a `\setcounter` on the intervening line. Write
  `Cau\-%` — discretionary hyphen, then `%` to eat the newline — and put a
  `%` on any `\setcounter`/`\markboth` line that sits between the two halves.
  **This must be an automated check, not a habit.** `joints.py` in
  `texts/brochner/det-religioese/` does it, and also catches the related seam
  bug: `splice.py` replaces a marker that the skeleton wrote with a blank line
  above it, so wherever a sentence runs across a batch boundary the joined file
  silently acquires a paragraph break the book does not have. Comments do not
  save you — a `%` line eats its own newline, so a comment between the text and
  the marker still leaves two consecutive newlines. Copy `joints.py` alongside
  the rest of the harness and run it after every splice, before `check.py`.
- **An agent rewrites rather than copies, and every structural check passes.**
  This is the costliest defect in the repo's history — ~0.9 errors per page
  through a whole 392-page book, undetected for as long as the book existed.
  The profile is specific, and recognising it is half the battle:
  - **dropped short words that leave grammatical Danish behind** — *kun*, *ikke*,
    *ny*, *og*, *saa*. p.336 of *Den menneskelige Tanke* read "Disse to Emner
    kunne reduceres til hinanden" where the page prints **ikke** reduceres: the
    transcription asserted the opposite of the original and read perfectly well.
  - **archaic forms silently modernised** — `egentligt`→`egentlig`,
    `Regelen`→`Reglen`, `Principet`→`Princippet`, `stansede`→`standsede`. A
    trailing *t* in 1910 orthography looks exactly like OCR noise to a reader who
    expects the modern form, so it gets "cleaned up".
  - **printer's errors silently corrected** — eleven of them in that book
    (*Benouvier*→Renouvier, *donnies*→données, *Anfangsgrunde*→Anfangsgründe).
    The same instinct aimed at the print, and the one thing the editorial stance
    most explicitly forbids.
  - **occasional paraphrase of a whole clause.** You cannot get that by
    mis-copying; it only happens when the text is being re-composed from sense.

  Braces balance, quotes balance, `check.py` is happy, the file compiles, the
  page markers are all present and strictly increasing. **`ocrdiff.py` in §3
  step 4 is the only thing that catches this**, and it catches it for free. The
  agent-side half of the fix is the copy-text discipline in §4: the instruction
  must forbid improving, not merely ask for accuracy.

- **Scope corrections to the heading block.** A skeleton chapter argument read
  `halvspeculative` where the printed head read `halvphilosophiske` — but
  `halvspeculative` occurs 13 times as the author's own term. A global replace
  would have corrupted twelve legitimate occurrences.
- **Don't trust the contents pages' OCR layer.** Chapter arguments reconstructed
  from it carried two errors on this book. Transcribe the Indhold from the image
  like any other page, and cross-check each argument against its printed head.
- **The book's own contents page and its chapter heads may genuinely differ.**
  Two such variants were confirmed at 600 dpi on both witnesses here. Record both
  readings; do not normalise them into agreement. The disagreement is a datum.

---

### A comment that wraps onto a second line is typeset (2026-10-03)

In *Erkendelsesteori og Livsopfattelse* two notes `% (set in smaller type in the print)` had been
wrapped by an editor, so the second line, `in smaller type in the print)`, was ordinary text and
was printed in the transcription PDF. Only the e-book comparison (`collate/xcheck.py`) caught it,
as words the print "has" and the e-book lacks. Never let a `%` comment wrap; a continuation line
must begin with `%` again. A quick test: a comment line with an unclosed `(` followed by a text
line with an unopened `)`.

### A PDF that nothing will open (2026-10-03)

The Academy's *Begrebet Analogi* PDF (ABBYY FineReader Server) has a broken page tree: poppler,
MuPDF and Ghostscript give up. `pikepdf.open(path, attempt_recovery=True)` still finds the page
objects, and the page images can be taken straight out of them
(`ebook-method/begrebet-analogi/repair_scan.py`). Before trusting a damaged file, count what is
really in it (page objects, image streams): this one announces 142 pages but holds 137, so the
last four printed pages were never there. A host tool that "reads every page cleanly" may only
have been asked about the early pages.

Later the same day an intact copy (all 142 pages) was obtained, so "byte-for-byte the same as
the Academy's download" did not mean no better copy existed: ask for another copy before
building around a damaged one. When the copy arrives: point `pagemap.py` at it (or at an OCR
file merged from the old OCR and the new pages, if the first pages are already read), lift the
build's tail limit, re-emit, and diff the formerly unwitnessed pages against the previous
emission. Only page markers and note numbering changed here; the e-book's words held.

### What the e-book method cannot see, and how to look (2026-10-03, Den nyere Filosofis Historie)

1. **A misprint both witnesses share.** The SAGA e-book is an OCR of the same print, so it reproduces
   the print's slips ("Udvikliug", "Tilskyndelssr", "Pechner"), and the tesseract layer reads them too:
   no hunk, no check, and the slip goes through silently corrected or silently kept with no comment.
   After the build, list every word of the transcription that occurs in no other transcription of the
   corpus (one short script: the corpus vocabulary is the build's VOC); read the list, and look at the
   image for each suspect. 476 unknown words gave 15 misprints to mark PRINTED AS IS.
2. **A turned letter that a rule settles.** The rule that writes off (n, u), (h, b), (I, l) ... as layer
   faults settled "hau" and "Kauts" for the e-book's "han" and "Kants" -- the print has a turned n
   both times -- and settled the e-book's "tumIede" against the layer's correct "tumlede". Keep the
   rule-settled hunks (build.py writes auto.json) and look at the classes that can be real: n/u,
   I/l, B/R.
3. **Word division.** The alignment compares letters, so an e-book that runs two words together
   ("Sjælog", "mansin") agrees with the print letter for letter. build.py's joins() compares the
   divisions in the two witnesses (line-end hyphens excepted); decide each at the image.
4. **A scan that loses the tails.** The Google scans of 1903-04 print a comma as a point and a
   semicolon as a colon wherever the tail is thin: dozens of punctuation checks where the scan
   "shows" a point. Read the zooms with that in mind: the e-book's comma or semicolon stands unless
   a tail is visible; a visible tail is evidence, its absence is not.
5. **Letterspacing recall.** Measure, then run a relaxed second measure over the rest and look at
   every crop (124 here, three sheets of 42 small crops): it found one name the first measure missed.
   A spaced word broken over a line end is not measured at all.
6. **patches.tsv**: "⏎" in the find column now means a newline (it was only honoured in the
   replacement, so a find with ⏎ silently never matched; the build prints PATCH NOT APPLIED -- read it).

### The same book, whole (2026-10-10): what a scan can and cannot show

Extending *Den nyere Filosofis Historie* from the selection to the Third and Ninth Books (~730 items read blind at
600 dpi, two planted controls per batch; details in that book's RESUME-NOTES, top section) corrected point 2 above.

1. **This Google scan cannot show a turned letter.** At 600 dpi it renders h with a closed foot ("ban", "Varigbed",
   "Goetbes") and n as u ("andeu", "Egeu-") in ordinary words all over the page. A reader cannot tell a turned n
   from the scan's own n, so "hau", "Kauts" and "aloue" (2026-10-03, read as turned n) are not evidence of a misprint.
   And the e-book was OCR'd from the same scans ("aloue", "grnndigere" are in it too), so it is no independent
   witness for these letters either. Policy: for n/u, h/b, e/o (worn e), l/i, c/e and a speck-sized accent or
   point, sense governs, with a `% scan:` comment where the image shows the odd form. Look at two whole sheets
   of a scan before trusting any letter-pair "misprint" a reader reports.
2. **Measure a rule before trusting it.** A blind 600-dpi sample of 60 rule-settled hunks, 15 per rule, showed
   which rules held (the ø rule 15/15) and which disagreed (layer-fault 4 of 10, all of them the artifacts in 1). It
   cost ~230k. Do it for any book whose rules settle hundreds of hunks.
3. **The e-book drops words, and the letter alignment never flags them.** "Ro", "ham", "ved", "Væsen", "Se", dashes,
   an opening », and the subscripts in "A₁ … B₁" were missing. The translators found them as odd spots.
   `ebook-method/nyere-filosofis-historie/dropsweep.py` compares the layer's word sequence with the
   transcription's and lists insertions only: 137 raw, 6 real (most are lines the layer read out of order).
4. **Cost.** A blind Sonnet reader costs ~1.8k tokens a crop (10 sheets of 6 crops ≈ 100–110k). The ~700 readings
   supported only one new safe rule (two e-book words the layer joins: 35/35). Budget per item, not per page.

5. **A "speck" rule can swallow letters.** A rule that writes off a layer character as a speck kept the e-book's word
   where the layer had a real extra letter (16 of 165 such hunks; "maatte", "træffe" …). A layer letter that turns an
   unknown e-book word into a known one is a check, never a speck.
6. **Two readers must never append to one output file.** In the front matter both rewrote it to tidy up; the merge had
   to be rebuilt line by line. Give each reader its own file.
7. **Editorial notes must be comments.** Three Register fixes were set as inline `{{…}}` text that would have printed;
   grep the emitted file for any editorial marker outside `%` lines before installing.

### Udvalgte Stykker (2026-10-11): an Internet Archive layer, two type sizes, blind sheets with controls
`ebook-method/udvalgte-stykker/` (pilot pp. 1-44; 176 disagreements on 44 pp., 4 a page).  Lessons:
1. IA's ABBYY layer gives every word of a line the same box, but sometimes compresses the pitch between two lines to
   ~8 pt: cluster lines at 0.45 of the box height, not 0.6, or two lines interleave (p. 35).
2. The box of the word after a line-end hyphen is misplaced (reads as indented, even centred): such a line never starts
   a paragraph.  Check the draft's paragraph starts against tesseract's indents (miscsheets.py 'par' items).
3. Two type sizes on one page (an editor's introductions vs the excerpts): the layer's box HEIGHT separates them
   cleanly (12-13 vs 14-15 pt); the line pitch jitters too much.  Never let the note detector run on such pages
   (pagemap NOTE_PAGES), or an introduction at the foot of a page becomes a footnote.
4. A letterspaced word comes out of the layer as single letters: join the run, divide it into words by the corpus's
   word frequencies (rejecting divisions with stray one- or two-letter words), and confirm at the image.  Letterspacing
   gap threshold 0.15 here (spaced 0.21-0.33, roman <= 0.11), not om-aandsdannelse's 0.105.
5. Blind word crops are matched to checks by their KEY (sheets-<tag>.tsv), and every sheet carries two seeded controls
   (a word both readings share; for italics a line of certainly roman text), kept in controls-<tag>.tsv away from the
   readers; reads.py scores them.  Readers mark small capitals <sc>..</sc>: a case-only check so marked becomes SC.
6. After the readers (same day): 48/48 controls right, but a reader marking letterspacing line by line left short words
   (og, om, man, Tiid, have) outside the spans; at 450 dpi the whole passages were spaced.  Set multi-line spaced passages
   whole by POST patch, and check a reader's "doubt" notes on spacing at the image.  A blind reader's head transcription
   added a stop („47.)“) the print lacks: structure answers are a lead, not a reading of record.
7. IA's layer sets a line-initial one-letter word (i) after the line's first word: four on 44 pp., invisible to the word
   collation when the witness's „i“ aligns elsewhere.  prescreen.py 'lone' lists one-letter words whose neighbours differ
   from tesseract's.
8. After OPEN 0 the blind page check (5 pp.) found 0 word errors but 2 markup faults; the translator's 7 odd spots found 3
   readings both OCRs shared (a faint comma read as a stop, „han er“ joined, å for à) and 3 misprints.  Keep both passes.

### Om Betingelserne for en kraftig Villie (2026-10-12): a Google layer, and a later RESETTING as a finding aid
`ebook-method/betingelserne-villie/` (Nielsen 1874, 83 pp. antiqua; om-aandsdannelse's pipeline + udvalgte-stykker's sheets
with controls).  623 disagreements, OPEN 0 -- and then a word diff against the KB layer of the 1884 »Andet Oplag«, a
resetting of the same text (`diff84.py`), found what the collation had passed.  Lessons:
1. **The `dash+` rule (take tesseract's lone „—“ where the layer has nothing) is unsafe on Google's 600-ppi bitonal scans:**
   tesseract reads the wide space after a full stop as a dash.  10 of 36 such dashes here were not in the print.  Crop
   them, or check them against another witness, before accepting the rule.
2. **A tesseract-only guillemet is not proof of a mark either** (`guill` rule): 2 of 77 were specks (pp. 20, 80).
3. Google's layer writes the print's guillemets as `>>` `<<` and its long dash as U+2015: map them in draft.py, or
   check.py keeps raising them as MANUAL.
4. **A later resetting (or any other edition) is a cheap third witness for FINDING, never for deciding:** list where it
   differs from the collated text, discard its own OCR noise by the corpus vocabulary, and read the rest at the image
   (113 spots, 8 crop sheets in the main session).  It found the spurious dashes, specks read as stops by BOTH OCRs,
   closing guillemets both missed, words lost at the gutter (p. 40, supplied from 1884 and so marked), and six
   misprints both OCRs had normalised.  Never vote with it: a reprint corrects misprints, so a vote would erase them.
5. A layer stop between a word and a lower-case word, where tesseract has none, was a speck 10 of 10 times; a stop only
   tesseract has may be a broken COMMA -- send those to the image.
6. Words split across a page turn (`Trede%` / `\opage{14}lingens`) look like splits to a naive word diff: join them first.
7. After all that, the blind 3-page check still found one misprint both OCRs normalised („bebandle“, p. 27): about one
   in a thousand words is the floor this method leaves.

### Om Phantasiens Magt (2026-10-12): a pencil-marked copy, and what OPEN 0 still hid
`ebook-method/phantasiens-magt/` (Nielsen 1876, 91 pp. antiqua, KB scan + ABBYY layer; betingelserne-villie's pipeline).
569 disagreements, OPEN 0 after 385 blind crops -- and then five cheap sweeps found ~40 faults the collation had passed.
1. **Measure candidate rules on a blind pilot before turning them on.** Four rules (`aa`: tesseract's aa read an/ag;
   `witfault`/`layerfault2`: one OCR's word attested and the other's not; `margin`: pencil read as marks) were sampled
   15 a rule in the pilot: 8/8, 12/12, 8/8, 14/15.  The miss („fiint“, both OCRs wrong, lengths differing) gave the
   restriction (equal lengths only).  The rules then settled 41 checks for ~0 image cost.
2. **reads.py matches the reader's BOX with whitespace ignored**, so a check whose draft reading is a split word
   („e gen Erkj endelseskreds“) is settled T, and a W can drop a word the reader saw („kan Tro sættes“ -> „kan“, p. 44).
   Afterwards: (a) `check.py --splits` and a split sweep (adjacent tokens whose concatenation is a corpus word and one
   of which is not) -- 18 words here; (b) match every reader's whole LINE, letters only, against the text
   (`ebook-method/phantasiens-magt/linecheck.py`) -- found the lost „Tro“ and „Feltraabet“ (both OCRs: „Feltraahet“).
3. **A T decision can hide words the witness has and the draft lacks**: list T decisions whose witness side has attested
   words the draft side lacks (p. 41: the layer lost „Phantasie.“ at a line end; the reader's box showed only the line
   above).
4. **Pencil in the margin is read as an indent**: check every paragraph start against tesseract's line indent
   (`ebook-method/phantasiens-magt/parcheck.py`); 5 false breaks.  And draft.py now never starts a paragraph after a line ending in a hyphen.
5. **Widely spaced lines**: the layer's word boxes on a justified, loosely set line were clustered as two lines, or a
   word sent to the line below (pp. 21, 60, 66, 83, 85, 87, 89, 91).  `check.py --moved` lists them; read every one.
6. **The unknown-word list** (words in no other transcription) found 4 misprints both OCRs kept and specks both read as
   accents (Herregaården, havdé); render 600-dpi crops for single letters -- 300 dpi could not tell „spørgsmal“ from
   „spørgsmål“.
7. **oefix.py's list maps „stode“ -> „støde“**, but „stode“ (stood) is a word: do not run it blind.
8. Cost: pilot 85k (70 crops), 5 readers 490k (393 crops: 1.25k a crop), page check 76k, 4 translators 450k.

### Gamle og nye Propheter (2026-10-12): OPEN 0, and the translators still found 21 faults
`ebook-method/gamle-nye-profeter/` (Nielsen 1878, 112 pp. antiqua, KB scan 250 ppi + ABBYY layer; phantasiens-magt's
pipeline, its rules re-measured on this book's own blind pilot).  518 disagreements, OPEN 0 after 352 blind crops.  Lessons:
1. **reads.py takes a sheet's KIND from the first letter of its tag**: a pilot tagged `p1` is read as nothing (0 decisions,
   every control "missed").  Tag word pilots `b0`.
2. **Turn on `LAYER_SPLITS` for a KB layer, antiqua too**: check.py's 'split/noise' settlement had passed five words the
   layer split („Ny rationali sme“, „F orsøg“, „gamm el“); `--splits` lists them, LAYER_SPLITS makes them checks.
3. **KB's layer reads V as a backslash** (`\iser`, `\idens`, `\idenskaben`): check.py strips `\idens` as a command, so
   the word vanishes from the collation and a W decision inserts the witness's word beside the garbage.  Map it in
   draft.py (a backslash before a lower-case letter, at a word start); grep every draft for `\\[a-z]+` that is no command.
4. **Letterspacing by box WIDTH** (`spacedwidth.py`) where the gap measure (spacedsheets.py) does not separate (here a
   250-ppi scan: 3955 gap candidates): fit a width per character over tesseract's boxes; spaced words run 1.2-1.3 times
   their predicted width, unspaced 99 % <= 1.07.  69 lines, 55 runs.  spaced.tsv rows apply IN ORDER: a row's "before"
   that holds an earlier row's word must hold it as `\emph{word}`; a run after a glued „ or a repeated phrase goes in POST.
5. **After --apply, every `=text` decision re-keys** (the witness still differs from the new text): add T decisions for
   the applied keys, or OPEN is not 0 on the built file.
6. **The translators' odd spots found 21 real faults after OPEN 0** (47 listed): specks that BOTH OCRs read as stops,
   commas, hyphens or apostrophes (`fremmer-det`, `dette.Eiendommelige`, `dem .i`), „ read as a comma, ? read as :, „Gud
   er“ run together, the pronoun I read as 1 -- and a reader's "damaged" note that reads.py's DOUBT pattern did not catch
   (now it does), so the witness's „Fo: ening“ was taken.  On a KB layer, punctuation where both OCRs agree is the
   residue: the translation pass is the cheapest net for it.
7. check.py --italics renders its pages in ONE pdftoppm batch, which can outrun a device call and leaves nothing named:
   render the pages in parallel first (`pdftoppm -r 290 … NAME-pN-290.png`), then the slant pass takes seconds.
8. Cost: pilot 108k (74 crops + 10 head crops + 15 lines), 5 readers ~500k (278 crops + 54 lines), page check 86k,
   6 translators ~670k.

### Om Liv og Haab (2026-10-12): a free third OCR, and what reads.py and --moved still hid
`ebook-method/liv-og-haab/` (Nielsen 1875, 103 pp. antiqua, Google/NYPL scan 600 ppi bitonal + Google layer;
gamle-nye-profeter's pipeline).  371 disagreements, OPEN 0 after 218 blind crops -- then the sweeps found ~25 faults.
1. **A Google Books scan is often on the Internet Archive too (`…goog` items), with an ABBYY OCR of the SAME images**
   (`_djvu.xml`, word boxes): a free third reading (`abbyy.py` maps its boxes to PDF points per page).  Measured on the
   blind pilot it is right 11/12 where it agrees with the layer but only 7/10 where it agrees with tesseract (it too reads
   specks as stops): use it to NARROW rules (`dash+` only where it has the dash, `numbers` only where it has no mark),
   never to vote.
2. **reads.py settled T on five words whose opening „ BOTH OCRs had lost** (draft „bedste“, tesseract „,bedste“, reader
   „„bedste“): the match used context not adjacent to the mark.  Guard added (a T whose word the box shows only with other
   marks goes by hand).  And it settled W on „skabelig“ where the reader's box was the second half of „viden-|skabelig“,
   deleting „viden“: list every W that SHORTENS the draft and every T where the witness has more letters, and read them.
3. **`check.py --moved` hides the layer's line-order faults**: of 9 MOVED pairs, 4 were lines Google's layer had put a line
   up or down (pp. 3, 86, 94), one with a false paragraph break.  Read every pair against tesseract's line order.
4. **A per-paragraph quote-balance sweep** („ against “) found the five lost „ above and a speck read as “ (p. 35).
5. Google's layer writes the print's „ as `99`, as Arabic `و و`, or as `,,`: draft.py maps all three.
6. On a 600-ppi bitonal scan the GAP measure separates letterspacing well (spaced 0.10-0.17, 99.5 % of words < 0.067:
   `spacedlines.py`); spacedwidth.py's width ratio was noise there.  The l-reader still missed whole spaced SENTENCES
   („det Personlige er i Himlen og paa Jorden høiere …“) and marked only the long words: read the doubts and the lines the
   measure flags but the reader left roman in the main session.
7. A leaf folded in the scanner (p. 17: the left third of each line distorted, both OCRs garbage): set the page whole from
   one crop by PATCH, and decide its checks T.
8. After OPEN 0 the page check (2 in 764 words) and the translators (13 real faults) still found specks BOTH OCRs read as
   marks, a ring (påa), „dog“ read „dag“: on a bitonal scan this residue is ~1 per 1000 words, and the translation pass
   remains the cheapest net.
9. Cost: pilot 122k (91 crops), 5 readers ~457k (127 crops + 44 spacing lines + headings), page check 87k, 6 translators
   ~595k; ~100 main-session line crops.

### Om Samfundets Vilkaar (2026-10-12): page-end hyphens, a pilot by class, and broken e's both OCRs read as c
`ebook-method/om-samfundets-vilkaar/` (Nielsen 1877, 103 pp. antiqua, Google/Harvard scan 600 ppi bitonal + Google layer;
liv-og-haab's pipeline).  449 disagreements, OPEN 0 after 255 blind crops -- then the sweeps and the translators found ~25.
1. **Google's layer loses the hyphen of a word broken at a PAGE end** (15 pages here: „Fleer“ / „talsmagten“), so the
   draft splits the word and the collation sees one word against two.  tesseract keeps the hyphen: draft.py now opens the
   word when tesseract's last text line on the page has it (the Digitized-by-Google watermark excluded).  Look for it on
   any Google layer: a page whose last word + the next page's first word is a corpus word.
2. **Sample the pilot BY CLASS** (`rules.py --classify [N SEED]`): every open check gets the candidate rule it would meet
   with all rules on, and up to N a class go to the pilot (.parts/pilot-keys.txt -> `sheets.py --keys`).  One pilot then
   measures every rule: here 13 rules 100 %, two narrowed by their single miss, one (the word-division rule) 3/8 and off.
3. **On pages with several insertions of the same mark** (`>—`, `>—#2` …) check.py --apply places only some per pass and
   the rest are renumbered: run `--apply` twice (the rebuild chain now does), or `--unapplied` lists them.
4. **=text and POST changes re-key** (gamle-nye-profeter lesson 5): after the notes are moved to their marks by POST, the
   collation sees the note text at the mark; add T decisions for those keys.
5. **The unknown-word sweep found what the collation cannot**: broken e's that BOTH OCRs read as c („Sclvbcherskelse“,
   „elcktrisk“), a broken n read as r, thin word spaces („afDannelsestrin“), and ten real misprints.  Read every unknown
   word that is not plainly a compound or a name; a printer's defect gets its letter supplied and a `% defect:` comment.
6. **The l-readers missed whole letterspaced sentences** again („hvor meget kan man byde et Folk, før det gjør Oprør“,
   „i den hellige Treenigheds Navn“): read every l-sheet in the main session (seven sheets, ~15k tokens) and crop the
   lines next to every spaced line with a few lines of context (`z300ctx`-style crops).
7. A `\lecture{I.} {Title}` macro with two arguments must end in `\ignorespaces`, and the `\opage` go on the next line:
   with `%\n` check.py glues the title's last word to the first word of the text.
8. The translators' 39 odd spots found 8 real faults after OPEN 0 (specks both OCRs read as stops, a dash the collation
   had doubled, „IIdens“ read „Ildens“, a broken m) and 7 misprints.  The translation pass remains the cheapest last net.
9. Cost: pilot ~115k (102 crops), 5 readers ~450k (153 crops, 97 spacing lines, 21 heading crops, 2 front pages), page
   check ~82k, 6 translators ~575k; ~70 main-session crops.

### Folkelige Foredrag (2026-10-12/13): a microfilm, two pages a frame, and an ABBYY layer that is not a third reading
`ebook-method/folkelige-foredrag/` (Nielsen 1875, 164 pp. antiqua; HathiTrust's PDF of Columbia's microfilm, scanned by the
Internet Archive; om-samfundets-vilkaar's pipeline).  1018 disagreements, OPEN 0 after 699 blind crops -- then the sweeps
and the translators found ~20.  Lessons:
1. **A two-up scan: derive a one-page-a-page PDF, change nothing downstream.**  `split.py` gives each frame two page
   copies whose MediaBox = CropBox is one half of the frame's image (gutter = the widest x-gap in the layer's word boxes);
   poppler clips text and renders to the box, so draft.py, check.py, ocr.py and every sheet script run unchanged through
   `pagemap.scan_path()`.  Map the printed pages from the folios of the layer, not by arithmetic: this film repeats a
   frame (pp. 130-131).
2. **Check whether a "second OCR" is independent before counting on it.**  HathiTrust's layer for an Internet Archive
   item IS the IA's ABBYY text (compare the djvu.txt of a page): no free third reading here, unlike liv-og-haab.
3. **The IA's ABBYY on grey film has its own fault classes**, each a cheap rule or draft.py mapping once seen: `^` for a
   rejected glyph, „see I“ for „see!“, y read `}'`, „ read `..` `.,` `,.`, “ read `''`, M read `]\I` or `:[`; split
   words at a kerned j („gj ælder“) and stray apostrophes.  The pilot measured `caret`, `bang`, `layerfault3`, and three
   narrow parts of `seam` (joinW, aposW, splitW) 7/8-8/8.
4. **The gap measure for letterspacing is noise on grey film** (99 % of words at 0.106: 439 candidate lines); the WIDTH
   ratio (spacedwidth.py) gave 110 lines, fed to spacedlines.py's sheets with its roman controls.  A sample of the wide
   words the readers left roman (12 crops) held no spaced word.
5. **Sweeps that caught what OPEN 0 hid:** the reader-LINE sweep (linecheck.py: a T decision had accepted „hedens“ where
   the layer had lost „Fri-“ inside the page); the W-shortens list („op-|dage“ cut to „dage“); quote balance (a speck
   read as “); and the translators' odd spots: four f's whose head did not ink, read t by BOTH OCRs (Folketriheden,
   tornemme, Utorstand, tor) -- first taken for misprints, then seen as one defective sort.  Look for a recurring broken
   sort before marking „misprints“ one by one.
6. **Removing a junk line can leave a blank line before a page marker** (a false paragraph break at the turn): tr_build.py's
   per-page paragraph count shows it; also check `\n\n% --- p.` where the next page opens lower-case.
7. **A W decision takes tesseract's marks (WMARKS): its straight quotes and its printer's spaces before ; ? came in.**
   draft.py --post now maps straight quotes to „ “ and drops the space before ; : ? ! in the body.
8. Cost: pilot 142k (122 crops), ten word readers 1,035k (577 crops: ~1.45k a crop on these larger grey crops), spacing
   212k, structure reader 107k, page check 91k, ten translators 963k: ~2.55M (estimated 2.1M).

### For Ide og Virkelighed 1869 (2026-10-13): five journal essays in ONE pipeline, and the IA layer's squeezed line starts
`ebook-method/for-idee-1869/` (Nielsen's five essays in one journal volume, 189 pp. antiqua; the Internet Archive's scan of
the Toronto copy, 400 ppi colour, the IA's ABBYY layer; folkelige-foredrag's pipeline).  1132 disagreements, OPEN 0 after
686 blind crops -- then the sweeps and the translators found ~25.  Lessons:
1. **Several works in one volume: one pipeline, one collation, then cut.**  pagemap.RANGES/ESSAYS and SKIP give check.py the
   Nielsen pages only; the draft is a combined working file (pagemap.TEXFILE under `.parts/`, which `make` ignores);
   `split5.py` cuts it into the five transcription.tex files (headings, signature, PRINTED AS IS records per essay).  One
   pilot then measures the rules for all five, and the sheets are filled across essays.  **The cut files must never enter
   the vocabulary that attests words** (check.py, rules.py, the sweeps): pagemap.OWN lists them, and check.py now honours it.
2. **Running heads with the title and a garbled folio** („To Slavs Undervisning. 3 OB“, „Om Siudsformerkelse. 705“): HEAD
   and FOOT regexes must tolerate letters in the folio and garbled titles; check the draft for title strings mid-text.
3. **The IA layer squeezes the first boxes of a line**: a lone „i“ gets a box inside the next word's (sorted after it:
   „det i Store“), and a paragraph's short last line reads as centred (17 false headings).  draft.py now moves the one-letter
   word before the word that holds its box, and never makes a heading of a line that opens lower-case or follows a hyphen.
4. **The IA layer's own glyph faults here**: x\ for A, \ for V/v inside a word (check.py would drop „\iderne“ as a command),
   fF for the ff ligature, { for (.  Map them in draft.py's emit_line BEFORE \dots{} is inserted (a brace map run after it
   turned every ellipsis into „\dots()“).
5. **reads.py matches the reader's box with whitespace ignored, and the reader's superscripts as letters**: a W took
   „derf.“ for „der f.“, dropped a note mark („Forsøget¹).“ -> „Forsøget“) and a closing «.  Run the W-shortens / T-longer
   list against the readers' boxes before the build (as liv-og-haab lesson 2 says) -- it found all three.
6. **Notes collated where they stand, then moved by POST** (draft.py --post, patches.NOTES: page, mark, start, and a run-over
   page): the move leaves a blank line before the next page marker -- a false paragraph break in mid-sentence (4 pages).
   draft.py --post now drops it when the next page opens lower-case.
7. **f's whose head did not ink, read t by BOTH OCRs, again** (tire, tik, tin, tinde, at for af: pp. 21-441), and blind
   readers read them t too: a recurring defective sort in this volume's types.  The translators found them.
8. **This print closes quotations with » as often as with «** (eight sites read at the image): a quote-balance sweep is
   noise here; read the » that stand after a word instead.
9. Cost: pilot 130k (107 crops), word readers ~760k (675 crops), spacing 272k (163 lines), structure + notes 187k, page check
   91k, twelve translators ~1.17M: ~2.6M (estimated 2.3M).

### Logik og Psychologie 1871–72 (2026-10-13): a KB scan holding two books, and a page reader who corrects the print
`ebook-method/logik-og-psychologie-1871/` (scharling-apologie's no-layer Fraktur pipeline, 8 pp.).
- **Look at what the PDF holds before mapping pages.**  KB's 263-page PDF for an "8 s." record is mostly another book
  (Funke's *Psychologie*, 1799, PDF 2-247); Nielsen's print is PDF 248-263.  A 12-dpi contact sheet of every page (one
  image, ~1.5k tokens) and tesseract on two pages identified both.  `pagemap.LAYER_PDFS` limits `ocr.py MODEL=layer` to
  the pages wanted (the others get blank layer pages, so PDF numbering holds).
- **No footnotes, but the draft found four**: the last line of a page, set off by a larger gap, passed draft.py's note
  test.  Set `NO_NOTES = True` once the page reader confirms there are none.
- **A full page reading after OPEN 0 still found 29 faults** in 1908 words that both tesseract models shared (Fraktur k
  read l, f, st or t: iffe, Produft, metaphysist, forstjellige; ø read o: Folge; three stops read as commas).  For a short
  Fraktur print with no layer, the full blind page check is the step that makes the text right, not a formality.
- **The reader is not an authority on grammar.**  The page reader wrote „Menneskets“ for the print's „Som Modus af
  Tænkningens Attribut er Mennesket / Aand“ (= man is mind), and the main session nearly marked the print a misprint.
  Read the sentence before marking PRINTED AS IS.
- **Short letterspaced words** (Aand, Lys) were left plain by the page reader where their partners (Legeme, Tyngde)
  were marked: check the short partner of every spaced pair on a line crop.
- Cost for 8 pp.: crop reader 89k, page reader 113k, translation inline.

### Propædeutik og Logik 1868–69 (2026-10-13): a "Cursus" volume made of earlier books' sheets
`ebook-method/propaedeutik-1868/`.  Nielsen's annual course books reuse the sheets of his earlier books; this 456-page
volume holds only ~16 new pages.  Before planning any transcription of a Nielsen Cursus (or any composite volume):
1. **Map content first** (`map1868.py`: 12-letter runs of each page's layer against every transcription in the repo),
   then **page for page** (`concord.py`: coverage both ways against the old page of the same number).
2. **Same text is not same setting; test the setting** (`setting.py`): compare the two Google layers' sequences of
   line-end words.  Same setting gives 80–100 % with equal line counts (lower only on formula pages or a poor scan);
   a resetting gives 0–10 % even where the words are the same.  Signature lines are a quick confirmation (here the
   GL II sheets still read »Grundideernes Logik. II«).
3. **The earlier book's errata are a free test for corrections**: look up each erratum's site in the new layer.  Here
   none was corrected, so the shared pages are unaltered and the earlier transcription serves.
4. **Seams are where new text hides**: a seam page can be partly old type and partly new (p. 81, 89), take up a line
   from the next page (p. 263), or reset old text to new line breaks (p. 264).  Read the seam pages' line ends one by one.
5. Page-level coverage misleads at book level: map1868.py's 64 % for the Oversigt against *Grundideernes Logik i kort
   Begreb* was common phrases; page-by-page it is 1–3 %.

6. **„Same setting“ is not „unaltered“.**  Two small changes turned up only because these pages were read anyway: a
   note line reset for 1868 (p. 263: „faae“ -> „faaet“, and a syllable lost: „Uende-/hedsbegrebet“) and a full stop
   added (p. 81).  The line-end test cannot see a reset of one line inside a page; changes.py (three-way word diff)
   finds only changes OCR does not blur.  Where the shared pages matter, read them; where they do not, say so.
7. **The crop readers' line-break forms leak in.**  readsbox.py's `read` rule takes the reader's text, and a reader
   writes a word divided over two boxed lines as „Gjen-standen“, „Qva-litet“, „sær-/ligt“: 7 such forms here, found
   only by the page check.  After readsbox --write, grep the text for `[a-zæøå]-[a-zæøå]` and `-/`.
8. **A word-division difference is invisible to pagecheck.py compare** (it skips diffs that vanish without spaces):
   „eren“ for „er en“ survived.  Run the division-only listing too (this session: a short script over read_streams/
   tokens; 1 real fault in 10 listed).
9. **Paragraphs: let the page reader's ¶ decide.**  The draft's INDENT_MAX found 26 of 47 paragraph starts; a script
   comparing the reader's ¶ lines with the transcription's paragraphs listed the 21 missing and 2 false ones
   (finish.py PARAS / JOINS).

### For Idee og Virkelighed 1870–73 (2026-10-13): six NB volumes, one working PDF, and rules calibrated on a known text
`ebook-method/for-idee-1870-73/` (eight Nielsen essays, 231 pp., Nasjonalbiblioteket scans, no text layer).  Set-up lessons:
1. **NB's ALTO is in "mm10" at a 400-dpi convention**, whatever the image's resolution: on these 300-dpi canvases 1 unit =
   400/254 px.  The page image nbfetch.py binds IS NB's canvas (1758-1893 px wide, varying by volume): no fit needed.
2. **Works spread over several volumes: bind only their pages into ONE working PDF with the ALTO as its layer**
   (combine.py, qpdf + reportlab), and number pages VIRTUALLY (1000 x volume + page) where the volumes' numbers collide;
   draft.py and check.py then run unchanged, and the split script turns V back into the printed page.
3. **pdftoppm takes ~10 s a page on a 300 MB image-only PDF; pdfimages -j takes 0.05 s.**  Where the PDF binds each page as
   one image at the render resolution, make the renders from the extracted image.
4. **Calibrate the candidate rules by script on a text already read at the image, from the same volume or type**, before
   the blind pilot: run the whole pipeline on it (here FIV_CAL=1 on Darwinismen, Bind 8 pp. 449-459) and score each rule's
   decision against the known transcription (calibrate.py).  It found three new NB rules (oinit: D/O/U/G for Ø, lih, Il),
   measured 15 candidates at 0 errors, and killed one ('seam', 3/11) without a crop.  Context matching must keep guillemet
   direction and ignore the space a stripped \emph{ leaves after », or right decisions score as unscorable.
5. **NB's ALTO reads the opening » as «** (122 times here) and breaks LETTERSPACED words into pieces („Lo kalk raften“):
   the pieces are the letterspacing candidates.  It also sets lower-case ø for a capital Ø (ødelæggelsens).
6. **Confirm the catalog's page ranges from the scan** (signature, next article's title, the volume's Indhold): Filosofi og
   sund Menneskeforstand ends on p. 404, not 406.
7. The device VM's home disk can be full while /tmp is not: `tempfile.mkdtemp()` follows $TMPDIR into the full disk; pass
   `dir='/tmp'`.

8. **Calibrate the letterspacing detector on the word readers' own <sp> marks** (spaced.py --calibrate): the words the
   blind b-readers marked spaced, each unique on its page, against the other words of their lines.  On these NB scans GAP
   and WIDTH each caught ~70-85 %; their union at GAP 0.08 / WIDTH 1.12 gave 361 lines for 231 pp.
9. **Letterspacing read line by line needs SPAN MERGING**: a spaced run crosses line ends and divides words („Hi-“ /
   „storie“); draft.py --post now lets a span's first/last piece match the whole joined word, finds every match first,
   and merges touching intervals into one \emph{} (never across a blank line).  Each row also carries two words AFTER, or a
   short word („skal“, „Magt“) matches twice on its page.
10. **A reader's output can be silently short**: one l-reader's file ended two sheets early (182 of 199 lines) although
   its report said 199.  Count the IDs in every reader file against the sheet index before reading the results.
11. **Notes: compare the built notes with a whole-note reading by script** (notecmp.py): after the word collation (OPEN 0
   on the notes too) 9 differences in 30 notes, among them a word wrong in both OCRs („Treeslære“ for „Troeslære“).
12. **Both OCRs run words together in tight and letterspaced lines** (afTydeus, ranedeHimlensNøgler): after OPEN 0 grep the
   text for lower-case + capital inside a token, and run the unknown-word sweep; on 231 pp. 7 + 4 such faults, 7 misprints.
13. **oefix.py's lexicon has „stode“ -> „støde“**, but „stode“ is the old past plural of „staae“ (they stood): check
   every oefix change in context.
14. **The translation found what the page check missed** (2026-10-14): 9 false paragraph breaks at page turns (the notes
   moved away from a page's foot leave a blank line; the 1869 rule joined only when the next page opens lower-case, but
   Danish nouns are capitalised -- join whenever the line before the turn ends without a stop, and check sentence-end
   breaks against ALTO's indent of the next page's first line); compound hyphens printed spaced („For - Historie“) taken
   as „For- Historie“; specks beside words taken for ‘ “ « or ~; a lost „I“ before a capital.  13 faults + 9 breaks in
   58k words: a sampled page check of 1965 words cannot see faults this rare -- the translators' odd spots can.

### Moderne Filosofer 1904 (2026-10-14): a Google scan with an OCR e-book as third witness
`ebook-method/moderne-filosoffer/` (Høffding, X + 157 pp., Google layer, SAGA e-book of the same 1904 text).  Lessons:
1. **An e-book made by OCR shares faults with the layer**: audit its votes FOR the layer's reading (78 at random: 1 wrong,
   „Sandbed“), and say in the header how many unaudited faults that implies.  It votes and finds; never the base.
2. **Measure what the e-book's markup means before using it**: its `underline-rw` spans looked like letterspacing and
   were not (letter gaps measured by spacecmp.py, then at the image).  Letterspacing here was only in the Noter.
3. **Google's layer moves a dash and the words after it onto the line above** (12 places): the word collation cannot see
   order.  Compare paragraph starts with the e-book (parcmp.py) and read such lines at the image.
4. **A stray `>` or `<` in the draft breaks check.py's `page|tex>witness` keys**: map lone ones to guillemets in draft.py,
   except on pages with formulas.
5. **The seam rule settles digit disagreements blind** (years, note labels): keep it OFF where numerals matter.
6. **Regex patches with optional groups**: C() adds an optional `\opage{}` group per centred line, so three C() blocks have
   six groups; a wrong back-reference silently made an empty heading (`\chapterhead{I.}{}`).  After a rebuild grep the
   built text for empty `{}` arguments of the heading macros.
7. **The translators' odd spots again found faults the page check could not** (10 after a check at ~1 per 1000 words):
   a Greek label read as Latin, a word split across a note boundary, two notes run together, a lost line.
8. **Compiling on the device VM when its home disk is full**: mktexpk writes to $HOME and fails; `export TMPDIR=/tmp
   TEXMFVAR=/tmp/texmfvar` and add `\usepackage{lmodern}` to the /tmp copy.

### Oplevelse og Tydning 1918 (2026-10-14): an NB scan with footnotes and an e-book; rules calibrated on Etik
`ebook-method/oplevelse-og-tydning/` (Høffding, 238 pp., NB scan without a layer, SAGA e-book of the same text).  Lessons:
1. **Before the first run of a copied model script, grep it for the model's book path** (`grep -n "'etik'\|moderne" *.py`):
   etik's draft.py, copied, overwrote `texts/hoeffding/etik/transcription.tex` on its first `--emit` (restored from its
   automatic `.bak.<date>-draft`).  Take paths from `pagemap.BOOKDIR`, never a literal.
2. **nb_scan.py build: put each ALTO line on its MEDIAN word bottom, not the lowest.**  A two-line initial (the „D“ of a
   chapter's first word) put the whole first line on the second line's baseline, and draft.py merged the two lines word by
   word („Det en er betydningsfuld af stor …“).  Grep the draft's first lines after every heading.
3. **Footnotes with a hanging indent** (label flush, continuation ~17 pt in) invert etik's grouping; measure the three
   left edges (text, note first line, note continuation) on two pages before trusting the note count.  Star marks
   (*) **) ***)): k = the number of stars; `\thefootnote` prints them.
4. **check.py moves footnotes to the page's foot without spaces**, so a note's last word glued to the next page's first
   („1911).mig,“: 105 false checks here) and a word divided across the turn glued to the note („pludSmlgn.“).  pagemap
   `NOTE_SPACE = True` (opt-in, so other books' keys do not change) puts a space before and after each moved note.
5. **Calibrate the rules on a sibling book's image decisions when no page of this book has been read**: Etik (the same NB
   OCR and the same SAGA e-book family) was redrafted in /tmp by a copy of its draft.py, collated pp. 1–150, and rules.py
   (`OOT_CAL=…`) scored against Etik's 204 checks decided at the image (e-book vote 35/37, the two wrong ones marks only).
   A rule that ignores spaces („mark“) hid a draft fault that no calibration on another book could show: read a random
   sample of each rule's own decisions in this book too.
6. **Audit the e-book vote at the image** (here 26 of its decisions mixed into the blind sheets): 1 wrong
   („Bakehantismen“, an OCR fault the e-book shared).  Then re-read every e-book decision whose word occurs nowhere else in
   the corpus.
7. **Read the footnotes whole** (notesheets.py, 300-dpi strips): both OCRs had dropped the same French accents (Térèse,
   Genève, très), which no collation can flag; 62 word differences, mended through postfix.tsv.
8. **The translators' odd spots go back to the image** (`sheets.py --extra`): 7 more faults where both OCRs agreed.
   Blind readers there normalised two misprinted names (Cécilie → Cécile, Eckchardt → Eckhardt) and said „doubt“: a
   doubted name gets a 600-dpi look (wordcrop.py) before any change.
9. **Never run check.py on the finished transcription** (without a fresh draft): the POST patches show as new checks
   and checks.tsv is overwritten; rebuild.sh restores it.

### Den engelske Philosophi i vor Tid 1874 (2026-10-15): two copies read twice, and what the translators still found
`ebook-method/engelske-philosophi/` (Høffding, [IV] + 190 pp., antiqua; Internet Archive: Toronto Scribe scan (the Archive's own
PDF, its layer = the Archive's ABBYY) and Google's Oxford copy (ABBYY bound by abbyy_scan.py); no e-book).  Lessons:
1. **Choose the working copy by measurement**: the share of layer words unattested in the corpus (3.2% vs 7.3%) and a
   crop of the same lines side by side.  An Internet Archive Scribe PDF can be used as it is: its text layer is the
   ABBYY reading word for word (compare it with `_abbyy.gz`, page k of the ABBYY = PDF page k-1).
2. **Read the second copy twice** (its ABBYY layer and tesseract on its images, `oxocr.py`) and let the two vote together
   (`vote2.py`): Oxford-ABBYY alone voting, as tydskland's umn rule, settled few checks, because its context rarely matched
   exactly.  But two tesseract readings agreeing are ONE engine twice (both read høieste as højeste, føies as føles): a lone
   tesseract vote for the witness counts only for a non-word in the draft.  And no vote may drop a word or import a mark the
   reader does not see (audit: „den:“ → „den”“).
3. **Lines by the line's MEAN centre**, not its first word's: a word with a descender opened a line 3.5 pt above its
   neighbour and the next word stood alone as a false centred heading (draft.py cluster).
4. **This print closes quotations both ways** (»...« and »...», in the text; „...“ in the notes): ten crops all showed »...»
   and a class rule was written on them; a later sweep of the remaining « found »...« on pp. 11-17, 175, 180.  A class rule
   on quote direction needs crops from across the book.  Where ABBYY and tesseract differ on the direction, tesseract was
   right in the audit; where they agree, the print was too.
5. **check.py's split/noise rule kept ABBYY's inner spaces** (Kollision stilfælde, Fors kjel): run `--splits` on a fresh
   draft and mend by POST.  Never run check.py (--moved, --splits, --italics) on the finished file.
6. **Run-over notes the draft cannot see**: a note whose last line ends without a stop (`theolo-`) runs over; its
   continuation on the next page was taken for TEXT (p. 155), and in the other direction the TEXT of a page was taken into
   the run-over (p. 162).  Read every page's note block whole (notesheets.py with ONLYPAGES for the continuation pages),
   compare word counts, and set the notes from the reading (NOTESET; noteset.py's join must escape % BEFORE it joins).
   Three one-line notes whose labels the OCRs lost (`)`, `•)`) were set as text: grep the draft for bare `\footnotemark`.
7. **Letterspacing by WIDTH, not gaps**, on a grey (Scribe) image: the gap measure never finds white columns between the
   letters of a spaced short word („D e t“, „e n d n u“, found by the page check).  Fit a width per character over the book
   by least squares and flag words > 1.22 x their predicted width (widthsheets.py): 180 candidates, 38 spans.
8. **The translators' odd spots found 71 faults after OPEN 0** (and 53 misprints): non-words both OCRs and the Oxford copy
   shared (Philosopbiens, Vexelvirkningeu, gjennnem), specks read as stops, I read as 1, a kj lost.  An unattested-word
   sweep of the collated text BEFORE the translators would have found most of them more cheaply; do it in every book.
9. **Cut translation parts at a paragraph start where you can**; where you cannot, the build must join the parts without a
   blank line (tr_parts.py now looks at the Danish).  Several parts here began in mid-word.

### Tilskueren 1886-90 (2026-10-15): four journal pieces, a voter that shares the draft's faults, and letterspacing measured
`ebook-method/tilskueren-1886-90/` (Høffding, Om Religionsfrihed + the three Nietzsche-debate pieces, 76 pp., Google scans of
the Harvard copies with the Archive's ABBYY layer).  Lessons:
1. **Fetch only the leaves you need**: an Archive item's `_jp2.zip` (1.3 GB) serves single files at
   `download/ID/ID_jp2.zip/ID_jp2%2FID_NNNN.jp2`; NNNN = ABBYY page index (0-based) = scan leaf.  ia_extract.py.
2. **Project Runeberg's pages may be the same scan** (file number = leaf - 1): then its OCR is a third READING, not a
   second copy, and it shares faults with ABBYY (bg/og, kim/kun, bar/har, Anstrengelser/Anstrængelser).  A vote FOR the
   draft must never make a non-word, and even so 7 of ~80 letter-changing votes were wrong: audit the class at the image.
3. **An e-text is a finding aid, never a correction**: one word taken from it on a partial crop (Tale-/maader) was
   wrong; the page check caught it (the print: Talemaaler).  Every finding-aid spot must be read whole at the image.
4. **Letterspacing: measure it.**  Two blind line rounds (256 + 134 lines) agreed on only 40 of 134 doubtful lines and
   missed planted controls at the ends of runs.  The median white run between the letters of a word (tesseract boxes,
   300 dpi) is bimodal over the whole text (1-4 px roman, 6-8 px spaced); threshold 5 px, isolated words need every gap
   wide (spacemeasure.py), then apply after the collation by letters only (spaceapply.py).  Check at zooms; residual
   ~2-3 errors per 1000 words, mostly the ends of runs in wide-set lines.  Do this BEFORE paying for line readers.
5. **Section numerals and short lines can vanish from the draft** (I. under a title; III. mid-page): compare the numeral
   sequence per piece with a structure reading.  A sheet signature with a star („10*“) merges into the last text line:
   drop tokens `\d{1,2}\*` in draft.py.
6. **The translators' odd spots again found 5 faults** (two lost stops, three specks) after OPEN 0 and a page check.

### Det nittende Aarhundrede and Nær og Fjern 1875-76 (2026-10-15): a tesseract layer, Fraktur columns, specks
`ebook-method/hoeffding-1875-76/` (Høffding, four journal pieces, ~17,100 words; the Archive's Scribe scans of the Illinois
copies, a Harvard copy's ABBYY as voter; Nær og Fjern a private Fraktur scan, two columns, one copy).  Lessons:
1. **Measure which OCR is the draft.**  An Internet Archive item may carry only the Archive's own tesseract (hOCR), and
   ours (tessdata_best, 300 dpi) was much better (words unmatched by the other copy's ABBYY: 3.0% against 9.5%; the
   Archive's dan model reads aa as åa).  Swap the roles (layer.py): our reading becomes the layer, theirs the witness.
   Two tesseracts share faults (German ä read å by both): the other copy's ABBYY must vote and the sweeps must follow.
2. **A two-column page as two virtual pages**: copy the page once per column and set MediaBox/CropBox to the column
   (combine.py, pagemap.COLS); pdftotext and pdftoppm keep to the box, so draft.py and check.py need no change.  Open each
   source page once per column, or the copies are one object and the last box wins.
3. **Proofreading whole Fraktur columns against the draft** (PROOF-BRIEF.md: corrections as FIND/REPLACE rows) found 171
   faults but missed ſom/fom, Teænker, ſtaaer: an unattested-word sweep and a long-s/ø sweep at zooms found the rest.  A
   reader's row that holds a planted control may ALSO hold a real fix (a stop): never drop such a row whole.
4. **Specks read as stops by both OCRs** (Illinois copies): the page check found 4 in 2 pages; a sweep of the marks the
   other copy lacks mid-sentence (specksweep.py) found 16 more, all specks at the zoom.  Run it on any Archive colour scan.
5. **Quotation marks by class** where the readings show one style: both OCRs read „ as , or ,, and “ as ' ” " »; the
   blind crops, notes and structure readings all showed „...“, so quotes.py sets them outside the notes.
6. **The translators' odd spots again found ~22 faults** after OPEN 0 and the sweeps (a footnote left in the body where
   the draft missed the note zone, a running head, ɔ: read as 2:, two paragraph breaks at page turns).

### Filosofien i Sverig, Om Pessimismen, the Böhme review 1879-82 (2026-10-15): ö beside ø, a third reading that votes wrong
`ebook-method/hoeffding-1879-82/` (Høffding, three pieces, ~28,100 words; NB scans with ABBYY ALTO, Runeberg's OCR of the same
NB images, an Archive Ude og Hjemme scan in two columns).  Lessons:
1. **A Danish print may set ö beside ø** (Nordisk tidskrift: göre, större beside første).  Read it with dan+swe
   (swe.traineddata), and switch off check.py's glyph-fault pairs ø/o, o/ö, a/ä for the book (pagemap.FAULT_OFF, the hook
   in collate/check.py), or the collation settles real ö's as faults unseen.  NB's ALTO DROPS umlauts (HOFFDING) and reads
   ö as b/d: an ALTO-only umlaut difference is no evidence.
2. **Audit every voter class at the image before trusting it, even after Tilskueren's warning**: Runeberg's votes (a third
   OCR of the same images) were wrong 5 times in 30 audited; all 183 were withdrawn and re-read blind.  The audit costs ~30
   crops; skipping it would have put ~30 wrong words in the text.
3. **Notes at their marks**: when the draft sets notes at page ends, place them from a NOTEMARKS table (noteplace.py) and drop
   the newline before a note that begins a line, or each page turn after a note becomes a false paragraph break (the
   translators found four).  A note mark read with no note under it means the note sheet clipped the foot: zoom.
4. **A build chain must not pipe a step into grep/head**: under sh a pipe's status is the last command's, and a failing
   proofapply.py --final was hidden for one rebuild.  Write logs to files and filter after (rebuild.sh).
5. **A rule written for one source must be fenced off the others**: the layerfault rule decided checks on the Archive pages
   too (Bøhme for Böhme).  rules.py now skips pages proofread whole (pagemap.WHOLE).

### Mindre Arbejder. Anden Række 1905 (2026-10-16): a gutter cut in the scan, and what the sampled check cannot see
`ebook-method/mindre-arbejder-2/` (Høffding, 237 pp., 17 pieces; Google/NYPL bitonal TIFFs + the Archive's ABBYY).  Lessons:
1. **A Google scan can CUT the gutter margin**: letters or short words physically missing at the line ends of even pages
   and the line starts of odd pages.  Both OCRs agree on the fragment, so the collation never sees it, and a line-end
   join makes nonsense of it (ud- + [tøm]t -> "udnt").  Find the damaged pages by tesseract's confidence on line-edge words
   (< 75: clean pages 0-1 such words, damaged ones 8-22), read them WHOLE at the image, and supply the lost letters by
   sense, each recorded with its reason ("uncertain" where the traces allow two words).
2. **Stratify the page check by damage**: 6 random pages gave 0 errors on the clean and 9/1000 on the damaged ones; the
   translators' odd spots then found ~105 more faults and ~130 cut-margin spots, nearly all on damaged pages not read
   whole.  Read every damaged page whole, or say in the header that the residue is there.
3. **The odd spots need crops of the whole line** (oddsheets.py: the line(s) of the spot, 300 dpi, ~12 a sheet) and readers
   who read all their sheets in ONE turn and write ONE file (90k tokens for 4 sheets, against 119k when they read item by
   item); a paragraph-break question needs the line before and after.
4. **Compact blind sheets** (3 columns, ~46 one-line crops, 2 controls) cut the reader's cost to ~28k a sheet with no
   loss of controls.  Skewed pages: fit the left margin as a line in y before judging indents, and count only the
   first line of an indent run as a paragraph start, or every skewed page grows false paragraphs.
5. **Proof rows applied before the line-end joins can leave a line that begins with , or .** (the print's mark after the
   last word): TeX sets a space before it.  oddapply.py joins such lines as the last step.

### Etiske Undersøgelser 1891 (2026-10-16): a layer swap that blanked the scan, and comments inside patches
`ebook-method/etiske-undersoegelser/` (Høffding, [VI] + 83 pp.; Google/Wisconsin bitonal + the Archive's ABBYY; a clean scan:
no damaged pages, gutter not cut).  Lessons:
1. **After any change to a scan's layer, render one page and look at its pixels** (`pdftoppm -r 50` and the mean).  qpdf
   --overlay puts the IMAGE page into a Form XObject too, and mindre-arbejder-2's `layer.py` stripped every Form: the scan in
   bibliotek kept its text and lost its images, which showed only when the page-check sheets came out white (two readers,
   ~0.15M tokens, before they stopped).  `layer.py` now keeps any form that holds an image.
2. **Never put a `%` comment into a patch's replacement text inside a line**: it hides the rest of the printed line (p. 57:
   seven words, found by the page check).  Record the reason in the patch's `why` or in the header.
3. **The unattested-word sweep's compound filter hides glued words** (`endomvendt` = end omvendt): tesseract loses word spaces
   in letterspaced lines.  List unattested words that split into two common words, and read them.
4. **Note readers normalise misprints** (Vierterljahrsschrift read Viertel-, both OCRs and a zoom agreeing on r): set the
   notes from the reading, but diff it against the collated draft's note text (`notesdiff.py`) and settle each at 600 ppi.
5. **A weak f reads as t in both OCRs and at the image** (`at` for `af`, six times): the translators find them by grammar;
   the print shows t, so they stay as printed, marked PRINTED AS IS.
6. **The translators' odd spots can be settled cheaply**: 52 spots as 600 ppi LINE crops (ABBYY line boxes, two lines each,
   ~12 to a composite) read in the main session cost ~10k tokens, against ~100k for reader agents; 12 were faults.  Line
   crops, never whole pages.
7. **Measured letterspacing runs that cross a line-end hyphen must be merged** before `spaceapply.py`, or the first run takes
   the joined word and the second finds nothing.  A sample read whole (30 runs + 12 lines with none) found no false run.
8. **An NB item can be down for a day** (images, ALTO and the PDF generator 404/500 while other items serve): try one image
   before planning on a second copy.

### Religiøse Tanketyper 1927 (2026-10-17): a missing leaf that looked like a repeat, pencil slashes, a lean budget
`ebook-method/religioese-tanketyper/` (Høffding, 165 pp.; NB scan without a layer, SAGA e-book; oplevelse-og-tydning's
pipeline).  ~1.4M agent tokens for transcription and translation together (~8.5k a page).  Lessons:
1. **Read the folios at the image before diagnosing a page-map anomaly.**  NB's ALTO gave the folios 26, 27, 28, 29 for
   four images whose text ran 26, 29, 26, 29; its text of „28-29“ matched „26-27“ line for line, and the session first
   reported a printed repeat with no text lost.  A 5-line crop of the heads showed 26, 29, 26, 29: NB had skipped a leaf
   and shot two pages twice.  The e-book proved the loss (~670 words between the last word of p. 26 and the first of
   p. 29).  Check every page join of the scan against the e-book's continuous text: a gap of hundreds of words is a lost
   leaf, whatever the folios in the layer say.  The missing pages were set from the e-book and flagged (Hans's choice),
   and listed in KB-VISIT-TODO.md.
2. **A former reader's pencil slashes between sentences are read „/“ by BOTH OCRs** (here 14); grep the body for „/“
   after OPEN 0, and read whether a stop lies under each slash.  Pencil crosses in the margin come as x / + in tesseract.
3. **NB's ALTO reads the print's „ as ~ (and «)** where the print has no guillemets: map in draft.py, after checking the
   e-book's quote marks (here „ “ only).
4. **Notes: measure the indent pattern, never copy it**: oplevelse's notes had a hanging indent, this book's indent the
   first line; and take notes only on the pages `nb_scan.py notes` lists, or verse in small type becomes notes.
5. **Settle checks by hand from three witnesses, tagged and audited**: where NB's word is no word and tesseract and the
   e-book agree (NB's l for I, n or .. for „, junk above an opening, German umlauts by the umlaut rule), 70 checks were
   decided as `hand-3wit` without crops; 10 of them in the blind audit, all right.  `collate/check.py` now writes
   `.parts/collate/checks-all.tsv` (every check with its box), so decided checks can be drawn for an audit.
6. **NB's `spaced` (wide words) was all false here**; the e-book's <i> spans in the body were the print's italics
   (6 of 6 read).  Read a few of each before trusting either.
7. **One question per crop for structure readers** (st1.py: title, dividers, end rules, verse, paragraph doubts, notes
   whole, ~72 crops on 21 sheets, two readers ~225k): the answers came back specific enough to patch from directly.
8. **A `% PRINTED AS IS` marker inserted before a phrase that begins mid-line comments out the rest of that line**: patch
   with a regex anchored at the line's start and put the comment on its own line before it.

### Kort Oversigt 1910 (2026-10-17): an e-book of another edition, small capitals, quotes, a dropped first line
`ebook-method/kort-oversigt/` (Høffding, 4th ed., 95 pp.; NB scan without a layer; religioese-tanketyper's pipeline).
Agents: two b1 readers, two structure readers (~210k), two page-check readers (~160k), six translators (~780k).  Lessons:
1. **An e-book's copyright year is not its edition.**  SAGA prints „Copyright 1898“ on a text of 1920 or later (Wundt's
   death, a second Tillæg, modernised verb plurals).  Date the e-book from internal evidence before calling it a witness
   of any edition; here it differed from the 1910 print in 1238 words and could vote only where it agreed with one OCR.
2. **Small capitals: tesseract reads them as CAPITALS, NB in mixed case, the e-book as capitals.**  An e-book vote for
   capitals is a vote for small capitals (rules2.py converts it to SC).  Names are often only HALF in small capitals in
   the draft (first name SC, surname not, or the reverse): sweep for `\textsc{X} Y` and `Y \textsc{X}` next to dates and
   read each at a line crop (sc5: 6 of 13 mended), and ask the structure readers for every run-in name opening.
3. **Balance the quotation marks per paragraph.**  NB read the print's „ as « or » or dropped it (the print has no
   guillemets at all; the b1 brief had wrongly said both occur): 45 lines in unbalanced paragraphs, read at line crops in
   the main session (q3.py, five sheets), all openers „.
4. **A running-head rule can eat the first text line**: draft.py dropped p. 2's first line because it began with a head
   word („Erkendelses …“) and lay in the head zone; the tesseract witness had lost it the same way, so the collation was
   silent.  Only the translator's „the Danish loses text at the page turn“ caught it.  draft.py now keeps a line that ends
   in a hyphen and logs HEADSKIP/HEADKEEP; grep the log for HEADSKIP on every book.
5. **Doubled dashes „--- ---“** (a dash at a line end read twice): grep after OPEN 0; here all twelve were one dash.
6. **Specks as stops**: „har. sin“, „paa. det“, „alle. Grænser“, „Brunos, Etik“ — a stop before a lowercase word or a
   comma before a capital in mid-sentence is worth a line crop.
7. **Main-session line crops are cheap**: oddlines.py crops the printed line behind any transcription line number (three
   of its words found on tesseract's lines); ~120 lines read this way in five sweeps for ~40k tokens, cheaper than a
   reader agent's fixed ~50k.

### Rydberg review 1882 (2026-10-17): a two-page piece without agents
`ebook-method/rydberg-anmeldelse-1882/` (~1,500 words, two columns, the Böhme review's scan).  For a piece this short the
whole apparatus (collation decisions, blind crops, page check) costs more than reading every line: our tesseract draft,
the Archive's hOCR as a pointer, then ALL 171 lines read at line crops in the main session (eight sheets, ~25k tokens)
with 3x zooms of doubtful marks; nine lines corrected; translated in the main session.  Lessons: (1) leaf offsets drift
inside a volume with unnumbered plates (Böhme: page + 15; here page + 11): find the page in the hOCR by its folio before
fetching; (2) a column- or page-break comment inserted with a blank line before it makes a false paragraph: insert page
markers without the blank line; (3) a word divided across a column joins onto the last TEXT line, not onto the column
marker.

### No e-book: two OCRs (2026-10-03, Personlighetsprincipen i filosofin)

When there is no e-book, make the draft from one OCR and collate it against another, independent one
with `ebook-method/collate/check.py` (ebook-method/personlighedsprincippet: `ocr.py` reads the scan with
tesseract into word boxes, `draft.py` builds the draft once -- folios and watermark dropped, footnotes
found below the rule by the gap and the smaller type and set at their anchors, paragraphs from the
indents, line-end hyphens joined -- and check.py collates it against the scan's own layer, here
Google's). What this taught:
1. Google Books layers drop guillemets and read dashes as hyphens: most disagreements are of that one
   kind and can be decided by class. But a class rule must test what it claims: "only quote and dash
   characters differ" also passed "lik- som" for "liksom" (a hyphen and a space are dash characters).
   Read the whole draft once after the collation; it found some twenty such slips.
2. Two OCRs agree on what neither can see: the italics (check.py --italics at its default threshold
   found none; at 1.015 it found the three real ones among 36 crops) and the footnotes' labels. Read
   every footnote whole at the image.
3. A word both OCRs agree on can still be the print's slip (möjliggör for omöjliggör): it is the
   translation that finds it. Mark it in the transcription when the translation does.

## 7. Bookkeeping

Keep **RESUME-NOTES.md** in the book directory, updated every ~20 pages, not
every batch. It should carry: the page map and how it was verified; the current
resume point; the running quote-balance total with every logged defect; open
review items; and anything that cost you an hour to learn. Write it for a reader
with no memory of the session — because that is exactly who reads it next.

**RESUME-NOTES.md is untracked** (see §1), so it exists only on your machine.
Anything in it that a *reader of the edition* would need — page map, errata,
emphasis rules, normalisation conventions, defect log — must be duplicated into
the `transcription.tex` header, which is what ships. Treat RESUME-NOTES as the
production log and the `.tex` header as the publication of record. When they
disagree, the header is what the world sees.

### What "done" is allowed to mean

A book is not done because it compiles. Before `status: complete` goes into
`catalog.yaml`, the book must be able to state, in the `transcription.tex`
header, how its accuracy was established:

```
% Word-accuracy: every batch diffed against <witness> before splicing
% (ocrdiff.py). <n> batches, <n> candidates, <n> transcription errors
% corrected, 0 unresolved.
```

If a book cannot carry that line — an older book transcribed before this rule,
or one whose batches have no `OCRDIFF:` record — it is not `complete`. Its
accuracy is *unmeasured*, which is a different thing from *good* and a different
thing from *bad*, and `catalog.yaml` should say so rather than imply a check
that never happened. An unmeasured book's error rate can be estimated cheaply
without re-collating it: **six random pages read at the image against the
transcription** gives a usable rate per book. That is how *Den menneskelige
Tanke*'s problem first surfaced — 8 of the 32 pages in its first collation were
a random control sample that nothing had flagged, and they carried errors at the
same rate as the flagged ones.

When the book is done, two passes remain: the Indhold/contents from the image
(§6), and the outstanding review items. Then update `catalog.yaml` — every
section needs `title`, `status`, and `links` (use `links: []` when empty; the
Haskell parser requires the key) — and the user runs
`~/hhalvors.github.io/publish-danish.sh "message"`, which rebuilds the PDFs,
regenerates the site, and pushes both repos.

### Before calling a transcription done: words per page and a prescreen (speculative-logik, 2026-10-07)
A transcription called done (OPEN 156, every image round run) still had a whole page of text missing (p. 81: the
§ thesis, taken by draft.py as an unplaced note and dropped by finish.py's notes step) and ~400 residue faults that the
translators and a script found.  Two cheap checks would have caught the worst before translation: (1) count words per
page against tesseract's reading and look at every page under 75 % (pages whose run-over notes moved are expected);
(2) ebook-method/speculative-logik/prescreen.py: words doubled by --apply where tesseract has them once, o: for ɔ:,
letter-spaced words still split into letters, heading debris (a § title set both by the macro and as text), compound
hyphens set as dashes.  A POST patch whose old text contains a newline is matched with \s+ there, which also eats the
blank lines around it: give the replacement the blank line it needs.

### The sampled page check (speculative-logik, 2026-10-07)
ebook-method/speculative-logik/pagecheck.py (sample / sheets / compare / rate) + PAGECHECK-BRIEF.md: 14 seeded random pages
(stratified, plus pages with notes), whole pages cut into line strips between the layer's lines (two strips a sheet),
transcribed blind line by line by one Sonnet reader (137k), compared word by word (hyphenation and word division not
compared), every difference decided with the three OCR readings beside it and crops for the doubtful.  Self-test first:
the transcription's own text read back must give 0 differences and injected faults must all show.  Result on a book that
had been collated, swept AND second-read by translation: 2.4 word errors per 1000 words.  Two lessons: (1) a doubled word
is not always an --apply artefact (p. 25 „er er“ was „er i“): a rule that removes doubled words must check the word
AFTER the pair in the witness, or be read at the image; (2) a reader's bold calls are not reliable enough to count
unchecked (1 of 8 checked was wrong), and heading macros give emphasis differences that are not errors.
