# Revision brief — Høffding, *Søren Kierkegaard som Filosof*: English made to follow the 1892 first edition

## The situation

- `/home/claude/skf/transcription.tex` is the established Danish text of the
  **1892 first edition** (diplomatic, checked against the scan three ways).
  It is now the source of truth. Printed page N begins at `% --- p. N ---` /
  `\opage{N}`.
- `/home/claude/skf/tr/old-translation-1919.tex` is an existing English
  translation made from a 2020 e-book of the **revised 1919 edition**. Its
  English is good and its terminology is settled; keep it wherever it already
  renders the 1892 Danish. But it follows the 1919 text, has no page markers,
  lacks Høffding's inline references, and carries 1919 notes.
- `/home/claude/skf/tr/CHANGES-1892-vs-ebook.txt` lists, page by 1892 page,
  every substantive difference a script found between the 1892 Danish and the
  e-book (spelling modernisation already filtered out). Use it as a map of
  where the old English must change — but it is a guide, not a guarantee:
  **read every 1892 sentence against the English**.

Your job: produce the English for your range that renders **the 1892 Danish,
sentence for sentence**, reusing the old English wherever it is already right.

## What to change

1. **Page markers**: put `% --- p. N ---` on its own line and `\opage{N}`
   before the first English word of each printed page, at the point that
   corresponds to the Danish page turn (a word divided over the turn stays
   whole in English, after the marker; a sentence divided over the turn is
   divided at the corresponding place).
2. **1919 additions out**: text in the old English with no counterpart in
   the 1892 Danish (see `[ins]` / `[rep]` lines) is removed. Where 1919 rewrote
   a passage, translate the 1892 Danish afresh in the old translation's
   register and terminology.
3. **1892 text in**: every 1892 sentence, clause and word must be rendered —
   including the **inline references** the e-book dropped (e.g. „(Efterladte
   Papirer. 1833–43. p. 335.)“ → `(Efterladte Papirer. 1833--43.
   p.~335.)`; „Uvidensk. Efterskr. p. 83“ → `Uvidensk. Efterskr. p.~83`).
   Keep Danish titles of works in references exactly as printed — in ROMAN
   type, as the 1892 print sets them (the audit counts italics: add none
   the Danish does not have) — with Høffding's own abbreviations and „p.“;
   do not translate or expand them. Titles named in running prose may be translated as the
   old English does.
4. **Footnotes**: exactly the 1892 footnotes (`*)` in the Danish), at the
   same anchors, translated. Remove the old translation's notes that are not
   in the 1892 edition (1919 endnotes such as references to *Danske
   Filosoffer*, 1909); a note in the old English whose content IS an 1892
   inline reference becomes that inline reference.
5. **Structure as in the Danish**: the same paragraphs; chapter and section
   heads as centred blocks mirroring the Danish (e.g.
   `\begin{center}I.\\[4pt] THE ROMANTIC-SPECULATIVE\\ PHILOSOPHY OF RELIGION.\\[2pt]\rule{1.5cm}{0.4pt}\end{center}`
   — follow the Danish block's form, rules and line division, in English
   capitals); inline paragraph numbers („2.“) kept; the same rules
   (single/double) and verse blocks; italics where the Danish has `\textit`
   (over the English words that render them); small-caps names as
   `\textsc{}`. Drop the old file's `\chapter*`/`\section*` commands.
6. Printer's errors logged in the Danish: render the evident sense, with a
   `% TR:` comment at the site.
7. Record each substantive change from the old English in a short `% REV:`
   comment on its own line at the site (e.g. `% REV: 1919 addition on the
   father's curse removed; 1892 text translated`). Not for every small
   rewording — for additions removed, passages retranslated, references and
   notes restored or removed.

## Conventions (unchanged from the old translation)

Scholarly, moderately literal, readable English; **American spelling**;
quotation marks „…“ and »…« → ``…''; German, Latin, French and Greek
quotations kept as printed; Kierkegaard's pseudonymous works by their
standard English titles in running prose (as the old translation does), but
the Danish short titles inside Høffding's references as printed.

## Output

ONE file, `/home/claude/skf/tr/ppFIRST-LAST.tex`: the English body for your
range only (no preamble), beginning with `% --- p. FIRST ---` (batch 1: the
front matter comes first — see below), ending where the Danish range ends.

## Check before you return

1. `cd /home/claude/skf && python3 tr_audit.py --frag tr/ppFIRST-LAST.tex`
   compares per printed page the `\opage` joints, italics, footnotes, centre
   blocks, paragraph breaks and the English/Danish word ratio (0.95–1.60)
   with the Danish. Fix every flag or explain it.
2. Walk through `CHANGES-1892-vs-ebook.txt` for your pages and confirm each
   entry is now handled (most `del` entries are inline references to
   restore; most one-word entries are e-book slips needing no change in
   English — check them anyway).
3. Re-read your English against the 1892 Danish sentence by sentence.

## Return (≤150 words)

Pages done; how many % REV: sites (with the 3 most important); references
restored; notes removed/kept; audit result; anything in the Danish you
found hard.

Use no web tools and no other edition. Edit nothing but your output file.
Do not run git. Text only — you do not need the page images.

## Findings from the pilot (front matter, pp. 1–27)

- Reference titles stay roman (see 3). Italic only where the Danish has it.
- 1919 notes to remove are typically references to Høffding's later books
  (Danske Filosoffer 1909, Mindre Arbejder); the 1892 reference in the text
  (often to Tilskueren 1885 or a Papirer page) is what replaces them.
- Look out for passages where 1919 updated a time reference ("nu 1890
  igen" vs 1892 „i det sidste Aars Tid“) and for small word changes the
  old English followed („Forudsætninger“ vs „overleveringer“).
