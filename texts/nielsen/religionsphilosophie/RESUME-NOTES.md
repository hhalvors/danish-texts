# Rasmus Nielsen — *Religionsphilosophie* (1869): transcription

# ✅ PHASE 1 (TRANSCRIPTION) IS COMPLETE — pp. 1–537, finished 2026-08-05

The whole body is transcribed and image-verified page by page against the KB
scan, with every doubtful reading collated against the Bodleian copy. All nine
RETTELSER errata are applied inline. `transcription.tex` is the single live file.

**Final state of the checks** (`python3 check.py transcription.tex`):

```
pages: 1..537  n=537  gaps=none      offsets correct: True
braces balanced: True                $ even: True
footnotes: 94 | sic: 48 | errata applied: 10 (= 9 applications + header prose)
partheads: 3 | lettersubs: 9 | greekruns: 78 | parmarks: 41
quote balance: 7 (standing expectation 7)
dropped openers at lines: [2696] (expect exactly one)
progress: 537/537 = 100.0%
```

**The quote balance of 7 is now a FIXED figure, not a running one.** It is
9 never-closed openers minus 2 never-opened closers, all nine defects of the
1869 setting and all confirmed by collation. Any deviation from 7 from here on
means the file has been edited by mistake.

## Structure as transcribed

| division | pages | §§ | lettered heads |
|---|---|---|---|
| Indledning | 1–81 | 1–5 | — (five `\subhead`s) |
| Tro paa Faderen | 82–271 | 6–17 | A 82, B 149, C 200 |
| Tro paa Sønnen | 272–442 | 18–29 | A 272, B 340, C 399 |
| Tro paa Aanden | 443–537 | 30–41 | A 443, B 500, C 519 |

p.538 carries only the RETTELSER; it is not set as body text.

## ✅ BUILD VERIFIED — 2026-08-05

`make` run on the author's machine. The build is clean and was checked, not just
assumed:

- **383 pages**, letter, no errors, no undefined references, `transcription.out`
  checksum unchanged (so no rerun pending).
- **ToC correct**: 4 section entries (Indledning + the three `\parthead`s) and
  14 subsections (5 Indledning sub-heads + A/B/C × 3). The stray „C.“ is gone
  and *C. Faderens Rige.* now carries its full stop like A. and B.
- **The spurious page break is gone**: *C. Faderens Rige* now sits mid-page on
  printed p.140 of the build, directly under the preceding paragraph, at
  `\large` like its siblings, with `§ 14` following. It had previously been
  forced to the top of a fresh page by the `\parthead` `\clearpage`.

## What is left to do

1. **`catalog.yaml` still says `status: in-progress`** for this text (line
   ~1830). Now that the PDF is rebuilt and correct, that can be flipped to
   `complete` — it was deliberately left alone until the build existed, so the
   site would not advertise a finished transcription while serving a stale PDF.
2. **Phase 2: translation**, via `../../../TRANSLATION-PLAYBOOK.md`.

### The ToC bug that was fixed (2026-08-05)

`C. Faderens Rige` (p.200) had been hand-expanded instead of using the macro:
`\parthead{C.}` + a centred title + a manual `\addcontentsline`. That was wrong
three ways — `\parthead` files a **section**-level ToC entry containing just
„C.“ (the stray entry in the Indhold), it issues `\clearpage` and so forced a
spurious page break mid-chapter, and it set the letter `\LARGE` instead of
`\large`. Replaced with `\lettersub{C.}{Faderens Rige.}`, which is what A. and
B. use. **Moral: use the macros; a hand-rolled head will not show up in any of
the structural counts** — `check.py` counted it as a `\parthead`, which is
exactly why the count read 4 when only 3 main divisions exist.

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

## TRO PAA AANDEN — the third and last main division, opens p.443

`\parthead{Tro paa Aanden.}` then `\lettersub{A.}{Aandens Væsen.}` and `§ 30`,
all on **p.443**. § 30's announcing sentence (p.446) names three lettered heads,
letterspaced throughout including the *og*: *Selvet i Aanden, Grundbestemmelser
i Aandens Selv og Aandens Personlighed*.

- ***a) Selvet i Aanden* (§ 31, p.446)**, with *α) Aanden paa Grundlag af det
  Almene* (p.446), *β) Aanden paa Grundlag af det Individuelle* (p.449),
  *γ) Aandens Selv: Mysteriet* (p.452).
- ***b) Grundbestemmelser i Aandens Selv* (§ 32, p.458)** — ✅ **the Indhold's
  last surviving number, and it is EXACT.** Every one of its numbers held, from
  the first (§ 9 at 129) to the last. With it the Indhold is now spent; the rest
  of the book is navigated by announcing sentences alone.
  Its heads: *α) Gudverdslige Grundbestemmelser* (p.459),
  *β) Gudmenneskelige Grndbestemmelser* (p.467 — `sic`, see below),
  *γ) Trinitariske **Form**bestemmelser* (p.480 — see the note below; not a
  misprint).
- ***c) Aandens Personlighed* (§ 33, p.487)**, with *α) Faderens Aand* (p.488),
  *β) Sønnens Aand* (p.491), *γ) Den Helligaand* (p.496).

### ✅ A. AANDENS VÆSEN IS COMPLETE — pp. 443–500, §§ 30–33

**B. Aandens Gjerninger** (§ 34) opens **p.500**. Its announcing sentence
(pp.500–501) names three lettered heads: *Opvækkelsen, Gjenfødelsen,
Helliggjørelsen*; ***a) Opvækkelsen: det levende Ord* (§ 35) opens p.501**.
Transcribed to p.502.

**⚠ A head can differ from its announcement in wording, not just in fullness.**
§ 32's announcing sentence (p.459) promised *trinitariske **Grund**bestemmelser*;
the head at p.480 reads *Trinitariske **Form**bestemmelser*. **Confirmed by
collation** — both copies, 700 dpi — so it is Nielsen's variation, not a wrong
sort, even though *Grund-/Form-* is exactly the kind of swap the late-book
compositor might have made. α and β matched their announcement word for word.
This is the second such case after p.438 (*Dommen* → *Dommedag: Salighed og
Fordømmelse*). **Collate any head that departs from its announcement** rather
than assuming either a misreading or a misprint.

§ 32's announcing sentence is **spread over three consecutive sentences** rather
than packed into one, each closing on a letterspaced title: *gudverdslige* /
*gudmenneskelige* / *trinitariske Grundbestemmelser* (pp.458–459). A new shape
for the same device — don't expect the whole list in a single sentence.

Transcribed to p.466.

Still to come: the close of § 25, then a *C.* division to finish *Tro paa
Sønnen* before *Tro paa Aanden* around p.458.

**The misbound range is now behind us** — from p.276 the offset is a plain +13
again for the rest of the book. (The `kb()` function still needs to stay in any
check script, since it covers pp.260–275 which are already transcribed.)

**Resume at printed p.503 (PDF 516).** p.502 ends mid-word ("Væk-"), outside any
quotation, so the check script should read exactly the standing balance — now
**4**, see the quote note below.

n.b. an earlier note here estimated *Tro paa Aanden* at "around p.458". That was
wrong — 458 is § 32's page from the Indhold leaf, not the division's opening.
The division in fact opened on **p.443** and is now transcribed.

**The Indhold has run out.** Its surviving leaves covered through § 21's second
head (324); *Tro paa Aanden* and § 32 (458) are on PDF 13 but with no
intermediate detail. From p.325 onward the structure is read off the running
text, as it was for the Indledning. Spot-check every run-head against the page.

**Quote balance is 4 — and the arithmetic is no longer naive.** Six openers are
never closed by the printer, and two closers are never opened:

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
8. **p.500, the Grundtvig quotation** — the reverse again: closed at
   "…uvedkommende“", then **resumed after the ellipsis with no opener** at "Det
   Samme gjælder om Konst-Ordet…", and closed once more at "…lader sig døbe
   paa“". 700 dpi. Only the second such event in the book, after the p.71
   footnote / p.72.

All eight are reproduced as printed, and #5–#8 are **CONFIRMED BY COLLATION**
against the Bodleian copy.

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
| the p.500 never-opened closer | −1 |
| **standing total from p.500** | **4** |
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

Checks that pass on the current file: 502 page-break comments, contiguous pp.1–502,
every offset correct against `kb()` above; braces balanced; `$` count even; 84
footnotes; 41 `% sic:` notes; 4 `\parthead` and 7 `\lettersub`; **8 of the 9
errata applied** (130, 257 ×4, 284, 392, 400); no lacunae outstanding; exactly
one entry in the dropped-open list and a balance of exactly 4 — the new standing
figure. The dittography sweep is clean.

**Progress: 502 of 537 body pages = 93.5% — 35 pages left, three batches.**

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
| 452 | δυναμις ἐξ ὑψους | δύναμις ἐξ ὕψους — ἐξ right, the other two carry breathings but no accents |
| 501 | ἀνθρωπος ψυχικος / ἀνθρωπος πνευματικος | breathings only, no acutes — **and note p.59 sets the same phrase ἄνθρωπος ψυχικος WITH the acute.** The two occurrences differ; both as printed |
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
| Nielsen, *Om Hindringer og Betingelser* | p.475 → p.476 | **eight lines** on p.476 |

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
- p.465 "Almagtsbegrebet altsaa **dobbelsidig** bestemt" — the *t* of
  *dobbeltsidig* has dropped out; the book sets it correctly on p.463, two pages
  earlier. **Confirmed by collation.**
- p.461 note: "K. Schwarz. **Anfr** Skr. S. 354" — no period after *Anfr*, where
  the note on the facing page (462) has "Anfr. Skr." 700 dpi; reproduced as
  printed.
- **p.403, IN A HEADING**: *α) Frihedens Grundbetingelser: Sædemanden og
  **Jordbnnden***— two *n*'s where *un* belongs. **Confirmed by collation.** The
  word is set correctly on pp.404 and 405. First wrong sort found in a head, so
  don't assume headings were proof-read more carefully than the body.
- **p.467, IN A HEADING**: *β) Gudmenneskelige **Grndbestemmelser*** — the *u*
  has dropped out. **Confirmed by collation.** Second head-error, and **the same
  kind as p.403's**: both are u/n confusions in the bold heading fount. Two in
  ~65 pages, against none in the first 400 — worth reading every remaining head
  letter by letter rather than at a glance.
- p.467 "hvis andet **Leder** en aandløs Aand" — *Led er* set without the space;
  the parallel clause four words earlier reads "hvis ene Led er en Aand". 700 dpi.
- p.469 "ikke ved nogen Samvirken med Naaden **kunne gjør** det muligt" — the
  final *e* of *gjøre* has dropped out. 700 dpi.
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

**Next step: `bash batch.sh 503` and transcribe printed pp. 503–514** in
`transcription.tex`. The offset is a plain +13. Inside *a) Opvækkelsen: det
levende Ord* (§ 35); expect its Greek heads, then *b) Gjenfødelsen*.

**⚠ THE p.508 ERRATUM — THE LAST ONE — FALLS IN THIS BATCH.** RETTELSER,
Lin. 11 **f.n.** (from the *bottom*, unlike most of the others): *til i sin* →
**til sin**. Apply inline with an `% ERRATUM APPLIED` comment recording the
printed reading; that completes all nine.

Body ends at p.537, so two batches remain after the next: 515–526, 527–537.

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
- Preamble (**corrected 2026-08-05 against the actual file** — this entry used to
  say `article`, a4paper, `setstretch{1.3}`, `margin=1.2in`, none of which is
  what the file has): `book`, 12pt, **default letter paper** (no paper option is
  given), `libertinus` + `libertinust1math`,
  `babel[danish]`, `microtype[protrusion,expansion]`, `onehalfspacing`,
  `geometry[margin=1.4in]`,
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

---

# Repair programme — full collation (REPAIR-PLAYBOOK.md §5C), started 2026-09-21

**Ground truth, established 2026-09-21 before any dispatch.** Scan
`~/bibliotek/Nielsen, Rasmus/1869-religionsphilosophie.pdf` (the notes above call it
`religionsphilosophie.pdf`; same file, renamed), sha256
`6de1f8224b838e3811a34eb5b71dfb0621e0227c7db0116002b63a12deb03be7` — confirmed by hand on
the device and on the staged copy; 557 pp. **Map = kb() above, not flat**: folio read from
the text layer on 522 of 537 body pages agrees with it, 0 disagree (PDF 339's folio OCRs as
"32"), which covers the misbound run pp.260–273 (+15) and 274–275 (−1). All 537 `printed p.N
(PDF M)` comments agree with kb(). Bodleian second witness `bodleian.pdf` sha256 88af4021…
(= bibliotek `religion-1869.pdf`), PDF = printed + 14.

**Method: full collation** — the 12-page sample found 0.17/pg and ocrdiff 0/15 rules out
§5B. 10 printed pages per agent, 54 agents, waves of 6 (wave k = pp. 60k−59 … 60k; wave 9 =
pp.481–537). Brief = `pgtools/COLLATE-BRIEF.md` + `BATCH-AGENT.md` (new, 2026-09-21).
**Hint sheets are built with the embedded layer REMAPPED through kb()** — the stock
`ocrdiff.py --frag --offset 13` compares pp.260–273 with the wrong PDF pages (validated:
two planted dropped „ikke“ on pp.265/268 caught by the remapped run, 0 by the stock run).
One `OCRDIFF:` line per wave below. `.bak` per wave: `transcription.tex.bak.collate-waveN`.
Blind second reader per wave on every PRN/UNSURE/non-emphasis FIX before applying.

## Waves

### Wave 1 — pp. 1–60, 2026-09-21. 6 agents × 10 pp. SPLICED + VERIFIED.
OCRDIFF: embedded ABBYY (kb-remapped) | pp.1-60 | 191 candidates | 0 real | 191 witness's fault | 0 unresolved
  (per agent: 1-10 25/0/25/0 · 11-20 30/0/30/0 · 21-30 37/0/37/0 · 31-40 35/0/35/0 · 41-50 38/0/38/0 · 51-60 26/0/26/0)
Found by reading: 2 FIX (p.26 „løb“→„lød“; p.39-note title „Der christliche Glaube“ is roman, not
\textit), 3 printer's errors the file had silently corrected, restored as printed with comments (p.13
„Umiddelharhed“, p.58 „omkrives“, p.60 „I Kraft of“), 2 already-as-printed misprints given comments
(p.11 „Adpredelsen“, p.41 „Aandvilliens“), 10 emphasis corrections (pp.6, 12 ×2, 13, 19, 39-note, 57 ×2),
2 lost paragraph breaks restored (at the p.38/39 and p.58/59 turns). All 537 markers OK in range.
Blind second reader on 17 items: all agree with the collators; p.40-note „Absolute,“ settled as comma
(file already right). Verify: braces 0, markers 537 contiguous/kb-correct, quote balance 7 (unchanged),
head/tail and all pages outside 1–60 byte-identical, no new doubled 4-grams; sandbox compile
(mathptmx, Greek mapped) 403 pp., 0 errors, 0 missing = the untouched original built the same way.
Results + blind Q/A in `.parts/collation/`. .bak = transcription.tex.bak.collate-wave1.

### Wave 2 — pp. 61–120, 2026-09-21. 6 agents × 10 pp. SPLICED + VERIFIED.
OCRDIFF: embedded ABBYY (kb-remapped) | pp.61-120 | 189 candidates | 0 real | 189 witness's fault | 0 unresolved
  (per agent: 61-70 30/0/30/0 · 71-80 30/0/30/0 · 81-90 27/0/27/0 · 91-100 38/0/38/0 · 101-110 30/0/30/0 · 111-120 34/0/34/0)
Found by reading: 1 FIX (p.78 „forskjelligt“→„forskjellig fra“, modernised); 7 printer's readings the file
had silently corrected, restored with comments (p.73 „Bevidtshed“, p.92 „immancnte“, p.92 „Beviis, Den“,
p.93 „Tilværelse, Hvad“, p.97 „Bevidthed“, p.99 μυστὴριον with GRAVE — the old note calling p.99 „✓ correct“
was wrong —, p.101 „o. s. v, Paa“); p.106 note ellipsis is four points, set `.\ .\ .\ .`; emphasis: p.63
\emph{Troen} removed (one loose gap, not Sperrsatz), p.81 ×3 extents; 3 lost paragraph breaks restored
(turns 64/65, 72/73, 93/94). Blind second reader on 15 items: all 15 agree with the collators.
Verify: braces 0, 537 markers contiguous/kb-correct, quote balance 7, head/tail and all pages outside
61–120 identical, no new doubled 4-grams, compile 403 pp. 0 errors 0 missing (= original).
Fixed in the applier this wave: `% sic` comments now quote only the changed words and never carry an
\opage (one draft comment did, which would have looked like a 538th marker to a naive regex).
.bak = transcription.tex.bak.collate-wave2.

### Wave 3 — pp. 121–180, 2026-09-21. 6 agents × 10 pp. SPLICED + VERIFIED.
OCRDIFF: embedded ABBYY (kb-remapped) | pp.121-180 | 202 candidates | 1 real | 201 witness's fault | 0 unresolved
  (per agent: 121-130 34/0/34/0 · 131-140 40/1/39/0 · 141-150 42/0/42/0 · 151-160 33/0/33/0 · 161-170 25/0/25/0 · 171-180 28/0/28/0)
Found by reading: 2 FIX (p.137 „Tavshed“→„Taushed“, modernised — the one real hint so far; p.143
„Villiesenhed“→„Villieseenhed“); printer's readings restored with comments: p.147 „Saligbedshaab“, p.158
two-point ellipsis „maa .\ .\ med“, p.159 „Modsætnig“, p.162 „systême“ (CIRCUMFLEX — the old sic comment
said acute, and the file had é; both corrected); comments added to already-as-printed p.155 „(rød Jord,)“
and p.170 „den uendelig Enemagt“. Emphasis: p.158 ×4 and p.166 extents (connectives „og“/„samt“ solid).
3 lost paragraph breaks restored (turns 134/135, 167/168, 174/175). Blind second reader on 13 items:
all 13 agree. Verify: braces 0, 537 markers ok, quote balance 7, pages outside 121–180 identical,
no new doubled 4-grams, compile 403 pp. 0 errors 0 missing. .bak = transcription.tex.bak.collate-wave3.

### Wave 4 — pp. 181–240, 2026-09-21. 6 agents × 10 pp. SPLICED + VERIFIED.
OCRDIFF: embedded ABBYY (kb-remapped) | pp.181-240 | 161 candidates | 0 real | 161 witness's fault | 0 unresolved
  (per agent: 181-190 21/0/21/0 · 191-200 26/0/26/0 · 201-210 36/0/36/0 · 211-220 35/0/35/0 · 221-230 18/0/18/0 · 231-240 25/0/25/0)
Found by reading: 0 FIX. Printer's readings restored with comments: p.195 „i Styrelsen; synes“ (stray
semicolon) and „Villieseenhed den“ (no comma) — both silently regularised before; p.209 „Gudsforhøldet“
(wrong ø sort; clear in the Bodleian, both readers). Comments added to already-as-printed citation slips
p.187 „(Ps. 139, 33)“ and p.188 „(Ps. 41)“ (= Ps. 51) — possibly authorial. Emphasis: pp.192–193 spurious
\emph over a whole sentence removed. 2 lost paragraph breaks restored (turns 221/222, 225/226). p.200 (the
KB ink-transfer page) collated against the Bodleian: agrees. Blind second reader on 8 items: all agree.
Verify: as before, all clean; compile 403 pp. 0/0. .bak = transcription.tex.bak.collate-wave4.

### Wave 5 — pp. 241–300 (includes the misbound run 260–275), 2026-09-21. 6 agents × 10 pp. SPLICED + VERIFIED.
OCRDIFF: embedded ABBYY (kb-remapped) | pp.241-300 | 182 candidates | 1 real | 181 witness's fault | 0 unresolved
  (per agent: 241-250 30/0/30/0 · 251-260 32/0/32/0 · 261-270 27/0/27/0 · 271-280 33/1/32/0 · 281-290 32/0/32/0 · 291-300 28/0/28/0)
Folios on all pages matched the kb() map, incl. p.260=PDF 275, 274–275=PDF 273–274, 276=PDF 289.
Found by reading: 3 FIX (p.276 dropped „det“ in „geraader det det dog“ — the one real hint; p.287 note
„S. 580“→„S. 380“, citation; p.294 „alene“→„aleneste“). Printer's readings restored with comments: p.259
„Sandsynlighed, Og“, p.277 „blevetfuld stændig“, p.281 άμαρτια (acute printed for the rough breathing),
p.289-note „blaudt“; comment added to already-as-printed p.252 „Luk, 4, 6“. Emphasis: p.247 spurious
removed, p.256, p.275 ×5 („Menneske“ solid), p.289-note ×2 (the old n.b. comment there was wrong and is
rewritten). 5 lost paragraph breaks restored (turns 243/244, 248/249, 262/263, 282/283, 297/298). The
p.299 „Sønnner“ sic comment's wording corrected. p.106 ellipsis reverted to `\dots` (house convention:
point-count is not recorded except the anomalous two-point one at p.158).
Blind second reader on 21 items: 17 agree; HELD OPEN, not applied: p.289-note „V 4.“ (KB shows no
point, the Bodleian shows one), p.282 „Idèal“ (KB shows the grave, the Bodleian none — file keeps KB),
p.262 „Linned“ (odd glyph in both copies; collator: not ø, blind reader: reads as ø — file unchanged).
Verify: all clean; compile 403 pp. 0/0. .bak = transcription.tex.bak.collate-wave5.

### Wave 6 — pp. 301–360, 2026-09-21. 6 agents × 10 pp. SPLICED + VERIFIED.
OCRDIFF: embedded ABBYY (kb-remapped) | pp.301-360 | 194 candidates | 2 real | 192 witness's fault | 0 unresolved
  (per agent: 301-310 34/1/33/0 · 311-320 32/1/31/0 · 321-330 29/0/29/0 · 331-340 29/0/29/0 · 341-350 34/0/34/0 · 351-360 36/0/36/0)
Found by reading: 10 FIX — p.303 „Magt“;“→„Magt“,“; p.309 Greek ἀρρήτως … ἀνεκδιηγήτως → ἀῤῥητως …
ἀνεκδιηγητως (NO accents printed; the old "verified" comment was wrong and is rewritten); p.316
„Dybder“→„Dybheder“ and „mig“*)?“→„mig“?*)“; p.319 „Forløsnings-“ ADDED (eye-skip from the line below);
p.341 „afhandlet:“→„;“; p.348 „tøisløs“→„tøilesløs“; p.349 full stop after the Hase note call restored;
p.353 „Frihed.“→„Frihed,“; p.355 „forsvundet“→„forsvunden“. Printer's readings restored with comments:
p.302 „Dagen eg Timen“, p.344 „jnst“, p.355-note „S, 314“, p.358 „Svovlpølen, I“; comments added to
already-as-printed p.330 „Ortodoxiens“, p.334-note „Proprædeut.“. Emphasis: p.303, p.322, p.328 „Gud og
Verden“, p.343, p.357 ×2. Blind second reader on 22 items: 20 agree. HELD, not applied: p.321 „…
Aabenbarelse og Personlighedens …“ and p.328 „Skaber og Skabning“ — blind reader sees „og“ SPACED there,
collator solid; file keeps \emph over „og“. Verify: all clean; compile 403 pp. 0/0.
.bak = transcription.tex.bak.collate-wave6.

### Wave 7 — pp. 361–420, 2026-09-21. 6 agents × 10 pp. SPLICED + VERIFIED.
OCRDIFF: embedded ABBYY (kb-remapped) | pp.361-420 | 174 candidates | 0 real | 174 witness's fault | 0 unresolved
  (per agent: 361-370 24/0/24/0 · 371-380 26/0/26/0 · 381-390 33/0/33/0 · 391-400 34/0/34/0 · 401-410 30/0/30/0 · 411-420 27/0/27/0)
Found by reading: 7 FIX — p.366 „skaansellos“→„skaanselløs“; p.373 „ved“→„veed“ (modernised) and
„Enkelthed“→„Enkeltheds“; p.381 καταλλαγή→καταλλαγὴ (GRAVE; the Greek table in these notes calling it
„✓ correct“ was wrong, and the p.381 sic comment is amended); p.389 „Grund-“ ADDED before „Uklarheden“
(eye-skip); p.413 a PARAPHRASED clause restored („Evigheden er det i Øieblikket absolut Nærværende. Den,
der er fordybet …“ — the file had fused two sentences); p.415 „er Glæden“ ADDED (eye-skip). Printer's
readings restored with comments: p.372 HEAD „dobbeltsidigc“, p.381 „Distinctioner;“, p.385 „Liv eg Død“,
p.414 ellipsis „Maalet. ,\,.\,.“. Emphasis: p.373-note „Grund“ removed, p.392, p.406, p.416. 2 lost
paragraph breaks restored (turns 398/399, 399/400). Blind second reader on 19 items: all agree; p.362
„bliver“ (c-like e, no positive signal) left as is. Verify: all clean; compile 403 pp. 0/0.
.bak = transcription.tex.bak.collate-wave7.

### Wave 8 — pp. 421–480, 2026-09-21. 6 agents × 10 pp. SPLICED + VERIFIED.
OCRDIFF: embedded ABBYY (kb-remapped) | pp.421-480 | 182 candidates | 1 real | 180 witness's fault | 1 unresolved
  (per agent: 421-430 31/0/31/0 · 431-440 21/1/19/1 · 441-450 23/0/23/0 · 451-460 35/0/35/0 · 461-470 31/0/31/0 · 471-480 41/0/41/0;
   the 1 unresolved = p.435 „ai“/„af“, settled by the blind reader as a broken f — file keeps „af“)
Found by reading: 5 FIX — p.428 „Propheter“→„Profeter“; p.438-note dropped „det“ („og det Gode“);
p.458 colon restored („altsaa:“); p.472 „;“→„,“; p.475/476-note „bevæge“→„bestemme“ (eye-skip). Printer's
readings restored with comments: p.428 „I see, Thi“, p.451 „Ordet. lever“, p.463 „Attributcr“, p.466
„guddommeligo“, p.476-note „Virkuing“. Emphasis: p.430, p.446 (old comment claiming the „og“ spaced was
wrong — rewritten), p.462, p.463. Paragraphing: one SPURIOUS break removed at the 439/440 turn (p.440 is
flush left). The p.476 „eight lines“ comments corrected to 15. Blind second reader on 16 items: all agree.
Verify: all clean; compile 403 pp. 0/0. .bak = transcription.tex.bak.collate-wave8.

### Wave 9 — pp. 481–537, 2026-09-21. 6 agents (the last 7 pp.). SPLICED + VERIFIED.
OCRDIFF: embedded ABBYY (kb-remapped) | pp.481-537 | 158 candidates | 3 real | 155 witness's fault | 0 unresolved
  (per agent: 481-490 24/0/24/0 · 491-500 31/2/29/0 · 501-510 33/1/32/0 · 511-520 30/0/30/0 · 521-530 27/0/27/0 · 531-537 13/0/13/0)
Found by reading: 6 FIX — p.496 „vilde“→„ville“; p.498 dropped „de“; p.502 „Skulde“→„Skulle“; p.509
dropped „for“ („blot for forsvarlig“); note-call after the full stop at pp.500, 536. Printer's readings
restored with comments: p.492 „Eenbed“, p.502 „Brng“, p.524-note „sigc“, p.526 HEAD „Vcxelvirkningen“,
p.527 „lovgivendo“, p.530 „Apostelmenighcdens“, and **p.522: the print TRANSPOSES the two footnotes** (the
*) call after „Tider.“ carries the Martensen note, the **) call after „Ord“.“ carries „Anfr. Skr. S. 424.“);
the file had silently reassigned them by sense — now as printed, with comments. Comment added: p.481
turned e in „Bestemmǝlser“. ~16 emphasis extents (pp.482, 485, 497, 517, 519, 522–524, 532, 536). Blind
second reader on 19 items: all agree; p.527 Greek (Ἔδοξε / ἡμῖν) left OPEN, comment added (two readers
now see no breathing on the E; the 2026-08 note saw one at 700 dpi). .bak = transcription.tex.bak.collate-wave9.

## COLLATION COMPLETE — 9 waves, 9 OCRDIFF lines, all 537 pages. Ledger: repaired (2026-09-21).
Totals: 36 transcriber's errors corrected (24 word-level), 41 silently corrected misprints restored as
printed + 10 comments added, 58 emphasis, 17 lost paragraph breaks + 1 spurious. ~77 transcriber faults
over 537 pp. ≈ 0.14/pg — consistent with the 12-page sample's 0.17. ocrdiff: 1,633 candidates, 8 real.
Post-repair re-sample (seed |post: pp.54, 131, 164, 187, 235, 471): 0 confirmed errors; one flagged mark
(p.131 „Modsigelsen;“ read as a colon) was overturned 2–1 by the collator and a third reader at
1000–1200 dpi (worn semicolon). STILL OPEN items are listed in the transcription.tex header.
translation.tex: made by Hans from the collated transcription, 2026-09-21/22 (not part of this repair).
Structural parity checked 2026-09-22: 537 \opage (contiguous), 94 footnotes, heads/§ marks, \textbf
all match the Danish 1:1; \emph 352 vs 353 is the p.197/198 hyphenated „vi-|l“ (two \emph in the
Danish, one „will“ in the English) — not a discrepancy; 0 errors in translation.log.
NOT DONE: old indledning/ folder untouched; note.md not updated.

---

# PHASE 2 (TRANSLATION): FULL DRAFT DONE, 2026-09-21/22, awaiting Hans's review

`translation.tex` (book level) is the whole book in English, pp. 1–537, with front
matter. It supersedes `indledning/translation.tex`: that pp. 1–30 draft was used
as the base for chunks 01–02 and corrected against the collated Danish.
- Method: 45 subagent chunks of about 12 pp. each, all working to one brief and
  glossary (`.parts/translation/BRIEF.md` plus two addenda), then a
  harmonization pass. Source fragments are in `.parts/translation/NN.texfrag`
  (00-head = preamble and front matter). Rebuild by concatenating 00..45 plus
  `\end{document}`. 99.texfrag is an empty stray file; ignore it.
- Checks against the Danish body: opage 537/537 (same sequence), footnotes
  94/94, and parmark/runhead/greekrun/lettersub/parthead/subhead all equal.
  \emph is 351 against 352: on p.197/198 "vil" is split across the page as two
  emphasized pieces, and it is one word in English. Quotes balance at 0 and
  braces at 0. There are 102 `% print:` notes.
- Test compile (lmodern substituted, Greek stripped): 438 pp., 0 errors, 0
  character warnings. Not yet built with libertinus on the Mac.
- A spot-check of 10 pages by an independent agent found about 0.2 errors per
  page; the one error that changed meaning (i og for sig / an sich, p.372) has
  been fixed across the book.
- Open items for Hans: `.parts/translation/FLAGS.md`. These are the Socinus
  footnote on pp.288–90, the footnotes on p.522 that may be transposed, the
  Bible references kept as printed where they look like Nielsen's own slips,
  "Mosebrand" on p.43x, and "Object/Gjenstand" on p.416.
- catalog.yaml: translation flipped to `status: complete` with a Translation link
  to translation.pdf, at Hans's request, 2026-09-22 (validate-catalog.py: 0 problems).
