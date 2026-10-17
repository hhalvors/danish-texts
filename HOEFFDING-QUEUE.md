# Høffding queue — the remaining Harald Høffding works, one per session

Drafted 2026-10-14 from `catalog.yaml` (every Høffding work still `to-do`), `hoeffding-epub-inventory.md`, the scans in
`~/bibliotek/Høffding, Harald/`, and searches of the Internet Archive (advancedsearch API), Nasjonalbiblioteket
(api.nb.no: `EVERYWHERE` = page images open to all; an NB record without images is listed as "NB record only") and
Project Runeberg.  When Hans says **"do the next one from HOEFFDING-QUEUE.md"**, a session follows the procedure below
for the first entry whose status is `next` (or, if none, the first `queued`).

## Procedure for the session

As in NIELSEN-QUEUE.md (steps 1–9), with these models:
- **Scan with a Google/IA text layer** (Internet Archive `…hfgoog`, `…hffd`): `ebook-method/tydskland-efter-hegel/`
  (two copies of one edition = two layers) or `ebook-method/humane-ethik/`; TRANSLATION-PLAYBOOK.md §6k.
- **NB scan, no text layer**: `ebook-method/for-idee-1870-73/` (`nbfetch.py` for the page images, `nbalto.py` for NB's own
  OCR as the draft, tesseract as the witness); TRANSCRIPTION-PLAYBOOK.md §6 "For Idee og Virkelighed 1870–73".
- **An e-book exists** (SAGA epub, bought DRM-free from Saxo — `hoeffding-epub-inventory.md`): the epub is a second
  witness for the collation (`ebook-method/erindringer/`, `ebook-method/etik/`), which saves most of the blind reading.
- **Terms:** the GLOSSARY.md files of the earlier Høffding translations (`ls ebook-method/*/GLOSSARY.md`); put any key
  term they do not settle to Hans as a multiple-choice question.
- Budget: the Nielsen sessions ran at roughly 12–15k agent tokens per printed page, transcription and translation
  together, with no second witness.  Estimate and report before any agent; pilot one, then batches of at most 5.

## The queue

Status: `next` | `queued` | `in progress (date)` | `done (date)` | `blocked (reason)` | `ask Hans`.

**Next: none** — every remaining entry (#12-#17) is blocked for want of a scan.  Done: #19 rydberg-anmeldelse-1882 (2026-10-17), #10 kort-oversigt (2026-10-17), #9 religioese-tanketyper (2026-10-17), #18 filosofien-i-sverig-1879 translation (2026-10-17), #6 etiske-undersoegelser (2026-10-16), #11 mindre-arbejder-2 with #5 analogi-1905 (2026-10-16), #4 filosofien-i-sverig-1879, om-pessimismen-1879, boehme-anmeldelse-1882 (2026-10-15; Filosofien i Sverig's translation queued as #18), #3 spencer-1875, wilkens-anmeldelse-1875, montaigne-1876, spinoza-1876 (2026-10-15), #2 religionsfrihed-1886 + nietzsche-debat-hoeffding (2026-10-15), #1 engelske-philosophi (2026-10-15), #0 oplevelse-og-tydning (2026-10-14), #8 moderne-filosoffer (2026-10-14).

### A. In the catalog (`to-do`), scan available

| # | Slug (catalog id) | Work | Scan | Status |
|---|---|---|---|---|
| 0 | oplevelse-og-tydning | *Oplevelse og Tydning. Religionsfilosofiske Studier* (1918), ~240 pp. | NB 363c131e7e2e2c6e3b0602f49dae5268 (EVERYWHERE, 247 images); epub 9788726363029 (OWNED: ~/bibliotek/Høffding, Harald/oplevelse.epub) | done (2026-10-14): transcription (three-witness collation, page check 0/2948) and translation made; year 1918 settled, no second copy found |
| 1 | engelske-philosophi | *Den engelske Philosophi i vor Tid* (1874), ~200 pp. | Internet Archive denengelskephilo00hffd (210 images) and denengelskephil00hfgoog (Google): two copies, two layers | done (2026-10-15): [IV] + 190 pp. transcribed (three-witness: Toronto ABBYY, tesseract, Oxford copy read twice; page check 0 word errors in 2434) and translated by eight agents; 71 faults found after collation by the translators' odd spots |
| 2 | religionsfrihed-1886, nietzsche-debat-hoeffding (3 parts) | *Om Religionsfrihed* (Tilskueren 1886, pp. 448–459); the Nietzsche debate with Brandes: *Demokratisk Radikalisme* (Nov.–Dec. 1889), *Gensvar* (1890, pp. 125–153), *Epilog* (1890, pp. 343–353) | Internet Archive tilskuerenmaaned1886nngoog, …1889nngoog, …1890nngoog (Google); Runeberg (tilskueren/1889, /1890); e-texts at henrikpontoppidan.dk as a finding aid.  **Transcription only for the three Nietzsche-debate pieces: do NOT translate them** (Hans, 2026-10-15): William Banks has translated them in *The Great Debate* (University of Wisconsin Press, 2024; catalog note).  Om Religionsfrihed is transcribed and translated as usual | done (2026-10-15): four transcriptions (ebook-method/tilskueren-1886-90/: ABBYY draft, tesseract, Runeberg OCR as guarded voter; 303 blind crops, notes and structure read, letterspacing measured; page check 0 word errors in 2202 after mending) and Om Religionsfrihed translated (2 translators); the Nietzsche pieces transcription only |
| 3 | spencer-1875, wilkens-anmeldelse-1875, montaigne-1876, spinoza-1876 | four pieces from the 1870s: *Herbert Spencers Filosofi* (Det nittende Aarhundrede, May 1875, pp. 106–130); the review of Wilkens (1875–76); *Montaignes Betydning i Ethikens Historie* (June 1876, pp. 210–230); *Benedikt Spinoza* (Nær og Fjern, 17 Dec. 1876) | Internet Archive detnittendeaarhu1875unse, detnittendeaarh1875unse_0, detnittendeaarh1876unse_0, naer-og-fjern-1876-77 | done (2026-10-15): four transcriptions (ebook-method/hoeffding-1875-76/: our tesseract as draft, the Archive's OCR as witness, the Harvard copy's ABBYY as voter; 210 blind crops, notes and structure read, Nær og Fjern's Fraktur columns proofread whole; page check 7 errors in 1143 words, mended, then a speck sweep) and four translations (5 translators); Wilkens pp. 81-85 |
| 4 | filosofien-i-sverig-1879, om-pessimismen-1879, boehme-anmeldelse-1882 | three short pieces: *Filosofien i Sverig* (Nordisk tidskrift 1879, pp. 30–73); *Om Pessimismen* (Vor Ungdom 1879); the review of Martensen's *Jacob Böhme* (Ude og Hjemme 1882) | Runeberg nordtidskr/1879 (images + OCR); NB 5913f0beb5001cb09055a914b1780933 (Vor Ungdom 1879, EVERYWHERE); Internet Archive ude-og-hjemme-aarg-5 / -aarg-6 (find the number first) | done (2026-10-15): three transcriptions (ebook-method/hoeffding-1879-82/: our tesseract as draft, NB ALTO / Archive OCR as witness; 746 blind crops, Runeberg votes withdrawn after audit; notes and structure read; Ude og Hjemme proofread whole; page check 1 word error in 1595, mended); Om Pessimismen and the review translated; **Filosofien i Sverig NOT yet translated** (moved to the end of the queue: #18). Found: a second Høffding review in Ude og Hjemme 5, p. 196 (Viktor Rydberg), not in the catalog (queued as #19) |
| 5 | analogi-1905 | *Om Begrebet Analogi og dets filosofiske Betydning* (Mindre Arbejder II, 1905) | Internet Archive mindrearbejder01hfgoog (Mindre Arbejder II, 261 images); Høffding's own English in *Mind* 1905 (archive.org sim_mind_1905-04_14_54) — the English is his, so a terminology anchor or the translation itself (ask Hans) | done (2026-10-16): transcribed and translated inside #11 (pp. 33-46 of texts/hoeffding/mindre-arbejder-2/; the catalog entry links there); Mind 1905 used as the terminology anchor |

### B. Added to the catalog 2026-10-14 (Hans), scan available

| # | Slug (catalog id) | Work | Scan | Status |
|---|---|---|---|---|
| 6 | etiske-undersoegelser | *Etiske Undersøgelser* (1891), ~95 pp. | Internet Archive etiskeundersgel00hfgoog (98 images, Wisconsin) and NB 8df6665866cef49a09cc7815de97c99b (EVERYWHERE, 99 images): two scans | done (2026-10-16): [VI] + 83 pp. transcribed (one copy, two readings: our tesseract + ABBYY; NB copy unreachable that day; blind crops 28/28 controls; notes read whole; stratified page check 0 collation errors in 1686 words) and translated (4 parts, anchored on IJE 1890 / Monist 1891); 52 odd spots settled at 600 ppi |
| 8 | moderne-filosoffer | *Moderne Filosofer* (1904; the print spells it so), ~200 pp. (incl. »Filosoferende Naturforskere«: Maxwell and others) | Internet Archive modern-filosofer (Google scan + OCR); epub 9788726363005 (OWNED: ~/bibliotek/Høffding, Harald/moderne-filosoffer.epub) | done (2026-10-14): X + 157 pp. transcribed (three-witness: Google layer, tesseract, e-book vote; ~1 error/1000 words in the page check, then mended) and translated by six agents; transcription.tex + translation.tex |
| 9 | religioese-tanketyper | *Religiøse Tanketyper* (1927), ~175 pp. | NB 7cfe6d92ba67c5ca2c2e33faa1f19da7 (EVERYWHERE, 177 images); epub 9788726363050 (OWNED: ~/bibliotek/Høffding, Harald/religioese-tanketyper.epub, bought 2026-10-17) | done (2026-10-17): 165 pp. transcribed (three-witness: NB ALTO, tesseract, e-book vote; blind crops 14/14 controls, audit 40/40; structure and notes read whole; page check 0 word errors in 2924) and translated by seven agents (*Types of Religious Thought*); **pp. 27-28 missing from the NB copy**, set from the e-book, flagged (KB-VISIT-TODO §11); ~1.4M agent tokens |
| 10 | kort-oversigt | *Kort Oversigt over den nyere Filosofis Historie* (1898; later editions), ~110 pp. | NB 17246e2b574fbd978af6a80c866e4e4b (1910 ed., EVERYWHERE, 109 images); Runeberg (scan + OCR, edition to check); epub OWNED (texts/hoeffding/kort-oversigt/) — choose the edition with Hans | done (2026-10-17): the 1910 fourth edition (Hans), 95 pp. transcribed (three-witness collation; the SAGA e-book, though „Copyright 1898“, is a LATER edition, ≥1920, voting only where it agrees) and translated (6 parts, *A Short Survey of the History of Modern Philosophy*); ~1.3M agent tokens |
| 11 | mindre-arbejder-2 | *Mindre Arbejder. Anden Række* (1905), ~230 pp., 17 pieces 1891–1905, incl. *Søren Kierkegaard. En Karakteristik* (1903) and the Analogi essay (#5: done in the same session) | Internet Archive mindrearbejder01hfgoog (as #5) | done (2026-10-16): 237 pp. transcribed (two-witness collation + damaged pages read whole + the translators' odd spots at the image; gutter-cut letters supplied by sense) and translated (13 parts, ~85k words) |
| 18 | filosofien-i-sverig-1879 (translation only) | Translation of *Filosofien i Sverig* (Nordisk tidskrift 1879, pp. 30–73), ~20,200 words; the transcription is done (#4) | none needed: build from texts/hoeffding/filosofien-i-sverig-1879/transcription.tex with ebook-method/hoeffding-1879-82/tr_parts.py (add parts by section I./II. and pages; extend GLOSSARY.md: Swedish names, titles, quotations); see texts/hoeffding/hoeffding-1879-82/RESUME-NOTES.md | done (2026-10-17): 4 Sonnet translators (~0.5M tokens); 27 odd spots read at zooms (6 transcription faults mended, 3 misprints marked); GLOSSARY.md S1-S8 ◆ for Hans |
| 19 | rydberg-anmeldelse-1882 | Høffding's review of Viktor Rydberg, »Ny Testamentes Lærdomme« (the issue's Indhold: „Viktor Rydberg: Forudtilværelsen og de sidste Ting“), *Ude og Hjemme* 5 (1881–82), pp. 196–197; found during #4 | Internet Archive ude-og-hjemme-aarg-5 (leaf 211; two columns, as the Böhme review): reuse ebook-method/hoeffding-1879-82/ (new virtual pages in B3) | done (2026-10-17): added to the catalog as rydberg-anmeldelse-1882 (Nr. 224, 15 January 1882, pp. 196-197: IA leaves 207-208, not 211); transcribed (two tesseract readings, every line read at the image) and translated, in the main session without agents |
| 7 | rousseau-filosofi | *Jean Jacques Rousseau og hans Filosofi* (1896), ~150 pp. | NB 911156308e618b811c1b8f30776c9400 (EVERYWHERE, 155 images); epub 9788726363036 (~68 kr, not owned) | queued (moved to the end, Hans 2026-10-16: less important) |

### C. No scan found yet — search KB (kb.dk/e-mat), Google Books, HathiTrust; then move the entry up

| # | Slug | Work | Status |
|---|---|---|---|
| 12 | antik-villie | *Den antike Opfattelse af Menneskets Villie* (dissertation, 1870) | blocked (scan) |
| 13 | om-erindring-1878, martensen-etik-kritik-1878, heegaard-intolerance-1878, sibbern-moralphilosophi-1878 | four pieces in *Nær og Fjern* vol. 7 (Nr. 275–326, Oct. 1877–Sept. 1878): the Internet Archive has vols. 6 and 8, not 7 | blocked (scan) |
| 14 | formel-logik | *Formel Logik* (1884; 6th ed. 1913) | blocked (scan) |
| 15 | charles-darwin-1889 | *Charles Darwin* (Studentersamfundets Smaaskrifter 91–92, 1889) | blocked (scan) |
| 16 | (not in catalog) | *Henri Bergsons Filosofi* (1914): epub OWNED (texts/hoeffding/bergsons-filosofi/), NB record only, no scan | blocked (scan) |
| 17 | (not in catalog) | *Mindre Arbejder. Tredie Række* (1913); *Ledende Tanker i det nittende Aarhundrede* (NB has 1920): NB records only | blocked (scan) |

### D. Not for this queue (Hans to decide)

- personlighedsprincippet, "Editorial apparatus" (Blegvad's introduction, Koch's commentary, 2013): modern scholarship,
  in copyright.
- meyerson-brevveksling (1939, French): Internet Archive copy is lending-only; NB record only.
- Manuscripts (nielsen-kursus-notes, relation-marginalia, bohr-brevveksling): a manuscript workflow, not this pipeline.
