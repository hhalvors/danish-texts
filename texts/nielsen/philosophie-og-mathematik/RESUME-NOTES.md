# Rasmus Nielsen — *Philosophie og Mathematik* (1857): START-HERE / resume notes

**Read this first, then the two standing-method files it points to, then begin.**

---

## 0. The one thing to understand before you start

The end goal Hans wants is an **English translation**. But you translate FROM a
Danish `transcription.tex`, and **that file does not exist yet** — there is no
`transcription.tex` for this book. So this is a **transcription-first** job:

1. **Phase 1 — transcribe** the Fraktur scan into an image-verified
   `transcription.tex` (Danish). This is the bulk of the work.
2. **Phase 2 — translate** that transcription into `translation.tex` (English).

Do NOT try to translate straight from the scan. Transcribe first, verify it,
then translate from the verified Danish. **Scope is settled: the WHOLE book**
(the full ~84-page body plus front matter — not selections). The `catalog.yaml`
"Selections" label is stale; it has been updated to the whole work.

---

## 1. The two standing methods (your real instruction manuals)

- **Transcription discipline** (Phase 1): follow the exact workflow proven on
  *Grundideernes Logik*, documented in
  `../grundideernes-logik/RESUME-NOTES.md`. That file is your model for how to
  render Fraktur Danish → image-verified LaTeX (Sperrsatz, quotes, footnotes,
  page-break comments, the portable verify compile, the balance checks). Read it
  in full — everything there applies here.
- **Translation discipline** (Phase 2): follow `../../../TRANSLATION-PLAYBOOK.md`.

Both were written for this repo; don't reinvent them.

---

## 2. This book, concretely

- **Title:** *Philosophie og Mathematik: en propædeutisk Afhandling*, af R.
  Nielsen, Professor i Philosophien. Kjøbenhavn: Gyldendal (F. Hegel), 1857.
- **Scan:** `~/bibliotek/Nielsen, Rasmus/1857phil-math.pdf` — the Royal Danish
  Library (KB) scan, **93 PDF pages**, public domain. Body extent ≈ **84 printed
  pages**. (An alternate scan `Philosophie_og_Mathematik.pdf`, 88 pp, also exists;
  prefer the KB `1857phil-math.pdf`.)
- **Script:** **Fraktur** throughout the body (same as *Grundideernes Logik*).
  Type ß/umlauts directly; Danish „…" quotes as U+201E / U+201D.
- **Front matter:** KB boilerplate on PDF pp. 1–5; **title page = PDF p. 6**;
  verso PDF p. 7; body text begins a page or two after. There may be a short
  preface — check pp. 8–10.
- **Page offset:** confirmed data point **PDF 30 = printed 25** (⇒ body offset ≈
  **PDF = printed + 5**). Do NOT trust a single point — verify the constant
  against several printed headers per the playbook, and record it here once fixed.
  Front-leaf pagination may differ from the body.
- **catalog.yaml:** id `philosophie-og-mathematik` (around line 196). When Phase 1
  compiles clean, set its section `status:` and add a Transcription link; do the
  same for a Translation link/section after Phase 2 (mirror the
  `grundideernes-logik` entry's shape).

---

## 3. The BIG difference from *Grundideernes Logik*: math + figures

This is a *propædeutisk* essay on philosophy **and mathematics**, so unlike
*Grundideernes Logik* (mostly prose with occasional equations) it is genuinely
**mathematics-heavy and contains geometric figures**. On printed p. 25 alone
there is: an asymptote/hyperbola **diagram** (points A, B, B′, D, E, D′, E′),
inline equations (`AB = x; BD = y; BE = y₁`), and a display equation
`f(x) = y = (b/a)·√(x² − a²)`. Expect throughout:

- **Display + inline math:** functions `f(x)`, fractions `\frac{b}{a}`, roots
  `\sqrt{x^{2}-a^{2}}`, subscripts/superscripts (`y_{1}`, `x^{2}`), Greek, limits,
  series, etc. Use `amsmath`. **Image-verify every equation by cropping and
  zooming**, exactly as was done for the Fechner/Herbart formulas in
  *Grundideernes Logik* — misread exponents and subscripts are the main risk.
- **Figures / diagrams — a new challenge not present in the previous book.**
  Decide a policy with Hans up front and keep it consistent. Options, roughly in
  order of fidelity/effort: (a) redraw each figure in **TikZ**; (b) crop the
  figure from the scan at high DPI and `\includegraphics` it (needs `graphicx`;
  keep the cropped PNGs in the book folder); (c) placeholder with a captioned box
  + a `% FIGURE` note for Hans to supply art later. Whatever you pick, flag every
  figure in `RESUME-NOTES` with its printed-page location.
- **Portability caveat carried over:** the portable verify build (xelatex,
  `fontspec`, no `libertinus`/`libertinust1math`) can't do amssymb-only glyphs or
  `\varkappa` without help. Prefer `amsmath`-only constructs; if you must use a
  `libertinust1math`/`amssymb` symbol (e.g. `\varkappa`), keep it in the real
  file and add a `\providecommand{...}{...}` **in the verify transform only** (see
  how the *Grundideernes Logik* notes handled `\varkappa` and `\gtrless`).

---

## 4. Preamble to start `transcription.tex` with

`book` class; `amsmath` (not amssymb unless truly needed); `graphicx` (for
figures); `libertinus` + `libertinust1math`; `textalpha` (Greek typed as Unicode,
as in the existing corpus); `fancyhdr`, `hyperref`, `microtype`. Mirror the
`grundideernes-logik/transcription.tex` preamble and adjust. For Phase 2's
`translation.tex`, use the playbook's §4 checklist (`enumitem` etc.).

---

## 5. Rhythm & the standing rule

- Work in ~10-printed-page batches. Per batch: render pages → **image-verify all
  Sperrsatz + every equation/figure** → single `Edit` inserting the block →
  balance-check (braces, `$` parity, `\[`/`\]`, no stray `text to be added`) →
  portable xelatex compile (target: 0 undefined control seqs, 0 runaway args) →
  spot-check the rendered math/figure pages → update this RESUME-NOTES → hand back.
- Use TaskCreate/TaskUpdate per batch (renders as a progress widget for Hans).
- **Hans commits and pushes. You never run `git commit` or `git push`.** (Standing
  security constraint across this whole repo.)

---

## CURRENT RESUME POINT
**PHASE 1 (TRANSCRIPTION) IS COMPLETE (2026-07-06).** The whole body — printed
pp.3--84 (title through the closing sentence „…at det Uendelige altsaa dog er
endeligt, og det Endelige uendeligt.") — is transcribed and image-verified in
`transcription.tex`. Final portable compile: **69 pages, 0 errors, 0 undefined cs,
0 missing-character warnings, 0 leftover markers.** 19 TikZ figures, 4 flagged print
oddities. Document structure intact: sections I--III with all subsections/sub-subs.

**Next step: Phase 2 — translation.** Create `translation.tex` (English) from the
verified Danish `transcription.tex`, following `../../../TRANSLATION-PLAYBOOK.md`.
Suggested first move: translate the front matter + Section I, batch by batch, mirroring
the transcription batching. Keep every figure/equation as-is (only prose is translated).
Optionally, before starting Phase 2, do a full read-through of `transcription.tex`
against the scan one more time for typos. (Historical transcription notes follow below.)

--- (transcription-phase notes retained for reference) ---
NB house rule (adopted
2026-07-05): put `\phantomsection` before every `\addcontentsline{toc}{...}`; wrap
any `\quad`-bearing section bookmark string in `\texorpdfstring{printed}{plain}`.

Verify-recipe reminder (locked in): the sandbox `sed` transform now needs the
extra `-e 's/\\usepackage\[danish\]{babel}/\\usepackage{babel}/'` (sandbox babel
lacks the danish option). Long inline-fraction footnotes / long displayed series
throw cosmetic Overfull \hbox warnings — harmless, they stay within the margin in
the rendered PDF and will be tighter with libertinus on the real machine. Where a
big inline fraction would run off the line, set it as a display (`\[ \]`) — the
print does that anyway (see p.44). TikZ figures embedded inside a `\footnote` (via
`\begin{center}…\end{center}`) compile fine (see the p.39 complex-plane figure).

## FIGURE POLICY IN PRACTICE (locked in, batch 3)
Figures are redrawn in **TikZ** and placed as **centred blocks** at their
reference point (the print wraps text around some of them; centred is the
transcription choice — flagged in a `% FIGURE` comment giving the printed-page
location and a description). `\usetikzlibrary{calc}` suffices so far. Four
figures done (pp.22--25) plus a 5th (p.39, a complex-plane cross embedded inside a
footnote) — see below. When a figure needs trig, use TikZ math (`{cos(40)}` etc.).
Keep each figure's `% FIGURE (printed p.N): …` comment.

## ERRATA TO APPLY (from the p.4 „Rettelse." page)
- **printed p.25, line 9:** print has „Tilnærmelse til et Uopnaaeligt"; the
  Rettelse says read „Tilnærmelse til et **Opnaaeligt**". APPLY in batch 3.
  (Recorded as a comment in transcription.tex at the p.4 slot; the errata page
  itself is not reproduced as body text.)

## RENDERING CONVENTIONS LOCKED IN (batch 1)
- Top-level divisions are Roman-numeral sections „I.", „II.", … with a
  letterspaced title. Rendered as a centred block: {\large\bfseries N.} +
  {\Large\bfseries Title.} + a short \rule, then \addcontentsline{toc}{section}
  and \markboth for the running head. (Section I = „Mathematiske Functioner".)
- Single italic/antiqua variables (a, b, x, y, z, t, u, A, B, C, D, n, m) and
  all equations → math mode. Multiplication dot in the print → \cdot.
- Function symbols: the four Fundamentalligninger use f with index below →
  \(f_{1..4}\). Inverse-function Greek φ, ψ → \varphi, \psi (math, portable).
  Roots \sqrt[n]{}, \sqrt[2m]{}. „arc (cos = x)" kept literal as
  \mathrm{arc}\,(\cos = x).
- Danish quotes „…“ as U+201E / U+201D. Footnotes at the anchor word.
- Page-break comments „% ---- printed p.N (PDF M) ----" at each boundary.

## SETTLED FACTS (verified this session)
- **Scan = KB's own DOD scan** (`1857phil-math.pdf`). Confirmed: PDF p.1 is the
  „Digitaliseret af | Digitised by — DET KGL. BIBLIOTEK" cover; metadata =
  iTextSharp / „Published: 1857." / A4 / 21 MB. The other file
  (`Philosophie_og_Mathematik.pdf`, 88 pp, 4.5 MB) is the lower-quality Google
  Books scan — do NOT use it. No better scan to obtain; this is the best.
- **Offset: PDF = printed + 5** (verified at PDF 10→p.5, 20→p.15, 30→p.25).
- **Structure:** title = PDF 6 (printed 1); blank verso = PDF 7 (printed 2);
  body begins PDF 8 (printed 3). No Forord / Indhold / Indledning.
- **Figure policy:** redraw every figure in TikZ, image-verified. (`tikz` in
  preamble.) First figure printed p.25.
- The faint „1 / Mathematisk Forbegreb" above the p.3 drop-cap is physical
  show-through/set-off, NOT a heading — do not transcribe it.

## DONE so far
- **Body batch 24 / FINAL (2026-07-06): printed pp. 83--84 done & image-verified —
  END OF BODY.** Closes **c) Integralets Bestemmelse** (and the book). p.83: the
  constant-of-integration wrap-up ($bdBD=\int_{x'}^x y\,dx=f(x)-f(x')=f(x)+C$), then
  the Punkt→Linie→Flade→Legeme / integration-w.r.t.-Masse passage; the **sphere
  attraction** derivation — **FIGURE #17** (printed p.83): circle centre $A$, element
  $dm$ on it, foot $B$, external $M$, angle $\alpha$, radius $r$, dashed $dm$--$M$;
  $AM=a$, $AB=r\cos\alpha$ (schematic redraw). $dm=pdw$, $dw=r^2\sin\Theta\,dr\,d\Theta
  \,d\alpha$; the attraction fraction $\frac{kdm(a-r\cos\alpha)}{(r^2+a^2-2ra\cos
  \alpha)^{3/2}}$ and its integral $k\int\dots$, then $kp\int\frac{dw(\dots)}{\dots}
  =kp\int\frac{r^2\sin\Theta dr d\Theta d\alpha(\dots)}{\dots}$ (print writes
  „$2ra\cdot\cos\alpha$" in the $dw$-form denominator — preserved). p.84: the three
  integration limits $\int_0^{2\pi}$ (Θ), $\int_0^{\pi}$ (α), $\int_0^{r}$ (r); the
  final **triple integral** $kp\iiint\frac{r^2\sin\Theta dr d\Theta d\alpha(a-r\cos
  \alpha)}{(r^2+a^2-2ra\cos\alpha)^{3/2}}$; and the closing sentence. „Man vil altsaa"
  join across the p.82/83 break handled. Portable compile clean: **69 pp., 0/0/0, 0
  markers** — Phase 1 done.
- **Body batch 23 (2026-07-06): printed pp. 80--82 done & image-verified.**
  Still in **c) Integralets Bestemmelse**. p.80: the **parabola** area worked example
  ($y^2=px$): $\int y\,dx=\sqrt{p}\int\sqrt{x}\cdot dx=\dots=\frac{2yx}{3}$, Segmentet
  $ACB=\frac{2yx}{3}-\frac{yx}{2}=\frac16xy$, Arealet $ADBCA=xy-\frac23xy=\frac13xy=
  2\times$ Segmentet $ACB$; **FIGURE #15** (printed p.80): parabola $y^2=px$ in
  rectangle $DBEA$ (vertex $A$), upper arc $A$--$C$--$B$, lower branch $A$--$H$, chord
  $A$--$B$, dashed $G$--$F$--$H$; $AE=x$, $EB=y$, $GFH=p$ (schematic redraw via
  `\draw plot`). TWO footnotes anchored on p.80: `*)` (Arealet $ABCE=\frac23xy$…
  Parablen kan qvadreres under endelig Form) set via `\footnotemark`/`\footnotetext`
  from inside the display (mark wrapped as `\text{\footnotemark}`); `**)` (the big
  „Læren om Constanten…" materialism footnote, Ramus refs, spanning pp.80--81) set as a
  normal `\footnote`. p.81: the mechanics **Exempel** — $v=\frac{dx}{dt}$,
  $\varphi=\frac{d^2x}{dt^2}$; case 1) constant velocity $x=at+b$; case 2) constant
  force $x=\frac12kt^2+ct+d$ (print writes „$\frac{d^2x}{dt}=kdt$" and „$dx=d\cdot at
  +db$" — preserved as printed). p.82: the area-under-a-line constant-of-integration
  argument; **FIGURE #16** (printed p.82): right triangle $O$,$D$,$B$ with inscribed
  Riemann strips $d$--$D$, point $b$ over $d$; $OD=x$, $BD=y$, $Od=x'=bd=y'$;
  $OBD-Obd=bdBD=\int_0^x-\int_0^{x'}=\int_{x'}^x y\,dx=f(x)-f(x')$; ends mid-sentence
  „…idet $C=-f(x')$. Man" →p.83. Print oddity preserved: „$=f(x')-f(x')=f(x')+C=0$".
  Portable compile clean: 68 pp., 0/0/0, 1 marker (batch 24); all 3 pages + both
  figures spot-checked rendered.
- **Body batch 22 (2026-07-06): printed pp. 77--79 done & image-verified.**
  Still in **c) Integralets Bestemmelse**. p.77: the „krum Linie"/Bevægelse
  philosophy; then the arc-length setup — **FIGURE #12** (printed p.77): the
  differential triangle (right angle at $C$, $CA=dy$, $CB=dx$, hypotenuse $AB=ds$ on
  a curve through $A,B$; caption „$A=ds$, den uendelig lille Sector"), the display
  $ds^2=dx^2+dy^2;\ ds^2=dx^2(1+\frac{dy^2}{dx^2});\ \frac{ds}{dx}=\sqrt{1+(\frac{dy}
  {dx})^2}$, the curve-list ($\sqrt{a^2-x^2}$ Cirklen, $\frac{b}{a}\sqrt{a^2-x^2}$
  Ellipsen, $\frac{b}{a}\sqrt{x^2-a^2}$ Hyperblen, $\sqrt{x}\sqrt{.\,p}$ Parablen —
  **print oddity**: a dot set inside the second radical „√x √.p", flagged; it means
  $\sqrt{x}\sqrt{p}$) with footnote „Ifr. Ramus. Analytisk Geometrie. S.13--23", and
  the ellipse reduction $\frac{ds}{dx}=\sqrt{\frac{a^4+(b^2-a^2)x^2}{a^2(a^2-x^2)}}$.
  p.78: $ds=dx\sqrt{\frac{a^4+(b^2-a^2)x^2}{a^4-a^2x^2}}$ and the quadrature integral
  $s=\int_0^{x=a}dx\sqrt{\dots}$ (upper limit printed „$x=a$") with the Qvadratur
  footnote (Ramus S.112--125); then $\int y\,dx=A$ as Areal-formel and **1) Exempel**
  (rectangle) — **FIGURE #13** (printed p.78): rectangle $B,C$ top / $A,D$ bottom,
  $AD=x$, $DC=y$, $AB=a$; display $\int y\,dx=\int a\,dx=adx+adx+adx+\dots$. p.79:
  finishes the rectangle ($\int a\,dx=a\int dx=ax$: Rectanglet $=$ Grundlinie $\times$
  Høide) and **2) Exempel** (triangle) — **FIGURE #14** (printed p.79): right triangle
  $A$(angle $\alpha$)$,C,B$ with inscribed step-rectangles, $AC=x$, $CB=y$;
  $y=\operatorname{tg}\alpha\,x$, and $\operatorname{tg}\alpha\int x\,dx=
  \operatorname{tg}\alpha\frac{x^2}{2}=y\frac{x}{2}$ ⇒ Trekantens Areal $=$ Grundlinien
  $\times\frac12$ Høide. Used `\operatorname{tg}` for tangent, `\alpha` macro (portable).
  Portable compile clean: 65 pp., 0 errors, 0 char-warnings, 0 undefined cs, 1 marker
  (batch 23); all three pages + figures spot-checked rendered.
- **Body batch 21 (2026-07-06): printed p.74 (c) heading + pp.74--76 footnote done
  & image-verified.** Added the sub-subsection heading **c) Integralets Bestemmelse**
  (centred bold + `\phantomsection` + `\addcontentsline{toc}{subsubsection}`) carrying
  a **3-page footnote** (set via `\footnotemark`/`\footnotetext`; LaTeX auto-splits it
  across output pages, verified). Footnote = Ramus quote („Der gives ingen almindelig
  Methode til at finde $\int X\,dx$ udtrykt under endelig Form…"; Ramus S.36) + the
  integration catalogue: $\int aX\,dx=a\int X\,dx$, the sin/cos integrals, integration
  by parts $\int f\,d\Phi=f\Phi-\int\Phi\,df$, and the partial-fraction worked example
  $\frac{1}{x^2-7x+12}=\frac{1}{x-4}-\frac{1}{x-3}$ with $k_1=1,k_2=-1$ (Ramus S.37).
  **Print oddity flagged**: the general form's first term prints „$\frac{k_1}{x\,
  \alpha_1}$" with NO minus (cf. „$x-\alpha_2$"); preserved. Main text (pp.74--76):
  the Differential/Integral = Negative/Positive Punkt→Linie→Flade→Legeme passage, the
  ponerende/negerende Virksomhed, brudt vs. krum Linie — ends „…men en gjennem to
  Momen-" →p.77. Portable compile clean: 62 pp., 0/0/0.
- **Body batch 20 (2026-07-06): printed pp. 73--74 done & image-verified.**
  Still in **3) Integralet / b) Integration**. p.73: the ellipse tangent limits
  $\frac{dy}{dx}=-\frac{b}{a}\frac{0}{\sqrt{a^2-0}}=0$ (x=0) and
  $=-\frac{b}{a}\frac{a}{\sqrt{a^2-a^2}}=-\frac{ba}{\sqrt0}=-\frac{ba}{0}=\infty$ (x=a),
  the latter carrying footnote „Til AB … svarer en Tangens $=\infty$" (set via
  `\footnotemark`/`\footnotetext` since the anchor sits inside a display). Then the
  directe/omvendte Tangentmethode recap ($\frac{dy}{dx}=\frac{d\,f(x)}{dx}$), and
  **1) Exempel** ($\frac{dy}{dx}=\frac{r-x}{\sqrt{2rx-x^2}}=f'(x)$, the Cirkel) whose
  sentence „Opgaven … er, at finde…" is **interrupted in the print** by the reduction
  display $\int_0^x 2x\,dx=\mathrm{Lim}2\frac{x^2}{n^2}(1+2+\dots)=\dots=x^2$
  („Grændsen er overskreden") — placed in physical order with a `% flag`. p.74:
  finishes the Cirkel ($\int f'(x)dx=f(x)=\pm\sqrt{2rx-x^2}$); **2) Exempel** the
  ellipse ($\int f'(x)dx=\frac{b}{a}\sqrt{a^2-x^2}=f(x)$); the Potens integration/
  differentiation contrast ending in the power rule $\int x^m dx=\frac{x^{m+1}}{m+1}+C$
  — whose derivation display **breaks mid-expression in the print** (ends „$=\int
  x^{n-1}$", orphaned „$dx$" starts next text line; preserved with a `% flag`).
  Batch stopped deliberately at „Men hvad betyder nu $C$…" — the next heading
  **c) Integralets Bestemmelse** has a pp.74–76 footnote left for batch 21. Portable
  compile clean: 61 pp., 0 errors, 0 char-warnings, 0 undefined cs, 1 marker
  (batch 21); pp.73–74 + the footnote page spot-checked rendered.
- **Body batch 19 (2026-07-05): printed pp. 70--72 done & image-verified.**
  Sub-subsection **b) Integration** (heading centred bold + `\phantomsection` +
  `\addcontentsline`). p.70: „$\infty\,dx$" as an indeterminate sum; the geometric
  series $1+\frac12+(\frac12)^2+\dots$; the Cirkel-as-Polygon Forvandling; and the
  projection identity $a = b\cos C + c\cos B$ with the $\cos C$, $\cos B$ Maclaurin
  series. **FIGURE #10** (printed p.70): a circular arc ($m$--$C$--$B$--$n$) with its
  chord $a=CB$ and the triangle $BCD$ (apex $D$, sides $b=CD$, $c=BD$, dashed
  altitude to foot $e$); redrawn in TikZ. p.71: the multi-line reduction
  $a = b(1-\frac{C^2}{1\cdot2}\dots)+c(1-\frac{B^2}{1\cdot2}\dots)=\dots=b+c-\frac{bC^2}
  {1\cdot2}-\frac{cB^2}{1\cdot2}$ (an `aligned` block; second-order terms vanish ⇒
  $a=b+c$); the arc/chord $CB<b+c$, $>a$ argument; then the „Integration = omvendt
  Differentiation" paragraph carrying a **big footnote** (Ramus. Differ. Integr. S.
  34 quote + the Euler integral $x^{-a_m-1}\int_0^x s_{n,m}\,x^{a_m}dx=s_{n,m-1}$,
  Ramus S. 308). p.72: Leibnitz aside; the circle recap
  $\frac{dy}{dx}=\frac{r-x}{\sqrt{2rx-x^2}}$; then the **ellipse** example
  $y=\frac{b}{a}\sqrt{a^2-x^2}$, derivative $-\frac{b}{a}\frac{x}{\sqrt{a^2-x^2}}$;
  ends mid-sentence („…befindes da at være … hvor-" →p.73). **FIGURE #11** (printed
  p.72): ellipse centred at $C$, semi-axes $CD=a$ (horizontal) and $CE=b$ (vertical),
  point $B$($x,y$) with reflection $B'$ and top-left $A$; redrawn in TikZ. „$\int$"
  via `\int`; lower limit set 0. Portable compile clean: 59 pp., 0 errors,
  0 char-warnings, 0 undefined cs, 1 marker (batch 20); all three pages spot-checked
  rendered (both figures, the aligned reduction, the Euler-integral footnote).
- **Body batch 18 (2026-07-05): printed pp. 67--69 done & image-verified.**
  Sub-subsection **a) Summation** (heading centred bold + `\phantomsection` +
  `\addcontentsline`). p.67: the „Tak/Utak" analogy; $\int dx = x$; and
  $\int dx = \infty\cdot0 = \frac{1}{0}\cdot0 = \frac{0}{0}$. p.68: $dx$ determinate
  only in a ratio; **FIGURES #? (two, side by side is NOT used here — stacked)**:
  the right triangle $ABC$ (equal $dy$, straight line) with $BC=y=dy+dy+\dots$,
  $AC=x=dx+dx+\dots$ and $\angle BAC=45^\circ\Rightarrow\frac{dy}{dx}=\frac00=1$; and
  the two-curve figure $AA'B$/$AA''B$ (unequal $dy$) with $y=dy+dy'+dy''+dy'''+\dots$
  — both redrawn in TikZ (staircase grids). Print notation „$dy=dy^{1}$" kept as
  printed. p.69: the „$0=0$/Intet=Intet" discussion; then the **telescoping-sum
  array** $f(a+2dx)-f(a+dx)=f'(a+dx)dx$, …, with a dotted omitted-rows row
  (`\hdotsfor`) and a summation rule (`\hline`), giving by addition
  $f(a+ndx)-f(a)=f'(a)dx+\dots f'(a+(n-1)dx)dx$; then $n=\infty$, $a+ndx=b$; ends
  „…har gjort dette Spring," (→p.70). Portable compile clean: 56 pp., 0 errors,
  0 char-warnings, 0 undefined cs; pp.67--69 spot-checked rendered (the two p.68
  figures, the ∫ equations, the telescoping array).
- **Body batch 17 (2026-07-05): printed pp. 64--66 done & image-verified.**
  Finishes sub-subsection **c)** and opens subsection **3) Integralet**. p.64: the
  Maximum condition $\frac{dy}{dx}=\pm\frac{r-x}{\sqrt{2rx-x^{2}}}=0$ at $x=r$, and
  $\frac{d^{2}y}{dx^{2}}$ reducing to $\mp\frac1r$; then the Tangent/Secant
  discussion. **FIGURES #8 and #9** (printed p.64, drawn side by side in one centred
  block): (A) the arch (upper half-circle) with vertical chords $Bm$/$CM$/$Dm'$,
  horizontal tangent at $M$ and inclined dashed tangents at $m,m'$ meeting the axis
  at $\alpha,\alpha'$; (B) the secant $O$--$o$ (angle $v$) and tangent at $o$ (angle
  $\alpha$) on a hump curve, with the right triangle legs $h$ (horizontal) and $k$
  (vertical), $\frac{k}{h}=\operatorname{tg}v$ — both redrawn in TikZ; caption
  „$OP=x$; $oP=y$; Punktet $(x,y)=o$." centred below. p.65: the tangent-limit
  $\lim\frac{k}{h}=\frac{dy}{dx}=\operatorname{tg}\alpha$; the sign-change of
  $\operatorname{tg}\alpha$ at the maximum; $\frac{d^{2}y}{dx^{2}}=\frac{d\,
  \operatorname{tg}\alpha}{dx}$ negative at a max; then the **3) Integralet**
  subsection heading (centred bold + `\phantomsection` + `\addcontentsline`) and its
  Positivt/Negativt (Punkt/Linie/Flade/Legeme) opening. p.66: pure prose — the
  Discretion/Continuitet dichotomy and the „Linie som uendelig mange Ikke-Linier"
  divisibility paradox; ends mid-sentence („…som at tænke" →p.67). `tg`/`cot`
  rendered `\operatorname{tg}` etc. (matching earlier batches); „$x$nes Axe" kept.
  Portable compile clean: 53 pp., 0 errors, 0 char-warnings, 0 undefined cs, 1 marker
  (batch 18); pp.64--66 spot-checked rendered (both figures side by side, the
  $\operatorname{tg}\alpha$ derivative display, the prose page — all within margin).
- **Body batch 16 (2026-07-05): printed pp. 61--63 done & image-verified.**
  Continues sub-subsection **c) Differentialcoefficienternes indbyrdes Forhold**.
  p.61: the false conclusion $\frac{d^{3}y}{dx^{3}}=(\frac23)^{3}$; the order-of-
  differential discussion ($dx^{2}=dx\cdot dx$ vs. $d^{2}y=d\cdot dy$; why $f''\neq
  (f')^{2}$); and the **rational-mechanics example** — velocity $v=\frac{dx}{dt}$,
  force $\varphi=\frac{dv}{dt}=\frac{d^{2}x/dt}{dt}=\frac{d^{2}x}{dt^{2}}$ (2nd
  differential coefficient = acceleration/force). p.62: the **Maximum/Minimum
  example** — the $f(x\pm h)$ Taylor pair, the sign argument giving $\frac{dy}{dx}
  =0$ with $\frac{d^{2}y}{dx^{2}}$ negative (max) / positive (min), and the circle
  set-up $y=\pm\sqrt{2rx-x^{2}}$. **FIGURE #7** (printed p.62): circle with
  horizontal diameter $O$--$O'$ ($=2r$) on the $x$-axis, $y$-axis through $O$, three
  vertical chords $Bm$/$CM$/$Dm'$ (M at top = Maximum); redrawn in TikZ as a centred
  block. p.63: the $\frac{dy}{dx}$ and $\frac{d^{2}y}{dx^{2}}$ for the circle, plus
  an **enormous single footnote** (the full quotient-/power-rule differentiation of
  $\pm\sqrt{2rx-x^{2}}$: $d\sqrt{x}$ rule, $d(y\pm z)$, $d(y/z)=\frac{z\,dy-y\,dz}
  {z^{2}}$, ending in $\frac{d^{2}y}{dx^{2}}$) — attached via
  `\footnotemark`/`\footnotetext` because the anchor sits in a display; nested
  radicals set with `\dfrac`/`\tfrac` throughout, compiles clean. Ends mid-sentence
  („…de anførte Værdier udtrykke" →p.64). Comma-as-separator „$(\frac23)^{2}$,
  $\frac{d^{3}y}{dx^{3}}$" preserved. Portable compile clean: 51 pp., 0 errors,
  0 char-warnings, 0 undefined cs, 1 marker (batch 17); all three pages spot-checked
  rendered (mechanics fractions, the circle figure, the giant $\sqrt{2rx-x^{2}}$
  footnote — all within margin).
- **Body batch 15 (2026-07-05): printed pp. 58--60 done & image-verified.**
  Finishes sub-subsection **b) Differentiation** and adds **c)
  Differentialcoefficienternes indbyrdes Forhold** (heading centred bold +
  `\addcontentsline{toc}{subsubsection}`). p.58: the Rækker enumeration continues
  ($a^{x+h}$, $\log(x+h)$, $\sin(x+h)$, $\cos(x+h)$ displays), then the „første
  Differentialcoefficient" list $\frac{d.x^{n}}{dx}=nx^{x-1}$, $\frac{d.a^{x}}{dx}
  =(la)a^{x}$, $\frac{d.\log x}{dx}=\frac{\log e}{x}$, $\frac{d.\sin x}{dx}=\cos x$,
  $\frac{d.\cos x}{dx}=-\sin x$, and the „0/0"-coefficient reflection. **Print
  oddity preserved + flagged:** $\frac{d.x^{n}}{dx}=nx^{x-1}$ — exponent set $x-1$
  (should be $n-1$). One footnote here (sin/cos expansions „Ved i hver Række…").
  p.59: main text is short („Hvor eiendommelig Tankeretningen…"); the page is
  dominated by TWO big footnotes — (\*) the compound-differentiation note with six
  rules I)--VI) (product $d.yz=ydz+zdy$, quotient
  $F'(x)=\frac{\varphi f'-f\varphi'}{\varphi^{2}}$, chain
  $\frac{dy}{dx}=\frac{dy}{dz}\frac{dz}{dx}$, inverse $f_{1}$), and (\*\*) the
  rectangle note that continues onto p.60. p.60: sub-subsection **c)** heading, the
  Række with $\frac{dy}{dx}$-coefficients vs. the same with „$\frac{0}{0}$"
  Betegnelse, and „Lad Qvotienten $\frac{dy}{dx}=\frac{0}{0}$…"; ends mid-sentence
  at „…at $\frac{d^{2}y}{dx^{2}}=\frac{0^{2}}{0^{2}}$" (→p.61). **FIGURE #6**
  (printed p.60): rectangle $ABCD$ (area $yz$) enlarged by $dy$ leftward and $dz$
  upward to the dashed outer rectangle $e$--$D$--$d$--$e'$; redrawn in TikZ and
  embedded inside footnote (\*\*), compiles cleanly. Print oddity flagged: the
  figure's first label set „$D = BC = ad = y$" (lone $D$; almost certainly $DA$).
  Function subscripts $f_{1},f_{2}$ kept as printed. Portable compile clean: 49 pp.,
  0 errors, 0 char-warnings, 0 undefined cs, 1 marker (batch 16); all three pages
  spot-checked rendered (derivative list, both giant footnotes, the rectangle
  figure inside its footnote, the 0/0-Betegnelse display — all within margin).
- **Body batch 14 (2026-07-05): printed pp. 55--57 done & image-verified.**
  Sub-subsections **a) Functionsgrændsen og Differentialcoefficienten** and **b)
  Differentiation** (both centred bold + `\addcontentsline{toc}{subsubsection}`).
  p.55: the $f(x)=x^{2}$ worked example ($k=2xh+h^{2}$), the „$dx$/$dy$ baade Noget
  og Intet" definition, $\frac{dy}{dx}=\frac{0}{0}$ as a determinate ratio, and the
  Taylor-derived difference quotient. p.56: the limit
  $\lim\frac{f(x+h)-f(x)}{h}=\frac{dy}{dx}=f'(x)$; the $x^{2}\!\to\!2x$ check; then
  b) Differentiation with $k'=d\cdot\frac{dy}{dx}$ (heading carries a footnote,
  „Ramus. Algbr. F. S. 99--108"). p.57: the higher differential coefficients
  $\frac{d^{2}y}{dx^{2}},\dots,\frac{d^{n}y}{dx^{n}}=f^{n}(x)$, the Taylor series in
  $\frac{d^{k}y}{dx^{k}}$ notation, the Ramus quote (footnote „S. 102"), and the
  $(x+h)^{n}$ Række with a big **gather\*** footnote („Man har nemlig:" — the four
  parallel expansions). **Print oddity preserved + flagged:** on p.57
  $\frac{d^{3}y}{dx^{3}}=f''''(x)$ is set with FOUR primes (should be $f'''$); the
  adjacent „$d^{3}y=f'''(x)\,dx^{3}$" has the correct three. Differentials rendered
  $dx,dy,\frac{dy}{dx}$; „lim" as `\lim`. Portable compile clean: 46 pp., 0 errors,
  0 char-warnings, 0 undefined cs; pp.55--57 spot-checked rendered (limit chains,
  compound $\frac{d\cdot dy/dx}{dx}$ fractions, Taylor series, gather\* footnote —
  all within margin).
- **Body batch 13 (2026-07-05): printed pp. 52--54 done & image-verified.**
  Resolves the $0/0$ indeterminate form and opens subsection **2) Differentialet**.
  p.52: the reduced quotient $f(a+h)=h^{\alpha_1-\beta_1}\frac{A_1+A_2h^{\alpha_2-
  \alpha_1}+\dots}{B_1+B_2h^{\beta_2-\beta_1}+\dots}$; at $h=0$,
  $f(a)=0^{\alpha_1-\beta_1}\frac{A_1}{B_1}$ (footnote „Ramus. Differential- og
  Integralregning 1844. S. 12--13." — anchored to „faaer man"); the three cases
  I) $\alpha_1>\beta_1$ ⇒ $=0$, II) $\alpha_1<\beta_1$ ⇒ $=\infty$, III) $\alpha_1=
  \beta_1$ ⇒ $=A_1/B_1$ (set as an `align*` block, matching the print's stacked
  layout); the „$h^{\alpha_1-\beta_1}=0^{\alpha_1-\beta_1}$ … i Begrebet exact, som
  Ligningen $A=A$" argument. Then the **2) Differentialet** subsection heading
  (centred bold + `\addcontentsline{toc}{subsection}`) and its opening. p.53: the
  Spring/Tilnærmelse discussion, the $\pi$-decimals aside, and the
  $a=a$/$a-a=0$ positiv-vs-negativ-Dom logic, closing with
  $\frac{1}{a-a}=\frac1a+\frac1a+\dots$ vs. $\frac{1}{a-a}=\frac10=\infty$. p.54:
  the geometric-series identity $\frac{1}{1-\frac12}=1+\frac12+(\frac12)^2+\dots=2$
  (two displays), and the Convergens paragraph with a **big footnote** (Ramus.
  Algebr. F. S. 79--80: the $\mathrm{Lim}\,u_n=0$ necessary- vs. $\mathrm{Lim}\,r_n
  =0$ necessary-and-sufficient convergence criterion, $s_n=u_0+u_1+\dots+u_n$).
  Ends mid-sentence at „…hvori det Endelige enes med det Uendelige" (→p.55). No
  figures. `n^{1}` notation kept as in earlier batches. Portable compile clean:
  44 pp., 0 errors, 0 char-warnings, 0 undefined cs, 1 marker (batch 14);
  pp.52--54 spot-checked rendered (three-case align\* block, both geometric-series
  displays, convergence footnote — all within margin).
- **Body batch 12 (2026-07-05): printed pp. 49--51 done & image-verified.**
  The $0/\infty$-relativity core of Section III: „Størrelsen $1{,}000{,}000$
  forestiller for et Øieblik $\infty$" and the six worked fractions set as a
  `gather*` block ($\frac{1{,}000{,}000}{1{,}000{,}000}=\frac\infty\infty=1$, the
  reciprocal $\frac00=1$, the squared/cubed pairs down to $0^2$); the „Indvending"
  that $1{,}000{,}000$ is infinitely far from $\infty$ („betyder Intet"); the „gode
  Guder nedstegne i Endeligheden" image; the relativity chain „$1=\infty$ / $1=0$ /
  $\infty=0$ / $0=\infty$"; and the setup of the $\frac00$ problem —
  $f(x)=\frac{\varphi(x)}{\psi(x)}$ with $\varphi(a)=\psi(a)=0$, expansions
  $\varphi(a+h)=A_1h^{\alpha_1}+\dots$, $\psi(a+h)=B_1h^{\beta_1}+\dots$, ending
  „Man har da:". Print oddity preserved + flagged: the $\frac{x}{x'}$ prime in the
  denominator (cf. the $\frac xx$ just discussed). No footnotes, no figures. The
  `gather*` 1,000,000 block spot-checked rendered — fits within margins.
- **Body batch 11 (2026-07-05): printed pp. 46--48 done & image-verified.**
  Opens **Section III „Det Uendeliges Analyse"** — new centred Roman heading
  ({\large\bfseries III.} + {\Large\bfseries Det Uendeliges Analyse.} + short
  `\rule`, `\addcontentsline{toc}{section}`, and NEW `\markboth{Det Uendeliges
  Analyse}{Det Uendeliges Analyse}` so the running head changes). Section III
  intro (Tilnærmelse/Uopnaaeligt recap; the programme naming the three tools —
  Functionsgrændsen/\emph{Limiten}, \emph{Differentialet}, \emph{Integralet});
  then subsection **1) Functionsgrændsen** (centred bold heading +
  `\addcontentsline{toc}{subsection}`) with the limit definition
  $\mathrm{Lim}\,f(x)=f(\infty)=c$ and the rational-function examples
  $f(\infty)=a_n/b_n=c$, $f(0)=a/b=c'$ (nested fractions; $c'$ prime kept). No
  figures. Portable compile clean.
  Completes **c) Taylors Række** and all of Section II. The double-expansion in
  Række (II): the $f(\overline{x+k}+h)$ two-variable array with two-index
  coefficients $X_{0,1},X_{0,2},\dots,X_{m,n}$ (rendered as an `aligned` block with
  a `\vdots` row for the omitted middle rows), giving $X_{m,n}h^mk^n =
  X_{m+n}\frac{(m+n)\dots(m+1)}{1\cdot2\dots n}$; the $X_{0,1}=X_1$ /
  $X_{m,1}\leftarrow X_m$ identification; the coefficient recursion
  $X_2=\frac{X_{1,1}}{2}=\frac{f''(x)/1}{2}=\frac{f''(x)}{1\cdot2}$, … ,
  $X_n=\frac{f^{n}(x)}{1\cdot2\dots n}$ (compound fractions, `align*`); then the
  **Taylor series** $f(x+h)=f(x)+f'(x)\frac h1+f''(x)\frac{h^2}{1\cdot2}+\dots$ and
  its **Maclaurin** form $f(x)=f(0)+f'(0)\frac x1+\dots$; and the $a^x$/$e^x$
  recap. Ends Section II at „Maalet … en Analyse af det Uendelige." (next: the
  Section III heading + its preceding centred rule). Two big inline coefficient
  fractions on p.44 were set as displays to avoid margin overflow (the print
  displays them too). No footnotes. Portable compile clean: 37 pp., 0 errors,
  0 char-warnings, 0 undefined cs, 1 marker (batch 11); pp.44--45 spot-checked
  rendered (aligned array, compound-fraction coefficients, Taylor/Maclaurin all
  within margin).
- **Body batch 9 (2026-07-05): printed pp. 41--43 done & image-verified.**
  The Realisme/Idealisme close of the p.40 excursus, then subsection **c) Taylors
  Række** (heading centred bold, p.41) and its lead-in: the „umiddelbar og dog
  uendelig formidlet" thesis, the Kjæde-af-Led / Mellemled discussion, the
  transparency-and-telescope analogy (Skillemuur → Rude → Kikkert), and the
  $A_mA_1=A_{m+1}\frac{m+1}{1}$ / $A_{m+1}=\frac{A_mA_1}{m+1}$ warm-up. Then the
  Taylor setup proper (p.43): $f(x+h)=A_0+A_1(x+h)+\dots$; the rewrite with
  $x$-only coefficients $f(x)+f_1(x)h+f_2(x)h^2+\dots=X_0+X_1h+\dots$; the four
  Betingelser (incl. the symmetry $f(x+\overline{h+k})=f(\overline{x+k}+h)$ using
  \overline groupings); and Række (I). Quote oddity preserved: p.41 „»indre
  Uendelighed"" opens with a guillemet » (U+00BB) and closes with " (U+201D) — set
  thus. No footnotes, no figures. Portable compile clean (see batch-10 line).
- **Body batch 8 (2026-07-05): printed pp. 38--40 done & image-verified.**
  The tail of subsection **b)** — the imaginary-magnitude / negative-logarithm
  excursus (NOT subsection c); c) „Taylors Række" turned out to start on p.41,
  next batch). Body: $\sqrt{-1}$ as „both impossible and yet possible", the
  \textit{diversus respectus} / \textit{possibile est…} logical maxims, and the
  Realisme-vs-System reflections. THREE footnotes, incl. TWO giants: (21) the
  rund Fiirkant / regulært Heptaeder aside; (22) the huge two-page note (pp.39--40)
  answering „1) er $\sqrt{-1}$ en absolut Umulighed?" (the $\times(-1)$-as-rotation
  argument with an **embedded complex-plane figure**, and the ellipse→hyperbola
  $b=\sqrt{-1}\,b'$ trick) and „2) Ere Logarithmer af negative Størrelser mulige?"
  (the $\sqrt a\sqrt b$ / $(\sqrt{-a})^2$ fallacy, Leibnitz–Bernoulli & Euler–
  d'Alembert history, and the (I)--(IV) $l.a$ vs $l^{1}a$ multi-valued-log
  comparison proving a real $\log(-a)$ impossible). **FIGURE #5** (p.39): a
  coordinate cross (real axis $A$--$B$ with $\pm a$, imaginary axis $C$--$D$ with
  $\pm b$) redrawn in TikZ and placed *inside* footnote 22 via a centred block —
  compiles cleanly. Notation preserved as printed: $l^{1}$, $p^{1}$, $p^{11}$
  (raised „1"/„11"). Every equation crop-verified (the $(\sqrt{-a})^2$ chain and
  the l¹/p¹ formulas zoomed). Portable compile clean: 32 pp., 0 errors,
  0 char-warnings, 0 undefined cs, 1 marker (batch 9); pp.38--40 spot-checked
  rendered (figure-in-footnote centred correctly, all footnote math within margin).
- **Body batch 7 (2026-07-05): printed pp. 35--37 done & image-verified.**
  Subsection **b) Functionernes Vexelforhold** (heading centred bold, p.35):
  System vs. Schema (nominal Definitioner vs. motiverede Begrebsovergange;
  mekanisk Inddeling vs. organisk Leddeling); the transcendent/algebraic boundary
  $a^x=b^y$ → $y=\frac{x\log a}{\log b}$; the exponential expansion in
  $\frac{\log a}{\log e}$ and then in $(l.\,a)$ with base $e$; $e^x$ series; and
  the **Euler-formula derivation** — $e^{x\sqrt{-1}}$ expanded (period-4 powers of
  $\sqrt{-1}$; multline\* display), multiplied through to
  $e^{x\sqrt{-1}}=\cos x+\sqrt{-1}\sin x$ and $x\sqrt{-1}=l.(\cos x+\sqrt{-1}\sin
  x)$. TWO footnotes: the huge $(1+x)^y$ double-expansion note (p.36) and the
  Ramus „trigonometriske Linier … reductibel til Logarithmen" quote (p.37, S.15).
  THREE print oddities preserved + flagged: (i) p.36 fn restates $\log(1+x)$ with
  denominators $1\cdot2,\,1\cdot2\cdot3,\dots$ — differs from the p.33 statement
  ($/2,/3,/4$); (ii) p.36 fn sets the 3rd term of the 2nd expansion as
  „$\log(\frac{1+x}{\log e})^2$" (for $(\frac{\log(1+x)}{\log e})^2$); (iii) p.37
  sin-series 4th term set $x^6$ (should be $x^7$, cf. p.34), and „s n x" typo for
  „sin x". No figures. Portable compile clean: 30 pp., 0 errors, 0 char-warnings,
  0 undefined cs, 1 marker (batch 8); pp.35--37 spot-checked rendered (multline\*
  Euler display breaks cleanly, both a^x displays fit).
- **Body batch 6 (2026-07-05): printed pp. 32--34 done & image-verified.**
  Opens subsection detail with the three programme points (a/b/c) and **a)
  Functionernes Grundformel** (heading centred bold): the universal Grundformel
  $f(x)=A_0+A_1x+A_2x^2+\dots$; the per-function coefficient specialisations
  ($a+x$, $ax$, $x^a$, $a^x$, $\log x$); $\log(1+x)=\log e(x-\frac{x^2}{2}
  +\frac{x^3}{3}-\dots)$; the even/odd $\cos x$/$\sin x$ series and their
  factorial „Udviklingens Resultat" forms. ONE enormous footnote (the ***/fn-18)
  spanning pp.33--34, merged into a single autonumbered \footnote at „Man faaer
  da:" — the full cos/sin coefficient derivation: sign-parity argument, the
  product-to-sum $\cos x\cos z$/$\sin x\sin z$ relations, $A_mA_n=A_{m+n}(\dots)$,
  $B_pB_q=-A_{p+q}(\dots)$, and the closed forms $A_m=(-1)^{m/2}/(1\cdot2\dots m)$,
  $B_p=(-1)^{(p+3)/2}/(1\cdot2\dots p)$ with worked $A_2,A_4,A_6,B_1,B_3,B_5$.
  Plus the two small p.33 footnotes (brudne Exponenter; Ramus S.87--88). The
  $B_pB_q=-A_{p+q}\dots$ subscript is as printed (kept). No figures. All dense
  equations crop-verified line by line (B_p exponent confirmed $(p+3)/2$ not
  $(p+8)/2$). Portable compile clean (see batch-7 line for the combined result).
- **Body batch 5 (2026-07-05): printed pp. 29--31 done & image-verified.**
  The densest stretch so far. Completes the $a^x$-coefficient derivation:
  the coefficient/potens correspondence, the Ligning
  $A_{m+n}\frac{(m+n)(m+n-1)\dots(m+1)}{1\cdot2\dots n}=A_mA_n$, reduction of the
  whole „Vrimmel" of coefficients to the single $A_1$ via
  $A_m=\frac{A_1^m}{1\cdot2\cdot3\dots m}$, the convergent sum
  $a^{1/A_1}=1+\frac11+\frac1{1\cdot2}+\dots$ giving
  $e=2{,}718281828459\dots$ (natural/neperian base), and $A_1=\frac{\log a}{\log e}$.
  FOUR footnotes fully transcribed & rendered (autonumbered \footnote, incl. two
  huge multi-line ones): the binomial-product derivation of the coefficient law;
  the „masked Nul" $\frac{n(n-1)\dots(n-n)}{1\cdot2\dots n(n+2)(n-n+1)}$ warning on
  ubestemte Coefficienters Methode; the full $A_{m+1}=\frac{A_mA_1}{m+1}$
  recursion → $A_1^m$ formula → $e$; and the $\log a/\log e$ note. Subsection
  **3) Functionernes Systematik** heading + intro placed (p.31): Uendelighedsproblem
  as Totalitetsproblem, "indre Uendelighed" = Functionsbegrebet. TWO print
  oddities preserved + flagged: (i) p.30 footnote sets a subscript as $A_nA_1$
  (should be $A_1A_1$); (ii) p.30 footnote sets „$a^x=1=A_1x+\dots$" with the
  stray „$=1=$". No figures, no letterspacing in the batch. Portable compile clean:
  26 pp., 0 errors, 0 char-warnings, 0 undefined cs, 1 marker (batch 6); all three
  rendered pages spot-checked. (Verify recipe now also needs
  `-e 's/\\usepackage\[danish\]{babel}/\\usepackage{babel}/'` — sandbox babel lacks
  danish.)
- **Body batch 4 (2026-07-05): printed pp. 26--28 done & image-verified.**
  (Tighter batch — dense algebra, stopped before the p.29--30 $e$-derivation.)
  Rest of the Asymptote-Læren: the rationalised asymptote gap
  $y_1-y=\frac{b}{a}\bigl(x-\sqrt{x^2-a^2}\bigr)=\frac{b}{a}\cdot
  \frac{a^2}{x+\sqrt{x^2-a^2}}$ (a real but absolutely unattainable approach —
  „Brøken er først 0, naar $x=\infty$"). Subsection **2) Rækker med stigende
  Potenser**: the two power-series paradigms (falling $f(x)=x^n+A_1x^{n-1}+\dots
  =(x-a_1)\dots(x-a_n)=0$; rising $f(x)=A_0+A_1x+A_2x^2+\dots A_nx^m\dots$); the
  geometric progression $a\frac{1}{1-x}=a+ax+ax^2+\dots$ with $x^\infty=\infty$
  ($x>1$) vs. $x^\infty=0$ ($x<1$); and the $f(x)=a^x$ series with first
  coefficient $A_0=1$ fixed. TWO long footnotes fully transcribed & rendered:
  Ramus „ubestemte Coefficienters Methode" (Algbr.\ F.\ S.82, the $A_i=B_i$
  proof) and „Binomialformlen" (Ramus Elmt.\ Algbr.\ S.35 / Algebr.\ Functl.\
  S.85: $(a+b)^2$, $(a+b)^3$, $(p+x)^n=p^n+\frac n1 p^{n-1}x+\dots$). Latin
  „\textit{diversus respectus}" (quoted) 2×. No letterspacing, no figures.
  „Cartesiusses" (double-s genitive) preserved. Ended mid-topic before p.29.
  Portable compile clean: 24 pp., 0 errors, 0 char-warnings, 0 undefined cs,
  1 marker (batch 5); p.26 derivation + p.28 footnotes spot-checked rendered.
- **Body batch 3 (2026-07-05): printed pp. 22--25 done & image-verified.**
  (Tighter batch — the four-figure cluster.) Continues Section II /
  subsection 1): the $\infty$/$0$ as mutual boundaries (dialectical
  boundary-determination); the trig-circle illustration
  ($AB=f_1(x)=\sin x$, $BC=f_2$, $DF=f_3=\operatorname{tg}x$,
  $EG=f_4=\cot x$; behaviour as $x:0^\circ\to90^\circ$; $\angle x=0$ vs.
  $\cot x=\infty$); the „classisk vs. romantisk" (finite-encloses-infinite vs.
  infinite-as-unattainable) analogy; the Tilnærmelse/Uopnaaeligt analysis; and
  the Asymptote-Læren opening with the hyperbola $f(x)=y=\frac{b}{a}\sqrt{x^2-a^2}$.
  **FOUR TikZ figures built & verified against the scan:** p.22 angle $ACB$ with
  dashed subdividing rays; p.23 full trig circle (C,D,E,A,B,F,G + angle x);
  p.24 circle detail (C, D, rays CA & CD′, angle x); p.25 hyperbola branch +
  dashed asymptote (A,B,B′,D,E,D′,E′) with caption „$AB=x;\ BD=y;\ BE=y_1$".
  **ERRATA APPLIED** (p.4 Rettelse): p.25 line 9 now reads „Tilnærmelse til et
  Opnaaeligt" (was „Uopnaaeligt"), flagged in a comment. No letterspacing in the
  batch (classiske/romantiske NOT spaced — crop-checked). No footnotes.
  Ended mid-sentence at „for Hyperblens Asymptote:". Portable compile clean:
  22 pp., 0 errors, 0 char-warnings, 0 undefined cs, 1 marker (batch 4); all
  four figure pages spot-checked in the rendered PDF.
- **Body batch 2 (2026-07-05): printed pp. 13--21 done & image-verified.**
  (Ended at p.21, before the p.22 figure, to group both figures into batch 3.)
  Rest of Section I: the water-tank problem (Ramus, Elementær Algebra S.179) and
  its harmonic fill-formula $x=1/\sum 1/a_i$; Formel vs. Slutning; the Cajus
  syllogism; single vs. mathematical formulas (footnote ends with the elastic-
  collision formula $\frac{MH+mh}{M+m}$); the Grundfunctioner
  $a\log x, a^x, x^a, ax, a+x$; $a+a+a+\dots a=na$ (Latin \textit{diversus
  respectus}); the arithmetic/geometric progressions $\varphi_1,\varphi_2$ and
  the recap formula $=F(\varphi(p))=f(p)$; the symmetric functions —
  $(x-a_1)(x-a_2)\dots$, the general $f(x)=x^n+A_1x^{n-1}+\dots=0$, and the
  coefficient/root laws $A_1, A_3, A_n$ with $f_{1},f_{3},f_{n}$. Then Section
  **II. Uendelighedsproblemet** (p.19), subsection **1) Rækker og trigonometriske
  Functioner** (p.20) with the three series types (arithmetic α, harmonic β,
  geometric γ; $u_n=f_{1,2,3}(n)$), and the $\infty$/$0$ „absolute Negationer"
  discussion. Letterspacing: p.19 \emph{Hvorledes forholder det Endelige sig til
  det Uendelige?} (the only body letterspacing; „det Endelige er det Endelige…"
  on p.21 is quoted, NOT spaced). Footnotes (3): Ramus Elementær Algebra p.13;
  the long „virkelige Love" note p.15; trig-functions note p.16. PRINT ERROR
  preserved + flagged: p.14 second fill-formula sets the 3rd denominator term as
  raised $a^{3}$ (typo for $a_3$). Print oddity flagged: p.18 stray raised „3"
  over „3 og 3 a". Every equation crop-verified. Portable compile clean: 18 pp.,
  0 errors, 0 char-warnings, 0 undefined cs, 1 marker (batch 3); rendered
  formula pages spot-checked (symmetric functions, series, syllogism, fill-formula).
- **Body batch 1 (2026-07-05): printed pp. 3--12 done & image-verified.**
  p.3 opening statement („Nærværende Afhandlings Forfatter…"); p.4 Rettelse
  (recorded, not reproduced); Section **I. Mathematiske Functioner** (p.5)
  through p.12. Covers: the „Function" concept (extra-/intra-mathematical),
  dependent/independent variables, the Ramus definition $y=f(x,z,t,u\ldots)$;
  Regel vs. Lov with the worked identities ($2(3+4)=\dots$, $(3\cdot4)^2=\dots$,
  $2^3\cdot2^4=\dots$) and the prime-number cautionary example
  ($2^{2m-1}-1$; $2^9-1=511=7\cdot73$; Fermat/Euler footnote); the two-column
  numeric→literal substitution block; logarithms; the four Fundamentalligninger
  $f_{1..4}$; inverse functions with $\varphi,\psi$ and roots; the „A er A"
  vs. $A=A$ (logic vs. mathematics) discussion; Stilpon footnote. Letterspacing
  verified: p.7 \emph{at et Forhold er}, \emph{Sagens Væsen} (only two in the
  batch; all other pages crop-checked clean). Footnotes (6): Norden „Gamle
  Minder" p.5; Ramus p.6 & p.9; Fermat/Euler p.8; chemiske Tegnsystemer p.10;
  Stilpon/Poul Møller p.12 — all placed whole at anchors. Every equation
  crop-verified. Portable compile clean: 11 pp., 0 errors, 0 char-warnings,
  0 undefined cs, 1 marker (batch 2); rendered math pages spot-checked.
- **Session (2026-07-05): scaffolded + front matter (title page).**
  `transcription.tex` created: book class; amsmath, graphicx, **tikz**,
  libertinus + libertinust1math, textalpha, fancyhdr, hyperref, microtype.
  Title page reproduced faithfully (main title, subtitle „En propædeutisk
  Afhandling", „R. Nielsen, Professor i Philosophien.", two rules, imprint
  „Kjøbenhavn. / Forlagt af den Gyldendalske Boghandling (F. Hegel). /
  \emph{Thieles Bogtrykkeri.} / 1857.") — image-verified against PDF 6, rendered
  check matches. Portable xelatex/pdflatex verify compile clean: 4 pp., 0 errors,
  0 char-warnings, 1 marker (the body-begins marker).
