#!/usr/bin/env python3
"""Validate catalog.yaml against the record definitions in
hhalvors.github.io/DanishTexts.hs, which is what actually fails the site build.

Field names come from  camelToKebab . lcFirst . stripPrefix <prefix>  applied to
the Haskell field name, so e.g. authorSecondaryLiterature -> secondary-literature.
Aeson IGNORES unknown keys, so extra fields are not errors; a MISSING required
key is what breaks the build.
"""
import sys, yaml

# (name, required?)  -- required = not Maybe in the Haskell record
LINK    = [("label",1),("url",1)]
SECTION = [("title",1),("status",1),("links",1)]
WORK    = [("id",1),("title",1),("year",1),("venue",0),("note",0),("sections",1)]
AUTHOR  = [("id",1),("name",1),("dates",1),("bio",1),("works",1),
           ("modern-editions",0),("secondary-literature",0),("bibliography",0)]
EDITION = [("id",1),("editor",0),("title",1),("year",1),("venue",0),("note",0),("sections",1)]
SECLIT  = [("id",1),("author",1),("title",1),("year",1),("venue",0),("doi",0),
           ("note",0),("sections",1)]
REFER   = [("id",1),("title",1),("authors",1),("year",1),("venue",0),("note",0),
           ("volumes",0),("links",0)]
BIBLIO  = [("published",0),("manuscripts",0)]
ENTRY   = [("year",1),("title",1),("venue",0),("note",0),("incollection",0)]

problems = []

def check(obj, spec, where, typename):
    if not isinstance(obj, dict):
        problems.append(f"{where}: expected a mapping for {typename}, got {type(obj).__name__}")
        return False
    for key, req in spec:
        if req and key not in obj:
            problems.append(f"{where}: {typename} is missing required key '{key}'  "
                            f"(has: {', '.join(sorted(obj))})")
    return True

def sections(lst, where):
    if not isinstance(lst, list):
        problems.append(f"{where}: sections must be a list"); return
    for i, s in enumerate(lst):
        w = f"{where}.sections[{i}]"
        if check(s, SECTION, w, "Section"):
            links = s.get("links")
            if links is None: continue
            if not isinstance(links, list):
                problems.append(f"{w}: links must be a list (use [] when empty)"); continue
            for j, l in enumerate(links):
                check(l, LINK, f"{w}.links[{j}]", "Link")

doc = yaml.safe_load(open(sys.argv[1] if len(sys.argv) > 1 else "catalog.yaml"))
if "authors" not in doc:
    problems.append("$: Catalog is missing required key 'authors'")

for ai, a in enumerate(doc.get("authors") or []):
    aw = f"$.authors[{ai}]" + (f" ({a.get('id')})" if isinstance(a, dict) else "")
    if not check(a, AUTHOR, aw, "Author"): continue
    for wi, w in enumerate(a.get("works") or []):
        ww = f"{aw}.works[{wi}] ({w.get('id') if isinstance(w,dict) else '?'})"
        if check(w, WORK, ww, "Work"): sections(w.get("sections") or [], ww)
    for ei, e in enumerate(a.get("modern-editions") or []):
        ew = f"{aw}.modern-editions[{ei}] ({e.get('id') if isinstance(e,dict) else '?'})"
        if check(e, EDITION, ew, "Edition"): sections(e.get("sections") or [], ew)
    for si, s in enumerate(a.get("secondary-literature") or []):
        sw = f"{aw}['secondary-literature'][{si}] ({s.get('id') if isinstance(s,dict) else '?'})"
        if check(s, SECLIT, sw, "SecondaryLit"): sections(s.get("sections") or [], sw)
    b = a.get("bibliography")
    if b is not None and check(b, BIBLIO, f"{aw}.bibliography", "Bibliography"):
        for k in ("published", "manuscripts"):
            for bi, e in enumerate(b.get(k) or []):
                check(e, ENTRY, f"{aw}.bibliography.{k}[{bi}]", "BibEntry")

for ri, r in enumerate(doc.get("references") or []):
    rw = f"$.references[{ri}] ({r.get('id') if isinstance(r,dict) else '?'})"
    if check(r, REFER, rw, "Reference"):
        for j, l in enumerate(r.get("links") or []):
            check(l, LINK, f"{rw}.links[{j}]", "Link")

print(f"{len(problems)} problem(s)")
for p in problems: print("  " + p)
sys.exit(1 if problems else 0)
