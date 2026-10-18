# Poul Martin Møller — "Om Muligheden af Beviser for Menneskets Udødelighed": resume notes

Source of truth: `transcription.tex` (Danish), **COMPLETE** (both articles).
Translation: `translation.tex` is a stub — **not to be completed**; Jon Stewart
already published an English translation (2022), doi:10.1163/9789004517912_003.

## STATUS
Danish transcription of the whole essay is complete and compiles clean in the
sandbox (0 errors, 0 missing-character warnings, 72 pp.). Marked `complete` in
`catalog.yaml` pending a local compile with the real fonts (libertinus +
textalpha) and a commit/push so the GitHub Pages links resolve.

**`transcription.pdf` in this directory is stale** — it predates the 2026-09-12
repairs below. Rebuild via `~/hhalvors.github.io/publish-danish.sh`.

## 2026-09-12 — repairs to the Art. I digitised transcript
The Art. I text came from a digitised transcript of SiU, not from page images,
and carried that transcript's page-foot damage. Full log, with SiU and MfL page
numbers for every site, is now in the **`transcription.tex` comment header** —
that is the record of publication; this is only the production note.

Summary: 24 paragraphs rejoined (each had been split mid-sentence at a page
foot); 4 sheet-signature asterisks deleted from the text (SiU 172, 175, 186,
213); 3 sentence-final full stops restored (SiU 171, 236, 244, all confirmed
against MfL); Art. I's 4 missing footnotes supplied from the MfL first printing
and normalised SiU-style (SiU 171, 174, 185, 212 = MfL 3, 6, 15, 38); the OCR
junk `*dolgoeO*` at SiU 189 resolved to `Ug.x` (MfL 19, the antiqua x of the
school mark "ug med kryds").

### Open review items
1. **Collate the four restored footnotes against SiU pp. 168--253** when the
   volume is to hand. They are reconstructions from MfL, not readings of the
   copy-text; SiU's wording, and its placement of the mark relative to the
   sentence stop, may differ. This is the one outstanding scholarly debt.
2. Closing high quote is written two ways in the file: literal `“` twice and
   LaTeX `` `` `` twice. Both typeset identically; balance is 4 open / 4 close.
   Normalise if it ever matters.
3. Art. I uses ` - ` for the dash (31x) where Art. II uses ` --- ` (13x). The
   Art. I hyphens are almost certainly the digitised transcript flattening em
   dashes. The 4 restored footnotes use `---`.
4. Footnote marks are printed `*)` throughout MfL but set here with plain
   `\footnote{}` numbering (1--13 continuous across both articles). If per-page
   `*)` is wanted, `\renewcommand{\thefootnote}{*)}` in the preamble --- not
   `\fnsymbol`, not `footmisc[perpage]` (see TRANSCRIPTION-PLAYBOOK §4).

## Two-part provenance (important)
The essay appeared in *Maanedsskrift for Litteratur* 17 (1837) in two
installments:

- **Article I** ("Første Artikel", §§ I–VII) — MfL pp. 1–72. Transcribed here
  from **Skrifter i Udvalg** (1930), pp. 168–253, in that edition's modernized
  orthography. `\opage{}` margin numbers in this part are the SiU page numbers.
- **Article II** ("Fortsat og sluttet", §§ VIII–XI) — MfL pp. 422–453. This
  installment was **omitted from Skrifter i Udvalg** (a selection), so it is
  transcribed from the **Fraktur first printing** (`moller-udoedelighed-scan.pdf`,
  scan pp. 73–104), rendered in the *same* SiU-style modernized orthography for
  continuity. `\opage{}` numbers 422–453 in this part are the 1837 MfL page
  numbers. A bracketed editorial note in the .tex flags the source switch at the
  Article I/II boundary.

## Article II section map (pp. 422–453)
- **§ VIII** p. 422 — restatement; the immortality proof belongs in the doctrine
  of absolute spirit. Long block quotation from **Weiße** (pp. 423–430) on the
  aesthetic consciousness as approach to the proof.
- **§ IX** p. 431 — the younger **Fichte**, *Die Idee der Persönlichkeit* (1834);
  long block quotation (pp. 432–439) on the natural-analogy / physiological proof.
- **§ X** p. 440 — **Göschel**, *Von den Beweisen …* (1835); two block
  quotations (the second closes p. 449), then Møller's critique of Göschel's
  Hegelian re-casting.
- **§ XI** p. 450 — survey of the wider literature (Dr. Mises = Fechner;
  Hubert-Becker), and the closing methodological point that a rigorous proof is
  possible only inside a fully articulated system. Ends p. 453, signed
  "Poul Møller."

## Conventions (book-specific)
See `../../../TRANSLATION-PLAYBOOK.md` for the standing method. Specifics:
- Main block quotations use Danish guillemets »…«; the German footnote quote and
  the short titles-in-quotes use „…``.
- Orthography modernized SiU-style: `Beviis`→`Bevis`, `speculativ`→`spekulativ`,
  `philosoph`→`filosof`, `æsthetisk`→`æstetisk`, `Existents`→`Eksistens`,
  `kj`→`k` / `gj`→`g` (but `gjort` stays), `ei`→`ej`, `øi`→`øj`, `ee`→`e`
  (`Fordeel`→`Fordel`), `stræng`→`streng`, `Villie`→`Vilje`, `Linier`→`Linjer`,
  `Literatur`→`Litteratur`. Emphatic numeral kept as `Eet`/`een`. `aa` retained.
- Old "id est" mark **ɔ:** (U+0254) mapped in the preamble via
  `\DeclareUnicodeCharacter{0254}{\reflectbox{c}}` (needs `graphicx`).
- German book titles and embedded Latin/French phrases in `\textit{}`.
- Footnotes rendered with `\footnote{}` (Göschel/Fichte/Weiße/Mises titles;
  the long authorial note in § VIII on "individuality"; the Sibbern program note
  on p. 451; the Mises and Hubert-Becker notes on p. 452).

## Sandbox compile recipe
Strip libertinus→lmodern, delete `libertinust1math`/`textalpha`, drop the
`[danish]` babel option; then `pdflatex` twice. Expect 0 errors, 0
missing-character warnings (a handful of Overfull hboxes from long unbreakable
quotation strings are harmless).

## 2026-10-18 — set-up for a DIPLOMATIC transcription of the 1837 first printing (machine collation only)
The current `transcription.tex` is a hybrid (Art. I = ADL e-text of SiU 1930, modernized; Art. II = 1837 print respelled
1930-style) and is to be replaced by a diplomatic text of MfL 17 (1837).  Nothing in `transcription.tex` or
`translation.tex` was changed; no agents were run.  Pipeline: `ebook-method/udoedelighed/` (README entry there).

**Scan.** Copied (not moved) to `~/bibliotek/Møller, Poul Martin/1837-maanedsskrift-17-udoedelighed.pdf` and registered in
SCANS.tsv (sha256 0a62304a…, 104 pp., USABLE; `scans.py verify` OK).  The byte-identical original is still at
`texts/moller/udoedelighed/moller-udoedelighed-scan.pdf` (deleting is not permitted to Claude): Hans may remove it.
The print is **FRAKTUR** (one 110-dpi render of PDF 3), with antiqua for some foreign words; notes marked `*)`, `**)`.

**Page map** (folios read off Google's layer, all consistent): MfL pp. 1–72 = PDF 1–72; MfL pp. 422–453 = PDF 73–104
(PDF = p − 349).  The layer misreads three folios (PDF 19 „31“, 73 „429“, 93 „449“).  No missing or duplicated pages, no
plates or ads; the scan holds only the essay's pages.  **p. 72 also carries the opening of the next piece** (a review of
Brunius, *Nordens äldsta Metropolitankyrka … Lunds Domkyrka*) under Art. I's „(Fortsættes).“: `pagemap.CUT` drops it.
Sheet signatures at the foot („1*“, „30 *“) are dropped.  Witness 2, Efterladte Skrifter 3rd ed. vol. 5 (1856):
pp. 38–140 = PDF 49–151 (+11; consistent at both ends — that layer has no folios).

**Draft** (`draft.py --emit`, from Google's layer, into `.parts/draft.tex`): 30,442 words, 159 paragraphs, 13 centred
lines, **14 footnotes** (13 placed at their marks; the `**)` mark on p. 452 not found).  Notes per page: pp. 3, 6, 15, 38,
62, 422, 423, 426, 431, 432, 440, 451, 452 (2) — the layer's own note starts number 13 (p. 431's star read „*“).  **The old
transcription lacks the p. 62 note** (Schopenhauer, „Die Welt als Wille und Vorstellung.“).  Still unjoined: 26 line-end
hyphens the layer read as „z“ (`grep '[a-zæø]z$'`); block quotations are not detected (Google's box heights are
quantized), so the German quotations need the structure reader.

**Collation** (check.py vs tesseract script/Fraktur, deu_latf + frak2021 as 3rd/4th readings; counted on a FRESH draft):
4,609 disagreements; check.py rules 648 (glyph 484, split/noise 138, moved 10, noise 16); rules.py 2,489 (frak-lit 557,
vote-T 504, frak 266, accent 181, freq 173, tokens 165, tokens-wnorm 152, IJ 121, vote-T-punct 109, layerfault 44, case
22, consensus 19, vote-W* 35, other 6 — none yet audited at the image).  **OPEN 1,472** (Art. I 1,088 ≈ 15/p.; Art. II
384 ≈ 12/p.): one word, letters differ 505; punctuation/quote/dash only 447; multi-word 299; witness-only marks 66 and
words 33; draft-only words 47 and marks 4; ø/o 57 (the ø rule settles non-words without the image); word division 11;
case 3.  `--moved` 10 (5 pairs: pp. 6, 42, 52, 64/65, 440); `--splits` 0 (LAYER_SPLITS on).  `--apply` applied 233,
10 MANUAL.  Not yet run: oepass / D-for-Ø / gi-for-gj lexicon scans (script, free).

**Emphasis.** `collate/spaced.py`: 26 letterspacing candidates, 5 of them on p. 72 in the Brunius review → 21 in the
essay (Magdeburg, Breslau …).  The emphasis device is NOT yet identified (letterspacing looks rare; Schwabacher, as in
*Bemærkninger* 1838, is possible): the recon/structure reader must settle it.  The slant test does not apply to Fraktur.

**Witness 2 diff** (`diff1855.py`, letter streams aligned in windows): 1,116 spots listed after dropping 452 as the 1856
OCR's faults; 227 coincide with OPEN checks, ~890 are new (59 1856 spelling, 306 one word vs one word, 524 multi-word,
mostly that layer's junk).  The 1856 layer is a poor ABBYY Fraktur OCR; **cheaper and cleaner: tesseract the 103 pages
of 1856 (device time only, no tokens) and diff against that.**

**Cost estimates** (rates from COLLATE-WORKFLOW §1 and the playbook):
- (a) disagreements only: ~1,620 blind crops (1,472 + ~10% controls), ~160 sheets of 10.  At the rate measured on this
  same pipeline (skjaebne-og-forsyn: 1,066 checks + audit ≈ 261k) ≈ 0.4–0.5M; + structure reader (title, headings, notes,
  block quotations, emphasis device, antiqua) ~0.1M; + the 1856 spots after a tesseract re-diff ~0.1M → **~0.6–0.7M**.
  (With 32-question LEAN-READER sheets the same work would be ~5M: do not.)
- (b) the repo's full rule, every page read blind with planted controls: 104 dense pages at the measured ~11–15k/page
  (staerkeres-ret, Erindringer, begrebet-noiagtighed) ≈ 1.2–1.6M, + main-session crops of the reader/machine differences
  ~0.1M → **~1.3–1.7M**.
- Cheaper way to satisfy (b): the begrebet-noiagtighed route — the blind page reading as text of record, each word voted
  against layer + tesseract (vote2.py), crops only where the reader is unsupported.  That replaces (a) instead of adding
  to it: ~1.3–1.5M in all, against ~2M for (a) + (b).

**Decisions for Hans:** (1) route (a), (b), or the vote route; (2) whether to OCR the 1856 resetting with tesseract
first (free); (3) when the new text replaces `transcription.tex` (and the stale `transcription.pdf`).

### 2026-10-18 (later) — the 1856 resetting read by tesseract (Hans approved this free step only)
`ebook-method/udoedelighed/ocr1856.py`: tesseract script/Fraktur on ES vol. 5 pp. 38–140 (PDF 49–151, 300 ppi), cached
in `.parts/collate/ocr-1856/pN.txt` (gitignored).  Far cleaner than that scan's ABBYY layer (31,689 tokens against the
draft's 30,468; the layer had 41,295 fragments).  It already shows editorial revision (p. 2: 1837 „Meningsyttring“,
1856 „Meningsfrihed“), so it is a witness of ANOTHER text.
- `diff1855.py` now uses it by default (`--layer` for the old layer): **863 spots** (was 1,116), 202 at OPEN checks, 661
  new (171 of them one word against one word), 376 dropped as the 1856 OCR's faults.
- `vote1856.py` (new) asks, for every check, whether the 1856 reading equals one of the two 1837 readings.  **Nothing is
  applied**: proposals go to `.parts/collate/vote1856.tsv`, not decisions.tsv, because the playbook's rule is that a
  resetting finds and never votes (Betingelserne lesson 4).  Important: tesseract makes the SAME Fraktur faults on both
  prints (ø→o, k/s→f, I→J, gj→gi), so an 1856 agreement with the 1837 tesseract on such a reading is one engine twice;
  the script discounts those (`witness-same-engine`, 45 open, 390 decided).
- Of the 1,472 OPEN: the 1856 sides with the draft (layer) in 650, with tesseract (independently) in 69, with neither in
  600; 108 could not be located/aligned.  **Under the repo's rule OPEN stays 1,472.**  If Hans accepts the 1856 agreement
  as a rule (audited by a blind sample):
  - SAFE subset only (letters differ and the losing reading is no corpus word; punctuation excluded, since editors revise
    it): 242 settled → **OPEN 1,230** (Art. I 893, Art. II 337): punctuation/quote/dash 447, one word 333, multi-word
    270, witness-only 83, ø/o 57, draft-only 27, division 11, case 2.
  - every agreement: 719 settled → **OPEN 753** (Art. I 533, Art. II 220): one word 278, multi-word 192, punctuation
    170, ø/o 57, draft-only 26, witness-only 20, division 8, case 2.  The misprint risk is higher here: a reprint
    corrects misprints, so a vote would erase them.
- **Rule decisions: none changed**, but the 1856 reading contradicts 38 of the 2,489.  These should go to the image.
  Likely rule errors are 12 `case` (the layer's lower case, e.g. „hensyn“, „hovedet“, where tesseract and 1856 have
  capitals) and 15 tesseract-vote W's (`vote-W1`, `vote4-W2`, `vote-W-punct`, `tokens`, `vote-W-raw`): „sine>fine“,
  „gjentage>gientage“ (×3), „Hiin>Hisn“, „med>ed“.  That repeats the staerkeres-ret lesson: a rule must never move a word
  INTO the gi/ki or f-for-s class, and rules.py needs that guard before any --write.  The list is in
  `.parts/collate/vote1856-conflicts.tsv`.
- **Revised estimates.** (a) Disagreements by blind crops, at skjaebne-og-forsyn's measured ~0.25k per crop:
  - under the rule: 1,472 + 38 + ~150 controls ≈ 1,660 crops → ~0.42M, plus the 661 new 1856 spots (~0.15M, fewer if
    sorted in the main session first) and a structure reader (~0.1M) → **~0.65M**;
  - with SAFE accepted: ~1,420 crops (incl. a 25-item audit) → **~0.6M**;
  - with all accepted: ~0.5M.

  (c) The vote route (the blind page reading as the text of record): the pages must still be read whole, so the 1856
  witness saves only adjudication crops → **~1.25–1.45M** (was 1.3–1.5M).

### 2026-10-18 (later still) — Hans chose route (c); SAFE 1856 votes applied; pilot prepared
- **SAFE subset applied**: the 242 proposals were appended to `ebook-method/udoedelighed/decisions.tsv` as
  `rule:vote1856-safe` (221 T, 21 W; backup in `.parts/decisions.tsv.bak.20261018-pre1856`).  Fresh draft + check.py:
  decided 2,731, **OPEN 1,230** (Art. I 893, Art. II 337); `--apply` applied 254, 10 MANUAL.
- **Lesson recorded** in TRANSCRIPTION-PLAYBOOK §6 („Om Menneskets Udødelighed 1837“): rules.py's tesseract-family W votes
  and its `case` rule err in the 38 decisions the 1856 contradicts.  A GUARD note was added to `rules.py`'s docstring (not
  yet coded).  The 38 go to crop sheets (`.parts/collate/vote1856-conflicts.tsv`), with the p. 431 footnote count.
- **Route (c) set up** after begrebet-noiagtighed: `READER-BRIEF.md` (blind; Fraktur; HEAD/SIG/notes/`[[antiqua]]`/
  `_spaced_`/`**heavier face**`/SMALL/CENTRED/¶), `bands.py` (600 ppi, cut between lines, ~7 lines a band, 1400 px wide,
  one PNG per band, **two planted image controls per batch**: a plain word's image replaced by another word's of nearly
  the same size, recorded only in `.parts/blind/controls.tsv`), `vote2.py` (reader words voted against layer, tesseract
  and the collated draft; stand-alone words → `.parts/vote/open.tsv`; omissions; control score).  vote2.py was tested on
  a synthetic reading outside the repo: it flagged both planted words, the one planted error, and a note-mark item.
- **Pilot batch R1 = pp. 1–5**: the title, the footnote on p. 3, letterspacing candidates on pp. 1–3, antiqua on p. 3;
  23 bands in `.render/bands/R1/`; controls on p. 2 and p. 4.  The controls' paste quality was not looked at (no image
  reading in the set-up).
- **Not run: the pilot reader.**  This session cannot spawn agents; the reader prompt went to the coordinator.  After
  it returns: `python3 ebook-method/udoedelighed/vote2.py`, then crop the stand-alone words (adapt
  begrebet-noiagtighed/cropsv.py) and the 38 + p. 431 items.
- **Pre-pilot estimate for (c)**: 104 pp. at the measured ~11–15k/page ≈ 1.15–1.55M, plus ~150–250 stand-alone and
  extra crops ≈ 0.05–0.1M, so **~1.2–1.65M** to be replaced by the pilot's measured figure.
- **Pilot R1 (pp. 1–5) read** (by the coordinator's agent): about 100k tokens by the harness count; 1,330 words; band
  controls 2/2 caught.  vote2.py: 26 checks (21 WORD, 5 PUNCT), 2 of them the planted controls.  The 17 omission
  candidates were all artefacts (6 running-head words, 11 pieces of words the machines split at a line end), and vote2.py
  now drops both kinds: 0 left.  Crop check prepared: `cropsv.py 1 pv` gives 24 checks + 2 sheet controls on 4 sheets
  (`.render/vote/udo-pv1-01..04.png`, `.parts/vote/sheets-pv1.tsv`); brief `CROP-BRIEF.md`; answers go to
  `.parts/vote/r-pv1.tsv`; adjudicate with `cropadj.py pv1` (STANDS / READER-ERROR, with proposed vote-fixes / THIRD).
- **Pilot crop sheet answered** (pv1; sheet controls 2/2).  Fixes made the same day:
  - `cropsv.py` now crops a word divided at a line end as BOTH lines, with both halves outlined (12 of the 14 THIRDs
    were first halves only).  It joins a fragment to its neighbour, crops only what `open.tsv` still holds, and writes a
    snapshot `checks-PREFIX.tsv` for cropadj.  Sheets are filled to ~1500 px.
  - `vote2.py` treats a hyphen or dash between words as its own token in every stream, so reader joins and spaced
    dashes are no longer WORD checks.  It also joins a doubled line-end hyphen („tem--“), never joins a page-end
    division across the note rule, drops the checks that ARE the planted controls, and undoes the controls in the text
    (`reads()`).
  - `cropadj.py` counts a divided word as STANDS when the crop's first half and the machines' second half agree with
    the reader.  It writes `settled-PREFIX.tsv`, which vote2.py reads.  Order: cropadj.py, then vote2.py.
  - `vote-fixes.tsv` (new): the 3 distinct reader errors (forblommet; støder, which was 2 checks; Opmærksamhed) plus 3
    confirmed `[?]` removals.  „fremstaaaer“ (p. 5) is a MISPRINT, printed as is.
- **R1, pp. 1–5, after these fixes: open 5** — Richter (p. 1; the crop reader was unsure), Spørgsmaal (p. 2; the first
  box held only the S), til / til, / til. (p. 3), Øde / Døde (p. 4), Göthes / Gø=thes (p. 5).  They stay in `open.tsv`
  and go on the next crop sheet.  A test sheet `udo-t1-01.png` holds them, NOT dispatched.
- **All bands cut**: Art. II R2–R8 (pp. 422–453), Art. I R9–R22 (pp. 6–72); 497 bands, 2 planted controls in every
  batch (44 in `controls.tsv`; R22's are both on p. 71, since p. 72 holds only two essay lines).  The manifest is
  `.parts/blind/MANIFEST.tsv`: batch, pages, folder, files.  bands.py refuses to cut a batch twice.

### 2026-10-18 — all 104 pages read blind (R1–R22); the full crop round prepared
- **Controls: 44/44 caught**, checked at the INSTANCE by `ctlfix.py`.  vote2.py only tests that the word occurs on the
  page, and „bliver“ occurs 5 times on p. 448.  The four planted words that occur more than once on their page (p. 448
  bliver, p. 452 derom, p. 69 vilde, p. 71 lever) are undone by `vote-fixes.tsv` lines; reads() undoes the rest.
- vote2.py changes: p. 72 is cut at „Nordens“ in every stream (`pagemap.CUT`).  The omission filter drops running-head
  words and line-end pieces read with z/s for the hyphen.  Only the planted word is excluded from the checks.
- **vote2 over the whole essay**: 30,441 reader words; **418 open** (Art. I 306, Art. II 112; WORD 334, PUNCT 84;
  87 carry a reader's [?]); 6 omission candidates (p. 14 „det“ — a band-edge line, R10; p. 62 „Uv“, likewise R20;
  p. 444 „Aan“; p. 449 „faavel/saavel“; p. 58 two head words).
- **Crop round** (`sheets2.py 6`): 417 V (one, p. 426 „Æsthetik/Esthetik“, has no box: settle by hand), 6 O, 38 C (the
  rule decisions the 1856 reading contradicts), S01 (p. 431 note count), 38 F (emphasis: 20 reader **heavy**, 8 reader
  _spaced_, the spaced.py candidates; p. 72 excluded).  The p. 439 „*“ is already a V question (reader
  „Religionsphilosophien.*“, layer „…. ““).  87 sheets (81 word, 6 face), 674 crops including 2 hidden controls a sheet
  (`.parts/blind/controls-sheets2.tsv`).  Manifest `.parts/vote/sheets2-manifest.tsv`; ids → sheets in
  `.parts/vote/sheets2.tsv`; questions in `questions2.tsv`.
- After the answers: `cropadj.py qK` for each reader (V items; others → `other-qK.tsv`, to adjudicate by hand), then
  vote2.py.  Band-edge lines (R10 p. 14, R12 pp. 24–25, R18 p. 52, R20 pp. 62, 64): any disagreement there is already a
  V question, and the omission check covers them (p. 14 and p. 62 found).  The owner's pencil marks (pp. 48, 52–54, 57,
  59–61, 67, 440) are not print.

### 2026-10-18 — crop round q (six readers) adjudicated; final round cut; the new text assembled (NOT installed)
- `cropadj.py q1..q6`: STANDS 269, READER-ERROR 57, THIRD 91 (after the rule fixes below).  Sheet controls: 162/174 by
  script.  10 of the 12 "misses" were controls cut without the second half of a divided word, and those readers were
  right.  So 172/174; the real misses were Villie read as „Willie“ and a plain word called „heavy-schwabacher[?]“.
- Tool fixes: cropadj accepts agreement when only one reading is unsure, and accepts a crop answer that includes the
  neighbour words.  vote2 reads „[[16]]de“ as one word, joins the layer's z or : for a line-end hyphen, drops the
  running head from the machine streams, and counts an unsure reader word as settled when the layer AND tesseract read
  the same letters.  applyfix.py turns reviewed corrections into literal-unique vote-fixes lines (keeping the
  reader's line breaks).
- **Corrections applied** (vote-fixes.tsv, all reviewed): 46 + 29 reader errors, mostly the reader MODERNISING (print → reader:
  skee→ske, Beskeed→Besked, Eenhed→Enhed, Literaturens→Litteraturens, Conseqventser→Consequentser; once the reverse,
  vist→viist; b for d in saadant→„saabant“), plus
  misprints the reader silently corrected, now set as printed with a comment: Charakteermennesker, ieg (×2), knnne,
  Kræft, hragt, gjenuemgribende, videnskabellg, Aaabenbaringer, ar, drt, Menneneskets (the Art. II title), metaphysike,
  Sanfund, Bekjendtgjørelseu, fremstaaaer.  Settled by review in `.parts/vote/settled-hand.tsv` (37 entries, each with
  its reason); p. 426 „Æsthetik“ = reader + tesseract (in the note).
- **The 38 rule decisions the 1856 reading contradicts**: the crops show the rule WRONG in 27 (12 `case` lowercasings,
  C25 R./K., and 14 tesseract-family W votes: sine, Mindeskrifter, ved, Hiin, i en, see, gjentage, gjentager, Kunstens,
  med, udfylde, Gjenstand, Denne, sin) and right in 11.  They concern only the draft; the reader text did not take them.
- **p. 431**: one footnote („*)“), as the draft had.  **p. 439**: the „*“ is a closing quote („…philosophien.“ “).
- **Emphasis (face sheets)**: the print's emphasis is a HEAVY (bold) Fraktur — confirmed for Leibniz p. 7, Fichte p. 21,
  virkelig p. 70, Kjendsgjerning(er) p. 428; Fredrich Richter p. 33 uncertain.  Letterspacing only for Magdeburg and
  Breslau on p. 1 (Tanken p. 449 uncertain).  All 18 of spaced.py's other candidates are plain.  Of the readers' 18
  „heavy“ spans, 12 were plain: the two pasted controls, Göschel p. 2 (pencil) and p. 451's German quotation.  No reader
  marked smaller type, so the quotations are in body type.
- **Final crop round** (`finalround.py`): 11 words (Using/Ussing p. 15, sjelden/siælden p. 17, skaber/skader p. 24,
  skjæv p. 29, Voxne/Vorne p. 56, Udtryk p. 62, Guddommen. p. 441, Beviser: p. 442, der/der. p. 446, stoleret/skoleret
  p. 450, endnn p. 453) + 4 faces (Fredrich Richter p. 33, Forf. p. 432, Tanken p. 449, -tumlet p. 15), on 3 sheets
  `.render/vote2/udo-z-01..03.png` with 2 controls each; answers → `.parts/vote/r-z1.tsv`; `cropadj.py z1` (RF ids by
  hand), then vote2.py and fromreads.py.
- **Assembly**: `fromreads.py` + `template-new.tex` → `.parts/transcription-new.tex` (header: source, page map, method,
  accuracy, conventions).  104 page markers, 14 notes (marks = notes on every page), 6 \textbf, 2 \emph, 18 \textit,
  16 PRINTED AS IS comments, 2 ø-rule changes (Overflødighed, føier).  Sandbox compile: 0 errors, 0 missing
  characters, 76 pp.  transcription.tex NOT replaced.

## 2026-10-18 — CURRENT STATE: the diplomatic transcription of the 1837 first printing is INSTALLED
- `transcription.tex` is now the diplomatic text of MfL 17 (1837), both articles, built by
  `ebook-method/udoedelighed/fromreads.py` (+ `template-new.tex`).  The old hybrid is kept as
  `transcription.tex.bak.20261018-hybrid`.  Sandbox compile: 0 errors, 0 missing characters, 76 pp.
  `transcription.pdf` is stale until the next `publish-danish.sh`.
- Final round (z1): Ussing, sjælden, skjæv, Guddommen., endnn (a misprint) settled, and Tanken p. 449 letterspaced.
  Sheet controls 5/6.  All crop-sheet controls: 177/180.  Band controls: 44/44.
- **9 DOUBTFUL sites**, each with a `% DOUBTFUL:` comment in the .tex (the reading set, its rivals, the reason).  One
  review sheet for Hans: `.render/review/udo-review-doubtful.png` (`review.py`).  The sites: p. 7 Leibnitz (reader and both machines tz; crop V011 Leibniz), p. 15 tumlet (face),
  p. 24 skader, p. 33 Fredrich Richter (bold?), p. 56 Voxne, p. 62 Udtryk, p. 442 Beviser:, p. 446 „der ei“,
  p. 450 skoleret.
- Bookkeeping done: ACCURACY-LEDGER row (read-whole-voted); catalog.yaml note and section title describe the 1837
  diplomatic edition (the Stewart translation link is kept; validate-catalog: 0 problems); SCANS.tsv verified OK;
  TRANSCRIPTION-PLAYBOOK §6 entries.
- `translation.tex` is still a STUB.  Stewart's translation (2022) exists; the RESUME-NOTES decision „not to be
  completed“ stands unless Hans says otherwise.
- `moller-udoedelighed-scan.pdf` stays in this directory (catalog „Scan“ link).  It is byte-identical to the bibliotek
  copy; Hans may delete it, and should then repoint the link.
- Rebuild: `python3 ebook-method/udoedelighed/vote2.py && python3 ebook-method/udoedelighed/fromreads.py`, then copy
  `.parts/transcription-new.tex` to `transcription.tex`.  Run cropadj.py for each crop prefix (pv1, q1–q6, z1) before
  vote2.py if the answers change.
- Spot-check fix (same day): fromreads.py applies the Fraktur I/J rule (a word-initial J before a consonant → I, outside
  antiqua, logged): Jdealisme → Idealisme (p. 6), Jdee → Idee (p. 14); no other case either way.  Leibnitz p. 7 added as a DOUBTFUL site.

### 2026-10-18 (last) — Hans's decisions applied through the pipeline; reinstalled
- The 9 doubtful sites, decided by Hans at the image: Leibnitz p. 7, tumlet plain p. 15, skader p. 24, Voxne p. 56,
  Udtryk p. 62 (`% NOTE:` the d is worn), Beviser: p. 442 (`% NOTE:` a smear at the colon), no mark after „der“ p. 446
  (a speck), skoleret p. 450.  No DOUBTFUL comments remain.
- **Leibnitz with the tz ligature at all six places** (pp. 7 ×3, 8 ×2, 9).  The crop readers' „Leibniz“ (V009, V013, V016,
  V018, V022) was a READER FAULT; the vote-fixes lines were rewritten and the settlements put in settled-hand.tsv.
- The I/J rule now also covers the one-letter word: „J ethvert“ p. 24, „J et saadant“ p. 435, „J Conceptionens“ p. 436 → I.
  Jdealisme → Idealisme (p. 6) and Jdee → Idee (p. 14) as before.
- **Faces**: proper names are in Schwabacher throughout and are not marked, so \textbf was removed from Leibnitz,
  Fichte and Fredrich Richter.  Schwabacher on an ordinary word = emphasis: \textbf{virkelig Tilværelse} p. 70 (the only
  one).  Kjendsgjerning(er) p. 428 is Fraktur.  The header's CONVENTIONS were rewritten to match.
- vote2: open 0.  fromreads → transcription.tex reinstalled; sandbox compile 0 errors, 0 missing characters, 76 pp.
- Sheet for Hans: `.render/review/udo-heavy-plain.png` (`heavysheet.py`).  It has a reference strip (Fraktur Form p. 21,
  Tilværelse p. 8; Schwabacher Fichte p. 38, Tilværelse p. 70), then 14 words tagged heavy and set plain: aabenbar p. 2
  (a control site), Göschel p. 2, Marheineckes p. 2, Udødelighed p. 64, ubunden p. 450 (a control site), and nine spans
  of the German quotation on p. 451.

### 2026-10-18 — Hans's face decisions, and emphasis from two witnesses (emph.py)
- Göschel and Marheineckes (p. 2) are Schwabacher (names, unmarked).  Udødelighed p. 64 is Fraktur.  „Freder. Christ.
  Sibbern“ in the p. 451 note is Fraktur: the names-in-Schwabacher rule holds in Møller's own text, not in the German
  quotation.  The header now says so; transcription.tex was rebuilt and reinstalled (compile 0 errors).
- **Stewart's translation** (Jensen & Stewart, Brill 2022) states its textual source as MfL 17 (1837), pp. 1-72 and
  422-453, and marks the MfL page breaks with „|“ plus the page in the margin.  The PDF states no convention for
  emphasis.  It italicises PROPER NAMES (~25: Richter, Magdeburg, Breslau, Marheineke, Göschel, Hegel, Leibniz …), which
  is consistent with the Schwabacher names; titles and foreign words (a priori ×40, raisonnement, ennui …) are also in
  italics.  Only 3 italic runs are English emphasis: „the Christian tradition“ (p. 40, the term), „actual existence“
  (p. 70 = virkelig Tilværelse), „something immortal“ (p. 425 = noget Udødeligt).
- **The 1856 resetting's letterspacing** (tesseract TSV of ES V, ocr1856.py TSV=1): a word's box width is compared with
  the width predicted from its letters (least squares), and a candidate also needs wide gaps between its letters.
  Calibrated on „virkelig Tilværelse“ (spaced in 1856: width ×1.33, gaps 0.21–0.23, against 0.06–0.09 elsewhere).
  Candidates are mapped to the 1837 text by letter alignment and kept only if the letters agree: 12.
- Candidates: `.parts/emph/candidates.tsv`, 14 rows.  Both witnesses: virkelig p. 70 (already bold) and noget p. 425.
  1856 only: Tilværelse p. 70 (bold), Udødeligt p. 425, Ogsaa p. 4, udtalt p. 8, sensu p. 31 (antiqua?), vilde p. 31,
  tilsyne p. 34, radical p. 65, findes p. 67, føres p. 423, Perfectibilität p. 451 (antiqua).  Stewart only: christelige
  (Tradition) p. 40.  Sheet for Hans: `.render/review/udo-emph.png` (reference strips first, then the 14 candidates,
  both-witness first; each word underlined below).  Script: `ebook-method/udoedelighed/emph.py`.
- **Hans's verdict on the 14 candidates** (at the 1837 image): emphasis in Schwabacher at „virkelig Tilværelse“ p. 70 and
  „noget Udødeligt“ p. 425 (both words, across the line break; added as a vote-fixes line + FACE_OK).  Plain Fraktur:
  Ogsaa p. 4, udtalt p. 8, vilde p. 31, tilsyne p. 34, christelige p. 40, radical p. 65, findes p. 67, føres p. 423,
  Perfectibilität p. 451.  „sensu strictissimo“ p. 31 is antiqua (already \textit).  The header's CONVENTIONS now state
  how emphasis was established.  Rebuilt and reinstalled; compile 0 errors.  Playbook §6 has the lesson.
