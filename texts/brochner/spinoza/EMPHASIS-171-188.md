# EMPHASIS-171-188.md — verification and patch pass, pp. 171–188 (final)

Verification pass of 4 September 2026, closing out the book: end of Cap. 8
(p. 171 head), all of Cap. 9 (»Charakteristik og Kritik af Spinozismen«,
pp. 171–180) and all of Cap. 10 to the end (»Spinozas Forhold til den
sildigere Philosophie«, pp. 181–188). All 18 pages rendered at 600 dpi in
overlapping top/bottom bands (body + footnotes) and read against the
transcription; several sites additionally re-cropped at 1000% for
letterform adjudication. No renders were left in the repository — all
staged in `bibliotek/.render-scratch/`.

## Job 1 — the p. 171 italic "i" — CONFIRMED GENUINE, edition changed

`Al Virkelighed er i Substantsen` (Cap. 9, first paragraph): the one-letter
word "i" is set in a **genuine italic sort**, not plain roman. Confirmed at
600–1000 dpi: a curved, calligraphic stem with a hooked/curled foot and a
slanted axis, categorically different in construction from every roman "i"
on the same page (`Virkelighed`, `indre`, `tilskyndende`, two lines above —
all straight-stemmed, upright). Calibrated against the book's only other
italic, the accented Greek tag on p. 63 (τοῦ μὴ ὄντος …), which is likewise
a distinct slanted/cursive fount set against the roman body — establishing
what "italic" looks like in this fount. Both OCR witnesses garble the site
(tesseract reads "Z"), consistent with an atypical glyph shape.

This is judged **not** to fall under the JBIG2 single-sort caution
(`JBIG2-TEST.md`): that rule concerns the encoder's symbol-matching
conflating two *pixel-similar* roman glyphs (n/u, c/e), and is silent on
whole-fount substitution. An italic sort and a roman sort of the same
letter are not pixel-similar — they differ in essentially every stroke —
so a false symbol-match between them is a different order of risk, and no
comparable italic-roman "i" symbol exists anywhere else in the book's
dictionary for the encoder to have confused this with (the sole other
italic content is Greek, a different alphabet entirely).

Read as the compositor's device for a case letterspacing cannot serve: a
single-letter word cannot be spaced out for emphasis, so italic supplies
the emphasis instead — the same functional gap that Greek fills with
italic rather than letterspacing.

**Applied**: `\textit{i}` at the site (was plain roman with a flagged
comment). `transcription.tex`'s header §3 (emphasis/italic rule) and
`check.py`'s suspect-reading regex were both updated to record this as the
book's **second** sanctioned `\textit{}`, alongside the p. 63 Greek — both
now documented as literal exceptions forced by the letterspacing device's
limits (a single letter; a non-Latin alphabet), not editorial choices.

## Job 2 — the two chapter heads — CONFIRMED

Both heads checked against the image and against BATCH-AGENT.md §Heads:
double rule closing the previous chapter (set single by the edition's
established convention), head, subtitle, single rule below, then
`\addcontentsline`/`\markboth` pair — all present and correctly formed.

| head | printed | subtitle | confirmed |
|---|---|---|---|
| p. 171 (mid-page) | `Niende Capitel.` | `Charakteristik og Kritik af Spinozismen.` | exact match |
| p. 181 (mid-page) | `Tiende Capitel.` | `Spinozas Forhold til den sildigere Philosophie.` | exact match |

## Job 3 — emphasis audit, pp. 171–188

**Result: 0 missing runs, 0 over-extensions.** Every `\emph{}` in the range
(70 runs: 31 on pp. 171–180 as reported, 39 on pp. 181–188 as reported) was
individually confirmed at its printed boundaries; every page's prose and
every footnote was additionally combed for anything spaced that the
batches might have missed. Two sites needed a second look before being
confirmed correct as transcribed (initially misread at lower resolution,
resolved at 1000% zoom): `Wolf` (p. 186) and `Jacobi` (p. 186) are both
genuinely letterspaced on first mention, matching the transcription.

### The first-mention/repeat name pattern — holds, checked specifically

Cap. 10 is the run of historical names, and this pass checked every one of
them for the claimed rule (letterspaced on first mention in a passage,
plain roman on repeats):

| name | first mention | repeats |
|---|---|---|
| Leibnitz | spaced (p. 183) | plain ×4 on the same page (p. 183–184) |
| Wolf | spaced (p. 186) | (not repeated) |
| Jacobi | spaced (p. 186) | plain (p. 186, same paragraph) |
| Mendelssohn og Herder | spaced (p. 186) | (not repeated) |
| Kant | spaced (p. 186/187 boundary) | plain (p. 188) |
| Fichte | spaced (p. 187) | plain ×2 (p. 187) |
| Novalis og Schleiermacher | spaced (p. 187) | (not repeated) |
| Schelling | spaced (p. 187) | plain (p. 187, footnote head aside) |
| Hegel(s) | spaced as `Hegels` (p. 187) | plain ×4 (p. 187–188) |
| Herbart | spaced (p. 188, body and again in its footnote) | (not repeated) |

The rule held with no counter-example found. One refinement worth
recording: **not every proper name gets the first-mention treatment** —
citation-apparatus names that are never central to the discussion,
`Bayle` and `Brucker` (p. 182, first mentions), are plain roman throughout
and never spaced, on this page or earlier in the book (cf. p. 175). The
pattern is not "every name once" but "every name central to the passage's
argument, once" — the batch's transcription already reflects this
correctly; nothing to change.

### The two partial runs

- **p. 171**: `»sui et Dei et rerum \emph{æterna} quadam \emph{necessitate}
  conscius,«` — confirmed at 600 dpi: `æterna` and `necessitate`
  letterspaced, `quadam` between them and `sui et Dei et rerum` before it
  in plain roman, exactly as transcribed.
- **p. 184**: `Forkjel som \emph{Grad}forskjel` — confirmed: `Grad`
  letterspaced, `forskjel` immediately following in plain roman, no space
  between them, exactly as transcribed.

## Job 4 — end of the book — CONFIRMED

- Last sentence confirmed verbatim against the image: "…Spinozas
  Philosophies dybere Motiver forstaaes først fuldstændig ved Hegel."
  Nothing follows it in the paragraph; nothing dropped.
- Below the final footnote block (Herbart, n. 1): a **tapered
  (lens-shaped) ornamental rule**, centred, confirmed on the image —
  distinct from the plain straight rules used at chapter ends elsewhere,
  correctly not reproduced with `\rule{}`.
- Below that, blank space, then the **BSB ink stamp** — "Bayerische
  Staatsbibliothek MÜNCHEN" in an oval border — confirmed, correctly not
  transcribed as text.
- **No colophon, no "Ende", no errata leaf, no advertisement.** The page
  ends with the stamp; nothing else is on it.

## check.py

```
pages: 1..188  n=188  gaps=none  dupes=none
braces balanced: True  (1560 open / 1560 close)
markers remaining (text to be added): 0
footnotes: 260 | emph: 789 | textit: 2 | sic: 0
quotes »«: »=112 «=112  balance=0
quotes „“: „=43 “=45  balance=-2
suspect readings: 0
```

`\textit` is 2, not 1, per Job 1 — both check.py's suspect-reading filter
and the `transcription.tex` header comment were updated to expect this.
Quote balances land exactly where RESUME-NOTES forecast through p. 170
(`»«` 0, `„“` −2), confirming nothing in pp. 171–188 disturbs the running
ledger — no new mixed pair or dropped mark in this range.

## Compile test

Sandbox substitution recipe (TRANSCRIPTION-PLAYBOOK §5). Direct pass:
22 `! LaTeX Error: Unicode character …` lines, all Greek letters from the
p. 63 tag — the documented false alarm from stripping `textalpha` — no
other `^!` lines. 142 pages output. Second pass with Greek substituted for
a placeholder (`re.sub(r'[Ͱ-Ͽἀ-῿]', 'G', s)`): **exit 0, 0 errors, 0
missing-character warnings**, 142 pages. Book compiles cleanly end to end.

## Book status

**188/188 pages done, audited, spliced and verified. Nothing outstanding.**
