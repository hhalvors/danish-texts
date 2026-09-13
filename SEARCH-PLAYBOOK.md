# Searching and reading the corpora

Two files do this work, and they live in a separate repository,
`~/sks-search`, a sibling of this one (the user posts it to GitHub separately):

- `sks_search.py` — builds the index and answers queries. Standard library only.
- `sks.el` — the Emacs interface. Everything it does, the script can do too.

It was split out of `danish-texts` once the core search behaviour stabilised,
so it could be reused (and shared) independently of this edition. It knows
nothing about `danish-texts` by default; **`$SKS_TEXTS` is what tells it where
our `texts/` tree is**, so that our own transcriptions and translations join
the SKS corpus in the index.

The question they exist to answer is: *does he say anything about X, where, and
what exactly does he say around it.*

## Setup, once

```sh
cd ~/sks-search
export SKS_TEXTS=~/danish-texts/texts   # so our own texts/ get indexed too
python3 sks_search.py index             # ~40 s, writes _working/sks_index.sqlite
```

`$SKS_TEXTS` has to be set in whatever shell runs `sks_search.py index` — export
it in your shell profile, or set it inline as above every time, or `(setenv
"SKS_TEXTS" "~/danish-texts/texts")` before requiring `sks` in Emacs (see below).
Without it, `sks_search.py` still works, but only over the SKS edition itself —
the `texts`, `translations`, `danish-texts`, `ebooks` and `everything-danish`
corpora described below come up empty.

In your Emacs init:

```elisp
(setenv "SKS_TEXTS" "~/danish-texts/texts")
(add-to-list 'load-path "~/sks-search")
(require 'sks)
(global-set-key (kbd "C-c k") #'sks-search)
```

`(setenv ...)` is needed even though the path looks like a plain string: Emacs's
`call-process` inherits `process-environment`, not the shell's, and `sks_search.py`
never sees the variable otherwise.

The index is derived data and lives in `~/sks-search/_working/`, which is
gitignored. Delete it and rebuild whenever you like; nothing depends on it but
speed.

## What is indexed

| Corpus name | What it is | Units |
|---|---|---|
| `journals` | SKS journals AA–KK, NB–NB36, notebooks Not1–15 | 6,529 entries |
| `papirer` | the loose papers, SKS 27 | 847 |
| `letters` | letters and dedications, SKS 28 | ~3,000 paragraphs |
| `published` | the published works | ~12,500 paragraphs |
| `sks` | all of the above | ~23,000 |
| `texts` | our own `transcription.tex` files | 23,539 paragraphs |
| `translations` | our own `translation.tex` files | 13,480 paragraphs |
| `danish-texts` | both of ours | 37,019 |
| `ebooks` | privately-owned epub reissues — see below | 7,126 paragraphs |
| `everything-danish` | ours plus the e-books | 44,145 |
| `all` | everything | 67,147 |

Each SKS entry carries its journal reference (`NB22:21`), date, *Papirer*
number for cross-referencing Hong, and SKS volume and page. Each paragraph of
ours carries its book and printed page where the source marks one.

## The `ebooks` corpus — privately owned, never published

Høffding wrote far more than we will ever transcribe. SAGA Egmont / Lindhardt
& Ringhof have reissued much of him as clean, well-set epub, and a purchased
copy indexed locally answers *does he discuss X, and where* across the whole
of him rather than across the handful of books we have keyed by hand. That is
the only thing this corpus is for. Typically you search `ebooks` to find the
passage, then read it in the epub — or, if it earns a place in the edition,
transcribe the page from the KB scan in the ordinary way.

The files live beside the edition as `texts/<author>/<slug>/*.epub`. Three
lines of defence keep them out of the public repo, and all three matter:

1. `*.epub` is in the root `.gitignore` (as are `.mobi`, `.azw*`, `.kepub`).
2. Nothing writes extracted text to disk. The text goes only into
   `_working/sks_index.sqlite`, and `_working/` is gitignored entire.
3. Results are shown as KWIC snippets, the same as everything else.

So: **do not commit an epub, do not paste an extracted chapter into a `.tex`
file, and do not put e-book text on the site.** These are in copyright. The
catalog links to Saxo so a reader can buy their own copy; that is the whole of
what we publish about them.

```sh
./sks_search.py search Irrationalitet -c ebooks
./sks_search.py search 'NEAR(Totalitet* Person*, 25)' -c ebooks
./sks_search.py search Kontinuitet -c everything-danish   # ours + e-books
./sks_search.py read 'hoeffding/religionsfilosofi(epub):412'
```

Two things behave differently here, both on purpose:

- **The locator is a chapter heading, not a page.** A reflowable epub has no
  printed pagination, so a hit cites `(Religionsfilosofi; II. Den religiøse
  Oplevelse; e-book)` and a running paragraph number. Do not cite these
  numbers in scholarly work — they are ours, not the book's. Go to the
  original for a page reference.
- **`--year-from` / `--year-to` exclude the e-books entirely.** Their only
  date is the reissue year (2020–23), which would sort *Psykologi* under the
  2020s; recording it was worse than recording nothing. Year filtering means
  date of composition everywhere else in this index, and it keeps meaning that.

The slug carries an `(epub)` tag for the same reason a translation's carries
`(en)`: `texts/hoeffding/psykologi/` holds both a transcription and an epub,
and `read hoeffding/psykologi:400` has to mean one of them.

## Four layers, kept apart

A search hits one or more of these, and it matters which:

| Layer | Contents | Reached by |
|---|---|---|
| `text` | the reading text — lemma, expanded abbreviations, his own footnotes | default |
| `marginalia` | the marginal column: his later additions beside an entry | default |
| `apparatus` | deletions, rival readings, abbreviations as actually written | `--apparatus` |
| `commentary` | kom.xml — Cappelørn, Garff et al. **Not Kierkegaard** | `--commentary` |

The default is `text` + `marginalia`: Kierkegaard's words and nothing else.
This distinction is the main reason not to grep the XML directly — a naive
grep conflates all four, and the editors mention Pascal far more often than he
does.

## Queries

```sh
./sks_search.py search Pascal -c journals
./sks_search.py search 'NEAR(Pascal* Jesuit*, 20)' -c journals
./sks_search.py search '"den Enkelte"' --year-from 1848 --year-to 1851
./sks_search.py search Fortvivlelse -c danish-texts
./sks_search.py search Pascal --commentary          # what the editors say
./sks_search.py search Χstd --apparatus             # his own shorthand
./sks_search.py person Pascal                       # by tagged persName key
```

Bare words are matched as **prefixes** — `Pascal` finds `Pascals`, `Pascalsk`.
Danish inflection makes this the right default; it is the difference between 20
entries and 27. `--exact` turns it off. Quotes, `AND`/`OR`/`NOT` and
`NEAR(a b, n)` are SQLite FTS5 syntax and pass through untouched.

`search` and `person` answer different questions. `search` finds the string.
`person` uses the TEI's normalised `@key`, so it finds entries where the
editors identified Pascal even where the text says only "P." — and it separates
Blaise from Jacqueline. On Pascal the two disagree by one entry, BB:2. Run both
when the question is about a person.

## Reading

```sh
./sks_search.py read NB22:21              # one entry, paragraphs intact
./sks_search.py read NB22:21 --around 3   # with three entries either side
./sks_search.py show NB22:21 --commentary
./sks_search.py dossier Pascal -c journals --year-from 1850 -o pascal.html
```

`read` and `dossier` re-render from the TEI rather than from the index, so they
keep what searching throws away: paragraph breaks, the marginal column in
place, SKS page marks, and Kierkegaard's underlining.

`dossier` writes one self-contained HTML file with every matching entry in
full — the way to turn a search into something you can sit and read.

## In Emacs

`M-x sks-search`, or `C-u M-x sks-search` to pick a corpus. Then in the results:

| Key | Does |
|---|---|
| `RET` | open that entry and read it |
| `n` / `p` | next / previous hit |
| `g` | run the search again |
| `c` | same query, different corpus |

And in an entry:

| Key | Does |
|---|---|
| `n` / `p` | the next / previous entry **of that journal** — reading around a hit |
| `M-n` / `M-p` | the next / previous **search hit** |
| `c` | show or hide the editors' commentary for these pages |
| `a` | the apparatus: deletions, variants, abbreviations |
| `y` | copy the citation (`sks-citation-format` shapes it) |
| `w` | copy the entry, or the region, as a LaTeX `quote` with its citation |
| `l` | back to the results |

`n` is the one that matters. A hit is a coordinate; `n` and `p` are how you read
the neighbourhood, which is usually where the argument actually is.

## Things worth knowing before you trust a result

- **Entries without their own page break inherit the previous entry's page.**
  Most short entries carry no `<pb>`, so the page shown is the page the entry
  begins on, carried forward. Right for citation, but check the printed edition
  before quoting a page for something at an entry's end.
- **The commentary is not Kierkegaard.** It is modern scholarship, and it is
  where most proper names actually occur. `--commentary` is opt-in for that
  reason.
- **The reading text drops deletions.** What he crossed out is in `apparatus`,
  not `text`. If the question is about revision, search there.
- **Our LaTeX is converted by a pragmatic detex**, not a TeX engine. It keeps
  words, footnotes and emphasis; it drops typesetting. Page numbers come from
  `\opage{N}` or a `% ---- printed p.N` comment, and only about a fifth of the
  books mark pages at all.
- **The published works and letters are indexed per paragraph**, each
  tagged with the SKS page(s) it falls on (a paragraph spanning a page turn
  carries a page number too, via the same carry-forward rule journal entries
  use for pages with no `<pb>` of their own). A hit in *Enten–Eller* now
  cites the actual page, e.g. `EE1:35` (SKS 2, 35) — not just the book.
  `ref` for these units is `<SIGLUM>:<page>` (a numeric suffix like `.2`
  disambiguates a second paragraph landing on the same page), so `read`,
  `show`, dossier and `n`/`p` in Emacs jump to the right paragraph, the same
  as for a journal entry's `<SIGLUM>:<entry-n>`.

## Rebuilding and extending

Re-run `python3 sks_search.py index` (from `~/sks-search`, with `$SKS_TEXTS`
set as above) after transcribing new pages — it reindexes everything from
scratch in about forty seconds. Re-run it too after `git pull` in
`~/bibliotek/Kierkegaard, Søren/SKS_tei`.

To add a corpus, write a function that yields `(meta, text, marginalia,
apparatus, person_keys)` per unit, in the shape `parse_tex` uses, and call it
from `build()`. To add an interface, drive `search --json` and `entry REF`;
those two commands are the whole contract `sks.el` relies on, and they are
documented by example at the top of `sks_search.py`.

## Provenance

The Kierkegaard text is the TEI edition of *Søren Kierkegaards Skrifter*
published by Det Kgl. Bibliotek at <https://github.com/kb-dk/SKS_tei> under
CC0, cloned into `~/bibliotek/Kierkegaard, Søren/SKS_tei` (~520 MB, its own
git, outside this repository). `sks_search.py` looks there by default; set
`$SKS_TEI` to the `data/v1.9` directory to point it elsewhere. The
file headers retain a legacy "restricted/copyright" note from the Søren
Kierkegaard Forskningscenter which the repository's CC0 licence supersedes;
worth remembering before republishing the commentary, which is recent
scholarship.

`sks_search.py` and `sks.el` themselves are a separate project,
`~/sks-search`, with its own README, its own `.gitignore`, and its own git
history — see that repository for how it's licensed and how the `$SKS_TEI` /
`$SKS_DB` / `$SKS_TEXTS` environment variables fit together.
