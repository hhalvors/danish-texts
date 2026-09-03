# Can this scan settle an n/u question? — No.

A forensic test on the encoding of
`bibliotek/Brøchner, Hans/Benedict_Spinoza.pdf` (Google Books' digitisation of
the BSB copy of Brøchner, *Benedict Spinoza*, 1857), run 3 September 2026 in
the main session.

## Why the test was needed

Three transcription batches logged apparent **turned sorts**, all n/u, and
transcribed them as printed with confident `%` comments at the site:

| printed page | reading | claimed |
|---|---|---|
| 9 | `Elemeut` for `Element` | turned n |
| 36 | `nnder` for `under` | turned n |
| 39 | `Fornden` for `Foruden` | turned u |

Each comment argued from the appearance of the glyph at 600 dpi ("shoulder at
the top left", "open at the top") and from both OCR witnesses agreeing.

**Neither argument can work on this file.** The recon pass (RECON §14) had
already established that the scan is a symbol-matching JBIG2: 57–59% of glyph
components on a sample page are pixel-identical to another instance of the same
letter, so the file reconstructs letters from a dictionary rather than
reproducing each impression. The rendered page is the encoder's output, so
looking at it harder cannot distinguish a compositor's turned sort from an
encoder's substitution — and *both OCR witnesses read the same reconstructed
image*, so their agreement is not independent corroboration of anything.

An n-for-u substitution is precisely the documented failure mode of
symbol-matching compression (the Xerox scanner affair). So the question is
whether **this** encoder's clustering is tight enough to keep the two classes
apart.

## Method

Tools available in the sandbox: `pdfimages`, `tesseract`, `convert`, PIL,
numpy. No `mutool`, no `jbig2dec`, so the symbol dictionary could not be
enumerated directly and the fallback calibration of playbook §2 was used
instead.

1. `pdfimages -png` extracted the **native 1-bit page bitmaps** (≈2840×4600,
   600 ppi) for PDF pp. 19, 20, 46, 47, 49 — the three pages carrying the
   doubtful readings plus a neighbour of each. No interpolation, no rendering:
   these are the encoder's own output.
2. `tesseract -l dan … makebox` gave per-character boxes; every box labelled
   `n` or `u` was cropped, trimmed to its ink bounding box, and hashed.
3. Exact bitmap identity was then tested within and across the two classes.

664 instances labelled `n`, 161 labelled `u`.

## Result 1 — dictionary reuse confirmed, at the expected rate

| class | distinct bitmaps | bitmaps recurring | instances identical to an earlier one |
|---|---|---|---|
| n | 478 | 73 | 186 (28%) |
| u | 129 | 21 | 32 (20%) |

Exact pixel identity between separate impressions of a letter is impossible
under lossless coding, so this reproduces the recon's finding independently:
the file is placing dictionary symbols, not impressions.

## Result 2 — the decisive one: two bitmaps are placed as BOTH n and u

**Two bitmaps occur in positions where the text requires an `n` and in
positions where it requires a `u`.**

Bitmap A, 42×40, all three occurrences on **printed p. 36 — the page carrying
`nnder`**:

| context | letter the word requires |
|---|---|
| `…intéressés [·]ur les matiè…` (*sur*) | u |
| `…e Samling u[·]der Titele…` (*under*) | n |
| `…g: tractat[·]s de emenda…` (*tractatus*) | u |

Bitmap B, 44×38:

| context | letter the word requires |
|---|---|
| `…s Middelpu[·]ct, indire…` (*Middelpunct*), printed p. 9 | n |
| `…den conseq[·]ente Udvik…`, printed p. 9 | u (or v) |
| `…ddet Absol[·]te og med Na…` (*Absolute*), printed p. 10 | u |

The words are unambiguous — *sur*, *tractatus*, *Middelpunct*, *Absolute* — and
the crops carry no neighbouring ink (they match across different neighbours,
which they could not do if they did). So a single dictionary symbol is being
placed in both roles.

Both shared bitmaps read as **u-shaped** on a top-band/bottom-band ink measure
(arch index −0.264 and −0.297, against a labelled-`u` mean of −0.229 and a
labelled-`n` mean of −0.016). That points to a u-shaped symbol standing where
`under` and `Middelpunct` require an n — i.e. the scan showing `uuder` and
`Middelpuuct`, with tesseract's Danish language model quietly restoring the
real word. **But see the caveat below: that measure is not trustworthy, and
nothing here rests on it.**

## What this test does NOT show, and the apparatus that failed

**The arch index does not separate the classes**, and this must be said
plainly. Labelled `n`: mean −0.016, sd 0.278, range −0.872 to +0.792.
Labelled `u`: mean −0.229, sd 0.278, range −0.824 to +0.750. 271 of 664
labelled `n` come out negative and 27 of 161 labelled `u` come out positive;
the "cleanest" instances have bounding boxes of 60×77 and 61×63, far larger
than an x-height letter at this size, so some boxes are certainly merged or
misaligned pairs.

Since the two distributions overlap almost completely, **the metric is not
calibrated and no quantitative claim about the orientation of any individual
glyph may be drawn from this run** — which is exactly the error playbook §2
was written about. Result 2 does not depend on it: identity of trimmed bitmaps
plus unambiguous word context is the whole of the argument.

Nor does the test show that any one of the three readings *is* an artefact. It
shows that the mechanism which would produce them is demonstrably active in
this file.

## Verdict

**(ii) — the encoder demonstrably can merge n and u, so the three readings
cannot stand as evidence about the print.**

Per playbook §2 rule 3, the burden of proof lies on the claim of a defect, and
this scan can never discharge it for an n/u pair. The three sites are therefore
transcribed as **sense-readings** — `Element`, `under`, `Foruden` — with the
printed appearance and the reason recorded in a `%` comment at each site. The
printing house is not accused.

This generalises into a standing rule for the book: **where a reading is not a
word in Danish or Latin and differs from a real word only by n↔u, take the
sense-reading and log the doubt.** It is now in BATCH-AGENT.md.

## What would settle it

Enumerating the symbol dictionary directly — `mutool show` on the JBIG2
segments, or `jbig2dec -d` with symbol tracing, neither of which is installed
here — would give symbol IDs and their placements, and so turn Result 2 from
two observed collisions into a complete census of which classes this encoder
merges.

Better: **a different scan.** A non-JBIG2 digitisation (a KB scan of a Danish
copy, or greyscale page images from the BSB) would make every sort-level
question in this book answerable, and would be worth a re-reading pass. Nothing
short of that will.
