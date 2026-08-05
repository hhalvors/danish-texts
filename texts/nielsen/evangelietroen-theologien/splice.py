#!/usr/bin/env python3
"""
splice.py [.parts/ppA-B.tex ...]   ->  replace each batch marker in transcription.tex

Written for concurrent batches. Several subagents may transcribe different page ranges
at the same time, but they must NOT each Edit transcription.tex: Edit is a
read-modify-write over the whole file, so two agents finishing at once can clobber one
another. Instead each writes .parts/pp<FIRST>-<LAST>.tex, and this script splices them
in afterwards — one process, one write, no race.

Each fragment replaces the line

    % [text to be added: pp. FIRST--LAST]

matched by the FIRST--LAST pair parsed out of the fragment's own filename, so a fragment
can never land under the wrong marker. Refuses to run if a marker is missing (already
spliced?) or a fragment is empty. With no arguments, splices every fragment in .parts/.

Fragments are named .texfrag, NOT .tex, and spliced ones are moved to .parts/spliced/.
Both matter: the repo Makefile builds every .tex it finds under texts/, and a fragment has
no preamble and no \\begin{document}, so a stray fragment named .tex breaks `make` with
"Missing \\begin{document}". Do not rename them back.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEX = HERE / "transcription.tex"
PARTS = HERE / ".parts"
DONE = PARTS / "spliced"


def marker_for(name: str) -> tuple[str, int]:
    m = re.fullmatch(r"pp(\d+)-(\d+)\.texfrag", name)
    if not m:
        raise SystemExit(
            f"fragment {name!r}: expected the name pp<FIRST>-<LAST>.texfrag "
            "(the .texfrag extension keeps the Makefile from trying to build it)")
    first, last = int(m.group(1)), int(m.group(2))
    return f"% [text to be added: pp. {first}--{last}]", first


def main(argv: list[str]) -> None:
    frags = [Path(a) for a in argv] if argv else sorted(PARTS.glob("pp*.texfrag"))
    stray = sorted(PARTS.glob("pp*.tex"))
    if stray:
        raise SystemExit(
            "found fragments named .tex: " + ", ".join(f.name for f in stray) +
            "\nRename them to .texfrag — the Makefile builds every .tex under texts/ and "
            "will fail on a fragment with 'Missing \\begin{document}'.")
    if not frags:
        raise SystemExit(f"no fragments found in {PARTS}")

    text = TEX.read_text(encoding="utf-8")
    plan = []
    for f in frags:
        marker, first = marker_for(f.name)
        body = f.read_text(encoding="utf-8").strip("\n")
        if not body.strip():
            raise SystemExit(f"{f.name} is empty — refusing to splice")
        if text.count(marker) != 1:
            raise SystemExit(
                f"{f.name}: found {text.count(marker)} copies of {marker!r} in "
                "transcription.tex (already spliced, or the marker was edited?)")
        plan.append((first, marker, body, f))

    for first, marker, body, f in sorted(plan):          # page order, for tidy diffs
        text = text.replace(marker, body)
        print(f"spliced {f.name:>20}  ({body.count(chr(10)) + 1} lines) at p. {first}")

    TEX.write_text(text, encoding="utf-8")

    # Retire spliced fragments so a later run cannot double-splice and so nothing
    # lingers in the tree that a build system might pick up.
    DONE.mkdir(exist_ok=True)
    for _, _, _, f in plan:
        f.rename(DONE / f.name)
    print(f"archived {len(plan)} fragment(s) to {DONE.relative_to(HERE)}/")
    print(f"\n{TEX.name} written. Now run:  python3 check.py")


if __name__ == "__main__":
    main(sys.argv[1:])
