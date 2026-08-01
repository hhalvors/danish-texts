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
- **DONE (image-verified, compiles 0/0, 112 pp., 522 emph):**
  - **Indledning COMPLETE, printed pp. 1–10** (§§ 1–6)
  - **1ste Hovedstykke COMPLETE, printed pp. 11–34** (§§ 1–18)
  - **2det Hovedstykke, 1ste Afdeling COMPLETE, printed pp. 34–60**
    (§§ 1–16, with § 6 skipped by the print — see below)
  - **2den Afdeling COMPLETE, printed pp. 60–90** (§§ 1–16)
  - **3die Afdeling COMPLETE, printed pp. 90–146** (§§ 1–24, with 24 used twice)
  - **4de Afdeling COMPLETE, printed pp. 146–188** (§§ 1–15)
  - **➤ THE 2det HOVEDSTYKKE IS COMPLETE (pp. 34–188).**
  - **3die Hovedstykke (Om Føleevnen), 1ste Afdeling (Om Følelser i
    Almindelighed) COMPLETE: printed pp. 188–227** (§§ 1–17, with 13 used twice)
  - **2den Afdeling (Om de forskiellige Slags behagelige og ubehagelige Følelser)
    begun: printed p. 227** (§ 1)
  - **pp. 1–227 are CONTINUOUS** — verified, no gaps in the page-marker sequence.
    That is **47 %% of the body** (which runs to p. 486).
- **NEXT — printed pp. 228–237** (scan 246–255), continuing the 2den Afdeling
  (which runs to p. 269). Resume at the foot of p. 227, mid-§ 1, after "…Stik af
  et giftigt Insect foraarsager ligeledes en dobbelt ubehagelig Følelse; hvoraf
  den ene ei kunde".
- **THEN** the rest of the 2den Afdeling, and finally the 4de Hovedstykke (Om den
  menneskelige Villie, pp. 270–486) — which alone is 217 pp., nearly half the
  book.
- **THEN** the rest of the 1ste Afdeling (to p. 227), the 2den (pp. 227–269), and
  finally the 4de Hovedstykke (Om den menneskelige Villie, pp. 270–486).
- **THEN** the rest of the 4de Afdeling (to p. 188), which closes the 2det
  Hovedstykke; after that the 3die Hovedstykke (Om Føleevnen, pp. 188–269) and
  the 4de (Om den menneskelige Villie, pp. 270–486).
- **THEN** the rest of the 3die Afdeling (to p. 146) and the 4de (pp. 146–188).
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
- ⚑ **p. 224 keeps the monism running through the philosophy of mind.** Of the
  Sieleorgan: "rimeligviis er den finere Materie, hvoraf det bestaaer, dog **ei
  væsentlig forskiellig fra den grovere**, hvis almindelige Beskaffenheder vi
  kiende." Finer and grosser matter differ in degree, not in kind — the same
  move as "Godt og Ondt… kun i Graderne forskiellige" (p. 214) and the reduction
  of qualities to "det Reales besynderlige Indskrænkninger" (p. 215). Note also
  his candour: such explanations should not be expected to satisfy completely,
  since in both grosser and finer matter "ere der saa utallige Afændringer, at det
  hverken er muligt at angive dem allesammen".
- ⚑ **p. 221 — a methodological rule that cuts against his own besetting
  temptation.** "Man maa i Sielelæren, ligesom i den øvrige Naturlære, vogte sig
  for den Feil af alt for **besynderlige** Aarsager at ville forklare alle
  Phænomener." Beware explaining all phenomena from causes that are too
  particular. The target is Verri and Locke on pleasure as mere relief from pain
  — remarks "som oftest rigtige, men blive skæve og ensidige, fordi man fra en
  alt for lav Standpunct betragter den hele Sag."
- **§ 16 (pp. 222–225) is a typology of individual difference in feeling** —
  ease of reception (with two kinds of sensitivity, one joined to weakness and
  one showing strength, on the analogy of soft versus hard-and-elastic bodies),
  constancy of retention, capacity for more or fewer kinds, vehemence and
  strength, fineness and coarseness. Its conclusion is worth having: "Føleevnen
  selv ei er saa enkelt; men, ligesom Sandseligheden overhovedet, bestaaer af
  flere, og at dens Organer derfor tillige ere flere" (p. 225) — the faculty of
  feeling is not simple, and neither is its organ, "enhver Nerve har sin egen
  Maade at føle paa".
- **§ 17 (pp. 225–227) closes the Afdeling on the reform of feeling**, and the
  line is characteristically two-sided: correct concepts are needed to bring the
  feelings into a rational proportion, "Men dette Middel er ei tilstrækkeligt,
  dersom ikke Legemet tillige styrkes." He is caustic about the philosophies that
  distort feeling — Epicureans, Stoics, Mystics, Eudaemonists, Rigorists — and
  notes that systems condemning all feeling merely make one feeling, "den af egen
  Høihed og Værdighed", the more vivid: "Spartanerne, Stoikerne og adskillige
  **Kantianere** bevise ved Exempler denne Setnings Rigtighed."
- **The 2den Afdeling opens at p. 227** with a division of feelings by source —
  from representations, or from bare impressions on the body and outer senses
  "hvoraf vi om Gienstandenes eiendommelige Beskaffenhed intet lære."
- ⚑⚑ **p. 215 — an explicit prohibition on inferring the real from the felt, plus
  a striking account of what sensory qualities are.** "Men derfor maa man ei
  heller bedømme **Tingenes virkelige Beskaffenheder af Følelser**." And then:
  "saaledes forholder det sig ved enhver sandselig Fornemmelse, hvis forskiellige
  Qvaliteter ei er noget andet end **det Reales besynderlige Indskrænkninger** at
  tilskrive." Sensory qualities are to be ascribed to nothing but the particular
  *limitations of the real* — a privative account of quality that sits exactly
  where the monism needs it: the real is one and unlimited, qualities are its
  restrictions. Note the parallel argument about physical evil, which only
  *seems* positive, and which is explained teleologically.
- ⚑ **p. 217 restates the double-aspect thesis for affect.** "\emph{Alle Følelser
  have følgelig noget i sig af Menneskets dobbelte Natur:} ingen hører gandske til
  en Art alene." No feeling belongs wholly to one side. This is the Indledning
  § 2 doctrine — the same reality under two irreducible modes — now applied to
  the feelings, and it is argued empirically (religious enthusiasm and moral
  feeling show themselves in flashing eyes, blushing, muscular exertion just as
  sensual objects do).
- **p. 216 carries a *resolvable* cross-reference, "II, 2, 12"** — Hovedstykke II,
  Afdeling 2, § 12, printed p. 79, i.e. the parallelism law itself. So the
  reference apparatus does sometimes work, and this one confirms the format.
- **p. 214: "Godt og Ondt… ere dog kun i Graderne forskiellige, og berøre, saa at
  sige, hverandre: ellers var ingen Overgang muelig."** Good and evil differ only
  in degree — the quantitative thesis of p. 197 extended to value. But note the
  qualification at p. 215: although the *causes* of these feelings differ only in
  magnitude, that does not hold of the feelings themselves — "Man kan ikke sige,
  at Smerte bestaaer i en høiere eller lavere Grad af Vellyst."
- **§ 12–13 (pp. 209–214) distinguish the *interesting* from the merely
  agreeable**, and the criterion is effort: an object is interessant when it
  gives matter for activity "men til en, der koster Anstrængelse", whereas the
  agreeable demands no work we do not think we can do easily. Hence tragedy,
  executions and bad news draw as many spectators as their opposites: "Det kommer
  ei an paa Gienstandens Beskaffenhed, men paa dens Størrelse" (p. 209). The
  novelty/habit material that follows is a small sociology of intellectual
  resistance — Anaxagoras, the Roman statesmen on Christianity, Meiners, Feder and
  Eberhard declining to become Kant's disciples because that would mean recanting
  what they had taught.
- ⚑⚑ **§ 6 (p. 199) states the law of the agreeable in terms of *qualities*, and
  it is worth having beside the p. 197 subject/object split.** In Sperrsatz:
  "\emph{Gienstandenes Qvaliteter kun ved den forskiellige Beqvemhed, de kan have
  til at hindre, mere eller mindre at vække vor Virksomhed og Bevidstheden af
  samme, ere os behagelige eller ubehagelige.}" Qualities are pleasant or
  unpleasant *only* through their fitness to arouse or block our activity — so
  affective value is a relation to a capacity, not a property of the object, yet
  it is grounded in the object's qualities. Neither a projectivism nor a naive
  realism about value.
- ⚑ **p. 200 turns the 1810 thesis into an explanatory demand.** To say why a
  given smell pleases, "maatte man ei alene kiende Tingenes og det følende
  Subjects Egenskaber i Almindelighed, men ogsaa **Grundene til al Individualitet
  og Idiosyncrasie**." General properties of object and subject are not enough;
  one would need the grounds of individuality itself. And he adds the
  methodological point that our ignorance of the mechanism licenses no inference
  against the main proposition.
- **§ 5's law is then filled out with a long empirical catalogue (pp. 201–208)**,
  and it is more interesting than it looks. Quantity alone converts one kind of
  feeling into the other (Socrates on the chain-marks: "Godt og Ondt… ere bundne
  sammen ved Enderne", p. 201). Sustained irritation becomes unpleasant, whence
  \emph{Kedsomhed} and then \emph{Væmmelse}: "Naar samme Organ nemlig altid
  pirres paa samme Maade, taber det efterhaanden sin særegne Virksomhed"
  (p. 202) — so **variation is a condition of continued function**, not a mere
  preference. Representations that sustain aroused activity please, those that
  block it displease (§ 8, p. 203), with applications to long digressions in epic
  and to notes in a text. § 9 (p. 204): all exercise pleases "hvorved vi føle
  Styrken af vor Kraft".
- **§ 10 (pp. 205–207) is the best-written stretch here**: no state is more
  unbearable than one in which we have nothing left to hope, "om den endog i sig
  selv var den lykkeligste". Suppose every wish granted on condition of no
  further advance — one would see at once how much better it had been to work
  toward "et ubestemt Maal, som han stedse, jo videre han kom, var istand til at
  forlænge." Alexander lamenting no world left to conquer; Pyrrhus embarrassed by
  the question what he would do when tired of conquering; the old man consoled
  that the trees he planted will spread. **Holberg** appears too (p. 205), taking
  the metaphysics chair unwillingly and gladly exchanging it — a nice cross-link
  to the Holberg entry in the catalogue.
- ⚑⚑ **p. 197 (C) — the cleanest subject/object statement in the book, and it
  divides the labour by *category*, not by degree.** "\emph{Grunden til vore
  Følelser er altsaa dobbelt, nemlig baade subjectiv og objectiv.}" Then: when we
  *represent* a thing the relation between subject and object is
  \emph{qvalitativt} — "mellem Sandselighedens og de udvortes Tings **selve Væsen
  eller Natur**"; when we *feel* it the relation is only \emph{qvantitativt}, a
  matter of the two forces' strength. So representation reaches essence,
  feeling only magnitude. That is a principled place to put the
  objective/subjective line, and it is the same architecture as the Materie/Form
  analysis of Afd. 1 § 8 (p. 46), now applied to affect.
- **§ 4 (pp. 195–197) argues the point in two moves.** A (p. 195): pleasure and
  pain are *not* to be ascribed to the object or our representation of it alone,
  "thi ellers maatte de deraf nødvendig og stedse følge" — habit, boredom,
  temperament and circumstance make people differ. B (p. 196): but neither do
  they rest on the subject alone, since we are affected differently according to
  the objects' constitution "endskiøndt Subjectet og dets Tilstand for Resten ere
  de samme". The examples are good — tobacco smells the same to everyone yet
  delights some and disgusts others; yellow makes the same impression on all, yet
  only the Chinese prefer it, as the Turks prefer green. **This is exactly the
  structure the paper wants for secondary qualities: constant objective input,
  variable affective response, and neither side alone sufficient.**
- ⚑ **§ 1 (p. 189) states the deflationary half plainly:** "\emph{Følelser ere
  altsaa ikke Forestillinger, men blotte subjective Fornemmelser}" — when we call
  something pleasant "saa mene vi dog ikke, at dette er Tingen tilhørende". And a
  fine observation on how affect crowds out representation: when the fire burns we
  think no longer of the fire or its heat "men paa vor Smerte".
- **§ 2 (pp. 190–192) is a sustained refutation of Leibniz**, whose view — that
  all feelings arise from *confused* representations, so that feeling must cease
  when they become distinct — Treschow says "grunder sig paa en ufuldstændig
  Induction". He grants two of Leibniz's points and denies the conclusion: what
  makes a representation move us "er snarere Liv og Styrke end Utydelighed", and
  distinctness does not hinder feeling "naar man, efterat Analysen er fuldendt,
  bag efter overskuer det Hele" (citing Mendelssohn). Then the strong thesis:
  **no representation whatever is without effect on feeling** — even those that
  seem wholly indifferent, "saa foretrække vi dem dog for slet ingen at have."
- **§ 5 (p. 198) gives the general law of the agreeable**: an impression is
  pleasant when it has "et passende Forhold til vor Receptivitet eller Kraft" —
  stimulating without over-straining or blocking. The a priori argument for it is
  worth noting: the feeling of our own existence cannot be indifferent to us,
  hence neither can the feeling of our force and activity, "thi **kun for saavidt
  vi virke ere vi til**." Descartes and Wolff (perfection) and Sulzer (freedom in
  thinking) are named as the rival accounts.
- ⚑⚑ **p. 186 — "Stykkeviis Kundskab er derfor ikke heller Viden."** Piecemeal
  knowledge is not knowledge, "thi hiin standser ved de besynderlige Grunde, denne
  omfatter Alt formedelst de almindelige og høieste, **hvori det nødvendig ligger
  skiult, om der end maaskee gives meget Besynderligt, som man deraf ei er istand
  til at udvikle.**" The particular lies *contained* in the highest grounds — but
  not derivably, for us. Read alongside p. 168 ("Enhver enslig Ting… Aftryk af en
  Idee") this is the whole position in miniature: individuals are what is real and
  fully determinate; the general grounds contain them; and no finite knower can
  unfold the one from the other. Note too the concession just before: "I Henseende
  til Tingenes reale Grunde, er den menneskelige Kundskab ifølge Tænkekraftens
  Væsen selv **nødvendig ufuldkommen og relativ**."
- **p. 178 gives individuality a social cost.** "Ethvert Menneske har sin
  individuelle Form, hvoraf følger noget i Handlinger og Charakter afstikkende,
  hvorved… [man] bliver mindre skikket til det selskabelige Liv." Politur is the
  wearing-down of "det Rue og Ujævne" until people fit together "ligesom Delene af
  en Maskine". The Englishman takes Cultur as well as anyone but Politur badly,
  "som han mindre kan fornægte sin Individualitet" (p. 180). So the individual
  Grundform of p. 168 is metaphysically basic and socially abraded — a nice
  tension to note, not to resolve.
- **§§ 12–13 (pp. 181–185): Oplysning, Visdom, Klogskab.** Enlightenment requires
  both a *form* (facility in orderly thinking) and *material* knowledge, and
  Treschow is sharp about the difference: memorised propositions, "skiøndt i sig
  selv rigtige", produce no enlightenment, and much supposed enlightenment "bestaaer
  alligevel ei i andet end i visse Ordformularer og Sentenzer". He then takes the
  contemporary debate over popular enlightenment seriously on both sides before
  coming down for it. Wisdom is defined as "Oplysning, forenet med Sielestyrke til
  at handle derefter"; Aristotle (*Magna Moralia*) is cited for the wisdom/prudence
  distinction, and Horace for the ancients' conception.
- **§ 14 (pp. 185–187) closes the Hovedstykke with definitions** of Videnskab,
  Kunst and Lærdom — learning being "et velordnet Vare-Magazin" that by itself
  yields neither art nor science, "langt mindre Visdom eller Klogskab" — and § 15
  treats *sensus communis* as natural good sense that has nonetheless been
  cultivated, so the dispute over whether it is innate or acquired is dissolved
  rather than settled.
- **The 3die Hovedstykke, Om Føleevnen, opens at p. 188** with a definition that
  matters for the paper's subjective/objective theme: "Ordet \emph{Følelse} betyder
  her i Almindelighed en Fornemmelse, saavidt den enten er behagelig eller
  ubehagelig. Disse Ord betegne ei Beskaffenheder i Gienstanden, men i
  Fornemmelsen alene."
- ⚑⚑⚑ **p. 168 — the 1810 thesis restated in the vocabulary of Ideas, and the
  bridge to *Om Gud*. This may be the single most quotable sentence in the book.**
  Having defined Ideas as "de rene Begreber om Tingenes høieste Grunde", divided
  into \emph{theoretiske} and \emph{practiske}, he lists the theoretical ones:
  "Gud, Kraft, saavidt den tænkes uden Grændser, **Individualitet, som Tingenes
  uforanderlige Grundform**, der evig udvikler sig efter et uendeligt Mønster, ere
  theoretiske Ideer." And then:
  > **Enhver enslig Ting kan i denne Mening betragtes som Aftryk af en Idee, ei
  > Arterne og Slægterne alene.**
  Every singular thing is the impress of an Idea — **not the species and genera
  alone.** That is exactly the 1810 claim, now with a positive metaphysics behind
  it: individuality *is* a Grundform, and there are Ideas of individuals. Note
  also "Ingen af disse Ideer er for os anskuelig, men vel for den guddommelige
  Forstand" — the Ideas are fully determinate but not intuitable by us, which is
  the p. 163 point again.
- ⚑ **p. 171, first line — Treschow locates his own position.** "Dualismus's
  Opfindelse røber derfor mere Skarpsind, Identitets Systemets Dybsind." The
  invention of dualism betrays more acuteness; that of the Identity System, depth.
  Acuteness dissolves, depth unifies — and he has just said (p. 169) that
  "\emph{Dybsindighed forudsetter derfor Skarpsindighed}", so the monist is not
  excused from analysis, only required to go further.
- ⚑⚑ **p. 170 is Treschow diagnosing precisely the tension you raised.** "Derfor
  er Philosophie, Metaphysik og det Spørgsmaal om Tingenes første Grunde, om de
  simpleste og rene Begreber tidt en Daarlighed i skarpsindige Naturforskeres
  Øine. De største Chemikere, Anatomer, Naturbeskrivere… ere tidt Foragtere af de
  høiere Videnskaber, og declamere med Iver mod alle Systemer, der af faa eller
  endog et eneste almindeligt Princip søger at forklare alle Naturens Særsyner."
  His diagnosis: acuteness is so busy dissolving "at den ei faaer Tid til at tænke
  paa nogen Forbindelse". And the examples he gives of unification are real,
  contemporary science — whether electricity and galvanism are one, whether plant
  and animal life is the same activity that shows itself in crystal formation.
- **p. 169 on method:** an objective science can be *presented* synthetically but
  is "altid opfunden ved Analysis"; one starts from the most composite objects of
  experience, and the more different Beskaffenheder one finds in them, the closer
  one comes to their ground — because one then notices how a barely perceptible
  difference gradually becomes larger "og omsider gaaer over i en gandske modsat".
- **§ 9 (pp. 171–175) on genius**, defined at last as "en \emph{Naturgave til
  efter uudviklede Ideer eller selv opfundne, men ubestemte, Ordens Regler ved
  Phantasiens Hielp at frembringe eller opfinde}." Against Kant, who "har derfor
  indskrænket Begrebet om Genie til de skiønne Kunster alene", Treschow insists
  genius is needed in mathematics (choosing among equally good forms of an
  equation), in the practical sciences, and in ordinary life — where what is
  wanted is *Tact*, "der som et pludseligt Skin i Mørke paa engang oplyser
  Gienstandene, men alt for hastig igien forsvinder til at man kunde beskrive
  deres Udseende." Gerard, Resewits and Kant are named as the moderns who worked
  on the question; Oholiab and Bezalel as scripture's artistic geniuses.
- **§ 10 (pp. 175–176) opens on Cultur**, with the agricultural etymology spelled
  out (preparing the ground, sowing, favourable weather) and the threefold Vilde /
  Barbarer / civiliserte division. The definition of the savage uses "enslig"
  once more: those whose knowledge extends no further than "det \emph{enslige}
  Væsens Vedligeholdelse og første Nødvendigheder."
- ⚑⚑⚑ **p. 164 — the single best answer to the objection that Treschow's position
  is anti-theoretical.** Judgement is sharpened, he says, "c) \emph{Ved
  theoretiske Kundskaber,} endog saadanne, der hentes af Tingenes første Grunde;
  da Dømmekraften ellers let forvildes af saa mange **eenslige** Exempler,
  besynderlige Regler og Undtagelser. **Uden Principier**, ved hvis Hielp man,
  ligesom fra et høiere Sted, kan oversee deres Forbindelse eller Rekke, vil man
  hverken være istand til at erindre dem alle, eller vide hvad der passer paa
  nærværende Tilfælde." And then, of the mere practitioner who applies to a new
  case the rules that worked in similar ones: **"Thi hvorvidt de virkelig ligne,
  kan Theorien alene lære."**
  Real similarity is not read off the surface; theory alone can teach it. Note the
  use of "eenslige" — here the singular cases are the *problem*, and principles
  the remedy. Taken with p. 148, this settles that the 1810 thesis is a claim
  about what is *real*, not a recommendation about how inquiry should proceed.
- ⚑ **p. 158 gives the two ways distinction-drawing fails, and they are exactly
  the two tiers.** "Men Skarpsindighed vanslægter undertiden til
  \emph{Spidsfindighed}, naar Tingenes Forskiel **ei er værd at bemærke**, og til
  \emph{Haarkløverie}, naar den **ei engang er virkelig**." Over-subtlety = a real
  difference not worth marking; hair-splitting = a difference that is not real at
  all. Same structure as the essence/importance split at p. 150. The scholastic
  examples are good ones for a paper: whether a goat's hair may be called wool,
  whether the ox is drawn to market by the rope or by the man.
- **§ 4 concluded (p. 157): acuteness must cut both ways.** "\emph{Den ægte
  Skarpsindighed er altsaa en Gave til at udfinde Tingenes **virkelige** Lighed
  eller Forskiel}" — and the acute man "ligesaa vel maa bemærke den væsentlige
  Overensstemmelse, der mellem de forskielligste Ting er at finde", on pain of an
  Ensidighed that turns the perfection into a defect.
- ⚑ **p. 160 — a genetic account of the categories.** The highest concepts (Tid,
  Rum, Afstand, Aarsag, Grund, Substans) are products of "Tænkekraftens ubevidste
  Virksomhed i en Alder, hvori vi handle paa en gandske instinctmæssig Maade";
  philosophers' disputes about their origin only prove how little we can recall
  forming them. Hence metaphysics and logic contain nothing but efforts "for at
  besinde sig" — recollection, but **not** Plato's of pre-natal knowledge, rather
  of "vor Barndoms Beskæftigelser og Tænkekraftens Udvikling formedelst samme."
- **p. 163 states the realism about determinacy** that the paper's monistic
  reading needs: in any difficult case one becomes aware of "kun nogle, ei alle,
  Sider… af en **uforanderlig og i sig selv fuldkommen bestemt Idee**." The object
  is fully determinate; our access is partial. This is the 1812 form of what *Om
  Gud* will call the individual Ideas.
- **§§ 5–6 (pp. 158–166) on Fatteevne and Dømmekraft** are largely practical, but
  two points carry: judgement "kan følgelig ei engang i den empiriske Sielelære
  betragtes som en besynderlig og fra de andre gandske forskiellig Evne" — it is
  not a separate faculty, and has no domain of its own (contra the third Critique,
  though Kant is not named here); and the old dispute of theory vs. practice is
  refused rather than settled — "Uden Tvivl er det bedst, naar begge Midler ere
  forbundne."
- **A dated political aside worth knowing about (p. 166):** the first draft of the
  French Revolution was made by "et philosophisk Partie" that miscalculated how
  far principles about innate rights, liberty and equality could be applied in
  legislation to a people not yet prepared for them by enlightenment and morality.
  Treschow grants the principles are "i sig selv meget rigtige" — the objection is
  about application, and it is the same application/content distinction he uses
  throughout.
- ⚑⚑⚑ **The 4de Afdeling (from p. 146) is on the Forstand, and pp. 148–156 are the
  richest stretch in the book for the natural-properties paper. Four passages.**
- **(i) p. 148 — Treschow answers the charge of excessive particularism.** He
  reports that the newest school undervalues the understanding, in part because
  it "kun afsondrer og deler uden at forbinde, hvorover den menneskelige Aand er
  kommen saavidt ind i **det Enkelte og Enslige** eller Besynderlige, at den neppe
  bliver istand til at samle det igien." His reply: such charges can be made
  against any faculty taken alone, and "Forstandens Arbeide [bestaaer] ei alene i
  at opløse og abstrahere, eller dele, da vi derved alene intet Begreb kunde faae,
  men ogsaa i at **forbinde**: og denne Forbindelse samt Indsigt i Enheden af det
  Mangfoldige…" So Treschow explicitly disowns the position that stops at the
  singular. This is the passage to cite against the objection that his 1810 thesis
  leaves him unable to account for general structure.
- **(ii) p. 149 — the monist argument runs *through* analysis, not against it.**
  "Jo flere Slags Stoffer vi paa denne Maade lære at kiende, desto tydeligere
  bliver Enheden af en første Materie… desto mere bliver det os indlysende, at
  Grundkraften og Grundformen kun er en eneste." And then a mathematical
  illustration: circle and polygon, curve and straight line "ei ere saa
  forskiellige som de synes: modsatte Ting selv smelte derved sammen." Note the
  direction of argument — *more* science, more analysis, yields *more* monism.
  That is the reply to the worry that Treschow's metaphysics is at odds with
  scientific practice.
- **(iii) pp. 149–151 — understanding is *classification*, and importance is
  interest-relative while essence is not.** To understand a thing is to know
  "hvad Orden eller Klasse vi skal henføre Gienstanden til, hvad Plads vi skal
  anvise den blandt de Ting, vi ellers kiende" — "Vi forstaae ikke hvad Mosen,
  Skimmelen og Paddehatten er, saalænge det er uvist til hvilket af de saa kaldte
  Naturriger de bør henføres." Then the crucial distinction (p. 150): "Begrebet om
  \emph{Vigtighed} er relativt, og har altid Hensyn til noget andet… En Tings
  **væsentlige** Egenskaber ere uden Tvivl **for den selv** de vigtigste, men for
  andre Ting kan de tilfældige være vigtigere. Blomsternes Lugt og Farve ere for
  dem selv uvæsentlige, men i Lysthaver og Urtepotter tages disse fornemmelig i
  Betragtning." **Two tiers: essence is absolute, importance is relative to a
  purpose.**
- **(iv) p. 151 makes it a *domain* thesis, which is the reframing the paper
  needs.** "En grundig Naturbeskriver bestemmer Planternes Kiendemærker i
  Natursystemet efter Kiønsdelene, men for Havekunsten enten efter deres Skiønhed
  eller Nytte i Huusholdningen, for Forstvæsenet efter deres Størrelse og Træets
  Brugbarhed… **Men i alle tre Videnskaber kan Forstanden vise Grundighed.** Denne
  yttrer sig derfor i anvendte saavelsom i rene Videnskaber, hvoraf disse
  fornemmelig have **Tingenes Væsen**, hine deres **Vigtighed for et eller andet
  Øiemed** til Formaal." Linnaean sexual system, horticulture and forestry are all
  capable of *Grundighed*; they differ in aim, not in rigour.
- **And p. 152 blocks the relativist reading outright:** "\emph{Skæv er
  Forstanden,} naar den finder Ligheder og Kontraster **hvor ingen ere.**" A
  general concept can be *wrong* — one under which "de forskielligste Ting synes
  lige", or under which likeness disappears among things that fully agree. With
  p. 156's "mangen Lighed kan være mere væsentlig end den synes", this is as clear
  a realism about similarity as one could want from someone who denies an elite
  class of properties.
- **Lighter matter in §§ 3–4 (pp. 154–156): a theory of wit.** Wit is "en med
  Overlæg spillende Forstand" — pretending to treat the unimportant as important
  in order to draw attention to what is essential. The examples are worth keeping:
  the author who matched monastic orders to insect species by Linnaean characters
  ("abdomine magno, dorso incurvo"), Wessel on the wren, the Franklin epigram
  "eripuit cœlo fulmen sceptrumque tyrannis". Wit and acuteness differ in that
  acuteness looks to the essential and wit to the accidental — but they converge,
  because a likeness may be more essential than it looks.
- **§§ 20–23 (pp. 130–140): sleepwalking, presentiment, prophecy and madness.**
  Naturalistic throughout, and the method is worth noting even where the content
  is dated — in each case Treschow takes a phenomenon the age treated as
  supernatural and derives it from the § 18 machinery running without the usual
  checks.
- **§ 20 (pp. 130–133) explains sleepwalking by a *dissociation of two systems*.**
  Sensibility and motion depend on nerve-force and muscle-force respectively;
  these are normally proportioned, but need not be. In sleepwalkers the sense
  organs are weak while the muscles retain strength, so the images are vivid and
  the limbs still obey the will. The confirming contrast is elegant: in the dying
  and the apparently dead the ratio is reversed — they can move no limb "men
  alligevel see og høre" — and in wasting diseases muscle-force fails before the
  senses, "hos Nattevandrere har det Modsatte Sted." No special faculty is posited.
- **§ 21 (pp. 133–135) on *Ahnelse*.** Presentiment is not a power of foresight
  but an inference whose premises are dark: "Heri er Slutningen alene tydelig, ei
  Forsetningerne." A dark sensation of some imperceptible change in the body can
  arouse the much clearer thought of approaching death — and the bodily change may
  genuinely be a sign or a cause of it. Animals are granted the same. This is the
  dark-sensations doctrine of Afd. 1 § 10 cashed out, and it is a good example of
  Treschow explaining away an apparent anomaly without denying the datum.
- **Then the debunking (pp. 134–135)**, which is briskly done: the ancients divided
  dreams into natural and supernatural only because they could not explain why
  some came true. Spinoza is named as deriving divination from the imagination
  (not in Sperrsatz). Prophecies that do come true are put down to deep insight
  into character, constitutions and historical analogy, plus luck, plus a real
  "Talent til at giette" — with Böhme, Drabicius and Nostradamus named. Shamans'
  ecstasies get the same treatment.
- **§ 23 (pp. 137–140) is a clinical taxonomy of madness** built entirely out of
  the theory of dominant representations: fixed ideas are those whose force equals
  or exceeds that of immediate sensation and persists; \emph{Raserie} is when they
  obliterate outer perception; \emph{Forrykthed} is when the sufferer perceives
  normally *and knows it* but blends the two kinds of representation. Then a cross
  classification into \emph{Total} and \emph{partial}, temporary and permanent,
  where "Total" means the dominant representations are knit to all the others "saa
  at man intet kan tænke eller sige uden at hine tillige komme frem." The examples
  are the standard ones of the period (the man of glass, feet of straw, the monk
  who takes himself for a cardinal) plus Tasso, Swift and Le Clerc from
  overexertion, and Spinello driven mad by the devil he had painted. Treatment is
  "deels physiske… deels psychologiske", and the psychological rules are the § 4
  rules for weakening dominant representations, applied "aldrig ligefrem… men ved
  en Omvei".
- ⚑⚑ **§ 18 (p. 126) — the single most useful sentence in this stretch.** Having
  said that imagination can revive or produce nothing except by Association,
  Treschow adds: "Men blandt disse Regler føre nogle til vigtige, skiønne og
  **Gienstandene selv væsentlige** Forbindelser; andre til uvigtige, heslige og
  uvæsentlige. I første Tilfælde faaer \emph{Indbildningskraften} Navn af en
  \emph{høiere}, i det andet \emph{af en lavere}."
  So the associative laws are *not* all on a par: some of them track connections
  belonging to the objects themselves, and that is what makes an imagination a
  higher one. This is as close as Treschow comes to a naturalness constraint —
  and note where he puts it. It is not a distinguished class of *properties* but a
  distinguished subset of *combining rules*, graded by whether they answer to the
  object. For the paper: this is the resource that answers the aptness objection
  without conceding the Lewisian elite. The imagination is then described as "paa
  en vis Maade sammensat af Sandselighed og Fornuft" — reason supplies the
  correctness of outline, sensibility the colours.
- **§ 15 (p. 121) qualifies "creative" hard.** The productive imagination is
  called \emph{skabende}, but this "skal ei betyde, at den frembringer noget, som
  hverken heelt eller stykkeviis tilforn har været til" — only that it (a)
  enlivens, (b) composes and separates parts that were once present, (c) fits them
  into a whole. And at p. 127: "Vi kan intet drømme uden hvad vi tilforn
  stykkeviis have fornemmet; thi Phantasien kan i egentlig Forstand intet skabe."
  A strict recombination theory of imagination.
- **§ 16 (p. 122) uses "enslige" again, and in the plainest sense**: the images of
  enthusiasm "kan snart være enslige og om virkelige Ting… snart almindelige eller
  rene Begreber, f. Ex. Fædreland, Dyd og Ære." Singular versus general
  representations — the 1810 vocabulary doing routine work. (Not in Sperrsatz
  here; verified by zoom.)
- **§ 17 (pp. 122–125): the three perfections of Phantasie** — the life of its
  images, the ease of passing from one image to another, and \emph{Orden}. The
  second is given a nice diagnostic function: fixation on a single vivid image is
  a *deficit* of the first perfection, and "Extensiv Fuldkommenhed forenet med hiin
  intensive afværger den Forrykkelse, som en eneste herskende Forestilling kan
  foraarsage." Order is what makes genius look instinctive — it "frembringer hvad
  der hos andre først er en sildig Frugt af langvarig Eftertanke", and one finds
  in poets "ofte Sæden til de dybsindigst udtænkte Philosophemer."
- **§§ 19–20 (pp. 126–130) on dreams and sleepwalking.** The mechanism is the § 18
  one running unchecked: in sleep the active powers rest, so the passive
  Phantasie "saa meget lettere mechanisk følge sine Love, som dens Gang af ingen
  Selvvirksomhed forstyrres." Hence dreams combine the most unsuitable things
  without our noticing any absurdity — "Vi ere paa engang døde og handle dog som
  levende… herske i Lænker, og eie intet midt i den største Overflødighed."
  Plato is invoked (in Sperrsatz) for the thought that living moderately and free
  of passions would give us philosophical dreams.
- **⚠ Two more cross-references, both defective.** p. 126: "Association §. 6, 3 og
  15" — but Association is *defined* at § 2 (p. 92), so "6" is very likely an
  error for "2". p. 130: "S. 3, Afd. 2, A, b, sammenholdt med I Afd. 10" — the most
  complex reference in the book and not cleanly resolvable; the likely targets are
  this Afdeling's § 2 A b (p. 93) and Afd. 1 § 10 (p. 48). Both left as printed
  with the problem documented at the site. **The reference apparatus of this book
  is unreliable and should be silently corrected only in the translation, with a
  note.**
- **§§ 9–14 (pp. 111–120) finish the treatment of memory**, and the tone shifts:
  much of this is practical pedagogy. Worth knowing what is here rather than
  mining it for the paper.
- ⚑ **§ 9 (p. 111): forgetting is a moral matter, not only a physical one.**
  "\emph{Glemsomhed er en Mangel af Erindringsevne, ei af Hukommelse}" — the
  faculty may be intact — and then: "Vi glemme hvad der ei synes os vigtigt nok.
  Hvo der glemmer noget, som Pligt og Ære burde giøre ham kiert, kan derfor ei
  undskyldes." Hence punishing children *and adults* for forgetting is
  intelligible, since fear then binds the thought. Only where neither fear nor
  hope can bind the thoughts is the cause "blot physisk" — that is
  \emph{Sandsesløshed}.
- **§ 10 (p. 112) distinguishes Sag- from Stedhukommelse**, i.e. memory for
  connections of ground and consequence versus memory for merely contingent
  likeness or contiguity, with *Local-Hukommelse* a species of the latter. "Efter
  Dr. Gall har enhver af disse endog et eget Organ" — reported, not endorsed, and
  Treschow's own point is the dissociation: the man who can retain a chain of
  inferences at one reading may not manage a few vocabulary items, and those with
  a memory like Simonides or Mithridates "lære maaskee aldrig nogen grundig
  Videnskab." A clean statement of what we would call a double dissociation.
- **§§ 11–12 (pp. 113–117): the four components of good memory** — Lethed to
  receive, Troskab to retain, Rummelighed for many and various things, Hurtighed
  to recall and refer each representation to its object — and then the mnemonic
  rules. The interesting one is the **rejection of artificial mnemonics** on
  grounds of associative structure: the ancient art rested on whole/part symbolism
  (the house whose parts stand in a known connection), but "saa megen Kunst
  besværer, som \emph{Qvintilian} med Rette erindrer, snarere end den letter."
  What actually works is connecting the new to what is already fixed, and the
  ordering of the five sub-rules is *itself* the list of association laws from
  § 2: inherence, causal relation, likeness, part/whole, same time and place.
  So the mnemonic advice is derived from the theory rather than tacked on.
- ⚑ **And a warning that belongs in the paper's vicinity** (p. 116): whichever
  order one uses, "bør man vogte sig for, at ei Tildragelsernes væsentlige
  Forbindelse tilsidesettes for den tilfældige af Tid og Sted." Essential
  connection versus accidental connection, as a norm on how to organise
  knowledge. Compare the *egentlige/uegentlige* kinds of *Almindelig Logik* § 30:
  the same distinction, now as advice to the historian choosing between the
  synchronistic and the ethnographic method. Treschow does have a working
  essential/accidental distinction; what he denies is that it individuates a
  privileged class of properties.
- **Two cultural details worth keeping.** p. 115: the Hebrew beth is taught to
  children by its resemblance to a house open at the front. p. 117: Catholic
  rosaries and "de americanske Vildes Wampooner eller Skielsnorer med adskillige
  Farver" are treated as external signs serving the same mnemonic function — wampum
  as writing.
- **§ 14 (p. 120) makes memory the condition of every other faculty**: without it
  all we know "vilde være en indelukt Skat, som vi ikke kunde bruge"; the
  understanding needs it to compare, reason to survey the whole chain of causes,
  productive imagination to have any stock to work on, and even judgement — "som
  man mest pleier at adskille fra Hukommelsen" — cannot do without it. The roll of
  great memories is Aristotle, Leibniz, **Kant**, then the two Scaligers,
  Salmasius, Grotius, and "blandt vore Landsmænd" Hans Gram.
- ⚑ **§§ 4–5 (pp. 100–105): herskende Forestillinger, and this is where Treschow
  gets closest to a *theory of what makes a classification stick*.** A
  representation is *levende* not when it violently stirs the senses — "thi da
  ere de kun \emph{stærke}" (p. 101) — but when it is fit to arouse feelings of a
  different kind from those the impression itself can produce. It becomes
  *herskende* when repeated and deeply impressed, and above all when it is
  "sammensat af mange Dele, men formedelst disse tillige associeret med saa mange
  andre" (p. 102). Then the model: think of the whole system of impressions as
  divided into smaller ones, with the Hovedbegreb "som det herskende" occupying
  the centre and the rest the circumference, "hvert i sin Orden", fastened both
  to it and to each other. He is candid that this "Skyggerids" may give no real
  insight into the matter, only a picture for the imagination "paa hvis
  Berigtigelse man siden maa arbeide."
  **The relevance: a dominant concept earns its centrality by its associative
  connectivity, not by carving nature. That is a rival to naturalness as a
  primitive — closer to a network-centrality story than to Lewis.**
- **p. 103 pushes it further, into constitutive luck.** Thousands read and saw
  what Cæsar and Themistocles did without being equally inflamed; the same
  representation "associerer sig ei ligedan hos alle" — in some minds it drags
  every other into its vortex, in others certain concepts lie "aldeles ensomme og
  uvirksomme." And every innate talent demands matter and nourishment from all
  the rest, so the thinking power "har intet andet at bestille end at bearbeide
  dem efter et saa indskrænket Øiemed."
- **§ 5 (pp. 104–106) fixes the vocabulary of memory.** Persisting after-effects
  (the sun's image, the ringing ear, the echo) are *efterklingende* and must not
  be confused with *Spor*; representations revived from traces are
  \emph{Indbildninger} and the faculty \emph{Indbildningskraft}, which is either
  \emph{reproductiv} (mere renewal) or \emph{productiv} (forming new
  representations by separation and combination, and deepening the traces).
- **§ 6 (pp. 106–108): imagination is *anskuende* only.** Like sensibility it
  confines itself to "Gienstandens Materie og udvortes Form, uden at agte paa dens
  indvortes Væsen eller virkelige Forhold og Forbindelser" — so imagination
  cannot reach the real relations, which is what § 13 of Afd. 1 (p. 53) reserved
  to the *metaphysiske Form* of a Begreb. The division of labour is consistent.
  Sight supplies the most vivid Anskuelser and the most durable traces, which is
  why the faculty is named for it.
- **§ 7 (p. 108) separates recall from recognition**, and the aside is memorable:
  memory in the first sense is "ligesom den Riges Forraadskamre, hvori der findes
  mange Ting, han selv ikke veed af." Hence the ancient poets' belief in
  inspiration — they were not conscious of having had the idea before, nor of
  having just produced it by reflection — and hence, drily, "De fleste
  Skribentere laane Andres Tanker uden selv at vide det, især naar de ikke
  excerpere."
- **⚑ Two more author's cross-references, both resolvable this time.** p. 104 has
  "§.~1" (printed "§. I."), pointing back to § 1 of the same Afdeling, p. 90; and
  **p. 110 has "S.~2, C.~e."** = Stykke 2, division C, item e — the contiguity law
  at p. 96. So the book uses *three* reference formats: Hovedstykke–Afdeling–§
  (roman, arabic, arabic) for distant references, "§. N" within an Afdeling, and
  "S. N, C. e" down to a lettered item. Worth normalising in the translation's
  apparatus rather than reproducing all three.
- **p. 107 cites Croesus and Solon** (both in Sperrsatz, spelled "Croisos" and
  "Solons") for the delayed comprehension of a remark — Croesus grasping Solon's
  words only on the pyre.
- ⚑ **§ 2 (pp. 92–100) is a full theory of the association of ideas**, and the
  organising distinction is the one worth having: "Denne \emph{Forbindelse er}
  deels \emph{logisk} deels \emph{physisk}." The logical connection is "blot
  ideal og frembragt ved vor egen Virksomhed eller Tænkekraft"; the physical is
  "en Følge af vor passive Natur og uafhængig af den fri Villie", and it is the
  latter alone that is properly called \emph{Association} (p. 92). So the
  ideal/real distinction of the 1810 essay is here doing work *inside* the theory
  of mind: our groupings come in two kinds, one of them our own doing and one not.
- **The laws of association (C, pp. 95–97) are read off the table of categories**
  — "de mange Slags saavel naturlige som tilfældige Forhold, der efter
  Kategorierens Tavle kan være mellem Ting eller Forestillinger." Six are given:
  (a) thing/metaphysical subject ↔ its properties; (b) cause → effect, ground →
  consequence, with the asymmetry noted that ascent is easier than descent
  ("Virkningen fører derfor lettere til Aarsagen, den opstigende Røg til at tænke
  paa en Lue"); (c) like and contrasting representations, where opposites are as
  close in thought "som Sirkelens første og sidste Punct"; (d) whole ↔ parts,
  with the observation that it makes no difference whether whole and parts are
  ideal (several things of one kind) or real (body and limbs); (e) contiguity in
  time and place, *in the original order* — hence we can recite a passage
  forwards but not backwards; (f) transfer of one object's properties to another
  by Vexelvirkning.
- **(f) is turned immediately into a debunking explanation** (p. 97): the origin
  of many a foolish and superstitious opinion "f.~Ex.\ om Helgenes Reliqvier,
  Adelskab, Sympathie" — and at p. 100, punishing the malefactor *in effigie* and
  the working of witchcraft are put down to the same associative sympathy. Note
  he lists nobility alongside relics and magic.
- ⚑ **D (p. 97): association is the condition of language and of thought at all.**
  Without it neither could representations of absent things be aroused nor could
  any thinking take place; the traces would be preserved in vain. "Ligesaa lidet
  vilde noget Sprog da være muligt. Thi af Association have Ord saavelsom andre
  Tegn deres Betydning." Then a *typology of intellects by dominant associative
  law*, which is a nice piece of psychology: if likeness is the chief rule, the
  result is wit or acuteness (Vid, Skarpsindighed); if the causal relation, depth
  (Dybsindighed); if mere contiguity in time and place, superficiality. Slow plus
  superficial gives stupidity.
- **E (p. 98) keeps the will in play without breaking the laws.** The laws are
  "physisk nødvendige", yet the will, by way of attention, can steer and alter
  their effects: we cannot stop the stream, but we can dam it so it does not carry
  us off, and we can tighten some bonds and loosen others. Compare the § 15
  attention taxonomy at pp. 55–60 — this is the same compatibilism applied to
  thought's succession.
- **Home and Homerus** are the two proper names in Sperrsatz here (pp. 96, 99).
  "Home" is Henry Home, Lord Kames — cited for the observation that love and
  hatred transfer from parents to children but not as readily in reverse. Worth
  noting for the Scottish-Enlightenment side of Treschow's reading.
- **⚠ A third author's cross-reference, but a corrupt one (p. 91).** The print has
  "I, 2, I3", where the last numeral is plainly 13 set with the antiqua I. The
  first element is therefore ambiguous too, and the reference does not resolve
  cleanly under the Hovedstykke–Afdeling–§ format used at pp. 76 and 82. Most
  likely target is the dark sensations at II, 1, 10 (printed p. 48), or II, 2, 14
  (p. 83). Left as printed, with the problem documented at the site — **worth
  checking against the 1817 second edition if one exists.**
- ⚑ **p. 81 — the Jeget passage, and it is the sharpest anti-materialist argument
  in the book.** Set in Sperrsatz across the page break: "\emph{Jeget maa være
  Foreningspuncten af alle saavel Fornemmelser som Bevægelser. Men dette er
  tillige den Punct, fra hvilken de gaae ud.}" The argument for it is compressed
  and clean: the Sielevæsen one means by the word *Jeg* does possess
  Sensibilitet, but it cannot be the brain or the nerves, because "disse kan
  forandres, men Jeget selv bestaaer: de ere mange, Jeget kun et eneste."
  Changeability and plurality against persistence and unity. Yet we do count the
  brain's changes as *our own* — "Jeget tilegner sig samme" — so they must become
  ours "ved Meddelelse". Note this is *not* in tension with the § 12 parallelism:
  the I is the point of convergence and of origin, not a third thing interacting.
- ⚑ **§ 16 (pp. 86–90) is the epistemology of the senses, and directly useful.**
  Thesis in Sperrsatz: "\emph{Sandseligheden lærer intet om Objecterne: den giør
  ingen Slutninger.}" Sensations in themselves are neither correct nor incorrect,
  since correctness requires agreement or conflict *among several*, on which the
  understanding must judge — therefore "\emph{Sandserne kan derfor ikke
  bedrage.}" He then takes the three ways one might mean that they do, and
  answers each (pp. 87–90). The **first answer (p. 87) matters most for the
  paper**: it is no business of sensibility to teach us what things are in
  themselves, "men hvad Forhold de staae i til os og vore Nødvendigheder" — so
  the subjectivity of sensation is not a defect to be deplored but a design one
  should praise. And the thought-experiment that follows is a real argument, not
  a pious remark: *suppose* the senses gave us only the Grundegenskaber, or only
  what survives purging every subjective appearance — that sight showed only the
  elements' passage from free to bound state, hearing only the wave-motion of
  sound — would this world's stage not lose all the beauty that makes it
  ravishing, and would such dissolved, faint and inert sensations be able to
  produce the feelings that rouse us to useful activity? To demand knowledge of
  things' inner and absolute constitution *by the senses* is "en urimelig
  Fordring", since sensibility would thereby lose its own nature.
  **This is a functional vindication of the manifest image against the scientific
  one, on grounds of the work it does — worth setting directly against the
  Lewisian preference for the elite class.**
- **p. 88's second answer** is a nice methodological aside: if all sensations
  stood in the best harmony, nature's secrets "neppe bleve nogen Gienstand for
  vore Granskninger", because "Hensigten af al Forskning er at kunne forene det
  Stridige, oplyse det Mørke, ordne det Forvirrede." Ordinary events do not
  attract attention; the unusual, which does not agree with other experience,
  forces us to look for grounds. Illusion is epistemically productive.
- **p. 89 cites Pascal and Bonnet** (in Sperrsatz) as examples of otherwise
  rational people who knew their waking visions were only images of the fancy —
  Charles Bonnet, hence the syndrome later named for him.
- **§ 14 (pp. 83–84) is an economy-of-attention argument** with the same shape as
  the p. 57 passage: the stronger sensation darkens the weaker, and since "enhver
  menneskelig Kraft er endelig og har sine bestemte Grændser: hvad den altsaa
  vinder i en Henseende taber den i en anden", intensity is bought with extension.
  Five benefits follow (skill acquisition, the possibility of pleasure at all,
  the overriding of pain, the cure of mental disorder, presence of mind).
- **A second author's cross-reference, "II, I, 9" (p. 82)** — Hovedstykke II,
  Afd. I, § 9, printed p. 47 — again confirming the citation form. Used here to
  send the reader back to the dark/unconscious sensations, which are what make
  voluntary control of one's own body possible without anatomical knowledge of it.
- **The 3die Afdeling opens (p. 90)** on memory, and the opening move is to ask
  what a *Spor* is: taken mentally, a persisting activity or determination of the
  inner force, "færdig at yttre sig"; taken physically, a lasting change in the
  organism, an *Anlæg* to a certain kind of motion in a single part. The § 12
  parallelism applied to traces.
- ⚑ **p. 79 — "Sandselighedens første Lov", and this is the most important
  passage in the book so far for the natural-properties project.** Set in
  Sperrsatz, so Treschow is flagging it as the thesis: "Enhver legemlig Bevægelse
  er forbunden med en aandelig Fornemmelse, som baade i Beskaffenhed og Størrelse
  dertil svarer: enhver Fornemmelse ligeledes med en Bevægelse." And then the
  crucial disclaimer in roman: "**Forholdet mellem begge er altsaa ikke
  caussalt.** En Bevægelse kan blot frembringe en anden Bevægelse, og en
  Fornemmelse ligeledes kun en anden." So: a strict correspondence in both
  quality *and* magnitude, with causation explicitly denied in both directions.
  This is the 1812 book's version of the identity claim that *Om Gud* (1831–33)
  will make metaphysical — and it is a *parallelism*, not an interaction, which
  is exactly what the "same reality under two irreducible modes of access"
  reading of § 2 predicts. Note also the preceding sentence: motion and sensation
  are "det ene Væsens Grundegenskaber", impossible to unite in a single
  Anskuelse yet "dog uadskillelige".
- **p. 76 contains an author's cross-reference, "II, I, 5"** — i.e. Hovedstykke
  II, Afdeling I, § 5 (printed p. 43). This settles the citation format and
  independently confirms that the § numbering restarts within each Afdeling.
  Worth adopting the same form in the translation's editorial notes.
- **§ 10 (pp. 75–77) on the *indvortes Sands*.** Two claims to flag: (i) it
  requires an *organ* just as the outer senses do, because "kun ved dettes
  Reaction kan Sielen tænkes som lidende" and "ingen Kraft indskrænker sig selv"
  — so introspection is not self-transparency but a causal transaction; and (ii)
  "Bevidsthed og indvortes Fornemmelse maa man ikke holde for det samme" (p. 77,
  spaced) — one can undergo changes or have sensations without referring them to
  any object or subject. Consciousness is "en Handling", sensation "en Forandring
  af en blot passiv Evne". This is the unconscious-sensation thesis of § 10
  (p. 48) now given its official statement.
- **The brain is "det fælles Organ for begge Slags Sandser"** (p. 76), and
  Treschow is pointedly cautious about localisation: we find many distinct parts
  in the brain, but their function is not known to us as the outer sense-organs'
  is, so "derfor tale vi kun om *en indvortes Sands*". He then complains that
  attempted assignments of brain parts to particular faculties neither agree with
  sound psychology nor can be established by anything better than "en hidindtil
  meget ufuldstændig Induction" — a direct swipe at Gall, cited approvingly on
  purely anatomical grounds at p. 61.
- **§ 11 (pp. 77–78): the senses correct themselves, not the understanding.**
  Knowing the moon's distance does not make it look bigger — "formaaer den dog ei
  at omstøbe Forestillingen selv" — so when objects *are* presented at their real
  size despite a false retinal image, it must be the senses themselves that
  repair the error by "en nye Virksomhed". His account of the horizon illusion is
  atmospheric (dust and vapour) rather than judgemental, and he explicitly
  rejects the inference-from-intervening-objects explanation.
- **§ 8 (pp. 71–74) on sight** is largely Berkeleyan in its data: distance, size,
  figure, density and transparency are known by sight only *mediately*, by
  comparison with touch, and the evidence offered is the newly-couched blind and
  the behaviour of infants.
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
- ✎ **EDITORIAL NORMALISATION (the one silent change in this edition).** The print
  sets the **first** enumerator of a numbered series with the antiqua capital
  "I)" and then continues "2)", "3)", "4)". Verified at s. 80 and s. 86. This is
  a type-case artefact — the same sort served for I and 1 — not a compositor's or
  author's choice, and in a reading edition it just trips the eye. It is
  therefore **normalised silently to "1)" throughout**, with a comment at each
  site. Everything else that departs from modern usage is carried as printed.
- ⚠ **Print slips in pp. 167–176, all carried with a `% sic`:** s. 167 "Dictum
  **et** omni et nullo" (for *de omni et nullo*); s. 169 "forskitllige"; s. 173
  "en sikker Dømmekraft, **det**," (for "der,"); s. 173/174 the word broken as
  "videnska=/lig", i.e. **"videnskalig" for "videnskabelig"** — the syllable "be"
  is simply missing, and both halves were re-checked at magnification; s. 176
  "udsletede". Also s. 168's page number is set with an inked-in 8 that reads as a
  9 at montage resolution — it *is* 168, verified by zoom.
- ✎ **ë added to the permitted character set** for "Poëm" (s. 173).
- ✎ **A Greek word at s. 179**, ἀστεῖα, printed with the **stigma ligature** for
  στ. As with the Hebrew beth at s. 115, the edition has no Greek font
  (`textalpha` is *not* in the preamble), so the word is given transliterated and
  in italic, with the substitution documented at the site. **Note that this italic
  is not Sperrsatz** — the translation must not treat it as emphasis. To restore
  the Greek, add `\usepackage{textalpha}`. Second open item of this kind.
- ⚠ **A third repeated section number: "13" twice** in the 3die Hovedstykke,
  1ste Afdeling — § 13 (Det Ny) at s. 210 and § 13 (Det Behagelige bliver
  ubehageligt) at s. 212, both verified by zoom. Not renumbered; a `% sic` marks
  the second. Together with the double § 24 and the skipped § 6 and § 3, the
  section numbering of this book is simply unreliable and **the translation
  should carry a general note rather than reproduce every slip**.
- ⚠ **s. 221 carries its page number as "121"** (antikva-I for the 2) — a
  misprinted folio, not a sequence error; noted at the site, the marker keeps the
  true number. Print slips in pp. 219–227, all with a `% sic`: s. 223
  "Legemetnes" (for "Legemernes") and "et alene" (for "ei alene"); s. 224
  "tilfredsstilende" and "en forskiellige Receptivitet"; s. 225 "i selv" (for
  "i sig selv").
- ⚠ **s. 211 prints "Bygnkng"** (for "Bygning"); carried with a `% sic`. Three
  montage-level misreadings were caught and corrected before writing: s. 211
  "sei" is **slet**, s. 218 "Klosterløsterne" is **Klosterløfterne** (long-s
  vs. f), and s. 201 "søb" is **sød** (see the d/b trap above).
- ⚠ **The print numbers two consecutive sections "24"** — § 24 Fanatismus at
  s. 141 and § 24 Adspredelse at s. 146 (verified by zoom). Not renumbered; a
  `% sic` marks the second.
- ⚠ **Print slips in pp. 141–156, all carried with a `% sic`:** s. 143
  "indbiidte" (for "indbildte"); s. 148 "Mangfoidige"; s. 150 "Opmærsomhed";
  s. 154 "Væseutlige" — the third instance of the turned n/u slip after
  "Meunesker" (s. 70) and "iutet" (s. 87), so it is this compositor's signature
  error. Two montage-level misreadings were caught and corrected before writing:
  s. 148 "affondrer" is **afsondrer** (long-s) and s. 156 "abskille" is
  **adskille** (Fraktur d).
- ⚠⚠ **A CORRECTED MISREADING, and a standing trap: Fraktur x vs r.** At montage
  resolution (975 px/page) the Fraktur **x** (𝔵) is easily read as **r** (𝔯). This
  produced a wrong reading of "Afvexlingerne" as "Afverlingerne" at p. 119 in the
  previous batch, **now fixed**; p. 124 "afvexler" was nearly mis-set the same
  way. **Rule going forward: any word that looks like it contains "-erl-" or
  "-ver-" and is not a Danish word must be re-cropped at ≥300 %% before being
  written.** Note also that nb.no's OCR is *not* a reliable arbiter here — it read
  p. 124 correctly ("afvexler") but repeated the error at p. 119
  ("Afverlingerne"). Zooming the image is the only check that settles it.
  A grep sweep for words containing "verl" is now part of the per-batch
  verification; through p. 198 it returns only legitimate forms of "overlade",
  "Overlæg" and "overlegen". **The trap caught a third time at s. 194** — the
  montage read "afverler", the 500 %% crop showed "afvexler". Always re-crop.
- ✎ **A Hebrew letter at p. 115.** The print sets the letter beth itself (U+05D1)
  in "Det hebraiske ב har nogen Lighed med et Huus, der er aabent paa den
  forreste Side." Since the edition is built with pdfLaTeX + Libertinus and has
  no Hebrew font, the glyph is rendered **by its name**, `\emph{beth}`, with the
  substitution documented at the site. Treschow's point depends on the *shape*,
  so if `cjhebrew` is installed the glyph should be restored: add
  `\usepackage{cjhebrew}` to the preamble and set `\cjRL{b}`. **Open item.**
- ⚠ **Print slips in pp. 111–120, all carried with a `% sic`:** p. 112 "negen"
  (for "nogen"); p. 120 "alt hvad vide" (the "vi" dropped); p. 120 "Slut=/ger"
  for "Slutninger". Section numbers 11 and 14 are set with antiqua-I ("II.",
  "I4.") and normalised per the policy above, as are the 1) enumerators on
  pp. 113 and 114.
- ⚠ **Print slips in pp. 101–110, all carried with a `% sic`:** p. 101 the
  dittography "blive blive levende"; p. 104 "pragmagtiske" (for "pragmatiske");
  p. 106 "Forestillngen" (missing i); p. 108 "dert" (for "deri"); p. 109 "af vi
  ei kan erindre" (for "at"). Also **p. 106 skips 3)** — it runs 1), 2), then 4),
  with the intended third item ("Indbildningskraften handler deels
  uvilkaarlig… Deels handler den vilkaarlig…") standing unnumbered. Same species
  of slip as the missing § 6 in Afd. 1. Not renumbered.
- ✎ **The antiqua-I/1 normalisation is now doing real work.** In pp. 101–110 the
  print sets the first enumerator with the capital I **eight** times (pp. 101,
  102, 103, 104 ×2 incl. "§. I.", 106, 109, 110), always followed by arabic 2),
  3). All silently normalised to "1)", per the policy above.
- ⚠ **p. 92 prints "Forbindelse laf Sielens Virksomhed"** (for "af") and **p. 95
  "efter Kategorierens Tavle"** (for "Kategoriernes"); both carried as printed
  with a `% sic`.
- ✎ **Antiqua-within-Fraktur is a script switch, not emphasis.** p. 100 sets
  "in effigie" in antiqua roman because it is a Latin phrase; the print does this
  for foreign words generally. Since the transcription is already in Latin type,
  such words are rendered as ordinary text and **not** given `\emph{}`. Only
  Sperrsatz (and antiqua *italic*) become `\emph{}`.
- ⚠ **p. 87 prints "iutet hørte"** (turned n/u for "intet"), the same slip as
  "Meunesker" at s. 70; carried as printed with a `% sic`.
- ⚠ **p. 72 prints "i det vi domme"** (for "dømme") and **p. 80 sets the first
  enumerator as the roman "I)" and the second as "2)"** — both carried as
  printed with a `% sic`. p. 72 also has "Gebet" (the German *Gebiet*), left as
  printed with a plain comment, not a sic — it is a period-legitimate loan.
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
