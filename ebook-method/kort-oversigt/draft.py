#!/usr/bin/env python3
"""ebook-method/kort-oversigt/draft.py (copied 2026-10-14 from ebook-method/etik/draft.py: NB layer + footnotes;
changes for this book are marked "oplevelse:") -- formerly ebook-method/etik/draft.py -- the script-built DRAFT transcription of Høffding, Etik (4th ed., 1913), from the
scan's text layer (the National Library of Norway's OCR, laid into the scan by nb_scan.py).  Adapted from
ebook-method/spinozas-ethica/draft.py (comments marked spinozas-ethica are that book's and kept where harmless).
Step 1 of TRANSCRIPTION-PLAYBOOK.md §00 for a book with no e-book: no one re-types the text; the layer is turned into
LaTeX by rule, and everything after this is correction by list (check.py decisions), never re-typing.
Self-contained; needs python3 and pdftotext (poppler).

    python3 ebook-method/etik/draft.py           report only: pages, paragraphs, headings, notes, flags
    python3 ebook-method/etik/draft.py --emit    write texts/hoeffding/etik/transcription.tex from template.tex,
                                                 then apply patches.PATCHES and layout()
    ... --emit --raw     the draft without patches.py and layout() (to write a new patch against)
    ... --emit --force   overwrite a transcription.tex that is no longer the plain draft (backup made first)
    python3 ebook-method/etik/draft.py --post    LAST step, after collate/check.py --italics --apply: patches.POST

What the rules do, page by page (settings in pagemap.py):
  * lines are rebuilt from the word boxes (the layer's own order is scrambled: skew and curvature are fitted, as in
    collate/check.py), page furniture (folio line, watermark text, marks in the margin) dropped;
  * punctuation, which the layer boxes separately, is attached to its word; the layer's straight " is the print's
    closing quote “ (the opening one is „);
  * a hyphen at a line end joins the word (kept when the next part starts with a capital); across a page turn the
    word is split with %, the house convention;
  * a free-standing hyphen, and the hyphen in a range of numbers, is the print's long dash: ---;
  * a paragraph begins at an indented line; a centred line is set as a heading;
  * the running head (chapter title + folio) is dropped; the layer's soft hyphen (U+00AD) is a line-end hyphen;
  * footnotes: the lines under the text that begin with 1), 2), ... (the layer reads 1) also as *) or ')) are the
    notes, put at their reference marks as \\footnote[k]{...}, numbered per page as printed; a note whose mark is
    not found, or a note that runs over to the next page, is set where it stands with a "% CHECK" comment;
  * the running head is the two folios (the volume's and the book's own); the series line and the sheet number at a
    sheet's foot are dropped;
  * names in small capitals: a word in capitals in the layer (not a roman numeral) is set \\textsc{Name}; a word with
    a capital stem and a short lowercase tail (SPINOza) when the stem is in capitals elsewhere in the book.
Every rule-made choice that needs the image is marked "% CHECK" in the output.  Letterspacing and italics are NOT
found here: run collate/check.py --italics after the collation.
"""
import os, re, sys, html, subprocess, statistics, shutil, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE); import pagemap as C
BOOK = C.BOOKDIR; TEX = os.path.join(BOOK, 'transcription.tex')   # oplevelse: was etik's path (a copied draft.py overwrote etik's transcription.tex once, 2026-10-14; restored)
if '--post' in sys.argv:                                # see the docstring: the last step of the pipeline
    import importlib.util
    spec = importlib.util.spec_from_file_location('patches', os.path.join(HERE, 'patches.py'))
    P = importlib.util.module_from_spec(spec); spec.loader.exec_module(P)
    new = open(TEX, encoding='utf-8').read(); bad = []
    _pf = os.path.join(HERE, 'postfix.tsv')            # etik: page-scoped corrections read at the image, one per line
    if os.path.exists(_pf):
        for _l in open(_pf, encoding='utf-8'):
            if _l[:1].isdigit():
                _f = _l.rstrip('\n').split('\t'); P.POST.append((('pg', int(_f[0])), _f[1], _f[2], _f[3] if len(_f) > 3 else 'postfix.tsv'))
    for kind, find, repl, why in P.POST:
        if kind == 'g':                                 # etik: a regex for a fault that recurs: all matches (at least one)
            new = re.sub(find, repl, new); continue    # (none left is fine: a rerun, or the fault mended upstream)
        if isinstance(kind, tuple):                     # etik: ('pg', N): literal, exactly once on printed page N
            a_ = new.index(f'% --- p. {kind[1]} ---'); b_ = new.find('% --- p. ', a_ + 10); b_ = len(new) if b_ < 0 else b_
            seg = new[a_:b_]
            if seg.count(find) != 1: bad.append((seg.count(find), f'p. {kind[1]}: ' + find[:60], why)); continue
            new = new[:a_] + seg.replace(find, repl) + new[b_:]; continue
        n = new.count(find) if kind == 's' else len(re.findall(find, new, re.S))
        if n != 1: bad.append((n, find[:70], why)); continue
        new = new.replace(find, repl) if kind == 's' else re.sub(find, repl, new, count=1, flags=re.S)
    print(f'post patches: {len(P.POST) - len(bad)} applied')
    for after_, frag_ in getattr(P, 'INSERT', []):     # religioese: text from elsewhere (pp. 27-28, missing from the scan), after a find
        k_ = new.index(after_); assert new.count(after_) == 1, after_; k_ += len(after_)
        new = new[:k_] + open(os.path.join(HERE, frag_), encoding='utf-8').read() + new[k_:]
        print('inserted', frag_)
    # etik: letterspacing (\\emph): the words nb_scan.py spaced found wider than their letters (names, mostly in the
    # notes).  On each page the n-th such word goes to the n-th plain occurrence of the word that best matches it
    # (the text is corrected, the OCR's word is not); small capitals (\\textsc) are already the body's names.
    _sp = os.path.join(HERE, 'spaced.tsv'); nsp = 0
    if os.path.exists(_sp):
        import difflib
        SP = {}
        for _l in open(_sp, encoding='utf-8'):
            if _l[:1].isdigit(): _f = _l.split('\t'); SP.setdefault(int(_f[0]), []).append(_f[1])
        norm = lambda w: re.sub(r'[^A-Za-zÀ-ÿ]', '', w).lower()
        for p_ in C.PAGES:                              # oplevelse: was range(1, 600) (etik)
            ws_ = SP.get(C.pdfpage(p_))
            if not ws_ or f'% --- p. {p_} ---' not in new: continue
            a_ = new.index(f'% --- p. {p_} ---'); b_ = new.find('% --- p. ', a_ + 10); b_ = len(new) if b_ < 0 else b_
            seg = new[a_:b_]; used = set()
            for w in ws_:
                nw = norm(w)
                if len(nw) < 4: continue
                best = None
                for m_ in re.finditer(r'(?<![\\{A-Za-zÀ-ÿ])[A-ZÀ-ÞÆØÅ][A-Za-zÀ-ÿ\'’-]{2,}', seg):
                    if m_.start() in used or seg[max(0, m_.start() - 8):m_.start()].endswith(('textsc{', 'emph{', 'textsc{\\', '\\')): continue
                    if m_.group(0).isupper(): continue      # a word in capitals is a heading's, not a spaced name
                    r_ = difflib.SequenceMatcher(None, nw, norm(m_.group(0))).ratio()
                    if r_ >= 0.75 and (best is None or r_ > best[0] + 0.1): best = (r_, m_)
                    if r_ == 1: break
                if best: used.add(best[1].start())
            notes_ = []                                 # the spans of the notes on the page
            for m_ in re.finditer(r'\\footnote\[\d\]\{', seg):
                d_ = 1; j_ = m_.end()
                while j_ < len(seg) and d_: d_ += {'{': 1, '}': -1}.get(seg[j_], 0); j_ += 1
                notes_.append((m_.end(), j_))
            for st_ in sorted(used, reverse=True):
                m_ = re.match(r"[A-ZÀ-ÞÆØÅ][A-Za-zÀ-ÿ'’-]{2,}", seg[st_:]); e_ = st_ + len(m_.group(0))
                if seg[e_ - 1] in "'’-": e_ -= 1
                # in a note the print letterspaces a name; in the text it sets it in small capitals, which are as wide
                cmd_ = 'emph' if any(a <= st_ < b for a, b in notes_) else 'textsc'
                seg = seg[:st_] + '\\' + cmd_ + '{' + seg[st_:e_] + '}' + seg[e_:]; nsp += 1
            seg = re.sub(r'\\(emph|textsc)\{([^{}]*)\} \\\1\{', r'\\\1{\2 ', seg)   # „Stuart Mill“: one command
            new = new[:a_] + seg + new[b_:]
    print(f'letterspacing: {nsp} words set \\emph')
    for b_ in bad: print('  POST PATCH NOT APPLIED (%d matches): %r -- %s' % b_)
    if bad: sys.exit('not written: every post patch must match exactly once (run the whole pipeline from --emit)')
    open(TEX, 'w', encoding='utf-8').write(new); print('wrote', TEX); sys.exit(0)
ROMAN = []; PAGES = list(C.DRAFT_PAGES); PLAIN_MARKS = False # kort-oversigt: the Fortale (unpaged) is static in template.tex
FLAGS = []
def flag(p, what): FLAGS.append((p, what)); return f'% CHECK p. {p}: {what}\n'

# ---------------- the layer, all pages in one pdftotext call ----------------
lo, hi = min(C.pdfpage(p) for p in PAGES), max(C.pdfpage(p) for p in PAGES)
X = subprocess.run(['pdftotext', '-bbox', '-f', str(lo), '-l', str(hi), C.scan_path(), '-'], capture_output=True, text=True).stdout
RAW = X.split('<page ')[1:]
def words(p):
    pg = RAW[C.pdfpage(p) - lo]
    ph = float(re.search(r'height="([\d.]+)"', pg).group(1))
    pw = float(re.search(r'width="([\d.]+)"', pg).group(1))
    ws = [(html.unescape(w[4]).replace('\xad', '-'), tuple(map(float, w[:4]))) for w in
          re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', pg)]
    PW[p] = pw
    return ws, ph
PW = {}
def edge_junk(p, ln):
    # etik: NB's scans are cropped tight; letters of the facing page, at the gutter edge, are read as words (";8",
    # "\\", "I" before each line): drop a short word wholly within 8 pt of the page's edge and set apart from the
    # line by a gap wider than a word space (the line's own last letters can reach the edge: "ti" "l")
    pw = PW.get(p, 1e9)
    if len(ln) > 1 and len(ln[0][0]) <= 3 and ln[0][1][2] < 8 and ln[1][1][0] - ln[0][1][2] >= 8: ln = ln[1:]
    elif len(ln) > 1 and len(ln[0][0]) <= 2 and ln[0][1][0] < 3 and ln[0][1][2] < 9 and ln[1][1][0] - ln[0][1][2] >= 3:
        ln = ln[1:]                                     # a page cropped to the text: the junk touches the edge (p. 323)
    if len(ln) > 1 and len(ln[-1][0]) <= 3 and ln[-1][1][0] > pw - 8 and ln[-1][1][0] - ln[-2][1][2] >= 8: ln = ln[:-1]
    return ln
def cluster(ws):                                   # as in collate/check.py: fit skew a, curvature c; cluster; sort by x
    xm = sum(b[0] for w, b in ws) / max(1, len(ws))
    yof = lambda b, a, c: (b[1] + b[3]) / 2 - a * b[0] - c * (b[0] - xm) ** 2
    def peak(ac):
        h = {}
        for w, b in ws: k = round(yof(b, *ac)); h[k] = h.get(k, 0) + 1
        return sum(v * v for v in h.values())
    a = max((k / 500 for k in range(-30, 31)), key=lambda a: peak((a, 0)))
    c = max((k / 1e5 for k in range(-20, 21)), key=lambda c: peak((a, c)))
    for _ in range(2): a, c = max(((a + i / 1000, c + k / 2e5) for i in range(-4, 5) for k in range(-6, 7)), key=peak)
    big = [b[3] - b[1] for w, b in ws if len(w) > 2]
    lh = sorted(big)[len(big) // 2] if big else 10
    lines = []
    for w, b in sorted(ws, key=lambda t: yof(t[1], a, c)):
        yc = yof(b, a, c)
        if lines and yc - lines[-1][0] < 0.6 * lh: lines[-1][1].append((w, b))
        else: lines.append([yc, [(w, b)]])
    return [(yc, sorted(ln, key=lambda t: t[1][0])) for yc, ln in lines], lh
LETTER = re.compile(r'[A-Za-zÀ-ÖØ-öø-ÿ]')
JUNK = re.compile(r'KONGELIGE|BIBLIOTEK')
def page_lines(p):
    ws, ph = words(p)
    ws = [t for t in ws if not JUNK.search(t[0])]
    lines, lh = cluster(ws)
    real = [ln for yc, ln in lines if sum(len(LETTER.findall(w)) for w, b in ln) >= 3]
    if not real: return [], lh
    # punctuation the layer boxes on its own (tiny boxes, off the baseline) forms fragment lines: merge each into
    # the nearest real line, by height
    if len(real) < len(lines):
        reals = [(yc, ln) for yc, ln in lines if sum(len(LETTER.findall(w)) for w, b in ln) >= 3]
        for yc, ln in lines:
            if sum(len(LETTER.findall(w)) for w, b in ln) >= 3: continue
            t = ' '.join(w for w, b in ln)
            if len(t) > 8 or re.fullmatch(r'\d+|\d+\s+\d+|[IVX]+\s?\.?', t): reals.append((yc, ln)); continue   # folio, section numeral
            j = min(range(len(reals)), key=lambda j: abs(reals[j][0] - yc))
            if abs(reals[j][0] - yc) > 0.8 * lh and re.search(r'\w', t) and not re.fullmatch(r'[IVXLlx1]{1,7}\s?[.,:]?', t.strip()):
                reals.append((yc, ln)); continue        # etik: a short line of its own ("p. 122."), not a chapter's numeral
            if re.fullmatch(r"[\w*'’!>?]{1,2}\)", t):     # a note's number, boxed apart: it begins the line to its right
                cand = [k for k in range(len(reals)) if reals[k][1][0][1][0] >= ln[-1][1][2] - 2 and abs(reals[k][0] - yc) < 1.5 * lh]
                if cand: j = min(cand, key=lambda k: abs(reals[k][0] - yc))
            reals[j] = (reals[j][0], sorted(reals[j][1] + ln, key=lambda t: t[1][0]))
        lines = sorted(reals, key=lambda t: t[0])
    real = [edge_junk(p, ln) for ln in real]
    xs = sorted(ln[0][1][0] for ln in real); xe = sorted(ln[-1][1][2] for ln in real)
    left, right = xs[len(xs) // 4], xe[max(-len(xe), -len(xe) // 4 - 1)]          # the text block
    out = []; headed = False                       # kort-oversigt: one running head a page (see HEADKEEP)
    for yc, ln in lines:
        ln = edge_junk(p, ln)
        ln = [t for t in ln if left - 25 <= (t[1][0] + t[1][2]) / 2 <= right + 25]   # margin marks, pencil
        if not ln: continue
        t = ' '.join(w for w, b in ln)
        folio = str(p) if isinstance(p, int) else p
        if re.sub(r'[\s.,]', '', t) == folio and (not out or yc > out[-1][0]):
            continue                                    # the folio, at the head or (on a chapter's first page) the foot
        if not out and re.fullmatch(r'\d+\s+\d+', t.strip()) and folio in t.split():
            continue                                    # spinozas-ethica: the running head is the two folios
        tw = t.split()                                  # etik: a folio read in two pieces ("5 3", "41 1"): join them
        if len(tw) > 2 and tw[-2].isdigit() and tw[-1].isdigit() and tw[-2] + tw[-1] == folio: tw = tw[:-2] + [folio]
        if len(tw) > 2 and tw[0].isdigit() and tw[1].isdigit() and tw[0] + tw[1] == folio: tw = [folio] + tw[2:]
        tj = ' '.join(tw)
        mh = re.fullmatch(r'[IVXL]{1,7}\.\s.*?\s(\d[\d ]{0,4}\d)', tj.strip())
        if not out and yc < 60 and mh and re.search('.*'.join(mh.group(1).replace(' ', '')), folio):
            continue                                    # etik: the running head, its folio read short ("57" for 575)
        if not out and len(tj.split()) > 1 and folio in (tj.split()[0], tj.split()[-1]) and yc < 60:
            continue                                    # etik: the running head, folio and chapter title (mixed case)
        if not out and yc < 60 and (re.search(C.HEAD, tj.strip()) and not re.search(r'[-¬]$', tj.strip()) or len(LETTER.findall(tj)) <= 2):   # kort: a head never ends in a hyphen (p. 2's first line, „Erkendelses Gyldighed ... Aandsvirk-“)
            if len(LETTER.findall(tj)) > 2:              # kort-oversigt (2026-10-17): only ONE running head a page; a first text
                if headed:                              # line that begins with a head word (Erkendelses..., John, Den nye ...)
                    print(f'  HEADKEEP p. {p}: {tj[:70]}', file=sys.stderr); out.append((yc, ln)); continue   # was dropped
                headed = True; print(f'  HEADSKIP p. {p}: {tj[:70]}', file=sys.stderr)
            continue                                    # religioese: the running head (folio + short title, the folio often garbled), or a speck above it
        caps = [c for c in t if c.isalpha()]
        if not out and folio in t.split() and caps and sum(c.isupper() for c in caps) > 0.8 * len(caps):
            continue                                    # the running head: chapter title and folio
        if re.fullmatch(r'[\dil]{1,2}\s?[*«»]?', t.strip()) and out and yc > out[-1][0] and t.strip() != folio:   # religioese: also „5«“, „ii*“
            continue                                    # a signature mark at the foot (not transcribed)
        out.append((yc, ln))
    # the series line at the foot of a sheet's first page: "D. K. D. Vidensk. Selsk. Skr., 7. Række, ... III. 3.  45"
    while out and re.search(r'Vidensk\W*Selsk', ' '.join(w for w, b in out[-1][1])): out.pop()
    # etik: the signature line at a sheet's foot ("H. Høffding: Etik." and the sheet number), and specks under it
    out = [o for k, o in enumerate(out) if not (k >= len(out) - 3 and re.search(r'H\S{0,2}\s*H\S{3,7}\W*Etik\b|^\W*H\S{3,9}\W*Kort\W*Oversigt\W.{0,15}$', ' '.join(w for w, b in o[1])))]
    while out and len(re.findall(r'[^\W_]', ' '.join(w for w, b in out[-1][1]))) <= 2 and not re.search(r'[¹²³⁴⁵⁶⁷⁸⁹]', ' '.join(w for w, b in out[-1][1])): out.pop()
    return out, lh, left, right

# ---------------- tokens into text ----------------
CLOSE = set('.,;:!?)]“') | {'*)', '**)', '***)'}
def jointoks(toks):
    s = ''
    for w in toks:
        if re.fullmatch(r'\d{1,2}\*', w): continue           # spinozas-ethica: a sheet number (43*), read into the last line
        w = w.replace('\\', '⟦BS⟧')                            # etik: a backslash in the layer is text (emit_line)
        w = w.replace('{', '\\{').replace('}', '\\}')         # a brace in the print (the schema, p. 29) is text
        # spinozas-ethica: the layer gives most note marks as superscript digits, ¹) ²): a plain digit; a superscript
        # without its parenthesis is an edition number (Historie², I): \textsuperscript
        # etik: NB's OCR marks superscripts (nb_scan.py lays them in as ¹ ² ³): a superscript digit is a note mark;
        # a plain „1)“ in the text is an enumeration (Hovedbud: 1) ... 2) ...), not a mark
        w = re.sub(r'([¹²³⁴⁵⁶⁷⁸⁹])\)?', lambda m: '⟦FN' + str('¹²³⁴⁵⁶⁷⁸⁹'.index(m.group(1)) + 1) + '⟧', w)
        if re.fullmatch(r'"[.,;:!?)]*', w): w = '“' + w[1:]       # the layer's straight quote, alone or with punctuation: closing
        if w in ('-', '--', '—'): w = '---'                 # the print's long dash (the layer gives a hyphen)
        w = re.sub(r'(?<![\w-])(\d+)-(\d+)', r'\1---\2', w)  # a range: 44-46 is printed 44—46; spinozas-ethica: also „(13-57)“
        w = re.sub(r'^([(\[]?)~+(?=\S)', r'\1„', w)                 # religioese: NB reads „ as ~ (kort-oversigt: « kept -- this print sets «...» too)
        if w in ('~', '~~'): w = '„'
        if w in (',,', '„'): w = '„'
        # the layer reads the closing quote “ as 11, 14, 41, 44, 1*, *1, **, 4*, 4', 1' after a word or a mark
        # oplevelse: not ** 1* *1 4* -- here they are the note marks **) and *) (etik's layer read “ so)
        w = re.sub(r"(?<=[^\W\d_.,;:!?])(11|14|41|44|4'|1')(?=[.,;:!?)]*$)", '“', w)
        w = re.sub(r"(?<=[.,;:!?])(11|14|41|44|4'|1')$", '“', w)
        w = re.sub(r'^([Ss])mign\.$', r'\1mlgn.', w); w = re.sub(r'^\(([Ss])mign\.$', r'(\1mlgn.', w)   # „Smlgn.“, read Smign.
        w = re.sub(r'^([Ss])mig\.$', r'\1mlg.', w); w = re.sub(r'^\(([Ss])mig\.$', r'(\1mlg.', w)
        if w in ('»', '«', '#', '%', '•', '__', '_', '✓', '■', "'", '’', '^', '/', '|'): continue   # specks the layer read as marks (the print uses „ “ only)
        if not s: s = w; continue
        if (w in CLOSE or re.fullmatch(r'[.,;:!?)\]“]+', w) or re.fullmatch(r'\*+\)?', w)) or s[-1] in '(„[': s += w
        else: s += ' ' + w
    s = re.sub(r'\s*(⟦FN\d⟧)(?:\s?\))?', r'\1', s)   # (2026-10-04: the space after the mark is kept)            # etik: the mark joins its word; its parenthesis is part of it
    s = re.sub(r'(?<=\S)"', '“', s)                       # a straight quote after a word or mark: closing
    s = re.sub(r'\s?\\textsuperscript\{([1-9])\}\s?\)', r'\1)', s)   # spinozas-ethica: a mark ¹ ) boxed in two parts
    s = re.sub(r'(^|(?<=\s))"(?=\w)', '„', s)                # before a word: opening
    return s
STAR = re.compile(r"([1-9]|\*{1,3}|['’xJlL!>sa?h])\)")    # 1) read as *) ') x) J) l) L) !) >)
def knum(g): return int(g) if g.isdigit() else 1
HOMO = str.maketrans('рсоаеехуНТВМКАОРСЕХт', 'pcoaeexyHTBMKAOPCEXt')   # Cyrillic look-alikes the OCR put in
GRLAT = str.maketrans('ΑΒΕΖΗΙΚΜΝΟΡΤΥΧı', 'ABEZHIKMNOPTYXi')
def emit_line(s):                                   # LaTeX specials the layer may carry
    if any(0x400 <= ord(ch) < 0x500 for ch in s): s = s.translate(HOMO)
    # spinozas-ethica: Greek capitals (and a dotless ı) inside a Latin word are look-alikes (SpinoΖΑ, KΕΡ-)
    s = re.sub(r'\S*[A-Za-z]\S*', lambda m: m.group(0).translate(GRLAT) if re.search('[Α-Ωı]', m.group(0)) else m.group(0), s)
    s = ''.join(ch for ch in s if not (0x0E80 <= ord(ch) < 0x0F00 or 0x0600 <= ord(ch) < 0x0700))   # Lao, Arabic marks: specks read as script
    # etik: specks and stray marks in NB's layer: a box (■), a superscript zero; ^ ~ and a backslash are text
    s = re.sub(r'[■□▪▫●⁰]', '', s)
    s = s.replace('^', '\\textasciicircum{}').replace('~', '\\textasciitilde{}')
    s = s.replace('&', '\\&').replace('%', '\\%').replace('#', '\\#').replace('_', '\\_').replace('$', '\\$')
    s = s.replace('⟦BS⟧', '\\textbackslash{}')
    s = s.replace('...', '\\dots{}')
    s = re.sub(r'(?<![A-Za-zæøå])lagttag', 'Iagttag', s)     # spinozas-ethica: I read as l (both OCRs; no word begins lagttag)
    return s

# ---------------- names in small capitals ----------------
# spinozas-ethica: names are set in small capitals (SPINOZA, DESCARTES); the layer gives them in capitals, now and
# then with a lowercase tail (SPINOza).  SCN: every word in capitals (3+ letters, not a roman numeral) in the layer.
SCN = set()
for _p in PAGES:
    for _w, _b in words(_p)[0]:
        _m = re.sub(r"['’][Ss]$", '', re.sub(r'[^\wÆØÅæøå’\']', '', _w))
        if len(_m) >= 3 and _m.isupper() and _m.isalpha() and not re.fullmatch(r'[IVXLCDM]+', _m): SCN.add(_m)
def smallcaps(s):
    """a word in capitals (3+ letters, not a roman numeral), or one the layer read in mixed case with 3+ capitals
    making up at least 40% of its letters (SPINOza, DuNIN, HoBBEs), is a name in small capitals: \\textsc{Name}; a
    possessive 's stays outside, in lowercase"""
    def sc(m):
        word, poss = m.group(1), m.group(2) or ''
        up = sum(c.isupper() for c in word)
        if re.fullmatch(r'[IVXLCDM]+', word) or up < 2 or (up < len(word) and (up < 3 or up < 0.4 * len(word))): return m.group(0)
        if up == 2 and len(word) > 2: return m.group(0)
        if up == len(word) and len(word) == 2 and word.upper() not in SCN: return m.group(0)
        return '\\textsc{' + word[0].upper() + word[1:].lower() + '}' + ("'s" if poss else '')
    return re.sub(r"(?<![\\\w])([A-ZÆØÅÉÖÜa-zæøåéöü]*[A-ZÆØÅÉÖÜ][A-ZÆØÅÉÖÜa-zæøåéöü]*)(['’][Ss])?(?![\w{])", sc, s)

# ---------------- one page: body lines, notes ----------------
JUNKMARK = re.compile(r"(?<=[A-Za-zæøåÆØÅöüé“”.,;!?])(?:\s?[-:'’*¹²³lJx]|\s!)\)(?=[\s.,;:“]|$)")
NOTEMARKS = {}                                      # etik: page -> [the text a lost mark follows, or 'prev'], read at the image
_nm = os.path.join(HERE, 'notemarks.tsv')
if os.path.exists(_nm):
    for _l in open(_nm, encoding='utf-8'):
        if _l[:1].isdigit(): _f = _l.rstrip('\n').split('\t'); NOTEMARKS.setdefault(int(_f[0]), []).append(_f[1])
DROPS = []                                          # etik: (page, text) for the marks of dropped notes
NOTETOPS = {}                                       # etik: where the notes begin, from NB's ALTO (nb_scan.py notes)
_nt = os.path.join(HERE, 'notetops.tsv')
if os.path.exists(_nt):
    for _l in open(_nt, encoding='utf-8'):
        if _l[:1].isdigit(): _f = _l.split('\t'); NOTETOPS[int(_f[0])] = float(_f[1])
def split_notes(p, lines, lh):
    k = C.pdfpage(p) if isinstance(p, int) else None
    if k in NOTETOPS:                                   # etik: the ALTO lines decide where the notes begin
        body = [l for l in lines if l[0] < NOTETOPS[k] - 0.5]
        if 0 < len(body) < len(lines): return body, lines[len(body):], False
    if NOTETOPS: return lines, [], False                # religioese: a page nb_scan.py notes did not list has no notes (verse in small type on pp. 132, 135)
    return _split_notes(p, lines, lh)
def _split_notes(p, lines, lh):
    """notes are set in smaller type: they begin at the first line from which the line pitch stays below 0.85 of the
    body's, provided that line starts with a star or stands under a gap; a single-line note needs both star and gap"""
    # den-store-humor: the notes are set smaller, and the layer's word boxes show it (x-height boxes ~20 against
    # ~24 in the text): the notes begin at the first line from which every line is small
    # etik: a line that begins with the note's number (NB's superscript, or "x )") under a gap begins the notes
    _ys = [yc for yc, ln in lines]; _d = [b - a for a, b in zip(_ys, _ys[1:])]
    if len(_d) >= 3:
        _pitch = statistics.median([x for x in _d if x > 0.6 * lh] or [2 * lh])
        for i in range(2, len(lines)):
            t0 = [w for w, b in lines[i][1]]
            st = t0[0][:1] in '¹²³⁴⁵⁶⁷⁸⁹' or (len(t0) > 1 and len(t0[0]) <= 2 and t0[1].startswith(')'))
            # etik: NB often reads the note's number as a mark-like token ("')", "■)", "l)") -- a line under the gap
            # that starts so begins the notes when the lines after it are set closer (the notes' smaller type)
            st2 = len(t0) > 1 and bool(re.fullmatch(r"\S{1,2}\)", t0[0])) and (i == len(lines) - 1 or statistics.median(_d[i:]) < 0.93 * _pitch)
            if (st or st2) and _d[i - 1] > 1.15 * _pitch: return lines[:i], lines[i:], False
    H = []
    for yc, ln in lines:
        hs = [b[3] - b[1] for w, b in ln if len(w) > 2 and w.isalpha()]
        H.append(statistics.median(hs) if hs else None)
    ref = statistics.median([h for h in H if h] or [0])
    for i in range(2, len(lines)):
        tail = [h for h in H[i:] if h]
        if H[i] and tail and all(h < 0.9 * ref for h in tail):
            return lines[:i], lines[i:], not STAR.match(lines[i][1][0][0])
    ys = [yc for yc, ln in lines]
    d = [b - a for a, b in zip(ys, ys[1:])]
    if len(d) < 4: return lines, [], False
    for i in range(3, len(lines)):
        before = statistics.median([x for x in d if x > 0.6 * lh] or [2 * lh])   # etik: the whole page (a heading above inflates the pitch)
        after = d[i:]; gap = d[i - 1]
        t0 = [w for w, b in lines[i][1]]
        star = bool(STAR.match(t0[0])) or t0[0][:1] in '¹²³⁴⁵⁶⁷⁸⁹' or (len(t0) > 1 and len(t0[0]) <= 2 and t0[1].startswith(')'))   # etik: NB's number, or "x )"
        small = bool(after) and statistics.median(after) < 0.85 * before
        if (star and (small or gap > 1.25 * before)) or (small and gap > 1.2 * before and len(after) >= 1):
            return lines[:i], lines[i:], not star
    return lines, [], False

def register(p):
    """the Register is printed in two columns: each column is clustered into lines on its own; a line at the
    column's left edge begins an entry, an indented line continues the one before"""
    ws, ph = words(p)
    ws = [t for t in ws if not JUNK.search(t[0])]
    xs = sorted((b[0] + b[2]) / 2 for w, b in ws); mid = (xs[0] + xs[-1]) / 2
    text = f'\n% --- p. {p} ---\n\\opage{{{p}}}'
    for col in ([t for t in ws if (t[1][0] + t[1][2]) / 2 < mid], [t for t in ws if (t[1][0] + t[1][2]) / 2 >= mid]):
        lines, lh = cluster(col)
        lines = [(yc, ln) for yc, ln in lines if sum(len(LETTER.findall(w)) for w, b in ln) >= 2 or re.search(r'\d', ' '.join(w for w, b in ln))]
        if not lines: continue
        left = sorted(ln[0][1][0] for yc, ln in lines)[len(lines) // 4]
        ents = []
        for yc, ln in lines:
            t = emit_line(jointoks([w for w, b in ln]))
            if re.fullmatch(r'\s*(\d+|R\s?E\s?G\s?I\s?S\s?T\s?E\s?R)\s*', t): 
                if 'R' in t: text += '\\begin{center}REGISTER\\end{center}\n'
                continue
            if ents and ln[0][1][0] - left > 4: ents[-1] += ' ' + t
            else: ents.append(t)
        ents = [re.sub(r'([A-Za-zæøå])- (?=[a-zæøå])', r'\1', e) for e in ents]
        for e in ents:                                  # a new initial: a new group, its letter in bold, as printed
            m = re.match(r'(Fru |)([A-ZÆØÅ])', e)
            if m and m.group(2) != (register.last or ''):
                if register.last: text += '\\par\\smallskip\n'
                e = e[:m.start(2)] + '\\textbf{' + m.group(2) + '}' + e[m.end(2):] if not m.group(1) else e
                register.last = m.group(2)
            text += '\\entry ' + e + '\n'
    return text

register.last = None

def build():
    out = []; prev_open = None; stats = dict(par=0, head=0, notes=0, placed=0)
    carry_note = None
    for p in PAGES:
        r = page_lines(p)
        if not r[0]: out.append((p, f'\n% --- p. {p} --- (no text in the layer)\n' + flag(p, 'page has no layer text'))); continue
        lines, lh, left, right = r
        # spinozas-ethica: Google's word boxes are tight round the letters (median height ~5.5 pt at a line pitch of
        # ~13): measure indents and centring against the type size, taken as 0.75 of the line pitch
        _ys = [yc for yc, ln in lines]; _d = sorted(b - a for a, b in zip(_ys, _ys[1:]) if b > a)
        if _d: lh = max(lh, 0.75 * _d[len(_d) // 2])
        body, notes, unmarked = split_notes(p, lines, lh)
        # --- notes: text per star-count
        nt = []
        # den-store-humor: a note's first line is indented (its number stands in the indent), its other lines are
        # flush: indentation, not the misread number, decides where a note begins; the number is then dropped
        nl = sorted(ln[0][1][0] for yc, ln in notes); nleft = nl[0] if nl else 0
        # etik: the notes stand flush with the text; measure the indent against the text's left edge (the bottom
        # lines), so that a page whose only note line(s) are flush is seen to carry on a note from the page before
        bx = sorted(ln[0][1][0] for yc, ln in body[-8:])
        if len(bx) >= 4: nleft = min(nleft, bx[len(bx) // 4])
        for yc, ln in notes:                            # oplevelse: HANGING indent -- a note's first line is flush with the
            toks = [w for w, b in ln]                   # text (its label *) **) hangs at the left), its other lines are indented
            if not toks: continue
            if len(re.findall(r'[A-Za-zÀ-ÿ]', ' '.join(toks))) <= 1: continue   # religioese: the printed rule above the notes, read as „I“ or „[“
            if ln[0][1][0] - nleft <= 5:            # religioese: a note's FIRST line is indented ~10 pt (its label in the indent), the rest flush
                if nt: nt[-1][1] += toks
                else: nt.append([0, toks])              # an indented first line: a note running over from the page before
                continue
            if len(toks) > 1 and re.fullmatch(r'[1-9lIi]', toks[0]) and toks[1].startswith(')'): toks = [toks[0] + ')'] + ([toks[1][1:]] if toks[1][1:] else []) + toks[2:]   # religioese: „1 )“
            if toks and re.fullmatch(r'[¹²³⁴⁵⁶⁷⁸⁹]\)?', toks[0]): toks = [')'] + toks[1:]   # religioese: NB's superscript label
            m_ = re.match(r"([^\w\s(]{0,5}\)|[1-9lIi]\))(.*)$", toks[0])   # the label: 1) 2) (NB: l) i) *) ') for 1)); religioese: numbered per page
            if m_ and len(toks[0]) <= 6 or (m_ and m_.group(1).count('*')):
                toks = ([m_.group(2)] if m_.group(2) else []) + toks[1:]
                k_ = sum(1 for x in nt if x[0]) + 1   # religioese: the print numbers 1) 2) per page; NB's labels are unreliable
            else:
                k_ = sum(1 for x in nt if x[0]) + 1     # no label read: the next in order
            nt.append([k_, toks])
        if False:
          for yc, ln in notes:
            toks = [w for w, b in ln]
            if toks and toks[0] == ')' and nt: toks = toks[1:]
            if len(toks) > 1 and re.fullmatch(r"[1-9*'’xJlL!>]", toks[0]) and toks[1].startswith(')'): toks = [toks[0] + ')'] + ([toks[1][1:]] if toks[1][1:] else []) + toks[2:]
            m = STAR.fullmatch(toks[0]) if toks else None
            if m and not unmarked: nt.append([knum(m.group(1)), toks[1:]])
            elif nt: nt[-1][1] += toks
            else: nt.append([0, toks])
        nt = [x for x in nt if re.search(r'[A-Za-zÀ-ÿ0-9]', ' '.join(x[1]))]      # a rule line read as dashes
        # two notes the layer set on one run of lines: split at „ N) “ where N is the next number
        nt2 = []
        for k, toks in nt:
            cur = []
            for w in toks:
                if k and cur and re.fullmatch(r'[2-9]\)', w) and int(w[0]) == (nt2[-1][0] if nt2 and nt2[-1][0] else k) + 1 and re.search(r'[.)]$', cur[-1]):
                    nt2.append([k, cur]); k = int(w[0]); cur = []; continue
                cur.append(w)
            nt2.append([k, cur])
        nt = nt2
        notes_txt = []
        for k, toks in nt:
            t = jointoks(toks); t = re.sub(r'(\w)- (\w)', lambda m: m.group(1) + m.group(2) if m.group(2).islower() else m.group(0), t)
            t = re.sub(r'([A-ZÆØÅÖÜ][A-Za-zÆØÅÖÜæøåöü]*[A-ZÆØÅÖÜ])- ([A-ZÆØÅÖÜ][A-ZÆØÅÖÜa-zæøåöü]*[A-ZÆØÅÖÜ])', r'\1\2', t)   # spinozas-ethica: a name in capitals divided at a line end in a note
            t = re.sub(r'\s+\d{1,2}\s?\*\s*$', '', t)
            if k: t = re.sub(r'^[^\w\s(]{0,4}\)\s?', '', t)   # oplevelse: a label left on the note (the line's first token was not it)          # spinozas-ethica: the sheet number (44*) at the foot, read into the last note
            notes_txt.append([k, re.sub(r'⟦FN(\d)⟧', r'\\textsuperscript{\1}', smallcaps(emit_line(t)))])   # etik: a superscript in a note is an edition number (Historie²)
        # --- body: lines, indents, headings, hyphen joins
        head = f'% --- p. {p} ---\n\\setcounter{{footnote}}{{0}}%\n'   # no blank line before it: a page turn is not a paragraph break
        page_out = []; errata = False
        X0 = [ln[0][1][0] for yc, ln in body]; X1 = [ln[-1][1][2] for yc, ln in body]
        for i, (yc, ln) in enumerate(body):
            toks = [w for w, b in ln]
            x0, x1 = ln[0][1][0], ln[-1][1][2]
            # the scan is rotated a little, so the margins drift down the page: measure the indent against the
            # nearby lines (second-smallest left edge, second-largest right edge within four lines)
            nb = range(max(0, i - 4), min(len(body), i + 5))
            lo_ = sorted(X0[j] for j in nb); hi_ = sorted((X1[j] for j in nb), reverse=True)
            ll = lo_[1] if len(lo_) > 2 else lo_[0]; rr = hi_[1] if len(hi_) > 2 else hi_[0]
            centred = x0 - ll > 2.5 * lh and rr - x1 > 2.5 * lh
            indent = 0.5 * lh < x0 - ll <= 4 * lh and not centred    # spinozas-ethica: the indent is ~2.6 type sizes
            kind = 'head' if centred else ('par' if indent else 'line')
            page_out.append([kind, toks])
        text = ''; depth = 0
        for i, (kind, toks) in enumerate(page_out):
            if kind == 'par' and i > 0 and page_out[i - 1][1] and re.search(r'[a-zæøå]-$', page_out[i - 1][1][-1]):
                kind = 'line'                           # religioese: a line after a divided word does not begin a paragraph
            s = jointoks(toks)
            if kind in ('par', 'head'): depth = 0
            # spinozas-ethica: "N)" that closes an open parenthesis is a citation, „(Eth. I, Def. 6)“, not a note mark
            def cite(m, d0=depth):                   # (a mark glued to a word is a mark: „(som KEPLER³) selv ...)“)
                pre = m.string[:m.start()]; return not (pre[-1:].isalpha() and not m.group(0)[:1].isspace()) and d0 + pre.count('(') - pre.count(')') > 0
            # a note mark: a digit glued to the word or mark before it; *) ') etc. also after a space
            ABBR = re.compile(r'(?:^|\s|\()(?:cap|Cap|Kap|Chap|ch|p|P|S|Sc|N|Nr|No|Bd|Vol|vol|Bog|Aft|§)\.?\s?$')
            def fmark(m):
                if m.group(1) and ABBR.search(m.string[:m.start()] + ('' if m.group(0)[0] == ' ' else '')): return m.group(0)   # „cap. 6)“: a citation
                if cite(m): return m.group(0)
                return '⟦FN' + str(knum(m.group(1) or m.group(2).strip())) + '⟧'
            if PLAIN_MARKS:                          # etik: off (marks come as superscripts, see jointoks)
                s = re.sub(r"(?:(?<=[^\W\d_])|(?<=[.;:!?“]))(?:\s?([1-9])|(\s?[*']|x|\s[xJlL]))\)(?=\s|$|[.,;:])", fmark, s)   # not !) ’) l): „Kopier!)“, „(emotions’)“, „Schlegel)“ are text
                s = re.sub(r"(?<=\))\s?([1-9]|x)\)(?=\s|$|[.,;:])", lambda m: '⟦FN' + (m.group(1) if m.group(1).isdigit() else '1') + '⟧', s)
                s = re.sub(r"(?<=[.“])\*\s([1-9])\)(?=\s|$)", lambda m: '⟦FN' + m.group(1) + '⟧', s)        # „Livsførelsen.* 2)“   # after a closing parenthesis: „(… 1824) 1).“
                s = re.sub(r"(?<=,)\s?([*'x])\)(?=\s|$)", lambda m: '⟦FN1⟧', s)
                s = re.sub(r"(?<=[,)])([1-9])\)(?=\s|$|[.,;:])", lambda m: m.group(0) if cite(m) else '⟦FN' + m.group(1) + '⟧', s)   # glued after a comma or a parenthesis     # after a comma: not a digit ("VIII, 1)" cites a section)
            # oplevelse: the note marks are stars, *) **) ***) glued to the word or mark before them (NB: also •*) for *))
            s = re.sub(r"\s?[•■]?(\*{1,4})\)", lambda m: '⟦FN' + str(len(m.group(1))) + '⟧', s)
            depth = max(0, depth + s.count('(') - s.count(')'))
            s = emit_line(s)
            if i == 0 and prev_open is not None:          # a word broken over the page turn
                text += prev_open + '%\n' + head + f'\\opage{{{p}}}' + s.lstrip(); prev_open = None
                if kind == 'par': text = text.replace('%\n' + head, '%\n' + head + flag(p, 'indent after a broken word?'))
                continue
            if i == 0:
                lead = '\n' if kind not in ('par', 'head') else '\n\n'
                text += lead + head + (flag(p, 'centred line: heading or verse') + '\\begin{center}' + s + '\\end{center}\n' if kind == 'head' else f'\\opage{{{p}}}' + s)
                if kind == 'head': text = text.replace('\\begin{center}', f'\\opage{{{p}}}\\begin{{center}}', 1); stats['head'] += 1
                if kind == 'par': stats['par'] += 1
                continue
            if kind == 'head': text += '\n\n' + flag(p, 'centred line: heading or verse') + '\\begin{center}' + s + '\\end{center}\n'; stats['head'] += 1; continue
            if kind == 'par' or (i > 0 and page_out[i - 1][0] == 'head'): text += '\n\n' + s; stats['par'] += 1; continue
            if kind == 'entry': text += '\n\\par\\noindent\\hangindent=1.5em ' + s; continue
            if kind == 'verse': text += '\\\\\n' + s if not text.rstrip().endswith('\\end{center}') else '\n' + s; continue
            text += '\n' + s
        # hyphen joins at line ends (inside the page), and an open hyphen at the page end (etik: also when the next line
        # starts with a space: a tilted line, or a note line read into the body)
        def join(m):
            a, b = m.group(1), m.group(2)
            return a + '-' + b if b[:1].isupper() else a + b
        text = re.sub(r'([A-ZÆØÅ]{2,})-\n(?!%)([A-ZÆØÅ]{2,}\S*)', r'\1\2\n', text)   # a name in capitals divided at a line end
        text = re.sub(r'([A-Za-zÀ-ÖØ-öø-ÿ])-\n(?!%)(og|eller) ', r'\1- \2\n', text)   # spinozas-ethica: „Tids- og Kvantitetsforskelligheder“: the hyphen stays
        text = re.sub(r'([A-Za-zÀ-ÖØ-öø-ÿ])-\n(?!%) *(\\par\\noindent\\hangindent=1\.5em )?([^\s]+)', lambda m: (m.group(1) + '-' + m.group(3) if m.group(3)[:1].isupper() else m.group(1) + m.group(3)) + '\n', text)
        text = re.sub(r'\n +', '\n', text)
        text = re.sub(r'\s\d{1,2}\s?\*(?=\s*$)', '', text)           # spinozas-ethica: the sheet number at the foot of a note-less page
        text = '\n'.join(l if l.lstrip().startswith('%') else smallcaps(l) for l in text.split('\n'))   # not in the CHECK comments
        # spinozas-ethica: a name in small capitals divided at a line end, whose first part the layer read in mixed
        # case: „Des-\\textsc{Cartes}“, „Ga-\\textsc{Lilei}“, „\\textsc{Spi}-Noza“ -> one name
        text = re.sub(r'(?<![\\\w])([A-ZÆØÅ][A-Za-zæøå]{1,3})-\\textsc\{([A-ZÆØÅ][a-zæøå]+)\}', lambda m: '\\textsc{' + m.group(1)[0] + (m.group(1)[1:] + m.group(2)).lower() + '}', text)
        text = re.sub(r'\\textsc\{([A-ZÆØÅ][a-zæøå]{1,3})\}-([A-Za-zæøå]+)', lambda m: '\\textsc{' + m.group(1) + m.group(2).lower() + '}' if (m.group(1) + m.group(2)).upper() in SCN else m.group(0), text)
        mo = re.search(r'([A-Za-zÀ-ÖØ-öø-ÿ]+)-\s*$', text)
        if mo and p != PAGES[-1]:
            prev_open = mo.group(1); text = text[:mo.start()]
        # notes into their marks
        orphans = [int(m) for m in re.findall(r'⟦FN(\d)⟧', text)]
        for n in notes_txt:                            # a note whose star the layer lost: the first mark with no note
            if not n[0]:
                free = [k for k in orphans if k not in [m[0] for m in notes_txt]]
                if free: n[0] = free[0]; n.append('star lost in the layer: paired with the mark by order')
        # den-store-humor: the notes are numbered 1), 2) ... per page in the order of their marks, and the layer's
        # numbers are unreliable (1) read as *) ') x) h) a) ...): when the marks and the numbered notes are equally
        # many, pair them in order.  The layer also repeats a note's number at the end of the last text line: one
        # surplus mark there is dropped.
        nn = [n for n in notes_txt if n[0]]
        # etik: notes read at the image (notemarks.tsv): a note that runs on from the page before ('prev'), and the
        # words after which a mark the layer lost stands; then, if marks are still missing, NB's junk for a
        # superscript glued to its word („-)“, „:)“, „ ')“, „*)“, „l)“), when there is exactly one such per missing mark
        # and it does not close a parenthesis
        for a_ in NOTEMARKS.get(p, []):
            if a_ == 'prev' and nn and out and '\\footnote[' in out[-1][1]: nn[0][0] = 0; nn = nn[1:]; continue
            if a_.startswith('setnote:'):               # a note the layer garbled, typed from the image (its pieces go)
                k_, t_ = a_[8:].split(':', 1); k_ = int(k_)
                notes_txt[:] = [n_ for n_ in notes_txt if n_[0] not in (0, k_)] + [[k_, t_]]
                nn[:] = [n_ for n_ in notes_txt if n_[0]]; nn.sort(key=lambda n_: n_[0]); continue
            if a_.startswith('dropnote:'):              # a piece the layer took for a note: drop it, its „mark“ back to REPL
                k_, r_ = a_[9:].split(':', 1); k_ = int(k_)
                notes_txt[:] = [n_ for n_ in notes_txt if n_[0] != k_]; nn[:] = [n_ for n_ in nn if n_[0] != k_]
                DROPS.append((p, r_)); continue
            if a_.startswith('note:'):                  # a note the layer did not read at all, typed from the image
                n_ = [len(nn) + 1, a_[5:]]; notes_txt.append(n_); nn.append(n_); continue
            if a_.startswith('sup:'):                   # an edition number („Vernunft¹“) the layer took for a mark
                m_ = re.search(re.escape(a_[4:]) + r'⟦FN(\d)⟧', text)
                if m_: text = text[:m_.start()] + a_[4:] + '\\textsuperscript{' + m_.group(1) + '}' + text[m_.end():]
                continue
            if a_ == 'frac':                            # a fraction („²/₅“) the layer took for a mark
                text = re.sub(r'⟦FN(\d)⟧/(\d)', r'\\textsuperscript{\1}/\\textsubscript{\2}', text); continue
            pre_, junk_, aft_ = (a_.split('|') + ['', ''])[:3]   # WORDS|JUNK|AFTER: the mark stands after WORDS; JUNK
            if pre_ + junk_ in text:                    # (the layer's reading of it) goes, AFTER (a stop it lost) comes in
                i_ = text.index(pre_ + junk_) + len(pre_); text = text[:i_] + '⟦FN0⟧' + aft_ + text[i_ + len(junk_):]
            else: FLAGS.append((p, 'notemarks.tsv: words not found: ' + a_))
        nmk = len(re.findall(r'⟦FN\d⟧', text))
        if len(nn) > nmk:
            cands = []
            for m_ in JUNKMARK.finditer(text):
                par = re.sub(r'⟦FN\d⟧', '', text[:m_.start()]).rsplit('\n\n', 1)[-1]
                if par.count('(') <= par.count(')'): cands.append(m_)
            if len(cands) == len(nn) - nmk:
                for m_ in reversed(cands): text = text[:m_.start()] + '⟦FN0⟧' + text[m_.end():]
                FLAGS.append((p, 'note marks read from the layer\'s junk'))
        mk = list(re.finditer(r'⟦FN\d⟧', text))
        if len(mk) == len(nn) + 1 and nn and '\n' not in text[mk[-1].end():].strip():
            text = text[:mk[-1].start()] + text[mk[-1].end():]; mk = mk[:-1]; FLAGS.append((p, 'note number at the foot of the text dropped'))
        if mk and len(mk) == len(nn):
            for i, (m_, n) in enumerate(reversed(list(zip(mk, nn)))):
                j = len(mk) - i
                text = text[:m_.start()] + f'\\footnote[{j}]{{{n[1]}}}' + text[m_.end():]
            if [n[0] for n in nn] != list(range(1, len(nn) + 1)) or [int(m_.group(0)[3]) for m_ in mk] != list(range(1, len(mk) + 1)):
                text = text.replace('\\setcounter{footnote}{0}%\n', '\\setcounter{footnote}{0}%\n' + flag(p, 'notes paired with the marks in order (the layer misread a number)'), 1)
            notes_txt = [n for n in notes_txt if not n[0]]
            stats['placed'] += len(nn); stats['notes'] += len(nn)
        for n in notes_txt:                            # a note whose number the layer misread: the first mark with no note
            if n[0] and f'⟦FN{n[0]}⟧' not in text and len(n) == 2:
                free = [k for k in orphans if k not in [m[0] for m in notes_txt]]
                if free: n[0] = free[0]; n.append('note number misread in the layer: paired with the mark by order')
        for n in notes_txt:
            k, t = n[0], n[1]
            mark = f'⟦FN{k}⟧'
            if len(n) > 2 and mark in text:
                text = text.replace(mark, f'\\footnote[{k}]{{{t}}}' + '%\n' + flag(p, n[2]).rstrip('\n') + '\n', 1); stats['placed'] += 1
            elif k and mark in text:
                text = text.replace(mark, f'\\footnote[{k}]{{{t}}}', 1); stats['placed'] += 1
            elif not k and out and '\\footnote[' in out[-1][1]:      # the rest of the last note of the page before
                pt = out[-1][1]; i0 = pt.rindex('\\footnote['); i1 = pt.index('{', i0); d = 0
                for j in range(i1, len(pt)):
                    d += {'{': 1, '}': -1}.get(pt[j], 0)
                    if d == 0: break
                pt = pt[:j] + ' ' + t + pt[j:]
                out[-1] = (out[-1][0], pt); FLAGS.append((p, 'note run over from the page before, joined'))
            else:
                text += '\n' + flag(p, 'note ' + ('without a star: runs over from the page before?' if not k else 'whose mark was not found')) + f'\\footnote[{k or 1}]{{{t}}}'
            stats['notes'] += 1
        # the layer often repeats a note's number at the end of the last text line above the notes: an unused mark
        # there, whose note exists on the page, is that number, not a reference
        lastnl = text.rstrip().rfind('\n')
        for mark in set(re.findall(r'⟦FN\d⟧', text[lastnl:])):
            if int(mark[3]) in [n[0] for n in notes_txt]: text = text[:lastnl] + text[lastnl:].replace(mark, ''); FLAGS.append((p, 'note number at the foot of the text dropped'))
        for mark in set(re.findall(r'⟦FN\d⟧', text)):
            text = text.replace(mark, '\\textsuperscript{' + mark[3] + '}') + '\n' + flag(p, 'superscript, no note: an edition number?')   # religioese: Etik⁵, Religionsfilosofi³
        out.append((p, text))
    return out, stats

pages, stats = build()
# a blank line (paragraph break) after a line that does not end a sentence, before a line that opens with a dash or
# a lowercase letter, is the indent rule misled (a line opening with a dash sits indented): not a paragraph
def _join(t):
    L = t.split('\n'); out = []; k = 0
    while k < len(L):
        if L[k].strip() == '' and out:
            j = k
            while j < len(L) and L[j].strip() == '': j += 1
            prev = next((x for x in reversed(out) if x.strip() and not x.lstrip().startswith('%') and not x.startswith('\\setcounter')), '')
            nxt = next((x for x in L[j:] if x.strip() and not x.lstrip().startswith('%') and not x.startswith('\\setcounter')), '')
            nxt = re.sub(r'^\\opage\{\w+\}', '', nxt)
            if re.search(r'[A-Za-zÀ-ÖØ-öø-ÿ,;]$', prev.rstrip()) and not prev.rstrip().endswith('\\end{center}') \
                    and (nxt.startswith('---') or re.match(r'[a-zæøå]', nxt)):
                k = j; continue
        out.append(L[k]); k += 1
    return '\n'.join(out)
front = ''.join(t for p, t in pages if p in ROMAN); body = ''.join(t for p, t in pages if p not in ROMAN)
front, body = _join(front), _join(body)
# centred lines: a chapter heading ("I. HUMOR SOM TOTALFØLELSE", read at the image) loses its CHECK; two or more
# centred lines in a row that are not headings are verse, set as a quote with \\ between the lines
CB = r'% CHECK p\. \d+: centred line: heading or verse\n(\\opage\{\d+\})?\\begin\{center\}(.*?)\\end\{center\}\n\n\n'
def _verse(m):
    ls = re.findall(CB, m.group(0))
    if len(ls) < 2 or any(re.match(r'[IVX]+\. ', t) or t.isupper() for op, t in ls): return m.group(0)
    return (ls[0][0] or '') + '\\begin{quote}\n' + '\\\\\n'.join(t for op, t in ls) + '\n\\end{quote}\n\n'
body = re.sub('(?:' + CB + ')+', _verse, body)
body = re.sub(r'% CHECK p\. \d+: centred line: heading or verse\n((\\opage\{\d+\})?\\begin\{center\}[IVX]+\. )', r'\1', body)                    # over the whole text: a break can fall at a page turn
print(f"pages {len(PAGES)} | paragraphs {stats['par']} | headings {stats['head']} | notes {stats['notes']} (placed at their marks {stats['placed']})")
print(f"CHECK flags: {len(FLAGS)}")
for p, w in FLAGS[:60]: print(f'  p. {p}: {w}')
# etik: the headings, from the Indhold (pp. I-VII; read in the layer, to be checked at the images): the three parts,
# the groups of the Social Etik (A.-C., 1.-3., and A.-C. inside "2. Den ideelle Kultur"), and the chapters I-XLI.
# (page where the heading stands, command, text as printed)
HEADS = [   # kort-oversigt: from the Indhold (PDF 7) and the ALTO of each page; every one checked at the image (structure pass)
    (1, 'introhead', 'INDLEDNING.'),
    (5, 'chapterhead', 'I.|DEN NYERE FILOSOFIS TILBLIVEN.'),
    (5, 'sectionhead', '1. Opdagelsen af det naturlige Menneske.'),
    (10, 'sectionhead', '2. Det nye Verdensbillede.'),
    (14, 'sectionhead', '3. Den nye Videnskab.'),
    (17, 'chapterhead', 'II.|SYSTEMDANNELSER.'),
    (35, 'chapterhead', 'III.|ERFARINGSFILOSOFIEN.'),
    (43, 'chapterhead', 'IV.|OPLYSNINGSFILOSOFIEN.'),
    (50, 'chapterhead', 'V.|IMMANUEL KANT OG DEN KRITISKE FILOSOFI.'),
    (63, 'chapterhead', 'VI.|ROMANTIKENS FILOSOFI.'),
    (74, 'chapterhead', 'VII.|POSITIVISMEN.'),
    (82, 'sectionhead', 'a. Det psykologiske Problem.'),
    (85, 'sectionhead', 'b. Tilværelsesproblemet.'),
    (88, 'sectionhead', 'c. Erkendelsesproblemet.'),
    (92, 'sectionhead', 'd. Vurderingsproblemet.'),
]
def _notes(x):                                      # the \\footnote[k]{...} in x, braces balanced
    out, i = [], 0
    while True:
        i = x.find('\\footnote[', i)
        if i < 0: return out
        j = x.index('{', i); d = 0
        for k in range(j, len(x)):
            d += {'{': 1, '}': -1}.get(x[k], 0)
            if d == 0: break
        out.append(x[i:k + 1]); i = k + 1
def _norm(x):
    for n in _notes(x): x = x.replace(n, '')
    x = re.sub(r'\\textsc\{([^{}]*)\}', lambda m: m.group(1).upper(), x)
    x = re.sub(r'\\(?:textit|emph)\{([^{}]*)\}', r'\1', x)   # oplevelse: keep the words of an italic heading
    x = re.sub(r'\\[a-z]+\*?(\{[^{}]*\})?', ' ', x)
    x = ' '.join(w for w in x.upper().split() if not re.fullmatch(r'[IVXL1]+\.?|\d+\.?|[A-D]\.?', w))
    return re.sub(r'[^A-ZÆØÅ]', '', x)
def layout(t, P):
    """etik, after patches.PATCHES: the headings (HEADS above).  On a heading's page, the run of one to four
    lines (centred lines, quote lines or plain short lines, as the draft set them) whose letters match the
    heading's best (ratio >= 0.6, the roman numeral and the label ignored) is replaced by the heading; a heading
    not found is reported.  Centred lines still flagged afterwards are left for the image."""
    import difflib
    t = re.sub(r'(?<=\d)–(?=\d)', '---', t)             # the layer's en dash in a range: the print's —
    t = re.sub(r'(?<=\d) ?--- ?(?=\d)', '---', t)       # NB boxes the dash of a range apart: 43 --- 48 is printed 43—48
    for p, cmd, text in HEADS:
        m0 = re.search(r'%% --- p\. %d ---\n' % p, t)
        if not m0: print('  HEADING: page not found', p, text); continue
        m1 = re.search(r'\n% --- p\. \d+ ---\n', t[m0.end():]); end = m0.end() + (m1.start() if m1 else len(t) - m0.end())
        L = t[m0.end():end].split('\n'); want = _norm(text.split('|')[-1])
        best = (0, None, None)
        for i in range(len(L)):
            for j in range(i + 1, min(len(L), i + 6) + 1):
                seg = [l for l in L[i:j] if not l.lstrip().startswith('%')]
                if not seg or not _norm(seg[0]) or not _norm(seg[-1]): continue
                got = _norm(' '.join(seg))
                if len(got) > 2 * len(want) + 6: break
                r = difflib.SequenceMatcher(None, got, want).ratio()
                if r > best[0]: best = (r, i, j)
        r, i, j = best
        if r < 0.6: print('  HEADING NOT FOUND: p. %d %s (best %.2f)' % (p, text, r)); continue
        while i > 0 and (not L[i - 1].strip() or L[i - 1].lstrip().startswith('%') or re.fullmatch(r'(\\opage\{\d+\})?\\begin\{center\}[IVXL1]+\.?\\end\{center\}', L[i - 1].strip())):
            if not re.search(r'center', L[i - 1]) and not L[i - 1].lstrip().startswith('% CHECK') and L[i - 1].strip(): break
            i -= 1                                       # the roman numeral, centred on its own line above the title
        seg = '\n'.join(L[i:j])
        op = ''.join(re.findall(r'\\opage\{\d+\}', seg))
        parts = text.split('|'); parts[-1] += ''.join(_notes(seg))   # a note on the heading stays on it
        args = '{' + '}{'.join(parts) + '}'
        L[i:j] = ['', op + '\\' + cmd + args, '']
        t = t[:m0.end()] + '\n'.join(L) + t[end:]
    # oplevelse: a quote environment the draft set round a chapter's heading lines holds nothing else: unwrap it
    t = re.sub(r'\\begin\{quote\}\s*((?:\\(?:chapterhead|sectionhead|essayhead|essaysource)\{.*?\n\s*)+?)\\end\{quote\}',
               lambda m: m.group(1).strip() + '\n' if all(l.startswith(('\\chapterhead', '\\sectionhead', '\\essayhead', '\\essaysource')) for l in m.group(1).strip().split('\n') if l.strip()) else m.group(0), t, flags=re.S)
    # oplevelse: a centred line that is only a roman numeral (I. II. ... in the essays; NB reads 11. 111. i.) is a section numeral
    t = re.sub(r'% CHECK p\. \d+: centred line: heading or verse\n((?:\\opage\{\d+\})?)\\begin\{center\}([IVXl1i]{1,4})\.?\\end\{center\}',
               lambda m: m.group(1) + '\\romanhead{' + m.group(2).replace('1', 'I').replace('l', 'I').replace('i', 'I') + '}\n% CHECK roman numeral read', t)
    t = re.sub(r'\n{3,}', '\n\n', t)
    return t

if '--emit' in sys.argv:
    tpl = open(os.path.join(HERE, 'template.tex'), encoding='utf-8').read()
    new = tpl.replace('%%FRONT%%', front.strip('\n')).replace('%%BODY%%', body.strip('\n'))
    if '--raw' not in sys.argv:                         # corrections read at the image that a word decision cannot express
        import importlib.util
        spec = importlib.util.spec_from_file_location('patches', os.path.join(HERE, 'patches.py'))
        P = importlib.util.module_from_spec(spec); spec.loader.exec_module(P); bad = []
        for kind, find, repl, why in P.PATCHES:
            n = new.count(find) if kind == 's' else len(re.findall(find, new, re.S))
            if n != 1: bad.append((n, find[:70], why)); continue
            new = new.replace(find, repl) if kind == 's' else re.sub(find, repl, new, count=1, flags=re.S)
        print(f'patches: {len(P.PATCHES) - len(bad)} applied')
        for b_ in bad: print('  PATCH NOT APPLIED (%d matches): %r -- %s' % b_)
        if bad: sys.exit('fix patches.py: every patch must match exactly once')
    if '--raw' not in sys.argv: new = layout(new, P)
    if os.path.exists(TEX):
        old = open(TEX, encoding='utf-8').read()
        if 'GENERATED; DO NOT EDIT BY HAND' not in old and '--force' not in sys.argv:
            sys.exit('transcription.tex does not say it is generated (edited by hand?): not overwritten; --force to override')
        b = TEX + f'.bak.{datetime.date.today():%Y%m%d}-draft'
        if not os.path.exists(b): shutil.copy2(TEX, b)
    os.makedirs(BOOK, exist_ok=True); open(TEX, 'w', encoding='utf-8').write(new); print('wrote', TEX)
