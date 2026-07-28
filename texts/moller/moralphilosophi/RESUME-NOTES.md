# Poul Martin Møller — "Forelæsnings-Paragrapher over Moralphilosophien": resume notes

Source of truth: `transcription.tex` (Danish), **COMPLETE** (printed pp. 141–162).
Translation: `translation.tex` (English), **COMPLETE** (mirrors transcription 1:1).
Scan: ~/bibliotek/Møller, Poul Martin/efterladte-skrifter5.pdf
Page-offset: **PDF = printed + 11** (printed 141 = PDF p.152; piece runs PDF pp. 152–173).

## STATUS
Both files transcribed/translated in full and compile clean in the sandbox
(0 errors, 0 char-warnings, 20 pp. each). Marked `in-progress` in `catalog.yaml`
pending your local compile with the real fonts (libertinus + textalpha) and a
commit/push so the GitHub Pages links resolve. Flip the section `status:` to
`complete` once both PDFs build and the links work.

## What this piece is
Møller's **ethics** in 47 numbered lecture-paragraphs, reconstructed by the
editor "Efter Collegier fra 1837, sammenlignede med Forfatterens Manuscript.
F. C. O." (F.C. Olsen). The practical-philosophy counterpart to the *Ontologien*.
NOTE: PHILOSOPHY-PRIORITIES.md gave the range as pp. 141–164; the piece in fact
**ends on p. 162** (§ 47, followed by a rule). Printed p. 163 begins the next
section, "Recensioner af philosophisk Indhold."

## Structure (§§ 1–47)
- **§§ 1–5** — Introduction: method (dogmatic vs. philosophical); freedom vs.
  indifferentism (§2) and determinism/fatalism (§3); the empirical character
  (§4); the three main parts announced (§5).
- **First Chapter — On Imputation (Tilregnelse), §§ 6–12.** Voluntary /
  intentional / deliberate action; chance (§8), negligence (§9); action in the
  widest sense (§11); every action aims at a purpose (§12).
- **Second Chapter — On Happiness (Lyksalighed), §§ 13–22.** Interest (§13),
  feeling (§14); Cyrenaic/Cynic/Epicurean sequence and the eudaimonistic
  principle (§15); moral feeling (§16); self-preservation (§17), benevolence
  (§18), right (§19), the contemplative life and action-according-to-cognition
  (§20), striving after harmony (§21), the perfect existence / perfection (§22).
- **Third Chapter — On the Good (det Gode), §§ 23–47.**
  - **A. On Virtue, §§ 23–39.** Virtue as second nature (§24), as active force
    (§26), as the mean between two extremes (§27); individuality (§28);
    **affectation** (§29); "Virtue in its outward appearance" (§31) — a run of
    concrete virtues each set as a mean (courage/temperance, perseverance/
    energy/industriousness, good husbandry, love of honour, love of freedom,
    the sympathetic mind, manliness/compliance, equity of mind, love of art
    and science).
  - **B. On Duty, §§ 40–43.** The categorical imperative (§41); collision of
    duties and the impossibility of a universal ranking (§42); ascetic exercises
    (§43).
  - **C. On Conscience, §§ 44–47.** Conscience, erring conscience (§44); evil
    conscience, hypocrisy, probabilism (§45); the good-intention-sanctifies-the-
    means slide into **moral irony** (§46 — links to the *Ironie* fragment);
    and the concluding reconciliation of individual and **State** (§47).

## Conventions (book-specific)
See ../../../TRANSLATION-PLAYBOOK.md for the standing method. Follows the
**Ontologien/Ironie** conventions (Fraktur, original orthography):
- Original orthography kept (aa-spellings, capitalised nouns, "Characteer",
  "Conseqvents", the -mus endings Determinismus/Indifferentismus/Probabilismus,
  "philosophisk"). Long-s → s. "Øiemed" (aim) — Fraktur capital Ø reads D-like.
  "&c." for the old "2c." etc.-ligature (§23).
- Letterspaced emphasis in the original → `\emph{}` (the defined terms; carried
  into the translation).
- Danish quotes „…" → ``…'' (few here).
- Printed page numbers → `\opage{N}` (141–162, sequential, all present).
- Numbered §§ set with a `\slaw{N}` macro ("§ N." centered); the three editor's
  "Anm." remarks set smaller via `\anm{}`; chapter heads via `\mchap{}{}`.
- **Editorial footnotes** (all "F. C. O."): the title-note (source of the text);
  the p.147 manuscript-variant ("ved Menneskets Øiemed"); the p.150 variant
  ("Selskabelighedens"); the p.158 variant ("deels Vredagtighed og Egensind").
- Preamble note: `\ombreak` MUST be defined (it caused the one compile failure
  when first omitted). Keep it if re-generating.

## Next candidate pieces (priority list)
Per PHILOSOPHY-PRIORITIES.md: Forberedelser til en Afhandling om Affectation
(vol. 3, Brudstykke IV, pp. 163–188 — natural pairing with § 29 here); a Fraktur
transcription of the Strøtanker (vol. 3, pp. 1–147); the vol. 4 history-of-
philosophy course; the vol. 5 philosophical Recensioner.
