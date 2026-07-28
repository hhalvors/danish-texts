# Rasmus Nielsen — *Philosophiske Grundproblemer* (1879): translation instructions

You are translating this book from Danish into English. **Read the standing
method first:** `../../../TRANSLATION-PLAYBOOK.md` (Danish→English translation
playbook). This file is the **book-specific** companion to it — it records
everything particular to *Philosophiske Grundproblemer* and overrides the
playbook only where noted.

**Standing rule (non-negotiable): Hans commits and pushes. You never do.**

---

## 0. State of this book

- **Source of truth:** `transcription.tex` (Danish) — **COMPLETE**, all 77 pp.,
  verified against the color scan, compiles 0 errors / 0 char-warnings.
  Translate FROM this file, not from the PDF scan.
- **`translation.tex`: does not exist yet.** Your first job is to create it from
  scratch (preamble in §3, structure in §4), then fill it in batches.
- Page-offset: **PDF page = printed page + 9** (verified).
- Scan (reference only): `~/bibliotek/Nielsen, Rasmus/philosophiske-grundproblemer-color.pdf` (91 pp.).
- The transcription is an **`article`-class** file (not `book`) — a single
  continuous essay with three numbered top-level sections and no chapters. The
  translation mirrors that: `article` class, `\section*{}` headings.

---

## 1. Structure to mirror 1:1

The whole work is one essay. Verified structure (from the transcription header):

- **[Introduction, untitled]** — pp. 3–4 (p. 1 title, p. 2 blank).
- **I. Erkjendelsesproblemet** — pp. 4–26. Heading sits at the foot of p. 4.
  → *The Problem of Knowledge* (or *of Cognition*).
- **II. Realitetsproblemet** — pp. 27–50.
  → *The Problem of Reality*.
- **III. De ueensartede Principers Problem** — pp. 50–77. Heading on p. 50.
  → *The Problem of the Heterogeneous Principles* (see §5 on "ueensartet").

There are **only three numbered sections.** The soul–body discussion, the
problem of freedom, and the whole *Tro og Viden* (Faith and Knowledge)
discussion all fall **within Section III** — they are *not* separate sections.
(An earlier scaffold once guessed a "III. Frihed, Sjæl og Legeme" and a fourth
"Tro og Viden" section; both were wrong. Don't reintroduce them.)

Headings in the Danish are `\section*{I.\ Erkjendelsesproblemet}` etc.
(unnumbered star form, with the roman numeral typed in). Mirror that:
`\section*{I.\ The Problem of Knowledge}`, and keep a `\label{}` on each if you
add one, so structure maps 1:1.

**Key passage — get it exactly right (p. 72):** "Principerne for Tro og Viden
ere absolut ueensartede" → *"the principles of Faith and Knowledge are
absolutely heterogeneous."* This is the most explicit popular statement of the
book's central thesis; it is immediately followed by the claim that the
dualistic separation is itself the *condition for a reconciling unity*. The
closing sentence (p. 77) makes the same point: "ogsaa om Tro og Viden gjælder
det, at modsatte Poler tiltrække hinanden" → *"of Faith and Knowledge too it
holds that opposite poles attract one another."* Translate both with care.

---

## 2. Batch loop

Work in **~10-printed-page batches** (so ~8 batches for the 77 pp.). For each:

1. Pick the next `% [text to be added: pp. X--Y]` marker in `translation.tex`
   (you'll create these when you scaffold the file — see §4).
2. Find the matching Danish span in `transcription.tex`. The transcription has
   `% p. N` comments on every page boundary — use them to locate the span
   precisely, and put the **same `% p. N` comments** in the translation at the
   corresponding points so the two files stay aligned.
3. Translate the span (conventions: playbook §2 + §5 below). Replace the marker
   with the Edit tool; leave a fresh marker at a clean paragraph boundary if you
   stop mid-section.
4. Compile with the sandbox recipe (playbook §3). Expect **0 errors,
   0 char-warnings, page count sane**.
5. Short report: section, page range, notable choices, compile result (pages +
   0/0), markers remaining. Then stop.

Use the task list (TaskCreate/TaskUpdate) — one task per batch renders as a
progress widget for Hans.

---

## 3. Preamble for `translation.tex`

Mirror the transcription's preamble but in English and with `lmodern`-friendly
choices. Start from this (matches the house style used in the Nielsen
`darwinismen` translation, adapted to this book's `textalpha` + fancy headers):

```latex
% ============================================================
%  Rasmus Nielsen, Philosophiske Grundproblemer (Philosophical Fundamental Problems)
%  Festskrift, University of Copenhagen 400th-anniversary, June 1879. 77 pp.
%  TRANSLATION (English)
% ============================================================
\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{libertinus}
\usepackage{libertinust1math}
\usepackage{textalpha}          % polytonic Greek typed directly (kept verbatim)
\usepackage[english]{babel}
\usepackage{enumitem}           % keep even if unused now — cheap insurance
\usepackage[protrusion=true,expansion=true]{microtype}
\usepackage[margin=1.4in]{geometry}
\usepackage{setspace}
\usepackage{fancyhdr}
\usepackage[colorlinks=true,linkcolor=black,urlcolor=black,
  pdftitle={Philosophical Fundamental Problems},
  pdfauthor={Rasmus Nielsen}]{hyperref}
\setlength{\headheight}{15pt}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\textit{Philosophical Fundamental Problems}}
\fancyhead[LO]{\textit{\rightmark}}
\setlength{\parindent}{1.5em}
\setlength{\parskip}{0pt}
\onehalfspacing

\title{\textbf{Philosophical Fundamental Problems}\\[0.5em]
  \large Festschrift for the University's Four-Hundredth Anniversary}
\author{R.\ Nielsen\\[4pt]\small Translated from the Danish}
\date{Copenhagen: Gyldendal, 1879}

\begin{document}
\maketitle
```

On Hans's machine the real Greek renders via `textalpha`; the sandbox lacks it,
so the compile check strips Greek (playbook §3) — never put those substitutions
in the real file.

---

## 4. Scaffolding the skeleton (first session only)

Before translating, build the empty structure so batches have markers to fill:

1. Write the preamble (§3) + `\maketitle`.
2. Lay down the section headings in order (Introduction has no heading), each
   followed by a marker:

   ```latex
   % Introduction (pp. 3--4)
   % [text to be added: pp. 3--4]

   \section*{I.\ The Problem of Knowledge}
   % [text to be added: pp. 4--26]

   \section*{II.\ The Problem of Reality}
   % [text to be added: pp. 27--50]

   \section*{III.\ The Problem of the Heterogeneous Principles}
   % [text to be added: pp. 50--77]

   \end{document}
   ```
3. Then begin the batch loop, subdividing the long sections into ~10-page
   markers as you go (leave a `% [translation continues from p. N]` note at any
   mid-section seam, per playbook §1.3).

---

## 5. Book-specific translation notes

**Terminology (keep consistent across the whole book):**
- *ueensartet* → **heterogeneous** (the load-bearing term; also *of a different
  kind*). *ueensartede Principer* = *heterogeneous principles*. Do not drift to
  "dissimilar/disparate" mid-book.
- *Tro og Viden* → **Faith and Knowledge** (capitalized as a paired term when
  Nielsen uses it as his thesis phrase).
- *Erkjendelse* → **cognition / knowledge**; *Realitet* → **reality**;
  *Selveenhed* → **self-unity**; *Selvvæsen* → **self-being / self-essence**;
  *objectiverende Subjectivitet* → **objectivizing subjectivity**;
  *Aandsvirkelighed, Virkelighed for Aanden* → **spirit-reality, reality for
  the spirit** (both letterspaced in the print → keep `\emph{}`).
- Nielsen coins compound abstractions freely (Frihedsprincip, Realbegreb,
  Naturnødvendighed). Compound English coinages (freedom-principle,
  real-concept, natural-necessity) are acceptable and often clearer for
  alignment — match the register of the completed Nielsen/Brøchner translations.

**Emphasis / letterspacing.** The transcription marks every letterspaced span
with `\emph{}` — carry **all** of them into the translation as `\emph{}`. There
are many in Section III (e.g. p. 72 "Ingen personlig sammenhængende
Livsanskuelse…", p. 66 "Tingene bestemmes af deres Begreber…", p. 69
"Realgrunde, Motiver, og Villie", p. 77 "subjectivt aandsklare").

**Greek — keep verbatim, translate around it** (playbook §2). Occurrences:
`ὕλη ἄμορφος` (~p. 13), the Aristotle *Metaphysics* tag `αὑτὸν ἄρα νοεῖ … καὶ
ἔστιν ἡ νόησις νοήσεως νόησις`, `τέρατα` (p. 74), `μετάβασις εἰς ἄλλο γένος`
(p. 67 footnote). Don't translate the Greek; you may add a translator's gloss in
a footnote if helpful, marked clearly as the translator's.

**Latin phrases → `\textit{}`,** matching the original: e.g.
`\textit{principia præter necessitatem non esse multiplicanda}` (p. 71),
`\textit{a priori}` (p. 75 fn), `\textit{la foi démontrée}` / `\textit{la foi
révélée}` (p. 65 fn), plus any in Sections I–II you meet as you go
(`causa sui`, `generatio æqvivoca`, `libera necessitas`, etc.).

**Long foreign-language quotations — keep in the original language.** Nielsen
quotes primary sources at length in their own tongue; reproduce them verbatim as
transcribed, and translate only the surrounding Danish. The two big ones:
- **p. 65 footnote** — a long **French** quotation from Comte (*Anfr. Skr.
  IIIme partie…*). Keep the French exactly.
- **pp. 66–68 footnote** — a long **German** quotation: F. A. Lange quoting
  Ueberweg's *Logik* (§§ 38–44), ending "Geschicht. d. Materalsm. S. 497–98."
  Keep the German exactly (including its letterspaced words `Form`, `Stoff`,
  `In uns`, etc. as `\emph{}`), and translate the Danish frame around it.
  (Optionally add a translator's-footnote English rendering; mark it as such.)

**Quotation marks.** Danish „…" → English `` ``…'' ``. Comte's phrase „Aandens
moderne Oprør imod Hjertet" (p. 72) → curly-quoted English. The two first-person
credo quotations on p. 72 („Jeg kan ikke troe…" / „Jeg maa nødvendig troe…") →
curly-quoted English.

**Print quirks preserved verbatim in the transcription — render the intended
meaning in English, and add a brief translator's footnote flagging the original
oddity where it matters:**
- p. 68: "med andre, **Ord** kjende Friheden" — the comma is misplaced in the
  print (should be "med andre Ord,"). Translate as "in other words, know
  freedom by necessity."
- p. 42: "Realitetet" — a typo for *Realitet* (reality). Translate as reality.
- p. 38: "polentia af posse" — set in roman with em-dashes; almost certainly a
  misprint for *potentia ab posse*. Render the intended sense; footnote the
  oddity.
- p. 58: closing low quote „Gangliet føler, Hjernen tænker„ — the closing mark
  is a low quote in the print. Translate normally: "The ganglion feels, the
  brain thinks."
- p. 51: a **handwritten** margin note "idealistisk" beside the printed
  "materialistisk" — the transcription keeps the *printed* word; ignore the pen
  marginalia (a later reader's, not Nielsen's).
- p. 71: "Ansvaret hviler paa den vælgende Subjectivitet" carries a reader's pen
  **underline** in the scan — not authorial emphasis; do **not** italicize it.
- p. 67 fn: "Geschicht. d. Materalsm." — Nielsen's abbreviation drops the *i* in
  *Materialismus*; leave the German as transcribed.
- French accents in the p. 65 footnote are inconsistent in the print (á vs à,
  "rien a parlé"); the transcription reproduces them as printed — leave them.

**Footnotes.** Translate the Danish frame; keep `\footnote{}` at the same anchor
word; keep foreign quotations inside them in the original language (above).
Preserve work/volume/page references as Nielsen gives them.

**Proper names** unchanged (Comte, Lange, Ueberweg, Kant, Hegel, Newton,
Spinoza, Aristotle…). Danish work-titles in citations: leave in Danish.

---

## 6. Finishing

When `grep -c 'text to be added'` and `grep -c 'translation continues'` both
return 0:
1. Final sandbox compile → confirm pages, 0/0.
2. In `catalog.yaml`, the `philosophiske-grundproblemer` section is currently
   `status: in-progress` with a note "Danish transcription complete; English
   translation pending." When the translation is done, set `status: complete`
   and update/remove the note; add a **Translation** link entry pointing to
   `…/philosophiske-grundproblemer/translation.pdf` (mirror the
   `videnskabslaere` entry, which has both Transcription and Translation links).
3. Tell Hans to compile both PDFs locally with the real fonts and confirm the
   Transcription + Translation links resolve.
4. **Hans commits and pushes. You don't.**

---

## Quick start for the new session

1. Read `../../../TRANSLATION-PLAYBOOK.md`, then this file.
2. `grep -n "% p\." transcription.tex | head` to see the page map; skim
   `transcription.tex` end-to-end once.
3. Create `translation.tex` (§3–§4 scaffold).
4. Run the batch loop (§2), ~10 pages at a time, Section I → III.
5. Report after each batch. Never commit or push.
