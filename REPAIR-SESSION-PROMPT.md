# Session-start prompt for the accuracy repair programme

Paste the block below to start any session of this programme. It is deliberately
the same every time — the state lives in `ACCURACY-LEDGER.tsv`, not in the prompt.

---

Work on the transcription-accuracy repair programme in ~/danish-texts.

Read first, in this order: CLAUDE.md, REPAIR-PLAYBOOK.md, and
ACCURACY-LEDGER.tsv. The ledger is the state of the programme — it says what
has been assessed, what it scored, and what is left. Start from it, not from
anything you infer about the repo.

THIS SESSION: assessments only. Take the next 6 books with status `unassessed`
from the ledger, published ones first (that is the ledger's order already).
Do not repair anything this session, even if a book scores badly — record the
finding and stop. A session does one kind of work; mixing assessment and repair
is how a 6-page sample turns into an unplanned collation.

For each book, follow REPAIR-PLAYBOOK.md §3 exactly:
  - `python3 scans.py path <book>` gives the verified scan (identity is the
    sha256, not the filename; SCANS.tsv also says which witness the book uses).
  - Choose the sample pages by the deterministic rule in §3 — not by eye.
    Books of 30 printed pages or fewer are read in full instead of sampled.
  - Dispatch ONE subagent per book with the brief in §3. It reads every page
    image in its own context and returns only the numbers and the errors found.
  - NEVER read a page image in this conversation. That single rule is what
    makes the programme affordable.

Then, per §4, record for each book in ACCURACY-LEDGER.tsv: pages sampled,
errors found, the implied rate, the ocrdiff precision, and the treatment the
result earns. Be honest about what a clean sample proves — 6 clean pages bound
the error rate only at ≤0.5/page, 12 at ≤0.25/page. A clean book is recorded as
"sampled clean, rate ≤X", never as "accurate". Apply any errors the sample
actually turned up, and log them in the transcription.tex header.

Constraints, all learned the hard way:
  - Do not retry the four proxies in REPAIR-PLAYBOOK.md §1. They were measured
    and they do not work. There is no free proxy for the error rate.
  - Validate any script you write against a case whose answer you already know
    BEFORE acting on its output. Three tools were trusted on first output during
    this project and all three were wrong, two of them corpus-wide.
  - When a check disagrees with the user or with a document, say so and show the
    evidence — but do not treat your own tool's failure as proof. Verify twice
    before concluding something is missing or broken.
  - DO NOT COMMIT. The user commits and pushes.

Finish by writing the ledger rows and reporting: which books were assessed,
their rates, which treatment each earned, and what is now next in the queue.
A session that ends with 3 books assessed and the ledger written has succeeded.
One that ends with 6 assessed and no ledger row has produced nothing.
