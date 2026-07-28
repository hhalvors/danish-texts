# Niels Treschow — *Om den menneskelige Natur i Almindelighed, især dens aandelige Side* (1812): resume notes

**This is a COMPLETE-WORK job**, not a selection: printed pp. 1–486 plus front
matter. The first psychology written in Danish. Expect many sessions. Work in
~10-printed-page batches; after each, compile, report briefly, hand back.
**Hans commits and pushes — the assistant never does.**

Companions in this collection: `../enslige-ting/` (1810 essay, complete),
`../almindelig-logik/` (§§ 26–35), `../om-gud/` (1831, two spans).

## Scan, offset, type
- Scan: `~/bibliotek/Treschow, Niels/om-den-menneskelige-natur-1812.pdf`
  (511 scan pp.), from nb.no IIIF `URN:NBN:no-nb_digibok_2008040712004`,
  public domain, "Tilgang for alle".
- **Offset: scan = printed + 18**, and it holds across the volume — verified at
  p. 1 = scan 19, p. 16 = scan 34, p. 27 = scan 45, p. 486 = scan 504.
  Spot-check on entering each new Hovedstykke.
- Scan 505–506 are tail matter; **507–511 return a 1150-byte blank** from the
  IIIF endpoint (not an error on our side — those leaves are empty).
- **FRAKTUR.** Emphasis = letterspacing (Sperrsatz) → `\emph{}`. Treschow
  letterspaces **whole thesis-sentences** in this book, not just names — often
  the opening proposition of a §. Carry every one.
- Orthography uses **ø**. Note `Siel`/`Sielen` beside `Siæl` (both occur —
  transcribe as printed), `Gienstand`, `Bevidsthed`, `Noümen` (with diaeresis),
  `Sands` = sense, `indvortes`/`udvortes` = inner/outer.
- §§ are numbered **continuously through the whole book** (1., 2., 3., …), set
  inline at the head of a paragraph, not as display headings. Transcribe them as
  `8.~\emph{...}` etc., matching the existing text.

## Structure (from the Indhold, printed pp. XV–XVI = scan 17–18)

| Part | pp. | scan |
|---|---|---|
| Fortale | I–VI+ | ~5–10 |
| Indhold | XV–XVI | 17–18 |
| **Indledning** | 1–10 | 19–28 |
| **Første Hovedstykke.** Almindeligt Begreb om Mennesket, især fra dets aandelige Side | 11–34 | 29–52 |
| **Andet Hovedstykke.** Om Forestillingsevnen — 1ste Afd., denne Evne i Almindelighed | 34–60 | 52–78 |
| — 2den Afd., Sandseligheden og umiddelbare Fornemmelser | 60–90 | 78–108 |
| — 3die Afd., Evnen til at kalde Forestillingerne tilbage, og middelbare Fornemmelser | 90–146 | 108–164 |
| — 4de Afd., Tænkekraften eller den høiere Forestillingsevne | 146–188 | 164–206 |
| **Tredie Hovedstykke.** Om Følеevnen — 1ste Afd., Følelser i Almindelighed | 188–227 | 206–245 |
| — 2den Afd., de forskiellige Slags behagelige og ubehagelige Følelser | 227–269 | 245–287 |
| **Fierde Hovedstykke.** Om den menneskelige Villie — 1ste Afd., Villien i Almindelighed | 270–293 | 288–311 |
| — 2den Afd., Drifter og Tilbøieligheder | 293–363 | 311–381 |
| — 3die Afd., Vaner og Færdigheder | 363–383 | 381–401 |
| — 4de Afd., Lidenskaber og Affecter | 384–486 | 402–504 |

## Working method (fast path — use this)
Rendering from the local PDF is slow. **Fetch page images from nb.no instead**
(~40 pages in 6 s), then read them as 2-up montages; do **not** OCR:

```bash
URN=URN:NBN:no-nb_digibok_2008040712004
for P in $(seq 19 33); do n=$(printf "%04d" $P)
  echo "url = \"https://www.nb.no/services/image/resolver/${URN}_${n}/full/1500,/0/native.jpg\""
  echo "output = \"/tmp/mn/m${n}.jpg\""
done > cfg
curl -s --parallel --parallel-max 12 -K cfg
montage m0019.jpg m0020.jpg -tile 2x1 -geometry 975x1690+3+3 -background gray out.png
```

6-up contact sheets at 640 px are right for *finding* headings; 2-up at 975 px
for *transcribing*. nb.no caps the IIIF width at native 1440 px. Do **not**
parallelise tesseract — it already multithreads and gets killed by the call
timeout; reading images directly is both faster and more accurate here.

**Page-boundary convention** (as in the other Treschow files): no blank line
before a `% printed p. NN` marker when the page turns mid-paragraph; end the
previous line with `%` on a broken word-stem (dropping the print's hyphen);
keep a blank line only at genuine paragraph breaks.

## Verification compile (sandbox lacks libertinus — substitute; NOT in the file)
```bash
cd /tmp && D=verMN && mkdir -p $D && cd $D
SRC=".../texts/treschow/menneskelige-natur/transcription.tex"
sed -e 's/\\usepackage{libertinus}/\\usepackage{lmodern}/' -e '/libertinust1math/d' \
    -e 's/\\usepackage\[danish\]{babel}/\\usepackage{babel}/' "$SRC" > t.tex
pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1
grep -o 'Output written.*' l.txt; grep -ic 'not set up\|missing character' l.txt
```
Expect 0 char-warnings, 0 errors.

## STATE
- **DONE (image-verified, compiles 0/0):**
  - **Indledning COMPLETE, printed pp. 1–10** (§§ 1–6, ending with the closing
    ornament on p. 10)
  - Første Hovedstykke, **printed pp. 16–21** (end of § 7 through § 11 opening)
- **NEXT — printed pp. 11–15** (scan 29–33), the opening of the Første
  Hovedstykke. §§ 7 and 8 are already in hand from p. 16, so this batch supplies
  the missing § 7 opening and whatever §§ fall on 11–15 — note the numbering
  jumps from § 6 (p. 5) to § 8 (p. 16), so § 7 spans pp. 11–15. Closing this
  gap makes pp. 1–27 continuous.
- **THEN — printed pp. 22–27**, finishing §§ 11–14 and the Første Hovedstykke's
  argument, ending "Mennesket er altsaa i sin individuelle Grundform og som Idee
  eller Noümen uforgængeligt."
- **THEN** the Fortale (roman I–VI+), then onward through the Hovedstykker.
- **Translation:** hold until the Danish of a whole Hovedstykke is complete, then
  translate it as a unit (mirroring 1:1), rather than interleaving page by page.
  Terminology per `../enslige-ting/RESUME-NOTES.md`, plus for this book:
  Sands = sense; indvortes/udvortes = inner/outer; Aand = spirit; Legeme = body;
  Forestillingsevne = the faculty of representation; Følеevne = the faculty of
  feeling; Villie = will; Drift = drive; Færdighed = acquired skill;
  Lidenskab/Affect = passion/affect; Noümen = noumenon.
- **catalog.yaml:** DONE — entry set to `in-progress` under Treschow,
  `menneskelige-natur`, with the § 2 / § 11 / p. 27 material recorded.

## Notable so far
- **§ 2 (p. 2)** already sets up the two-sidedness: the human being "kan
  betragtes fra en dobbelt Side, nemlig en legemlig og aandelig," and taking
  either exclusively makes knowledge one-sided. He asks whether there is a
  "fælles Sands, i Midten af den indvortes og udvortes" from which both could be
  seen united, and answers that no *anskuelig* knowledge is to be had that way —
  hence anthropology must be *divided* into the physiological and the
  psychological, each keeping the other in view. That is the programmatic
  statement the §§ 8–14 argument later cashes out.
- **§ 4 (p. 4)** names the discipline: since the soul is no more wholly
  self-active than the body, natural laws hold of it too, though only so far as
  it is *passive* — "I denne Henseende er denne Videnskab en aandelig
  Naturlære" (in this respect this science is a spiritual natural philosophy).
- **§ 5 (p. 4)** ties psychology to philosophy through the *inner* experience
  from which philosophy borrows the matter of its concepts, and sets four
  demands on the discipline — Fuldstændighed, Nøiagtighed, Orden, Grundighed —
  with a warning against the "Overfladig" anthropology that generalises from
  few, often misunderstood, experiences.
- **§ 6 (pp. 5–10)** is the long apologia for the usefulness of knowledge of
  man: for attaining our destiny, and then in religion, pedagogy, aesthetics,
  medicine, the rest of natural science, jurisprudence, and statecraft. The
  medical section (p. 8) is striking — the causes of many illnesses "ligger mere
  i visse herskende Forestillinger og deres Forbindelse end i nogen Legemets,
  d.e. den grovere Organismes, Uorden," and glad news or fear has overcome
  diseases "der have trodset de kraftigste Lægemidler." The statecraft section
  (pp. 9–10) closes the Indledning by rejecting the doctrine that only
  self-interested drives exist: acting on it "fornedret dem, saaret deres
  moralske Følelse."
