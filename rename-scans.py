#!/usr/bin/env python3
"""Apply the renames in SCAN-RENAME.tsv, safely, and keep SCANS.tsv true.

Safety, in order:
  * the file is identified by its sha256 from SCANS.tsv BEFORE it is touched;
    a hash mismatch aborts that row rather than renaming the wrong file
  * a row whose new_name still contains ???? is skipped, loudly
  * a destination that already exists is skipped, never overwritten
  * every rename is recorded to SCAN-RENAME.done.tsv so it can be reversed
  * SCANS.tsv paths are rewritten at the end, so scans.py keeps resolving

MOVE-TO-BIBLIOTEK rows are the repo's own scan.pdf copies. Four are byte-identical
twins of a bibliotek file and are deleted; pascal-kierkegaard's is the only
original and is moved in. Deleting inside the repo needs the device's approval.

  python3 rename-scans.py --dry      show what would happen, change nothing
  python3 rename-scans.py            do it
"""
import csv, hashlib, os, shutil, sys

REPO = os.path.dirname(os.path.abspath(__file__))
BIB  = os.path.join(os.path.dirname(REPO), "bibliotek")
COLS = ["book","scan","sha256","bytes","pages","page_size","witness","note"]
DRY  = "--dry" in sys.argv


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 22), b""): h.update(c)
    return h.hexdigest()


def find_twin(path, want_hash, skip_path=None):
    """Any byte-identical PDF elsewhere in the library. Size is a free prefilter."""
    try: size = os.path.getsize(path)
    except OSError: return None
    for root, _, files in os.walk(BIB):
        for fn in files:
            if not fn.lower().endswith(".pdf"): continue
            q = os.path.join(root, fn)
            if skip_path and os.path.abspath(q) == os.path.abspath(skip_path): continue
            try:
                if os.path.getsize(q) != size: continue
            except OSError: continue
            if sha(q) == want_hash: return q
    return None


def load_scans():
    head, rows = [], []
    for line in open(os.path.join(REPO, "SCANS.tsv"), encoding="utf-8"):
        if line.startswith("#") or line.startswith("book\t"): head.append(line.rstrip("\n")); continue
        if line.strip(): rows.append(dict(zip(COLS, line.rstrip("\n").split("\t"))))
    return head, rows


def full(rel):
    return os.path.join(REPO, rel) if rel.startswith("texts/") else os.path.join(BIB, rel)


def main():
    head, srows = load_scans()
    want = {}                                   # current rel path -> expected sha
    for r in srows:
        if r["scan"] != "UNRESOLVED": want[r["scan"]] = r["sha256"]

    plan, skip = [], []
    for line in open(os.path.join(REPO, "SCAN-RENAME.tsv"), encoding="utf-8"):
        if line.startswith("#") or line.startswith("current\t") or not line.strip(): continue
        cur, folder, new, src, books = (line.rstrip("\n").split("\t") + [""] * 5)[:5]
        if not new.strip():                      skip.append((cur, "blank new_name - skipped")); continue
        if "????" in new:                        skip.append((cur, "year still ???? - fill it in")); continue
        if cur not in want:                      skip.append((cur, "not in SCANS.tsv")); continue
        src_abs = full(cur)
        if not os.path.exists(src_abs):          skip.append((cur, "file not found")); continue
        if folder == "MOVE-TO-BIBLIOTEK":
            # BUG FIXED 2026-09-13, after it fired: this used to resolve to a bare
            # filename, which dropped six scans at the TOP LEVEL of bibliotek instead
            # of into an author folder -- and, because the destination name was new,
            # the duplicate check never saw the byte-identical twin already sitting in
            # that folder. Result: nothing deduplicated and the duplication doubled.
            # A move now REQUIRES an author folder, and dedup is checked by hash across
            # the whole library rather than at the single destination path.
            print(f"REFUSED    {cur}\n           MOVE-TO-BIBLIOTEK needs an author folder, "
                  f"e.g. 'Hoeffding, Harald'. Put it in the new_folder column.")
            skip.append((cur, "no author folder given for the move")); continue
        dest_rel = f"{folder}/{new}"
        plan.append((cur, src_abs, dest_rel, os.path.join(BIB, dest_rel), folder))

    done = []
    for cur, src_abs, dest_rel, dest_abs, folder in plan:
        if sha(src_abs) != want[cur]:
            print(f"ABORT ROW  {cur}\n           hash does not match SCANS.tsv - not touched"); continue
        twin = find_twin(src_abs, want[cur], skip_path=src_abs)
        if twin and os.path.abspath(twin) != os.path.abspath(dest_abs):
            print(f"DUPLICATE  {cur}\n           byte-identical copy already at "
                  f"{os.path.relpath(twin, BIB)} - rename THAT one and drop this copy")
            skip.append((cur, "duplicate of an existing library file")); continue
        if os.path.exists(dest_abs) and os.path.abspath(dest_abs) != os.path.abspath(src_abs):
            if sha(dest_abs) == want[cur]:
                print(f"DUPLICATE  {cur}\n           identical file already at {dest_rel}")
                if not DRY and cur.startswith("texts/"):
                    os.remove(src_abs); print(f"           removed the repo copy")
                done.append((cur, dest_rel, "dedup")); continue
            print(f"SKIP       {cur}\n           {dest_rel} exists and differs - resolve by hand"); continue
        verb = "MOVE" if folder == "MOVE-TO-BIBLIOTEK" else "RENAME"
        print(f"{verb:10s} {cur}\n           -> {dest_rel}")
        if not DRY:
            os.makedirs(os.path.dirname(dest_abs), exist_ok=True)
            shutil.move(src_abs, dest_abs)
        done.append((cur, dest_rel, verb.lower()))

    for cur, new_rel, how in done:
        for r in srows:
            if r["scan"] == cur: r["scan"] = new_rel
    if not DRY and done:
        with open(os.path.join(REPO, "SCANS.tsv"), "w", encoding="utf-8") as f:
            f.write("\n".join(head + ["\t".join(r.get(c, "") for c in COLS) for r in srows]) + "\n")
        with open(os.path.join(REPO, "SCAN-RENAME.done.tsv"), "a", encoding="utf-8") as f:
            for cur, new_rel, how in done: f.write(f"{cur}\t{new_rel}\t{how}\n")

    print(f"\n{'would apply' if DRY else 'applied'}: {len(done)}   skipped: {len(skip)}")
    for c, why in skip: print(f"  skip  {c[:60]:62s} {why}")
    if DRY: print("\nrun without --dry to apply")


if __name__ == "__main__":
    main()
