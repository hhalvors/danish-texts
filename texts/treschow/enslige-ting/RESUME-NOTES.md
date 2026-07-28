# Niels Treschow — *Gives der noget Begreb eller nogen Idee om enslige Ting?* (1807/1810): transcription resume notes

This is a **TRANSCRIPTION** job (antiqua Danish, from scan → LaTeX), to be
followed later by an English translation (Phase 2). Work in ~10-page batches;
after each, compile, give a short report, hand back. **Hans commits and
pushes — the assistant never does.**

Essay: *Gives der noget Begreb eller nogen Idee om enslige Ting? Besvaret med
Hensyn til Menneskeværd og Menneskevel.* Af Professor Treschow. In *Det
Kongelige Danske Videnskabers Selskabs Skrifter*, femte Deel (V), 1. Hæfte
(signed "1807"; volume published 1810).

## Scan & offset (VERIFIED against page images)
- Scan: `~/bibliotek/Treschow, Niels/videnskabernes-selskabs-skrifter-ser3-bd5-1810.pdf`
  (632 PDF pp.; Internet Archive `kongeligedanskev35kong`, ser.3 bd.5, 1810;
  MBLWHOI copy, clean 300 ppi). Public-domain; kept locally, not committed.
- **Offset: PDF = printed + 10.** Verified at both ends: title page (printed
  223) = PDF 233; last essay page (printed 254) = PDF 264.
- **Essay extent:** title PDF 233 (printed 223); body PDF 235–264 (printed
  225–254). PDF 234 is the blank verso of the title. Ends "…paa dette Sted
  engang gandske passende." + ornamental rule. PDF 265 begins the volume's
  *Sagregister* (subject index) — NOT part of the essay.
- No Rettelser/errata leaf applies to this essay (checked whole-volume OCR).

## Typography — READ THIS
- **Type is ANTIQUA (roman)**, not Fraktur — the learned-society *Skrifter*
  convention. OCR with `-l dan` (or the archive.org ABBYY layer as a base),
  then image-verify every page.
- **Emphasis = italic** (antiqua italic), e.g. author names *Frisack*, *Scheel*,
  *Pomponatius*, and the running signature *Vid. Sel. Skr. V Deel …*. Wrap each
  italic span in `\emph{}`. (No Fraktur letterspacing/Sperrsatz here.)
- **Long-s** does not occur (antiqua). No `ſ`.

## Orthography — preserve 1807/1810 spelling exactly
- **This printing uses `ö` (o with diaeresis), NOT `ø`.** Seen: Undersögelsen,
  Spörgsmaal, nödvendigt, behövede, Udförelse, Skiönhed, sögt, förer, Fölge,
  förskiellige. Keep `ö` glyph-for-glyph. (Do not "modernize" to ø.)
- **gi- for gj-/gie-:** Gienstande, giöre, Gienstanden. Keep as printed.
- Double vowels (Skiönhed, Maalestok, Såes→Söes), `kj/gj` variants, `-ii-`,
  and `æ` per the image. When in doubt, match the glyph.
- Danish quotes as printed; use the repo's „…" (U+201E … U+201D) if any occur.
- **Footnotes** (if any) marked in print → `\footnote{}` at the anchor word.

## OCR pipeline (antiqua)
```bash
SRC="/sessions/<id>/mnt/bibliotek/Treschow, Niels/videnskabernes-selskabs-skrifter-ser3-bd5-1810.pdf"
# printed page P: PDF = P + 10
PDFP=$((P+10))
# base OCR (archive.org already carries an ABBYY layer):
pdftotext -f $PDFP -l $PDFP -layout "$SRC" -
# verification image (300 dpi) -> copy PNG into outputs, open with Read tool:
pdftoppm -f $PDFP -l $PDFP -r 300 -png "$SRC" /tmp/p
```
**Page-marker convention (match Nielsen/Sibbern):** a `% printed p. NN` marker
must NOT be preceded by a blank line when the page turns mid-paragraph — a blank
line is a LaTeX `\par` and would inject a spurious indent/break. So: mid-paragraph
word boundary → prev text line, then the marker on its own line, then the
continuation (the source newline gives the single space). Mid-word split across
pages → end the prev line with `%` on the broken stem (drop the print's hyphen),
e.g. `...eller Vink%` / `% printed p. 234 ...` / `lernes` → "Vinklernes". Keep a
blank line before the marker ONLY where the boundary is a real paragraph break
(here: pp. 247 and 253). In this essay every other page turn is mid-paragraph.

**Hybrid method:** take the ABBYY/pdftotext words as a base, then render ONE
verification image per page (300 dpi) to (a) fix predictable OCR slips,
(b) catch italic → `\emph{}`, (c) place footnotes/quotes, (d) restore `ö`.
Predictable OCR errors on this scan: **ö misread as o/ö/ő/á** (restore ö from
the image); stray accents on capitals (É, à) from foxing; show-through from the
facing page (ignore the faint mirrored text); long dashes rendered as commas.

## Verification compile (sandbox lacks libertinus — substitute; NOT in real file)
```bash
cd /tmp && D=verT_$$ && mkdir -p $D && cd $D
SRC="/sessions/<id>/mnt/danish-texts/texts/treschow/enslige-ting/transcription.tex"
sed -e 's/\\usepackage{libertinus}/\\usepackage{lmodern}/' -e '/libertinust1math/d' \
    -e 's/\\usepackage\[danish\]{babel}/\\usepackage{babel}/' "$SRC" > t.tex
pdflatex -interaction=nonstopmode -halt-on-error t.tex >l.txt 2>&1
grep -o 'Output written.*' l.txt; echo -n 'char-warnings: '; grep -ic 'not set up\|missing.*character' l.txt
```
Expect 0 char-warnings, 0 errors.

## Notable readings / editorial decisions (image-verified)
- **`ö` throughout**, never `ø` (this printing). 248 `ö` in the body; the only
  `ø` in the file are in the header comment and the modern place-name
  "Kjøbenhavn" in \date.
- **`Dispyt` / `Dispyter`** (pp. 230, 236) — spelled with `y` in the print (two
  occurrences, sing.\ + pl.), not "Disput/Disputer". Kept as printed.
- **`virkekelig`** (p. 241) — printer's line-break dittography ("virke-|kelig")
  for "virkelig"; kept as printed with a `% sic` note at the site.
- **`sympathetiske Blik`** (p. 249) — printed "Blik", not the expected term
  "Blæk" (invisible ink). Kept as printed (600 dpi verified).
- **`Afmindelse`** (p. 248) — rare/nonce noun, "til evig Afmindelse"; as printed.
- **`alexandrinsk`** (p. 246) — confirmed at 600 dpi (not "alexandriask").
- Italics (`\emph{}`, 11 total): first \emph{Aristoteles} (p. 228) and
  \emph{Aristoteles} (p. 253), \emph{Plotin} & \emph{Spinoza} (p. 245),
  \emph{Fichte} & \emph{Schelling} (p. 246), \emph{Linneus} (p. 238),
  \emph{Pomponatius} (p. 253), \emph{rationes seminales} (p. 251), and the two
  running signatures folded into headers. Later name-mentions (Monboddo,
  Hallen, Lamark, Fabricius, Platos, Theseus, Anaxagoras, Democrit, Bonnet,
  Schellingske) are set roman in the print → left roman.
- The key phrase is on p. 240: "de almindelige Begreber kun ere \emph{}Hielpemidler
  til Oversyn, ei til nöiagtig Kundskab om Tingene i sig selv." (Treschow spells
  it *Hielpemidler*; the brief's "Hjælpemidler" is modernized.)
- The thesis restatement is on p. 247: "Der gives altsaa et fast Begreb om
  enslige Ting. Dette Begreb har objectiv Gyldighed eller Realitet."

## Translation terminology (FIXED — keep consistent; chosen with Hans)
Treschow uses two vocabularies that both tempt "individual" in English. They are
kept distinct:

| Danish | English |
|---|---|
| `enslig`, `enslige Ting`, `det Enslige`, `de Enslige` | singular, singular things, the singular |
| `Enslighed` | singularity |
| `Individ`, `Individuer`, `Individualitet` | individual(s), individuality |
| `besynderlig`, `det Besynderlige` | particular (18c sense — NOT "strange") |
| `Hielpemidler til Oversyn` (p.240) | **aids to survey** (matches catalog + Hans's paper) |
| `Begreb` / `Idee` / `Forestilling` | concept / idea / representation |
| `Gienstand` / `Grundform` / `Kiendemærke` | object / fundamental form / criterion |
| `Forstand` / `Fornuft` / `Sands(elig)` | understanding / reason / sense (sensuous) |
| `Kierne` / `Kime` | kernel / germ |
| `Slægt` / `Art` / `Afart` | genus / species / variety |
| `d.~e.` | i.e. |

Note: Treschow's own spelling is *Hielpemidler*; "Hjælpemidler" is modernized.
Emphasis is carried 1:1 (9 spans, all proper names + *rationes seminales*); no
emphasis was added where the print sets roman — including "aids to survey" and
the p.247 thesis sentence, both of which are roman in the original.

## STATE — TRANSCRIPTION COMPLETE
- **All of the essay transcribed & image-verified: title (PDF 233) + body
  printed pp. 225–254 (PDF 235–264).** 30 `% printed p.` markers.
- Compiles 0 char-warnings / 0 errors (18 pp. in the sandbox lmodern substitute;
  real file uses libertinus + textalpha).
- No Rettelser/errata leaf applies.

## Høffding's 1910 excerpt — collation against the complete text

Høffding (ed.), *Udvalgte Stykker af dansk filosofisk Litteratur* (= *Mindesmærker
af Danmarks Nationallitteratur* III, Gyldendal 1910). Copies in
`~/bibliotek/Høffding, Harald/`: `mindesmaerkerafd03ande.pdf` (Internet Archive —
**much cleaner OCR**, use this one) and `udvalgte-stykker.pdf` (HathiTrust /
Wisconsin — jumbled OCR).

The 1810 essay appears in section **IV, "Den psykologiske Skole (Treschow,
Sibbern, Howitz)"**, under Høffding's own title — not Treschow's:

> **TRESCHOW: DET INDIVIDUELLES UUDTØMMELIGHED**
> ("The Inexhaustibility of the Individual"), anthology pp. 100–109
> (= IA PDF pp. 105–114; anthology offset PDF = printed + 5)

A **second** Treschow excerpt, **"TRESCHOW: UDVIKLINGSLÆRE"**, follows at
anthology p. 110 (IA PDF 115 ff.) — developmental/cosmogonic material, relevant
to the teleology strand.

**What Høffding kept and cut** (collated mechanically: 12 evenly-spaced 30-char
probes per printed page, matched against the anthology OCR; FULL = 10–12/12):

| Original printed pp. | In the 1910 excerpt |
|---|---|
| 225–229 | **kept** (full) |
| 230 | partial (opening of the metaphysics-of-singularity discussion) |
| **231–234** | **cut** |
| 235–240 | **kept** (full) |
| **241–254** | **cut** |

So the excerpt **ends exactly at the "Hielpemidler til Oversyn" passage (p. 240)**
and goes no further.

**What this means for the Bohr/Høffding transmission argument.** What reached
Bohr's milieu was the *epistemological* Treschow only:

- kept — the Begreb/Idee/Forestilling distinction; the sciences' neglect of the
  individual; Aristotle and the unrefuted Platonic Ideas; the central question
  whether each human has a Grundform; self-consciousness as the foremost
  expression of individuality; the dissolving boundaries between species
  (Monboddo, Hallen, Lamarck, Fabricius); Linnaeus and Kant on races; nature
  proceeding only gradually; and the "aids to survey" thesis.
- cut — Plato/the Neoplatonists/Schelling and the souls-as-drops-of-ocean
  passage (231); the rights-and-personality argument against treating persons as
  mere means (232); Theseus's ship, Anaxagoras, the circle/sphere and the Godhead
  as most perfect individuality (233–234); **the entire second half (241–254)**:
  the identity-system exposition, Plotinus/Spinoza/Fichte/Schelling, **the thesis
  restatement at p. 247** ("Der gives altsaa et fast Begreb om enslige Ting.
  Dette Begreb har objectiv Gyldighed eller Realitet"), Democritus, germs and
  preformation, "each is this whole itself under his own peculiar form" (251),
  nature as a perfect organic whole (252), Aristotle on providence and
  Pomponatius (253), and the closing on egoism (254).

In short: Høffding transmitted the limits-of-general-concepts epistemology and
dropped the monistic metaphysics *and* the claim that the concept of singular
things has objective validity. Note also a tension worth exploiting — in *Danske
Filosofer* (1909) Høffding calls the essay "directed against Schelling," yet in
the anthology he cuts both Schelling passages (231 and 246).

## STATE — TRANSLATION COMPLETE
- **translation.tex covers the whole essay, printed pp. 225–254**, mirroring
  transcription.tex 1:1: same 30 `% printed p.` markers in the same order, same
  37 body paragraphs, same 9 `\emph{}` spans.
- Compiles 0 errors / 0 char-warnings (18 pp. in the sandbox lmodern substitute).
- Printer's errors carried as printed in the Danish with `% sic`, and silently
  normalized in the English: p.234 "en" for "end" (→ "than"); p.234 "Ikke de
  mindre" for "Ikke desmindre" (→ "Nevertheless"); p.241 "virkekelig" (→ "really").
- Both files now ready for a local compile with the real fonts (libertinus +
  textalpha); catalog.yaml section set to `complete`.
