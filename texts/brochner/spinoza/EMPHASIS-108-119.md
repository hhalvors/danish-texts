# EMPHASIS-108-119.md — verification and patch pass, pp. 108–119

Verification pass of 3 September 2026: audits both the nine suspected false
paragraph breaks and the emphasis density flagged for this range (23 runs /
1.9 per page, against 2.9–7.6 elsewhere). Every page 108–119 was cut into
600 dpi bands (body and footnotes both) and read against the image; the
paragraph-joint flags were checked by reading the top band of each flagged
page. Method: `bash`-side `pdftoppm -r 600` into a sandbox `mktemp -d`,
`convert -crop` bands into `bibliotek/.render-scratch/`, read with the `Read`
tool. No renders were left in the repository.

## Job 1 — paragraph joints (pp. 109, 110, 111, 112, 115, 116, 117, 118)

All eight were checked against the top of the printed page. **All eight are
false** — none begins a new, indented paragraph; each continues the sentence
running off the bottom of the previous page. Two (116, 117) are provably
false independent of the image, since the break falls mid hyphenated word
(`Ima-/ginationen`, `Kjærlig-/heden`); the other six (109, 110, 111, 112, 115,
118) were confirmed by reading the flush-left opening line on the image. All
eight blank lines were deleted. Unlike the earlier-calibrated true positives
at pp. 37, 96, 103, none of this batch's eight flags survived inspection.

| page | opening words on the image | verdict |
|---|---|---|
| 109 | "Opfattelsen af det menneskelige Væsen som virkende og lidende." | false — continues "...maa ogsaa beherske" from p. 108 |
| 110 | "Natur og Kræfter og Aandens Magt over dem..." | false — continues "Jeg vil derfor afhandle Affecternes" from p. 109 |
| 111 | "ɔ: naar der af vor Natur følger Noget..." | false — continues the quoted definition begun on p. 110 |
| 112 | "flere uadæquate Ideer Aanden har..." | false — continues "Jo" at the foot of p. 111 |
| 115 | "(Eth. II, 13. schol.), og hvis Eiendommelighed..." | false — continues the footnote-citation sentence from p. 114 |
| 116 | "ginationen, at den afficerende Tings Billede..." | false — mid-word continuation of "Ima-" (Imaginationen) |
| 117 | "heden blive til Had..." | false — mid-word continuation of "Kjærlig-" (Kjærligheden) |
| 118 | "vore egne Affectioner fremkalde..." | false — continues "...og Attraaen, som" from p. 117 |

## Job 2 — emphasis: runs added

| page | text | note |
|---|---|---|
| 110 | `adæqvat Aarsag` | body, end of the Eth. III def. 2 quotation ("...til hvilket vi ere adæqvat Aarsag"); confirmed spaced letter-by-letter at 600 dpi against the immediately preceding normal-weight "i os eller udenfor os, til hvilket vi ere" |
| 111 | `Causam adæquatam` | footnote 2 (Eth. III def. 1 citation); opening two words of the definition are spaced, "appello eam, cuius effectus..." that follows is normal weight |
| 111 | `Inadæquatam` | same footnote, second definition; single word spaced, "autem seu partialem illam voco..." normal |
| 112 | `at bevare` | footnote 1 (Conatus); "efter" before and "hvad der allerede er tilstede" after are normal weight |

4 runs added, all on pp. 110–112 — the Latin-citation-heavy stretch. This
matches the pattern from the three prior audits: short technical/definitional
Latin terms spaced individually inside dense footnote citations.

## Pages re-verified with zero emphasis added

- **108, 113, 114**: existing `\emph{}` markers (Læren om Mennesket..., Villie,
  Attraa, Glæde og Sorg, Kjærligheden og Hadet, Lætitia, tristitia, hilaritas
  og melancholia, etc.) checked against 600 dpi crops, all confirmed correct.
  No unmarked letterspacing found elsewhere on these pages, footnotes included.
- **109**: zero emphasis anywhere on the page (body or the long tract. polit.
  footnote) — confirmed genuinely bare after full-page band inspection.
- **115**: existing tag (`Lidenskabernes Naturhistorie`, spanning the line
  break) confirmed; nothing else spaced.
- **116, 117, 118**: zero letterspacing anywhere on any of the three pages —
  body and footnotes both — confirming the batch's own claim that this
  affect-catalogue stretch, in plain Danish paraphrase, is genuinely sparse.
  Only the existing `Ligheden` tag on p. 117 was found.
- **119**: existing tag (`Tilnærmelse`) confirmed; nothing else spaced. The
  printed "coufusa" (misprint for confusa) was independently visible here too.

Total emphasis in range: 23 (batch) + 4 (this audit) = **27 runs**, 2.25/page.
Still below the book-wide 2.9–7.6/page band, but this range genuinely
straddles a dense-citation stretch (108–114, where the 4 new runs all fall)
and a plain-paraphrase affect catalogue (115–119, confirmed bare on every
page checked) — consistent with, not contradicting, the batch's own
explanation for the low count.

## Job 3 — spot-checks

1. **`ifr.` → `jfr.` (p. 113)**: confirmed on the image. The footnote reads
   "...andre uadæquate quate (ifr. Eth. III, 3. dem. II, 15. 19. 38)" — the
   compositor printed "ifr.", a misread j per the standing single-sort rule
   (JBIG2-TEST.md). The `%` comment at the site is accurate.
2. **`coufusa` → `confusa` (p. 119)**: confirmed on the image. "den er
   coufusa idea, qua mens maiorem vel minorem..." prints exactly "coufusa",
   an n/u confusion per the same standing rule. The `%` comment is accurate.
3. **Two unbalanced quotation marks, left as printed:**
   - **p. 109**: confirmed. The `»Der skeer Intet i Naturen...` quotation
     opened mid-page 109 runs to "...ved hvis blotte Betragtning vi frydes."
     with no closing `«` anywhere on the image before "Jeg vil derfor". The
     existing `%` comment correctly names the missing mark (`«`) and its
     location.
   - **footnote on p. 111**: confirmed, but **no `%` comment existed at this
     site before this pass** — added one now. The footnote to Eth. III def. 1
     opens `„Causam adæquatam appello eam...` and runs the full Latin
     citation to "...non potest adæquate concipi." with no closing `"`
     anywhere on the image. New comment added immediately before `concipi.}.`,
     naming the missing mark and cross-referencing the p. 109 case.

## Checks

`python3 check.py`: pages 1..119, no gaps or dupes, braces balanced (1053/1053),
`\textit` still 1 (the p. 63 Greek), 0 suspect readings, quote balances
`»«` = +1 (63/62) and `„"` = −2 (16/18) — all exactly as expected.

Compile test (TRANSCRIPTION-PLAYBOOK §5, Greek mapped to a placeholder,
libertinus/babel substituted): `pdflatex` exit 0, 95 pages produced, 0 lines
matching `^!` other than the expected Unicode-character false alarms from
stripping `textalpha`, 0 missing-character warnings.
