# EMPHASIS-143-152.md — verification and patch pass, pp. 143–152

Verification pass of 4 September 2026. The batch reported 29 letterspaced
runs (2.9/page) and flagged that `spacing.py` fired only on pp. 143 and 152,
missing 144–151 entirely. This pass confirms every run against 600 dpi crops
of every page, body and footnotes, plus the note-4 continuation read off
p. 153 for Job 1. It finds **12 missed runs and 0 over-extensions** — every
run the batch transcribed was correct as printed; the errors were all
omissions, concentrated in the two densest footnote pages (148 and 149).
Total after patching: 42 runs across pp. 143–152 (43 counting the
p. 153 continuation's own "legitime argumentari").

Method: `pdftoppm -r 600 -singlefile` into a sandbox `mktemp -d`, `convert
-crop` full-page bands and further zoomed sub-crops (300–400%) into
`bibliotek/.render-scratch/`, read with the `Read` tool. No renders were
left in the repository.

## Job 1 — footnote 4, p. 152, completed from p. 153

**Confirmed unfinished as reported.** The note's Latin parenthesis, opened
at "(tract. theol.-polit. pag. 141, jfr. princ. phil. Cart. II, 13.", is not
closed on p. 152. The continuation sits at the head of p. 153's note block
(before that page's own note 1) and reads:

> schol. Cog. metaph. II. c. 12), og Forholdet mellem cognitio supranaturalis
> og *legitime argumentari* bestemmes som et omvendt Forhold (tract.
> theol.-polit. pag. 139). Det „Mere" i Aabenbaringen bliver „res
> imperceptibiles, quas tantum imaginari possumus" (pag. 97).

This closes the parenthesis exactly where the print does (after "II. c.
12)") and completes the note with a full stop before p. 153's note 1 begins.
The phrase "legitime argumentari" is letterspaced in the print (it spans a
line break on p. 153, "naturalis / og legitime argumentari") and is rendered
`\emph{}`. Appended inside the existing `\footnote{}` on p. 152; no body
text from p. 153 was transcribed. The batch's `%` comment (which only
recorded the note as unfinished) was replaced with one recording the
carry-over and the attachment-to-mark convention.

## Job 2 — p. 148 note 1, the mixed `»…"` pair

**Confirmed correct as printed, both counts.**

- The quotation opens with a guillemet `»` (before "verum Dei syngraphum")
  and closes with the raised high double `"` (after "consignavit."), not a
  matching `«`. Verified at 400% zoom on both marks. This is the second such
  mixed pair in the book (after pp. 75–76), exactly as the site's `%`
  comment and RESUME-NOTES' ledger say. **Not normalised.**
- `ɔ: humanæ menti` verified: the file holds U+0254 (ɔ) followed by `:`,
  confirmed both against the image (a clear reversed-c glyph) and by
  extracting the actual codepoints from the file (`0x254 0x3a`).

## Job 3 — emphasis audit, pp. 143–152

### Runs added (misses) — 12 total, 0 removed

| page | text | note |
|---|---|---|
| 143 | `Friheden` | "og fra Fornuften er ligeledes **Friheden**¹) uadskilllelig" — spaced at 600 dpi, missed by the batch |
| 147→148* | `nødvendig` | in the long footnote 3 attached to p. 147's »naturlige Lys«, whose text overflows onto p. 148's note block: "som **nødvendig** for Gudserkjendelsen" — isolated single-word spacing in a list of otherwise-unspaced parallel "som X" clauses |
| 148 (n. 2) | `Romana` | "skarpt adskilles fra rel. **Romana**)" — spaced; "rel." itself is not |
| 148 (n. 2) | `toti humano generi universalis` | "religio **toti humano generi universalis** (pag. 148)" — "religio" itself is not spaced |
| 148 (n. 2) | `naturalis` | "og som maxime **naturalis** (pag. 149)" — "maxime" itself is not spaced |
| 148 (n. 2) | `lex` | "om en **lex** catholica, der bliver liig med lex divina universalis" — only this occurrence of "lex" is spaced; the two others in the same note ("som lex divina", "lex divina universalis") are not |
| 148 (n. 2) | `fides` | "om en **fides** catholica (pag. 160)" — spaced; "catholica" itself never is, anywhere in this note |
| 149 (n. 1) | `revelata` | "et a Deo æque **revelata**, sive hoc sive illo modo" — first of three spaced Latin instances in this footnote |
| 149 (n. 1) | `revelatam` | "sive prophetico **revelatam** concipiamus" — second instance; "prophetico" beside it is not spaced |
| 149 (n. 1) | `lumine naturali revelata` | "decreta Dei, **lumine naturali revelata**." — third instance, spans the line break; "decreta Dei," itself is not spaced |
| 149 (n. 2) | `intellectus limites` | "eos multa extra **intellectus limites** percipere potuisse" — spans the word-break "in-/tellectus"; "percipere potuisse" after it is not spaced |
| 149 | `Imaginationens` | "Guds Aabenbaring paa anden Maade end ved **Imaginationens** Hjælp" — single word; "Hjælp" beside it is not spaced |

\* This footnote's mark (»naturlige Lys«³) sits on p. 147, so per the
"whole note belongs to its mark" convention its full text — including the
part printed on p. 148 — is transcribed under the p. 147 marker in the
file, even though the run itself is only visible on the p. 148 image.

### Confirmed correct as printed (checked, no change) — 30 runs

`Statsformer`, `Demokratie`, `Aristokratie`, `Monarchie`, `Finis ergo
reipublicæ revera libertas est.` (143); `omnino absolutum imperium`,
`negativ` (144); *(145 has none — confirmed genuinely bare, body and all
four footnotes)*; `Religionen`, `Videnskabens`, `Religionens` [2nd
occurrence, confirmed **not** spaced], `deels`, `deels` (146); `Fornuften`,
`sande` (147); `overnaturlig` (148); `Aabenbaringen`, `Prophetien`,
`revelata` [body], `Midler` (149); `Christus`, `Christendommen`, `Christi
Aand`, `Christus` [2nd], `menneskelig` (150); `særegen og ualmindelig`,
`Tegnene`, `Propheternes moralske Charakteer` (151); `Propheterne have
været uvidende om mange Ting`, `gode Gjerninger` (152).

Candidates checked and confirmed **not** spaced (dense citation/Latin
passages, exactly where misses tend to hide): `Statsformer` [2nd occurrence,
p. 144, unspaced unlike p. 143's], `causa`-type Latin tags throughout p.
144's footnote 1 (tract. polit. citations); `sui juris`-style short Latin
tags across pp. 147–149; `religio catholica` [1st and 2nd occurrences],
`rel. Romana`'s `rel.`, `lex divina` [1st and 3rd occurrences], `catholica`
[every one of its ~9 occurrences in n. 2 — never itself spaced],
`documenta rationis`, `lumine naturali` [1st occurrence, "en rel. catholica
lumine naturali et prophetia revelata"], `intellectus` [body, "bestemmes
ved intellectus"], `Religionen` [in parens, "(Religionen)", p. 146],
`»naturlige Lys«`, `nempe sua idea` [visually suggestive at low zoom but
confirmed normal weight at 300%].

Page-by-page run counts after patching: 143→6 (+1), 144→2, 145→0, 146→5,
147→3 (+1, attached mark though visible on p. 148), 148→6 (+5, of which one
more is attached from p. 147's mark), 149→9 (+5), 150→5, 151→3, 152→3.
Total 42 for pp. 143–152 by print page, or 43 counting the p. 153
continuation's `legitime argumentari` (attached to the p. 152 mark).

## Job 4 — spot-checks

Only **three** sense-reading sites matching the standing single-sort rule
were found in pp. 143–152 (the brief said "four" but named three; no
fourth site exists in this range under a `%` comment of this kind — the
count in the brief appears to be off by one):

- **`deltage`/`dceltage` (p. 144)**: confirmed. The scan reads "saa Mange
  **dceltage** i Regjeringsmagten" unambiguously at 600 dpi (extra `c`
  before `eltage`). Sense-reading and comment accurate.
- **`Fornuften`/`Fornufteu` (p. 148 n. 2)**: confirmed. The scan reads "med
  **Fornufteu** overensstemmende Indhold" (n/u confusion, final letter).
  Sense-reading and comment accurate.
- **`ostendimus`/`ostendimas` (p. 152 n. 3)**: confirmed. The scan reads
  "ut jam **ostendimas**, veritatis regnum sibi vindicavit" (not a Latin
  word; single-letter difference). Sense-reading and comment accurate.

## check.py and compile results

`python3 check.py`: pages 1..152, no gaps or dupes; braces balanced; quote
balances `»«` +2, `„"` −3 (as predicted once p. 148 landed); `\textit`=1
(p. 63 Greek); 0 suspect readings.

Compile test (TRANSCRIPTION-PLAYBOOK §5 substitution, Greek mapped to a
placeholder): `pdflatex -interaction=nonstopmode` exits 0. 0 real errors,
0 missing characters.

`joints.py --fix` was **not** run, per instructions.
