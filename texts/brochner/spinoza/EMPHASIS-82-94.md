# Emphasis (Sperrsatz) verification, pp. 82–94

Verification pass over the batch that transcribed pp. 82–94 (end of Fjerde
Capitel, all of the opening of Femte Capitel, "Den menneskelige Aand"), per
the concern that its reported rate — 30 runs, 2.3/page — was well under the
book's floor elsewhere (7.6/page for pp. 1–14, 5.2 for 17–43, 4.6 for 44–64,
4.4 for 65–81). Method: every page was rendered at 600 dpi
(`pdftoppm -r 600`) into a scratch directory outside the repository, cropped
into bands and then into single-line strips wherever a candidate needed
adjudication, and inspected at full resolution. `spacing.py` (with its
`-l dan` fix already applied per RECON.md §3) was run first as a locating
hint only; several of its "single?" flags turned out to be justification
noise and are not carried into the table below unless independently
confirmed on the image.

Legend: **Spaced?** = does the print letterspace this text (Y/N, verified at
600 dpi). **Marked?** = does `transcription.tex` currently wrap it in
`\emph{}`.

## Table: every candidate checked

| p. | Words (as in transcription.tex / as printed) | Spaced in print? | Marked now? |
|---|---|---|---|
| 82 | Tænkningens Attribut | Y | Y |
| 82 | den menneskelige Aand | Y | Y |
| 82 | res cogitans, ens cogitans infinitum | Y | Y |
| 82 | uendelige Modification er intellectus absolute infinitus (spans p.82/83 break) | Y | Y |
| 83 | `Tænkningens endelige modi ere Ideerne: per ideam intelligo` — **endelige** | Y | **N — missing** |
| 83 | same sentence — **Ideerne:** | Y | **N — missing** |
| 83 | same sentence — **ideam** (`per ideam intelligo`) | Y | **N — missing** |
| 83 | `modi ere` / `per` / `intelligo` — the words between the three spaced items above | N | N — correctly unmarked |
| 83 | Sammensætning (`han taler om Sammensætning af Ideer`) — first occurrence | Y | Y |
| 83 | Sammensætning af corpora simplicissima — second occurrence, same sentence | N | N — correctly unmarked |
| 83 | footnote 1: `intellectus actu infinitus` — **actu** | Y | **N — missing** |
| 83 | footnote 4: `mentis conceptus, ikke mentis perceptio` — **conceptus** | Y | **N — missing** |
| 83 | footnote 4, same sentence — **perceptio** | Y | **N — missing** |
| 84 | enkelte (`Forestillede som enkelte staae Ideerne parallele`) — first only | Y | Y |
| 84 | enkelte Legemer — second occurrence, same sentence | N | N — correctly unmarked |
| 84 | Guds uendelige Natur | Y | Y |
| 84 | Guds Idee | Y | Y |
| 84 | idea Dei (all four occurrences on this page) | N | N — correctly unmarked |
| 85 | `illæ tamen infinitæ ideæ, quibus exprimitur,` — up to and incl. **quibus exprimitur,** | N (this part) | N — correctly unmarked |
| 85 | `quibus exprimitur, unam eandemque rei singularis mentem constituere nequeunt, sed infinitas; quandoquidem unaquæque harum infinitarum idearum nullam connexionem cum invicem habeat` | Y (all of it, incl. **quibus exprimitur,**) | **Partial — marked run starts at `unam`, missing `quibus exprimitur,` at its head** |
| 85 | (Ep. 68). after the quote | N | N — correctly unmarked |
| 86 | den menneskelige Aand (`er den menneskelige Aand ikke sat`) | Y | Y |
| 86 | Legemet (`denne Ting er Legemet ɔ:`) | Y | Y |
| 86 | actuelt (`ɔ: en actuelt existerende bestemt Udstrækningsmodus`) | Y | Y |
| 86 | `dens actuelle Væren` / first `actuelt existerende enkelt Ting` | N | N — correctly unmarked |
| 86 | `og idea corporis bliver saaledes til en idea` / `ideæ (idea mentis)` — **idea ideæ**, spans the line break | Y | **N — missing** |
| 86 | `(idea mentis)` immediately after | N | N — correctly unmarked |
| 86 | forma ideæ (`Ideens Idee er Ideens Væsen (forma ideæ)`) | N | N — correctly unmarked |
| 86–87 | footnote: concrete umiddelbare Selvvished / Selvfølelse | Y | Y |
| 87 | adæquate og uadæquate (Idee) | Y | Y |
| 87 | the long »Den menneskelige Aand er en Deel af Guds uendelige intellectus…« quotation (Eth. II, 11 Coroll.) | N | N — correctly unmarked |
| 88 | Erkjendelsens Arter | Y | Y |
| 88 | imaginere | Y | Y |
| 89 | os selv (footnote 2) | Y | Y |
| 90 | ideæ confusæ | Y | Y |
| 90 | `og vi opfatte Tingene som tilfældige og forgængelige,` — **tilfældige og forgængelige** | Y | **N — missing** |
| 90 | `men ved Erindringen om den tilfældige Sammenkjædning` — **Erindringen** | Y | **N — missing** |
| 90 | footnote 2: `Begrebet duratio er,` — **duratio** | Y | **N — missing** |
| 91 | alle (`blive alle Imaginationens Ideer uadæquate`) | Y | Y |
| 91 | `sættes, ɔ: idet Ideen føres tilbage til Gud, er den sand` — **idet Ideen føres tilbage til Gud,** | Y | **N — missing** |
| 91 | `sættes, ɔ:` before it / `er den sand` after it | N | N — correctly unmarked |
| 92 | Forstandens (intellectus) | Y | Y |
| 92 | sand (`ikke blot at være sand, men at have Visheden`) | Y | Y |
| 92 | footnote 2: `Per ideam adæquatam` | Y | Y (but see below) |
| 92 | footnote 2: `intelligo ideam,` (between the two spaced phrases) | **N** | **Y — false positive, currently swept into the same emph** |
| 92 | footnote 2: `quæ quatenus in se, sine relatione ad obiectum consideratur,` | Y | Y (but see below) |
| 92 | footnote 2: `omnes veræ ideæ proprietates sive denominationes intrinsecas habet.` | **N** | **Y — false positive, currently swept into the same emph** |
| 93 | `opfatter den dem under en Evighedens Form (sub quadam` — **Evighedens** (first occurrence) | Y | **N — missing** |
| 93 | `under Evig-hedens Form.` — second occurrence, later same paragraph | N | N — correctly unmarked |
| 93 | `indeslutter nødvendigen Ideen om Guds evige og uendelige Væsen.` — whole clause | Y | **N — missing** |
| 93 | Sandsynligheden | Y | Y |
| 93 | Erfaringen | Y | Y |
| 93 | Existents (`sig til den endelige Existents`) | Y | Y |
| 93 | footnote 2: necessitatis | Y | Y |
| 94 | `men efter sin Natur (»loquor de ipsa natura existentiæ«.` — whole clause up to the close-quote | Y | **N — missing** |
| 94 | `Eth. II, 45. schol.),` immediately after | N | N — correctly unmarked |
| 94 | `den menneskelige Aand har saaledes en adæquat` (as currently marked) | Y | Y |
| 94 | `Erkjendelse af Guds evige og uendelige Væsen` — continuation of the **same** run, up to the footnote mark | Y | **N — marked run stops short; extend it** |
| 94 | Fornufterkjendelsen | Y | Y |
| 94 | footnote 1: ipsa existentia, ipsa natura existentiæ | Y | Y |

## (a) Runs to ADD or EXTEND (confirmed spaced at 600 dpi, not (fully) marked)

1. p.83 — `Tænkningens **endelige** modi ere **Ideerne**: per **ideam** intelligo mentis conceptum` — three separate one-word spaced items in one sentence; `modi ere`, `per`, and `intelligo` between them are plain. Mark each of the three individually, not as one run.
2. p.83, footnote 1 — `Denne betegnes ogsaa som intellectus **actu** infinitus (Eth. I, 30),`
3. p.83, footnote 4 — `Ideen kaldes mentis **conceptus**, ikke mentis **perceptio**, forat betegne,` — two separate spaced words.
4. p.85 — extend the existing `\emph{unam eandemque…}` leftward: the print spaces `**quibus exprimitur,** unam eandemque rei singularis mentem constituere nequeunt, sed infinitas; quandoquidem unaquæque harum infinitarum idearum nullam connexionem cum invicem habeat` as one continuous run; `illæ tamen infinitæ ideæ,` just before it is plain.
5. p.86 — `og idea corporis bliver saaledes til en **idea ideæ** (idea mentis), der paa samme Maade` — spans the `idea / ideæ` line break; `(idea mentis)` itself is plain.
6. p.90 — `og vi opfatte Tingene som **tilfældige og forgængelige**, hvilke Bestemmelser`
7. p.90 — `men ved **Erindringen** om den tilfældige Sammenkjædning af Legemets Affectioner.`
8. p.90, footnote 2 — `Begrebet **duratio** er, i sin Forskjel fra Evigheden,`
9. p.91 — `Begrændsningen hæves og Helheden sættes, ɔ: **idet Ideen føres tilbage til Gud,** er den sand` — the `ɔ:` before and `er den sand` after are plain.
10. p.93 — `opfatter den dem under en **Evighedens** Form (sub quadam æternitatis specie.` — only this first occurrence; the second, `under Evighedens Form.` two sentences later, is plain.
11. p.93 — `eksisterende Ting indeslutter nødvendigen **Ideen om Guds evige og uendelige Væsen**.` — whole four-word clause, one continuous run; `Tingenes Existents er` right after is plain.
12. p.94 — `men **efter sin Natur (»loquor de ipsa natura existentiæ«.**` — the clause plus the embedded Latin quotation, stopping before `Eth. II, 45. schol.),`.
13. p.94 — extend the existing run: currently `\emph{den menneskelige Aand har saaledes en adæquat}` stops before `Erkjendelse`, but the print letterspaces the whole clause through to the footnote mark: `\emph{den menneskelige Aand har saaledes en adæquat Erkjendelse af Guds evige og uendelige Væsen}` (Eth. II, 46 f.).

## (b) Existing `\emph{}` judged NOT (fully) letterspaced in print

1. p.92, footnote 2 — the current markup wraps the entire sentence `Per ideam adæquatam intelligo ideam, quæ quatenus in se, sine relatione ad obiectum consideratur, omnes veræ ideæ proprietates sive denominationes intrinsecas habet.` in one `\emph{}`. At 600 dpi this is **two** separate spaced phrases with plain text between and after them:
   - spaced: `Per ideam adæquatam`
   - plain: `intelligo ideam,`
   - spaced: `quæ quatenus in se, sine relatione ad obiectum consideratur,`
   - plain: `omnes veræ ideæ proprietates sive denominationes intrinsecas habet.`
   Should become `\emph{Per ideam adæquatam} intelligo ideam, \emph{quæ quatenus in se, sine relatione ad obiectum consideratur,} omnes veræ ideæ proprietates sive denominationes intrinsecas habet.`

No other existing `\emph{}` in pp. 82–94 was found to be a false positive — every other current marking was confirmed spaced at 600 dpi, with boundaries matching the print exactly.

## Not chased (out of scope)

The long Eth. II, 11 Coroll. quotation on p.87 (»Den menneskelige Aand er en
Deel af Guds uendelige intellectus…«) and the Eth. II, 17. schol. quotation
on p.88 (»De Affectioner af det menneskelige Legeme…«) were both checked in
full at 600 dpi and confirmed plain roman throughout — long block quotations
in this stretch are evidently not spaced as a matter of course, unlike the
shorter embedded citation-clauses that are (cf. items 4, 9, 11, 12 above).
This is a reading finding, not an emphasis question, and is noted here only
so the next pass does not re-check the same ground.
