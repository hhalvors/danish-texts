# EMPHASIS-120-131.md — verification and patch pass, pp. 120–131

Verification pass of 3 September 2026. The batch reported 51 letterspaced
runs (4.25/page) and a single paragraph-break claim at p. 130; this pass
confirms both against 600 dpi crops of every page, footnotes included, and
finds four boundary errors in the batch's own \emph tags — three cases of
over-extension (spacing claimed for words that print normal-weight) and one
case of a genuine miss inside a discontinuous run. Two further short misses
(individually spaced "Godt"/"Ondt") were found on p. 124, exactly the
"short abstract term inside a dense passage" pattern the earlier audits kept
finding. Total after patching: 55 runs.

Method: `pdftoppm -r 600 -singlefile` into a sandbox `mktemp -d`, `convert
-crop` bands (and further zoomed sub-crops for boundary judgment) into
`bibliotek/.render-scratch/`, read with the `Read` tool. No renders were left
in the repository.

## Job 1 — emphasis

### Runs added (misses)

| page | text | note |
|---|---|---|
| 124 | `Godt` / `Ondt` | body: "ledes, at **Godt** bliver det... nyttigt for os, **Ondt** det Modsatte" — each word individually letterspaced, confirmed at 600 dpi; surrounding text normal weight |
| 124 | `Godt` | footnote 1, opening word ("**Godt** bliver saaledes det, der disponerer...") — spaced; "godt" later in the same note (lowercase, second occurrence) is NOT spaced |
| 124 | `Døden` | footnote 1, mid-note ("(Dette er **Døden**, men Dødens Begreb...") — spaced; "Dødens" immediately following is NOT spaced |
| 128 | `affecterne: Attraa og Glæde; thi Sorgen forudsætter en` | second half of a discontinuous run opening the page (see boundary correction below) — this half was already inside the batch's \emph span, so not a fresh miss, but the internal break was |

### Boundary corrections (over-extension: the batch's \emph claimed spacing for words that print normal-weight)

| page | prior span | corrected | note |
|---|---|---|---|
| 123 | `\emph{som res particularis æterna}` | emphasis removed entirely | confirmed at 600 dpi, letter-by-letter and word-spacing both match the surrounding normal text; not letterspaced |
| 123 | `\emph{Dette opstilles som exemplar humanæ naturæ, quod intueamur}` | `Dette opstilles som \emph{exemplar humanæ naturæ, quod intueamur}` | side-by-side 600 dpi crop shows "Dette opstilles som" tight-kerned, "exemplar..." clearly spread — partial run, cf. BATCH-AGENT.md's p. 71 "natura naturans" case |
| 127 | `\emph{Fornuftens Erkjendelse af det Gode og Onde}` | `\emph{Fornuftens}` only | only "Fornuftens" is spaced; "Erkjendelse af det Gode og Onde" is normal weight at 600 dpi |
| 128 | `\emph{og ere active. Disse maae henføres til de to af Grund-affecterne: Attraa og Glæde; thi Sorgen forudsætter en}` | `\emph{og ere active.}` Disse maae henføres til de to af Grund- `\emph{affecterne: Attraa og Glæde; thi Sorgen forudsætter en}` Liden. | discontinuous: spaced / normal / spaced / normal in four segments across three lines, confirmed at 600 dpi — the batch's single \emph bridged a normal-weight stretch |
| 128 | `\emph{Anvendes Bestemmelserne Godt og Ondt}` | Anvendes Bestemmelserne `\emph{Godt og Ondt}` | only "Godt og Ondt" is spaced; "Anvendes Bestemmelserne" is normal weight at 600 dpi |

### Confirmed correct as printed (checked, no change)

Every other letterspaced run already in the fragment was verified at 600 dpi
and found accurate, including several dense stretches that were candidates
for misses and turned out NOT spaced: `impotentia` (p. 126, both
occurrences), `hilaritas` (p. 129), `titillatio og dolor` (p. 129),
`tristitia` (p. 130, both occurrences), `conatus` (p. 131, inside the Eth.
IV App. c. 32 Latin block quote), `res particularis æterna` unmarked on
p. 122, `Naturens Attraa` beside the spaced `Fornuftens Fordring` on p. 122,
`Generositas` (capitalized, sentence-initial, beside the spaced lower-case
`generositas`) on p. 128, and the second (unspaced) `Overgang` on p. 121
beside the spaced first occurrence. The p. 129/130 footnote's documented
discontinuous run (`større` alone / normal stretch / `Overgangen til en
mindre ... et værende` / normal / `-gangen ... Ikke-Værende`) was checked
segment by segment and matches the existing `%` comment exactly.

Runs per page after patching: 120→0, 121→7, 122→6, 123→1, 124→6, 125→3,
126→2, 127→6, 128→15, 129→5, 130→3, 131→1 (total 55, up from 51).

## Job 2 — the p. 130 paragraph break

**Confirmed genuine.** At 600 dpi, "Gjennem disse forberedende
Udviklinger..." on p. 130 begins with a clear paragraph indent — its first
line starts markedly further right than every subsequent line, matching
the book's normal paragraph-indent convention. The batch's blank line
before `% --- p. 130 ---` is correct and was left in place.

The other eleven page openings (120–129, 131) were each checked the same
way: every one is flush left, continuing the sentence off the bottom of the
previous page. None opens a new paragraph; no other page needs a blank line.

## Job 3 — spot-checks

- **`mindve` → `mindre`** (p. 125, footnote 1): confirmed at 600 dpi. The
  scan clearly reads "mindve" (not "mindre"); the `%` comment's sense-reading
  and single-sort-substitution rationale are accurate.
- **`lid nde` → `lidende`** (p. 129, footnote 3, continuing into p. 130's
  note block): confirmed at 600 dpi. There is a visible word-internal gap
  reading "lid" + space + "nde" where "lidende" belongs; the `%` comment is
  accurate.
- **p. 130 note 2 continuing at the head of p. 131's note block**: confirmed.
  The note opens on p. 130 ("Erkjendelsen af det Onde er en uadæquat
  Erkjendelse...") and its text — including the "tristitia" sentence — runs
  directly into p. 131's note block, closing there with "Begrebet Godt (Eth.
  IV. 64. 68)." before p. 131's own note 1 begins. The whole note is attached
  to its p. 130 mark, not split.

## check.py and compile results

`python3 check.py`: pages 1..131, no gaps or dupes; braces balanced (1155/
1155); quotes »« balance +1, „" balance −2; `\textit`=1 (p. 63 Greek); 0
suspect readings. `emph` count 590 (book-wide).

Compile test (TRANSCRIPTION-PLAYBOOK §5 substitution, Greek mapped to a
placeholder): `pdflatex -interaction=nonstopmode` exits 0, produces a
103-page PDF. `grep '^!' t.log` (excluding the expected "Unicode character"
false alarm) — 0 matches. "Missing character" warnings — 0. "Unicode
character" warnings — 0 (none appeared, since Greek was pre-mapped to a
placeholder). No real errors, no missing characters.

`joints.py --fix` was **not** run, per instructions.
