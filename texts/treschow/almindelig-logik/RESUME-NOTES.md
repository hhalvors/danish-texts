# Niels Treschow — *Almindelig Logik* (1813), §§ 26–35: resume notes

Selective transcription. **Not** the whole book (330 printed pp.) — only
printed **pp. 91–108**, which carry the machinery the 1810 essay presupposes but
never supplies. Companion: `../enslige-ting/` (the 1810 essay, complete,
transcribed + translated).

## Scan, offset, type
- Scan: `~/bibliotek/Treschow, Niels/almindelig-logik-1813.pdf` (345 scan pp.),
  built from nb.no IIIF, `URN:NBN:no-nb_digibok_2008040210002`, public domain.
- **Offset in this region: scan = printed + 8.** §26 opens printed 91 = scan 99;
  §35 ends printed 108 = scan 116, closing the First Main Part. p. 109 (scan
  117) begins *Andet Hovedstykke. Om Sandhed og Vished*, § 36 *Hvad er Sandhed?*
- ⚠ **The offset drifts elsewhere in the volume** (+10 near the end: scan 340 =
  printed 330). Re-verify before working outside pp. 91–108.
- **FRAKTUR**, emphasis = letterspacing (Sperrsatz) → `\emph{}`.
- Orthography uses **ø**, not the **ö** of the 1810 antiqua essay.
- No *Indhold* in this book; the body begins at scan 11 after a roman-numeral
  *Fortale*. The section map below was established by inspection.

## Section map (printed pages)

| § | Heading | p. |
|---|---|---|
| 26 | Ordforklaringer | 91 |
| 27 | Hvilke Ord man bør forklare | 93 |
| 28 | Beskrivelser | 94 |
| — | **4de Afdeling. Om Delinger** | 95 |
| 29 | Høiere og lavere Begreber | 95 |
| 30 | Egentlige og uegentlige Slægter eller Arter | 97 |
| 31 | Et Heelt og dets Dele | 98 |
| 32 | Logiske og andre Delinger | 100 |
| 33 | Nytten af Delinger | 102 |
| 34 | Overalt nødvendige Regler | 104 |
| 35 | Andre Regler | 105 |
| — | *(end of Første Hovedstykke, p. 108)* | |
| (36 | Hvad er Sandhed? — NOT included | 109) |

## Working method (fast path — use this)
Rendering from the 177 MB local PDF is slow (~7 s/page). **Fetch page images
straight from nb.no instead** — 38 pages took 6 seconds:

```bash
URN=URN:NBN:no-nb_digibok_2008040210002
for P in $(seq 99 113); do n=$(printf "%04d" $P)
  echo "url = \"https://www.nb.no/services/image/resolver/${URN}_${n}/full/1500,/0/native.jpg\""
  echo "output = \"/tmp/sec/s${n}.jpg\""
done > cfg
curl -s --parallel --parallel-max 12 -K cfg
```

Then **read the pages as 2-up montages** (975 px per page is fully legible for
Fraktur) rather than OCR-ing:

```bash
montage h0099.jpg h0100.jpg -tile 2x1 -geometry 975x1690+3+3 -background gray out.png
```

⚠ Do **not** try to parallelise tesseract — it already multithreads, and running
several at once thrashes and gets killed by the 45 s call limit. Single-page
Fraktur OCR is ~7 s. Contact sheets (6-up at 640 px) are excellent for *finding*
section headings; 2-up at 975 px for *transcribing*. Note nb.no caps the IIIF
width at the native 1440 px, so asking for 2400 returns 1440.

## Notable readings so far
- p. 91 `Hensigten deraf er deels at bevise...` — only **one** "deels", though
  the following "Det Sidste" presupposes a second limb. Kept as printed with a
  `% sic` note.
- p. 94 §28 *Beskrivelser*: "Intet uorganisk Legeme synes at have sand
  Individualitet... f. Ex. Noahs Ark eller Theseus's Skib" — the same Theseus
  example as the 1810 essay (printed p. 233), here in a doctrine of description.

## Substantive findings

**§ 30 is the payoff.** "Slægter saavelsom Arter ere deels egentlige, deels
uegentlige eller analogiske. Hines Kiendemærker ere væsentlige og bestandige,
disses blot tilfældige og ubestandige." — a criterion of *naturalness* for
classifications, which the 1810 essay asserts the need for but never supplies.
Note the twist: Treschow does **not** discard improper kinds. They are
"nødvendige" where no proper kind is available or where general theories must be
applied — and the improper divisions of human beings by temperament, sex, age
and descent are defended precisely because singular characters cannot be studied
out one by one. So general concepts remain *aids to survey* (1810, p. 240), now
with a two-tier structure: proper kinds track essential and abiding criteria,
improper kinds are admittedly accidental but indispensable. Cf. the "kunstige
Systemer" at the end of § 30.

**§ 31 complicates the monistic reading.** Treschow distinguishes *real* from
*ideal* parts and then writes: "Pantheismen og Emanations Systemet beroe
fornemmelig paa denne Misforstaaelse. Det høieste Væsen er hverken et
almindeligt Begreb, hvorunder Aand og Legeme, som Arter, indbefattes, ei heller
noget Heelt, som Verden, hvoraf alle Individuer ere Dele." He explicitly denies
that the highest being is a whole of which individuals are parts. This cuts
against a straightforward mereological monism and should be weighed against the
1810 essay p. 251 ("each is this whole itself under his own peculiar form")
before the Horgan–Potrč comparison is settled.

**§§ 32–34 are a theory of division**, more directly useful for the
coarse-graining project than the kinds material: *partitio* (real parts) vs
*divisio* (logical, genus into species); division always relative to a chosen
*Inddelingens Grund*; and § 34's three rules — the parts must **exhaust** the
whole, must be **mutually exclusive**, and there must be **no leap** from higher
to lower species. § 29 adds the extension/comprehension inverse and the point
that "highest genus" is indexed to a science (body is highest in natural
science, much lower in metaphysics).

**§ 35 sharpens § 30 into a rule of method.** Rule (a): "Inddelingens Grund bør
tages af Tingenes væsentlige og bestandige Kiendemærker. Findes ingen saadanne,
maa man blandt flere andre vælge dem, der mest nærme sig hine." — where no
natural joint is available, choose the criteria that come *nearest* to essential
and abiding ones. That is a graded, comparative naturalness, not a binary
elite/non-elite split, and it is the clearest statement of the position. Among
inward criteria form outranks matter; among outward, cause and origin outrank
effect and object. § 35 also concedes that usage often fixes a classification we
cannot change "uden at indføre en gandske ny Nomenclatur", and closes with a
frank admission of how much arbitrariness trichotomy and every other mode of
classification has introduced into the history of philosophy — "naar man ingen
vis Regel har at følge... bliver kun vildsomme Stier... tilbage."

**§ 28** carries the Theseus's ship example (with Noah's Ark and Tyre) inside a
doctrine of *description*, and states that no inorganic body has true
individuality — the same claim as 1810 p. 233, but here doing methodological work.

## STATE — TRANSCRIPTION AND TRANSLATION COMPLETE (§§ 26–35)
- **transcription.tex**: printed pp. 91–108, all 18 pages image-verified, 10
  section headings, 0 stray `ö`. Compiles 0 errors / 0 char-warnings (10 pp.).
- **translation.tex**: mirrors it 1:1 — same 18 page markers in the same order,
  same 10 headings, same 49 `\emph{}` spans. Compiles 0/0 (10 pp.).
- Emphasis is carried strictly: no emphasis added where the print sets plain
  (e.g. "Philosophiens, Ontologiens" in § 26, and "reale/ideale" in § 32, are
  roman in the print and roman in the translation — unlike § 31, where they are
  letterspaced and so italic).
- `catalog.yaml`: entry added under Treschow, `almindelig-logik`.
- **Possible next steps:** the second "enslige" cluster at printed pp. ~66–82 has
  not been examined; and *Andet Hovedstykke, Om Sandhed og Vished* opens at
  p. 109 with § 36 *Hvad er Sandhed?*, which may bear on the truth/aptness side.
