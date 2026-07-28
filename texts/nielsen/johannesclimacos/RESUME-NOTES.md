# Rasmus Nielsen — *Mag. S. Kierkegaards „Johannes Climacus“ og Dr. H. Martensens „Christelige Dogmatik“. En undersøgende Anmeldelse* (1849): transcription resume notes

This is a **TRANSCRIPTION** job (Fraktur Danish, scan → LaTeX), Phase 1. English
translation is Phase 2 (separate job, per `../../../TRANSLATION-PLAYBOOK.md`).
Work in ~10-page batches; after each, compile, report, hand back.
**Hans commits and pushes — the assistant never does.**

Book: *Mag. S. Kierkegaards „Johannes Climacus“ og Dr. H. Martensens
„Christelige Dogmatik.“ En undersøgende Anmeldelse.* Af R. Nielsen, Professor i
Philosophien. Kjøbenhavn: Forlagt af Universitetsboghandler C. A. Reitzel;
Trykt hos Kgl. Hofbogtrykker Bianco Luno, 1849.

## Why this text
Published **15 October 1849**, a few months after Martensen's *Christelige
Dogmatik*. It is Nielsen's public response to the *Concluding Unscientific
Postscript* (1846) — he reads Climacus *against* Martensen to argue that
Martensen's dogmatics fails "i dens Princip som i dens Problem." This is the
pamphlet that opened the Danish faith/knowledge controversy and the one that
soured Kierkegaard on Nielsen.

## Scan & offset (VERIFIED)
- Scan: `~/bibliotek/Nielsen, Rasmus/Kierkegaards_Johannes_Climacus_og.pdf`
  (146 PDF pp., Google Books, Harvard/Widener copy, clean high-contrast).
- **OFFSET: PDF = printed + 8.** printed p.5 = PDF 13; p.10 = PDF 18;
  p.132 = PDF 140.
- Half-title (cover title, ornamental border) = PDF 7; full title page = PDF 9.
- Text opens on **printed p.3 = PDF 11** (folio suppressed on the opening leaf;
  signature mark "1*" at the foot).
- ⚠ **FOLIO MISPRINT: printed p.58 (PDF 66) is numbered "53" in the original.**
  Zoom-verified at 400 dpi; the text runs on continuously from p.57, and PDF 67
  is correctly numbered 59. An isolated compositor's slip, **not** an offset
  change — PDF = printed + 8 holds throughout. Flagged inline in the
  page-break comment. Do not "correct" the offset on account of this leaf.
- **EXTENT: printed pp. 3–132 (PDF 11–140).** Ends with the dateline
  "Kjøbenhavn, d. 18. Sept. 1849." + signature "R. Nielsen.", then a centred
  ornament rule. Back matter: colophon leaf "Trykt hos Kgl. Hofbogtrykker
  Bianco Luno." (PDF 142) inside the same ornamental border as the half-title.

## Structure — READ THIS
Unlike the 1857/1864 treatises, this is a **continuous review-essay**: no
numbered §§, no chapters, no Indhold. It has **two levels** of articulation:

1. **Display questions in larger bold Fraktur** — the top-level divisions.
   Render `\begin{center}{\large\bfseries …\par}\end{center}`.
   - p.9: **Har ikke „Johannes Climacus“ dialektisk skjærpet det christelige Problem?**
   - p.48: **Har ikke „den christelige Dogmatik“ udialektisk omgaaet det christelige Problem?**

The Martensen half **also** has lettered sub-heads, beginning at p.57 — so the
a)/b)/c)/d) series restarts rather than continuing:
   - p.57 — *a) „Den christelige Dogmatik“ famler efter Problemet, men finder
     det ikke.*
   - p.67 — *b) „Den christelige Dogmatik“ vil tilegne sig Speculationen, men
     uden at fatte Speculationens Problem.*
   - p.90 — *c) „Den christelige Dogmatik“ vil tilegne sig Troen, men uden at
     fastholde Troens Problem.*
   - p.125 — *d) „Den christelige Dogmatik“ er principløs.*

  Note the deliberate parallel in b) and c): the *Dogmatik* wants to
  appropriate **speculation** without grasping speculation's problem, and to
  appropriate **faith** without holding fast faith's problem. Keep the
  symmetry in translation.

**The book is in two halves**, and the hinge is at **p. 42**: a centred rule
closes the Climacus report, then Nielsen turns to Martensen (*„den christelige
Dogmatik“*, letterspaced). The two display questions are deliberate mirror
images — *dialektisk skjærpet* vs. *udialektisk omgaaet* — so keep the parallel
audible in translation. The a)/b)/c)/d) sub-heads belong to the Climacus half
only; nothing comparable has appeared in the Martensen half through p. 54.
2. **Lettered sub-heads in letterspaced Fraktur**, centred, running a)/b)/c)/d)…
   Render `\begin{center}\emph{…}\end{center}`.
   - p.11 — *a) Hvorledes Problemet fremkommer.*
   - p.21 — *b) Sandheden, Inderligheden er Subjectiviteten.*
   - p.27 — *c) For den existerende Subjectivitet er den høieste Sandhed Paradoxet.*
   - p.34 — *d) I Modsætning til Speculationens objective Viden er Christendommen
     at betegne som en Existens-Meddelelse.*

Inside a) there is a further Greek-letter split, run-in rather than centred:
**α) den historiske** (p.12) / **β) Den speculative Vei.** (p.17). Typed as
`$\alpha$)` / `$\beta$)` so no `textalpha` dependency is added for these.

Log each new heading here as it appears so the translation skeleton can mirror
the transcription 1:1.

## Quote-balance ledger — READ THIS BEFORE PANICKING
Whole-file „/“ counts are **deliberately unbalanced**. The print opens
quotations it never closes (Nielsen nests Postscript citations inside his own
quoted matter), and once closes one it never opened.

| where | what the print does | effect |
|---|---|---|
| pp. 12, 14, 18 | opening „ with no closing | **+3** |
| p. 46 footnote | closing “ with no opening — the Martensen preface quote resumes after „…til sit Princip.“ without reopening, then closes again at „…Udviklingsformer.“ | **−1** |
| pp. 59–60 | „Den religiøse Anskuelse“ closes at the *title phrase*, then the citation runs on **unopened** through the dash and closes on p.60 at „…Phantasiens Medium.“ | **−1** |
| p. 71 | the Martensen citation closes at „…renses ved Philosophie“, resumes after „ikke betænkende, at" **unopened**, and closes again at „…Naadens Rige“ | **−1** |
| p. 92 | „Ved sit *credo, ut intelligam*“ closes at the tag phrase, the citation resumes after „— hedder det (S. 73 § 33) —" **unopened**, and closes at „…dialectiske Drift.“ | **−1** |
| pp. 103, 105 | same construction twice — „Den objective Canon for al Christendom“ — hedder det (§ 22) — … and „Den udvortes Canon“ (§ 24) … — each closing at the tag phrase, then running on unopened to a later closing mark | **−2** |
| p. 123 fn. | the long Climacus footnote is never formally opened but **is** closed at „…en stille Opløftelse.“ before the attribution „Johannes Climacus." | **−1** |

**Baseline by stretch: +3 through p. 45; +2 from p. 46; +1 from p. 60; 0 from
p. 71; −1 from p. 92; −3 from p. 105; −4 from p. 123.**
**FINAL whole-file ledger: −4** — six documented print anomalies, every one
verified against the page image. This is the expected end state, *not* an
error.

The pattern is now **pervasive**, not exceptional: through the Martensen half
Nielsen quotes the *Dogmatik* section by section as `„Short phrase“ — hedder
det (§ N) — <citation continues>…“`, and the reopening mark after the dash is
supplied only sometimes. Expect the baseline to keep drifting negative. Trace
each batch, spot-check the dash against the image, and record — do not
normalise, and do not treat a falling baseline as evidence of a dropped quote
without checking.

⚠ **Recurring pattern, expect more of it.** Nielsen habitually writes
`„Short Title“ — hedder det … — ` and then lets the quotation continue with no
reopening mark. Same shape at p.54 („Saavidt jeg nemlig“ — vedbliver Dr. M. —
„formaaer…", which *does* reopen) and p.61 („Philosophien søger…"). So the
mark is inconsistent in the print itself: sometimes reopened, sometimes not.
**Always check the image at the dash** rather than normalising.
Across a page seam the running total oscillates by ±1 (a quote opened on one
page closing on the next) and must **return to the baseline** at each batch
end. If a batch ends off-baseline, trace it page by page with the script below
*before* assuming it is genuine — twice now the ledger has caught something,
and both times it was the print, not the transcription. Verify against the
page image either way.

```bash
python3 - <<'PY'
import re
s=open('transcription.tex',encoding='utf-8').read()
parts=re.split(r'% ---- (printed p\.\d+|footnote continues[^-]*)',s); run=0
for i in range(1,len(parts),2):
    o,c=parts[i+1].count('„'),parts[i+1].count('“'); run+=o-c
    if o-c: print(f"{parts[i]:34s} delta={o-c:+d} running={run:+d}")
PY
```

## Typography — READ THIS
- **Type is FRAKTUR** (Danish body); Latin phrases in antiqua → `\textit{}`
  (so far: *in optima forma* p.7 fn., *eo ipso* p.10).
- **Emphasis = letterspacing (Sperrsatz)** → `\emph{}`. OCR cannot see it;
  image-verify every page. First instance: the governing question on p.4,
  "Vil Christendommens Sandhed efter sin Natur være Gjenstand for objectiv
  Viden?" (whole sentence letterspaced).
- **⚠ READER'S MARKS — do not mistake for emphasis.** The Harvard copy has a
  previous reader's **pencil underlining/highlighting** (renders as grey bands)
  and marginal strokes in the outer margin. Seen on pp.9, 10 and elsewhere.
  These are **not** Sperrsatz. Verify by letter-spacing of the glyphs, not by
  the grey band.
- **Greek** — first occurs at **pp.63–64**: the Archimedean tag, zoom-verified
  at 500 dpi as **ποῦ στῶ** (p.63) and the Doric **πᾷ στῶ** (p.63 once, p.64
  twice). Typed as raw polytonic Unicode; needs `textalpha`, already in the
  preamble. The sandbox cannot render Greek — the verify recipe now strips the
  Greek range to `[Gr]` **for the check only** (see §Verify below); confirm the
  real glyphs on a local libertinus compile.
- **Quotes:** Danish „…“ (low-high), U+201E / U+201C.
- **Footnotes** marked `*)` → `\footnote{}` at the anchor word. Note the p.7
  footnote **runs over onto p.8**; kept as one `\footnote{}` with an inline
  page-break comment.
- Page-break comments `% ---- printed p.N (PDF M) ----` at every boundary.

### ⚠ PAGE-BREAK MECHANICS — the two traps (both hit this book, both now fixed)
A `% comment` line eats its own newline, so a marker sitting between two text
lines does **not** break the paragraph. The two ways to get it wrong:

1. **A blank line before the marker** = a LaTeX paragraph break. Correct only
   where the *print* starts a new indented paragraph on the new page; wrong
   everywhere the sentence runs on. This crept in at every **batch seam**
   (each `Edit` replaced a `% [text to be added]` marker that had a blank line
   above it) — 14 spurious breaks, now removed. Conversely 9 pages where the
   print *is* indented had no break — now added.
   **Verify indentation from the image, don't guess:** measure the first text
   line's left edge against the median of the following lines; a real paragraph
   opening indents ~45–50 px at 150 dpi. Crop the outer ~12 % first, or scan
   edge-marks swamp the measurement (it failed silently on pp. 17, 57, 131 and
   had to be eyeballed — all three turned out flush/continuations).
   Blank lines are intended before exactly these markers:
   **3, 4, 26, 30, 36, 48, 52, 54, 76, 92, 97, 117.**

2. **A line ending in the print's hyphenation hyphen** renders as
   `For- fatters` — hyphen *and* stray space. 31 cases here. Fix: drop the
   typographic hyphen and end the line with `%` to swallow the newline —
   `…humoristiske For%` / marker / `fatters, som…` → *Forfatters*, with the
   page boundary still exactly where the print puts it.

**Regression check** (run after any edit; both must be empty/zero):
```bash
pdftotext transcription.pdf - | tr '\n' ' ' | tr -s ' ' | grep -o '[a-zæøå]- [a-zæøå]' | wc -l   # -> 0
python3 - <<'PY'
import re
L=open('transcription.tex',encoding='utf-8').read().split('\n')
KEEP={3,4,26,30,36,48,52,54,76,92,97,117}
for i,l in enumerate(L):
    m=re.match(r'% ---- printed p\.(\d+)',l)
    if not m: continue
    n=int(m.group(1)); prev=L[i-1].rstrip()
    if (L[i-1].strip()=='') != (n in KEEP): print("para-break mismatch p.",n)
    if prev.endswith('-') and not prev.endswith('---'): print("bare hyphen p.",n)
PY
```

**NB — the same latent defect exists in `../philosophisk-propaedeutik/`**
(25 lines ending in a bare hyphen before a page marker, so 25 renderings of
`Be- grebsanalyser`). Worth a pass there. `philosophie-og-mathematik` and
`brochner/problemet-tro-viden` are clean — they place the marker at a word
boundary instead, which also works but loses the exact break point.

## OCR pipeline (rebuild each session; nothing persists)
```bash
TD=/tmp/jc_ocr && mkdir -p "$TD" && cd "$TD"
wget -q https://github.com/tesseract-ocr/tessdata_best/raw/main/script/Fraktur.traineddata -O Fraktur.traineddata
export TESSDATA_PREFIX="$TD"
SRC="$(ls -d /sessions/*/mnt)/bibliotek/Nielsen, Rasmus/Kierkegaards_Johannes_Climacus_og.pdf"
mkdir -p pg txt
pdftoppm -f 11 -l 140 -r 300 -png -gray "$SRC" pg/p     # PDF = printed + 8
tesseract pg/p-0NN.png txt/p-0NN -l Fraktur --psm 6
```
**Sandbox gotcha:** background jobs (`nohup … &`) are **killed between bash
calls**, and each call caps at 45 s. Render/OCR in *foreground* chunks
(~6 pages of tesseract per call) and delete zero-byte `.txt` files left by
killed runs (`find txt -size -1c -delete`) before counting progress.

**Predictable OCR slips on this scan:** ſ→s (post-filter `sed 's/ſ/s/g'`);
ø read as o (Sporgsmaal→Spørgsmaal, gjore→gjøre, Forsoget→Forsøget);
ø/ö confusion in "Kjøbenhavn"; ck→ff; **d/b confusion** (fordunklet read as
"forbunklet"); **x read as r** (forvexles read as "forverles");
Reitzel→"Reigzel"; initial capitals in Fraktur (I/J, U/N) unreliable.
**Always zoom-verify any word that isn't a real Danish word before committing.**

## Verify compile recipe (locked in)
```bash
cd /tmp && rm -rf vjc && mkdir vjc && cd vjc
SRC="$(ls -d /sessions/*/mnt)/danish-texts/texts/nielsen/johannesclimacos/transcription.tex"
sed -e 's/\\usepackage{libertinus}//' -e 's/\\usepackage{libertinust1math}//' \
    -e 's/\\usepackage{textalpha}//' \
    -e 's/\\usepackage\[danish\]{babel}/\\usepackage{babel}/' "$SRC" > t.tex
# Greek stripped ONLY because the sandbox lacks textalpha — never in the real file
python3 -c "import re;p='/tmp/vjc/t.tex';s=open(p,encoding='utf-8').read();open(p,'w',encoding='utf-8').write(re.sub(r'[Ͱ-Ͽἀ-῿]+','[Gr]',s))"
perl -0pi -e 's/(\\documentclass\[[^\]]*\]\{book\})/$1\n\\usepackage{lmodern}/' t.tex
pdflatex -interaction=nonstopmode t.tex >l.txt 2>&1; pdflatex -interaction=nonstopmode t.tex >l.txt 2>&1
grep -o 'Output written.*' l.txt; grep -c '^!' l.txt
```
Expect 0 errors / 0 missing char. Balance-check braces and „/“ each batch.

## CURRENT RESUME POINT
## ✅ TRANSCRIPTION COMPLETE — whole book, printed pp. 3–132.

Nothing left to transcribe. `grep -c 'text to be added'` returns **0**; every
page 3–132 carries a `% ---- printed p.N (PDF M) ----` marker with no gaps
(verified programmatically). Final sandbox compile: **77 pp., 0 errors,
0 missing char**; braces 295/295; `$` = 8 (even); ledger **−4** (= expected,
see table).

The text ends with the dateline **Kjøbenhavn, d. 18. Sept. 1849.** and the
signature **R. Nielsen.**, followed by the centred ornament rule reproduced as
`\begin{center}---\end{center}`.

### Remaining, optional
1. Local compile with the real fonts (libertinus + libertinust1math +
   textalpha) — **confirm the Greek renders**: ποῦ στῶ, πᾷ στῶ (pp.63–64),
   δός πᾷ στῶ (pp.74–75), πᾷ στῶ (p.109).
2. A proofreading pass if wanted.
3. **Phase 2: the English translation** — a separate job. Build
   `translation.tex` mirroring this file 1:1 per
   `../../../TRANSLATION-PLAYBOOK.md`. See the structure map above for the two
   display questions and the two a)/b)/c)/d) sub-head series that the
   translation skeleton must reproduce.

## DONE so far (don't redo)
- **Batch 16 (printed pp. 127–132), image-verified — FINAL BATCH, book
  complete.** The half-a-principle joke that closes **d)**: even if one mediated
  and granted faith twice the influence of speculation, the system would still
  have *halvandet Princip* — and a dogmatics on one and a half principles is
  principle-less (p.127), with a footnote comparing the many mutually
  contradictory schools that formed after Socrates, who was no schoolman
  *ex officio*, to those that may yet form out of a *Hoveddogmatik ex officio*.
  Then the closing statement on the character of the dispute (pp.128–131):
  it is not a *Talentstrid*, not a hateful *Kjætterstrid* — Nielsen writes the
  Forord's jab at the "Enkelte" into the book of forgetting rather than rouse
  *rabies theologorum* — and not an egoistic contest for first place. He
  disclaims having discovered anything, says he is not organised to lead, and
  notes the asymmetry of the stakes with some dignity: if he is right he wins
  no victory, since he takes nothing originally from his own; if he is wrong he
  bears the shame alone, since no one else will want to take over his
  misunderstandings. Also his defence of blunt criticism over the "half-baked,
  moderate" review that is too envious to grant an author his due and too
  cowardly to raise a decisive objection (p.130). Closes with the offer that if
  Martensen shows him he has misunderstood the *Dogmatik* in its principle as
  in its problem, he will not hide behind an ambiguous silence but answer
  openly, though the answer be only the three words „jeg har feilet.“ Then the
  **dateline and signature**. Latin antiqua → `\textit{}`: *ex officio* ×2
  (p.127 fn.), *status quo* (p.128), *rabies theologorum* (p.129). One footnote
  (p.127). **Silent correction:** *Taushed* (p.132; my own slip caught on
  review, print is correct). Compile: **77 pp., 0 errors, 0 missing char**;
  braces 295/295; ledger **−4**; **markers 0**.
- **Batch 15 (printed pp. 119–126), image-verified.** Sub-head **d)** placed
  (p.125). The key formula of the whole Martensen half arrives at p.120,
  letterspaced: **\emph{Jeg begriber, at jeg ikke kan begribe}** — on this
  ground, Nielsen argues, dogmatics can meet religious philosophy freely and
  appropriate its yield without paying for it with its independence. He
  develops it through the woman with the alabaster jar: to sacrifice the most
  costly thing she must first have acquired it — so let the dogmatician grant
  that knowledge is precious, even the most precious, since it is precisely the
  most precious that must be sacrificed (pp.120–121). Then the striking reading
  of Martensen's own last section (pp.121–124): the *Dogmatik* sets out to
  mediate "den Høiestes Gjerninger" and ends at the antinomy between universal
  apokatastasis and eternal damnation, which will not mediate but stands as
  „et Kors for Tanken“ — and Nielsen's point is that this last word should have
  been the first, since all the dogmas stand in the same relation to objective
  knowledge and one incomprehensible point suffices to prove the whole
  incomprehensible. Kant posed the antinomies and, unable to solve them all,
  solved none; Hegel claimed to solve them all; each was a systematic head.
  Carries a **long Climacus footnote spanning pp.123–124** (kept as one
  `\footnote{}`), attributed at its close. Latin: *vulgus odi* (p.119),
  *ergo* (p.122), *eo ipso* ×3 (p.123 fn.). Two further footnotes (p.120
  citing Martensen's 1847 Maria Magdalena sermon; p.127 below). **Sixth ledger
  anomaly** at the p.123 footnote. Compile: **74 pp., 0/0**; braces 286/286;
  ledger **−4**.
- **Batch 14 (printed pp. 111–118), image-verified.** *Troens Forhold til den
  metaphysiske Objectivitet* (letterspaced, p.112). Hermeneutics, the
  spirit/letter distinction, and the demand for a *Criterium* by which to tell
  when that distinction runs with or against faith (p.111). **Three more
  self-citations**: two footnotes to *Den propædeutiske Logik* (S. 144–157;
  S. 182–86, comparing Martensen's angels to the *Logik*'s personifications and
  intermediate hypostases) and one to *Evangelietroen og den moderne
  Bevidsthed* (p.113), plus a reference to the *Smuler* (Ug. 1844). Then the
  Trinity test case (pp.114–115): is the dogma to be construed as philosopheme
  or not — *Ja eller Nei*? — and the trilemma of believing *with*, *without*,
  or *against* "the Concept". The answer comes as the **rich-uncle parable**
  (p.116), the best sustained image in the book: the poor labourer whose
  strength grew with his work and who thanked God, until an inheritance let him
  keep people to work for him — whereupon his courage sank as his wealth grew.
  So with a faith that becomes heir to knowledge: let philosophy, as on its
  deathbed, bequeath it a handsome capital of ontological "shadow-cognitions"
  and let it keep concepts to take the shock, and faith is weaned off exertion,
  weakened in idleness, and sickens into softness. Against which Nielsen sets
  Tertullian: *jeg troer, endskjøndt jeg ikke kan begribe* is ambiguous and
  resolves only into *jeg troer, fordi jeg ikke kan begribe* —
  *credo, quia absurdum est*, which he defends not as a barbarian's
  stumbling-block but as an incorruptible border-guard posted where faith and
  knowledge meet, to keep them from beguiling each other (pp.117–118). Latin:
  *theologia irregenitorum* / *regenitorum*, *lapis lydius*, *Criterium*,
  *fides humana* / *divina* (p.111), *in specie*, *conditio sine qua non*
  (p.113), *in absurdum*, *credo, quia absurdum est* ×3 (pp.117–118). Five
  footnotes. No print flags, no new ledger anomalies. Compile: **70 pp., 0/0**;
  braces 275/275; ledger **−3**.
- **Batch 13 (printed pp. 103–110), image-verified.** The examination of
  **Troens Forhold til den historiske Objectivitet** (letterspaced run-in at
  p.103) — Protestantism's material and formal principle, Scripture and the
  symbols, the witnessing Church. Nielsen's verdict: the fundamental question
  is missing, approximation reigns, and the whole thing runs out "i en flydende
  Omtrentlighed." He then walks the regress step by step, each step conceded
  with the same ironic formula (*Ja, paa en vis Maade, men dog ikke saa
  ganske*): Christ is the objective canon → but where is Christ found? in the
  Church → but then Protestantism collapses into Catholicism, so the deviation
  must be Scripture as final *lapis lydius* → but §23 withholds the literal
  Scripture-principle → but salvation-concern is individual → so the outward
  canon points to an inward one, the *testimonium spiritus sancti* (pp.104–105).
  Then the sharp question (p.107, letterspaced): **how does the
  evangelical-Lutheran Church get its adequate Læretypus, its Dogmatik?** The
  Church as "hiin store Enkelte" does not write dogmatics; a dogmatician does,
  and he is an Enkelt — so how can he identify his Christian subjectivity with
  the Church's true objective essence? The dilemma at p.108: either certain
  Enkelte possess faith's content richly enough to lay down the rule for all,
  or the Church goes on approximating its inward canon without ever reaching
  it. Closes on the **Greek** πᾷ στῶ ×2 (p.109) — dogmatics going from
  approximation to approximation without ever finding its promised standing
  place — and on the *fides humana / divina*, *fides historica / religiosa*
  distinctions the older Lutherans drew and Martensen passes over (p.110).
  Nielsen also splices in a long Climacus citation on the 100,000 witnesses,
  explicitly attributed „Joh.\ Cl." (p.106). Latin antiqua → `\textit{}`:
  *lapis lydius* ×3 (pp.104–105), *testimonium spiritus sancti* ×3
  (pp.105, 107), *punctum saliens* (p.105), *eo ipso* / *en masse* (p.106),
  *fides humana* / *fides divina* / *fides historica* / *fides religiosa*
  (p.110). `ɔ:` ×2 (pp.106, 108). **Two further ledger anomalies** (pp.103,
  105 — see table). No print flags. Compile: **65 pp., 0 errors, 0 missing
  char**; braces 252/252; ledger **−3**.
- **Batch 12 (printed pp. 95–102), image-verified.** Closes the long Climacus
  citation (p.95–96) with the **saw image** — in sawing, the lighter you make
  your hand the better the saw goes; press with all your strength and you do
  not saw at all. So too the speculant must make himself objectively light,
  whereas one infinitely interested in his eternal blessedness makes himself
  subjectively as heavy as possible, and thereby makes speculating impossible.
  Hence Martensen's *credo, ut intelligam* cannot justify speculation. Then the
  second cardinal sentence and the *fides quæ / qua creditur* apparatus
  (pp.96–97): Catholicism leans too far toward the objective, one-sided
  Protestantism toward the subjective, and the *Dogmatik* claims to hold the
  balance. Nielsen tests this against **sacramental doctrine** — the one place
  the free union of objective and subjective must show itself — and finds the
  Inderlighedsproblem simply absent. Baptism (Mark 16:16) and the Supper
  (1 Cor. 11:28–29) are each objectively true only *for the believer*; were an
  unbeliever convinced by objective proof he would have to become either a
  believer or a devil (p.98). His conclusion: what objective grounding achieves
  here is *aldeles Intet* — no evasions about it holding "to a certain degree."
  Yet this does not make faith self-feeding: it is precisely the *Troesobject*
  the believer feeds on, the grace given in the sacrament (p.102). Latin
  antiqua → `\textit{}`: *credo, ut intelligam* (p.96), *fides, quæ creditur* /
  *fides, qua creditur* / *res ipsa* / *usus* (pp.96–98, many). `ɔ:` ×3
  (pp.95, 98, 102). No print flags, no new ledger anomalies. Compile:
  **60 pp., 0 errors, 0 missing char**; braces 232/232; ledger **−1**
  (= baseline, settling exactly as predicted).
- **Batch 11 (printed pp. 87–94), image-verified.** Finishes **b)** and opens
  **c)** (p.90). The speculative demand pressed home with examples (p.87): the
  subjective idealists know as well as anyone that there is an external sensible
  world, yet treat it speculatively as *Skinverden*; why does Schelling fall
  back on the indifference of the Ground, why does Hegel begin with Being and
  Nothing, why does **Sibbern** define philosophy as an all-embracing debate of
  everything against everything? Because speculation *qua* speculation cares
  nothing for practical certainty. Hence, if speculation is to be carried
  through in dogmatics, every practical Christian representation must be
  converted into a speculative problem — an operation Nielsen doubts the
  dogmatician dares. Then presupposition vs. abstraction and the method
  question (p.88), with **the first self-citation in the book**: a footnote to
  Nielsen's own *Den propædeutiske Logik* (1845), S. 102–112. Daub and
  Marheineke as the test case (p.89): they lacked neither theological knowledge
  nor Christian presuppositions, so the failure of speculative dogmatics lies
  in speculation itself, not in missing premises. Sub-head **c)** at p.90.
  Nielsen is careful to acquit Martensen of both rationalism and enthusiasm
  (p.90) — the charge is naivety, a faith in speculation's dogmatic usability
  taken *de bonne foi*, and he quotes Martensen's own generous concession
  ("For ingen Priis… vilde jeg være uenig med den Troende") as a good
  confession on which much may later be built (p.91). The two cardinal
  sentences, *credo, ut intelligam* against *de omnibus dubitandum est*
  (p.92) — and Nielsen's retort that had Martensen made earnest of the
  "Skepsis" he grants, i.e. let dogmatics develop the critical and dialectical
  drive contained *in faith itself*, he would have found the principled
  difference he is looking for. Then Nielsen **quotes the Efterskrift back at
  Martensen** at length (pp.93–94): the speculant who builds his eternal
  blessedness on speculation contradicts himself comically. Latin/French
  antiqua → `\textit{}`: *in specie* (p.88), *de bonne foi* / *in gloriam
  fidei, in gloriam Dei* (p.91), *credo, ut intelligam* / *de omnibus
  dubitandum est* (p.92). `ɔ:` ×2 (pp.88, 93). One footnote (p.88). **Print
  flag:** *forvexler* for print "forverler" (p.89, r/x). **Fifth ledger
  anomaly** at p.92 (see table). Compile: **56 pp., 0 errors, 0 missing char**;
  braces 214/214; ledger **0** at the seam (= −1 baseline + one open quote).
- **Batch 10 (printed pp. 79–86), image-verified.** All inside sub-head **b)**.
  Nielsen argues that Martensen's Forord must be read *cum grano salis* — as
  irony — because it makes the rule an exception and the exception a rule in
  one and the same breath (pp.79–80); abstracting from the irony, Martensen is
  committed to the indissoluble unity of faith and thought, which sharpens the
  dilemma: if faith's thinking just *is* speculation, what entitles him to say
  he reached certainty by another road? (p.80). The **Martha passage** (p.81,
  Joh. 11:40) is the finest thing here: Martha's seeing was assuredly no
  speculative seeing — inferable not chiefly from her being a woman but best
  from her seeing God's glory *through tears*; and when the believer sees so,
  the seeing is upbuilding but not speculative. Then the *plus ultra* argument
  (pp.82–84): Fichte is plus ultra to Kant, Schelling to Fichte, Hegel to
  Schelling — but who is plus ultra to Hegel? Aspirants have announced
  themselves; none has won the prize; Hegel stands in pure speculation as the
  unbeaten master, as *non plus ultra*. Since Martensen nonetheless blames
  Hegel for the false mediation and the sham reconciliation of faith and
  knowledge, Nielsen concludes that on the speculative comprehension of
  Christianity "we are still exactly as near as before," and mock-reconstructs
  the three supposed advances since Hegel (believing in speculation; an
  upbuilding speculation; mediating the Absolute relatively). Closes on the
  regress of a "deeper appropriation" of what is already the most certain of
  all (p.85–86) and the statement of the speculative demand. Latin antiqua →
  `\textit{}`: *cum grano salis* (p.79), *non plus ultra* / *plus ultra*
  (pp.82–84, many), *retractationes* (p.83). Sperrsatz: *Stykkevise* (p.82),
  *tænke* / *troe* / *opbyggelige* / *Skuen* (p.84). No `ɔ:`, no footnotes, no
  Greek. **No print flags and no ledger anomalies** — the first batch since
  p.45 to run entirely straight. Compile: **51 pp., 0 errors, 0 missing
  char**; braces 203/203; ledger **0** (= baseline).
- **Batch 9 (printed pp. 71–78), image-verified.** All inside sub-head **b)**.
  The ironic set-up (p.71): since it is the same Logos at work in the realm of
  Nature and of Grace, "den christelige Dogmatik" will charitably take in the
  poor abandoned and bewildered Speculation — well knowing that it is
  speculation, not Christianity, that is being done the favour. Nielsen then
  warns that before we congratulate speculation on its dogmatic elevation we
  should check the terms on offer. **Two fully letterspaced quotation blocks**
  carry the argument — the whole citation is in Sperrsatz, not just a phrase,
  so the `\emph{}` wraps the entire quoted paragraph: the *Videnskabs Organ /
  Kirkes Organ* declaration (p.72, § S. 4) and the *For Dogmatiken … δός πᾷ στῶ*
  passage (p.74, § S. 5). Between them, the objection that serving two masters
  makes the dogmatician treat his science *overvidenskabelig, det vil nok sige:
  paa en uvidenskabelig Maade* (p.73), and the principled point that
  speculation is an *ideal Potens* which must stand or fall by its own
  power — it can be ignored or despised, but not *used* for something else
  without violating the Absolute (p.74). The finest stretch is p.75: dogmatics
  as the best-endowed of all sciences, having from the cradle everything the
  others must labour for — so why does it stoop to beg what belongs to
  speculation? Speculation, says Nielsen, is not envious; it simply cannot see
  what moves so richly endowed a dogmatics to get involved with speculation's
  poverty, and holds back "som var den bange for at blive tilovers." Then the
  attempt to rescue a sense for "Tænkning" as existential rather than
  speculative (p.76), its refusal (p.77 — *det kalder jeg at troe — paa
  Speculationen*), and the closing dilemma (p.78). **Greek:** δός πᾷ στῶ
  (pp.74, 75, δός in antiqua → `\textit{}`), πᾷ στῶ ×2 (p.75) — zoom-verified
  at 500 dpi. Latin: *credo ut intelligam* (p.72). `ɔ:` (p.74). **Print flags,
  corrected + flagged inline:** *er* for print "ev" (p.71, r/v), *doterede* for
  print "boterede" (p.75, d/b). **Fourth ledger anomaly** at p.71 (see table) —
  verified at 500 dpi before accepting. Compile: **47 pp., 0 errors, 0 missing
  char**; braces 184/184; ledger **0** (= new baseline).
- **Batch 8 (printed pp. 63–70), image-verified.** Closes sub-head **a)** with
  the answer to the p.62 question: between dogmatics and
  Christendomsphilosophie there is *„ingen, aldeles ingen"* difference — the
  philosopher must take his stand in the Centre just as the dogmatician does.
  **First Greek in the book** (pp.63–64, see above): it is no use, Nielsen
  says, for the dogmatician to invoke faith and puff himself up in the Church
  when what he says speculatively is ποῦ στῶ — for the philosopher now says
  πᾷ στῶ too, and there they both stand in the middle of speculation. Then the
  imagined interlocutor's three attempts to name a difference — in treatment of
  material (p.64), in the *flydende/vordende* boundary (p.64), in the
  "intellectual love" proper to the *Lærerstanden i Kirken* (p.65) — each
  answered with the same refrain, *hvor er saa Forskjellen?* The failed
  examples (Schleiermacher, Jacob Böhme) at p.66, and the verdict that the
  intended separation "ender i et reent Nul" (p.67). Sub-head **b)** placed at
  p.67. Then the most personal passage in the book (pp.68–69): Nielsen reads
  Martensen's *skarpe Sideblik* at certain "Enkelte" as aimed at himself, and
  asks to be told his sentence publicly — the mordant image of the man who
  learned from the newspaper that he had been dismissed from his post, and the
  footnote that "den christelige Viisdom" *veed at pointere*. Latin antiqua →
  `\textit{}`: *miserabile dictu* (p.68), *con amore et ex officio* (p.69).
  `ɔ:` ×2 (p.63). One footnote (p.68). **Print flags, corrected + flagged
  inline:** *han* for print "har" (p.63, n/r glyph), *Forvexling* for print
  "Forverling" (p.65). Compile: **42 pp., 0 errors, 0 missing char**;
  braces 173/173; ledger **+2** at the seam (mid-quote; baseline +1).
- **Batch 7 (printed pp. 55–62), image-verified.** Nielsen presses the "small
  Enkelte" question (p.55) — he looks and looks at the *Tidernes Tegn* and
  cannot see the heretics Martensen warns against; "om jeg saa fik syv Par
  Briller paa". The advice that if no such heretic exists, the dogmatician had
  better watch himself and leave "de Enkelte" in peace (p.56). Sub-head **a)**
  placed at p.57. Then the central catch of this stretch (pp.57–60): Martensen
  declares on p.4 of the *Dogmatik* that he "ingenlunde" concedes scientific
  insight into Christian truth is possible without Christian faith — and on
  p.14 grants that philosophers, poets and sculptors have rendered Christian
  representations with great plastic force without holding them religiously.
  Nielsen sets the two passages side by side ("som de nu staae, ligne de to
  Paarørende, der have skilt sig i indbyrdes Uenighed og vende hinanden
  Ryggen"). Then the *credo ut intelligam* passage (§ 35) and the argument that
  the "merely relative" difference between Christian philosophy and dogmatic
  speculation shrinks until no one can point to it (pp.61–62).
  **Findings:** the **folio misprint at p.58** (see above); a **third
  quote-ledger anomaly** at pp.59–60 (see ledger) — verified at 400 dpi at the
  dash before accepting. Latin antiqua → `\textit{}`: *in specie* (p.56),
  *credo ut intelligam* (p.61). `ɔ:` (p.60). **Print flag:** *fordret* for
  print "forbret" (p.58). Compile: **37 pp., 0 errors, 0 missing char**;
  braces 161/161; ledger **+1**.
- **Batch 6 (printed pp. 47–54), image-verified.** Closes the Martensen preface
  quotation (p.47) and Nielsen's dry gloss on how easily Dr. M. has "let
  himself be taught by the signs of the times." The **second display question**
  placed at p.48. Then the core symmetry argument of the Martensen half
  (pp.49–51): Christianity communicates the Absolute in the form of *Tro*,
  speculation in the form of *Viden*; to be "absolut i Viden" and "absolut i
  Troen" are each, properly understood, not presumption but a duty of
  self-limitation — and each principle is *forqvaklet* the moment it leans on
  the other (the mathematician who argues from immediate experience instead of
  stringent proof). Fichte/Schelling/Hegel on one side, Paulus-to-Luther on the
  other. Then the pressing of Martensen's phrase "altfor tidligt" (pp.52–53) —
  Nielsen cannot make it mean anything that is both true and non-trivial — and
  the Eph. 4:13 quotation on the one great Enkelte (p.54). Note Nielsen's
  needling courtesy throughout ("min høiærværdige Ven"). Compile: **33 pp.,
  0 errors, 0 missing char**; braces 151/151; „/“ = 135/133 (**+2** = new
  baseline).
- **Batch 5 (printed pp. 38–46), image-verified.** Finishes the Climacus half:
  Christianity as existence-communication vs. doctrine, the polemic against
  *Mediation* (*Mediationen* / *medieres* letterspaced, p.39), the mordant
  simile of speculation and Christianity merging like two noble families or two
  trading houses into one firm (pp.39–40), and the closing distinction between
  a doctrine to be comprehended and one to be realised in existence (pp.40–41).
  **The hinge at p.42:** centred rule (`\begin{center}---\end{center}`), then
  the turn to Martensen, *den christelige Dogmatik* letterspaced. Nielsen's
  strikingly two-edged appreciation of Martensen's style (p.43) — the
  architectonic dogmatics that "weds the University building to the Palace
  chapel," daylight mixed with the gleam of an altar candle. The governing
  question restated and narrowed at p.44 (both forms letterspaced): *Vil
  Christendommen være Gjenstand for dogmatiserende Speculation?* Then the
  autobiographical passage (pp.44–45) on Martensen's 1837 *Autonomie* and
  Nielsen's own 1840 dissertation written on the same premise — and his
  admission that he has since *skiftet Standpunkt* while Martensen has not.
  **Footnotes begin here:** three short ones (pp.44–45) plus a long quotation
  from Martensen's preface **spanning pp.45–46**, kept as one `\footnote{}`
  with an inline page-break comment. Compile: **28 pp., 0/0**; braces 148/148.
- **Batch 4 (printed pp. 30–37), image-verified.** Sub-head **d)** placed
  (p.34). Subjectivity as *Usandheden*, the move that makes inwardness deeper
  than the Socratic; *Synd* and *Arvesynden* (both Sperrsatz → `\emph{}`, p.31);
  the eternal truth come-to-be-in-time as the Paradox (p.32); the Absurd as the
  *Kraftmaaler* of faith (p.33); the big **fully letterspaced display
  proposition** on p.34 (*Individets evige Salighed afgjøres i Tiden ved
  Forholdet til noget Historisk…*) → whole paragraph in `\emph{}`; Christianity
  as fact rather than doctrine, faith's object as the teacher's *Virkelighed*
  (p.35); faith not a *Sinke-Lectie* in the sphere of intellectuality (p.36);
  the parody diagnosis — it has become nothing to become a Christian and a busy
  task to comprehend Christianity (p.37). Latin antiqua → `\textit{}`:
  *eo ipso* (pp.32, 35, 36), *sensu strictissimo* (p.33), *quam maxime* (p.36).
  `ɔ:` ×2 (p.35). **Print flags (glyph confusions), corrected + flagged
  inline:** *forvexler* for print "forverler" (p.33), *forvexles* for print
  "forverles" (p.36). Compile: **23 pp., 0 errors, 0 missing char**; braces
  136/136; „/“ = 87/84 (**+3**, on ledger).
- **Batch 3 (printed pp. 19–29), image-verified.** Sub-heads **b)** (p.21) and
  **c)** (p.27) placed. Closes the objective-way argument (speculation's
  *sub specie æterni* illusion, p.19; the objective reflection's way to abstract
  thought and the Hamlet aside, p.20); then the whole subjectivity stretch —
  poetry and the priests as evidence that it is *something distinguished* to be
  a subject (pp.21–22), madness vs. inwardness (pp.22–23), the Jeg-Jeg as a
  mathematical point (p.23), the objective/subjective *Vei-Forskjel* with
  **Hvorledes** and **saaledes** letterspaced (p.24), the prayer/idol example
  (p.25), the immortality example and the **letterspaced definition of truth**
  (*den objective Uvished, fastholdt i den meest lidenskabelige Inderligheds
  Tilegnelse…*, p.26). Then Nielsen's remarkable **first-person confession**
  about the Paradox — the book by turns attracting and repelling him, the
  "bagvendt forheret Tænker" suspicion, and the staged dialogue with the
  pseudonym (pp.27–28). Closes on the Socratic ignorance/Absurd analogy (p.29).
  Latin/French antiqua → `\textit{}`: *sub specie æterni* (p.19),
  *coup de hasard* (p.27), *in mente* (p.29). `ɔ:` ×2 (pp.22, 28).
  **Print flags, corrected + flagged inline:** *fordi* for print "forbi"
  (p.22), *paradox* for print "parador" (p.29). **Zoom-verified:** p.27
  *Øiet* (OCR read "Diet" — Fraktur Ø reads as D). Compile: **18 pp., 0/0**;
  braces 123/123; „/“ = 69/66 (**+3**).
- **Batch 2 (printed pp. 11–18), image-verified.** Sub-head **a)** (p.11) and
  the α)/β) split. The historical way: scripture-criticism as endless
  approximation (the Thames-tunnel image, p.12), church vs. bible (p.13), the
  eighteen-centuries proof as *Adspredelsens Magt* (p.14), the two thought
  experiments — grant the scholars everything, then grant the enemies
  everything (pp.15–17) — and the opening of the speculative way (pp.17–18).
  **Preamble fix:** added `graphicx` + `\DeclareUnicodeCharacter{0254}{\reflectbox{c}}`
  for the `ɔ:` id-est mark (the repo's house convention; without it the file
  errors). Latin antiqua → `\textit{}`: *conditio sine qua non* (p.11),
  *e concessis* (p.15), *ubique et nusquam* + *integri* (pp.16–17). `ɔ:` (p.11).
  **Print flags:** p.13 *„bortskjærer al den Bevisen og Bevisen,"* — the print
  genuinely repeats the word; **zoom-verified**, reproduced verbatim + flagged.
  *forvexle* for print "forverle" (p.16). Compile: **12 pp., 0/0**;
  braces 105/105; „/“ = 41/38 (**+3**).
- **Batch 1 (front matter + printed pp. 3–10), image-verified.** Preamble
  (book class; amsmath, enumitem, libertinus, libertinust1math, textalpha,
  fancyhdr, hyperref, microtype — prose only, no tikz/graphicx). Title page
  (PDF 9) reproduced. Opening paragraph + the **display citation of the two
  books under review** (the *Efterskrift* with its full subtitle and the
  *Christelige Dogmatik*), set as a centred block. The governing question on
  p.4 set `\emph{}` (Sperrsatz, zoom-verified). The Ja-branch (Skoletheologien's
  claim on the Church, the ironic "Kirkebøn for den christelige Videnskab" /
  "Bededag for den kritiske Indledning") and the Nei-branch (give Caesar his
  due; the learned disciplines to their own fate), pp.5–6. The methodological
  apology for reporting an indirect-communication text in direct form, pp.7–8,
  with the **footnote spanning pp.7–8** (*in optima forma*; the joke about the
  reader's pleasure "at lee og tænke paa een Gang"). The "Risico" paragraph and
  the wager that *et Princip er meer end et Individ*, p.9. The **first display
  question** placed at p.9. Opens the problem-statement argument, p.10
  (*eo ipso*; theology/philosophy spend as much labour stating a problem as
  solving it; the *flydende* boundaries). **Zoom-verified against OCR slips:**
  p.7 *forvexles* (print glyph ambiguous r/x — flagged inline), p.10
  *fordunklet* (OCR's "forbunklet" was the slip; print is correct, no flag).
  Compile: **7 pp., 0 errors, 0 missing char**; braces 95/95; „/“ = 24/24
  (balanced); `$` = 0; 1 marker remaining.
