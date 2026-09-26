#!/usr/bin/env python3
"""build.py — the "entydig" dossier: Bohr's word, and whether it had a Danish past.

Bohr's writings are in copyright, so this script makes two versions from one
source (printed.yaml and intro.texfrag beside it):

  public  (default)  -> dossier.tex here, built by `make` and published.
                        Aligned originals in Part III are cut to the sentences
                        that carry the corresponding word; Part II's passages
                        are short quotations.
  private (--private -o PATH)  -> the same with the aligned originals whole.
                        Refused inside this repository; the usual place is
                        ~/research/entydig-dossier/ (its Makefile calls this).

How dossiers work in general: ../README.md.

It assembles four parts into dossier.tex:

  I   Before Bohr: every use of entydig/eentydig in the sks-search corpus
      (Kierkegaard, Sibbern, Nielsen, Brøchner, Høffding, Kroman ...), with
      counts of tvetydig/utvetydig for comparison.
  II  Bohr's Danish as printed, with page numbers: the hand-checked passages
      in printed.yaml (each transcribed from the page image).
  III Bohr's own Danish collections, Filosofiske Skrifter I and II: every
      paragraph with entydig, beside the aligned paragraph of the printed
      original (German or English), via bibliotek-search's bohr-fs.
  IV  Filosofiske Skrifter III and IV: counts only. Those volumes translate
      Bohr's English and German; their "entydig" is the editors' word.

Needs ~/sks-search and ~/bibliotek-search with their indexes built;
override the paths with $SKS_SEARCH, $BIB_SEARCH and $BIBLIOTEK.
"""
import collections, json, os, re, subprocess, sys, tempfile, datetime
import argparse
import yaml

def tc(s):
    return s[:1].upper() + s[1:].lower()

HERE = os.path.dirname(os.path.abspath(__file__))
SKS = os.environ.get("SKS_SEARCH") or os.path.expanduser("~/sks-search")
BIB = os.environ.get("BIB_SEARCH") or os.path.expanduser("~/bibliotek-search")
PY = sys.executable

ap = argparse.ArgumentParser(description="The entydig dossier (public by default).")
ap.add_argument("--private", action="store_true", help="keep aligned originals whole")
ap.add_argument("-o", "--output", default=os.path.join(HERE, "dossier.tex"))
args = ap.parse_args()
OUT = os.path.abspath(args.output)
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
if args.private and os.path.commonpath([OUT, REPO]) == REPO:
    sys.exit("build.py: --private output must lie outside the danish-texts repository.")

SENT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÆØÅ])")
def trim(text):
    """Public version: only the sentences of an aligned original that carry the word."""
    keep = [x for x in SENT.split(text) if ORIG.search(x)]
    return " … ".join(keep)

def run(args, cwd=None):
    r = subprocess.run(args, capture_output=True, text=True, cwd=cwd)
    if r.returncode != 0:
        sys.exit(f"build.py: {' '.join(args[:3])} failed:\n{r.stderr}")
    return r.stdout

def esc(s):
    s = s.replace("\\", r"\textbackslash{}")
    for a, b in (("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"), ("_", r"\_"),
                 ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"), ("^", r"\^{}")):
        s = s.replace(a, b)
    return s

DA = re.compile(r"(?<![\wæøå])(e?entydig\w*|Eentydig\w*|Entydig\w*)", re.I)
ORIG = re.compile(r"(?<![\w])(eindeutig\w*|unambiguous\w*|unique\w*|univocal\w*)", re.I)
def hl_da(s):   return DA.sub(r"\\tlg{\1}", s)
def hl_orig(s): return ORIG.sub(r"\\olg{\1}", s)

body, counts = [], collections.OrderedDict()

# ------------------------------------------------------------------ Part I
tmp = tempfile.mkdtemp(prefix="entydig-")
frag = os.path.join(tmp, "before.tex")
run([PY, os.path.join(SKS, "sks_search.py"), "dossier", "entydig* OR eentydig*",
     "-c", "all", "-n", "1000", "--order", "date", "-o", frag])
blocks = re.findall(r"\\begin\{quote\}\n(.*?)\n\\end\{quote\}\n% ([^\n]+)", open(frag).read(), re.S)

def tally(query):
    out = json.loads(run([PY, os.path.join(SKS, "sks_search.py"), "search", query,
                          "-c", "all", "--json", "-n", "100000"]))
    c = collections.Counter()
    for h in out["hits"]:
        ref = h["ref"]
        who = ref.split("/")[0] if "/" in ref.split(":")[0] else "kierkegaard"
        c[who] += h.get("n", 1)
    return c
tve, utve = tally("tvetydig*"), tally("utvetydig*")

body.append("\\part*{I.\\quad Before Bohr: the Danish philosophical corpus}\n"
            "\\addcontentsline{toc}{part}{I.\\quad Before Bohr}\n\n")
rows = []
for who in sorted(set(tve) | set(utve), key=lambda w: -tve.get(w, 0)):
    rows.append(f"{esc(who)} & {tve.get(who, 0)} & {utve.get(who, 0)} \\\\")
body.append("\\noindent Occurrences in the sks-search index (SKS, and the transcriptions "
            "and e-books of the other authors). \\emph{entydig} and \\emph{eentydig} occur "
            f"{len(blocks)} times in all, every one below; the old word for the "
            "opposite, \\emph{tvetydig}, and its negation \\emph{utvetydig} are counted "
            "for comparison.\n\n"
            "\\begin{center}\\begin{tabular}{@{}lrr@{}}\\toprule\n"
            "author & \\emph{tvetydig*} & \\emph{utvetydig*}\\\\\\midrule\n"
            + "\n".join(rows) + "\n\\bottomrule\\end{tabular}\\end{center}\n\n")
CAT = os.environ.get("DANISH_TEXTS") or os.path.expanduser("~/danish-texts")
venues = {}
try:
    for a in yaml.safe_load(open(os.path.join(CAT, "catalog.yaml")))["authors"]:
        for w in a["works"]:
            venues[f"{a['id']}/{w['id']}"] = ", ".join(x for x in (str(w.get("year") or ""),
                                                             w.get("venue") or "") if x)
except OSError:
    pass
for b, c in blocks:
    b = re.sub(r"\\\$([^$]{1,40}?)\\\$", r"$\1$", b)      # sks-search escapes inline math
    slug = c.split(":")[0]
    where = f" — {venues[slug]}" if slug in venues else ""
    body.append("\\begin{quote}\n" + hl_da(b) + "\n\\end{quote}\n\\dcite{" + esc(c + where) + "}\n\n")
counts[("I", "entydig/eentydig in the sks-search corpus")] = len(blocks)

# ------------------------------------------------------------------ Part II
body.append("\\part*{II.\\quad Bohr's Danish in print}\n"
            "\\addcontentsline{toc}{part}{II.\\quad Bohr's Danish in print}\n\n"
            "\\noindent Each passage was transcribed from the page image and checked "
            "against it; the page is the one printed on it.\n\n")
printed = yaml.safe_load(open(os.path.join(HERE, "printed.yaml")))
for item in printed:
    body.append("\\section{%s}\n\n" % esc(item["heading"]))
    if item.get("note"):
        body.append("\\noindent " + esc(item["note"]).strip() + "\n\n")
    if item.get("variants"):
        cols = item["columns"]
        spec = "@{}" + ">{\\raggedright\\arraybackslash}p{%.3f\\textwidth}" % (0.80 / len(cols)) * len(cols) + "@{}"
        body.append("{\\small\\begin{longtable}{" + spec + "}\\toprule\n"
                    + " & ".join("\\textbf{%s}" % esc(c) for c in cols) + "\\\\\\midrule\n")
        for row in item["variants"]:
            cells = [hl_orig(hl_da(esc(x))) for x in row]
            body.append(" & ".join(cells) + "\\\\[1ex]\n")
        body.append("\\bottomrule\\end{longtable}}\n")
    for p in item.get("passages", []):
        body.append("\\begin{quote}\n" + hl_da(esc(p["text"].strip())) + "\n\\end{quote}\n"
                    "\\dcite{" + esc(p["cite"]) + "}\n\n")
    counts[("II", item["heading"])] = len(item.get("passages", [])) + len(item.get("variants", []))

# ------------------------------------------------------------------ Part III
body.append("\\part*{III.\\quad Bohr's Danish collections: Filosofiske Skrifter I--II}\n"
            "\\addcontentsline{toc}{part}{III.\\quad Filosofiske Skrifter I--II}\n\n"
            "\\noindent Every paragraph of \\emph{Filosofiske Skrifter} I and II with "
            "\\emph{entydig}. The Danish is unpaginated there. Beneath each, in small type, "
            "is the paragraph of the printed original it was aligned to (OCR of the "
            "\\emph{Collected Works} extract), with the words that correspond marked "
            "\\olg{like this}. An alignment marked ``$\\approx$'' is right about nine times "
            "in ten; the usual error is a slip of one paragraph.\n\n")
def fs(vol):
    return json.loads(run([PY, "bib.py", "bohr-fs", "entydig* OR eentydig*", "--vol", str(vol),
                           "--json", "--full", "-n", "1000"], cwd=BIB))
for vol in (1, 2):
    hits = fs(vol)
    body.append("\\section{Filosofiske Skrifter %s}\n\n" % ("I" if vol == 1 else "II"))
    cur = None
    for h in hits:
        if h["essay"] != cur:
            cur = h["essay"]
            src = (f" \\normalfont({esc(h['source'])})" if h.get("source") else "")
            body.append("\\subsection{%s%s}\n\n" % (esc(tc(cur)), src))
            counts[("III", f"FS {vol}: {tc(cur)}")] = 0
        counts[("III", f"FS {vol}: {tc(cur)}")] += 1
        body.append("\\begin{quote}\n" + hl_da(esc(h["text"])) + "\n\\end{quote}\n")
        body.append("\\dcite{" + esc(f"Filosofiske Skrifter {vol}, {tc(cur)}, ¶{h['seq']}"
                                     f" — {h['locator']}") + "}\n")
        pr = h.get("printed")
        if isinstance(pr, dict):
            pr = pr.get("text") or ""
        if pr and h.get("method") != "matched":
            shown = pr if args.private else trim(pr)
            if shown:
                body.append("{\\footnotesize\\begin{quote}\\itshape\n" + hl_orig(esc(shown)) +
                            "\n\\end{quote}}\n")
            else:
                body.append("{\\footnotesize\\begin{quote}\\itshape (No corresponding word "
                            "in the aligned paragraph of the original.)\\end{quote}}\n")
        body.append("\n")

# ------------------------------------------------------------------ Part IV
body.append("\\part*{IV.\\quad Filosofiske Skrifter III--IV (counts only)}\n"
            "\\addcontentsline{toc}{part}{IV.\\quad Filosofiske Skrifter III--IV}\n\n"
            "\\noindent These volumes translate Bohr's English and German; "
            "\\emph{entydig} there is the translators' word, not his. Counted, not quoted.\n\n"
            "\\begin{center}\\begin{tabular}{@{}p{0.8\\textwidth}r@{}}\\toprule essay & paragraphs\\\\\\midrule\n")
for vol in (3, 4):
    c = collections.Counter(h["essay"] for h in fs(vol))
    for essay, n in c.items():
        body.append(f"FS {vol}: {esc(tc(essay))} & {n}\\\\\n")
        counts[("IV", f"FS {vol}: {tc(essay)}")] = n
body.append("\\bottomrule\\end{tabular}\\end{center}\n")

# ------------------------------------------------------------------ assemble
intro = open(os.path.join(HERE, "intro.texfrag")).read() if os.path.exists(
    os.path.join(HERE, "intro.texfrag")) else ""
today = datetime.date.today()
rights = (r"The dossier is private: it reproduces the aligned originals whole, and "
          r"Bohr's writings are in copyright." if args.private else
          r"Bohr's writings are in copyright. \emph{Filosofiske Skrifter} I--IV appear "
          r"in this collection with the rights-holders' permission; the other Bohr "
          r"passages here are brief quotations for the purposes of study, and the "
          r"aligned originals are cut to the sentences that bear on the word.")
head = rf"""% dossier.tex — GENERATED by build.py; edit printed.yaml or intro.texfrag, then `make`.
% {"PRIVATE: aligned originals whole. Never publish." if args.private else "Public version."}
\documentclass[11pt]{{article}}
\usepackage[letterpaper,margin=1in]{{geometry}}
\usepackage{{fontspec}}
\IfFileExists{{libertinus.sty}}{{\usepackage{{libertinus}}}}{{\setmainfont{{DejaVu Serif}}}}
\IfFileExists{{danish.ldf}}{{\usepackage[english,danish]{{babel}}}}{{\usepackage[english]{{babel}}}}
\usepackage{{microtype,xcolor,booktabs,longtable,array}}
\usepackage[hidelinks]{{hyperref}}
\setcounter{{secnumdepth}}{{0}}
\setcounter{{tocdepth}}{{2}}
\emergencystretch=5em
\tolerance=1500
\newcommand{{\dcite}}[1]{{{{\nopagebreak\raggedleft\small #1\par}}\medskip}}
\newcommand{{\tlg}}[1]{{{{\setlength{{\fboxsep}}{{0.8pt}}\colorbox{{yellow}}{{#1}}}}}}
\newcommand{{\olg}}[1]{{{{\setlength{{\fboxsep}}{{0.8pt}}\colorbox{{cyan!25}}{{#1}}}}}}
\title{{\emph{{Entydig}} hos Niels Bohr\\[0.5ex]\large {"Kildedossier (privat)" if args.private else "Kildedossier"}}}
\author{{Compiled from sks-search and bibliotek-search}}
\date{{{today.day} {today.strftime('%B')} {today.year}}}
\begin{{document}}
\maketitle
\begin{{otherlanguage}}{{english}}
{intro}
\section{{About this dossier}}
\noindent Danish \tlg{{entydig}} is marked in yellow throughout; in the printed
originals, the corresponding \olg{{eindeutig}}, \olg{{unique}} or \olg{{unambiguous}}
is marked in blue. {rights} Its four parts are listed in the contents.
\end{{otherlanguage}}
\tableofcontents
\clearpage
"""
out = OUT
open(out, "w").write(head + "".join(body) + "\n\\end{document}\n")
print(f"wrote {out}")
for (part, what), n in counts.items():
    print(f"  {part:4} {n:4}  {what}")
