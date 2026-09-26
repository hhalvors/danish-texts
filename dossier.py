#!/usr/bin/env python3
"""dossier.py — a cross-author source dossier on one word, as a LaTeX document.

Collects every passage in which a word occurs, across chosen authors, from
the collection's transcriptions (texts/<author>/<slug>/transcription.tex) and,
for Kierkegaard, from Søren Kierkegaards Skrifter (TEI). The passages come
from sks-search's `dossier` command; this script only groups them by author
and work, dates the works from catalog.yaml, makes each citation visible, and
highlights the matched word. How to use it is in texts/dossiers/README.md.

The ordinary way to run it is on a dossier directory, which `make` does
whenever that directory's selection.txt or intro.texfrag changes:

    python3 dossier.py texts/dossiers/tilegnelse

That reads the recipe from the '#%' lines of texts/dossiers/tilegnelse/selection.txt
(query, authors, title), keeps only the passages the file lists, puts
intro.texfrag (if there is one) at the head of the document, and writes
texts/dossiers/tilegnelse/dossier.tex. The same thing spelled out in flags:

    python3 dossier.py 'tilegn*' --authors sibbern,kierkegaard,brochner,hoeffding \\
        --title 'Tilegnelse' -o texts/dossiers/tilegnelse/dossier.tex \\
        --select texts/dossiers/tilegnelse/selection.txt

--select FILE keeps only the passages FILE lists, one reference per line
(texts/dossiers/tilegnelse/selection.txt is the example; its '#:' lines become
the dossier's statement of criterion). The selection is made by reading, not
by this script: regenerate without --select to see everything it chose from.

--ebooks adds passages from the privately held e-book reissues. Those are in
copyright and must never be committed or published (hoeffding-epub-inventory.md,
SEARCH-PLAYBOOK.md), so the script refuses --ebooks for any output path inside
this repository.

Needs ~/sks-search (override with $SKS_SEARCH). Compiles with lualatex (the
Makefile rule for texts/dossiers/) or xelatex.
"""
import argparse, collections, datetime, os, re, subprocess, sys, tempfile
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SKS = os.environ.get("SKS_SEARCH") or os.path.expanduser("~/sks-search")

ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
ap.add_argument("query", help="a dossier directory (texts/dossiers/<word>), or an FTS5 query such as 'tilegn*'")
ap.add_argument("--authors", help="comma-separated catalog ids, in the order wanted")
ap.add_argument("--title", help="the word, as the title shows it")
ap.add_argument("-o", "--output")
ap.add_argument("--ebooks", action="store_true", help="include e-book passages (never inside the repo)")
ap.add_argument("--select", metavar="FILE",
                help="keep only the passages whose references FILE lists (see a selection.txt)")
ap.add_argument("--intro", metavar="FILE", help="LaTeX to put at the head of the document")
args = ap.parse_args()

# Directory mode: the recipe lives in the directory's selection.txt.
if os.path.isdir(args.query):
    d = args.query
    args.select = args.select or os.path.join(d, "selection.txt")
    recipe = {}
    for line in open(args.select):
        m = re.match(r"#%\s*(\w+)\s*:\s*(.*\S)", line)
        if m:
            recipe[m.group(1)] = m.group(2)
    missing = [k for k in ("query", "authors", "title") if k not in recipe]
    if missing:
        sys.exit(f"dossier.py: {args.select} lacks '#% {missing[0]}: ...' recipe line(s)")
    args.query = recipe["query"]
    args.authors = args.authors or recipe["authors"]
    args.title = args.title or recipe["title"]
    args.output = args.output or os.path.join(d, "dossier.tex")
    if args.intro is None and os.path.exists(os.path.join(d, "intro.texfrag")):
        args.intro = os.path.join(d, "intro.texfrag")
for k in ("authors", "title", "output"):
    if not getattr(args, k):
        ap.error(f"--{k} is required unless the first argument is a dossier directory")
intro_tex = open(args.intro).read().strip() + "\n\n" if args.intro else ""

out_path = os.path.abspath(args.output)
if args.ebooks and os.path.commonpath([out_path, HERE]) == HERE:
    sys.exit("dossier.py: --ebooks output must lie outside the repository — "
             "the e-book reissues are in copyright and never committed.")
authors = [a.strip() for a in args.authors.split(",") if a.strip()]
selected, criterion = None, []
if args.select:
    selected = set()
    for line in open(args.select):
        if line.startswith("#:"):
            criterion.append(line[2:].strip())
        ref = line.split("#", 1)[0].strip()
        if ref:
            selected.add(ref)
def wanted(cite):
    """A citation string's reference is its first token: 'AE:187', 'sibbern/erkjendelse:49'."""
    return selected is None or re.split(r"\s{2,}|\s+\(", cite.strip())[0] in selected
stem = re.sub(r"[^\wæøåÆØÅ]", "", args.query.split()[0]).lower()

catalog = yaml.safe_load(open(os.path.join(HERE, "catalog.yaml")))
names, works = {}, {}
for a in catalog["authors"]:
    names[a["id"]] = a["name"]
    for w in a["works"]:
        val = (str(w.get("year") or ""), w.get("title", ""))
        works[(a["id"], w["id"])] = val
        # A work's id need not equal its directory name; its links say which it is.
        for sec in w.get("sections") or []:
            for l in sec.get("links") or []:
                m = re.search(r"/texts/([^/]+)/([^/]+)/", l.get("url", ""))
                if m and m.group(1) == a["id"]:
                    works.setdefault((a["id"], m.group(2)), val)
unknown = [a for a in authors if a not in names]
if unknown:
    sys.exit(f"dossier.py: not catalog author ids: {', '.join(unknown)}")

# ---------------------------------------------------------------- fetch
tmp = tempfile.mkdtemp(prefix="dossier-")
def fetch(corpus):
    fn = os.path.join(tmp, corpus + ".tex")
    r = subprocess.run([sys.executable, os.path.join(SKS, "sks_search.py"), "dossier",
                        args.query, "-c", corpus, "-n", "100000", "--order", "date",
                        "-o", fn], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"sks_search dossier -c {corpus} failed:\n{r.stderr}")
    BLK = re.compile(r"\\begin\{quote\}\n(.*?)\n\\end\{quote\}\n% ([^\n]+)", re.S)
    return [(b, c.strip()) for b, c in BLK.findall(open(fn).read())]

texts = fetch("texts")
sks_pub = fetch("published") if "kierkegaard" in authors else []
sks_all = fetch("sks") if "kierkegaard" in authors else []
ebooks = fetch("ebooks")

# Guard against a stale or partial sks-search index, which would otherwise
# drop passages silently: every non-Kierkegaard author must be present, and
# every reference in the selection must still be found.
def ref_of(c):
    return re.split(r"\s{2,}|\s+\(", c.strip())[0]
for aid in authors:
    if aid != "kierkegaard" and not any(c.startswith(aid + "/") for _, c in texts):
        sys.exit(f"dossier.py: the sks-search index holds no transcriptions by '{aid}'. "
                 "Rebuild it with SKS_TEXTS pointing at this repo's texts/ "
                 "(texts/dossiers/README.md, 'What it needs').")
if selected is not None:
    found = {ref_of(c) for _, c in texts + sks_all + ebooks}
    # E-book references matter only when e-books are wanted: the public build,
    # or a machine without the privately held epubs, simply skips them.
    lost = sorted(r for r in selected if r not in found and (args.ebooks or "(epub" not in r))
    if lost:
        sys.exit("dossier.py: these references in the selection were not found in the "
                 "index (renumbered by a re-transcription, or a stale index?):\n  "
                 + "\n  ".join(lost))

# ---------------------------------------------------------------- helpers
WORD = r"[\wæøåÆØÅäöüÄÖÜ]"
HIT = re.compile(rf"(?<!{WORD}|\\)({WORD}*{re.escape(stem)}{WORD}*)", re.I)
def highlight(body):
    return HIT.sub(r"\\tlg{\1}", body)

def hebrew(body):
    return re.sub(r"([\u0590-\u05FF]+)\u200f?", r"\\hebr{\1}", body)

def esc(s):
    return (s.replace("\\", r"\textbackslash{}").replace("&", r"\&").replace("%", r"\%")
             .replace("#", r"\#").replace("_", r"\_").replace("$", r"\$"))

def norm(s):
    s = re.sub(r"\\[a-zA-Z]+\*?|[{}]", " ", s)
    return re.sub(r"[^a-zæøåäöü]", "", s.lower())

def year_key(y):
    m = re.search(r"\d{4}", y or "")
    return int(m.group()) if m else 9999

body, counts = [], collections.OrderedDict()
nhits = 0
def quote(b, visible, comment):
    global nhits
    nhits += len(HIT.findall(b))
    body.append("\\begin{quote}\n" + hebrew(highlight(b)) + "\n\\end{quote}\n")
    body.append("\\dcite{" + esc(visible) + "}\n% " + comment + "\n\n")

def transcribed(aid, short):
    bywork = collections.OrderedDict()
    for b, c in texts:
        m = re.match(re.escape(aid) + r"/([^:]+):(\d+)\s+\((.*)\)$", c)
        if m and wanted(c):
            bywork.setdefault(m.group(1), []).append((int(m.group(2)), b, c, m.group(3)))
    for slug in sorted(bywork, key=lambda s: (year_key(works.get((aid, s), ("", ""))[0]), s)):
        yr, title = works.get((aid, slug), ("", slug))
        items = sorted(bywork[slug])
        # The transcription's own title: two volumes of one catalog work differ here.
        title = items[0][3].split(";")[0].strip() or title
        counts[(short, title + (f" ({yr})" if yr else ""))] = len(items)
        body.append("\\subsection{\\textit{%s}%s}\n\n" % (esc(title), f" ({esc(yr)})" if yr else ""))
        for n, b, c, paren in items:
            loc = paren.split(";", 1)[1].strip() if ";" in paren else ""
            quote(b, f"{short}, {title}" + (f", {loc}" if loc else "") + f"  [{aid}/{slug}:{n}]", c)
    return [norm(b)[:200] for items in bywork.values() for _, b, _, _ in items]

def kierkegaard():
    pubcites = {c for _, c in sks_pub}
    def vol(c):
        m = re.search(r"SKS (\d+), (\d+)", c)
        return (int(m.group(1)), int(m.group(2))) if m else (99, 0)
    bysig = collections.OrderedDict()
    for b, c in sorted(sks_pub, key=lambda x: vol(x[1])):
        if wanted(c):
            bysig.setdefault(c.split(":")[0], []).append((b, c))
    body.append("\\section{Published works}\n\n")
    for sig, items in bysig.items():
        v = vol(items[0][1])[0]
        counts[("Kierkegaard", f"{sig} (SKS {v})")] = len(items)
        body.append("\\subsection{%s \\normalfont(SKS %d)}\n\n" % (esc(sig), v))
        for b, c in items:
            quote(b, c, c)
    body.append("\\section{Journals, notebooks and papers}\n\n")
    cur = None
    for b, c in sks_all:
        if c in pubcites or not wanted(c):
            continue
        m = re.search(r"\((\d{4})", c)
        y = m.group(1) if m else "Undated"
        if y != cur:
            cur = y
            body.append("\\subsection{%s}\n\n" % y)
        k = ("Kierkegaard", f"Journals etc., {y}")
        counts[k] = counts.get(k, 0) + 1
        quote(b, c, c)

def ebook_part(aid, short, seen):
    eb, dropped = collections.OrderedDict(), 0
    for b, c in ebooks:
        m = re.match(re.escape(aid) + r"/([^(]+)\(epub[^)]*\):(\d+)\s+\((.*)\)$", c)
        if not m or not wanted(c):
            continue
        nb = norm(b)[:200]
        if any(nb and (nb in s or s in nb) for s in seen if s):
            dropped += 1
            continue
        eb.setdefault(m.group(1), []).append((int(m.group(2)), b, m.group(3), c.split()[0]))
    if not eb:
        return 0, dropped
    body.append("\\section{E-book texts (no printed pagination)}\n\n"
                "\\noindent\\textit{From privately held e-book reissues, in copyright: "
                "not for circulation. Located by chapter heading only; find the printed "
                "page before citing.}\n\n")
    n = 0
    for slug in sorted(eb, key=lambda s: (year_key(works.get((aid, s), ("", ""))[0]), s)):
        yr, title = works.get((aid, slug), ("", None))
        title = title or eb[slug][0][2].split(";")[0].strip()
        counts[(short, "e-book: " + title + (f" ({yr})" if yr else ""))] = len(eb[slug])
        body.append("\\subsection{\\textit{%s}%s \\normalfont(e-book)}\n\n"
                    % (esc(title), f" ({esc(yr)})" if yr else ""))
        for _, b, paren, ref in sorted(eb[slug]):
            ps = [p.strip() for p in paren.split(";")]
            chap = ps[1] if len(ps) > 2 else ""
            vis = (f"{short}, {title}" + (f", chapter “{chap}”" if chap else "")
                   + " — e-book text; printed page not located")
            quote(b, vis, vis + "  [" + ref + "]")   # the ref, for editing a selection file
            n += 1
    return n, dropped

# ---------------------------------------------------------------- assemble
roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
ebook_skipped = collections.Counter()
ebook_dropped = 0
for i, aid in enumerate(authors):
    short = names[aid].split()[-1]
    body.append("\\part*{%s.\\quad %s}\n\\addcontentsline{toc}{part}{%s.\\quad %s}\n\n"
                % (roman[i], esc(names[aid]), roman[i], esc(names[aid])))
    if aid == "kierkegaard":
        kierkegaard()
        continue
    has_eb = any(c.startswith(aid + "/") for _, c in ebooks)
    if has_eb and args.ebooks:
        body.append("\\section{Transcribed texts (with printed pagination)}\n\n")
    seen = transcribed(aid, short)
    if has_eb:
        if args.ebooks:
            _, d = ebook_part(aid, short, seen)
            ebook_dropped += d
        else:
            ebook_skipped[short] = sum(1 for _, c in ebooks if c.startswith(aid + "/") and wanted(c))

others = collections.Counter(c.split("/")[0] for _, c in texts
                             if c.split("/")[0] not in authors and c.split("/")[0] != "kierkegaard")

# ---------------------------------------------------------------- front matter
def clause_list(xs):
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]

shorts = [names[a].split()[-1] for a in authors]
total = sum(counts.values())
today = datetime.date.today()
datestr = f"{today.day} {today.strftime('%B')} {today.year}"
rows = "\n".join(f"{esc(w)} & {esc(t)} & {n} \\\\" for (w, t), n in counts.items())
table = ("\\begin{longtable}{@{}p{0.17\\textwidth}p{0.66\\textwidth}r@{}}\n\\toprule\n"
         "Author & Text & Passages\\\\\n\\midrule\n\\endhead\n" + rows +
         f"\n\\midrule\n& Total & {total}\\\\\n\\bottomrule\n\\end{{longtable}}\n")

items = []
for aid in authors:
    short = names[aid].split()[-1]
    if aid == "kierkegaard":
        nk = sum(v for (w, t), v in counts.items() if w == "Kierkegaard")
        items.append(rf"\item \textbf{{Kierkegaard:}} {nk} passages from "
                     r"\emph{Søren Kierkegaards Skrifter}, TEI "
                     r"edition (Det Kgl.\ Bibliotek), reading text only: no deletions, variants "
                     r"or editorial commentary. Published works are ordered by SKS volume, the "
                     r"journals, notebooks and papers by year of composition. Each passage is the "
                     r"whole SKS unit in which the word occurs, which for a published work can be "
                     r"a full page. The citation strings are sks-search's, verbatim.")
    else:
        n = sum(v for (w, t), v in counts.items() if w == short and not t.startswith("e-book"))
        nw = sum(1 for (w, t) in counts if w == short and not t.startswith("e-book"))
        items.append(rf"\item \textbf{{{esc(short)}:}} {n} passages from {nw} "
                     rf"work{'s' if nw != 1 else ''} transcribed in this collection. Diplomatic "
                     r"transcriptions; page references are the printed pages recorded in the "
                     r"transcription, and ``p.~109+'' means the passage begins on p.~109 and "
                     r"runs on.")
caveats = [
    (rf"\item The passages were found lexically and then selected by hand ({total} kept); "
     rf"see the selection file named in this file's header. " if selected is not None else
     r"\item The search is lexical. It catches every sense of the word, alongside the "
     r"epistemic and religious uses; nothing has been filtered by sense. ") +
    rf"Every word form containing \emph{{{esc(stem)}}} is \tlg{{highlighted}} ({nhits} in all).",
    r"\item The quotations are machine-assembled. An entry without a page break of its "
    r"own carries the page it begins on; for a quotation taken from late in a long "
    r"entry, check the printed page.",
]
if "kierkegaard" in authors:
    caveats.insert(1, r"\item Much of Kierkegaard's \emph{Notesbøger} (the \texttt{Not} sigla) "
                      r"records lectures and reading. Check the SKS commentary before attributing "
                      r"a notebook passage to him.")
for short, n in ebook_skipped.items():
    if n:
        caveats.append(rf"\item {n} further {'selected ' if selected is not None else ''}passages in e-book reissues of {esc(short)} are not "
                       r"reproduced: those editions are in copyright.")
if args.ebooks and ebook_dropped:
    caveats.append(rf"\item E-book passages duplicating a transcription have been dropped "
                   rf"({ebook_dropped}).")
if others and selected is None:
    caveats.append(r"\item The collection also holds passages by " +
                   clause_list([f"{esc(names.get(a, a).split()[-1])} ({n})"
                                for a, n in others.most_common()]) + ", not included here.")

selection_tex = ("\\subsection{Selection}\n\n\\noindent " + esc(" ".join(criterion)) + "\n\n") if criterion else ""
intro_lead = ("A selection from the passages" if selected is not None else "Every passage")
head = rf"""% dossier.tex — source dossier on the word {args.title}.
% GENERATED by dossier.py; do not edit by hand. Edit selection.txt or
% intro.texfrag beside it instead, then run `make` (see texts/dossiers/README.md).
% This file was produced by the equivalent of:
%   python3 dossier.py '{args.query}' --authors {",".join(authors)} --title '{args.title}' -o <this file>{" --ebooks" if args.ebooks else ""}{(" --select " + os.path.relpath(os.path.abspath(args.select), HERE)) if args.select else ""}
% Each passage is followed by a visible \dcite{{...}} and by sks-search's own
% citation string as a % comment, in the shape sks.el's `w' key produces.
% Compile with lualatex (Makefile) or xelatex.
\documentclass[11pt]{{article}}
\usepackage[letterpaper,margin=1in]{{geometry}}
\usepackage{{fontspec}}
\IfFileExists{{libertinus.sty}}{{\usepackage{{libertinus}}}}{{\setmainfont{{DejaVu Serif}}}}
\IfFileExists{{danish.ldf}}{{\usepackage[english,danish]{{babel}}}}{{\usepackage[english]{{babel}}}}
\usepackage{{microtype}}
\usepackage{{xcolor,booktabs,longtable}}
\usepackage[hidelinks,bookmarksnumbered]{{hyperref}}
\setcounter{{secnumdepth}}{{0}}
\setcounter{{tocdepth}}{{2}}
\makeatletter\renewcommand{{\@pnumwidth}}{{2.2em}}\makeatother
\emergencystretch=5em
\tolerance=1500
\newcommand{{\dcite}}[1]{{{{\nopagebreak\raggedleft\small #1\par}}\medskip}}
\newcommand{{\tlg}}[1]{{{{\setlength{{\fboxsep}}{{0.8pt}}\colorbox{{yellow}}{{#1}}}}}}
\IfFontExistsTF{{SBL Hebrew}}{{\newfontfamily\hebrewfont{{SBL Hebrew}}}}{{%
  \IfFontExistsTF{{Arial Hebrew}}{{\newfontfamily\hebrewfont{{Arial Hebrew}}}}{{%
    \newfontfamily\hebrewfont{{DejaVu Sans}}}}}}
\ifdefined\XeTeXversion \TeXXeTstate=1
  \newcommand{{\hebr}}[1]{{{{\hebrewfont\beginR #1\endR}}}}
\else
  \newcommand{{\hebr}}[1]{{{{\hebrewfont\textdir TRT #1}}}}
\fi
\title{{\emph{{{esc(args.title)}}} hos {esc(clause_list(shorts)).replace(" and ", " og ")}\\[0.5ex]\large {"Udvalgt kildedossier" if selected is not None else "Kildedossier"}}}
\author{{Danish Philosophical Texts}}
\date{{{datestr}}}
\begin{{document}}
\maketitle

\begin{{otherlanguage}}{{english}}
{intro_tex}\section{{About this dossier}}

\noindent {intro_lead} in which a form of the word occurs (query \texttt{{{esc(args.query)}}},
prefix-matched, so compounds are included), in {len(authors)} bodies of text:

\begin{{enumerate}}
{chr(10).join(items)}
\end{{enumerate}}

{selection_tex}\noindent Caveats:

\begin{{enumerate}}
{chr(10).join(caveats)}
\end{{enumerate}}

\subsection{{Contents by work}}
{table}
\end{{otherlanguage}}

\tableofcontents
\clearpage

"""
os.makedirs(os.path.dirname(out_path), exist_ok=True)
open(out_path, "w").write(head + "".join(body) + "\n\\end{document}\n")
print(f"{total} passages, {nhits} highlighted -> {out_path}")
for k, v in counts.items():
    print(f"  {k[0]:12} {v:4}  {k[1]}")
