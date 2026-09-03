# Emphasis (Sperrsatz) verification, pp. 65–81

Verification pass over Batch 6's emphasis calls for Tredie/Fjerde Capitel
(pp. 65–81), per the concern that Batch 6 read spacing off downscaled
`Read`-tool images rather than 600 dpi crops. Method: every page in the
range was rendered at 600 dpi (`pdftoppm -r 600`) into a scratch directory
outside the repository, cropped into line-height bands with
`convert -crop`, and inspected band by band. `spacing.py` was run first as a
locating hint only, per BATCH-AGENT.md.

Legend: **Spaced?** = does the print letterspace this text (Y/N, verified at
600 dpi). **Marked?** = does `transcription.tex` currently wrap it in
`\emph{}`.

## Table: every candidate checked

| p. | Words (as in transcription.tex) | Spaced in print? | Marked now? |
|---|---|---|---|
| 65 | Uendeligheden og Causaliteten | Y | Y |
| 65 | Forstand, Villie, Attraa, Kjærlighed | Y | Y |
| 65 | Substantsbegrebet (`Vi saae, at Substantsbegrebet i sin Fuldstændighed`) | Y | **N — missing** |
| 65 | Gudsbegrebet (`faldt sammen med Gudsbegrebet, og at`) | Y | **N — missing** |
| 65 | Gud (`og at Gud bestemtes som det absolut`) | Y | **N — missing** |
| 66 | Øiemedsbegrebet (`bestemt saaledes, at Øiemedsbegrebet udelukkes`) — spacing survives the line break `Øiemedsbe-grebet` | Y | **N — missing** |
| 67 | Frihed (`Indbildningen om den menneskelige Frihed, og gjennem`) | Y | **N — missing** |
| 67 | personlig (`Anskuelsen af en personlig Gud`) — `Gud` itself NOT spaced | Y (personlig only) | **N — missing** |
| 67 | Naturmagtens Nødvendighed (`I dennes Sted træder Naturmagtens Nød-vendighed`) — whole phrase spaced across the line break | Y | **N — missing** |
| 68 | Uendelighed (`Naar Substantsens Uendelighed medførte`) | Y | **N — missing** |
| 68 | samme Betydning (`Aarsag i samme Betyd-ning som han kaldtes`) — across line break | Y | **N — missing** |
| 68 | Frihed (`blive Tale om en individuel Frihed,`) — `individuel` NOT spaced | Y (Frihed only) | **N — missing** |
| 68 | Nødvendighed og Umulighed (`Begreberne Nødven-dighed og Umulighed (skjøndt`) — across line break | Y | **N — missing** |
| 69 | nødvendig (`nemlig nødvendig,¹) enten med Hensyn`) — opening word of the page | Y | **N — missing** |
| 69 | Umulige (`Modsætningen til det Nødvendige bliver det Umulige, hvilken`) | Y | **N — missing** |
| 69 | det Tilfældige / det Mulige | Y | Y |
| 69 | tilfældig; mulig | Y | Y |
| 69 | **natura naturata** (`finde Anvendelse paa natura naturata, der ikke`) | **N — plain roman** | **Y — false positive, unspace** |
| 69 | footnote 2: contingentem (`illam contingentem dicemus — — quia`) | Y | **N — missing** |
| 70 | (nothing letterspaced found on this page) | — | — |
| 71 | ydre (`Nødvendigheden som ydre Tvang hænger`) | Y | **N — missing** |
| 71 | indre (`bliver den ydre Nødvendighed til en indre, til`) | Y | **N — missing** |
| 71 | natura naturans / natura naturata (calibration case, first word of each pair only) | Y (first word only) | Y — correct as printed |
| 72 | Naturen (`Naturen bliver det fælles Navn, Gud og Naturen`) — only the first occurrence | Y | **N — missing** |
| 72 | Deum seu naturam (`quod Deum seu naturam appellamus, eadem`) | Y (all three words) | Y |
| 72 | Dei sive naturæ (`»Ipsa Dei sive naturæ potentia«`) | Y | Y |
| 72 | cum tota natura (`quam mens cum tota natura habet«`) | **N — `cum` NOT spaced, only `tota natura`** | **Y — false positive on `cum`; should read `\emph{tota natura}`** |
| 72 | Ex natura (`— »Ex natura, sub quovis`) | **N — `Ex` NOT spaced, only `natura,`** | **Y — false positive on `Ex`; should read `\emph{natura}`** |
| 72 | Udstrækning og Tænkning | Y | Y |
| 72 | Ideen (`Tanke: Ideen, og den bestemte begrændsede`) | Y | **N — missing** |
| 72 | Legemet (`Udstrækning: Lege-met²), have deres`) — across line break | Y | **N — missing** |
| 72 | footnote 1: naturæ divinæ (`omnia ex naturæ di-vinæ necessitate sequi`) — across line break | Y | **N — missing** |
| 73 | parallele (`sideordnede og parallele Rækker¹)`) — `Rækker` NOT spaced | Y (parallele only) | **N — missing** |
| 73 | Ordenen og Sammenhængen i Ideerne | Y | Y |
| 73 | den samme som Ordenen og Sammenhængen i Tingene | Y | Y |
| 74 | Natur : Udstrækningens (`kalde Natur: Udstrækningens²) Attribut`) | Y (both) | **N — missing** |
| 74 | Attribut (`Udstrækningen opfattet som Attribut³), altsaa`) | Y | **N — missing** |
| 74 | udelelig (`som uendelig og udelelig; men ogsaa som`) | Y | **N — missing** |
| 74 | activ (`men ogsaa som activ. Den`) | Y | **N — missing** |
| 74 | actuosa (`Hvert Attribut udtrykker en actuosa essentia`) | Y | **N — missing** |
| 74 | agendi eller operandi potentia | Y | Y |
| 74 | footnote 2: corporea (`Udtrykket: substantia corporea.`) | Y | **N — missing** |
| 75 | Uendelighed og Udelelighed (`dens Uendelighed og Udelelighed (jfr. Eth.`) — both words | Y | **N — missing** |
| 75 | hvilket er meget vanskeligt (`begribe den som Substants, hvilket er meget vanskeligt, saa`) — 3-word run | Y | **N — missing** |
| 75 | Materien (`Hensyn til, at Materien overalt er den samme`) | Y | **N — missing** |
| 76 | den udstrakte Substantses (`I Opfattelsen af den udstrakte Substantses Væsen`) | Y (all three) | Y |
| 76 | udenfra (`Udstrækningsmodus som fremkaldt udenfra, om end`) — first occurrence only; the later `de udenfra fremkaldte` is NOT spaced | Y (1st only) | **N — missing** |
| 76 | Udstrækning, udstrakt Substants (legemlig Substants), Quantitet, Materie (the "Udtrykkene:" list) | Y | Y |
| 76 | Materie (`synes Bestemmelsen Materie at være en`) — second, later occurrence | Y | **N — missing** |
| 77 | moles quiescens | Y | Y |
| 77 | rerum varietas (footnote) | Y | Y |
| 77 | Udstrækningens ɔ: Materiens Enhed med **Gud**, og de endelige Tings **Ikke-Realitet** — the whole clause is one continuous spaced run | Y (entire clause, incl. Gud and Ikke-Realitet) | **Partially — current `\emph` stops short of `Gud` and of `Ikke-Realitet`; extend** |
| 77 | "kan ikke Tale" (spacing.py false lead) | N | N — correctly unmarked |
| 78 | uendelige modi (`Som Udstrækningens uendelige modi¹) bestemmes`) — `Udstrækningens` NOT spaced | Y | **N — missing** |
| 78 | Bevægelse og Hvile (`nu Bevægelse og Hvile²) (Ep. 66`) | Y | **N — missing** |
| 78 | facies totius universi | Y | Y |
| 78 | endelige (`— De endelige Modi ere Legemerne.`) — `Modi ere` NOT spaced | Y | **N — missing** |
| 78 | Legemerne (`Modi ere Legemerne. De`) | Y | Y (already marked) |
| 78 | deduceres (`De deduceres ikke af hine`) — `De`/`ikke` NOT spaced | Y | **N — missing** |
| 78 | hine (`af hine; thi en saadan`) | Y | **N — missing** |
| 78 | Begrebet variatio | Y | Y |
| 78 | Legemer forudsættes hypothetisk (across line break `for-udsættes`) | Y | Y |
| 78 | footnote 1: secundum leges naturæ extensæ per motum et quietem (across line break) | Y | **N — missing** |
| 79 | tilbage (`saa tilbage til de uendelige Modificationer`) — `føres` and `uendelige` here NOT spaced (checked closely; ambiguous justification stretch, not real spacing) | Y (tilbage only) | **N — missing** |
| 79 | Physikens almindelige Sætninger an- (`Grundbegreber, Physikens almindelige Sætninger an-givne.`) — spacing stops mid-word at the line break, `givne` not spaced | Y (partial) | **N — missing** |
| 79 | corpora simplicissima (`Legemer (corpora simplicissima)²)`) | N — plain roman | N — correctly unmarked |
| 79 | sammensatte (`for de sammensatte Legemer`) — `Legemer` NOT spaced | Y | **N — missing** |
| 79 | indbyrdes forenede (`kaldes indbyrdes forenede, og siges`) | Y | **N — missing** |
| 79 | eet Legeme eller Individuum | Y | Y |
| 80 | hele Naturen er eet Individuum | Y | Y |
| 80 | (nothing else letterspaced found on this page) | — | — |
| 81 | enkelte (`Forestilling om enkelte Legemer, gives der`) — `Legemer` NOT spaced | Y | **N — missing** |
| 81 | (nothing else letterspaced found on this page) | — | — |

## (a) Runs to ADD (currently unmarked, confirmed spaced at 600 dpi)

Quoting enough context to locate each site unambiguously in
`transcription.tex`:

1. p.65 — `Vi saae, at **Substantsbegrebet** i sin Fuldstændighed faldt sammen med **Gudsbegrebet**, og at **Gud** bestemtes som det absolut uendelige Væsen.` — three separate words, all spaced.
2. p.66 — `og derfor bliver den nødvendige Causalitet bestemt saaledes, at **Øiemedsbegrebet** udelukkes.` (spacing survives the `Øiemedsbe-grebet` line break)
3. p.67 — `denne Indbildning forvandles Bevidstheden om Attraaen til ... Indbildningen om den menneskelige **Frihed**, og gjennem`
4. p.67 — `de Forestillinger, der ligge til Grund for Anskuelsen af en **personlig** Gud.` (Gud itself not spaced)
5. p.67 — `I dennes Sted træder **Naturmagtens Nødvendighed**,` (spans the line break; both halves spaced)
6. p.68 — `Naar Sub-stantsens **Uendelighed** medførte, at Alt, hvad der er,`
7. p.68 — `deri, at Gud kaldtes alle Tings Aarsag i **samme Betydning** som han kaldtes causa sui,` (spans line break)
8. p.68 — `der kan ikke blive Tale om en individuel **Frihed**, om Valgfrihed`
9. p.68 — `Gyldighed for Tingene have Begreberne **Nødvendighed og Umulighed** (skjøndt det sidste,` (spans line break)
10. p.69 — opening words of the page: `**nødvendig**,\footnote{...} enten med Hensyn til dens Væsen`
11. p.69 — `Modsætningen til det Nødvendige bliver det **Umulige**, hvilken Bestemmelse vi bruge`
12. p.69 — footnote 2: `illam **contingentem** dicemus — — quia`
13. p.71 — `Forestillingen om Nødvendigheden som **ydre** Tvang hænger altsaa`
14. p.71 — `giver Plads for den sande Idee om det Uendelige, bliver den ydre Nødvendighed til en **indre**, til Frihed ɔ:`
15. p.72 — opening word of the page: `**Naturen** bliver det fælles Navn, Gud og Naturen blive Synonymer.` (only this first "Naturen"; the second in the same sentence is not spaced)
16. p.72 — `Den bestemte begrændsede Tanke: **Ideen**, og den bestemte begrændsede Udstrækning: **Legemet**²), have deres positive Bestaaen` (Legemet spans the `Lege-met` line break)
17. p.72 — footnote 1: `omnia ex **naturæ divinæ** necessitate sequi,` (spans the `naturæ di-vinæ` line break; the later `secundum æternas naturæ leges` is NOT spaced)
18. p.73 — `enkelte Attributer danne sideordnede og **parallele** Rækker¹).` (Rækker not spaced)
19. p.74 — `vi i snævrere Forstand kalde **Natur: Udstrækningens**²) Attribut,` (both Natur and Udstrækningens spaced; Attribut on this line not)
20. p.74 — `Hos Spinoza er Udstrækningen opfattet som **Attribut**³), altsaa ikke blot`
21. p.74 — `altsaa ikke blot som uendelig og **udelelig**; men ogsaa som **activ**. Den` (two separate words)
22. p.74 — `Hvert Attribut udtrykker en **actuosa** essentia,`
23. p.74 — footnote 2: `I Eth. I, 15. schol. bruges Udtrykket: substantia **corporea**.`
24. p.75 — `saaledes ogsaa dens **Uendelighed** og **Udelelighed** (jfr. Eth. I, 8. 12. 13. Coroll. 15. schol.).` (both words)
25. p.75 — `og begribe den som Substants, **hvilket er meget vanskeligt**, saa vil den findes` (4-word run, comma excluded)
26. p.75 — `især naar der tages Hensyn til, at **Materien** overalt er den samme,`
27. p.76 — `sætte enhver Bestemmethed til Bevægelse i den enkelte Udstrækningsmodus som fremkaldt **udenfra**, om end det Bevægedes` (first occurrence only — the later `de udenfra fremkaldte` is plain)
28. p.76 — `Hvilende, synes Bestemmelsen **Materie** at være en hensigtsmæssigere Betegnelse.` (second occurrence of Materie, distinct from the already-marked one in the "Udtrykkene:" list)
29. p.77 — extend the existing run: `nemlig: \emph{Udstrækningens} ɔ: \emph{Materiens Enhed med} Gud, og de \emph{endelige Tings} Ikke-Realitet.` should become one continuous emphasis through **Gud** and through **Ikke-Realitet** — the whole clause `Udstrækningens ɔ: Materiens Enhed med Gud, og de endelige Tings Ikke-Realitet` is letterspaced as a unit in print.
30. p.78 — `Som Udstrækningens **uendelige modi**¹) bestemmes` (Udstrækningens itself not spaced)
31. p.78 — `nu **Bevægelse og Hvile**²) (Ep. 66, jfr. Eth. I, 32. Coroll. 2.);`
32. p.78 — `— De **endelige** Modi ere Legemerne.` (Modi/ere not spaced)
33. p.78 — `Legemerne. De **deduceres** ikke` (De/ikke not spaced)
34. p.78 — `af **hine**; thi en saadan Deduction er,`
35. p.78 — footnote 1: `sed tantum certo modo **secundum leges naturæ extensæ per motum et quietem** determinata` (spans a line break; "determinata extensio" after it is not spaced)
36. p.79 — `og føres saa **tilbage** til de uendelige Modificationer¹).` (føres and uendelige checked closely and judged NOT spaced — ordinary justification, not Sperrsatz)
37. p.79 — `Grundbegreber, **Physikens almindelige Sætninger an**-givne.` (spacing stops mid-word at the line break; "givne" is plain — printer's partial run, flag in a `%` comment rather than completing it)
38. p.79 — `Hurtighed og Langsomhed; for de **sammensatte** Legemer` (Legemer not spaced)
39. p.79 — `saa kunne disse Legemer kaldes **indbyrdes forenede**, og siges alle tilsammen`
40. p.81 — `stridende Forestilling om **enkelte** Legemer, gives der Individualitetens Begreb` (Legemer not spaced)

## (b) Existing `\emph{}` judged NOT letterspaced in print (false positives)

1. p.69 — `kunne de Bestemmelser finde Anvendelse paa \emph{natura naturata}, der ikke udtrykke` — the print sets `natura naturata` here in plain roman, no letterspacing at all (contrast with the genuinely spaced instances on p.68/p.71/p.72). Remove the `\emph{}`.
2. p.72 — `quam mens \emph{cum tota natura} habet«` — `cum` is set normally; only `tota natura` is spaced. Narrow to `\emph{tota natura}`.
3. p.72 — `— »\emph{Ex natura}, sub quovis attributo` — `Ex` is set normally; only `natura,` is spaced. Narrow to `\emph{natura}`.

## Not chased (out of scope)

`possibilis` in the p.69 footnote 2 (`Res *possibilis* — dicitur`) prints in
a visibly slanted/italic face, not letterspacing. The book's stated
convention is "no italic anywhere," so this is worth a maintainer's look —
but it is not a Sperrsatz question and this pass does not touch it.
