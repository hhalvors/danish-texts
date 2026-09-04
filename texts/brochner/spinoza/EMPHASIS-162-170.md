# EMPHASIS-162-170.md — verification and patch pass, pp. 162–170

Verification pass of 4 September 2026, Cap. 8 (»Menneskets Frihed og
Evighed«). The batch reported 26 letterspaced runs (2.9/page) read off
600 dpi crops, said `spacing.py` caught only 9 of them, and flagged one
partial run on p. 166 (`den intuitive` spaced, `Viden` not) as printed.

This pass rendered all nine pages at 600 dpi, cropped each into three
overlapping bands (body + footnotes), and read every band against the
transcription — all 26 runs individually confirmed, and every line of
prose and every footnote combed for anything spaced that the batch might
have missed, including the Latin technical vocabulary (`amor Dei
intellectualis`, `duratio`, `acquiescentia`, `æternus cogitandi modus`)
that is exactly the environment where earlier batches under-counted.

**Result: 0 missed runs, 0 over-extensions.** Every one of the 26 runs is
correctly placed with correct start/end boundaries, and nothing else in
the range is letterspaced in print. This range's emphasis work was
already clean before this pass; no `Edit` was needed.

Method: `pdftoppm -r 600 -singlefile` into a sandbox `mktemp -d`, `convert
-crop` into three ~1650 px vertical bands per page plus targeted zoom
crops, staged in `bibliotek/.render-scratch/` and read with the `Read`
tool. No renders were left in the repository.

## Job 1 — the p. 168 closing « after "intellectus"

**Confirmed genuine as transcribed — a structural printer's defect, not a
transcription slip.** The closing `«` sits at the end of the sentence
"Saaledes bestemt er Aanden en evig Tankemodus … saaledes at alle i
Enhed (simul) constituere Guds evige og uendelige intellectus«
(Eth. V, 40. schol.)" — Brøchner's rendering of the Ethics V, 40 Coroll.
clause "… ita ut omnes simul Dei aeternum et infinitum intellectum
constituant."

Scanned back through the whole paragraph at 600 dpi — from the sentence's
own opening ("Saaledes bestemt er Aanden…", no » before it), through the
middle ("…saaledes at alle i Enhed (simul) constituere…", no » there
either), back across the p. 167/168 page boundary to the last lines of
p. 167 ("…ikke blot til det menneskelige Legemes Existents,") — and found
no opening `»` anywhere. The only other guillemet pair in this paragraph
(»Aandens Øine … ere selve Beviserne«, mid p. 168) is self-contained and
balanced; it does not supply the missing opener. No damaged-sort
ambiguity either: the gap where an opener would sit is clean, not a
faint or broken glyph. This is the same pattern as the confirmed dropped
opener at p. 77, cf. header §6/RESUME-NOTES. Kept as printed; the `%`
comment at the site is accurate. Affects the whole-file ledger:
`»«` −1 for this range, bringing the running total through p. 170 to
`»«` **0**, `„"` **−2** — exactly as RESUME-NOTES forecast pending this
confirmation.

## Job 2 — emphasis audit, pp. 162–170

| page | runs confirmed | notes |
|---|---|---|
| 162 | `Frihed`, `Befrielsen` | both full runs, boundaries correct |
| 163 | `active` | correct; `ambitio`, `pietas` correctly left unspaced |
| 164 | `nødvendige`, `elsker det Gud`, `handle` | all three confirmed at their printed boundaries |
| 165 | `den er derfor den bestandigste af alle Affecterne` | confirmed; `directe` two lines above this run is plain roman in print (not spaced) and is correctly left unmarked |
| 166 | `det nærværende Liv`, `duratio`, `Udvikling af Aandens sande, evige Væsen som det under Evighedens Form opfattede Legemes Idee`, `Stræben`, `den intuitive` (partial), `directe` | the `den intuitive`/`Viden` partial run reconfirmed at 600 dpi: `den intuitive` letterspaced, `Viden` immediately following in plain roman — printed exactly as transcribed |
| 167 | `amor Dei intellectualis`, `Aanden som evig`, `evig` | all three confirmed; the `intuitive Erkjendelse` a few lines above the `Aanden som evig` run is plain roman in print and correctly left unmarked |
| 168 | `som evigt`, `ikke vorder`, `den intellectuelle` | confirmed |
| 169 | `Frihed`, `Salighed` | confirmed |
| 170 | `der er, og ikke vorder`, `Sammensætning`, `ved Siden`, `Deel`, `mere` | confirmed |

No footnote in this range carries any letterspacing (checked all: p. 163
n.1, p. 164 n.1, p. 165 nn.1–3, p. 166 nn.1–2, p. 167 n.1, p. 168 nn.1–2,
p. 169 nn.1–3) — matches the batch's report and print.

## Job 3 — spot-checks

| page | printed | sense-reading | confirmed |
|---|---|---|---|
| 162 | `Begrændssingen` | `Begrændsningen` | yes — clearly `ss`, no `n`, at 600 dpi |
| 166 | `llgesaa` | `ligesaa` | yes — double `l`, no `i`, at 600 dpi |
| 167 | `Erkjendelsdsart` | `Erkjendelsesart` | yes — `d` for `e`, at 600 dpi |
| 168 | `Besiddclse` | `Besiddelse` | yes — `c` for `e`, at 600 dpi |
| 169 | `Sanime` | `Samme` | yes — `ni` for `m`, at 600 dpi |

All five comments accurately describe what the scan shows; no changes
needed.

## Word-break joins

| join | page | joins correctly | blank line? |
|---|---|---|---|
| `hand-/lende` → handlende | 163 | yes | no |
| `liden-/skabelige` → lidenskabelige | 164 | yes | no |
| `Grund-/anskuelse` → Grundanskuelse | 166 | yes | no |
| `Er-/kjendelse` → Erkjendelse | 167 | yes | no |

All four confirmed: the two halves read correctly across the page
boundary and no blank line (no stray `\par`) separates them anywhere.

## check.py and compile

```
pages: 1..170  n=170  gaps=none  dupes=none
braces balanced: True  (1435 open / 1435 close)
footnotes: 252 | emph: 719 | textit: 1 | sic: 0
quotes »«: »=104 «=104  balance=0
quotes „“: „=43 “=45  balance=-2
suspect readings: 0
```

Compile test (sandbox substitution recipe, TRANSCRIPTION-PLAYBOOK §5):
0 errors (`grep '^!' log | grep -v 'Unicode character'` empty), 0
missing-character warnings, 129 pages output. `libertinus`/Greek
substitutions applied as documented; no real defects.
