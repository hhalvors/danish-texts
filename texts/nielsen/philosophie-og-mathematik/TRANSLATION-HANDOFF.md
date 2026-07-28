# Handoff — translate *Philosophie og Mathematik* (Nielsen, 1857) into English

**For a fresh session.** Phase 1 (Danish transcription) is **complete and
image-verified**. Your job is Phase 2: produce `translation.tex` (English) from the
finished `transcription.tex`. Read this file, then the two standing docs it points to,
then start the batch loop.

---

## 0. Read these first (in order)
1. **This file** — book-specific facts and the one big deviation from the playbook.
2. `../../../TRANSLATION-PLAYBOOK.md` — the standing translation method (batch loop,
   quote/emphasis/footnote conventions, sandbox compile recipe, finishing steps).
3. `RESUME-NOTES.md` (this folder) — the transcription log. Its **"DONE so far"**
   section is a page-by-page content map of the whole book (newest batch first): use
   it to know what's on each printed page before you translate it.

**Standing rule (unchanged): you never `git commit` or `git push` — Hans does that.**
After every batch, say the work is not committed/pushed.

---

## 1. Book facts
- **Folder:** `texts/nielsen/philosophie-og-mathematik/`
- **Source of truth:** `transcription.tex` (Danish, `book` class). Translate FROM it,
  not from the scan. It is final: 69 typeset pages, compiles 0 errors / 0 undefined cs
  / 0 missing-char warnings, no leftover markers.
- **Target:** `translation.tex` (English) — **does not exist yet; you create it** (see §3).
- **Scan (for reference only):** `~/bibliotek/Nielsen, Rasmus/1857phil-math.pdf`
- **Page offset:** PDF = printed + 5. Body = printed pp. 3–84. (You shouldn't need the
  scan — the Danish is verified — but it's there if a term is ambiguous.)
- **Author/register:** R. Nielsen, a *philosopher* writing on the philosophy of the
  infinite and the calculus. The prose is speculative/Hegelian (Tilblivelse, det
  Værende, Negation, ponerende/negerende Virksomhed, Moment) wrapped around real
  analysis. Translate in a scholarly, moderately literal register that keeps that
  philosophical flavor.

### Structure (mirror this 1:1 — headings from the final transcription)
- **I. Mathematiske Functioner** → *Mathematical Functions*
- **II. Uendelighedsproblemet** → *The Problem of Infinity*
  - 1) Rækker og trigonometriske Functioner — 2) Rækker med stigende Potenser —
    3) Functionernes Systematik [a) Functionernes Grundformel, b) Functionernes
    Vexelforhold, c) Taylors Række]
- **III. Det Uendeliges Analyse** → *The Analysis of the Infinite*
  - 1) Functionsgrændsen — 2) Differentialet [a) Functionsgrændsen og
    Differentialcoefficienten, b) Differentiation, c) Differentialcoefficienternes
    indbyrdes Forhold] — 3) Integralet [a) Summation, b) Integration,
    c) Integralets Bestemmelse]

There is no Forord/Indhold/Indledning; the essay opens directly (printed p.3 drop-cap
"Nærværende Afhandlings Forfatter…"). Printed p.4 is an errata page, already applied
(not reproduced). Headings are **not** `\section{}` — they are centered `\textbf{}`
blocks followed by `\phantomsection` + `\addcontentsline{toc}{…}` (+ `\markboth` /
`\texorpdfstring` on the Roman-numeral sections). Copy each heading block from the
transcription and translate only the title text inside; keep the toc/bookmark plumbing.

---

## 2. THE BIG DEVIATION FROM THE PLAYBOOK — this book is math-heavy
The playbook was written for prose books (Brøchner, Høffding). This one has **dense
mathematics and 19 TikZ figures**. So:

- **Translate only natural-language prose**: body sentences, footnote prose, headings,
  and the *words* inside figure captions (e.g. "den uendelig lille Sector" → "the
  infinitely small sector"; "Segmentet ACB" → "The segment $ACB$"; "Arealet" → "The
  area"; "Grundlinien × ½ Høide" → "base × ½ height").
- **Carry over VERBATIM, byte-for-byte** (do not re-typeset, re-derive, or "improve"):
  - every display and inline equation (`\[ … \]`, `$…$`, `gather*`, `align*`);
  - every `tikzpicture` block **and its `% FIGURE (printed p.N): …` comment**;
  - point/label tokens like `$AM = a$`, `$AB = r\cos\alpha$`, `$CD=a$` — these are
    math, not prose; leave them.
  - the four `% flag` comments recording print oddities — **keep them verbatim** so the
    translation preserves the same scholarly apparatus (missing minus in `x α₁`; the
    `√x √.p` parabola dot; the `d²x/dt = kdt` and `f(x')−f(x')=f(x')+C=0` oddities).
- Easiest safe workflow per span: **copy the Danish span, then edit only the prose in
  place**, leaving all math/TikZ untouched. That guarantees equation fidelity.
- Danish decimal/notation quirks already in the math (`\cdot`, `\operatorname{tg}`,
  `\mathrm{Lim}`, Danish `,` etc.) stay as-is.

---

## 3. Create `translation.tex` (no skeleton exists)
Unlike the playbook's books, there's no pre-made marker skeleton here. Build
`translation.tex` **sequentially, mirroring the transcription batch order** (see §5).
Two ways: (a) build straight through, section by section; or (b) first scaffold the
front matter + all heading blocks with `% [text to be added: pp. X--Y]` markers between
them, then fill markers via the playbook's batch loop. Either is fine; (b) makes the
"markers remaining" reporting in the playbook work verbatim.

**Preamble:** copy the transcription's preamble almost exactly (it already has
`amsmath`, `graphicx`, `tikz` + `\usetikzlibrary{calc,intersections,arrows.meta}`,
`libertinus`, `libertinust1math`, `textalpha`, `fancyhdr`, `hyperref`, `microtype`,
`\onehalfspacing`). Changes for the English file:
- `\usepackage[danish]{babel}` → `\usepackage[english]{babel}`
- running head: `\fancyhead[RE]{\textit{Philosophy and Mathematics}}` and translate the
  `\leftmark` section titles (they come from `\markboth`, so translate those).
- `hyperref` `pdftitle={Philosophy and Mathematics}`.
- add `\usepackage{enumitem}` **only if** you introduce `\arabic*)`-style lists (the
  transcription doesn't use them; probably not needed).
- Title page: translate sub-title/role lines ("En propædeutisk Afhandling" → "A
  Propaedeutic Treatise"; "Professor i Philosophien" → "Professor of Philosophy"),
  but keep the author name "R. Nielsen" and it's conventional to keep the imprint
  ("Kjøbenhavn … Gyldendalske Boghandling (F. Hegel), 1857") as printed — match how the
  sibling `texts/nielsen/*/translation.tex` files handle title pages.

Look at a finished sibling for house style, e.g.
`texts/nielsen/videnskabslaere/translation.tex` or
`texts/brochner/problemet-tro-viden/translation.tex` (the playbook's reference book).

---

## 4. Recurring-term glossary (keep consistent across the whole book)
Mathematical:
- Function → function; afledet Function → derived function; oprindelig Function →
  original function; omvendt → inverse
- Functionsgrændse → function-limit (the limit of the function); Grændse → limit;
  "Grændsen er overskreden" → "the limit is transgressed"
- Differentialcoefficient → differential coefficient; Differential → differential
- Række → series; stigende Potenser → increasing powers; Grundformel → fundamental
  formula; Vexelforhold → reciprocal relation (interrelation)
- Integral / Integration / Summation / Integralets Bestemmelse → the determination of
  the integral; arbitrær Constant → arbitrary constant
- Curve → curve; Ligning → equation; Tangent → tangent; den directe/omvendte
  Tangentmethode → the direct / inverse tangent method
- Keglesnitslinier → conic sections; Cirkel/Ellipse/Hyperbel/Parabel →
  circle/ellipse/hyperbola/parabola; Grundlinie → base; Høide → height
- Qvadratur → quadrature; Rectification → rectification; Reduction → reduction
- Vægtfylde → density; Volumen → volume; Kraft → force; Masse → mass; Kugleskal →
  spherical shell; Kuglemasse → mass of the sphere; Tiltrækning → attraction
- Vinkel → angle; Radius → radius; Rectangel → rectangle; Trekant → triangle

Philosophical:
- det Uendelige / det Endelige → the Infinite / the Finite
- Tilblivelse → coming-into-being (becoming); det Tilblevne → that which has come to be;
  det Værende → that which is (Being); det Ikke-Værende → the Not-Being
- Bevægelse → motion; Moment → moment; ponerende/negerende Virksomhed → positing /
  negating activity; Deling → division; Sammensætning → composition; Sammenstykning →
  piecing-together
- Continuitet → continuity; Discretion → discreteness; Forandring → change

**Keep unchanged:** proper names (Ramus, Euler, Leibnitz, Taylor, Newton) and Danish
work-title citations in footnotes (e.g. "Ramus. Differential- og Integral-Rgn. S. 36",
"Ramus. Analytisk Geometrie. S. 13—23") — leave those Danish titles/refs verbatim.
Quotes: Danish „…" → English ``…''. Letterspaced emphasis is `\emph{}` in the
transcription → keep `\emph{}`.

---

## 5. Batch plan (mirror the transcription's 24 body batches)
Work in ~coherent chunks; the transcription's natural seams (matching RESUME-NOTES
"DONE so far") are a good batching guide:
front matter → I (pp.3–~12) → II.1 → II.2 → II.3 a/b/c → III.1 → III.2 a/b/c → III.3
a/b/c. Roughly pp.3–12, 13–22, 22–31, 32–45, 46–57, 58–69, 70–79, 80–84 gives ~8–10
translation batches at ~10 printed pages each. Use TaskCreate/TaskUpdate per batch.

Per batch: translate the prose (carry math/figures verbatim, §2) → sandbox compile
(§6) → 2–4 sentence report (section, page range, notable choices, page count + 0/0,
markers remaining) → hand back.

---

## 6. Sandbox compile recipe (English file)
Same idea as the transcription's portable check. The sandbox lacks `libertinus`,
`libertinust1math`, `textalpha`, and the Danish babel option; substitute for the check
only (never put substitutions in the real file). Greek `α β γ` appear as LaTeX macros
`\alpha …` in the math and as literal glyphs nowhere critical, but strip textalpha and
map any literal α/β/γ → a/b/g just as the transcription check did:

```bash
cd /tmp && mkdir -p vt && cd vt
SRC="$(ls -d /sessions/*/mnt)/danish-texts/texts/nielsen/philosophie-og-mathematik/translation.tex"
sed -e 's/\\usepackage{libertinus}//' -e 's/\\usepackage{libertinust1math}//' \
    -e 's/\\usepackage{textalpha}//' \
    -e 's/\\usepackage\[english\]{babel}/\\usepackage{babel}/' \
    -e 's/α/a/g' -e 's/β/b/g' -e 's/γ/g/g' "$SRC" > t.tex
perl -0pi -e 's/(\\documentclass\[[^\]]*\]\{book\})/$1\n\\usepackage{lmodern}/' t.tex
pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1
pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1
grep -o 'Output written.*' l.txt
echo -n "errors: ";  grep -c '^!' l.txt || true
echo -n "undef cs: "; grep -c 'Undefined control sequence' l.txt || true
echo -n "missing char: "; grep -c 'Missing character' l.txt || true
echo -n "markers left: "; grep -c 'text to be added' "$SRC" || true
```
Expect 0 / 0 / 0. On Hans's real machine the file compiles with libertinus +
libertinust1math + textalpha. Spot-check rendered pages against the transcription PDF
so equations/figures line up (they should, since you copied them).

---

## 7. Finishing
When `grep -c 'text to be added'` (and any `translation continues`) return 0:
1. Final sandbox compile → confirm page count, 0/0/0.
2. In the repo's `catalog.yaml`, set this book's `status:` to reflect translation
   complete (check how sibling entries are marked).
3. Tell Hans to compile both PDFs locally with the real fonts and confirm the
   Transcription + Translation links resolve.
4. Hans commits/pushes. You don't.

That's the whole job: read the playbook + RESUME-NOTES, create `translation.tex` from
the transcription's preamble, and translate prose-only span by span with every equation
and TikZ figure carried over verbatim.
