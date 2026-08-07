#!/usr/bin/env python3
"""
polish.py <fragment.texfrag>   ->  rewrites it in place

The second half of the mechanical pipeline. build_frag.py gets the words and
the paragraphing out of tesseract; polish.py fixes the things that are wrong in
a *systematic* way, from an explicit table, so that every change is reviewable
and none of it is a guess made in passing.

Four passes, in order:

 1. SPECK STRIPPING. The scan carries marginal dirt — a stray "{", ";", "°",
    "-" or "|" that tesseract reads as a word at the start of a line. They are
    always a single non-alphanumeric glyph followed by a space, and no line of
    this article legitimately begins that way.

 2. APOSTROPHE NORMALISATION. tesseract returns a mix of U+2019 and ASCII "'".
    Batches pp. 221--229 and pp. 239--246 are ASCII throughout (0 curly in
    either), so this fragment is normalised to match. This is a transcription
    convention, not a claim about what the journal's punch-cutter did.

 3. OCR CORRECTIONS. The table below. Every entry was checked against the page
    image at 300 dpi before being written down. These are OCR failures, NOT
    printer's errors: printer's errors are transcribed as printed and logged in
    a % comment at the site (see CLAUDE.md, "Editorial stance"). Where the two
    could be confused the comment says which it is.

 4. PARAGRAPH BREAKS the geometry missed. build_frag.py finds an indent by
    comparing left-x against the page's median; three openings sit within the
    jitter and have to be named explicitly.
"""
import re
import sys
from pathlib import Path

# --- pass 3 table: (page, wrong, right, why) -------------------------------
CORRECTIONS = [
    (230, "de'chercher", "de chercher", "OCR joined two words with an apostrophe"),
    (230, "démèêler", "démêler", "OCR doubled the circumflex/grave"),
    (230, "aplitude", "aptitude", "OCR t->l"),
    (230, 'M”° Perier', r"M\textsuperscript{me} Perier",
     "printed as a superscript 'me' abbreviation for Madame"),
    (231, "eb moyens", "et moyens", "OCR t->b"),
    (231, "opinions recues", "opinions reçues", "OCR dropped the cedilla"),
    (232, "convaineu", "convaincu", "OCR c->e, u->n"),
    # The journal misprints Kierkegaard's title: Afsluttende -> Alsluttende.
    # That is the PRINTER's error and is kept; "Alstuitende" was merely how
    # tesseract read the misprint, and that is what is corrected here.
    (232, "Alstuitende", "Alsluttende", "OCR of the printed (mis-set) form"),
    (232, "Eftershrift", "Efterskrift", "OCR k->h in the Danish"),
    (233, "il! y a", "il y a", "OCR added a spurious exclamation mark"),
    (235, "un abime", "un abîme", "OCR dropped the circumflex"),
    (235, "consa-\n eérées", "consacrées", "line-break join the dehyphenator missed"),
    (236, "itmrninente", "imminente", "OCR mangled the minims"),
    (237, "le foyaume", "le royaume", "OCR r->f"),
    (238, "ce qu'on à fait", "ce qu'on a fait", "OCR added a grave to the verb"),
    (238, "la pertedes", "la perte des", "OCR lost a word space"),
    (238, "ilavait déjà", "il avait déjà", "OCR lost a word space"),
    (238, "Mémoiresur", "Mémoire sur", "OCR lost a word space"),
    (238, "théologiescolastique\net jésuite", "théologie scolastique et jésuite",
     "OCR lost a word space across a line break"),
    (238, "18° Provinciale", r"18\textsuperscript{e} Provinciale",
     "printed as a superscript ordinal"),
]

# --- pass 4: paragraph openings the indent test missed ---------------------
PARA_OPENINGS = [
    "Pascal ramène à deux types",
    "Il reste convaincu que la grandeur",
    "S'il y a tant d'écart",
]

SPECK = re.compile(r"^\s*[^\w\s«»(\[]\s+(?=[A-ZÀÉÈÎÔÛa-zà-ÿ])")


def main():
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")

    # 1. specks
    lines = text.split("\n")
    specks = 0
    for i, line in enumerate(lines):
        if line.startswith("%"):
            continue
        new = SPECK.sub("", line)
        if new != line:
            specks += 1
            lines[i] = new
    text = "\n".join(lines)

    # 2. apostrophes
    curly = text.count("’")
    text = text.replace("’", "'")

    # 3. corrections
    applied, missing = 0, []
    for page, wrong, right, _why in CORRECTIONS:
        if wrong in text:
            text = text.replace(wrong, right)
            applied += 1
        else:
            missing.append((page, wrong))

    # 4. paragraph breaks
    lines = text.split("\n")
    added = 0
    for opening in PARA_OPENINGS:
        for i, line in enumerate(lines):
            if line.lstrip().startswith(opening[:22]):
                if i > 0 and lines[i - 1].strip() != "":
                    lines.insert(i, "")
                    added += 1
                break
    text = "\n".join(lines)

    path.write_text(text, encoding="utf-8")
    print(f"specks stripped:      {specks}")
    print(f"curly apostrophes:    {curly} -> ASCII")
    print(f"corrections applied:  {applied}/{len(CORRECTIONS)}")
    print(f"paragraph breaks added: {added}/{len(PARA_OPENINGS)}")
    if missing:
        print("NOT FOUND (check by hand — the OCR may have changed):")
        for page, wrong in missing:
            print(f"  p.{page}: {wrong!r}")


if __name__ == "__main__":
    main()
