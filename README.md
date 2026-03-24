# Danish Philosophical Texts

Transcriptions and English translations of Danish philosophical works,
primarily from the nineteenth century. All source texts are in the
public domain; scans are drawn from the Royal Danish Library (Det
Kongelige Bibliotek).

## Structure

```
texts/
  <author-surname>/
    <work-slug>/
      <section-slug>/
        transcription.tex   — Danish transcription
        translation.tex     — English translation
        transcription.pdf   — compiled PDF (committed)
        translation.pdf     — compiled PDF (committed)
```

## Compiling

Each `.tex` file is self-contained and compiles with `pdflatex`:

```bash
cd texts/nielsen/religionsphilosophie/indledning
pdflatex transcription.tex && pdflatex translation.tex
```

## Texts included

### Rasmus Nielsen (1809–1884)

- **Religionsphilosophie** (Copenhagen: Gyldendal, 1869)
  - Indledning (Introduction), §§ 1–3, pp. 1–30 — *in progress*

### Harald Høffding (1843–1931)

*(placeholder — texts forthcoming)*

## Web front page

The `index.html` at the root of this repository is served via GitHub
Pages at <https://hhalvors.github.io/danish-texts/> and linked from
<https://hanshalvorson.com>.

## License

Translations © Hans Halvorson. All transcriptions are reproductions of
public-domain texts. Feel free to use translations with attribution.
