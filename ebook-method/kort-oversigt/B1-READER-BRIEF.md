# B1 reader brief — Kort Oversigt over den nyere Filosofis Historie (Høffding 1910), blind crop sheets

You read crop sheets cut from a scan of a Danish book printed in 1910 (antiqua type, old orthography: aa for å,
nouns capitalised; both „…“ and «…» quotation marks occur).  Each crop is labelled `b1-NN-KK  p.N` and is one of two kinds:

- **word crop** (no tag): a word or a few words are boxed in RED.  Transcribe EXACTLY what is printed inside the red
  box: every letter, accent (é è à ö ü ä ø æ å), capital, and every mark touching the boxed words (quotation marks
  „ “ ’ ', commas, stops, parentheses, dashes —, hyphens).  Do not correct anything: if the print has a misprint, give
  the misprint.  Say "italic" in the note when the boxed words are italic.  Names are often set in SMALL CAPITALS: say "small caps" in the note.  If a mark is a faint speck or a pencil stroke (a hand-drawn slash or cross, not type), say so in the note
  and leave it out of the reading.  If the box cuts a word, give the whole word the box touches.
- **[LINE] crop**: three lines are shown; look at the MIDDLE line only.  List every word in it that is LETTERSPACED
  (s p a c e d   o u t) or set in *italic*, as `spaced: word word` / `italic: word`; or write `none`.

Some crops are controls whose reading is known; read every crop with the same care.

## Procedure (cost discipline)
1. Stage all your sheets in ONE call of mcp__remote-devices__device_stage_files (load it with ToolSearch first:
   `select:mcp__remote-devices__device_stage_files`), then Read each staged PNG.  Read each sheet once, whole.
2. If a device call fails twice, stop and return what you have.  No other tools are needed.
3. Return ONLY a TSV block, one line per crop, in sheet order:
```
id<TAB>reading<TAB>note
b1-02-01<TAB>„Substans“<TAB>
b1-02-05<TAB>spaced: er<TAB>
```
`note` is optional: "unsure", "pencil slash after the word", "italic", "letterspaced", "speck", etc.
