# Translation hand-off — R. Nielsen, *Om Theologiens Naturbegreb* (1855)

Point a fresh Claude session at this file **together with**
`../../../TRANSLATION-PLAYBOOK.md` (the standing method for every book in this
repo). This file records only what is specific to *this* text. The Danish
transcription is **complete and image-verified** (printed pp. 3–47), so the
translation phase can begin immediately.

---

## 0. Status & files

- `transcription.tex` — Danish, **COMPLETE** (0 markers, compiles 0/0, 32 pp.).
  **This is the source of truth. Translate FROM it, never from the scan.**
- `translation.tex` — English. Preamble is ready (includes `textalpha` for the
  p.34 Greek and `enumitem`). The body holds **5 batch markers** in reading
  order; fill them one batch at a time.
- Scan (reference only): `~/bibliotek/Nielsen, Rasmus/theologiens_naturbegreb.pdf`.
  **Offset: PDF = printed + 6** (printed p.3 = PDF 9; last text page p.47 = PDF 53).
- Title already set in the stub: **"On Theology's Concept of Nature, with Special
  Reference to Malebranche: *De la recherche de la vérité*."**

**The user (Hans) commits and pushes. The assistant never does.**

---

## 1. What this book is (so you translate the right thing)

An 1855 university *Indbydelsesskrift* (invitation programme) for the Reformation
festival. It has two clearly separate parts:

1. **The treatise, printed pp. 3–37** — Nielsen's philosophical essay arguing
   that theology and natural science share no common concept of nature. It works
   through **Malebranche** (occasionalism, "seeing all things in God") as the
   consistent example of the theological view, then criticises **Leibniz**, then
   closes by echoing its opening sentence. This is the substance; translate it in
   full and with care.
2. **The appendix, printed pp. 38–47** — the standard programme matter: three new
   doctors' autobiographical **vitae** (Salomonsen, Müller, Helweg) and the formal
   **festival invitation** ending "Under Universitetets Segl." + the seal. Plain
   19th-century prose; no philosophical content.

The essay is continuous — **no chapter or section headings** anywhere. The
transcription marks structure only with `% p. N` page comments and centred rules
`\begin{center}---\end{center}`. Mirror that: continuous prose, reproduce each
centred rule at the same break, and keep the `% p. N` comments if you like them
for alignment.

---

## 2. Decisions for Hans (resolve before or during batch 1)

- **Appendix scope.** Do you want the vitae + invitation (pp. 38–47) translated,
  or is the treatise (pp. 3–37) the deliverable? The final marker in
  `translation.tex` is flagged "TRANSLATE ONLY IF IN SCOPE." Default assumption:
  translate everything for completeness, but it's low priority relative to the
  essay.
- **Leibnitz vs. Leibniz.** The Danish prints "Leibnitz." Standard English is
  "Leibniz." Recommend modernising to **Leibniz** in the English (the playbook
  keeps proper names, but this is a spelling-modernisation call). Pick one and be
  consistent.
- **"Aand" = mind or spirit?** In the Malebranche epistemology (pp. 7–15) `Aand`
  renders Malebranche's *esprit* = **mind** ("the mind's essence is thought").
  In the theological stretches (Trinity, Holy Spirit) it means **spirit**.
  Recommend translating by sense, not one-to-one; note your choice per passage.

---

## 3. Batch plan (≈10 printed pages each; markers already in `translation.tex`)

1. **pp. 3–10** — opening; theology vs. natural science; Malebranche introduced;
   the long Malebranche quotations begin (heavy French footnotes from here on).
2. **pp. 11–20** — Malebranche on mind, modifications, ideas, seeing all things in
   God; the centred maxim **"Que nous voyons toutes choses en Dieu."**
3. **pp. 21–30** — the occasionalist system (*systema causarum occasionalium*);
   Leibniz criticised; creation vs. conservation; "Naturens Væsen."
4. **pp. 31–37** — faith vs. understanding; Athanasius/Arius (**Greek on p.34**);
   creation vs. birth; the treatise closes by repeating its first sentence.
5. **pp. 38–47** — appendix (vitae + invitation), if in scope.

After each batch: compile (sandbox recipe in the playbook §3), report, hand back.

---

## 4. Book-specific handling rules

These extend the playbook §2 conventions. Where this book differs, follow this
list.

- **Malebranche quotations (the bulk of pp. 6–21).** These are *Nielsen's Danish
  renderings* of Malebranche, set in Danish low-high quotes „…". **Translate the
  Danish into English** and keep the quotation marks (English `` ``…'' ``). Do
  **not** back-translate from the French footnotes.
- **French footnotes (`\footnote{…}` throughout pp. 6–29).** These are
  Malebranche's **original French**, quoted as primary-source citations. **Leave
  them verbatim in French — do NOT translate them.** Just carry each `\footnote{}`
  across to the same anchor word. (This is the opposite of the playbook's usual
  "translate the note" rule, because here the notes *are* the source text.) Keep
  the "S. NNN." / "Jvnf." page references as printed.
- **Inline French parentheticals** — e.g. `(un sentiment confus)`,
  `(l'entendement)`, `(la volonté)`, `(vers le bien en general)`. These gloss
  Nielsen's Danish with Malebranche's French; **keep them verbatim** in the
  English, exactly as they stand in the Danish.
- **Latin phrases and scripture** — inline Latin (`credo, ut intelligam`, `fides
  præcedit intellectum`, `dixit et facta sunt`, `nihil negativum`,
  `harmonia præstabilita`, the p.16 Vulgate quotations, `Soli Deo honor et
  gloria`, etc.). **Keep the Latin verbatim** (wrap in `\textit{}` if you want it
  visually marked; the transcription left it plain roman). Do not translate;
  optionally add a short English gloss in brackets only where a reader would be
  lost. The Latin dissertation titles in the vitae stay as printed.
- **Greek (p.34)** — `(ὁμοούσιος)`, `(θεία φύσις)`, and the footnote Aristotle
  quote. **Copy the glyphs verbatim** from `transcription.tex`; translate only the
  surrounding Danish prose. `textalpha` is already in the preamble. NB: the
  sandbox has no greek-fontenc, so verify the Greek on a **local** compile.
- **Emphasis.** Danish `\emph{}` (letterspacing in the original) → keep `\emph{}`.
  In the vitae, candidate names are `\textbf{}` and family/official names are
  `\emph{}` — **carry these over unchanged**; don't re-decide them.
- **Section-break rules** `\begin{center}---\end{center}` → reproduce at the same
  points (after the p.6 intro; after the p.22 Malebranche block; on p.30; the two
  on p.37 around the closing line; before each vita heading; on pp. 46–47).
- **Numbered vita heads** `\begin{center}\textbf{1.}\end{center}` (…2., 3.) →
  keep as is.
- **Danish work-titles in the vitae** stay in Danish inside „…" quotes (e.g. „Om
  Tro og Viden", „Den Danske Psalmedigtning"); the French/Latin titles (De
  resurrectione…, *Numismatique d'Alexandre le Grand*) stay as printed.
- **Proper names** (Malebranche, Athanasius, Arius, Kant, Strauß, Descartes,
  Thorvaldsen, Grundtvig, …) unchanged, except the Leibnitz/Leibniz call in §2.
- **Register.** Scholarly, moderately literal but readable English. Nielsen's
  prose is aphoristic and antithetical ("nothing and yet really something"; "faith
  in the Oratory, understanding in the Laboratory"); preserve the parallelism.

---

## 5. Terminology glossary (keep consistent across the whole essay)

| Danish | Suggested English |
|---|---|
| Naturbegreb | concept of nature |
| Naturlære(n) | natural science / the doctrine of nature |
| Naturvidenskab | natural science |
| Erfaringsvidenskab | empirical science |
| Naturfornegtelse | negation of nature |
| det Skabte | the created (that which is created) |
| Skabelse; Skabelsesdogmet; Skabelseslære | creation; the dogma of creation; the doctrine of creation |
| Opholdelse | conservation / preservation ("conservation is a continued creation") |
| Almagt; den Almægtige | omnipotence; the Almighty |
| Anledningsaarsag | occasional cause (*causa occasionalis*) |
| sand / virkelig Aarsag | true / real cause |
| Occasionalsystem; Occasionaltheori | occasionalist system; occasionalist theory |
| Vorden | becoming |
| Væsen | essence / being (Naturens ~ = nature's essence; Aandens ~ = the mind's essence) |
| Væsenhed | substantiality / essential being |
| Aand | mind (Malebranche's *esprit*) / spirit (theological) — see §2 |
| Materie; det Udstrakte | matter; the extended |
| Modification(er) | modification(s) |
| Idee(r) | idea(s) |
| Sandser; Sandsning; Sandseindtryk | senses; sensation; sense-impression |
| Forstand(en) | understanding / intellect (*l'entendement*) |
| Villie(n) | will (*la volonté*) |
| Forestilling | representation / idea |
| Vildfarelse | error |
| Intet; Noget | nothing / naught; something ("nothing and yet really something") |
| Mirakel | miracle |
| Grændse | limit / bound |
| Selvvirksomhed; Selvstændighed | self-activity; independence / self-subsistence |
| Tro | faith |
| Væsenseenhed (ὁμοούσιος) | unity of essence / consubstantiality |
| Anskuelse | view / conception |
| Conseqvens; conseqvent | consistency (logical) / consequence; consistent |
| Eensidighed | one-sidedness |
| Grundsætning | principle / fundamental proposition |
| Fornuftidee | idea of reason |
| Kjendsgjerning | fact |
| Phænomen | phenomenon |
| Skin og Skygge | semblance and shadow |
| Blændværk | illusion / delusion |

Keep the Latin tags (`credo ut intelligam`, `fides præcedit intellectum`) in
Latin rather than translating them inline.

---

## 6. Finishing (playbook §6)

When `grep -c 'text to be added' translation.tex` = 0 and it compiles 0/0:
1. Final sandbox compile → confirm pages, 0 errors, 0 char-warnings.
2. In `../../../../catalog.yaml`, set the `theologiens-naturbegreb` section
   `status:` from **in-progress → complete**.
3. Tell Hans to compile both PDFs locally with the real fonts (libertinus +
   textalpha) and confirm the Transcription + Translation links resolve — and to
   eyeball the p.34 Greek, which the sandbox cannot render.
4. Hans commits & pushes. You don't.
