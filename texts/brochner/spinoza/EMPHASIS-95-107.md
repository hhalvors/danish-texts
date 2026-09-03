# EMPHASIS-95-107.md — audit of pp. 95–107

Verification pass of 3 September 2026, following the pattern found in the
pp. 65–81 and 82–94 audits: a transcription batch reporting emphasis density
well below the book's rate (here: 25 runs / 1.9 per page, against 3.3–7.6
elsewhere) had missed short, individually-spaced technical/Latin terms inside
dense citation and list passages. Every page 95–107 was cut into 600 dpi
bands (body and footnotes both) and read against the existing `\emph{}` in
`transcription.tex`. Method: `bash`-side `pdftoppm -r 600` into a sandbox
`mktemp -d`, `convert -crop` bands into `bibliotek/.render-scratch/`, read
with the `Read` tool. No renders were left in the repository.

## Runs added

| page | text | note |
|---|---|---|
| 95 | `ab experientia vaga` | body; "sine ordine ad intellectum" immediately before it is NOT spaced — partial-phrase pattern, as p. 71's `natura` naturans |
| 96 | `simplicissimas` | footnote (mark on p. 96, text prints on p. 96/97) |
| 96 | `toti naturæ communes` | same footnote, prints on p. 97; "res maxime universales et" immediately before is NOT spaced |
| 98 | `notiones universales` | body, opening line of p. 98 (tail of a sentence begun on p. 97); the SECOND occurrence of the same phrase two sentences later ("de saakaldte notiones universales.") is NOT spaced — confirmed both ways at 600 dpi |
| 99 | `universales imagines` | body; the FIRST "universales" in the same sentence ("disse universales notiones ere...") is NOT spaced — only the second occurrence, split across a line end ("uni-/versales imagines"), is |
| 99 | `Art, Slægt; Tid, Tal, Maal, Modsætning, Orden, Overensstemmelse, Forskjel o. desl.` | body; one continuous spaced run across a whole list of technical terms — the longest run found in this range |
| 99 | `Ende, Grændse, Mørke` | body |
| 99 | `Orden-Forvirring, Godt-Ondt, Skjønt-Hæsligt o. desl.` | body |
| 99 | `almindelige` | body — single word only; "Imaginationens" before it and "Bestemmelser" after are NOT spaced |
| 101 | `universelle Erkjendelse` | body; the following "(cognitio universalis)" is NOT spaced |
| 105 | `Ideen er` | body — two words only, comma after "er" falls outside; "som Tankemodus" that follows is not spaced |
| 105 | `Evne` | body, single word — "Bestemmelsen:" before and "er kun et" after are NOT spaced. (A second, unrelated "Evne" earlier on the same page is likewise not spaced, matching prior transcription.) |
| 106 | `samme` | body, single word inside "vi med den samme Villies Magt" — "med den" before it is NOT spaced, confirmed by close zoom; a look-alike phrase "den samme abstracte Opfattelse" earlier on the same page is genuinely NOT spaced, so this is a real, deliberate case, not a miss carried over from there |

13 runs added, spread over pages 95, 96, 98, 99 (5 of the 13), 101, 105, 106.

## Pages re-verified with zero emphasis added (already correct or genuinely bare)

- **95, 96, 97, 100, 101, 105, 106, 107**: existing `\emph{}` markers checked
  against 600 dpi crops and confirmed correct, including partial-word cases
  already flagged (p. 96 `secundi`/not `tertii`; p. 95/96/97's various
  already-marked runs).
- **100, 102, 103, 104, 107**: no unmarked letterspacing found anywhere,
  body or footnotes, after full-page band inspection. Pages 102 and 103 in
  particular were re-confirmed as genuinely zero-emphasis pages (matching the
  batch's own claim for those two) — but **page 98, which the batch also
  named as a zero-emphasis page it had rechecked, was not**: its very first
  line carries a missed run (`notiones universales`, see table above). The
  batch's "three zero-emphasis pages, re-verified" claim (98, 102, 103) is
  therefore only two-thirds right.

## Density after this patch

25 (batch) + 13 (this audit) = 38 runs over 13 pages ≈ 2.9/page — still below
the book's 3.3–7.6 range, but pages 95, 99, 105, and 106 alone account for
most of the addition and several pages (100, 102–104, 107) are confirmed
genuinely light or bare on inspection, unlike the flat 1.9/page the batch
reported for the whole range. No further pass was run beyond this one
image-by-image audit; if a third audit is ever warranted, pp. 99 (5 runs
found in one page) is the strongest signal that dense list/citation passages
are still the risk pattern to watch.

## Other findings from this pass

- **p. 96 footnote-rule comment corrected.** The transcription's own comment
  claimed p. 96's note block carries no rule above it ("tight page, per
  recon"). Direct inspection at 600 dpi shows this is wrong: a standard
  footnote rule *is* present, positioned after only two short body
  paragraphs (rather than near the page foot) because the note area below it
  is unusually long — the overflow of p. 95's footnote 3 plus p. 96's own
  footnote 1. The comment in `transcription.tex` has been corrected in place.
- **pp. 96 and 103 paragraph breaks: both genuine, not false positives.**
  Checked both pages at the image: p. 96 opens with a new, indented paragraph
  ("For bestemtere at opfatte Forholdet...") and p. 103 likewise ("Sammenstiller
  man imidlertid hvad der saaledes er sat..."). In both cases the body text on
  the *preceding* page ends in a complete sentence immediately before a
  footnote mark; the footnote's own internal continuation onto the next page's
  note block is what confused `joints.py`'s heuristic, not an actual mid-sentence
  break in the body-text flow. The blank lines before both `% --- p. 96 ---`
  and `% --- p. 103 ---` are correct as they stand; nothing was changed.
- **The `1) 2) 3) 4)` enumeration question (pp. 95–96): footnote text,
  confirmed by the image.** RECON.md and BATCH-AGENT.md's claim that pp.
  95–96 carry an in-text "1)2)3)4)" enumeration of Spinoza's four modes of
  perception conflates two different lists:
  - The genuine in-text enumeration on p. 95 is **three** items ("De
    forskjellige Erkjendelsesarter blive altsaa følgende tre: 1) ... 2) ...
    3) ..."), set in full body type — this is body text.
  - The **four**-item "4 modi percipiendi" list ("1) perceptio ex auditu...
    2) ab experientia vaga; 3) ubi essentia rei...; 4) naar Tingen begribes...")
    is set in visibly smaller type, below the footnote rule described above,
    as the tail of footnote 3 opened on p. 95 — confirmed footnote text, not
    body text, by direct comparison of type size against the surrounding
    body paragraphs at 600 dpi. The transcription's own existing comment
    (already correctly encoding this as `\footnote{}`) had it right; the
    batch agent's verdict of "footnote text" is correct and BATCH-AGENT.md's
    description should be read as referring to the footnote's internal list,
    not to body text.
