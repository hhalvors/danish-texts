# Sibbern — *Bemærkninger og Undersøgelser, fornemmelig betreffende Hegels Philosophie* (1838): transcription resume notes

Hand-off for continuing in a **fresh session** (to avoid re-billing a long thread).
Work in batches of ~10 pages, then compile + give a short report. Don't pause per page.
Method mirrors the Brøchner *Problemet om Tro og Viden* project, which went well.

## Goal
Faithful LaTeX transcription (Danish) of the full book. **NO English translation** —
Jon Stewart's English translation (Museum Tusculanum, *Texts from Golden Age Denmark* vol. 7,
2018) already exists and is linked in the catalog. This project produces the Danish text only.

Files live in `texts/sibbern/bemaerkninger/`:
- `transcription.tex` — the active Danish file (book class).
- Source scan: `~/bibliotek/Sibbern, Frederik/hegels-philosophie.pdf` (169 PDF pages; KB scan,
  free of copyright; 300 ppi color, excellent quality; title = *Bemærkninger og Undersøgelser…*).
  A byte-identical duplicate sits at `111408009315-color.pdf` in the same folder.
- Catalog entry: `~/danish-texts/catalog.yaml`, author id `sibbern`, work id `bemaerkninger`,
  status currently `to-do`. When the transcription is done + hosted, add a `Transcription` link
  (pattern: `https://hhalvors.github.io/danish-texts/texts/sibbern/bemaerkninger/transcription.pdf`)
  and set the section status to `in-progress` / `complete`.

## Page-offset (verified)
**PDF page = printed page + 11.** (printed p.1 = PDF 12; printed p.3 = PDF 14.)
Front matter uses separate Roman numbering: title page = PDF 8, *Fortale* pp. III–IV = PDF 10–11.
Verify via the printed page numbers / running heads in the top strip.

## CURRENT RESUME POINT
**TRANSCRIPTION COMPLETE — front matter + pp. 1–152 + table of contents ("Til Oversigt").**
- Title page, *Fortale* (pp. III–IV) incl. the full *Rettelser* (errata) list — complete.
- Main text pp. 1–152 (PDF 12–163) — complete. Book text ends on p.152 with the "Anm."
  paragraph ("…tjene som et lignende Modificationsmiddel.") between two centred rules.
- Back matter: "Til Oversigt" table of contents (PDF 164–165) transcribed as a manual TOC
  (original page numbers preserved, `\dotfill` leaders, roman-numeral sections hung with
  `\makebox[2.4em]`, sub-letters indented 2.4em). "Principium indiscernibilium" → `\textit`;
  "Tænkningen"/"Følelsen" → `\textbf` (bold in the printed TOC).
- Verified compile: **109 pp., 0 char-warnings, 0 errors** (lmodern substitute in sandbox;
  ~15 overfull hboxes are cosmetic artifacts of the substitute font and Greek→[Gr] stand-in).

### Remaining (for the user)
1. Compile `transcription.pdf` on the real machine (libertinus + libertinust1math + textalpha).
2. In `catalog.yaml`, add the `Transcription` link under work id `bemaerkninger`; set status.
3. Commit/push (user does this; Claude does not).

**Batch 16 (pp.143–152 + TOC) notes:**
- Latin/antiqua → `\textit`: `eo ipso` (p.143, p.146), `in abstracto` (p.143), `unio` (p.144
  ×1, p.145 ×2, p.146 ×1), `natura naturans` (p.145), `coram se` (p.151).
- **Greek** (antiqua, typed directly): `θεὸς δεύτερος` (p.144 once, p.146 twice; grave on
  θεὸς, acute on δεύτερος).
- **Emphasis (letterspacing → `\emph`):** `hel` (p.146, adverbial "den hel christelige Lære" —
  only three glyphs h-e-l, NOT "hele").
- German set in Fraktur → PLAIN, „…“ kept: „der absolute Geist" (p.148 inline, p.149/p.151
  quoted), the Marheineke rubric quotes p.151 („das Reich des Sohnes", „die ewige Idee
  Gottes…das Reich des Sohnes", „die Idee im Element der Gemeinde oder das Reich des
  Geistes."), p.151 „Die Wahrheit der Religion ist die sich offenbarende Gottheit selbst",
  p.149 „metaphysische Definitionen Gottes,"/„die Lehre vom Seyn". "der Geist als Gott",
  "der absolute Geist", "das Element des Vorstellens", "Religion der Schönheit", "für sich"
  all plain. "qvå Tohed/Eenhed/Enkelte" is Fraktur → PLAIN (not Latin qua italic).
- Danish words in „…“ (Anm. p.152): „saa at sige", „ligesom", „egentlig" — plain.
- No footnotes in batch 16.
- Compounds/hyphens: "Idee-Realitet", "Slutnings-Trilogie". Page-break hyphens rejoined:
  er Gud|den hellige Aand, Reli-|gion → "Religion der Schönheit".
- As-printed oddities: "saadannre" (p.152, sic for saadanne), "objectivt" (c, p.150),
  "Bevisthed"/"Bevidsthed" both appear, "verdenlig", "Hypostasis"/"Hypostase".
- Two centred section rules on p.152 → `\begin{center}---\end{center}` (before Anm. and
  after, closing the book).

**Batch 15 (pp.133–142) notes:**
- **NEW DIVISION "V." on p.137** (bottom of page; regular-weight display heading, numeral bold):
  "Om Treenighedslæren hos Hegel." — formatted like divs I–IV.
- Retroactively inserted `\markboth{Hegels Philosophie.}{Livets Fiirheder.}` before the p.132
  paragraph "Men reent skudte tilside ere Livets mangelunde Fiirheder…" (recto head confirmed
  "Livets Fiirheder." on pp.133,135,137).
- **RUNNING HEADS:** recto "Livets Fiirheder." through p.137; recto → "Hegels Treenighedslære."
  set at the div-V heading (head first appears p.139). Verso always "Hegels Philosophie."
- Latin/antiqua → `\textit`: `contemplative` (p.133 twice), `per ascensum` & `per descensum`
  (p.138, antiqua bold), `in abstracto` (p.139, p.140, p.141, p.142).
- **Bold Fraktur (fett) → `\textbf`:** `Dr.\ Rothe` (p.139, both occurrences).
- **Emphasis (letterspacing → `\emph`):** `autopathisk`, `autopathetisk` (p.134 footnote);
  `hele` (p.142), `til` (p.142). (Body words sympathetiskt/egoistiskt/autopathetiskt on p.134
  are NOT letterspaced → plain.)
- **Greek** (antiqua, typed directly): p.134 footnote `αἰσθητικόν og αἰσθητόν, νοητικόν og
  νοητόν`; p.141 `λόγος`.
- German set in Fraktur → PLAIN, „…“ kept: rubric "Specifische Schwere, Cohäsion, Klang,
  Wärme" (p.137, Fraktur display, not letterspaced → plain); „der absolute Geist,“ (p.138);
  „die Vierzahl des Lebens“ (p.139); the Marheineke quotes p.139–141 („Gott an und für sich“,
  „Gott in seiner Ewigkeit…außerhalb der Welt.“, „die Erschaffung der Welt“, „der Proceß der
  Versöhnung…in seiner Gemeinde.“, and the long „Diese drei angegebenen Formen…die absolute
  Einzelnheit.“). "Perseus" (p.136 fn) is Fraktur → PLAIN; "1, 78" plain.
- **FOOTNOTES:** p.134 `*)` (Mærkeligt er det…autopathetisk…) on "for vor egen Skyld" and
  `**)` (See videre…§ 81…Pag. 295--308) on "Selvfølelsen Henhørende"; p.136 `*)` (Prof.
  Heiberg (Perseus, 1, 78)…) on "denne Fiirhed til Grund"; p.139 `*)` (Ved det Ord: „Urtheil“…)
  on "seinem Urtheil"; p.140 `*)` (Jeg tillader mig herved…Philos. Arch. og Repert. andet Hefte
  Pag. 139 ff.) on "Aandens Værk".
- Compounds/hyphens: "Contrast- eller Modsætningsforhold" (suspended compound), "Fiir-Trehed",
  "Sigmanifestations-Proces", "Tre-Enighed". Page-break hyphens rejoined: Annu-laternes →
  "Annulaternes", Til-bagegaaen → "Tilbagegaaen".
- As-printed: "Besaligende", "egoistiskt", "sympathetiskt/sympathiske" distinction, "Cohäsion"
  (rubric, ä) vs "Cohæsion" (body, æ), "Wärme", "Zoologie", "actuelle", "§§ 281--85".

**Batch 14 (pp.123–132) notes:**
- **NEW DIVISION "IV." on p.124** (regular-weight display heading; numeral bold):
  "Om den Hegelske Trilogisering." — formatted like divs I–III
  (`\bigskip \begin{center}{\large\textbf{IV.}} \medskip Om den Hegelske Trilogisering.
  \end{center}\bigskip`).
- Latin/antiqua → `\textit`: `per ascensum` (p.125, p.127), `in abstracto` (p.127).
  Enumerators a) b) c) d) (p.127, antiqua) rendered PLAIN; 1) 2) 3) inside the German block
  quote (p.129) PLAIN.
- Roman numerals in antiqua kept PLAIN: "Werke I, 106--107" (p.123), "Werke IV, 2, 234,
  241--43" (p.124). Section signs kept: § 85, § 247, § 112, § 158, § 198.
- German set in Fraktur → PLAIN, „…“ quotes kept. Big passages: the two Hegel-on-Jacobi
  quotes p.123 („Schon dasjenige…Seite“, „Aber Jacobi nennt…Vernünftigste ist.“); the
  Wesen/Begriff chain p.128 (die Wahrheit des Ersten inline; „die Wahrheit der Idee ist die
  Natur“; „Die Natur hat sich…ergeben.“; „Die Wahrheit des Seyns ist das Wesen;“; „das durch
  die Negativität…Seyn.“; „die Wahrheit der Substanz ist der Begriff“; „Der Begriff ist
  hiemit…ist,“); the long Sonnensystem/Staat block p.129 („Wie das Sonnensystem…erhalten.“);
  „das Maaß“ (p.131); Franz Baaders „Vierzahl des Lebens.“ (p.132). Inline German without
  quotes also plain: "Seyn, Wesen, Begriff", "(durch die Negation der Negation)", "das Wesen".
- **Emphasis (letterspacing → `\emph`):** `hvor`, `hvor` (p.123). (Checked "Widerspruch",
  "Negativitet" p.126 — normal Fraktur, NOT letterspaced → plain.)
- **FOOTNOTES:** p.126 `*)` (Hegel „es ist überall gar nichts…“ + "See Anm.\ til 89 i
  Encyklopædien") on "Udtrykket Widerspruch"; p.127 `*)` ("See det forhen allerede anførte
  Slutningscapitel…") on "en Qvadruplicitet".
- **RUNNING HEADS (verso always "Hegels Philosophie."):** recto → "Den Hegelske
  Trilogisering." at the div-IV heading (pp.125–129); recto → "Af Hegel ei opstillede
  Treheder." placed at the p.130 paragraph "See vi nu hen til den trilogiske Gang…"
  (head first appears p.131).
- As-printed oddities preserved: "Charakteer", "Konstlerie" (p.130), "Specifikke", "Fiirhed/
  Fiirheder", "Legemligt". German "objektiven"/"objektiv" spelled with k as printed (vs
  Danish "objective").

**Batch 13 (pp.113–122) notes:**
- Latin/antiqua → `\textit` (bold or roman antiqua both italicised, per convention):
  `in fidem intellectus` (p.113, twice), `in fidem protocollorum` (p.113), `Cartesii
  meditationes`, `cogito, ergo sum` (p.113; also in its footnote), `imaginor, ergo sum`
  (p.113 footnote), `harmonia originaria`, `harmonia præstabilita` (p.114), `pia mente` (p.115).
  NOTE Sibbern's pun "Thi en fides hører her nu til" — *fides* there is set in FRAKTUR → plain.
- Roman numerals in antiqua kept PLAIN (citation apparatus): "Werke B.\ IV, 1, 234",
  "Werke I, 107" (p.121).
- German set in Fraktur → plain, „…“ quotes kept: „Das Amt der Philosophie ist der leibhafte
  Moses“ (p.119, Hamann/Hjorth); „giv mig Dit Hjerte“ (p.119); the long Heiberg quote in the
  p.117 footnote; the Jacobi/Hegel quotations p.121 („Sie beriefen sich…“, „Ueber die
  Reflexionsphilosophie“, „Kann es eine größere…Gesetze.“). "freies Urtheil" (p.121 footnote)
  plain.
- **Emphasis (letterspacing → `\emph`):** `Videnskabens`, `Livets` (p.118); `evangeliske`,
  `apostolisk` (p.119 footnote).
- **Bold Fraktur (fett → `\textbf`):** the whole lead-in sentence on p.116 "Angaaende
  Philosophiens Suprematie, efter Hegel, eller dens blot Intermediære, efter hvad jeg har
  tydet hen paa, vil jeg endnu kun bemærke Følgende:".
- **FOOTNOTES:** p.113 `*)` (imaginor/cogito) on "cogito, ergo sum"; p.117 `*)` (long Heiberg
  quote) on "er løst op"; p.119 `*)` (evangeliske/apostolisk) on "som Apostelen prædiker";
  p.121 `*)` "freies Urtheil" printer's-error note attached inside the German quote after
  "ihr feines Urtheil".
- **RUNNING HEADS (verso always "Hegels Philosophie."):** recto → "Om Philosophiens
  Suprematie." at the p.116 bold lead-in; recto → "Hegel og Jacobi." at p.120 paragraph
  "Endnu kunde her en Deel være at sige angaaende Jacobi…". (p.120's printed verso head is
  a misprint "Hegels Philosohpie." — not reproduced; markboth keeps the correct spelling.)
- As-printed oddities preserved: "Øiet" (p.121, Fraktur cap Ø, zoom-confirmed — sense: Jacobi
  "har havt Øiet henvendt paa"), "dabey" (p.121 German), "Diet"→corrected reading "Øiet".

**Batch 12 (pp.103–112) notes:**
- Seam: p.102 ended "…Herhen hører, at philo-"; batch opens "philosophisk Erkjendelse og
  Gehalt…" (hyphenated word rejoined).
- Latin/antiqua-italic → `\textit`: `in usu` (p.103), `in abstracto`, `in concreto` (p.106),
  `eo ipso` (p.108). In the p.105–106 footnote: `objectiv`, `correlata`, `subjectiv`, `objectiv`.
- Fraktur → plain: „Præsents.“ (p.103), (Medfølelse) (p.108), (percursivt, discursivt,
  dialektiskt) (p.104). Title abbreviations `Prof.`, `Dr.` (Dr. in antiqua) rendered plain.
- **FOOTNOTES:** p.105–106 `*)` long footnote on objective/subjective sense of *Erkjendelse*
  (spans the page break) → one `\footnote` attached to "…anerkjende sig i sin Ugyldighed". p.111
  `*)` "See ovenfor Pag.\ 29." → `\footnote` on the „…Tro“ quotation.
- **RUNNING HEAD change:** recto flips from "Tre Slags Erkjenden." to
  "Anskuen, Begriben, sympathisk Erkjenden." at p.111 → new
  `\markboth{Hegels Philosophie.}{Anskuen, Begriben, sympathisk Erkjenden.}` placed at the
  paragraph "Men ei blot i Tilegnelsen i enhver Sphære…".
- Preserved as-printed oddities: "sympatethiskt" (p.110, zoom-confirmed), "Tænkningens Maa"
  (p.105).

**HEADING-STYLE CORRECTION (batch 11):** Discovered the division display headings are set in
REGULAR-weight (larger) Fraktur, NOT bold — only the roman numeral (I./II./III.) is bold.
Earlier div. I (p.33) and div. II (p.79) headings had wrapped the heading TEXT in `\textbf`;
this batch removed that so all three heading texts are regular weight (numeral stays
`{\large\textbf{…}}`). Letterspaced words inside a heading → `\emph{}` (as in body).

**Batch 11 (pp.93–102) notes:**
- **NEW DIVISION "III." on p.93** (regular-weight display heading; three words letterspaced →
  `\emph`): "Om og i Anledning af den overvægtige Betydning, Hegel giver \emph{Tænkningen}, og
  det Misforhold, hvori han stiller \emph{Følelsen} og den deri grundede \emph{Erkjenden}."
- **RUNNING HEADS (verso always "Hegels Philosophie."):** recto changes within div. III —
  set `\markboth{Hegels Philosophie.}{Erkjendelse, Følelse og Villie.}` at the div-III heading,
  then `\markboth{Hegels Philosophie.}{Tre Slags Erkjenden.}` at the paragraph "Den første er
  den, i og gjennem hvilken det Sande gjør sig gjeldende…" (start of the three-kinds
  enumeration). NOTE: the print also shows recto "Principium indiscernibilium." on p.93 alone
  (a one-page carryover from the prior topic) and "Erkjendelse, Følelse og Villie." pp.95–99,
  "Tre Slags Erkjenden." p.101+; since my pagination differs I approximate at topic shifts and
  do NOT reproduce the p.93 one-page carryover.
  (Head history: 1–11 Heibergs Perseus.; 12–32 Hegel i Forhold til vor Tid.; 33–57 split
  Hegels Philosophie./Philosophiens Begreb.; 58–70 Philosophien i Forhold til Troen.; 71–78
  Philosophiens Hovedinddeling hos Hegel.; 79–88 split /Contradictionsprincipet m. M.; 89–92
  /Om den formale Logik.; 93 /Principium indiscernibilium. [carryover]; 93/95–99 /Erkjendelse,
  Følelse og Villie.; 101→ /Tre Slags Erkjenden.)
- **CORRECTION to batch 10 seam:** the p.92 sentence ends with a PERIOD ("…hvor det slet ikke
  hører hen."), not a comma — section II closes there; fixed.
- No Greek this batch. No Latin `\textit` this batch (the foreign matter is German/citation).
- German plain (Fraktur): p.94 (in der „Empfindung“); p.98 (daß wir in Gott zurück wallen
  d. h. wollen mögen, siger Franz Baader etsteds) — no „…“ quotes, parenthetical; p.102
  Innewerden (in the ** footnote).
- Footnotes: p.100 two (See min Psychol. … / See min Afhandl. …); p.102 two (Cfr. mit Skrivt:
  „om Erkjendelse og Granskning“ … / the Innewerden note). All rendered plain (citation
  apparatus, not Latin prose), matching the p.88 footnote precedent.
- Bible ref p.100: (1 Cor. 13, 12), plain. Self-citations „om Erkjendelse og Granskning“
  (Sibbern's own work) in „…“ quotes, plain.
- Names plain Fraktur: Kant, Franz Baader.
- Dittography tally unchanged (p.6, p.49, p.57, p.58; + p.78 „Erkennnen“ misprint).

**Batch 10 (pp.83–92) notes:**
- **RUNNING-HEAD CHANGE at p.89 (recto):** the recto Overskrift switches from
  "Contradictionsprincipet m. M." to "Om den formale Logik." (verso stays "Hegels
  Philosophie."). Set `\markboth{Hegels Philosophie.}{Om den formale Logik.}` at the
  paragraph "Det være mig tilladt her, hvor vi have havt Gjenstande, som høre hen til den
  saakaldte formale Logik…" (begins on p.88 verso; recto head takes effect p.89). No display
  heading — a topical running-head change within div. II.
  (Head history: 1–11 Heibergs Perseus.; 12–32 Hegel i Forhold til vor Tid.; 33–57 split
  Hegels Philosophie./Philosophiens Begreb.; 58–70 Philosophien i Forhold til Troen.; 71–78
  Philosophiens Hovedinddeling hos Hegel.; 79–88 split Hegels Philosophie./Contradictionsprincipet
  m. M.; 89→ split Hegels Philosophie./Om den formale Logik.)
- Greek (verified by zoom): p.84 κατὰ τὸ ἑαυτοῦ (rough breathing clear; ultima circumflex
  worn/absent in scan — set standard ἑαυτοῦ since the book's Greek is otherwise fully
  accented); p.87 κατά τι, πρός τι, ἔν τινι χρόνῳ.
- Latin `\textit{}` (all antiqua, several set BOLD upright — still `\textit` per convention):
  p.83 principium exclusi medii inter duo contradictoria; p.84 diversus respectus tollit omnem
  contradictionem; p.86–87 aut-aut (×5, incl. bare "aut"), contradictoria; p.88 fallacia falsi
  medii, fallacia medii insufficientis; p.90 qvæstio / quæstio facti / quæstio juris; p.91–92
  principium indiscernibilium (×2), eo ipso.
- French `\textit{}`: p.92 suivant son point de vue, point de vue (antiqua bold → \textit).
- Formula p.84: the identity principle printed with the equation sign (Sibbern explicitly
  discusses "Æqvationstegnet") — rendered "A = A" as plain text with a `%` note (printed sign
  slightly ambiguous, looks like = plus a short dash).
- German plain (Fraktur, „…“): p.83 „vom Wesen“, „Die Form des Satzes … was seine Form
  fodert.“, „ein wahres Denkgesetz“; p.84 „Namentlich wird es durch die folgenden Denkgesetze
  … zu Gesetzen machen.“, Gegensätze; p.85–86 Widersprüche/„Widerspruch“ (several), „Die Welt
  ist voller Widerspruch“, „Und sollte sichs nicht widersprechen?“; p.88 „Alles ist ein
  Schluß“; p.89 kategorischer Schluß, „Schluß des Daseyns.“; p.91 „Unterschied“, „Identität“.
- Footnotes: p.88 "See Logik III Pag. 142--43 i første Udg., tredie Cap. A. a." (plain — the
  antiqua bits are citation numerals/abbrevs, not Latin prose); p.92 long note on Leibnitz's
  Monader as Sjæle/Entelechier.
- Names plain Fraktur: Mynster(s), Leibnitz/Leibnitziske, Goethe, Aristoteles, Treschow.
- No line-break dittographies this batch (tally unchanged: p.6, p.49, p.57, p.58; plus the
  p.78 „Erkennnen“ spelling misprint).

**Batch 9 (pp.73–82) notes:**
- **INSTALLMENT BREAK on p.78:** the article's first Maanedsskrift installment ends with a
  right-aligned "(Fortsættes.)" + signature "F.\ C. Sibbern." and a short centered rule —
  reproduced faithfully (`\begin{flushright}…\end{flushright}` + `\rule`).
- **NEW DIVISION "II." on p.79** (display heading, bold, same format as div. "I." p.33):
  "Om den Maade, hvorpaa Contradictionsprincipet behandles i den Hegelske Skole, med Mere,
  som henhører til de logiske Grundbetragtninger."
- **RUNNING-HEAD CHANGE at p.79 (div. II):** back to split heads
  `\markboth{Hegels Philosophie.}{Contradictionsprincipet m.\ M.}` (verso "Hegels Philosophie.",
  recto "Contradictionsprincipet m.\ M."). Set right at the div-II opening.
  (Head history: 1–11 Heibergs Perseus.; 12–32 Hegel i Forhold til vor Tid.; 33–57 split
  Hegels Philosophie./Philosophiens Begreb.; 58–70 Philosophien i Forhold til Troen.; 71–78
  Philosophiens Hovedinddeling hos Hegel.; 79→ split Hegels Philosophie./Contradictionsprincipet m. M.)
- Greek (all verified by zoom): p.74 ῥοή (Heraklitiske); p.80 τὸ αὐτό; p.81 κατὰ τὸ αὐτό,
  πρὸς τὸ αὐτό, ἐν τῷ αὐτῷ χρόνῳ.
- Bold `\textbf{}`: p.75 the Rothe quote „Gud er alle Muligheders Virkelighed“ (verified;
  "Dr. Rothe" and "carpere" are NOT bold — carpere is plain Fraktur, not \textit).
- Latin `\textit{}`: p.79 footnote *Aristotelis Metaph. IV*, 3–4, og *XI*, 5 (`\footnote`);
  p.80 *eo ipso*.
- German plain (Fraktur, „…“): „Thätigkeit.“, „Erster Entwurf eines Systems der
  Naturphilosophie“ p.73–74; das Erkennen, „das Erkennen,“, der objective Geist,
  das Recht/die Moralität/die Sittlichkeit p.78; „um seiner Unbestimmtheit willen“,
  „das Werden“, Seyn/Nichts/ein Seyn/ein Nichts p.80–81; ein Uebergehen, in seinem
  Andersseyn p.82.
- **DITTOGRAPHY/misprint:** p.78 „Erkennnen“ printed with THREE n's — reproduced as printed
  with `% [sic: Erkennnen, tre n]`. (Line-break dittography tally unchanged: p.6, p.49, p.57,
  p.58; this is a spelling misprint, tallied separately.)

**NEW CONVENTION (batch 8): bold-Fraktur emphasis → `\textbf{}`.** The book uses TWO emphasis
devices: letterspacing (Sperrung) → `\emph{}` (as before), AND heavier/bold Fraktur (fett) →
`\textbf{}` (new). Distinguish by eye at zoom: bold = thicker strokes, same letter-spacing;
letterspaced = normal strokes, gaps between letters. First bold instances: p.63
`\textbf{christelig Philosophie}`, `\textbf{christelige Tro}`, `\textbf{christelige Leven}`;
p.65 `\textbf{kan}` ("at det kan opvise den"). (On p.65 "Randsagelsesaanden" is NOT bold —
verified by zoom.)

**Batch 8 (pp.63–72) notes:**
- **RUNNING-HEAD CHANGE at p.71:** switches to symmetric
  `\markboth{Philosophiens Hovedinddeling hos Hegel.}{Philosophiens Hovedinddeling hos Hegel.}`
  Set at the paragraph "At gaae ind i Detaillen af Hegels Philosophie…" (after the section-break
  rule on p.70). No numbered display heading. (Head history: 1–11 Heibergs Perseus.; 12–32 Hegel
  i Forhold til vor Tid.; 33–57 split Hegels Philosophie./Philosophiens Begreb.; 58–70
  Philosophien i Forhold til Troen.; 71→ Philosophiens Hovedinddeling hos Hegel.)
- Latin `\textit{}`: p.66 a priori, prius; p.67 potentià (×2), mutatis mutandis, actu.
- German plain (Fraktur, „…“): (in seinem Andersseyn) p.71; „die Lehre vom Seyn“, „vom Wesen“,
  „von dem Begriff“, Mechanismus/Chemismus/Teleologie p.72.
- Footnotes: p.63 (ref to Sibbern's own Bog om Erkjendelse), p.69–70 (long note on the word
  "speculativ", spans two pages — reproduced as one \footnote).
- Section-break rule `\begin{center}---\end{center}` on p.70.
- No line-break dittographies this batch (tally still: p.6, p.49, p.57, p.58).

**Batch 7 (pp.53–62) notes:**
- **RUNNING-HEAD CHANGE at p.58:** the Overskrift switches to symmetric
  `\markboth{Philosophien i Forhold til Troen.}{Philosophien i Forhold til Troen.}`
  (both verso & recto now read "Philosophien i Forhold til Troen."). I set the `\markboth`
  at the paragraph "Jeg er her paa et Punct…" (the topic shift to faith). No numbered display
  heading accompanies it — the book just re-titles the running head. Division "I." (from p.33)
  had a body heading; this transition does NOT.
- Greek: p.60 κάθαρσις (acute on first α; verified 400 dpi).
- Latin `\textit{}`: p.54 Hegelianismo adscriptus; p.59 in specie; p.60 intussuscipere;
  p.61 footnote — a long Spinoza citation (Poenitentia virtus non est…; Humilitas…; humilitas;
  acqviescentia in se ipso; summum, qvod sperare possumus; tristitia, orta ex eo…contemplatur;
  Qvi recte novit…miserebitur). NB the print sets the long Latin quotes in antiqua **roman**
  and only "in se ipso"/"tristitia" in italic; per the project's Latin→\textit convention I
  wrapped ALL the Latin runs in \textit (same as earlier upright-bold Latin like p.33/40),
  not reproducing the print's internal roman/italic split.
- German plain (Fraktur): Göthe distich „Dieser ist mir der Freund…“ (quote block, pentameter
  line indented with \quad); das Wißthum / das Wissen, als Wissenschaft / Wissenschaftslehre /
  „die Lehre von den Thatsachen des Bewußtseyns“ (p.58); „Phänomenologie des Geistes“,
  „bittweise“ (p.57); eine gegliederte Anschauung, (Gliederung) (p.56). Danish quotes „…“
  for the Poul Møller and Heiberg citations. ß kept (Wißthum, Bewußtseyns).
- Footnotes: p.54 (Gabrielis ref), p.55 (Poul Møller obituary note), p.61 (Spinoza Latin).
- Section-break rule `\begin{center}---\end{center}` on p.53.
- **TWO more line-break dittographies kept as printed with `% [sic]`:** p.57 "af / af"
  ("Uddrag af af denne Phænomenologie"); p.58 "han / han" ("das Wißthum, som han han kaldte
  den"). (Running tally of this dittography species: p.6 "et et", p.49 "for for", p.57 "af af",
  p.58 "han han".)

**Batch 6 (pp.43–52) notes:**
- Greek: p.45 ἀειδές (smooth breathing + acute; verified by 400 dpi zoom).
- Latin `\textit{}`: p.43 natura naturans; p.45 periculum vitæ; p.51 generatio ex ovo,
  generatio spontanea.
- German plain (Fraktur, „…“ quotes): „Ursprüngliche“ / der absolute Geist / der Geist als Gott
  (p.43); „ob man mit dem Anfange anfangen müsse.“ (p.44); "in ihrer Sichgestaltung" (p.46);
  the 2-line Mephistopheles verse „Möchte solch einen Menschen kennen, / Würde ihn Herrn
  Mikrokosmos nennen.“ (p.51, set in a `quote` block); aufgehobene (p.51).
- Footnotes: p.50 (long Heiberg Pag.34 quote), p.52 (Sibbern on his citation practice).
- Section-break rule `\begin{center}---\end{center}` on p.44.
- **`% [sic]` flag on p.49:** the print doubles "for" across a line break
  ("…fra Grunden af, for / for at de nu kunne faae…") — same dittography species as p.6
  "et et andet". Kept as printed.
- No letterspaced emphasis in this batch (checked Suprarationalt/Extrarationalt on p.48 by
  zoom — NOT spaced). Running heads unchanged: verso "Hegels Philosophie.",
  recto "Philosophiens Begreb." (division I still running).

**Preamble header change (done at batch 5):** verso/recto running heads now DIFFER, so the header
block uses `\fancyhead[CE]{\textit{\leftmark}}` + `\fancyhead[CO]{\textit{\rightmark}}` (was a single
`[CE,CO]{\leftmark}`). Set both sides per section via `\markboth{VERSO}{RECTO}`.

**Greek so far** (all verified with zoom crops): p.15 πίστις; p.26 βασιλεία τῶν οὐρανῶν;
p.23 uses "α)" as an enumerator inside a German quote. (No Greek in pp.33–42.)

**Latin/foreign in `\textit{}` so far:** p.9 sibi defuit; p.13 qvod petis hic est; p.15 credere,
fides, natura naturans; p.23 incuria (in fn); p.28 partie honteuse / partie modeste; p.29 the
Anselm/Schleiermacher motto "qvi non crediderit…non intelliget"; p.30 affreuse; p.31 aut-aut;
p.33 totum est parte sua prius; p.36 subreptitie; p.37 ex ovo, e nihilo, generatio spontanea;
p.38 a constitutore, ovum; p.39 rationes essendi / constituendi, ovum; p.40 totum est parte sua
prius, perfectum est index sui et imperfecti, verum est index sui et falsi, ovum,
qvod non curare deberet talis vir.

**Emph (letterspaced) added in batch 5:** p.36 `\emph{andetstedsfra}`; p.42 `\emph{philosophisk}`.
(Capitalized German terms Moment/Aufgehobenseyn/Væren/Intet/Eet/Tvende on p.35 are NOT
letterspaced → left plain, per the conservative rule.)

**Footnotes placed:** p.3 (×2, Göthe), p.11, p.16, p.18, p.22, p.23 (×2), p.24, p.29, p.30, p.32,
p.37, p.38, p.40.

**Running-head (Overskrift) log:** pp. 1–11 = "Heibergs Perseus."; changed at p.12 to
"Hegel i Forhold til vor Tid." (through p.32); **at p.33 the book starts division I and the heads
split: verso = "Hegels Philosophie.", recto = "Philosophiens Begreb."** (current at p.42, set via
`\markboth{Hegels Philosophie.}{Philosophiens Begreb.}`). Keep watching the top strip each page and
reset `\markboth` whenever the recto Overskrift changes; also watch for the Overskrift changes
flagged in the *Rettelser* (p.91 → drop "Om den formale Logik"; p.95 → "Tænkningens Suprematie";
p.99 → "Tre Slags Erkjenden"; p.111 likewise).

**p.33 division heading** rendered centered: `\textbf{I.}` + bold title "Angaaende det Hegelske
Begreb om Philosophie med Hensyn til dens Udgangspunct og dens hele Grundlag." Watch for the next
numbered division ("II." etc.) further on and render it the same way.

**NEXT: p. 103 onward (PDF 114 →).** `grep -n "text to be added" transcription.tex` → 1 marker.

## Convention decisions locked in
- **German is set in Fraktur in this book** (both in the body and in footnotes), same script as
  the Danish → transcribe German **plain** (keep „…“ quotes), do NOT wrap it in `\textit{}`.
  Only genuinely Latin/Greek/French words that the print sets in *antiqua italic* get `\textit{}`.
  (Caught and fixed an early slip: the p.22 German footnote had been wrapped in `\textit`.)
- Letterspaced emphasis **inside the long quoted German Hegel passages** is left unmarked
  (e.g. the "a priori" on p.26); Danish authorial letterspacing is always marked with `\emph{}`.
- p.6 prints "gjennem et et andet Materiale" (line-break dittography); kept as printed with a
  `% [sic …]` flag. Transcribe faithfully; do NOT apply the *Rettelser* corrections to the body
  (they live in the front matter). Errata targets seen so far and left as printed: p.2
  Skikkelsen/bundne; p.20 "294--97"; p.21 "Mere"; p.32 "Sufficence".

## OCR pipeline (rebuild each session; models don't persist; /tmp dirs may be owned by other users)
```bash
mkdir -p /tmp/sibtess && cd /tmp/sibtess     # use a FRESH dir you own if perms fail
wget -q https://github.com/tesseract-ocr/tessdata_best/raw/main/dan.traineddata -O dan.traineddata
wget -q https://github.com/tesseract-ocr/tessdata_best/raw/main/script/Fraktur.traineddata -O Fraktur.traineddata
# per page P (PDF page number = printed + 11):
export TESSDATA_PREFIX=/tmp/sibtess
SRC="/sessions/<id>/mnt/bibliotek/Sibbern, Frederik/hegels-philosophie.pdf"
pdftoppm -f P -l P -r 300 -png "$SRC" /tmp/ro >/dev/null 2>&1   # writes /tmp/ro-0PP.png (3-digit pad)
tesseract /tmp/ro-0PP.png stdout -l Fraktur --psm 6 2>/dev/null \
  | sed -e 's/ſ/s/g' -e 's/œ/æ/g' | tr -s ' '
```
The `Fraktur` model is ~98% at word level but SLOW (~20s/page; sandbox times out at 45s), so
OCR ONE page per bash call. **Hybrid method (chosen):** read words from OCR, then also render
the page image (render to the outputs dir and Read it) to (a) catch letterspaced emphasis →
`\emph{}` [OCR can't see letterspacing], (b) fix OCR's plausible errors (k↔f e.g. "fan"→kan,
"iffe"→ikke; dropped ø e.g. "gjor"→gjør), (c) place footnotes. Render for viewing:
`pdftoppm -f P -l P -r 200 -png "$SRC" /sessions/<id>/mnt/outputs/pg` then Read the host path.

## Conventions (preserve 1838 orthography exactly)
- Spellings as printed: Philosophie, Tidsskrivt, directe, Conseqvents, Skjæbne, gjøre, Øieblik,
  særskilt, deels, capitalized nouns, ø/aa, double vowels (Deel, Skyld, heelt). Do NOT modernize.
- Transcribe the text **as printed**; the *Rettelser* corrections are reproduced separately in the
  front matter and are NOT applied to the body (e.g. p.2 keeps "Skikkelsen … bundne", though the
  errata would read "Skikkelse … lænkede").
- Quotes: Danish „…“ (low-high) as printed; guillemets »…« / «…» where the book uses them.
- Em-dashes: `---`. Section-break rules the book prints → `\begin{center}---\end{center}`.
- Letterspaced emphasis → `\emph{...}` (the most common thing OCR misses).
- Latin/foreign in italics: `\textit{principium indiscernibilium}`, etc. Roman-numeral cross-refs
  the book italicises (e.g. *XI*, *XIII* in "Pag. XI") → `\textit{XI}`.
- Footnotes → `\footnote{...}` inline at the anchor. Check each page's bottom strip.
- The old Danish "id est" mark ɔ: → type the literal `ɔ` (preamble maps it via `\reflectbox{c}`,
  needs `graphicx`, already added).
- Greek (if any) typed directly; `textalpha` is in the preamble.
- Running heads reproduce the printed **Overskrivter** via `\markboth`; page numbers on outer edge.

## Verification compile (sandbox lacks libertinus; substitute, keep ɔ to catch mapping bugs)
```bash
D=/tmp/sibverify_$$; mkdir -p $D && cd $D
SRC="/sessions/<id>/mnt/danish-texts/texts/sibbern/bemaerkninger/transcription.tex"
sed -e 's/\\usepackage{libertinus}/\\usepackage{lmodern}/' -e '/libertinust1math/d' \
    -e '/textalpha/d' -e 's/\\usepackage\[danish\]{babel}/\\usepackage{babel}/' "$SRC" > t.tex
python3 -c "import re;s=open('t.tex',encoding='utf-8').read();open('t.tex','w',encoding='utf-8').write(re.sub(r'[Ͱ-Ͽἀ-῿]+','[Gr]',s))"
pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1; pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1
grep -o 'Output written.*' l.txt; grep -ic 'not set up\|missing.*character' l.txt
```
Expect 0 char-warnings. On the user's real machine libertinus + textalpha handle the real glyphs;
do NOT add the Greek/ɔ substitutions to the actual file.

## Final steps (when the whole book is transcribed)
Compile `transcription.pdf` on the user's machine (libertinus + libertinust1math), then in
`catalog.yaml` add the `Transcription` link under work id `bemaerkninger` and set section status.
(User commits/pushes; do not.)
