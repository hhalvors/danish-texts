# EMPHASIS-153-161.md — verification and patch pass, pp. 153–161

Verification pass of 4 September 2026. The batch reported 25 letterspaced
runs (2.8/page) and said `spacing.py` caught about half, with false
positives on short words and Latin abbreviations (confirmed:
`spacing.py 153 161` only fired on pp. 153 and 161, all of it either real
runs already transcribed or `single?` false positives on ordinary words
like `disse,`, `paa`, `Devotion.`). This pass checked every one of the 25
runs, body and footnotes, against 600 dpi crops, and separately combed
every footnote (the site of the misses in the preceding range's audit,
pp. 143–152) for anything spaced that the batch might have missed.

**Result: 0 missed runs, 0 over-extensions.** Every run the batch
transcribed is correctly placed, with correct start/end boundaries, and
nothing else in the range is letterspaced in print — including the whole
of p. 156, which has no emphasis at all (see below). This contrasts with
the 143–152 audit's 12 misses; this batch's emphasis work is clean.

Method: `pdftoppm -r 600 -singlefile` into a sandbox `mktemp -d`, `convert
-crop` full-page bands and further zoomed sub-crops (150–500%) into
`bibliotek/.render-scratch/`, read with the `Read` tool. No renders were
left in the repository.

## Job 1 — the p. 156/157 quotation, opens „ closes «

**Confirmed genuine as transcribed — the print really does open with a low
double comma `„` (end of p. 156, before "saaledes") and close with a
guillemet `«` (p. 157, after "from Tro").** Both marks verified at 400–500%
zoom: the opening mark is unambiguously the low `„` shape (not a
guillemet), and the closing mark is unambiguously the angled `«` chevron
(not a curly `"`), matching the guillemet the book uses elsewhere on the
same page (e.g. »sine scelere toto coelo errare« just above it).

This is the **third** mixed pair in the book (after the note on pp. 75–76
and note 1 on p. 148) and the first one running in the *opposite*
direction — those two open `»` and close `"`; this one opens `„` and
closes `«`. Left exactly as transcribed; `%` comments added at both ends
recording what the image shows and cross-referencing the other end. No
character was changed. **For the ledger: this datum is real, not a
transcription error** — the whole-file quote balances of `»«` +1 / `„"` −2
(reported by `check.py` below) are correct as they stand once this range
is included.

## Job 2 — emphasis audit, pp. 153–161

### Runs added or removed: none. 25 runs confirmed as printed.

Per-page tally (all confirmed by 600 dpi crop, boundaries checked at each
end): p. 153 — `Religionens`, `lex divina`, `Ceremonier`, `Erfaringen` (4).
p. 154 — `Mirakler`, `Skriften` [1st], `Skriften og Philosophien derfor
maae sættes som gjensidig uafhængige`, `Skrifttheorie` (4). p. 155 —
`hellig og guddommelig`, `»Guds Ord«` [1st occurrence only — confirmed the
**2nd** occurrence of `»Guds Ord«` later on the same page is set in normal
weight, not spaced], `Guds Ord, der indeholdes i den, uforvansket.` (3).
**p. 156 — none** (confirmed; see below). p. 157 — `alene`, `»Philosophiens`
[opens a long `»…«` block quote spanning several sentences — a normal
guillemet pair, not a second mixed case], `Troens` (3). p. 158 —
`Propheternes Autoritet` (1). p. 159 — `jus circa sacra`, `at Gud ikke har
noget Rige uden gjennem dem, der have Herredømmet.`, `Ex rationis igitur
ductu Deum quidem amare, sed non obedire ei possumus` (3). p. 160 —
`indre`, `internus`, `Videnskaben`, `Tænke-` [run continues across the page
break] (4, one split). p. 161 — `friheden` [continuation of p. 160's
`Tænke-`, confirmed spaced on both halves], `ligeledes Friheden til at
udtale sine Tanker,`, `libertas est.`, `alene` (4, one shared with p. 160).
Total 25.

The `Tænke-/friheden` split (flagged by the batch) is set continuously in
print: both `Tænke-` at the foot of p. 160 and `friheden` at the head of
p. 161 are letterspaced, confirmed at 200% zoom on each side of the page
break. The existing markup (`\emph{Tænke\-%` / `friheden}`) is correct.

### p. 156 — confirmed genuinely bare

The whole page (body text and its one footnote, including the Latin
enumeration `1)…7)`, checked line by line at 600 dpi) carries no
letterspacing whatsoever. Zero is the correct count, not a miss.

### Candidates checked and confirmed *not* spaced

`der kun kaldes Guds Ord` (p. 155, 2nd `»Guds Ord«`), `Philosophien`
[unmarked occurrence, p. 157], `Philosophiens`/`Troens` [2nd, unmarked
occurrences later in the same paragraph, p. 157], `Kilde i Naturen alene`
and `alene Skriften` [2nd and 3rd `alene` on p. 157, unmarked], every Latin
citation term in the p. 153, 154, 156, 158, 159 and 160 footnotes
(`legitime argumentari`-style short Latin tags, the full seven-point
Latin enumeration on p. 156, `Ex rationis…` neighbours), all confirmed
normal weight against `spacing.py`'s `single?` false positives.

## Job 3 — two claims against the recon

- **p. 156 footnote count: the batch is right, the recon is wrong.**
  The page carries exactly **one** footnote (mark `¹)` after "derfor",
  confirmed on the image). Its text is a single long Latin quotation from
  the *tractatus theologico-politicus* containing an in-text enumeration
  `1) Deum … 7) Denique Deum poenitentibus peccata condonare`, which is
  what the recon's footnote census evidently miscounted as five separate
  footnote marks. Recon's "five footnotes, the most in the book" claim
  should be corrected in the census.
- **p. 161 closing rule: confirmed double in print**, matching pp. 43, 64,
  82, 108, 132 (two parallel horizontal rules, verified at 300% zoom).
  The transcription's single-rule template is left unchanged, per
  instructions — this is a global markup decision, not one to settle here.

## Job 4 — spot-check

**`sem`/`som` (p. 156) confirmed.** At 500% zoom the scan unambiguously
reads "Spinoza ellers forkaster **sem** anthropomorphistiske" — a closed,
rounded `e`, not `o`. Sense-reading `som` and the `%` comment are correct
and unchanged.

## check.py and compile results

`python3 check.py`: pages 1..161, no gaps or dupes; braces balanced; quote
balances **`»«` +1, `„"` −2** — exactly the figures predicted if the
p. 156/157 pair is genuine, which Job 1 confirms it is; `\textit`=1 (p. 63
Greek); 0 suspect readings.

Compile test (TRANSCRIPTION-PLAYBOOK §5 substitution, Greek mapped to a
placeholder): `pdflatex -interaction=nonstopmode` exits 0. 0 real errors,
0 missing characters.

`joints.py --fix` was **not** run, per instructions.
