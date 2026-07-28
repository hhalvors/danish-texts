# Høffding (ed.), *Udvalgte Stykker af dansk filosofisk Litteratur* (1910) — resume notes

= *Mindesmærker af Danmarks Nationallitteratur* III, ed. Vilhelm Andersen.
Kjøbenhavn: Gyldendal 1910, 306 pp. Høffding supplied the introductions.

**Why this file exists.** Not to re-transcribe the anthology's excerpts — the
1810 Treschow essay is already transcribed and translated *complete, from the
original printing*, at `../../treschow/enslige-ting/`. What matters here is the
**transmission document**: Høffding's own framing of Treschow, and the shape of
the selection he passed on to his readers (Bohr's milieu among them).

## Scan & offset
- `~/bibliotek/Høffding, Harald/mindesmaerkerafd03ande.pdf` — Internet Archive,
  320 PDF pp., **clean OCR — use this**.
- `~/bibliotek/Høffding, Harald/udvalgte-stykker.pdf` — HathiTrust (Wisconsin,
  Google-digitized), 321 pp., **badly jumbled OCR** (column order scrambled);
  useful only as a second set of page images.
- **Offset: renderer page = printed + 8.** Section IV opens printed p. 99
  (unnumbered section opener, signature "7*" at foot) = render p. 107.
- ⚠ `pdftotext`'s form-feed indexing differs from `pdftoppm`'s by ~3 on this
  file. Trust the renderer offset when pulling images; recalibrate if in doubt.
- Type is **antiqua**; proper names in small caps; Danish low–high quotes „…".

## Structure of section IV, "Den psykologiske Skole (Treschow, Sibbern, Howitz)"

| Anthology pp. | Content |
|---|---|
| 99 | Section heading + Høffding's § 1 (introduction to Treschow) |
| 99–108 | **A. Det Individuelles Uudtømmelighed** — from the 1810 essay |
| 108–113 | **B. Udviklingslære** — from another work (see below) |
| 114 | § 2 introduces F. C. Sibbern (then § 3, presumably Howitz) |

Høffding's editorial notes are **distributed**, one before each author, not
gathered at the head of the section.

## What Høffding kept from the 1810 essay (excerpt A)

Collated mechanically against the complete transcription (12 evenly spaced
30-character probes per printed page):

| Original printed pp. | In excerpt A |
|---|---|
| 225–229 | kept (full) |
| 230 | partial |
| **231–234** | **cut** |
| 235–240 | kept (full) |
| 241 | first line only (completes the sentence begun on 240) |
| **242–254** | **cut** |

The excerpt therefore **ends on the "Hielpemidler til Oversyn" passage**, with
its closing words "...rigtigen er det alligevel at giøre Forskiel paa denne
abstrakte Forestilling om det Enslige og den concrete." **The omissions are
silent** — no ellipses, no rules, no editorial note marks the cuts.

What this means: Høffding transmitted the *epistemological* Treschow (the limits
of general concepts, dissolving species boundaries, individuality as nature's
aim) and dropped the metaphysics — the rights-and-personality argument, the
circle/sphere and Godhead-as-perfect-individuality, and the whole second half:
the identity-system, Plotinus/Spinoza/Fichte/Schelling, the thesis restatement at
p. 247 that the concept of singular things has objective validity and reality,
Democritus, germs and preformation, and the closing. See
`../../treschow/enslige-ting/RESUME-NOTES.md` for the full discussion.

## Three points worth exploiting

1. **Høffding's own title.** The excerpt is headed *Det Individuelles
   Uudtømmelighed* — "The Inexhaustibility of the Individual." That is
   Høffding's phrase, not Treschow's, and it names an epistemic thesis (the
   individual outruns any concept) rather than the metaphysical one Treschow
   actually argues for.
2. **A shifted framing.** In *Danske Filosofer* (1909) Høffding calls the essay
   "directed against Schelling"; here in § 1 the opposition is broadened to
   "den tyske Filosofis Opgaaen i almene og abstrakte Begreber" — German
   philosophy's absorption into general and abstract concepts. Note that the
   anthology cuts *both* Schelling passages (original pp. 231 and 246).
3. **Høffding's dating.** § 1 cites the essay as *Videnskabernes Selskabs
   Skrifter* **1807** — the signed date carried in the volume's footline —
   though the volume was published 1810. Cite with care.

## Excerpt B, *Udviklingslære* — source VERIFIED

Høffding prints no source at the excerpt. His § 1 points to *Elementer til
Historiens Filosofi* (1811), and that attribution is **confirmed**:

- Searching nb.no's full-text index across Treschow's works, the distinctive
  tokens **"Thibetanerne"** and **"Evolutions"** occur **only** in *Elementer til
  Historiens Philosophie* (1811) — zero hits in *Om Gud* I, *Philosophiske
  Forsøg* (1805), *Om Philosophiens Natur og Dele* (1811), *Om den menneskelige
  Natur* (1812).
- Anthology pp. 111–112 are word-for-word identical with *Elementer*, **printed
  p. 80 = scan p. 92** (image-verified against
  `~/bibliotek/Treschow, Niels/elementer-til-historiens-philosophie-1811.pdf`).
  The relevant region of *Elementer* is roughly scan pp. 87–95.
- ⚠ **Orthography differs.** The 1811 original is Fraktur and uses **ø**;
  Høffding's anthology normalizes (and drifts — e.g. "Øjet" beside "Øiekast").
  The anthology is Høffding's redaction. **Cite the 1811 original**, and
  transcribe from it if the passage is quoted at length.
- Extent within *Elementer* has **not** been collated end-to-end; only the
  identity of the source and the p. 80 anchor are established. Whether Høffding
  cut silently here too, as he did in excerpt A, is still open.

## STATE
- **DONE:** Høffding's editorial matter for Treschow — section heading, § 1, and
  both excerpt headings — plus **excerpt B in full** (anthology pp. 108–113),
  transcribed, **every page image-verified**, and translated. Both files compile
  0 errors / 0 char-warnings, 5 pp. each, with structural parity (8 page markers,
  5 `\emph{}` spans, 1 footnote on each side).
- Excerpt A is deliberately **not** re-transcribed here: the 1810 essay exists
  complete and from the original printing at `../../treschow/enslige-ting/`.
- **TODO (optional, in rough value order):**
  1. § 2 on Sibbern (p. 114) and § 3 on Howitz — relevant to the
     Treschow→Sibbern→Kierkegaard question.
  2. Collate excerpt B against *Elementer* end-to-end, to see whether Høffding
     cut silently here as well.
  3. Høffding's general *Indledning* (pp. 1 ff.) mentions Treschow in passing
     when tracing the Holberg/Sneedorff line forward to Høffding and Kroman.
