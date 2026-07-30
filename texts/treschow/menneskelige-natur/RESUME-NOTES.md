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
- ⚠ **§-numbering RESTARTS at each Hovedstykke.** The Indledning has §§ 1–6;
  the 1ste Hovedstykke begins again at § 1 (p. 11). So "§ 8" in this file means
  *1ste Hovedstykke § 8* (p. 16), not the eighth § of the book. Check which
  Hovedstykke you are in before citing a §. They are set inline at the head of a
  paragraph, not as display headings; transcribe as `8.~\emph{...}`.
- The chapter heading on p. 11 reads **"1ste Hovedstykke"** and "især fra **den**
  aandelige Side", where the Indhold has "dets". Headings are transcribed as
  printed on the page, not as given in the Indhold.

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
| **Tredie Hovedstykke.** Om Føleevnen — 1ste Afd., Følelser i Almindelighed | 188–227 | 206–245 |
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
- **DONE (image-verified, compiles 0/0, 34 pp., 164 emph):**
  - **Indledning COMPLETE, printed pp. 1–10** (§§ 1–6)
  - **1ste Hovedstykke COMPLETE, printed pp. 11–34** (§§ 1–18)
  - **2det Hovedstykke, 1ste Afdeling COMPLETE, printed pp. 34–60**
    (§§ 1–16, with § 6 skipped by the print — see below)
  - **2den Afdeling: printed pp. 60–70** (§§ 1–7)
  - **pp. 1–70 are CONTINUOUS** — verified, no gaps in the page-marker sequence.
- **NEXT — printed pp. 71–80** (scan 89–98), continuing the 2den Afdeling.
  Resume at the foot of p. 70, mid-§ 7 (Hørelsen), after "…Ja, der gives
  Meunesker, som uagtet deres Hørelse".
- **THEN** pp. 81–90 to finish the 2den Afdeling, then the 3die Afdeling
  (pp. 90–146) and 4de (pp. 146–188).
- The **Fortale** (roman I–VI+) is still untranscribed; do it at any convenient
  point — it is short and self-contained.

- **Translation:** hold until the Danish of a whole Hovedstykke is complete, then
  translate it as a unit (mirroring 1:1), rather than interleaving page by page.
  Terminology per `../enslige-ting/RESUME-NOTES.md`, plus for this book:
  Sands = sense; indvortes/udvortes = inner/outer; Aand = spirit; Legeme = body;
  Forestillingsevne = the faculty of representation; Føleevne = the faculty of
  feeling; Villie = will; Drift = drive; Færdighed = acquired skill;
  Lidenskab/Affect = passion/affect; Noümen = noumenon.
- **catalog.yaml:** DONE — entry set to `in-progress` under Treschow,
  `menneskelige-natur`, with the § 2 / § 11 / p. 27 material recorded.

## ⚠ A trap that has bitten once
A **Cyrillic е (U+0435)** got typed into "Følеevnen" and propagated into
transcription.tex, RESUME-NOTES.md and catalog.yaml. It is visually identical to
Latin "e" but breaks the LaTeX build with "Unicode character е (U+0435) not set
up for use with LaTeX". All instances are now fixed. To check after a batch:

```bash
grep -rnP '\x{0435}' --include='*.tex' --include='*.md' --include='*.yaml' .
```

A stricter sweep for any unexpected non-ASCII in the .tex:

```bash
python3 -c "
import io,collections
ok=set('æøåÆØÅéÉöüäÖÜÄ§—–…“”„»«‘’·×÷⚠')
bad=collections.Counter()
for ch in io.open('transcription.tex',encoding='utf-8').read():
    if ord(ch)>127 and ch not in ok: bad[ch]+=1
print({f'U+{ord(c):04X} {c}':n for c,n in bad.items()} or 'clean')"
```

Note also: p. 42 carries algebra ($a = x + y$ etc.). The print's **÷ is the older
sign for MINUS, not division** — transcribed as `\div` in math mode with a `% NB`
note at the site, so the glyph is faithful but the meaning is recorded. A literal
÷ therefore appears in one comment line; that is expected.

Also: an edit once **swallowed the `\end{document}`**, producing a bare
"Emergency stop" with no line number. If the log ends that way, check
`grep -c '\end{document}' transcription.tex` first.

## Notable so far
- **2den Afdeling, §§ 1–7 (pp. 60–70): the doctrine of the senses.** The
  organising claim is that *Sands* is originally **one** and only "ligesom deler
  sig" by the constitution of objects and of organs; the division into five is
  therefore read off the organs Nature has actually supplied us with ("hvor mange
  tydelig adskilte Sandseredskaber Naturen selv har forsynet os med", p. 61),
  not stipulated. Note the phrenological aside: the nerves "udgaae eller, som
  *Gall* mener, ende sig i Hiernen" (p. 61) — Franz Joseph Gall, contemporary.
- **§ 3 (pp. 61–63) argues for a *fælles Forestillingssands*** — a common
  objective sense — and this is the passage most directly useful for the
  natural-properties paper. Against "de fleste Philosopher", who derive the
  common representations by abstraction and so make the Understanding their
  source, Treschow objects that the Understanding "vel bemærker Ligheden, men at
  disse dog for at bemærkes, nødvendig maae være givne" (p. 62): likenesses must
  be *given* before they can be noticed. Hence a common sense through which
  "adskillige objective Beskaffenheder, saasom Enhed, Mangfoldighed,
  Forandring… ere givne" (p. 63). This is a *realist* answer to the aptness
  problem that does not go by way of an elite class of properties — the
  similarities are delivered in sensation, not selected by the intellect.
- **The senses are ranked by objective yield, not by nobility.** Hudfølelsen
  (§ 4, pp. 63–64) is conventionally counted among "de grovere og uædlere", yet
  Treschow insists it gives "baade de fleste og objectiv gyldigste
  Fornemmelser", and is what we use to correct the reports of the other senses
  about real presence, distance and size. Smagen (§ 5, pp. 64–66) is by contrast
  "den ringeste og uædleste af vore Sandser": its qualities are "blot subjective
  Fornemmelser, ei Egenskaber i Salterne selv", and its representations can at
  most prompt a *Formodning* about inner differences in the stuffs "hvis sande
  Beskaffenhed man dog paa en langt anden Maade maa udforske" (p. 65). So there
  is a working subjective/objective discrimination *within* sensation.
- **Lugten (§ 6, pp. 66–68)**: enriches the imagination but not the
  understanding, and the accompanying observation is a nice one about the poverty
  of a vocabulary — we have "meget faa Ord at betegne dem med", and must resort
  to comparisons ("sukkersødt, ædikesurt"), so these representations "ere derfor
  lidet klare".
- **Hørelsen (§ 7, pp. 68–70)** gets the strongest claim in the Afdeling: by
  sound alone we know "et *indvortes Liv i Tingene*", and we get a nearly
  immediate concept of *Harmonie* even though harmony "er et Forhold mellem
  Flere, og altsaa ei kan fornemmes" — the vibrations succeed each other fast
  enough that they are genuinely blended in the organ. Hence: "Der er følgelig
  ingen Sands, som til den menneskelige Aands Uddannelse mindre kan undværes"
  (p. 69). Worth flagging: this is a case of a **relation** being all but
  sensed, which is the Høffding *Relation som Kategori* thread arriving early.
- **§§ 15–16 (pp. 55–60) are a full theory of *Opmærksomhed* (attention)**, and
  the most systematically organised stretch of the book so far: attention is
  Tænkekraft with a determinate *intensive* magnitude, catalogued under three
  headings — **A.** how it is aroused (a) involuntarily by outer impressions,
  (b) freely by the will; **B.** its qualities (fiin, udstrakt, hurtig, let
  fortskridende, skiønsom, stadig/vedholdende); **C.** what weakens it (a)
  uniformity vs. distraction by manifoldness, (b) prolonged exertion, (c) the
  old and familiar vs. the new and surprising. The taxonomy is set in Sperrsatz
  throughout and rendered `\emph{}`; the A/B/C and a)/b)/c) labels are antiqua
  and are **not** emphasised (verified by zoom).
- **The Sperrsatz on p. 56 stops at the page break** — "d) *let fortskridende
  fra en*" is spaced, but "Ting til en anden" at the head of p. 57 resumes in
  ordinary Fraktur. A compositor's inconsistency; carried as printed with a
  comment.
- ⚠ **"enslige" resurfaces on p. 57**, and this is the term of art from the 1810
  prize essay: "Jo længere Tid desuden han behøver til nøiagtig Kundskab om
  **enslige Gienstande**, desto færre kan han i den korte Levetid lære at
  kiende." The context is a *cognitive-economy* argument against excessive
  Stadighed — the mind that isolates single objects becomes one-sided in
  judgement, because the important things can never be grasped except in
  connection with many lesser ones. This is worth flagging for the paper: it is
  Treschow himself supplying the pressure that the 1810 thesis is under. Only
  individuals are real, but a finite knower cannot afford to attend to them
  individually — so the "Hjælpemidler til Oversyn" are not an optional
  convenience but forced by the shortness of life.
- **p. 58: the "særegen Kreds" passage** — Nature assigns each person a
  characteristic field of attention; Philopoemen sees terrain as ground for
  attack or defence, the naturalist sees only plants, animals and minerals, the
  statesman cultivated and uncultivated fields, the antiquary monuments and
  ruins. A nice historical anticipation of *interest-relativity of salience* —
  and again in tension with an elite-class reading of naturalness.
- **§ 16 (pp. 59–60) defines *Reflexion*** as the Vexelvirkning between mind and
  objects: "Tanken er et Lys, vi kaste paa Tingene", and from the way things
  throw it back — i.e. by comparing the sensations of the Tænkekraft with the
  outer ones — we infer "Tingenes rette Beskaffenhed". The worked example is
  astronomical (a faint point in the sky referred to fixed stars, planets, or
  comets, then confirmed by closer observation of its place and motion). So
  reflection is inference to the object's real constitution, not mere
  classification — the realist half of the position.
- **2den Afdeling opens (p. 60)** by dividing sensation into immediate (real
  presence of the object outside the mind) and mediate (through the traces it
  leaves) — this is the Sandselighed/Indbildningskraft distinction. Then a claim
  relevant to the natural-properties project: *Sands* is **originally one**,
  and only modifies and "ligesom deler sig" according to the constitution of
  the objects and of the organs. Were the objects' side taken as the ground,
  there would be as many senses as there are Qvaliteter in things.
- ⚠ **p. 64 prints "de fleste Empiriken"** (for "Empirikerne") and **p. 70
  prints "Meunesker"** (a turned n/u for "Mennesker"); both carried as printed
  with a `% sic`.
- ⚠ **p. 57 prints "koster Mange Møie" with a capital M** (for "mange");
  carried as printed with a `% sic`.
- ⚠ **The print skips § 6** in the 2det Hovedstykke, 1ste Afdeling: it runs § 5
  (p. 43) → § 7 (p. 45). The unnumbered paragraph "For at kiende sig selv…"
  (pp. 44–45) continues § 5. Verified by zooming both pages; recorded with a
  `% sic` at the site. Do not renumber.
- **§ 8 (pp. 46–47)** carries over the § 4 algebra into a general claim about
  every representation: matter is the two unresolvable "Stoffer", the sub- and
  objective, present in every sensation, which no art can separate — compared to
  a compound the chemist cannot decompose. Then the pointed formulation: "Det
  Objective fremstiller de virkelige Ting, det Subjective blotte Phænomoner."
- **§ 9 (p. 47) is a direct hit on Kant**, and useful for the natural-properties
  project. Following Locke, Treschow distinguishes composite concepts *given in
  experience* (of natural substances) from those *we form ourselves* (the
  philosophical and mathematical). And: "Havde Kant lagt Mærke til denne
  Forskiel, vilde han ei have begaaet den Hovedfeil, at ansee alle Begreber om
  Gienstande for blotte Forstandens Former, og nægtet dem sand objectiv
  Realitet." He also denies there are simple representations at all — "ligesaa
  lidt aldeles enkelte Fornemmelser som Atomer og Monader."
- **§ 10 (pp. 48–50)** argues at length for **unconscious sensations** (*dunkle
  Fornemmelser*) — from unbidden associations, from delayed recognition of
  speech heard while asleep, from involuntary movements in sleep, and from the
  origin of the natural drives. The argument form is notable: the alternative
  would make the sequence of representations "gandske regelløs og uden Grund,
  hvilket dog er urimeligt at paastaae."
- **§ 13 (p. 53)** is where the naturalness vocabulary resurfaces: the object's
  own form consists in the real relation of the parts to each other and of the
  whole to other things, and this is knowable only through a *Begreb* with a
  **metaphysical form**, which is "ikke subjectiv, men objectiv: fordi den har
  almindelig Gyldighed". Lower representations "tiene saa at sige kun til privat
  Brug; de høiere ere overalt gangbare, og have, ligesom Mynten, et Slags
  offentligt Præg."
- **2det Hovedstykke § 3 (pp. 37–38)** contains the sharpest epistemological
  passage yet. One and the same sensation can be referred two ways: to the
  subject, as our own inner modification, or to the object, as a sign of
  something outside us — and then: "**Den første Maade er idealistisk, den anden
  realistisk.**" Idealism and realism are, on this account, not rival theories
  but two directions of reference available for the *same* sensation. He adds
  that we are self-conscious insofar as we are *active*, conscious of other
  things insofar as we are *passive*, and concludes "**Selvbevidsthed og
  Bevidsthed ere derfor ei ensbetydende.**" This is the two-modes doctrine
  applied to consciousness itself, and it is closer to a
  contextuality-of-description claim than anything in the 1810 essay.
- **§ 3 (p. 38)** also has a developmental argument: in early childhood we are
  conscious neither of ourselves nor of things; children speak of themselves in
  the third person, because "den udvortes Sands er skarpere end den indvortes" —
  so we learn to know ourselves as *object* before as *subject*.
- **§ 4 (pp. 41–43)** asks how a representation could resemble a thing at all,
  and answers with algebra: if the sensation is known $= a$ and object and
  subject are unknown $= x$ and $y$, then $a = x + y$, and solving for $x$ gives
  an equation "which one cannot solve at all without further given quantities."
  Two partial constraints are offered — agreement across several senses, and
  agreement of inner with outer — but he grants they are insufficient, and
  concludes that reason can fix the necessary *form* of things while sensibility
  must supply the matter: "derom kan Fornuften intet lære."
- **§ 5 (pp. 43–44)** separates *Kundskab* from *Forestilling*: to know is to
  represent the actual as determined by properties answering to our sensations,
  and knowledge is "ei alene noget andet end Indbildninger, men endog end
  Forestillinger om virkelige Ting." Hence Socrates could disclaim knowledge
  without disclaiming representations — "der imellem dem og Kundskab er en
  uendelig Forskiel."
- **§ 15 (pp. 27–29)** reaches a striking parity claim. Neither soul nor body is
  immediately known: knowledge of both is *mediate*, reached by the same kind of
  inference. Hence "Man kan derfor ikke sige, at enten Siel eller Legeme er os
  bedre bekiendt end det andet; thi begges Kundskab er middelbar, og Beviserne
  … have paa begge Sider lige Styrke." He uses this to hold the balance between
  materialists and spiritualists — each of whom, he says, takes experience in
  too narrow a sense and forgets the other side.
- **§ 16 (pp. 29–30)** shows what the identity-system costs: on the dualist
  scheme "pure spirits" are unproblematic, since spirit subsists by itself; on
  Treschow's, no finite spirit can be pure, because as a finite being it needs
  the body for its development and interaction with the world — so **every
  object of the inner sense must have an outwardly intuitable form as its other
  side**. And, characteristically: "Men herom kan Erfarenhed intet lære."
- **§§ 17–18 (pp. 30–34)** set up the book's architecture: one *Grundkraft*, but
  as many faculties as there are distinguishable kinds of inner experience;
  hence the three main faculties — Forestillingsevnen, Føleevnen, Villien —
  which give the remaining three Hovedstykker. § 18 grades "higher" faculties by
  fineness, extent (*Omfang*), strength and self-activity — with the nice detail
  that the senses are moved only by *enslige Gienstande*, while the
  understanding takes in all of them by the higher concepts of genera and
  species, and reason the possible as well as the actual.
- **§ 12 (p. 23)** distinguishes four senses of "Aand": the subject of the inner
  changes; the subject of consciousness alone; the finer organism or abiding
  Grundform; and **the human being as noumenon or Idea, "der ikkun tænkes, men
  ei erfares"**. The Kantian vocabulary is explicit, and the fourth sense is the
  one that links to the 1810 Grundform and to *Om Gud*.
- **§ 13 (p. 24)** meets the Kantian objection head-on — that experience is "en
  blot subjectiv Grund" and the unity of consciousness "kun en Form i
  Forstanden". Treschow's reply is that consciousness is *immediate* and so
  cannot arise except from the very being one thereby perceives, "hvori ingen
  Forblindelse eller Vildfarelse kan have Sted"; and that without an objective
  ground consciousness would be unintelligible.
- **§ 14 (pp. 25–27)** answers the gradual-extinction objection: forces are not
  quantities that fade out, they only appear to vanish when displaced from a
  connection. Hence "Bevidstheden svækkes derfor ikke i sig selv eller som Kraft
  betragtet, men kun som enslig Handling eller Virkning af samme Kraft" — with
  the fine image of the old man in whom the inner force still glitters, "som
  Lysets sidste Glimt, i et tindrende Øie og Tankens himmelske Flugt."
- **The chapter's conclusion (p. 27)** is careful about its own status: the
  formative force that rebuilds after dissolution "kan derfor som Hypothese i
  Anthropologien vel have Sted. De høiere Grunde for dens Rigtighed vedkomme
  derimod den speculative Philosophie." He marks exactly where empirical
  psychology stops and speculation begins — then states the conclusion.
- **1ste Hovedstykke § 1 (p. 11)** states the identity thesis outright, and more
  sharply than the later p. 20 formulation: "Efter Identitets Systemets
  Grundsætninger kan Mennesket vel betragtes som et sammensat Væsen; men ei som
  sammensat af Siel og Legeme; thi begge ere kun **modsatte Sider af det
  samme**: saavidt det nemlig baade kan være Gienstand for den indvortes og
  udvortes Sands." Body and soul are opposite *sides*, individuated by which
  sense can take them as object.
- **§ 2 (p. 12)** ties the book to the 1810 essay by name: the Grundform's
  development in the sense-world answers to what in a higher order of things is
  called an Idea, and "I denne Grundformens og Ideens Uforanderlighed bestaaer
  hvert Menneskes Individualitet."
- **§ 7 (p. 15)** dissolves the mind–body problem rather than solving it: "Om
  Muligheden af en reel Forbindelse mellem Siel og Legeme kan her intet
  Spørgsmaal være; thi i sig selv ere de jo den samme Ting." What remains is
  only the easier question how a finer and a coarser organisation are united.
- **§ 6 (p. 15)** anticipates the § 11 argument: the unity and indivisibility of
  consciousness gives "en langt fastere Middelpunct end nogen, der udvortes
  lader sig anskue" — the inner access yields a centre the outer never could.
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
