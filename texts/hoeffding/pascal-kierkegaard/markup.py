#!/usr/bin/env python3
"""
markup.py <fragment.texfrag>   ->  rewrites it in place

Third and last mechanical pass. build_frag.py got the words and the
paragraphing; polish.py fixed the systematic OCR failures; markup.py adds the
things OCR is *constitutionally* unable to see, because they are carried by
the typeface rather than the letterforms:

  - ITALICS. tesseract reports no font information at all, so every one of
    these was read off the 300 dpi page image by eye. Titles of works, and the
    one Latin tag (carpe diem), are italic in this journal.
  - SECTION HEADS, set as caps + small caps, matching the style established for
    section I on p. 225 and section IV on p. 242 by the other two batches.
  - THE FOOTNOTE on p. 232, which the journal sets at the page foot and which
    has to be re-attached to its reference mark in the running text.
  - PRINTER'S DEFECTS, logged in a % comment at the site and left in the text
    exactly as printed. See CLAUDE.md, "Editorial stance": the compositor is
    never silently corrected.

Everything here is a literal find/replace, so the diff is the whole argument
for its correctness.
"""
import sys
from pathlib import Path

# A few word-level OCR fixes found while doing the italics pass, same status as
# the polish.py table: checked against the image, all genuine OCR failures.
LATE_OCR = [
    ("son maitre, le professeur", "son maître, le professeur"),
    ("tout en És'assimilant", "tout en s'assimilant"),
    ("Pascal à consacré un mémoire", "Pascal a consacré un mémoire"),
    ("les Lettres à un pro- ,\nvincial", "les Lettres à un pro-\nvincial"),
    ("une réalisation ;", "une réalisation"),
    ("criminel de la vie ;", "criminel de la vie"),
]

ITALICS = [
    # p. 231
    ("ils pratiquent le carpe diem", r"ils pratiquent le \emph{carpe diem}"),
    ("dans ses Pensées,", r"dans ses \emph{Pensées},"),
    # p. 232 — Kierkegaard's title, given in French translation in the text
    ("(Postscriptum définitif non scientifique, 1846)",
     r"(\emph{Postscriptum définitif non scientifique}, 1846)"),
    # p. 233 — Either/Or and Stages on Life's Way, in Høffding's French titles
    ("plus populaires (Ou l'un ou l'autre et Étapes de la route humaine).",
     r"plus populaires (\emph{Ou l'un ou l'autre} et "
     r"\emph{Étapes de la route humaine})."),
    # p. 237
    ("Saint Augustin (De civitate\nDei, XX, 9)",
     "Saint Augustin (\\emph{De civitate\nDei}, XX, 9)"),
    ("dans les Lettres à un pro-\nvincial, il a élevé",
     "dans les \\emph{Lettres à un pro-\nvincial}, il a élevé"),
    ("à la Comparaison des chrétiens des\npremiers temps avec ceux d'aujourd'hui.",
     "à la \\emph{Comparaison des chrétiens des\npremiers temps avec ceux "
     "d'aujourd'hui}."),
    # p. 238
    ("intitulé Augustinus,", r"intitulé \emph{Augustinus},"),
    ("dans son Mémoire sur\nle Vide, repoussé",
     "dans son \\emph{Mémoire sur\nle Vide}, repoussé"),
    (r"dans sa 18\textsuperscript{e} Provinciale il expose",
     r"dans sa \emph{18\textsuperscript{e} Provinciale} il expose"),
    ("le Pascal des Pensées.", r"le Pascal des \emph{Pensées}."),
]

HEADS = [
    ("II. — PRÉDISPOSITIONS INTELLECTUELLES.",
     "% Section II opens here, set exactly as section I on p. 225:\n"
     "% the numeral and dash in full capitals, then caps + small caps.\n"
     r"\section*{II. --- \textsc{Prédispositions intellectuelles.}}"),
    ("III. — LE PROBLÈME CHRÉTIEN.",
     "% Section III opens here.\n"
     r"\section*{III. --- \textsc{Le problème chrétien.}}"),
]

# The single footnote in this batch. Printed mark: a superscript arabic numeral
# followed by a baseline closing parenthesis; at the foot, "1." in small type.
FOOTNOTE = (
    "(\\emph{Postscriptum définitif non scientifique}, 1846)*,",
    "(\\emph{Postscriptum définitif non scientifique}, 1846)%\n"
    "% printed mark: superscript 1 followed by a baseline ')'\n"
    "\\footnote{\\dk{\\emph{Alsluttende uvidenskabelig Efterskrift.}} "
    "Copenhague, 1846.}%\n"
    "% PRINTER'S ERROR, transcribed as printed: the journal sets\n"
    "%   \"Alsluttende\" for Kierkegaard's \"Afsluttende\". Verified at 600 dpi.\n"
    ",",
)
FOOTNOTE_FOOT = "\n1, Alsluttende uvidenskabelig Efterskrift. Copenhague, 1846.\n"

DEFECT_COMMENTS = [
    ("le professeur Paul Moller,",
     "le professeur Paul Moller,%\n"
     "% As printed: \"Paul Moller\", for Poul Møller. Høffding's own French\n"
     "% form of his teacher's name, without the ø. Not corrected.\n"),
    ("tout en s'assimilant",
     "% A single damaged/over-inked sort stands immediately before\n"
     "% \"s'assimilant\" here; it is not legible as any letter at 600 dpi.\n"
     "% Sense wants \"tout en se l'assimilant\". Left as the visible text.\n"
     "tout en s'assimilant"),
    ("de Montaigne et d'Epictète,",
     "de Montaigne et d'Epictète,%\n"
     "% As printed: \"Epictète\" without the acute here, though the same name\n"
     "% is set \"Épictète\" on p. 231. Both readings recorded, not normalised.\n"),
]


def apply(text, pairs, label):
    hit = 0
    missing = []
    for old, new in pairs:
        if old in text:
            text = text.replace(old, new, 1)
            hit += 1
        else:
            missing.append(old[:50])
    print(f"{label}: {hit}/{len(pairs)}")
    for m in missing:
        print(f"   NOT FOUND: {m!r}")
    return text


def main():
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")

    text = apply(text, LATE_OCR, "late OCR fixes")
    text = apply(text, ITALICS, "italics")
    text = apply(text, HEADS, "section heads")

    # footnote: attach at the reference, remove the foot-of-page line
    text = apply(text, [FOOTNOTE], "footnote attached")
    if FOOTNOTE_FOOT in text:
        text = text.replace(FOOTNOTE_FOOT, "\n")
        print("footnote foot-line removed: 1/1")
    else:
        print("   NOT FOUND: footnote foot-of-page line")

    text = apply(text, DEFECT_COMMENTS, "printer's defects logged")

    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
