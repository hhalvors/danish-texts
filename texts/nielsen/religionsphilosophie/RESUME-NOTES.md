# Rasmus Nielsen — *Religionsphilosophie* (1869): transcription resume notes

**Phase 1 (transcription) job.** Read this, then the two standing-method files, then
continue the batch loop.

---

## SESSION PROTOCOL — read this first, it is about cost

This job's cost is dominated by **context replay**, not by the transcribing. A
two-up scan render is ~2,800 tokens and stays in context forever; the LaTeX output
is only ~500 tokens per page. Working 2 pages per turn in a long-running session
meant paying roughly 30× the irreducible cost per batch. The rules below exist to
stop that. Follow them.

1. **Start each sitting in a FRESH conversation.** Do not continue a session that
   has already done a batch or two. Cold start ≈ 15k tokens; a session twenty
   batches deep is 150k+, mostly retained page images.

2. **Never read `transcription.tex` whole — it is >560 KB.** To resume, read only
   the tail: `tail -60 transcription.tex`. The status block near the top of the
   file names the resume page; `check.py` prints it too.

3. **Twelve pages per turn, not two.** Inside one turn the marginal cost of another
   page is just its image. `bash batch.sh <first>` renders six two-ups in one call
   and prints the verification report at the same time.

4. **One edit per batch.** Write all twelve pages in a single `Edit`, appending
   before `\end{document}`. Do not edit page-by-page.

5. **Zoom only on real doubt.** No routine confirmation zooms. When several
   readings are doubtful, `montage` the crops into ONE image and read it once.
   (ImageMagick crop offsets are pixels even when written with `%` — see below.)

6. **Bookkeeping every ~20 pages, not every batch.** The status block in
   `transcription.tex` and the resume line in this file do not need touching after
   each batch.

So the per-batch loop is: `bash batch.sh N` → read six PNGs → one `Edit` → next
turn `bash batch.sh N+12` (which verifies what you just wrote and renders ahead).

**Do not use the OCR text layer as a draft.** Checked and rejected: `pdftotext`
returns scrambled reading order and character-level errors ("psycliologisk"), so
correcting it costs more than transcribing from the image.

---

## The two standing methods
- **Transcription discipline:** follow `../grundideernes-logik/RESUME-NOTES.md`
  (image-verified LaTeX: Sperrsatz → `\emph{}`, Danish quotes, footnotes,
  page-break comments, portable verify compile, balance checks).
- (Phase 2, later: translation via `../../../TRANSLATION-PLAYBOOK.md`.)

## This book, concretely
- **Title:** *Religionsphilosophie*, af R. Nielsen. Kjøbenhavn: Forlagt af den
  Gyldendalske Boghandel (F. Hegel), I. Cohens Bogtrykkeri, 1869.
- **Scan:** `~/bibliotek/Nielsen, Rasmus/religionsphilosophie.pdf` — Det Kgl.
  Bibliotek, **557 PDF pp.**, 177 MB. Copied into this folder as `scan.pdf`
  (gitignored). Sidecars in bibliotek: `religionsphilosophie.txt` (raw pdftotext),
  `religionsphilosophie_clean.txt` (cleaned; **strips page numbers** — not usable
  for locating printed pages), plus `extract_*.py` / `clean_*.py`.
- **Script:** **Antiqua** (Latin type) throughout — not Fraktur. Emphasis is
  **Sperrsatz** (letterspacing), which is invisible in the OCR text layer, so every
  page must be checked against the image.
- **OCR quality: poor.** Word order is scrambled on many pages, and letters are
  routinely misread ("Prinoiper", "Villi es", "Sønn en's Væ s en", "livad",
  "Eorskjellen"). Use the text layer only as a crutch; transcribe from the image.
- **Offset (VERIFIED): PDF = printed + 13.** printed p.1 = PDF 14; p.17 = PDF 30;
  p.42 = PDF 55; p.56 = PDF 69; p.82 = PDF 95; p.538 = PDF 551.
  Title leaf = PDF 8; preface theses (undated body, signed "Kjøbenhavn, den 28de
  December 1868. R. Nielsen.") = PDF 10.
- **Extent:** body printed pp. **1–537** (KB catalogue records "537 s.").
- **catalog.yaml:** id `religionsphilosophie`, status in-progress.

## Front matter, as bound in this scan
- PDF 1–7: KB digitisation notice, marbling, stamps, blanks.
- PDF 8: title page. PDF 10: the five preface theses + date + signature.
- PDF 11–13: **Indhold** — but only three leaves, beginning mid-way at
  "c) Faderens Personlighed. § 9 … 129". **The first Indhold leaf (covering the
  Indledning through § 8) is missing from this scan.** The structure below was
  therefore reconstructed from the running text, not from the Indhold.
- PDF 551 (printed 538): **RETTELSER** (errata). None of the errata touch pp. 1–81;
  they affect pp. 130, 257, 284, 400, 508, 592 — see "Errata" below.

## Structure of the INDLEDNING (printed pp. 1–81)
Section head `INDLEDNING.` on p.1, then centred bold sub-heads, each followed by a
centred `§ N.` marker:

| Sub-head | § | printed pp. | PDF pp. |
|---|---|---|---|
| *(unheaded opening paragraph)* | — | 1 | 14 |
| Religion og Philosophie | § 1 | 1–10 | 14–23 |
| Religion og Mythologie | § 2 | 11–22 | 24–35 |
| Aabenbaring og Tro | § 3 | 23–41 | 36–54 |
| Ordet og Aanden | § 4 | 42–55 | 55–68 |
| Troesprincipet: Religionsphilosophiens Methode | § 5 | 56–81 | 69–94 |

Third-level divisions are inline italic run-heads of the form
`a) Ordets Oprindelighed.`, `b) Ordets Troværdighed.`, `c) Aabenbaringens
Tilegnelse i Troen.`, `a) Troen og dens Indhold.`, `b) Troesbekjendelsen.` — these
are centred italic lines in the setting, rendered in the existing transcription as
`\noindent\textit{a) …}` between `\medskip`s.

The Indledning closes on p.81 by announcing the tripartite plan: "…deling ved: Tro
paa Faderen, Tro paa Sønnen og Tro paa Aanden."

## Structure of the body (after the Indledning)
- **Tro paa Faderen** — § 6 begins printed p.82 (PDF 95).
  A. Faderens Væsen … c) Faderens Personlighed § 9 (129); B. Faderens Gjerninger
  § 10 (149) — a) Skabelsen § 11 (151), b) Opholdelsen § 12 (165), c) Styrelsen
  § 13 (179); C. Faderens Rige § 14 (200) — a) Ideal og Virkelighed § 15 (201),
  b) Verdensidealer § 16 (224), c) Gudsrigets Ideal § 17 (256).
- **Tro paa Sønnen** — A. Sønnens Væsen § 18 (272): a) Selvet i Sønnen § 19 (273),
  b) Grundbestemmelser i Sønnens Selv § 20 (304), c) Sønnens Personlighed § 21 (321).
- **Tro paa Aanden** — … b) Grundbestemmelser i Aandens Selv § 32 (458) …
  (full detail on PDF 13; the § 22–31 leaf is present, § 1–8 leaf is not.)

## STATE OF PLAY (as of 2026-08-02)

**The live file is `transcription.tex` in this folder — one file for the whole
book.** Done and image-verified: title leaf, preface theses, and printed
**The INDLEDNING IS COMPLETE — pp. 1–81, §§ 1–5.** In *Tro paa Faderen* /
*A. Faderens Væsen*: § 6 (p.82), *a) Selvet i Faderen* with § 7 (p.83), then
*α) …fra Videns Standpunkt* (p.84) and *β) …fra Troens Standpunkt* (p.88).
…and *γ) Det faderlige Selv: Mysteriet* (p.97). § 7 closes on p.107; *b)
Grundbestemmelser i Faderens Selv* with § 8 opens p.108, subdivided by
*α) Det Absolutes Attributer* (p.109), *β) Opløsningens Betydning for
Videnskaben* (p.116) and *γ) Den religiøse Theisme: Grundbestemmelser i det
faderlige Selv* (p.120). § 8 closes on p.129; *c) Faderens Personlighed* with § 9
opens p.129 — the last of the three run-heads under *A. Faderens Væsen* —
subdivided by *α) Idealet af Høihed* (p.133), *β) Idealet af Kjærlighed* (p.138)
and *γ) Salighedsidealet* (p.143). *A. Faderens Væsen* closes p.148.

**B. Faderens Gjerninger** (§ 10) opens p.149, with *a) Skabelsen* (§ 11, p.151)
and its three Greek heads: *α) Den videnskabeligt naturalistiske Anskuelse:
Kosmogonie* (p.152), *β) Den bibelsk religiøse Anskuelse: Skabelse i sex Dage*
(p.154), *γ) Skabelse og Kosmogonie: Mysteriet* (p.157).
*b) Opholdelsen* (§ 12) opens p.165, with *α) Skabelse og Opholdelse* (p.166),
*β) Opholdelse og Naturproces* (p.170) and *γ) Opholdelsens Mysterium* (p.174).
*c) Styrelsen* (§ 13) opens p.179, with *α) Styrelsen og Verdensløbet* (p.181),
*β) Det aabenbarede Ord om Forsynets Styrelse* (p.185) and *γ) Tro paa det
styrende Forsyn* (p.191). **C. Faderens Rige** (§ 14) opens p.200 — the last of
the three lettered divisions of *Tro paa Faderen*.
Within it, *a) Ideal og Virkelighed* (§ 15, p.201) with *α) Uskyldighedsidealet*
(p.201), *β) Fristelse og Fald* (p.207) and *γ) Forbandelsen* (p.217); then
*b) Verdensidealer* (§ 16, p.224) with *α) Den faldne Slægt* (p.226),
*β) Verdensguderne* (p.238) and *γ) Denne Verdens Fyrste* (p.245); then
*c) Gudsrigets Ideal* (§ 17, p.256) with *α) Udvælgelsen: det udvalgte Folk*
(p.256).
*β) Lovgivningen: Theokratiet* opens p.260. (The Indhold reads this head as
"Timokratiet"; the page itself reads **Theokratiet** and is followed.)
and *γ) Forjættelsen: Messiasidealet* (p.267).

### ✅ TRO PAA FADEREN IS COMPLETE — pp. 82–271, §§ 6–17

**TRO PAA SØNNEN opens p.272** with *A. Sønnens Væsen* (§ 18); *a) Selvet i Sønnen*
(§ 19, p.273) with *α) Det menneskelige Selv* (p.274), *β) Det guddommelige
Selv* (p.286) and *γ) Det gudmenneskelige Selv: Mysteriet* (p.295). § 19 closes
p.304; *b) Grundbestemmelser i Sønnens Selv* with § 20 opens p.304, subdivided
by *α) Sønnens Selv er Logos* (p.305), *β) I Sønnens Selv er Livet* (p.310) and
*γ) Sønnens Selv er Verdens Lys* (p.317). § 20 closes p.321; ***c) Sønnens
Personlighed* with § 21 opens p.321** — the last of the three run-heads under
*A. Sønnens Væsen* — subdivided by *α) Personlighedens Metaphysik* (p.322),
*β) Personlighedens Aabenbarelse* (p.324) and *γ) Personlighedens evige Liv*
(p.331). Transcribed to p.346. The Indhold was exact seventeen times running
(295 / 304 / 305 / 310 / 317 / 321 / 322 / 324) before it ran out; **p.331 is
the first head found by reading alone**, and it fits the α/β/γ series exactly.

### ✅ A. SØNNENS VÆSEN IS COMPLETE — pp. 272–340, §§ 18–21

**B. Sønnens Gjerninger** (§ 22) opens **p.340**, with *a) Lovens Opfyldelse*
(§ 23, p.343) and *α) Lovens Aand* (p.344). p.344 announces the α/β/γ series
outright — "en Belysning af *Lovens Aand*, af *Evangeliets Lov*, af *Lovens
Ende*" — so β) and γ) are named in advance; likewise p.343 announces the three
lettered heads of § 22: *Lovens Opfyldelse, Forsoningen og Forløsningen*. **Use
those two sentences as the navigation the Indhold no longer supplies.**

**Both predictions have now come true**: *β) Evangeliets Lov* opens **p.349** and
*γ) Lovens Ende* opens **p.354**. § 23 closes p.361; ***b) Forsoningen* with § 24
opens p.361**, as the p.343 sentence predicted. Transcribed to p.370.

**⚠ CORRECTION to a note written after the pp.359–370 batch.** I had recorded
that "the α/β/γ series is NOT invariable", on the ground that § 24's announcing
sentence on p.363 named only two heads. **That was wrong.** The sentence reads:

> "Ved at betragte Forsoningslæren først fra den *scholastisk-objective* og
> dernæst fra den *mystisk-subjective* Side bane vi os Vei til en Indsigt i
> ***Forsoningens dobbeltsidige Væsen***."

The final clause is not a summary — it is the title of the third head, which
duly appears as *γ) Forsoningens dobbeltsidige Væsen* on **p.372**. So § 24 has
three heads like every other §, and the announcing sentence named all three.
**The series has still never broken.** Read the whole sentence, including its
final clause, before counting.

§ 24's heads: *α)* p.364, *β)* p.368, *γ)* p.372. § 24 closes p.380;
***c) Forløsningen* with § 25 opens p.380**, and p.383 carries its announcing
sentence — "henføre den hele frelsende, frigjørende Virksomhed til Forløsning
***fra Synd, fra Død, fra Satans Rige***" — naming, again, exactly three heads:
*α) Fra Synden* (p.383), *β) Fra Døden* (p.390), *γ) Fra Satans Rige* (p.393).
All three appeared where promised.

### ✅ B. SØNNENS GJERNINGER IS COMPLETE — pp. 340–399, §§ 22–25

**C. Sønnens Rige** (§ 26) opens **p.399** — the last of the three lettered
divisions of *Tro paa Sønnen*. p.401 carries its announcing sentence — "opfatte
Sønnens Rige som ***Frihedens, Kjærlighedens*** og ***Salighedens*** Rige" —
naming three lettered heads; *a) Frihedens Rige* (§ 27) opens p.401. p.403 then
announces § 27's own three Greek heads: "anskueliggjøre Frihedens
***Grundbetingelser, Vilkaar og Byrder***", of which
*α) Frihedens Grundbetingelser: Sædemanden og Jordbnnden* opens p.403.

**Two announcing sentences are nested**, one for the lettered series and one for
the Greek series inside it — and both have now paid out in full:
*β) Frihedens Vilkaar: den forlorne Søn* (p.407), *γ) Frihedens Byrder* (p.410);
then ***b) Kjærlighedens Rige* with § 28 opens p.415**, whose own announcing
sentence (p.416) names three more — "dens *Væsen*, dens *Maal*, dens ydre
*Modstand* d. e. dens *Skranke*" — of which *α) Kjærlighedens Væsen: Had og
Kjærlighed* opens p.416, *β) Kjærlighedens Maal: Verdens Frelse* p.420, and
*γ) Kjærlighedens Skranke: Verdens Had* p.425.

§ 28 closes p.429; ***c) Salighedens Rige* with § 29 opens p.429** — the last
lettered head of *C. Sønnens Rige*, and so the last of *Tro paa Sønnen*. Its
announcing sentence (p.430) names three Greek heads: *α) Verdens Undergang*
(p.430), *β) De Dødes Opstandelse* (p.435), *γ) Dommedag: Salighed og
Fordømmelse* (p.438). **§ 29 closes p.442, and with it *Tro paa Sønnen*.**
Transcribed to p.442.

n.b. the announcing sentence called the third head simply *Dommen*; the head
itself is fuller (*Dommedag: Salighed og Fordømmelse*). The α and β heads match
their announcement word for word, so treat an announcing sentence as naming the
**topic**, reliably, but not always the head's exact wording.

### ✅ TRO PAA SØNNEN IS COMPLETE — pp. 272–442, §§ 18–29

Still to come: the close of § 25, then a *C.* division to finish *Tro paa
Sønnen* before *Tro paa Aanden* around p.458.

**The misbound range is now behind us** — from p.276 the offset is a plain +13
again for the rest of the book. (The `kb()` function still needs to stay in any
check script, since it covers pp.260–275 which are already transcribed.)

**Resume at printed p.443 (PDF 456).** p.442 ends at a full stop with the page
set short, outside any quotation, so the check script should read exactly the
standing balance of 5.

### ⚠ TRO PAA AANDEN OPENS ON p.443 — NOT p.458

The earlier estimate of "around p.458" was wrong: **458 is § 32's page**, taken
from the surviving Indhold leaf's line for *b) Grundbestemmelser i Aandens Selv*,
not the division's opening. Verified on the page image at PDF 456: p.443 carries

```
\parthead{Tro paa Aanden.}
\lettersub{A.}{Aandens Væsen.}
```

so the very first thing the next batch must emit is the third and last
`\parthead`, followed immediately by the `A.` division. `\parthead` issues a
`\clearpage`, which matches the scan (p.442 is set short).

**The Indhold has run out.** Its surviving leaves covered through § 21's second
head (324); *Tro paa Aanden* and § 32 (458) are on PDF 13 but with no
intermediate detail. From p.325 onward the structure is read off the running
text, as it was for the Indledning. Spot-check every run-head against the page.

**Quote balance is 5 — and the arithmetic is no longer naive.** Six openers are
never closed by the printer, and one closer is never opened:

1. the early dropped opener in the p.71 footnote (p.72);
2. the long Strauss quotation running pp.280–282 — no `“` before the footnote
   marker at the end of p.282, verified at 600 dpi;
3. **p.294, the Bethesda quotation** „end mere søgte at slaae ham ihjel … gjorde
   sig selv Gud lig; — the sentence returns to Nielsen's own voice at "følger en
   Udtalelse" with no closing mark. 400 dpi;
4. **p.294 footnote, the Martensen quotation** „De tre første Evangelier … — no
   closing mark after "ogsaa maa have Præexistens." 700 dpi.
5. **pp.349–350, the Hase quotation** — the reverse defect: it opens with no `„`
   at "Verbum divinum absolvitur…" on p.349 but *is* closed after "…til
   Evangeliet“" on p.350. 700 dpi.
6. **p.376, the Strauss/Hegel quotation** „Modsætningen mellem Substans og
   Subject … — never closed; the sentence runs on into Nielsen's own voice at
   "med Alt, hvad derunder maa henføres". 700 dpi.
7. **p.416, the Ideekjærlighed quotation** „den forvandler sig til lutter
   Indhold. — never closed; the next sentence ("I Kjærlighed til Kunst f. Ex.
   …") is already Nielsen's own voice. 700 dpi.

All seven are reproduced as printed, and #5, #6 and #7 are **CONFIRMED BY
COLLATION** against the Bodleian copy.

**⚠ The "dropped openers" line in `check.py` will not catch #5, and that is worth
understanding before trusting the check.** A stray `“` is only recorded there if
the running balance is already 0. Here it simply decrements the four standing
unmatched openers to three. So:

| what | effect on the running balance |
|---|---|
| four never-closed openers (pp.71, 282, 294 ×2) | +4 |
| the p.350 never-opened closer | −1 |
| the p.376 never-closed opener | +1 |
| the p.416 never-closed opener | +1 |
| **standing total from p.416** | **5** |
| a quotation still open at the batch cut | +1 each |

`check.py` now prints the standing figure from a `STANDING` constant — update it
there if another such defect turns up, and keep treating a *second* entry in the
neg list as a genuine transcription error.

**ImageMagick crop offsets must be pixels, not percentages.** `-crop 100%x9%+0+53%`
silently treats the offsets as 53 *pixels*, so you get the page header instead of
the region you wanted. Use `-crop WxH+X+Y` with absolute pixel values taken from
`identify` (a 600 dpi page here is ~2970×4885).

Structure ahead: no more Indhold numbers until § 32 (458). **But the text
announces its own divisions** — p.343 names § 22's three lettered heads (*Lovens
Opfyldelse, Forsoningen og Forløsningen*) and p.344 names § 23's three Greek
heads (*Lovens Aand, Evangeliets Lov, Lovens Ende*). So expect, in order:
β) Evangeliets Lov, γ) Lovens Ende, then *b) Forsoningen* (§ 24) and
*c) Forløsningen* (§ 25), then a *C.* division to close *Tro paa Sønnen* before
*Tro paa Aanden* around p.458. Watch for further such announcing sentences; they
are now the primary navigation.

**The Indhold's page numbers have now been confirmed exact eleven times running**
— 133 / 138 / 143 (§ 9), 149 (§ 10), 151 (§ 11), 152 / 154 / 157 (§ 11's heads),
165 (§ 12), 166 / 170 / 174 (§ 12's heads). The structure reconstructed from the
running text and the fragmentary Indhold leaf agree completely, so the Indhold's
remaining numbers (§ 13 at 179, § 14 at 200, § 15 at 201 …) are reliable
navigation.

A fifth structural device appears inside β): **letterspaced inline run-ins** that
divide the argument without being headings — *Beviis af Ordet.* (p.92), *Beviis af
Aanden.* (p.93), *Troesbeviset.* (p.94). They open a paragraph and run straight
into the sentence, so they take plain `\emph{}`, not `\runhead`. Watch for more.

### ⚠ The 160 dpi two-up can scramble line order — zoom before trusting a sentence

Three times now (pp.379, 393, 405, and again at pp.407/409) a sentence read off
the two-up came out garbled or duplicated, because gutter curvature and
downsampling make adjacent lines interleave. Each time a 400 dpi crop settled it,
and twice I had already written the garbled version into the file before
catching it. **If a sentence does not parse as Danish, the render is at fault,
not the compositor — crop that band at 400 dpi before transcribing or flagging a
`% sic:`.** The dittography sweep in the verification step exists because of
this.

Checks that pass on the current file: 442 page-break comments, contiguous pp.1–442,
every offset correct against `kb()` above; braces balanced; `$` count even; 71
footnotes; 36 `% sic:` notes; 5 `\lettersub` divisions; **8 of the 9 errata
applied** (130, 257 ×4, 284, 392, 400); no lacunae outstanding; exactly one entry
in the dropped-open list and a balance of exactly 5 — the standing figure. The
dittography sweep over the new pages is clean.

**Progress: 442 of 537 body pages = 82.3% — 95 pages left, eight batches.**

**Compile status: `make` confirmed green at the pp. 1–94 state**, which exercised
`\parthead`, `\lettersub` and `\greekrun` (including the Greek α/β/γ markers).

Mathematics has started appearing — the p.48 footnote sets
$\frac{o}{a}=0$ and $\frac{a}{\infty}=0$, and the Hume quotation on p.47 has
$=\frac{9}{10}$. `amsmath` is already loaded.

### Greek

Greek starts at p.59 (ἄνθρωπος ψυχικος, 1 Cor. 2:14). It is typed **directly**, with
`\usepackage{textalpha}` in the preamble — the same convention as every other file
in this repo (`philosophie-og-mathematik`, `philosophiske-grundproblemer`,
`videnskabslaere`, the Sibbern and Høffding texts, etc.). No macro, no conditional.

**This setting is unreliable about Greek accents, and they are reproduced as
printed, not normalised.** Verified at 600 dpi in each case:

| p. | printed | would normally be |
|---|---|---|
| 59 | ἄνθρωπος **ψυχικος** | ψυχικός |
| 99 | μυστήριον | ✓ correct |
| 100 | **ὑπερουσιον** | ὑπερούσιον |
| 116 | δημιουργὸς δίκαιος, θεὸς ἀγαθὸς | ✓ all correct |
| 288 | ἀμην, ἀμην λεγω ὑμιν, πριν Αβρααμ | ἀμήν … λέγω ὑμῖν, πρὶν Ἀβραάμ |
| 288 | ἐγω εἰμι / πατηρ παντων των πιστευοντων | ἐγώ εἰμι / πατὴρ πάντων τῶν πιστευόντων |
| 290 | ἐγενετο | ἐγένετο |
| 302 | κενωσις | κένωσις |
| 307 | κατα κρυφιν / κατα κενωσιν | κατὰ κρυφὴν / κατὰ κένωσιν |
| 309 | ἀρρήτως και ἀνεκδιηγήτως | ✓ acutes correct; only καί bare |
| 316 | κρύψις / Φανέρωσις | ✓ both fully correct |
| 327 | λογος, ζωη, Φως | λόγος, ζωή, φῶς (note the capital Φ) |
| 368 | θεοτόκος (body) | ✓ correct |
| 368 note | Λέγουσι … θεοτόκον | ✓ **the fullest and best Greek in the book** — breathings, acutes, graves and circumflexes all correct, except two bare words: βαστασαντας, διδασκειν |
| 429 | μετανοεῖτε ἤγγικε γὰρ ἡ βασιλεία τῶν οὐρανῶν | ✓ **fully and correctly accented** — circumflexes, acutes, graves, breathings all right |
| 381 | καταλλαγή | ✓ correct |
| 381 | **ἀπαλύτρωσις** | ἀπολύτρωσις — an α where the ο belongs. **Confirmed by collation.** Since καταλλαγή one line above is right, this is a wrong sort, not a habit |

The whole Socinus note on pp.288–290 keeps its breathings (ἀ, ὑ, ἐ, and the
separately-set ’ before Ἀβρααμ in the *second* occurrence only — the first is bare
Αβρααμ) and drops every acute. The cursive kappa **ϰ** appears there and is
normalised to **κ**, on the same footing as ϑ → θ.

Breathings are always present (ἄ, ὑ, ἀ); it is the acute that sometimes goes
missing, and **not systematically** — p.116 sets four words with correct accents
including graves. So check every Greek word against the page individually; neither
"always right" nor "always dropped" is a safe assumption.

The scan's Greek fount uses the script theta **ϑ**; this is normalised to **θ**, as
a fount variant rather than a distinct letter. Flagged in a comment where it occurs.

### Don't make the preamble conditional

An earlier version of this file wrapped `babel`, `libertinus` and `textalpha` in
`\IfFileExists` so that it would compile in a cut-down TeX install. Don't do this:

- It diverges from the ~25 other transcriptions, all of which load the packages
  plainly. The preamble should match `philosophie-og-mathematik` line for line.
- It was actively fatal. `\IfFileExists` stores its branches with
  `\def\reserved@a{...}`, so a bare `#1`/`#2` inside a branch becomes a parameter of
  `\reserved@a` and aborts with *"Illegal parameter number in definition of
  `\reserved@a`"* under TeX Live 2024.

The build target is the author's machine, which has the full TeX Live. A sandbox
that cannot compile the file is not a reason to change the file.

n.b. the p.59 Greek is printed with an accent on the first word and **none** on the
second (no accent over the omicron of ψυχικος). Verified at 600 dpi; reproduced as
printed rather than normalised.

### Two traps worth remembering

**1. Apparent italics in the two-up render.** On left-hand pages the gutter
curvature plus downsampling can make whole paragraphs look slanted. The lower half
of p.33 looked convincingly italic and is plain roman at 420 dpi. **Verify any
suspected italic at ≥400 dpi before marking it.** Genuine italic in this book is,
so far, only Latin tags: *ubique et nusquam* (p.6), *eo ipso* (p.36),
*per subtractionem* / *per additionem* (p.38), *Der christliche Glaube* (p.40 note).

**2. Footnotes can run across a page boundary — this is common, not exceptional.**
Each is transcribed whole at its opening marker, with a comment at both ends so the
page-break comments don't imply a full page of body text where there isn't one:

| note | spans | body text on the overrun page |
|---|---|---|
| Martensen/Schleiermacher | p.39 → p.40 | four lines |
| Kierkegaard, *Efterskrift* | p.71 → p.72 → p.73 | five lines on p.72 |
| Strauss on Fichte and Hegel | p.106 → p.107 | one closing paragraph |
| Strauss on Socinus's exegesis | p.288 → p.289 → p.290 | **two lines** on p.289 |
| Hilarius / Symbolum Nicænum | p.309 → p.310 | lower third of p.310 |
| **Hegel, *Religionsphilosophie*** | p.373 → p.374 → p.375 | **three lines** on p.374 — the longest note in the book |
| Martensen on Lady Macbeth | p.438 → p.439 | four lines; the note interrupts the word *Mulig-hed* mid-break |

## ⚠ MISBOUND LEAF IN THE KB SCAN — pp. 260–275

**The KB scan is not uniformly printed + 13.** A leaf bearing printed pp. **274–275**
was scanned two leaves early, pushing pp. 260–273 back by two. Established by
reading the folio numbers off PDF 268–301:

```
PDF 268-272 -> printed 255-259     (+13)
PDF 273-274 -> printed 274-275     (out of place)
PDF 275-288 -> printed 260-273     (+15)
PDF 289+    -> printed 276+        (+13)
```

Correct mapping, now implemented in `twoup.sh`:

| printed | KB PDF |
|---|---|
| ≤ 259 | printed + 13 |
| 260–273 | printed + **15** |
| 274–275 | printed − **1** |
| ≥ 276 | printed + 13 |

**The Bodleian copy is correctly ordered** (checked at bodPDF 273/274/275/288/289 →
printed 259/260/261/274/275, a clean +14), so this is a defect of the KB scan
rather than of the edition — no need to reorder anything in the transcription.

**Any check script must stop asserting a flat +13.** Use:

```python
def kb(p):
    if p <= 259: return p + 13
    if p <= 273: return p + 15
    if p <= 275: return p - 1
    return p + 13
```

This was caught only because the facing page of a two-up render showed folio 274
where 260 was expected. Worth spot-checking folio numbers against the expected
offset at the start of each batch rather than trusting the arithmetic.

## A SECOND COPY EXISTS — use it when the KB scan fails

**`~/bibliotek/Nielsen, Rasmus/religion-1869.pdf` is a Google Books scan of the
BODLEIAN copy of the same 1869 edition.** It is an independent witness to the whole
book. Whenever the KB scan (14,-225 8°) is damaged or illegible, collate there
rather than conjecturing.

**Already used once, at printed p.200.** The KB copy has an offset/ink-transfer
defect on that leaf which had lifted the type across ~2 lines. Nothing recovered it
— 900 dpi rendering, `-normalize`, `-sigmoidal-contrast`, `-level`, unsharp
masking, and the PDF's own text layer all failed, because the type had lifted
rather than faded. The Bodleian copy is clean there, and the missing words are:

> Tilstanden paa Jorden, da Mennesket fremkom, **Menneskelivets Begyndelse,**
> Overgangen fra Natur- til Culturtilstand …

**Note the methodological point.** From context I had guessed the gap read something
like *Menneskeslægtens Uddannelse*. It does not — it reads *Menneskelivets
Begyndelse*. Marking the lacuna instead of filling it was what kept a plausible
invention out of the text. Keep doing that: mark, then collate.

(KB also holds five other physical copies — Rel. 84530 8°, UK Nielsen 2,
UnReK A12 rel fil, U 7 Nie, and the digitised 14,-225 8° — if a third witness is
ever needed.)

### Using the second witness

**The scan must sit next to the script as `bodleian.pdf`** (12.6 MB, gitignored),
exactly the way `scan.pdf` does. Refresh or restore it with:

```bash
cp ~/bibliotek/"Nielsen, Rasmus"/religion-1869.pdf \
   texts/nielsen/religionsphilosophie/bodleian.pdf
```

⚠ **Why this matters.** `bodleian.sh` used to read the file straight out of
`~/bibliotek`. The file tools can see that path, but the *render sandbox* — where
`pdftoppm` actually runs — only mounts the repo, so the old path resolved to
nothing and **collation silently stopped being possible**. The script's guard
printed an error, but only if you ran it; the practical effect was that sic
readings accumulated marked-but-unconfirmed. The script now points at the local
copy and its error message gives the `cp` command. If collation ever seems
unavailable again, check for `bodleian.pdf` in the folder before concluding the
second witness is out of reach.

`bodleian.sh` sits next to `twoup.sh` and works the same way:

```bash
./bodleian.sh 200        # one page
./bodleian.sh 200 201    # facing pair
```

**The two scans have DIFFERENT offsets** — this is the easy thing to get wrong:

| witness | file | offset | text layer |
|---|---|---|---|
| KB, shelfmark 14,-225 8° | `scan.pdf` (in this folder) | PDF = printed **+ 13** | usable, poor |
| Bodleian, Google Books | `bodleian.pdf` (in this folder) | PDF = printed **+ 14** | **none** — image only |

Offset verified on Bodleian PDF 206/208/210/212/214 → printed 192/194/196/198/200,
and re-verified at PDF 364 → printed 350 by reading the folio off the page.
Because that copy has no OCR layer, collation against it is necessarily visual.

Beyond repairing damage, the second witness is also the way to settle the more
surprising `% sic:` readings — a genuine compositor's error will appear in *both*
copies; a defect peculiar to the KB copy will not.

### Quote marks

House form is „…“ (U+201E / U+201C), as in the rest of the repo.

**Two quotation defects in the setting are reproduced as printed.** Check the
*running balance*, not the totals — the two cancel, so raw counts look clean:

1. **p.72 (in the p.71 footnote): a dropped opening mark.** The quotation resumed
   at "Naar Skriften betragtes" has no opening „, yet is closed after
   "subjectivt“". Verified at 500 dpi.
2. **p.78: a dropped closing mark.** The quotation opened at „den Hellig-Aand ikke
   blot er noget forskjelligt fra…" is never closed; the single “ after
   "Videnskabens Aander" closes only the *inner* quotation. Verified at 500 dpi.

Expected signature: exactly **one** dropped-open event, and a final balance of
exactly **1**. Anything else is a real error in the transcription —

**except** when a batch stops in the middle of a quotation. The final balance is
then 1 + (number of quotations still open across the cut). At p.102 the Jacob Bøhme
quotation is mid-flight, so the balance reads 2 and is correct; it closes on p.103.
Before treating a high balance as a bug, check whether the last transcribed page
ends inside an open quote.

The same footnote sets „Dette“ and the Grundtvig quotation with the substitute
sorts `,,…‘‘` instead of `„…“`. Normalised to the house form, since it is the same
logical quotation rather than a distinct usage; flagged in a comment at the spot.

### Printer's slips found so far
Reproduced as printed, each with a `% sic:` comment. None is in RETTELSER.
- p.26 "lade Isaak **døer** for at vække ham op igjen" (for *døe*) — 400 dpi.
- p.35 run-head "c) **Aabenbaringen** Tilegnelse i Troen." — missing genitive *-s*;
  the forward reference on p.24 reads "Aabenbaringens". Verified at 420 dpi.
- p.50 "hvormed Aabenbaringen **uldendes**" — the initial *f* of *fuldendes* has
  dropped out of the forme. Verified at 500 dpi: the line begins flush at the left
  margin with no gap, and the line above ends "Aabenbaringen" with no hyphen.
- p.48 footnote: the numerator of the first fraction is a lowercase **o** standing
  for zero (ordinary 19th-c. setting), not a variable. Kept as printed.
- p.52 "virkelig trænger til **at** literærhistorisk Beviis" — *at* for *et*. 500 dpi.
- p.57 "saa er Aabenbaringsordet **blindthen** et Autoritetsord" — set as one word,
  for *blindt hen*. 500 dpi.
- p.62 "Er nu **Sevmodsigelsen**, saaledes forstaaet" — the *l* of *Selvmodsigelsen*
  has dropped out of the forme. 500 dpi. (Second dropped sort, after p.50.)
- p.114 "en **methaphysisk** Mulighed" — intrusive *h*; the book sets *metaphysisk*
  elsewhere (pp.46, 106). 500 dpi.
- p.126 "At det **guddommellge** Selv er Princip" — an *l* standing where the *i*
  belongs. 550 dpi. (Fourth wrong/dropped sort, after pp.50, 62, 114.)
- p.146 the German quotation prints "ein **Nun**"; Angelus Silesius has *ein Nu*
  (an instant). 550 dpi.
- p.160 note: „Philosophisk **Propædentik**“ — an *n* where the *u* belongs, in the
  title of Nielsen's own 1860–61 lecture course. 600 dpi.
- p.288 note: **γενεθαι** for γενέσθαι — the σ has dropped out of the forme, in
  both occurrences of the phrase. 700 dpi. (Fifth dropped sort.)
- p.288 note: **δί** for δι᾽ — an acute set over the iota where the elision
  apostrophe belongs (Rom. 4, 11 δι' ἀκροβυστίας). 700 dpi.
- p.289 note: the letterspacing of "**var i Begyndelsen hos** Gud" stops before
  *Gud*, although "Ordet var **Gud**" three lines below IS spaced throughout.
  Compared at 700 dpi; reproduced as printed.
- p.291 "Speculationen bestemmer **Subjectiviten** negativt" — a dropped syllable;
  the *Efterskrift* reads *Subjektiviteten*. 400 dpi.
- p.299 "to Guds **Sønnner**" — three *n*'s, for *Sønner*. 700 dpi; the same page
  and p.301 set *Sønner* correctly elsewhere.
- p.304 "maa ogsaa Troens **Objectiverering** være" — a doubled *-er-*. 400 dpi.
- p.313 "hvor det ikke behøves (**Mr. 13, 52**)" — Mark 13 has only 37 verses;
  the verse meant is Mr. 13, 32, which Nielsen quotes in full on p.302. 700 dpi,
  and not in RETTELSER.
- p.317 the letterspacing covers "*midlende*" only, not the following "Gud" —
  the same partial-Sperrsatz habit as p.289. 400 dpi.
- p.324 the same again, twice on one page: "*personlig* Gud" and "*treenig* Gud",
  with "Gud" plain both times. 400 dpi. **This is now a settled habit of the
  setting, not an accident — three pages, four instances.**
- p.331 "**Logos selvet** i Gud og **Logosselvet** i Christus" — set as two words
  and then as one, on the same line. 400 dpi.

- p.337 "men ikke som *Alskabningens* Afslutning" — letterspacing again stops
  one word short. 400 dpi.
- p.349 (Hase, in Latin) "additis minis in legis **tansgressores**" — the *r* of
  *transgressores* has dropped out. 700 dpi.
- p.383 "mod en **scholatisk**-objectiv Viden" — the *s* of *scholastisk* has
  dropped out; the book sets it correctly on pp.308 and 379. **Confirmed by
  collation.**
- p.394 "gjennemborer man Næsen **pan** Behemoth" — an *n* where the second *a*
  of *paa* belongs. **Confirmed by collation.**
- **p.403, IN A HEADING**: *α) Frihedens Grundbetingelser: Sædemanden og
  **Jordbnnden***— two *n*'s where *un* belongs. **Confirmed by collation.** The
  word is set correctly on pp.404 and 405. First wrong sort found in a head, so
  don't assume headings were proof-read more carefully than the body.
- p.350 note (Latin) "quovis puncto **mathemathico**" for *mathematico*, and
  "**Hollatius**" for *Hollazius* (David Hollaz). 700 dpi.

**All three of the pp.349–350 readings are CONFIRMED BY COLLATION** — the
Bodleian copy reads *tansgressores*, *mathemathico* and *Hollatius* as well, and
is markedly cleaner than the KB copy on that page (the KB ink blot beside the
*ll* of *Hollatius* raised the question but did not cause the reading). Errors of
the 1869 setting, not scan defects. The missing opening quotation mark at
"Verbum divinum" is likewise absent in the Bodleian, and the closer after
"Evangeliet" is present there too.

### Letterspacing INSIDE italic — an unresolved rendering question

On pp.349–350 the long Latin quotation from Hase is set in italic throughout,
but three phrases inside it are *additionally letterspaced*: the names of the
three uses of the Law — *politicus s. civilis*, *elenchticus s. pædagogicus*,
*didacticus, normativus s. tertius* — as against the plain-italic glosses that
follow each. Verified at 700 dpi.

This has no clean rendering in the current preamble: `\emph{}` inside `\textit{}`
flips to upright, which would misrepresent it as roman, and there is no
letterspacing macro. **The distinction is therefore recorded in a source comment
at the spot but not rendered.** If the author wants it in the PDF, the minimal
change is `\usepackage{letterspace}` plus something like
`\newcommand{\sperr}[1]{\textls[80]{#1}}` — but that diverges from the other ~25
transcriptions, so it is left as a decision rather than made unilaterally.

### One word is set in BOLD in running text

**p.327: "forgude `Absurdum`."** Bold, not letterspaced — verified at 700 dpi
against the neighbouring roman. Bold is otherwise reserved for headings
(`\runhead`, `\greekrun`, `\subhead`) throughout the book, so this is the single
exception so far and is rendered `\textbf{}`. Watch for others; do not silently
convert a bold word to `\emph{}`.

**The contrast is real, not an inking artefact.** p.343 sets *the same word* —
"det *Absurdum*, man ved at lægge Modsigelserne over paa Phænomenet" —
**letterspaced**, and it is rendered `\emph{}` there. Both compared at 700 dpi.
So the book does distinguish bold from Sperrsatz in running text; check the
stroke weight rather than assuming.

### Two names/abbreviations vary between pages — reproduce, don't regularise
- **Anticlimacus** (p.303) vs **Anti-Climacus** (p.342), in the two footnotes
  citing *Indøvelse i Christendom*.
- **Matth.** (pp.293, 306) vs **Mtth.** (pp.345, 346, and the rest of § 23).
- **Jvnfr.** (pp.318, 323, 324, 368) vs **Jvfr.** (pp.334, 342).
- **Gieseler.** and **Giesel.** — in the two footnotes on *the same page* (368),
  citing the same *Kirchengeschichte*.

### A collation that overturned a suspected sic

p.360 „Dette er Guds Gjerning, at I skulle troe …“ looked at 160 dpi — and still
at 700 dpi in the KB copy — as though the compositor had set a **full stop**
after *Gjerning* where a comma belongs. The Bodleian copy shows the comma's tail
plainly. **No sic.** Worth remembering as the counter-example: the second witness
is not only for confirming odd readings but for killing false ones, and the KB
copy's inking is light enough that comma-versus-point is not safely decidable
from it alone.

**It happened again at p.378** — "finder kun Forsoning i den Trøst, at den
fornuftige Gud …", where the KB copy again prints a bare dot and the Bodleian
again shows the tail. This is now a known systematic weakness of the KB scan, not
a one-off. **Treat every KB "full stop mid-sentence" as a comma until collated.**
- p.229 "Han har valgt **vig** Kain til Forbillede" — a *v* where the *s* of *sig*
  belongs. **CONFIRMED BY COLLATION**: the Bodleian copy reads "vig" too, so this
  is an error in the 1869 setting, not a defect in the KB scan. Both at 600 dpi.
  This is the pattern to follow for the remaining sic readings.

Two typographic points established while transcribing pp. 1–18, both of which the
old `indledning/` file got wrong and which recur constantly:
- Third-level run-heads (`a) Religionsphilosophien som speculativ Videnskab.`) are
  **centred bold**, not italic. Use `\runhead{}`.
- Sperrsatz is frequent and load-bearing — e.g. *speculativ Videnskab* /
  *kritisk Videnskab* / *omvendt Videnskab* (p.2), *Grændsevidenskab* (p.9),
  *sig selv i Troeslære ophævende Videnskab* (p.11), the whole Hegel schema on
  p.12, *en Viden af* / *en Viden om* (p.18). None of it survives in the OCR.
Latin phrases are set in antiqua italic (`\textit{ubique et nusquam}`, p.6).
Footnotes begin at p.13 (Hegel, *Religionsphilosophie* II, Berlin 1840).

### The superseded folder

`indledning/` contains `transcription.tex` (624 ll.) and `translation.tex` (642 ll.).

**Two problems with it, both verified against the page images:**

1. **It is truncated.** Its header claims "§§ 1–3, pp. 1–30". In fact it contains
   only § 1 and § 2, and it stops **mid-page 17** — at "…Fordi dens oprindelige
   Forudsætninger ere absolut ueensartede med Videnskab." Printed p.17 continues
   for a further ~15 lines after that point. So the real coverage is **pp. 1–17**,
   and **pp. 18–81 of the Indledning are untranscribed** (rest of § 2, all of
   §§ 3–5).
2. **The last sentence is wrong.** The transcription reads "…absolut ueensartede
   med Videnskab."; the page reads "…absolut **uforenelige med al** Videnskab."
   (p.17, PDF 30, verified at 160 dpi). Since the phrase "absolut ueensartet"
   occurs twice higher on the same page, this looks like a text-layer/model
   conflation rather than a typo — which is a reason to re-verify the whole of
   pp. 1–17 against images rather than trusting it.

A third error surfaced on re-verification: the old file rendered the p.17 clause
"der har **hildet sig i** Modsigelsen" as "der har **bildt sig ind at have løst**
Modsigelsen" — a different claim, not a misreading. Between that and the
"uforenelige med al Videnskab" substitution, nothing in the old file should be
carried over without checking it against the image.

**Next step: `bash batch.sh 443` and transcribe printed pp. 443–454** in
`transcription.tex`. The offset is a plain +13.

**The batch opens with `\parthead{Tro paa Aanden.}` + `\lettersub{A.}{Aandens
Væsen.}` on p.443** — see the verified note above. Expect a `\parmark` for § 30
right after, then the usual lettered/Greek heads; watch for an announcing
sentence naming them. The Indhold's one surviving datum for this division is
*b) Grundbestemmelser i Aandens Selv* = § 32 at p.458, which should fall in the
batch after next.

Only the **p.508 erratum** remains.

**`catalog.yaml` now points only at this file** — one section, "Complete work
(pp. 1–537)", linking `religionsphilosophie/transcription.pdf`. The `indledning/`
links have been removed at the author's request. The `indledning/` folder itself is
still on disk and still committed, so GitHub Pages continues to serve
`indledning/transcription.pdf` and `indledning/translation.pdf` at their old URLs
even though nothing links to them. Both are superseded/flawed (see above) and are
candidates for deletion.

## Division macros

Four levels, all defined in the preamble:

| Macro | Use | Example |
|---|---|---|
| `\parthead{…}` | the three main divisions; each starts a new page | `Tro paa Faderen.` (p.82) |
| `\lettersub{A.}{…}` | lettered sub-division, letter set over title | `A.` / `Faderens Væsen.` (p.82) |
| `\subhead{…}` | centred bold sub-head inside a division | `Religion og Philosophie.` (p.1) |
| `\runhead{…}` | centred bold run-head | `a) Ordets Oprindelighed.` (p.43) |
| `\greekrun{α}{…}` | fourth-level head, italic Greek marker + bold title | `α) Det guddommelige Selv opfattet fra Videns Standpunkt.` (p.84) |
| `\parmark{N}` | centred `§ N.`; deliberately **not** in the ToC | `§ 6.` (p.82) |

**The fourth-level markers are real Greek letters** — α) β) γ), not Latin a) b) c).
Verified at 600 dpi on p.84; the single-storey italic α is unmistakable against the
Latin `a)` of the level above (`a) Selvet i Faderen.`, p.83). The garbled Indhold
OCR ("«) … ß) … Y)") is this same series. `textalpha` is loaded, so they set
directly. Expect γ) as the third member throughout.

## Rendering conventions (inherited from `indledning/`, keep consistent)
- Preamble: `article`, 12pt a4paper, `libertinus` + `libertinust1math`,
  `babel[danish]`, `microtype`, `setstretch{1.3}`, `geometry[margin=1.2in]`,
  `fancyhdr` (rhead = short title, cfoot = page number), `hyperref[hidelinks]`.
- `\section*{INDLEDNING}` / `\subsection*{<sub-head>}` / `\subsubsection*{§ N}`.
- Third-level run-heads → `\medskip` + `\noindent\textit{a) …}` + `\medskip`.
- Sperrsatz → `\emph{}` — **verify each page by zoom render**; the OCR cannot see it.
- Danish quotes „…“ as U+201E / U+201C.
- Footnotes: present from p.41 onward (e.g. the long note on
  *Begrebsmodsigelsens Grundsætning*, p.41). Use `\footnote{}`; the printed marker
  is `*)`.
- Page-break comments `% ---- printed p.N (PDF M) ----` at each boundary.

## Don't compile in the sandbox

The sandbox lacks `libertinus`, `textalpha` and `danish.ldf`, so it cannot build
this file — and it should not try. Running `pdflatex` there writes
`transcription.pdf` and the aux files into the working tree with a timestamp newer
than `transcription.tex`, after which **`make` treats the target as up to date and
silently skips the rebuild**. That already happened once.

Checks that don't require a compile (use these instead):

```bash
python3 - <<'EOF'
import re
raw = open('transcription.tex', encoding='utf-8').read()
# Strip TeX comments first — the header and the "% sic:" notes contain „ and “ as
# prose, which otherwise skews the quote check.
body = '\n'.join(re.sub(r'(?<!\\)%.*$', '', l) for l in raw.split('\n'))
print("braces balanced:", body.count('{') == body.count('}'))
print("$ even:", body.count('$') % 2 == 0)
m = [(int(a), int(b)) for a, b in
     re.findall(r'---- printed p\.(\d+) \(PDF (\d+)\) ----', raw)]
print("range:", m[0], "..", m[-1], "n =", len(m))
print("gaps:", [p for i, (p, _) in enumerate(m) if p != i + 1])
def kb(p):                      # NOT a flat +13 — misbound leaf, see above
    if p <= 259: return p + 13
    if p <= 273: return p + 15
    if p <= 275: return p - 1
    return p + 13
print("offsets correct:", all(b == kb(a) for a, b in m))
# Running balance, not totals: the two known defects cancel in the raw counts.
bal, neg = 0, []
for i, line in enumerate(body.split('\n'), 1):
    for ch in line:
        if ch == '„': bal += 1
        elif ch == '“':
            bal -= 1
            if bal < 0: neg.append(i); bal = 0
print("dropped-open events (expect exactly 1, in the p.71 footnote):", neg)
print("final balance (expect exactly 1 — the unclosed open on p.78):", bal)
EOF
```

Leave the actual compile to `make` on the author's machine.

## Two-up render helper
Everything needed (poppler, ImageMagick, LaTeX) is in the sandbox; the scan must be
at `texts/nielsen/religionsphilosophie/scan.pdf`. Renders go to `.render/`
(gitignored — add `.render/` to `.gitignore` if not already covered).

```bash
#!/bin/bash
# twoup.sh <printed_first> <printed_second>
set -e
D=<repo>/texts/nielsen/religionsphilosophie
OFF=13
A=$(( $1 + OFF )); B=$(( $2 + OFF ))
pdftoppm -f $A -l $A -r 160 -gray -png "$D/scan.pdf" /tmp/pa
pdftoppm -f $B -l $B -r 160 -gray -png "$D/scan.pdf" /tmp/pb
montage /tmp/pa-*.png /tmp/pb-*.png -tile 2x1 -geometry +4+0 -background white \
  "$D/.render/p$1-$2.png"
convert "$D/.render/p$1-$2.png" -resize 2000x2000\> -quality 92 "$D/.render/p$1-$2.png"
rm -f /tmp/pa-*.png /tmp/pb-*.png
```

160 dpi grayscale, montaged two-up and capped at 2000 px, is legible for this
setting (verified on pp. 17/18, 41/42, 55/56) and keeps the image small.

## ERRATA (from RETTELSER, printed p.538 / PDF 551)

**Applied inline** as each page is reached, per the house convention used in
`philosophisk-propaedeutik`. Each application carries an `% ERRATUM APPLIED`
comment at the spot.

**The list is NOT in page order.** On the page it runs
130 · 257 · 257 · 257 · 257 · **400 · 508 · 284 · 392** — the last three are out
of sequence, which is why a quick scan of the top of the page appears to skip
284 and 392 entirely. Read all nine lines before concluding an entry is absent.

**Applied so far (8 of 9):** 130, 257 ×4, 284, 392, 400.
**Only p.508 is outstanding** — *til i sin* → **til sin**, Lin. 11 f.n.

- **p.130** Anm.: *unserer* → **unseres** — APPLIED at p.130. (The Fichte title
  *Ueber den Grund unseres Glaubens an eine göttliche Weltregierung*.)

**⚠ p.257 carries FOUR of the nine errata** — by far the densest page, and the next
one due. Read them off the errata page at ≥700 dpi before transcribing it; they are
long substitutions, not single words. Transcribed at 700 dpi they read:

- p.257 ll.12–13 f.o.: "den Kjendsgjerning, at Chanoch" → **"den Kjendsgjerning,
  at Modsætningen igjen udslettes. Ifølge c. 5 ere alle Adams Efterkommere uden
  Forskjel Sethiter, med mindre man da vil antage, at Chanoch."**
- p.257 l.15 f.o.: "Lamech selv med al" → **"Lamech — hvis c. 5, 25 og c. 4, 18
  ved en Blanding af Genealogierne hentyde paa samme Lamech — Lamech selv."**
- p.257 l.19 f.o.: *er Abraham selv* → **er da Abraham selv**
- p.257 l.20 f.o.: *denne Kjendsgjerning* → **slige Kjendsgjerninger, dersom det
  virkelig ere Kjendsgjerninger**

  n.b. an earlier note here claimed the errata list misprinted this as "S. 150"
  and that the list was wrong. **That was my misreading**, off a 170 dpi render of
  the errata page. At 700 dpi the line plainly reads "S. 130". The RETTELSER page
  numbers should be treated as correct unless verified otherwise at high
  resolution — and verified before any claim that the source is in error.
- p.257 ll.12–13 f.o.: "den Kjendsgjerning, at Chanoch" → "den Kjendsgjerning, at
  Modsætningen igjen udslettes. Ifølge c. 5 ere alle Adams Efterkommere uden
  Forskjel Sethiter, med mindre man da vil antage, at Chanoch."
- p.257 l.15 f.o.: "Lamech selv med al" → "Lamech — hvis c. 5, 25 og c. 4, 18 ved
  en Blanding af Genealogierne hentyde paa samme Lamech — Lamech selv."
- p.257 l.19 f.o.: *er Abraham selv* → **er da Abraham selv**
- p.257 l.20 f.o.: *denne Kjendsgjerning* → **slige Kjendsgjerninger, dersom det
  virkelig ere Kjendsgjerninger**
- p.284 l.6 f.n.: *forklare* → **bortforklare**
- **p.392 l.4 f.o.: *Selvishedeus* → Selvvishedens — APPLIED at p.392.**
  ⚠ **The errata list itself is misprinted here.** It quotes the faulty word as
  *Selvishede**us***, but the page (both copies, 700 dpi) reads
  *Selvishede**ns*** — a dropped second *v*, not an n→u slip. So the lemma you
  would search for does not occur on the page. The correction *Selvvishedens*
  is right; the lemma is not. Trust the correction.
- p.400 l.6 f.o.: *Prophetens* → **Propheternes** — APPLIED at p.400. The plural
  is corroborated by the next sentence, "maatte Propheterne bestandig anlægge
  Lovens … Maalestok".
- **p.508 l.11 f.n.: *til i sin* → til sin — STILL OUTSTANDING, the last one.**

All nine page numbers above were re-read at 700 dpi. **Two were previously recorded
wrong here** — "150" for 130 and "592" for 392 — both misreadings off the original
170 dpi render of the errata page. The second had also prompted a spurious note that
the errata cited a page beyond the 537-page body; it does not. Every RETTELSER page
number falls inside the body.
