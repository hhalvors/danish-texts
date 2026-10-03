#!/usr/bin/env python3
"""ebook-method/collate/xcheck.py -- check a translation against the Danish it should render, when the
Danish it was actually MADE FROM is a different text: an older state of transcription.tex (a git commit),
or a modern e-book (.epub).  Every place where that source differs from the current transcription of the
print is a place where the English may follow the wrong Danish.  Self-contained (python3 + git).

    python3 ebook-method/collate/xcheck.py BOOK --measure [--from SRC]
            count the differences between SRC and the current transcription, by class (below)
    python3 ebook-method/collate/xcheck.py BOOK --review [--from SRC] [--classes wording,markup,punct] [--width 300]
            write .parts/xcheck/BOOK/review.txt: for each difference, the Danish context [source => print]
            and the English around the same point of the same printed page (between the \\opage markers)
    python3 ebook-method/collate/xcheck.py BOOK --apply FIXES.txt [--write]
            FIXES.txt: lines "old English|new English" (# comments allowed).  Each old string must occur
            exactly once in translation.tex (whitespace and line breaks are matched loosely); without
            --write nothing is changed.  --write keeps a backup translation.tex.bak.YYYYMMDD-xcheck
    python3 ebook-method/collate/xcheck.py --all --measure
            measure every book listed in ebook-method/collate/xcheck-sources.tsv

SRC is a git commit (the state of transcription.tex at that commit), a path to an .epub, or a path to a
.tex file (relative paths are taken from the repo root, so ../bibliotek/... is the library beside it).  Without --from, the book's row in xcheck-sources.tsv is used.

Classes.  Words are compared after normalising case, aa/å, é/e and x/ks, so the e-books' spelling and
their lower-case nouns never count.  Then:
    spelling  the letters differ only in those respects, or a word is split or joined
    modern    the e-book's modern verb forms: opstaa/opstaar, ere/er, kunde/kunne, have/har ...
    punct     punctuation only
    markup    italics only (\\emph in the transcription, <i>/<em> in the e-book)
    wording   everything else -- these are the ones to read.  "small" = one word for one word, at most
              two letters apart (kun/kan; often an e-book OCR slip, but sometimes the meaning)
Footnotes are compared as a separate stream (e-book endnotes against the transcription's footnotes).
"""
import re, os, sys, json, html, zipfile, difflib, subprocess, shutil, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, '.parts', 'xcheck')
EM_ON, EM_OFF, PG = '\x03', '\x04', '\x01'

def book_dir(name):
    for a in sorted(os.listdir(os.path.join(ROOT, 'texts'))):
        d = os.path.join(ROOT, 'texts', a, name)
        if os.path.isdir(d): return d
    sys.exit(f'no texts/*/{name}')

# ---------------------------------------------------------------- reading TeX
def cut_notes(s, keep):
    """remove \\footnote{...}; keep gets (position-in-output, contents)"""
    out = []; i = 0; n = 0
    pat = re.compile(r'\\footnote(?![A-Za-z])')
    while True:
        m = pat.search(s, i)
        if not m: out.append(s[i:]); return ''.join(out)
        out.append(s[i:m.start()]); n += len(s[i:m.start()]); k = m.end()
        if s[k:k + 1] == '[': k = s.index(']', k) + 1
        while s[k] in ' \n': k += 1
        if s[k] != '{': out.append('\\footnote'); i = m.end(); continue
        d = 0; a = k
        while True:
            c = s[k]
            if c == '\\': k += 2; continue
            d += {'{': 1, '}': -1}.get(c, 0); k += 1
            if d == 0: break
        keep.append((n, s[a + 1:k - 1])); out.append(' '); n += 1; i = k

def mark_emph(s):
    """\\emph{...}, \\textit{...}, \\textsl{...} -> EM_ON ... EM_OFF (nested braces respected)"""
    out = []; i = 0; pat = re.compile(r'\\(emph|textit|textsl)\{')
    while True:
        m = pat.search(s, i)
        if not m: out.append(s[i:]); return ''.join(out)
        j = m.start(); out.append(s[i:j]); k = m.end(); d = 1; a = k
        while d and k < len(s):
            c = s[k]
            if c == '\\': k += 2; continue
            d += {'{': 1, '}': -1}.get(c, 0); k += 1
        out.append(EM_ON + mark_emph(s[a:k - 1]) + EM_OFF); i = k

def tex_plain(s):
    s = re.sub(r'\\[oa]page\{(\d+)\}', lambda m: f'{PG}{m.group(1)}{PG}', s)
    for a, b in (('guillemotright', '»'), ('guillemotleft', '«'), ('textquotedblleft', '“'), ('textquotedblright', '”'),
                 ('quotedblbase', '„'), ('textendash', '–'), ('textemdash', '—')):
        s = re.sub(r'\\' + a + r'(\{\}|(?![A-Za-z])\s?)', b, s)
    s = mark_emph(s)
    s = re.sub(r'\\begin\{(tabular|array|longtable)\*?\}(\{[^}]*\})?\{(?:[^{}]|\{[^{}]*\})*\}', ' ', s)   # with its column spec
    s = re.sub(r'\\multicolumn\{[^}]*\}\{[^}]*\}', '', s).replace('&', ' ')
    s = re.sub(r'\\(begin|end)\{[^}]*\}|\\\\(\[[^]]*\])?', ' ', s)
    s = re.sub(r'\\(label|addcontentsline|markboth|markright|thispagestyle|pagestyle|vspace|hspace|rule|setcounter|'
               r'addtocounter|marginnote|phantomsection|clearpage|newpage|cleardoublepage|tableofcontents)\*?(\[[^]]*\])?(\{[^}]*\})*', ' ', s)
    s = re.sub(r'\\(textsc|textbf|textup|textrm|mbox|spaced|so|dk|textsuperscript)\{', '', s)
    s = s.replace('\\-', '').replace('\\,', ' ').replace('\\ ', ' ').replace('~', ' ')
    s = re.sub(r'\\([%&$#_])', r'\1', s)
    s = re.sub(r'\\[A-Za-z]+\*?(\[[^]]*\])?', ' ', s)
    s = s.replace('{', '').replace('}', '').replace('\\', ' ')
    s = s.replace('``', '“').replace("''", '”').replace('---', '—').replace('--', '–')
    return s

def read_tex(src):
    a = src.find('\\begin{document}'); b = src.find('\\end{document}')
    body = src[a if a >= 0 else 0: b if b >= 0 else len(src)]
    body = re.sub(r'(?<!\\)%[^\n]*\n[ \t]*', '', body)
    notes = []; body = cut_notes(body, notes)
    return tex_plain(body), [(pos, tex_plain(t)) for pos, t in notes], body

# ---------------------------------------------------------------- reading an e-book
def read_epub(path):
    z = zipfile.ZipFile(path); names = z.namelist()
    opf = [n for n in names if n.endswith('.opf')][0]; o = z.read(opf).decode('utf-8')
    base = os.path.dirname(opf)
    man = dict(re.findall(r'<item [^>]*?id="([^"]+)"[^>]*?href="([^"]+)"', o))
    man.update({i: h for h, i in re.findall(r'<item [^>]*?href="([^"]+)"[^>]*?id="([^"]+)"', o)})
    body, notes = [], []
    for idref in re.findall(r'<itemref [^>]*?idref="([^"]+)"', o):
        h = man.get(idref, '')
        if not h or re.search(r'cover|TitlePage|Copyright|AboutThisBook|TOC|toc', h): continue
        s = z.read(os.path.join(base, h).replace('\\', '/')).decode('utf-8')
        s = s[s.find('<body'):]
        s = re.sub(r'<span class="ref-note[^"]*"[^>]*>.*?</span>|<a [^>]*epub:type="noteref"[^>]*>.*?</a>', ' ', s, flags=re.S)
        isnotes = 'Notes' in h or 'rearnote' in s[:5000]
        s = re.sub(r'<(i|em)\b[^>]*>', EM_ON, s); s = re.sub(r'</(i|em)>', EM_OFF, s)
        if isnotes:
            for m in re.finditer(r'<(p|li|aside|div)\b[^>]*(rearnote|footnote|endnote|note)[^>]*>(.*?)</\1>', s, re.S):
                t = re.sub(r'<[^>]+>', ' ', m.group(3)); t = html.unescape(t)
                t = re.sub(r'^\s*\d+\s*[.)]?\s*', '', t)
                notes.append((0, t))
            if notes: continue
        s = re.sub(r'<[^>]+>', ' ', s); body.append(html.unescape(s))
    return ' '.join(body), notes

# ---------------------------------------------------------------- tokens
def tokens(text, page=None):
    """[(raw, emph, page)] ; page markers PG N PG set the page of the following tokens"""
    out = []; em = False
    text = re.sub(PG + r'(\d+)' + PG, lambda m: f' {PG}{m.group(1)} ', text)
    for t in text.split():
        if t.startswith(PG): page = int(t[1:]); continue
        it = False                                   # italic if any letter of it is inside the italics
        for c in t:
            if c == EM_ON: em = True
            elif c == EM_OFF: em = False
            elif em and c.isalnum(): it = True
        raw = t.replace(EM_ON, '').replace(EM_OFF, '')
        if raw: out.append((raw, it, page))
    return out

LET = re.compile(r'[^A-Za-zÀ-ÖØ-öø-ÿ]')
def norm(w):
    w = LET.sub('', w).lower().replace('aa', 'å').replace('é', 'e').replace('è', 'e').replace('x', 'ks')
    return w
def key(raw):
    n = norm(raw)
    return n if n else re.sub(r'[“”„"«»‟]', '"', re.sub(r'[’‘`´]', "'", raw))
def psig(raw):
    s = re.sub(r'[A-Za-zÀ-ÖØ-öø-ÿ0-9]', '', raw)
    return re.sub(r'[“”„"«»‟]', '"', re.sub(r'[’‘`´]', "'", s)).replace('—', '-').replace('–', '-')

MODERN = {('ere', 'er'), ('have', 'har'), ('kunne', 'kan'), ('ville', 'vil'), ('skulle', 'skal'), ('vide', 'ved'),
          ('turde', 'tør'), ('burde', 'bør'), ('gøre', 'gør'), ('kunde', 'kunne'), ('vilde', 'ville'),
          ('skulde', 'skulle'), ('maatte', 'måtte'), ('saae', 'så'), ('gaae', 'gå'), ('staae', 'stå')}
def modern_eq(a, b):
    a, b = norm(a), norm(b)
    if a == b: return True
    if (a, b) in MODERN or (b, a) in MODERN: return True
    for x, y in ((a, b), (b, a)):
        if len(x) >= 3 and y == x + 'r': return True       # opstaa/opstaar, begynde/begynder
    return False
def dist(a, b):
    return 0 if a == b else (len(a) + len(b) - 2 * sum(m.size for m in difflib.SequenceMatcher(None, a, b).get_matching_blocks())) // 1

def compare(A, B):
    """A: source tokens, B: print tokens -> list of changes"""
    ka, kb = [key(t[0]) for t in A], [key(t[0]) for t in B]
    sm = difflib.SequenceMatcher(None, ka, kb, autojunk=False)
    ch = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            for i, j in zip(range(i1, i2), range(j1, j2)):
                ra, rb = A[i][0], B[j][0]
                if A[i][1] != B[j][1]: ch.append(('markup', i, i + 1, j, j + 1))
                elif psig(ra) != psig(rb): ch.append(('punct', i, i + 1, j, j + 1))
                elif LET.sub('', ra) != LET.sub('', rb): ch.append(('spelling', i, i + 1, j, j + 1))
            continue
        oa, ob = [t[0] for t in A[i1:i2]], [t[0] for t in B[j1:j2]]
        if ''.join(map(norm, oa)) == ''.join(map(norm, ob)):
            c = 'spelling' if ''.join(map(norm, oa)) else 'punct'
        elif len(oa) == len(ob) and all(modern_eq(x, y) for x, y in zip(oa, ob)): c = 'modern'
        else:
            c = 'wording'
            if len(oa) == 1 and len(ob) == 1 and dist(norm(oa[0]), norm(ob[0])) <= 2: c = 'wording-small'
        ch.append((c, i1, i2, j1, j2))
    return ch

# ---------------------------------------------------------------- sources
def git(*a):
    r = subprocess.run(['git', '--no-optional-locks', *a], cwd=ROOT, capture_output=True, text=True)
    return r.stdout
def load_source(src, book):
    p = os.path.join(ROOT, os.path.expanduser(src))           # relative paths are relative to the repo
    if src.endswith('.epub'):
        return read_epub(p)
    if src.endswith('.tex') and os.path.exists(p):
        b, n, _ = read_tex(open(p, encoding='utf-8').read()); return b, n
    rel = os.path.relpath(os.path.join(book_dir(book), 'transcription.tex'), ROOT)
    t = git('show', f'{src}:{rel}')
    if not t: sys.exit(f'{book}: no transcription.tex at {src}')
    b, n, _ = read_tex(t); return b, n
def sources_table():
    rows = {}
    p = os.path.join(HERE, 'xcheck-sources.tsv')
    for l in open(p, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        f = l.rstrip('\n').split('\t'); rows[f[0]] = f
    return rows

def page_of_notes(notes_with_pos, body_text):
    """give each print footnote the page in force at its anchor"""
    out = []
    marks = [(m.start(), int(m.group(1))) for m in re.finditer(PG + r'(\d+)' + PG, body_text)]
    for pos, t in notes_with_pos:
        pg = None
        for s, p in marks:
            if s <= pos: pg = p
            else: break
        out.append((pg, t))
    return out

def run(book, src, write_review=False, classes=('wording', 'wording-small'), width=300):
    bd = book_dir(book)
    tb, tn, _ = read_tex(open(os.path.join(bd, 'transcription.tex'), encoding='utf-8').read())
    sb, sn = load_source(src, book)
    res = {}
    streams = [('body', tokens(sb), tokens(tb))]
    A, B = [], []
    for _, t in sn: A += tokens(t)
    for pg, t in page_of_notes(tn, tb): B += tokens(t, pg)
    if A and not B:                      # the print sets its notes as a section at the end (endnotes):
        streams[0][1].extend(A); A = []  # compare the e-book's notes there, as part of the text
    streams.append(('notes', A, B))
    allch = []
    for name, A, B in streams:
        ch = compare(A, B); allch += [(name, c, A, B) for c in ch]
        cnt = {}
        for c in ch: cnt[c[0]] = cnt.get(c[0], 0) + 1
        res[name] = dict(src_words=len(A), print_words=len(B), **cnt)
    if write_review: review(book, bd, allch, classes, width)
    return res

def en_pages(en):
    return [(int(m.group(1)), m.start()) for m in re.finditer(r'\\opage\{(\d+)\}', en)]
def review(book, bd, allch, classes, width):
    en = open(os.path.join(bd, 'translation.tex'), encoding='utf-8').read()
    ep = en_pages(en); epd = dict(ep)
    os.makedirs(os.path.join(OUT, book), exist_ok=True)
    out = []; k = 0
    for name, (c, i1, i2, j1, j2), A, B in allch:
        if c not in classes: continue
        k += 1
        old = ' '.join(t[0] for t in A[i1:i2]); new = ' '.join(t[0] for t in B[j1:j2])
        pre = ' '.join(t[0] for t in B[max(0, j1 - 10):j1]); post = ' '.join(t[0] for t in B[j2:j2 + 10])
        pg = B[min(j1, len(B) - 1)][2] if B else None
        win = ''
        if name == 'body' and pg in epd:
            same = [j for j in range(len(B)) if B[j][2] == pg]
            f = (j1 - same[0]) / max(1, len(same)) if same else 0
            s = epd[pg]; e = min([x for p, x in ep if x > s] or [len(en)])
            c0 = int(s + f * (e - s)); win = en[max(s, c0 - width): min(e + 60, c0 + width)]
        elif name == 'notes' and pg in epd:
            s = epd[pg]; e = min([x for p, x in ep if x > s] or [len(en)])
            seg = en[s:e]; keep = []; cut_notes(seg, keep)
            win = ' || '.join(t for _, t in keep)[: 2 * width] or seg[:width]
        elif not epd:
            f = j1 / max(1, len(B)); c0 = int(f * len(en)); win = en[max(0, c0 - 2 * width): c0 + 2 * width]
        win = re.sub(r'\s+', ' ', win)
        out.append(f'#{k} {name} p.{pg} [{c}]\nDA: …{pre} [{old} => {new}] {post}…\nEN: {win}\n')
    p = os.path.join(OUT, book, 'review.txt'); open(p, 'w', encoding='utf-8').write('\n'.join(out))
    print(f'{k} entries -> {os.path.relpath(p, ROOT)}')

def apply(book, fixes, write):
    bd = book_dir(book); f = os.path.join(bd, 'translation.tex'); t = open(f, encoding='utf-8').read()
    bad = n = 0
    for line in open(fixes, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip() or line.lstrip().startswith('#'): continue
        old, new = line.split('|', 1)
        rx = r'\s+'.join(re.escape(w) for w in old.split())
        ms = list(re.finditer(rx, t))
        if len(ms) != 1: print(f'{len(ms)} matches :: {old}'); bad += 1; continue
        m = ms[0]; t = t[:m.start()] + new + t[m.end():]; n += 1
    print(f'{n} ok, {bad} not exactly once')
    if write and not bad:
        b = f + '.bak.' + datetime.date.today().strftime('%Y%m%d') + '-xcheck'
        if not os.path.exists(b): shutil.copy2(f, b)
        open(f, 'w', encoding='utf-8').write(t); print('written; backup', os.path.basename(b))
    elif write: print('nothing written')

def fmt(book, src, r):
    b, n = r['body'], r['notes']
    w = lambda d: d.get('wording', 0) + d.get('wording-small', 0)
    return (f"{book:34s} {src[:40]:40s} words {b['print_words']:6d}  WORDING {w(b):5d} (small {b.get('wording-small',0):4d})"
            f"  markup {b.get('markup',0):4d}  punct {b.get('punct',0):4d}  modern {b.get('modern',0):4d}"
            f"  | notes {n['src_words']}/{n['print_words']} words, wording {w(n):4d}")

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    if '--all' in a:
        for book, row in sources_table().items():
            src = row[1]
            if src == '-': print(f'{book:34s} {row[2] if len(row) > 2 else ""}'); continue
            try: print(fmt(book, src, run(book, src)), flush=True)
            except SystemExit as e: print(f'{book:34s} ERROR {e}')
        sys.exit()
    book = a[0]
    if '--apply' in a: apply(book, opt('--apply'), '--write' in a); sys.exit()
    src = opt('--from') or sources_table().get(book, [None, None])[1]
    if not src or src == '-': sys.exit(f'{book}: no source; give --from')
    cl = tuple(opt('--classes', 'wording,wording-small').split(','))
    if 'wording' in cl and 'wording-small' not in cl: cl += ('wording-small',)
    r = run(book, src, '--review' in a, cl, int(opt('--width', 300)))
    print(fmt(book, src, r)); print(json.dumps(r))
