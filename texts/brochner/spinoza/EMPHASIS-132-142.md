# EMPHASIS-132-142.md — verification and patch pass, pp. 132–142

Verification pass of 4 September 2026. The batch reported 35 letterspaced
runs (3.2/page). This pass confirms every run against 600 dpi crops of every
page, body and footnotes, and finds three boundary errors: one over-extension
(a run marked `\emph{}` that prints normal-weight throughout) and two genuine
misses (short single-word runs inside dense argument text — the same pattern
found on every earlier audit in this book). Total after patching: 36 runs.

Method: `pdftoppm -r 600 -singlefile` into a sandbox `mktemp -d`, `convert
-crop` full-page and zoomed sub-crop bands into `bibliotek/.render-scratch/`,
read with the `Read` tool. No renders were left in the repository.

## Job 1 — emphasis

### Runs removed (over-extension)

| page | prior span | verdict |
|---|---|---|
| 132 | `\emph{causa libera}` | **removed entirely.** "eneste causa libera, og at lade..." (opening line of p. 132, continuing a sentence from p. 131) is set in plain roman at 600 dpi — letter- and word-spacing both match the surrounding normal text. No letterspacing anywhere in the phrase. Flagged with a `%` comment at the site. |

### Runs added (misses)

| page | text | note |
|---|---|---|
| 135 | `det bliver derfor umuligt for den Enkelte at hævde sin Ret,` | confirmed spaced at 600 dpi; the preceding clause ("hans Ret staaer imod deres,") and the following word ("eftersom") are both normal-weight — the run's boundaries are exactly these two commas |
| 137 | `positivt` | single word, "og som væsenlig og **positivt** sammenholder den" — spaced; "væsenlig og" before it and "sammenholder den" after are normal weight. Classic short-technical-term-in-dense-passage miss. |

### Confirmed correct as printed (checked, no change)

All remaining 33 runs verified at 600 dpi and found accurate: `Staten og
Religionen`, `den evigt værende menneskelige Frihed`, `Samfundsforholdet`
(p. 132); `relative`, `egoistiske`, `Naturlove`, `ethiske`, `Enheden i det
Uendelige` (spanning the line break), `Menneskets Naturtilstand` (p. 133);
`de naturlige Tings Magt, ved hvilken de ere og virke,`, `Jus naturæ`,
`summo naturæ jure` (p. 134); `Menneskene ere af Naturen Fjender` (p. 135);
`Attraaen efter Selvopholdelsen driver derfor med Nødvendighed til Attraaen
efter Forening` (p. 136); `status civilis`, `civitas`, `respublica`,
`civis`, `subditus`, `hostis` (p. 137); `Lydigheden`, `Retfærdighed og
Uretfærdighed`, `retfærdig`, `uretfærdig` (p. 138); `Ret bestemmes ved
Magt,`, `Den Enkeltes naturlige Ret ophører imidlertid ikke egentlig i
Samfundstilstanden`, `Hobbes` (p. 139); `to forskjellige Stater forholde sig
til hinanden som to Individer i Naturtilstanden`, `Den øverste Statsmagt`
(p. 141); `den bedste`, `bedste`, `den sande Erkjendelse`, `secure et
commode vivere`, `optime` (p. 142, including the already-documented partial
second phrase "secure et **optime** vivere").

Candidates that were checked and confirmed **not** spaced (dense
citation/Latin passages, exactly where misses tend to hide): `causa libera`
p. 132 (see above); `modus` p. 132; `sui juris` (pp. 137, 139, 140, twice on
140, once on 141) and `civitatis juris` p. 139 — never spaced anywhere in
this stretch; `jus naturæ` second occurrence p. 135 ("Denne jus naturæ,
»under hvilken...«"); `status naturalis` / `status civilis` p. 136 (unspaced
here, unlike the spaced p. 137 occurrence); `jus in naturam` / `jus commune`
p. 137; `(status civilis)` p. 136; `potens` p. 140; `confoederatæ` p. 141;
`jure civile` / `jure civili` / `jure belli` p. 142.

Page-by-page run counts after patching: 132→3 (was 4, one removed), 133→6,
134→3, 135→2 (was 1, one added), 136→1, 137→7 (was 6, one added), 138→4,
139→3, 140→0, 141→2, 142→5. Total 36 (was 35: −1 removed, +2 added).

## Job 2 — the Cap. 7 head and the p. 138/139 blank lines

**Cap. 7 head: confirmed correct as spliced.** At 600 dpi the sequence
reads: a **double** rule closing Sjette Capitel (two clearly separated
parallel strokes, matching the batch's own comment and the p. 43/64/82/108
precedent), then bold roman `Syvende Capitel.` (not letterspaced), the
subtitle `Naturretten. Religionen.` (bold, not letterspaced), a short single
rule, then body text. Matches BATCH-AGENT.md §Heads exactly; the
`\addcontentsline`/`\markboth` pair is present and correctly worded.

**p. 138 and p. 139 blank lines: both confirmed genuine.** At 600 dpi, "Først
i dette nye Forhold..." (p. 138) and "Idet den almindelige Sætning..."
(p. 139) both begin with a clear paragraph indent, matching the book's
normal indent convention and distinct from the flush-left continuation seen
at every other page opening in this range. The other nine openings (132–137,
140–142) were each checked the same way and are all flush left, continuing
the prior page's sentence; none needs a blank line.

## Job 3 — spot-checks

- **`Tings`/`Tiugs` (p. 134)**: confirmed. The letterspaced run ("saa er de
  naturlige **T i n g s** Magt, ved...") reads unambiguously "Tings"; six
  lines later, unspaced, the scan reads "Tiugs" (a clear u, not n) —
  differs from "Tings" by one letter and is not a Danish word. Sense-reading
  and comment are accurate.
- **`Bundsforvandt`/`Bundsforvandi` (p. 137)**: confirmed. The scan reads
  "Bundsforvandi." at the site (dotted final stroke, no footnote mark), and
  p. 141 independently confirms the correct form as "Bundsforvandte." The
  sense-reading and comment are accurate.
- **p. 137 unmarked quotation in body type**: confirmed at 600 dpi. The
  quotation „Thi Aandens Frihed eller Styrke (fortitudo)...Sikkerheden" sits
  directly below the note rule, but its type is visibly the same size as the
  surrounding body paragraphs and clearly larger than footnotes 1) and 2)
  immediately below it. The batch's judgement (continuation of the body
  paragraph, not a footnote) is correct.
- **Spinoza's own chapter references not typeset as heads**: confirmed. Only
  two such references occur in this range — "(jfr. forrige Capitel)" p. 132
  and "(see forrige Capitel)" p. 137 — both plain inline body text, not
  headed. No occurrence of "i 7de Capitel" appears within pp. 132–142.

## check.py and compile results

`python3 check.py`: pages 1..142, no gaps or dupes; braces balanced; quote
balances »« +1, „" −2; `\textit`=1 (p. 63 Greek); 0 suspect readings.

Compile test (TRANSCRIPTION-PLAYBOOK §5 substitution, Greek mapped to a
placeholder): `pdflatex -interaction=nonstopmode` exits 0. 0 real errors,
0 missing characters.

`joints.py --fix` was **not** run, per instructions.
