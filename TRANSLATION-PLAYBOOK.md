# Danish → English translation playbook

Point a fresh Claude session at this file to translate any 19th-century Danish
book in this repo into English. It captures the workflow proven on Brøchner's
*Problemet om Tro og Viden* (1868), which is now **complete** (transcription +
translation, 182 pp., 0 errors). Use it as the standing method; keep a short
per-book **RESUME-NOTES.md** alongside it for state that changes batch to batch.

---

## 0. What you're doing

A book lives in `texts/<author>/<slug>/` and has two LaTeX files:

- `transcription.tex` — the Danish, in `book` class. **This is the source of
  truth for translation.** Translate FROM it, not from the PDF scan.
- `translation.tex` — the English. Built up over many sessions by filling
  markers (see below). Mirrors the transcription's structure 1:1.

If a book has no transcription yet, that's a *transcription* job, not a
translation job — different playbook (see the Brøchner RESUME-NOTES' OCR
pipeline section for that workflow). This file is about **translation**.

Work in **~10-printed-page batches**. After each batch: compile, give a short
report, and hand back. **The user commits and pushes — you never do.**

---

## 1. The batch loop

1. `grep -n "text to be added" translation.tex` → the markers, in reading order.
   Each looks like `% [text to be added: pp. X--Y]`. Also grep for
   `translation continues` — those are *continuation notes* marking a mid-section
   gap where translated text resumes; fill the gap, don't restructure.
2. Take the next marker. Find the matching Danish in `transcription.tex` (match
   the `\section`/`\subsection` heading and `\label`). Read the whole span,
   start heading to next heading.
3. If the span is much more than ~10 printed pages, do a coherent sub-chunk and
   leave/advance a `% [translation continues from p. N]` note at the seam.
4. Translate it (conventions in §2). Replace the marker via the `Edit` tool.
5. Compile with the sandbox recipe (§3). Expect **0 errors, 0 char-warnings**.
6. Report in 2–4 sentences: what section, page range, notable choices, the
   compile result (page count + 0/0), and markers remaining. Hand back.

Use the task list (TaskCreate/TaskUpdate) per batch: one task to translate, one
to compile/report. It renders as a progress widget for the user.

---

## 2. Translation conventions (keep these consistent across the whole book)

- **Quotes.** Danish „…" (low-high) and guillemets »…« / «…» → English curly
  doubles, written in LaTeX as `` ``…'' ``. (Foreign-language guillemet *terms*
  the author keeps as foreign — e.g. «plus ultra», «bonum est quia Deus vult»,
  «lazzi» — stay in guillemets as printed.)
- **Emphasis.** Danish `\emph{}` (letterspacing in the original) → keep as
  `\emph{}` (renders italic). Preserve every emphasized span — OCR/transcription
  often marks these; carry them all over.
- **Latin phrases** → `\textit{}` (e.g. `\textit{credo ut intelligam}`,
  `\textit{libera necessitas}`, `\textit{eo ipso}`, `\textit{per impossibile}`,
  `\textit{non liquet}`, `\textit{differentia specifica}`). Match the original's
  italicization.
- **Greek.** Copy the glyphs verbatim from the Danish (τέλος, μὴ ὄν, πίστις,
  γνῶσις, Νοῦς, Κόσμος, the Iliad tag, etc.). Translate the surrounding prose,
  not the Greek. Requires `\usepackage{textalpha}` in the preamble (see §4).
  Exception: where the author himself transliterates (e.g. an Antiquity section
  using `\textit{nous}`, `\textit{phronesis}`), keep the transliteration —
  match the author term-by-term.
- **The old "id est" mark `ɔ:`** → render `i.e.` in English. (Also `d.\ v.\ s.`
  → "that is"/"i.e.")
- **Em-dash** `---`. Section-break rules the book marks with a short centered
  rule → `\begin{center}---\end{center}`. Reproduce these at the same breaks.
- **Footnotes** → translate the note content, keep `\footnote{}` at the same
  anchor word. Danish footnotes are sparse — check each page's Danish for any
  `\footnote` and carry it. Keep work-title references (e.g. *Om den gode
  Villie* p. 28) as the author cites them; keep volume/page refs verbatim
  (e.g. `Gr. L. II, 442`).
- **Proper names** unchanged (Spinoza, Hume, Strauß, Kierkegaard, Martensen…).
  Danish book/work titles in footnotes: leave in Danish.
- **Numbered run-in heads** like `1.~\emph{Med Hensyn til…}` → keep the same
  form: `1.~\emph{With Respect to…}`. Enumerate lists with `\arabic*)` etc. need
  `enumitem` (see §4).
- **Register.** Scholarly, moderately literal but readable English. Brøchner's
  syntax is long and nominalized; it's fine — and often clearer for matching —
  to keep compound coinages (essence-willing, knowledge-determination,
  will-concentration, being-for-itself). Match the done sections' feel.
- **Headings / `\label{}`.** Keep labels and structure mirroring
  transcription.tex 1:1. Verify each heading against the FINAL transcription
  before filling — some skeleton headings were drafted against an earlier state.

### Two structural gotchas that recur
- **Section intros.** A `\section{}` often has an intro paragraph in the Danish
  *before* its first `\subsection{}`. The translation skeleton may jump straight
  from section heading to subsection — insert the intro paragraph in between.
- **Bridge paragraphs.** Watch for a paragraph the print places at the end of one
  section that a skeleton accidentally floated to the next chapter's intro. Put
  it where the Danish has it so the translation mirrors transcription 1:1.

---

## 3. Sandbox compile / verification recipe

The sandbox lacks `libertinus`; substitute `lmodern` and strip the Greek/danish
bits just for the check (do NOT put these substitutions in the real file). The
bash mount path is **session-specific** — find it with `ls /sessions/*/mnt/`
each session; below it's written generically.

```bash
cd /tmp && mkdir -p verify && cd verify
SRC="<sandbox-path-to>/translation.tex"   # …/mnt/danish-texts/texts/<author>/<slug>/translation.tex
sed -e 's/\\usepackage{libertinus}/\\usepackage{lmodern}/' -e '/libertinust1math/d' \
    -e '/textalpha/d' -e 's/\\usepackage\[english\]{babel}/\\usepackage{babel}/' "$SRC" > t.tex
python3 - <<'PY'
import re; s=open('t.tex',encoding='utf-8').read()
s=re.sub(r'[Ͱ-Ͽἀ-῿]+','[Gr]',s)   # Greek replaced ONLY because sandbox lacks textalpha
open('t.tex','w',encoding='utf-8').write(s)
PY
pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1; pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1
grep -o 'Output written.*' l.txt
echo "char-warnings:"; grep -ic 'not set up\|missing.*character' l.txt
echo -n "errors: "; grep -c '^!' l.txt || true
echo "markers left:"; grep -c 'text to be added' "$SRC"
```

Expect `0` char-warnings and `0` errors. (`grep -c` exits 1 when it finds zero —
that's the *good* outcome, not a failure; the `|| true` keeps the script going.)
If `pdflatex` errors with "Missing number, treated as zero" at an `enumerate`,
the preamble is missing `enumitem` (see §4).

On the user's real machine the Danish compiles with `libertinus +
libertinust1math`; the English is fine with `lmodern`. `textalpha` handles the
real Greek there. Don't add the sandbox substitutions to the actual file.

---

## 4. Preamble checklist for a translation.tex

When starting a new book's `translation.tex`, make sure the preamble has:
- `\usepackage[utf8]{inputenc}`, `\usepackage[T1]{fontenc}`
- `\usepackage{libertinus}` + `\usepackage{libertinust1math}`
- `\usepackage{textalpha}` — for real Greek glyphs
- `\usepackage[english]{babel}`
- `\usepackage{enumitem}` — needed for `\arabic*)`-style lists (easy to forget;
  it caused the one mid-project compile failure on Brøchner)
- `geometry`, `setspace`, `fancyhdr`, `hyperref`, `microtype` as desired

---

## 5. Page-offset (per book)

Find the constant offset between **printed page** and **PDF page** once, by
comparing printed headers in the scan to the PDF page numbers (don't trust OCR
`[side N]` markers — they drift). For Brøchner it was **PDF = printed + 9**.
Record the book's offset in its RESUME-NOTES.

---

## 6. Finishing a book

When `grep -c 'text to be added'` and `grep -c 'translation continues'` both
return `0`:
1. Final sandbox compile → confirm pages, 0/0.
2. In `catalog.yaml`, set the book's section `status:` to `complete`.
3. Tell the user to compile both PDFs locally with the real fonts and confirm the
   Transcription + Translation links resolve.
4. User commits/pushes. You don't.

---

## 7. Per-book RESUME-NOTES template

Keep a short `RESUME-NOTES.md` in each book's folder. Minimal shape:

```
# <Author> — <Title> (<year>): translation resume notes

Source of truth: transcription.tex (Danish), COMPLETE/▢ in progress.
Page-offset: PDF = printed + N.
Scan: ~/bibliotek/<author>/<file>.pdf

## CURRENT RESUME POINT
Next marker: <% [text to be added: pp. X--Y] — section name>.
<anything unusual about the next span: long quotes, footnote inventory,
 a section intro to fold in, a continuation note to advance, etc.>

## DONE so far (don't redo)
- <front matter, chapters/sections filled, with page ranges>

## Conventions
See ../../../TRANSLATION-PLAYBOOK.md (the standing method). Book-specific
deviations: <e.g. author transliterates Greek in section Z; work-title
abbreviations used in footnotes; etc.>
```

That's it. Read the playbook, read the book's RESUME-NOTES, grep the markers,
and start the batch loop.
