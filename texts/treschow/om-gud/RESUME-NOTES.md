# Niels Treschow — *Om Gud, Idee- og Sandseverdenen* I (1831): resume notes

Selective transcription: **two spans from vol. I, printed pp. 202–207 and
220–221**, not the volume (379 scan pp.) and not the trilogy (vols. II 1831,
III 1832, both also on disk). Companions: `../enslige-ting/` (1810 essay),
`../almindelig-logik/` (§§ 26–35).

## Why these spans
They settle a problem raised by *Almindelig Logik* § 31 (1813), where Treschow
denies that the highest being is "noget Heelt, som Verden, hvoraf alle Individuer
ere Dele," and blames pantheism and the emanation-system on that confusion. Read
alone, § 31 seems to contradict the monism of the 1810 essay (p. 251, "enhver er
dette Hele selv under sin særegne Form"). **They are consistent**, and these
pages show how — see Findings.

## Scan, offset, type
- Scan: `~/bibliotek/Treschow, Niels/om-gud-idee-og-sandseverdenen-1-1831.pdf`
  (379 scan pp.), from nb.no IIIF `URN:NBN:no-nb_digibok_2008040213001`,
  public domain, "Tilgang for alle".
- **Offset: scan = printed + 54** (verified at both ends: p. 202 = scan 256,
  p. 207 = scan 261, p. 220 = scan 274, p. 221 = scan 275). The large offset is
  the prefixed autobiography, *Forfatterens Levnet som Fortale*. Re-verify
  before working elsewhere in the volume, and separately for vols. II and III.
- **FRAKTUR**; emphasis = letterspacing → `\emph{}`. Orthography uses **ø**
  (as in the *Logik*, not the **ö** of the 1810 antiqua essay). Later spelling:
  `Idee`, `Sandseverden`, `Gjenstand`, `gjøre`, `Bevidsthed`.

## How the spans were located (no OCR needed)
nb.no's content-search endpoint, one call per term, then read the page images:

```bash
ID=744d25724c6a9bb8c825bcc9186eaef1   # Om Gud, Første Bog
curl -s "https://api.nb.no/catalog/v1/contentsearch/$ID/search?q=Heelt"
# page numbers are in the annotation ids: digibok_<urn>_(\d{4})
```

Term map for vol. I (scan pages): `Heelt` → 79, 88, 112, 114, 116, 137, 175,
184, 186, 207, 212, **221**, **274**, **275**, 371 · `Individ` → 148, 169, 181,
209, 222, **256, 258, 259, 260, 261**, 275, 280, 281, 301, 333, 370 · `Dele`,
`Deel` → widely scattered (46 pages each) · `Pantheisme`, `Emanation`,
`Totalitet` → 0 hits (token-exact search; try inflected forms).
Scan 275 is the only page carrying both `Heelt` and `Individ` — which is why it
was read first, and it proved to be the decisive one.

## Findings

**1. The monism is structural, not mereological.** p. 220: "In the ideal world,
as in the real, a constant reciprocity (*Vexelvirkning*) must obtain: otherwise
it could constitute no actual unity, no whole. Its members must be able to
communicate themselves, to know one another, without their state being thereby
altered." The unity of the ideal world is constituted by reciprocal relations
among Ideas that do not alter one another — a relational unity, not composition.

**2. Individuals compose the sense-world, not God.** p. 221: "These are the
individuals of which the sense-world consists" (*Disse ere de Individuer, hvoraf
Sandseverdenen bestaaer*). So *Logik* § 31's denial is exactly right on its own
terms, and the 1810 "each is this whole itself under his own peculiar form"
should be read via p. 221's closing line: "In every sensible individual its Idea
thus reveals itself as in an image ever proper to it" — expression, not parthood.
**This retires the mereological reading of 1810 p. 251.**

**3. The identity-system principle, stated.** p. 221: "According to the
principles of the identity-system we shall not be deceived in this either; for
essentially the highest and the lowest things are entirely alike."

**4. The strongest statement of the target position anywhere in the corpus**
(p. 207): "all *class-, genus- and species-concepts are more or less wavering and
indeterminable, whereas the individuals are in themselves so perfectly
determinate that a change or transition from one to another is impossible*, while
an individual, by contrast, may very well pass over into another species, genus,
order or class than the one to which it at present belongs." Determinacy at the
level of individuals, indeterminacy at every level of classification, and
individuals migrating across taxa while remaining themselves. Also: "Socrates and
Alcibiades just as much remain for all eternity Socrates and Alcibiades as the
animal an animal."

**5. Against Plato, and the Dasgupta inverse in his own words.** p. 206: the
theory "differs essentially from the Platonic in this, that the latter makes the
Ideas into the objects of general concepts" — Treschow's Ideas are *individual*.
And p. 202: "only individuals, not genera and species, are in every respect so
determinate that they can exist for themselves."

**6. A caution for the reading of "emanation".** Treschow uses *Udflydelse*
(outflowing) of both Ideas and sensible things at p. 203 — "Both kinds of being
are outflowings of the same, but in a different way: partly immediate, partly
mediate" — while the *Logik* § 31 rejects "Emanations Systemet". The rejection is
of composition, not of derivation; don't read § 31 as denying emanation in this
weaker sense.

## STATE
- **DONE:** both spans transcribed, all 8 pages image-verified, and translated.
  Each file 5 pp., compiles 0 errors / 0 char-warnings, exact 1:1 parity
  (8 page markers, 2 span headings, 6 `\emph{}` spans in each body).
- `catalog.yaml`: entry updated under Treschow, `om-gud-idee-sandseverdenen`.
- **Possible next steps:** p. 207 promises "a separate division of the following
  book" on why Socrates and Alcibiades persist — i.e. **vol. II**, which would be
  the natural continuation. The `Heelt` cluster at scan 112–116 (printed 58–62)
  is unexamined and may bear on the whole/part question earlier in the argument.
