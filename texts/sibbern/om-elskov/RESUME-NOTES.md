# RESUME-NOTES — Sibbern, *Om Elskov eller Kjærlighed imellem Mand og Qvinde*

State for the **transcription** of this book. Update after each batch.
The user compiles/commits/pushes — never the assistant.

## TRANSLATION (English) — `translation.tex`

Source of truth for the English version is the finished `transcription.tex`
(no need to reconsult the scan). Compiles cleanly in the sandbox with the
substitute recipe (lmodern / drop libertinust1math + textalpha / Greek→`[Gr.]`).

**Conventions** (also in the file header):
- **Elskov vs Kjærlighed:** both → "love"; when contrasted or the word
  choice matters, the Danish is bracketed — love [Elskov], love [Kjærlighed].
- 1819/1858 register kept but readable; long periods preserved, broken only
  where English demands. Paragraphing follows the transcription.
- German (Goethe), Greek, Latin left in original + English gloss footnote.
- Printed section rules reproduced as `\rule`. Proverb inversion
  "love makes seeing" (vs *Kjærlighed gjør blind*) footnoted.
- Chapter names: Preface to the Second/First Edition, Postscript to the
  Third Edition, First/Second/Third Book.

**Translation batch log**
- **2026-07-12 (T1)** — Preamble + title + Translator's note + all front
  matter (both Prefaces, Goethe verse w/ gloss, Gabrielis footnote,
  Postscript). Compiles.
- **2026-07-12 (T2)** — First Book, printed pp. 1–10 (transcription lines
  218–441; 5 paras, ending "One must live oneself into love [Kjærlighed].").
- **2026-07-12 (T3)** — First Book, printed pp. 11–20 (lines 443–657, ending
  "Never is the deep poverty of the I-hood felt sooner."). Compiles: 19 pp.
- **2026-07-12 (T4)** — First Book, printed pp. 21–30 (lines 659–851, ending
  "…not merely to love, but also to be loved in return with the same
  inwardness."). Includes the Plato *Symposion* (203) block quote on Eros
  (Poros/Penia) and μανία θεία w/ gloss; Tiresias reference left unglossed.
  Compiles: 24 pp.
- **2026-07-12 (T5)** — First Book, printed pp. 31–40 (lines 853–1065): jealousy
  and earthly precariousness, confiding/Fortrolighed, conscience (Goethe "wedded
  to his conscience"), the beloved as priest/priestess, love's earthly roots,
  marriage & family, transition to Nature. Ends "…a glance over the whole of
  Nature leads."
- **2026-07-12 (T6)** — First Book, printed pp. 41–50 (lines 1067–1298): Nature
  individualizes into two sexes; the third individual; union primary /
  procreation secondary; the natural drive not to be disdained (John 16:21);
  purity & ἀκολασία (gloss); bashfulness/Blyhed; outward reticence. Ends
  "…bashful and reserved with their love in social intercourse." Compiles: 35 pp.
- **2026-07-12 (T7)** — First Book, printed pp. 51–60 (lines 1300–1525): lovers'
  jest/play and its psychology (Tieck's Phantasus); love should not burn in
  restless craving (Jean Paul on Greek "plastic calm"; Schiller's Thekla);
  **section rule at line 1414** reproduced; the recapitulation of love's
  fullness; esteem/Agtelse; love as genial in origin (τὸ δαιμόνιον, Plato);
  cognition + will; resolution as the root of fidelity. Ends "…fidelity has
  its root and its seat." Includes footnote flagging the odd "contrasterer
  besmere." Compiles: 40 pp.
- **2026-07-12 (T8)** — First Book, printed pp. 61–69 (lines 1527–1725):
  fidelity (Troskab) and the ruin of infidelity; endurance of love into old
  age; the exclusive bond vs. the "envy-free mind" (ἀφθονία); loving with a
  sense of freedom; the long meditation on love in the life to come. Closing
  **section rule at line 1726** reproduced. **FIRST BOOK COMPLETE.** Compiles:
  45 pp.
- **Fix (T7 revisited):** removed `\textgreek{…}` wrappers everywhere — they are
  undefined; Greek is now typed inline (ἔρως, μανία θεία, ἀκολασία, τὸ
  δαιμόνιον, ἀφθονία), matching transcription.tex + textalpha. NB the sandbox
  lacks textalpha, so local Greek issues won't surface in the sandbox
  compile-check — trust the transcription's setup.
- **2026-07-12 (T9)** — Second Book opening, printed pp. 70–79 (lines 1735–1944):
  the fruit-tree image; going into marriage heedlessly; the two periods of life
  (youthful vs. later love; "better to marry than to suffer ardour", pio animo);
  don't hurry / long engagement. `\chapter*{Second Book.}` added.
- **2026-07-12 (T10)** — Second Book, pp. 80–89 (lines 1946–2163): the "higher
  verdict" and marriage "concluded in heaven"; growth takes time (corpora tantum
  soluta agunt); betrothal as trial of souls; egoism after possession; free
  intercourse of the sexes. **Section rule at 2095** reproduced; then the three
  grounds of unfitness — sex, age, station — through the difference of sex
  (Clärchen at Egmont's feet).
- **2026-07-12 (T11)** — Second Book, pp. 90–99 (lines 2165–2407): difference of
  station (mésalliance) and of age; **section rule at 2232**; love "makes seeing"
  even of the beloved's faults (build not on sand); marriage as a calling, duties
  & small irritations, "one place… his home"; total vs. one-sided shared life,
  "even Eros's service must not be desecrated." Compiles: 63 pp.
- **2026-07-12 (T12)** — Second Book, pp. 100–110 (lines 2409–2647): the
  "substrate/basis" a shared spiritual life needs; working with vs. for each
  other (country life); the calling (Schiller's Bride of Messina); "let the
  woman learn to serve" (Goethe) and her rightful disposal in the house; the
  earthly heaven-kingdom is no earth-kingdom (Wilhelm Meister on the
  wedding-feast); against petty egoism undermining the home's basis.
- **2026-07-12 (T13)** — Second Book, pp. 111–119 (lines 2651–2868): opens with
  **section rule at 2649**; the struggle of individualities & love as passion;
  jealousy's first shape (maintaining the I) — "egoism's devil," the unclean
  spirit & seven spirits, love turning to hatred; then jealousy proper toward a
  third person.
- **2026-07-12 (T14)** — Second Book, pp. 120–129 (lines 2870–3024): freedom as
  love's element (Goethe, Aus meinem Leben); how little the morbid love is
  genuine; the desert-island wish; resignation and "power made strong in the
  weak"; "other gods besides the Lord" — love must not be idolized. **Closing
  section rule at 3026. SECOND BOOK COMPLETE.** Compiles: 78 pp.
- **2026-07-12 (T15)** — Third Book opening, printed pp. 130–140 (lines
  3035–3261): Eros of mixed origin; the truly unhappy love (mismatch / lukewarm
  vs. still-vehement); when to keep or break the bond; the ethics & policy of
  divorce ("marriage, like the Sabbath, is there for man's sake"; 1 Cor 7:5 w/
  Greek διὰ τὴν ἀκρασίαν ὑμῶν). `\chapter*{Third Book.}` + **section rule at
  3079** added.
- **2026-07-12 (T16)** — Third Book, printed pp. 141–149 (lines 3263–3484):
  duty vs. right to separate; fidelity to the person (1 Cor 7:16 quote); the
  amicable divorce and its inner truth; betrothal vs. marriage; being made
  another's "prey" in youth; take no resolution in vehemence ("Deliver us from
  evil"). Ends before **section rule at 3486**. Carries the inline FLAG for
  "uskikker"/"unfit" (p. 149). Compiles: 89 pp.
- **2026-07-12 (T17)** — Third Book, printed pp. 150–156 (lines 3488–3619): love
  vs. duty to parents; entering a union "with suppression of the heart's best
  feelings" as profanation; the rare case where need may justify sacrifice; the
  breach with beloved parents. Opens after **rule 3486**, ends at **rule 3621**.
- **2026-07-12 (T18)** — Third Book, printed pp. 157–160 (lines 3623–3785): the
  hopeless love (haabløs Elskov) — Goethe's "these sorrows' secretly forming
  power"; philosophic love holding the image free of desire; bitterness/jealousy
  again; activity as the freeing condition. Opens with **rule 3621**, ends before
  **rule 3787**.
- **2026-07-12 (T19 — FINAL)** — Third Book, printed pp. 160–173 (lines
  3789–3977): bereavement & death — pain and consolation through memory;
  separation as transfiguring; living on for the departed (Goethe's Tasso /
  Eleonore); suffering as dispensation not fate; Plato's *Phaedo* ("to die… the
  wise man exercises himself in"); the closing on "the God in whom we all are,
  live and are moved." Opens with **rule 3787**, ends with the book's final
  **rule 3979**.

## ✅ TRANSLATION COMPLETE
Front matter + First, Second and Third Books all translated (T1–T19).
Whole `translation.tex` compiles in the sandbox substitute recipe: **101 pp.,
exit 0**. Compile locally with libertinus + textalpha for the real typesetting.
Two inline translator FLAGs remain for Hans's eye: the odd "contrasterer
besmere" (Book I) and "uskikker"/"unfit" (Book III) — both trace back to
uncertain readings already flagged in transcription.tex.

Possible follow-ups (not yet done): a light proofreading/consistency pass over
the whole translation; add a "Translation" link to the catalog.yaml om-elskov
entry once translation.pdf is built & pushed.

---

## Edition & source

- Scan: `~/bibliotek/Sibbern, Frederik/Om_elskov_eller_Kjærlighed_imellem_mand.pdf`
  (Google Books, Univ. of Wisconsin copy, 198 PDF pages, has an OCR text layer).
- **Edition: "Tredie uforandrede Udgave," Kjøbenhavn 1858** (Paa eget Forlag,
  trykt hos J. H. Schultz). *Uforandrede* = unchanged, so the text equals the
  1st edition (1819). Google's "1819" metadata refers to the work, not this printing.
- Typography: the **whole book is Fraktur** (prefaces and body alike; the earlier
  note that the body was roman was wrong). Google's OCR of this printing is
  surprisingly good, but verify every page against the image — Fraktur confusions
  (long-s, b/d, u/n, B/V) are common. No letterspaced (Sperrung) emphasis seen in
  pp. 1–10.

## Page map (important)

`printed page = PDF page − 16`  →  Første Bog p.1 = PDF 17.

**⚠ BINDING ERROR in the scan — printed pp. 41–56 are out of order in the PDF.**
The rule `printed = PDF − 16` holds for pp. 1–40 and again from p. 57 on, but
pp. 41–56 are shuffled (two 8-page sheets have their halves swapped). Correct
reading order (printed → PDF):

    41→61  42→62  43→63  44→64
    45→57  46→58  47→59  48→60
    49→69  50→70  51→71  52→72
    53→65  54→66  55→67  56→68
    then 57→73, 58→74, … back to printed = PDF − 16.

Verified page seams flow continuously in printed order. Transcribe in PRINTED
order, not PDF order.

| Section | Printed pp. | PDF pp. | Type | Status |
|---|---|---|---|---|
| Title page | — | 9 | Fraktur | done (in title block) |
| Fortale til anden Udgave | III–V | 11–13 | Fraktur | **done** (+ Goethe verse, dated 1 Nov 1853) |
| Fortale til første Udgave | V–VIII | 13–16 | Fraktur | **done** (dated 12 Dec 1819) |
| Efterskrivt ved tredie Udgave | VIII | 16 | Fraktur | **done** (dated 26 Apr 1858) |
| Første Bog | 1–69 | 17–85 | Fraktur | **COMPLETE (pp. 1–69)** |
| Anden Bog | 70–129 | 86–145 | Fraktur | **COMPLETE (pp. 70–129)** |
| Tredie Bog | 130–173 | 146–189 | Fraktur | **COMPLETE (pp. 130–173)** |
| Publisher's book-list ad | — | 190–198 | Fraktur | **NOT transcribed** (bookseller's catalogue of Sibbern's works — not part of the text; no "Indhold" section exists) |

**⚠ Page-map correction:** the earlier estimate "Tredie Bog 130–164, Indhold
165–174" was wrong. Book III body runs to printed **p. 173** (PDF 189, offset
−16 throughout). PDF 190+ is a *"Af følgende Skrivter af Professor Sibbern…"*
bookseller's advertisement, not part of the work. **The transcription of the
whole book (all three Books + front matter) is now COMPLETE.**

## Transcription conventions

- LaTeX `book` class, libertinus (matches the other transcriptions in this repo).
- **Preserve 1858/1819 orthography verbatim**: Kjærlighed, Qvinde, aa (not å),
  Sjæl, Elskov, doubled consonants, capitalised nouns, etc. Do NOT modernise.
- Danish low-high quotes „…“ kept as printed. Em-dash `---`. `\emph{}` for
  letterspaced emphasis in the original.
- Reading text: no inline printed-page numbers (matches house practice); running
  heads via `\markboth`.

## OCR pipeline (for the roman body)

1. `pdftotext -f <PDF> -l <PDF> scan.pdf -` gives a strong draft for roman pages.
2. Correct against a rendered image:
   `pdftoppm -f <PDF> -l <PDF> -r 150 -png "<scan>" /tmp/pg`
   then read the PNG. Recurring OCR errors seen: J↔I (Jo→Fo), R→K (Rørende→Kørende),
   long-s artefacts, „ / “ confusion, stray periods.
3. Compile check: `latexmk -pdf transcription.tex` (needs libertinus + Danish
   babel; the sandbox used for drafting lacks libertinus, so compile locally).

## Batch log

- **2026-07-12** — Scaffold created: preamble, 1858 title page, and *Fortale til
  anden Udgave* pp. III–IV (image-verified from PDF 11–12).
- **2026-07-12 (batch 2)** — Completed all front matter, image-verified from PDF
  13–16: rest of *Fortale til anden Udgave* (Goethe verse + signature),
  *Fortale til første Udgave* (V–VIII, with the Gabrielis footnote), and the
  *Efterskrivt ved tredie Udgave*. Structure compiles (6 pp. with font
  substitute). Catalog `om-elskov` set to in-progress with transcription link.
  **Next: Første Bog, printed pp. 1–69 (PDF 17–85), in ~10-page batches.**
- **2026-07-12 (batch 3)** — Første Bog pp. 1–10 (PDF 17–26), image-verified;
  five paragraphs, ends mid-paragraph with a continuation marker at p. 11.
  Compiles (12 pp. with font substitute). Three ambiguous Fraktur glyphs resolved
  by sense — **spot-check against the scan**: p. 6 "Vederqvægelse" (cap V/B),
  p. 7 "fordi han skuer" (b/d), p. 9 "Tilværelsens indre Væsen" (u/n). Kept
  archaic forms as printed (e.g. "jordiskt Lys", "altfor"/"alt for").
  **Next: printed pp. 11–20 (PDF 27–36).**
- **2026-07-12 (batch 4)** — Første Bog pp. 11–20 (PDF 27–36), image-verified.
  Re-added `\usepackage{textalpha}` to the preamble: p. 18 has Greek θεῖόν τι.
  Recurring b/d Fraktur habit confirmed — Sibbern's "fordi" reads like "forbi";
  transcribed as "fordi" throughout (pp. 17, 20). Compiles (17 pp. w/ substitute).
- **2026-07-12 (batch 5)** — Første Bog pp. 21–30 (PDF 37–46), image-verified.
  More Greek: p. 28 μανία θεία. Contains a block quote from Plato's *Symposion*
  (403), pp. 28–29, kept in „…“. Compiles (22 pp. w/ substitute).
  **Spot-check when proofing:** p. 21 "den Elskende, i sig Følelsen af sin
  Mangelfuldhed" (read e/en by sense; page also has stray reader pen-marks);
  p. 30 "Bryndefulde" (Brynde = ardour; glyph faint). Also confirmed cases
  fixed by sense: p. 22 "afsondrede", p. 26 "Riddertid", p. 27 "sød Nydelse".
  **Next: printed pp. 31–40 (PDF 47–56).**
- **2026-07-12 (batches 6–9)** — Første Bog pp. 31–69 completed, image-verified.
  **Discovered the binding scramble** (pp. 41–56; map recorded above) and
  transcribed in printed order. Greek added on pp. 47 (ἀκολασία), 59
  (τὸ δαιμόνιον), 65 & 69 (ἀφθονία). Section dividers (printed rules) on pp. 55
  and at the end of Første Bog rendered as centered \rule. **FIRST BOOK COMPLETE.**
  Whole file compiles (42 pp. w/ substitute).
  Fraktur readings resolved by sense (spot-check when proofing): p. 51/52
  "contrasterer besmere" (odd — flagged inline in the .tex); p. 61 "ødende",
  p. 65 "Frihedssands", p. 66 "Omdømme", p. 69 "udeelt" (all b/d or ſ/f fixes).
  **Next: Anden Bog — chapter heading at PDF 86 (printed p. 70, unnumbered),
  body printed pp. 70–129 (PDF 86–145), all offset −16 (scramble is over).**
- **2026-07-12 (batches 10–12)** — Anden Bog pp. 70–99 done, image-verified.
  Chapter heading rendered \chapter*{Anden Bog.}. Latin phrases kept as printed
  (pio animo; corpora tantum soluta agunt; en religio; Inertie). Section dividers
  (printed rules) on pp. 86 and 93. Compiles (58 pp. w/ substitute).
  b/d and B/V fixes by sense (spot-check): p. 76 "blødt", p. 84 "lunknes",
  p. 95 "Virkekreds" (×2, was B), p. 99 "Omdømmet"; "herrisk(t)" kept as printed
  (pp. 89, 90). **Next: Anden Bog pp. 100–129 (PDF 116–145).**
- **2026-07-12 (batches 13–15)** — Anden Bog pp. 100–129 done, image-verified.
  **SECOND BOOK COMPLETE.** Section divider on p. 112; Anden Bog ends with a rule.
  Goethe refs kept as printed (Aus meinem Leben; Wilhelm Meister; "Qvinden lære
  at tjene"). Compiles (74 pp. w/ substitute). Fixes by sense (spot-check):
  p. 123 "Fordring" ×2 (printed "Forbring", b/d), p. 128 "Stræben" (OCR "Sptren"),
  p. 129 "fordrende" (printed "forbrænde"), p. 125 "ulykkelige". Two ink-blots in
  the scan: p. 122 "idelig" and p. 128 "Jalousie" (read from context).
  p. 107 "Menneskelivvær" appears to be a Sibbern coinage — left as printed, verify.
  **Next: Tredie Bog — printed pp. 130–164 (PDF 146–180); chapter heading at
  PDF 146 (printed 130, unnumbered), then offset −16.**
- **2026-07-12 (batch 16)** — Tredie Bog opening, pp. 130–139 (PDF 146–155),
  image-verified. Inserted `\chapter*{Tredie Bog.}`. Eros of mixed origin;
  unhappy love; Skilsmisse (divorce). Greek 1 Kor 7:5 quote. Spot-check flags:
  p. 133 "Lænke" (printed like "Længe"); pp. 134–135 "Skilsmisse(rs)".
- **2026-07-12 (batch 17)** — Tredie Bog pp. 140–149 (PDF 156–165),
  image-verified. Divorce/Skilsmisse casuistry; 1 Kor 7:16 Danish quote. OCR
  fixes by image: p. 144 "er just **ei** altid" (OCR "et" — dot-over confirms
  i); p. 145 "medføre **Beføielsen**" (OCR "Besøielsen"); p. 143 "Qvide" (OCR
  "Ovide"). One inline FLAG: p. 149 "uskikker" (perhaps "uskikkelig/uskikket").
- **2026-07-12 (batch 18)** — pp. 150–159 (PDF 166–175), image-verified. Two
  section rules added: after p. 150 ("Frels os fra det Onde" para) and after
  p. 156, before the new subsection **"Vi komme nu til den Art af ulykkelig
  Kjærlighed"** (haabløs Elskov). Goethe quote p. 158 („disse Smerters…").
  p. 154 "Existentsens inderste **Rod**" (OCR "Nod").
- **2026-07-12 (batch 19)** — pp. 160–165 (PDF 176–181), image-verified. Section
  rule after p. 164 (before "Men naar vi saaledes…"). Greek θεῖον p. 165.
  Discovered the body runs past the old "164" estimate.
- **2026-07-12 (batch 20 — FINAL)** — pp. 166–173 (PDF 182–189), image-verified.
  Death/Døden and Plato's *Phaedo* ("At døe…") close the book; final centered
  rule = book-end ornament. **TREDIE BOG COMPLETE → whole book done.** Full file
  compiles cleanly in the sandbox with the substitute recipe (lmodern / english
  babel / Greek→placeholder): **97 pp., exit 0**. Compile locally with
  libertinus + Danish babel + textalpha for the real typesetting.
