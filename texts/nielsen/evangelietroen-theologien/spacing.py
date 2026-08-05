#!/usr/bin/env python3
"""
spacing.py <printed_page> [<printed_page> ...]

Finds Sperrsatz (letterspaced emphasis) mechanically, so that it does not have
to be hunted for by eye on every page image.

How it works: tesseract's TSV gives a bounding box per word. Fit, by least
squares over all the words on the page, an advance width for each glyph; the
predicted width of a word is then the sum of its glyphs' advances. Normally set
words match the prediction. Letterspaced words are systematically wider, so
they fall out as large positive residuals. Three reweighting rounds keep the
spaced words themselves from polluting the fit.

Output is grouped into RUNS of adjacent flagged words, because Sperrsatz comes
in phrases. A RUN is nearly always real emphasis; a single flagged short word
is often noise and should be confirmed on the image before being marked.

Validated against printed p. IV, where the letterspacing was confirmed by eye:
it recovers the whole prayer quotation „jeg takker Dig, Gud i Himlene, at Du
ikke har fordret af et Menneske, at han skal begribe Christendommen!“ and
almost nothing else.
"""
import csv, os, subprocess, sys, tempfile
import numpy as np
from pagemap import pdfpage, scan_path

D = os.path.dirname(os.path.abspath(__file__))
SCAN = scan_path()
THRESH = float(os.environ.get("SPACING_THRESH", "1.16"))


def tsv_for(pdfpage, tmp):
    png = os.path.join(tmp, "pg")
    subprocess.run(["pdftoppm", "-f", str(pdfpage), "-l", str(pdfpage),
                    "-r", "300", "-png", SCAN, png],
                   check=True, capture_output=True)
    img = [os.path.join(tmp, f) for f in sorted(os.listdir(tmp)) if f.endswith(".png")][0]
    out = os.path.join(tmp, "out")
    env = dict(os.environ, TESSDATA_PREFIX=os.environ.get("TESSDATA_PREFIX", "/tmp/tessdata"))
    subprocess.run(["tesseract", img, out, "-l", "Fraktur", "--psm", "6", "tsv"],
                   check=True, capture_output=True, env=env)
    with open(out + ".tsv", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def flags(rows):
    W = [r for r in rows
         if r["level"] == "5" and r["text"].strip() and float(r["conf"]) > 30]
    words = [(r["text"].strip(), int(r["width"]),
              (int(r["block_num"]), int(r["par_num"]),
               int(r["line_num"]), int(r["word_num"]))) for r in W]
    if len(words) < 25:
        return []
    chars = sorted({c for t, _, _ in words for c in t})
    idx = {c: i for i, c in enumerate(chars)}
    A = np.zeros((len(words), len(chars)))
    b = np.zeros(len(words))
    for i, (t, wd, _) in enumerate(words):
        for c in t:
            A[i, idx[c]] += 1
        b[i] = wd
    wt = np.ones(len(words))
    for _ in range(3):
        x, *_ = np.linalg.lstsq(A * wt[:, None], b * wt, rcond=None)
        res = (b - A @ x) / np.maximum(A @ x, 1)
        wt = np.where(res > 0.12, 0.15, 1.0)
    ratio = b / np.maximum(A @ x, 1)
    out = [(k, t, float(r)) for (t, _, k), r in zip(words, ratio)
           if r > THRESH and len(t) >= 3]
    out.sort()
    return out


def report(printed):
    with tempfile.TemporaryDirectory() as tmp:
        f = flags(tsv_for(pdfpage(printed), tmp))
    print(f"--- printed p.{printed} ---")
    if not f:
        print("  (no letterspacing detected)")
        return
    run, prev = [], None
    def dump(run):
        if len(run) >= 2:
            print("  RUN     :", " ".join(w for _, w, _ in run))
        elif run:
            print(f"  single? : {run[0][1]}  ({run[0][2]:.2f}) — confirm on image")
    for k, t, r in f:
        if prev and k[:3] == prev[:3] and k[3] - prev[3] <= 2:
            run.append((k, t, r))
        else:
            dump(run)
            run = [(k, t, r)]
        prev = k
    dump(run)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        report(int(p))
