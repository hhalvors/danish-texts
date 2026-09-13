# Notes and essays

How scholarly commentary gets written, stored, and published. Read this before
adding a note; read TRANSCRIPTION-PLAYBOOK.md or TRANSLATION-PLAYBOOK.md if the
job is producing a text rather than writing about one.

## Why this exists

Before this, commentary had three homes and no rules about which to use:

1. `catalog.yaml`'s `note:` field — one plain-text paragraph per work, rendered
   through `H.toHtml`, so **no markup survives**. It silted up: the note for
   *Evangelietroen og den moderne Bevidsthed* carried bibliography, transcription
   status, the three emphasis devices, the unreliable *Rettelser* leaf and the
   307-page unclosed quotation, all in one flat block.
2. `~/hhalvors.github.io/pages/danish-texts-notes.md` — 536 hand-written lines,
   parallel in structure to the catalog, linked to it by nothing, and already
   drifting: it had entries for nine Nielsen works and none for the 1849 book.
3. The comment header of `transcription.tex` — the only channel that was both
   durable and tracked, which is why the root `.gitignore` sends the scholarly
   record there. But no reader of the website ever sees it.

The fix is not a bigger `note:` field. It is to give commentary its own files,
beside the texts, and to make the catalog *link* to them rather than contain them.

## The two kinds

**A note** is about one work. It lives in that work's directory and is named
`note.md`:

    texts/nielsen/evangelietroen-bevidsthed/note.md

**An essay** is an argument that spans works, authors, or the whole collection.
It lives at the repo root under `essays/`:

    essays/nielsen-heterogeneity-1849.md

If you are describing a book, write a note. If you are arguing for a conclusion,
write an essay. A piece that compares three books to date a doctrine is an essay
even though it began as a question about one of them.

## Front matter

Both kinds carry YAML front matter. Fields not marked optional are required, and
a missing one fails the site build.

### Note

```yaml
---
kind: note
author: nielsen                     # must equal an authors[].id in catalog.yaml
work: evangelietroen-bevidsthed     # must equal a works[].id under that author
title: "Evangelietroen og den moderne Bevidsthed"
updated: "2026-08-30"
abstract: >
  One or two sentences. Shown on the notes index and used as the page
  description. Not a summary of the book — a summary of the note.
---
```

### Essay

```yaml
---
kind: essay
title: "Before the Heterogeneous Magnitudes"
subtitle: "Rasmus Nielsen in May 1849"      # optional
updated: "2026-08-30"
about:                                      # every catalog *work* this bears on
  - author: nielsen
    work: evangelietroen-bevidsthed
  - author: nielsen
    work: johannesclimacos
  - author: nielsen
    work: evangelietroen-theologien
about-authors:                              # every catalog *author* this bears on
  - nielsen                                 # (optional — see below)
abstract: >
  One or two sentences.
---
```

`about:` is what does the work-level cross-linking: each listed work gets an
"Essay" badge in its catalog row pointing here. Use it for a piece that is
about specific books — arguing a claim across two or three of them, say.

`about-authors:` does the same thing one level up: each listed author id gets
an "Essay" badge beside their bio, above the works list, rather than on any one
work's row. Use it for a piece that is about the *person* — a biography, an
account of their place in a movement — where attaching the badge to one work
among several would be arbitrary, and attaching it to all of them would be
noise. A piece can carry both `about:` and `about-authors:`, or either alone.

An essay with both empty or absent is still published and still listed on the
notes index; it just is not reachable from any catalog entry. That is allowed,
and occasionally right — a piece about the collection as a whole belongs to no
single work or author.

`slug:` is optional on an essay and defaults to the filename. Set it only when
renaming a file would otherwise break a published URL.

## The id contract

`author` and `work` are **not free text**, and so are the ids under
`about-authors:`. They are foreign keys into `catalog.yaml`, and the site
build resolves every one of them. An id that matches nothing aborts the build
with the offending file and key named — the
same discipline as the `links: []` requirement, and for the same reason: a
silent mismatch is a note that exists but that no reader can find.

This is the whole anti-drift mechanism. There is no field in `catalog.yaml`
saying "this work has a note." The site discovers notes by looking, so the
catalog cannot fall out of step with them.

## What goes in a note, and what stays in catalog.yaml

`note:` in `catalog.yaml` is a **catalog blurb**: two or three sentences saying
what the book is and what state our edition is in. Someone scanning the browse
list should be able to read it in one breath.

Everything longer goes in `note.md`. The conventional shape, in order:

- an opening paragraph on what the book is and why it is in the collection
- **The text** — what our edition covers, and its state
- **Editorial note** — page map, errata, emphasis devices, normalisation
  conventions, logged printer's defects: the diplomatic record
- **Reading** — content, argument, connections, open questions

Only the first is obligatory. Use `##` for these; `#` is reserved for the page
title, which comes from the front matter.

The editorial section and the comment header of `transcription.tex` say the same
things, and this is deliberate: the header travels with the LaTeX source for
whoever clones the repo, the note travels to the website for whoever reads it.
When you change one, change the other. The header stays the authority — it is
written at the page, against the image, while the transcription is being made.

## Writing conventions

- Quote Danish as our edition prints it, including transcribed printer's
  defects, and say so when a defect falls inside a quotation. `Naturloveu` with
  the turned sort is evidence of the edition's method; silently correcting it
  throws that away.
- Cite by **printed page**, not by PDF page and not by line number in the `.tex`.
- Give translations for quotations of more than a few words. The audience reads
  philosophy, not necessarily Danish.
- Claims that can be checked against the repo should say how. A word-frequency
  claim should give the figure, the denominator, and enough of the method that
  someone can rerun it.
- Markdown is processed by Pandoc with the site's reader options: math in
  `$…$` works, raw HTML works, footnotes work.

## Publishing

Notes and essays are **tracked** — unlike the per-book harness, which the root
`.gitignore` keeps off git. `publish-danish.sh` stages `catalog.yaml`, `texts/`
and `essays/`, so a new note is committed by the ordinary publish run with no
extra step.

The site reads them through two symlinks:

    ~/hhalvors.github.io/dansk-src    -> ~/danish-texts/texts
    ~/hhalvors.github.io/dansk-essays -> ~/danish-texts/essays

and builds:

| Source | URL |
|---|---|
| `texts/<author>/<slug>/note.md` | `/dansk/<author>/<slug>.html` |
| `essays/<slug>.md` | `/dansk/essays/<slug>.html` |
| all of the above | `/dansk/notes.html` (generated index) |

`/dansk/notes.html` used to be a hand-written page in the site repo. It is now
generated from these files, so nothing is written there by hand.

## Adding a note

1. Write `texts/<author>/<slug>/note.md` with front matter.
2. Check the `author` and `work` ids against `catalog.yaml`.
3. Trim that work's `note:` in `catalog.yaml` to a blurb if it has silted up.
4. `./publish-danish.sh "note on <work>"` — from `~/hhalvors.github.io`.

The build fails loudly on an unresolved id. That is the intended behaviour; fix
the id rather than working around it.
