# RESUME-NOTES — Sibbern, *Om Erkjendelse og Granskning* (1822)

State for the **transcription** of this book. Update after each batch.
The user compiles/commits/pushes — never the assistant.

Source of truth: `transcription.tex` (Danish), ✓ **TRANSCRIPTION COMPLETE**
(front matter + §§1–22 + Slutning + Rettelser errata leaf; body pp.3–204 + p.205 errata).
NB: §§21–22 (pp.165–204) have now had a full image proof pass (2026-07-19):
72 corrections applied against the scans, mostly Sperrung/\emph{} fixes plus a
handful of word-level OCR/orthography fixes (listed below).
See `../../../TRANSLATION-PLAYBOOK.md` for the standing method.

## Edition & source

- Scan: `~/bibliotek/Sibbern, Frederik/Om_Erkjendelse_og_Granskning.pdf`
  (Google Books, Nottingham copy, **234 PDF pages**, OCR draft; verify every page
  against the image). Second scan has a near-empty text layer — use the first.
- **Edition:** Kjøbenhavn 1822, Paa Fr. Brummers Forlag, Trykt hos C. Græbe.
- Typography: **whole book Fraktur**; Latin/German in antiqua — kept inline,
  verbatim, no italics. In Fraktur the initial glyph for I/J is shared: the word
  is "Iagttagelse(saand)" though it can look like "Jagttagelse" — rendered with I.
- **Heavy letterspaced emphasis (Sperrung)** → `\emph{}`. **273 spans through
  p.152.** A dedicated emphasis-proofing pass is worthwhile.

## Page map (verified: printed headers + Oversigt)
- Front matter (roman): `printed = PDF − 6`. Body (arabic): `printed = PDF − 22`.
  §.1 opens p.3 = PDF 25.

### Section → printed-page map (from the Oversigt; verified through §16)
§1 p.3 · §2 p.18 · §3 p.24 · §4 p.29 · §5 p.36 · §6 p.48 · §7 p.55 · §8 p.72 ·
§9 p.88 · §10 p.104 · §11 p.112 · §12 p.116 · §13 p.120 · §14 p.128 · §15 p.133 ·
§16 p.146 · §17 p.153 · §18 p.159 · §19 p.160 · §20 p.162 · §21 p.165 · §22 p.194.
Body ends ~p.203; then the **Rettelser** errata leaf. (To convert to PDF: +22.)

## CURRENT RESUME POINT
**DONE — whole book transcribed.** Body §§1–22 (pp.3–204), the Slutning
(1 Cor. 13; ends "Salige ere de, som ere fattige i Aanden"), and the
**Rettelser** errata leaf (p.205), reproduced verbatim at end of file.
Sandbox substitute compile: **108 pp., 0 warnings, 0 errors; 321 \emph spans.**
Optional follow-ups (not transcription): emphasis/image proof pass on §§21–22
(pp.169–204, drafted lighter from OCR); Hans's Rettelser decision (kept verbatim
for now); English translation.tex (separate future job, not started).

## DONE so far (don't redo)
- **batch 0** Front matter.  **1** §1 pp.3–12.  **2** §1–2 pp.13–22.
  **3** §2–4 pp.23–32.  **4** §4–5 pp.33–42.  **5** §5–6 pp.43–52.
  **6** §6–7 pp.53–62.  **7** §7–8 pp.63–72.  **8** §8 pp.73–82.
  **9** §8–9 pp.83–92.  **10** §9 pp.93–102.  **11** §9–11 pp.103–112.
  **12** §11–13 pp.113–122.  **13** §13–14 pp.123–132.  **14** §15 pp.133–142.
  **15** §15–16 pp.143–152.  **16** §16–20 pp.153–162.  **17** §20–21 pp.163–172.
  **18** §21 pp.173–182.
  Whole file (front matter + §§1–21 through p.182) compiles in the sandbox
  substitute recipe: **97 pp., 0 warnings, 0 errors; 314 \emph spans.**
  New flags: Greek Epictetus phrases p.167; "Fordølgelse" p.171 (OCR); "Enigmord/
  Saul" p.179 (OCR, uncertain word). §§17–20 cover method, genius, self-thinking,
  doubt; §21 the "trial by fire" of study, incl. the theology-student passage,
  Indifferentism/Intolerance/Tolerance, and "the way to truth goes through error."
  (§§14–16 cover the dialectic, system/method, and Detail + the observation-spirit;
  §13's aphorism on results and §15's warnings against Nebulisterie/crystallization
  are highlights. Refs to Plato's Parmenides, Goethe, the Dutch painters.)

## Open decision for Hans
- **Rettelser (errata) leaf** (~end): apply corrections silently, or footnote?


## PROOF PASS — §§21–22, pp.165–204 (2026-07-19)
Four parallel readers compared every page against the 300 dpi scan. 72 fixes
applied; file recompiles clean (108 pp., 0 warnings, 0 errors; 383 \emph spans,
up from 321). Most were emphasis (letterspacing) corrections. Word-level changes
worth a scholar's glance (all read off the image, but noted for the record):
- p.167 "Naarvaagenhed" -> "Aarvaagenhed"
- p.172 "til at finde" -> "til at sande"
- p.174 "som er foran" -> "som er fore"
- p.176 "Større bliver Faren" -> "Større blive Faren"
- p.177 "har vist sig" -> "har viist sig"
- p.178 "for at gjøre den gjeldende" -> "før at gjøre den gjeldende"
- p.179 "det Enigmord, Saul begik" -> "det Snigmord, Saul begik" (resolves old FLAG)
- p.179 "forkastelig Tankemaade" -> "Tænkemaade"; full stop added after "til."
- p.184 "til ægte Videnskabelighed" -> "til al ægte..." (dropped word restored)
- p.184 "derved fremkaldte" kept (scan looks like broken "derve"; left as derved) — VERIFY
- p.186 "fattede og overskuede" -> "fattede og oversaae"
- p.194 "practiske Udøvelse" -> "practisk Udøvelse"
- p.203 "havde Prophetie" -> "havde al Prophetie"; "Blik at see" -> "Blik at skue"
Greek verified: αὐτὸς ἔφα, φύσις, ὠδίς all correct (ὠδίς kept with acute — grave
would need no following punctuation; a comma follows). Comma after (φύσις) removed
per scan.

## Conventions
- `book` class, libertinus; 1822 orthography verbatim; em-dash `---`; printed
  rules → centred `\rule`; Danish quotes „…“; Greek inline (textalpha);
  Latin/German inline; letterspacing → `\emph{}`.

## Spot-checks / inline FLAGs (verify against scan when proofing)
Earlier flags stand (front matter + §§1–13; see prior notes / git history).
New this round (§§13–16):
- **p.131→132** seam "til Ba-sis" (basis) — B/V and sis/sig Fraktur; rendered
  "Basis" by sense.
- **Iagttagelse / Iagttagelsesaand** (§§15–16, pp.144–150) — print shows the
  I/J-shared Fraktur glyph ("Jagttagelse"); rendered with I throughout, matching
  the body's earlier "Iagttagelser" (pp.75–76).
- **p.146** "Jagttagelsesaand" → "Iagttagelsesaand" (same I/J point).
- General: §§13–16 again dense with multi-word Sperrung (e.g. p.128 "construere
  det videnskabelige Hele", p.143 "at tage fra en vis Side"/"Mueligheden af flere
  Fremgangsmaader eller Methoder", p.147 "Spørsmaal og Problemer", p.151
  "Interesse og Glæde ved Detaillet") — marked from 300 dpi; second pass advised.
