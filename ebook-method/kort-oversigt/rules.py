#!/usr/bin/env python3
"""ebook-method/den-store-humor/rules.py -- settle by rule the open checks that are the WITNESS's known faults
(tesseract) or the LAYER's known omissions, and write them to decisions.tsv with the rule's name in the note, so
every one can be found and undone.  Nothing is decided that could hide a reading of the print: letter differences
are left for the image, except accents the witness adds to a word attested elsewhere in the corpus.

    python3 ebook-method/collate/check.py den-store-humor      # writes .parts/collate/checks.tsv (open checks)
    python3 ebook-method/den-store-humor/rules.py               # dry run: counts per rule, examples
    python3 ebook-method/den-store-humor/rules.py --write       # append the decisions (backup first)
    python3 ebook-method/collate/check.py den-store-humor --apply

The rules (e = the draft's reading, w = tesseract's):
  mark      w adds a footnote mark (*) read as +) %) *) or a bare *): the notes are placed by draft.py      -> T
  quote     w reads „ as a comma and “ as % or 4, otherwise the same                                       -> T
  (a quote mark only e has is NOT settled by rule: see the comment in rule())
  dash+     w has a long dash e lacks (Google's layer drops them; tesseract's are all dash-shaped, ~40x5 px)  -> =---
  (a dash only e has is NOT settled by rule: see the comment in rule())
  hyphen    e "X --- Y" where w reads one word "X-Y": the layer boxed a hyphen apart                         -> =X-Y
  speck     w adds a point inside or before a word, a doubled point, a lone > or <                          -> T
  accent    w adds an accent or ring to a plain letter (Åstronomien); e's word is attested in the corpus and w's is not                   -> T
"""
import os, re, sys, glob, shutil, datetime, unicodedata, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
BOOK = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt')   # erindringer: copied 2026-10-07 from den-store-humor + etik's e-book vote
CHK = os.path.join(BOOK, '.parts', 'collate', 'checks.tsv'); DECF = os.path.join(HERE, 'decisions.tsv')
# oplevelse (2026-10-14): CALIBRATION.  KORT_CAL=/tmp/kortcal/conf scores every rule against a text already decided at the
# image: Etik (NB ALTO draft, tesseract witness, the SAGA e-book as the vote), pp. 1-150, rebuilt in /tmp by a copy of
# etik's draft.py (calibrate.sh); the truth is etik's decisions.tsv lines marked "image".  Nothing is written.
CAL = os.environ.get('KORT_CAL')
if CAL:
    BOOK = CAL; CHK = os.path.join(CAL, '.parts', 'collate', 'checks.tsv'); DECF = os.path.join(CAL, 'no-decisions.tsv')
L = 'A-Za-zÀ-ÖØ-öø-ÿ0-9'; letters = lambda s: re.sub('[^' + L + ']', '', s)
def strip_acc(s): return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
def qnorm(s): return re.sub('"+', '"', re.sub('[«»„“”"‚‘’\'`´]', '"', s).replace(' ', ''))   # den-store-humor: runs of quote marks count as one
MARK = re.compile(r"[+%*x×?'’!1-9\"“”]{1,3}\)|(?<![A-Za-z])\*{1,3}(?!\w)")   # oplevelse: tesseract reads **) as "") ”) %%) +%) too   # den-store-humor: notes 1), 2) read as ?) ') 1) etc.
VOC = set()
for f in glob.glob(os.path.join(ROOT, 'texts', '*', '*', 'transcription.tex')):
    if os.path.abspath(os.path.dirname(f)) == os.path.abspath(BOOK): continue      # never this book's own text
    if CAL and f.endswith(os.path.join('hoeffding', 'etik', 'transcription.tex')): continue   # nor, calibrating, etik's
    VOC.update(w.lower() for w in re.findall('[' + L + ']+', re.sub(r'\\[A-Za-z]+', ' ', open(f, encoding='utf-8', errors='replace').read())))
att = lambda x: x.lower() in VOC
def rule(e, w):
    w0 = re.sub(r'#\d+$', '', w)
    # oplevelse: the same words too (qnorm ignores spaces: „pludSmlgn.“ for „plud-“ + a note's „Smlgn.“ passed, 2026-10-14)
    if MARK.search(w0) and qnorm(MARK.sub('', w0)) == qnorm(e) and len(MARK.sub('', w0).split()) == len(e.split()): return 'mark', 'T'
    if e == '' and re.fullmatch(r"[?'’*!1-9]{1,2}\)", w0): return 'mark', 'T'
    # moderne-filosoffer: the e-book's vote comes BEFORE the generic rules (seam/numbers settled word divisions blind:
    # "densOpgave>dens Opgave" went T); a dash only the witness has is the e-book's to decide, else the image's
    v = ebook_vote(e, w0)
    if v: return 'ebook', v
    if e == '' and w0 and not letters(w0):                # marks only the witness has: the e-book has them, or nothing there
        mid = ebook_mid()
        if mid is None: return None, None
        m2 = re.sub(r'[\s.,;:!?»«"„“()]', '', mid)            # the context's own marks are in mid: what is left is the gap's
        if m2 == '': return 'ebook-mark', 'T'
        if re.fullmatch(r'[—–-]+', m2) and re.fullmatch(r'[—–\s-]+', w0): return 'ebook-dash', '=' + ' '.join(['---'] * len(re.findall(r'[—–]|-+', m2)))
        return None, None
    # the Noter's labels (pp. 148-157): the e-book has the bare number; with the sequence 1-46 it settles a misread label
    if re.fullmatch(r'\d{1,2}\)', e) and re.fullmatch(r"\S{0,3}\)", w0):
        mid = ebook_mid()
        if mid is not None and re.fullmatch(r'\d{1,2}', mid.strip()):
            return ('ebook-label', 'T') if mid.strip() + ')' == e else ('ebook-label', '=' + mid.strip() + ')')
    # the ø rule (Hans, 2026-10-08): the draft (Google's layer) has o where tesseract has ø, the o-form is no Danish word
    # (oefix.py's reviewed list, or the e-book has the ø-form here): the print has ø
    if e and len(e) == len(w0) and e != w0 and all(x == y or (x, y) in (('o', 'ø'), ('O', 'Ø')) for x, y in zip(e, w0)):
        mid = ebook_mid()
        if (mid is not None and mid.strip() == w0.strip()) or re.sub(r'\W', '', e) in OEM: return 'oe', 'W'
    if e and letters(e) == letters(w0):                   # the same letters: a word division, a quote's place, a mark
        mid = ebook_mid()
        if mid is not None:
            ms_, es_, ws_ = re.sub(r'\s+', ' ', mid).strip(), e.strip(), w0.strip()
            if ms_ == es_ != ws_: return 'ebook-sp', 'T'
            if ms_ == ws_ != es_: return 'ebook-sp', 'W'
            # an endnote mark (the draft's \textsuperscript{N}) read otherwise by tesseract: the e-book has the number
            # oplevelse: OFF -- footnotes with star marks here; it settled „1909).I.“ (a lost space at a note's seam) as T
            mk = re.search(r'(\d{1,2})\)', es_)
            if False and mk and re.sub(r'\s', '', ms_).find(mk.group(1) + ')') >= 0 and letters(re.sub(r'\d', '', es_)) == letters(re.sub(r'\d', '', ws_)): return 'ebook-mark', 'T'
    wq = re.sub(r'(^|\s|\()(,,?)\s?(?=[^\W\d_])', r'\1„', w0)                  # „ read as a comma, glued or apart
    wq = re.sub(r'(?<=[^\W\d_])[%4](?=[.,;:!?)]*$)', '“', wq)                    # “ read as % or 4 after a word
    wq = re.sub(r'(?<=[.,;:!?])[%4](?=[)]*$)', '“', wq)
    if wq != w0 and qnorm(wq) == qnorm(e): return 'quote', 'T'
    # NOT a rule: e has a quote mark w lacks.  Tried and withdrawn (2026-10-03): quotations crossing pages leave
    # paragraphs unbalanced, so balance could not vouch for the layer's mark.  These go to the image.
    if False and e == '' and w0 == '—': return 'dash+', '=---'   # moderne-filosoffer: off (the e-book decides, above)
    # NOT a rule: e has a dash w lacks.  The layer's free-standing "-" may be a speck or a hyphen boxed apart
    # (p. V "vor Tids - Forsken"), and tesseract finds real dashes reliably: these go to the image.
    m = re.fullmatch(r'([^\W\d_]+) — ([^\W\d_]+)', e)
    if m and w0 == m.group(1) + '-' + m.group(2): return 'hyphen', '=' + w0
    if letters(e) == letters(w0) and e and (re.search(r'[a-zæøå]\.[a-zæøå]', w0) or '..' in w0 or re.match(r'\.\w', w0)
            or re.search(r'\w\. \w', w0) and not re.search(r'\w\. \w', e)) and qnorm(re.sub(r'\.', '', w0)) == qnorm(re.sub(r'\.', '', e)):
        return None, None   # den-store-humor: the speck rule hid layer faults ("betingesde"): to the image
    if e == '' and w0 in ('>', '<'): return 'speck', 'T'
    if e and w0 and len(e) == len(w0) and e != w0 and len(e.split()) == 1 \
            and all(x == y or (strip_acc(y) == x and x.isascii()) for x, y in zip(e, w0)):   # w only ADDS accents
        if att(letters(e)) and not att(letters(w0)): return 'accent', 'T'
    # den-store-humor (tesseract's faults on this face, each checked on a crop sheet before it became a rule):
    if re.sub('§', '', e) == re.sub(r'[$S4]', '', w0, count=1) and '§' in e and re.search(r'[$S4]', w0) and len(e) <= 6: return 'para', 'T'   # § read as $ S 4
    if e and w0 and e != w0 and e.lower() == w0.lower() and e[0].islower() and w0[0].isupper() and e[1:] == w0[1:] and att(e) and False: return 'case', 'T'   # erindringer: off (never settle case by rule)
    if False and e.startswith('I') and w0.startswith('l') and e[1:] == w0[1:]: return 'I/l', 'T'   # erindringer: off (Iode/lode)
    # moderne-filosoffer: OFF -- it settled digit disagreements blind (1845>1843, the layer's 99) for 22)); no footnotes here
    # a seam in the note stream: the same words, w with a note mark (') ") ?) 1)) between them
    strip_ = lambda x: re.sub(r"[\s'\"”’?!*)(1-9]", '', x)
    if False and e and len(e.split()) == len(w0.split()) and not re.search(r"(?<!\d)[*'’xJlL!>1-9]\)", e) and letters(e) and re.sub(r'\d', '', letters(e)) == re.sub(r'\d', '', letters(re.sub(r"[?'\"”’!*1-9]\)", '', w0))) and strip_(e) == strip_(re.sub(r"[?'\"”’!*1-9]\)", '', w0)): return 'seam', 'T'
    # den-store-humor, after the notes were rebuilt: the witness keeps the notes' numbers (1) ?) ”) ') 2?) ...)
    # and the sheet signature „Den store Humor“ in the stream; with those taken out, the same letters
    wn = re.sub(r"(?:(?<=\s)|^)[^\s\w]{0,2}[0-9]?[^\s\w]{0,2}\)+(?=\s|$)", ' ', w0)
    wn = re.sub(r'Den store Humor', ' ', wn)
    en = re.sub(r'\$[<=]\$', '', e)
    if (e or wn.strip()) and len(en.split()) == len(wn.split()) and letters(en) == letters(wn) and (wn != w0 or en != e) and re.sub(r'[\w\s]', '', en) == re.sub(r'[\w\s)]', '', wn): return 'numbers', 'T'   # erindringer: the marks must agree
    if e == '' and not letters(wn): return 'numbers', 'T'
    # the witness reads the running head (or the black band at the top of the scan) into the first line
    m = re.match(r'(.*?)(\S+)$', w0)
    if e and ' ' not in e and m and m.group(2) == e and re.search(r'HARALD|HØFFDING|HUMOR|[A-ZÆØÅ]{4,}', m.group(1)): return 'headjunk', 'T'
    if e == '' and len(w0) >= 12 and len(re.findall(r'[a-zæøå]{4,}', w0)) <= 1: return 'noise', 'T'
    # erindringer: the e-book (Lindhardt og Ringhof 2021, the 1928 text) as a THIRD reading, as in etik: the same
    # spot found by the words around the check (unique in the e-book); its reading agrees with exactly one of the two.
    # Edition check 2026-10-07 against the 41 pages read at the image on 23 Sep: ~4 e-book faults in 13,000 words.
    return None, None
import zipfile, html as _html
OEM = set()                                              # oefix.py's reviewed o-forms that are no Danish words
try:
    _src = open(os.path.join(ROOT, 'oefix.py'), encoding='utf-8').read(); _m = re.search(r'pairs=\"{3}(.*?)\"{3}', _src, re.S)
    OEM = {p_.split()[0] for p_ in _m.group(1).replace('\n', '').split('|') if p_.strip()}
except Exception: pass
EB = ''
_EP = os.path.join(BOOK, 'Kort_oversigt_over_den_nyere_filosofis_historie.epub')            # privately owned, gitignored
if CAL: _EP = os.path.join(os.path.expanduser('~'), 'mnt', 'bibliotek', 'Høffding, Harald', 'etik.epub')
if os.path.exists(_EP):
    _z = zipfile.ZipFile(_EP)
    _names = sorted(n for n in _z.namelist() if n.endswith(('.xhtml', '.html')) and 'About' not in n and 'Copyright' not in n)   # moderne-filosoffer: the Noter are collated too
    EB = _html.unescape(re.sub(r'<[^>]+>', ' ', ' '.join(_z.read(n).decode('utf-8', 'replace') for n in _names))).replace('­', '')
_FT = str.maketrans({'å': 'a', 'ø': 'o', 'æ': 'e', 'ü': 'u', 'é': 'e', 'l': 'i', 'ö': 'o', 'ä': 'a'})
def _fold(x): return ''.join(c if c.isalnum() else ' ' for c in x.lower().translate(_FT))   # one char for one: indices stay
EBF = _fold(EB)
CTX = NEXT = ''
def ebook_mid():
    """moderne-filosoffer: the e-book's text between the check's context words (None if the context is not unique)"""
    if not EB: return None
    P = [x for x in _fold(CTX[:CTX.rfind('[')]).split() if x]; X = [x for x in _fold(NEXT).split() if x]; ms = []
    for k in (3, 2, 4):
        if len(P) < k or len(X) < k: continue
        pat = r'\b' + r'\W+'.join(map(re.escape, P[-k:])) + r'(\W.{0,80}?\W|\W+)' + r'\W*'.join(map(re.escape, X[:k])) + r'\b'
        ms = list(re.finditer(pat, EBF))
        if len(ms) == 1: break
    if len(ms) != 1: return None
    mid = re.sub(r'\s+', ' ', EB[ms[0].start(1):ms[0].end(1)]).replace('’', "'")   # the e-book's apostrophe is ’
    # the gap begins with the marks that close the context's last word and ends with those that open the next one: those
    # are the context's, not the check's (they made every mark comparison fail: ". Wundt" against "Wundt")
    pw = (CTX[:CTX.rfind('[')].split() or [''])[-1]; nw = (NEXT.split() or [''])[0]
    tail = re.search(r'[^\w\s]*$', pw).group(0); head = re.match(r'[^\w\s]*', nw).group(0)
    m_ = mid.lstrip()
    if tail and m_.startswith(tail): mid = ' ' + m_[len(tail):]
    m_ = mid.rstrip()
    if head and m_.endswith(head): mid = m_[:len(m_) - len(head)] + ' '
    return mid
def ebook_vote(e, w0):
    """the e-book's reading at the check's place: 'T' or 'W' when it agrees with exactly one of them (from etik)"""
    mid = ebook_mid()
    if mid is None: return None
    mid = mid.strip()
    Lt = lambda x: re.sub(r'\W', '', x)
    Q = lambda x: re.sub(r'\s', '', re.sub(r'[»«„“”"]|,,', '"', x)).replace('-—', '—').replace('—-', '—').replace('---', '—')
    le, lw, lm = Lt(e), Lt(w0), Lt(mid)
    if le != lw:
        pm = lambda x: re.sub(r'[\w\s]', '', Q(x))           # the marks must agree too
        if (lm == le != lw or lm.lower() == le.lower() != lw.lower()) and pm(mid) == pm(e): return 'T'
        if (lm == lw != le or lm.lower() == lw.lower() != le.lower()) and pm(mid) == pm(w0): return 'W'
        return None
    if len(e.split()) != len(w0.split()): return None    # a word split or joined: to the image
    qm, qe, qw = Q(mid), Q(e), Q(w0)
    if qe == qw: return None
    if qm.endswith(qe) and not qm.endswith(qw) and len(qm) - len(qe) <= 1: return 'T'
    if qm.endswith(qw) and not qm.endswith(qe) and len(qm) - len(qw) <= 1: return 'W'
    return None
done = set()
if os.path.exists(DECF):
    done = {l.split('\t')[0] for l in open(DECF, encoding='utf-8') if '\t' in l and not l.startswith('#')}
out = []; count = collections.Counter(); ex = collections.defaultdict(list)
for ln in open(CHK, encoding='utf-8'):
    parts = ln.rstrip('\n').split('\t'); cid, key, ctx = parts[:3]; NEXT = parts[3] if len(parts) > 3 else ''; CTX = ctx
    if key in done: continue
    e, w = key.split('|', 1)[1].split('>', 1)
    name, d = rule(e, w)
    if not name: continue
    out.append(f'{key}\t{d}\trule:{name}'); count[name] += 1; ex[name].append(key)
if CAL:                                                   # score against etik's image decisions
    TRUTH = {l.split('\t')[0]: l.split('\t')[1] for l in open(os.path.join(ROOT, 'ebook-method', 'etik', 'decisions.tsv'), encoding='utf-8') if '\timage' in l}
    sc = collections.defaultdict(lambda: [0, 0, []]); seen = 0
    for o in out:
        k_, d_, r_ = o.split('\t'); r_ = r_[5:]
        if k_ not in TRUTH: continue
        e_, w_ = k_.split('|', 1)[1].split('>', 1); w_ = re.sub(r'#\d+$', '', w_)
        rd = lambda d: e_ if d in ('T', 'SC') else (w_ if d in ('W', 'P') else (d[1:] if d.startswith('=') else None))
        qn = lambda x: None if x is None else re.sub(r'[«»„“”"]|,,', '"', x).replace('---', '—')
        ok = qn(rd(d_)) == qn(rd(TRUTH[k_]))      # the same READING (etik's SC = right words, small capitals)
        sc[r_][0 if ok else 1] += 1
        if not ok: sc[r_][2].append(f'{k_} rule {d_} image {TRUTH[k_]}')
    nimg = sum(1 for l in open(CHK, encoding='utf-8') if l.split('\t')[1] in TRUTH)
    print(f'CALIBRATION on {CAL}: {nimg} checks decided at the image; the rules settle {sum(a + b for a, b, c in sc.values())} of them')
    for r_, (a, b, w_) in sorted(sc.items()): print(f'  {r_:10s} right {a:4d}  wrong {b:3d}  ' + ' | '.join(w_[:6]))
    sys.exit(0)
for k, n in count.most_common(): print(f'{n:4d} {k:8s} e.g. ' + ' | '.join(ex[k][:4]))
print(f'{len(out)} of the open checks settled by rule')
if '--write' in sys.argv and out:
    if os.path.exists(DECF): shutil.copy2(DECF, os.path.join(BOOK, '.parts', f'decisions.tsv.bak.{datetime.datetime.now():%Y%m%d-%H%M%S}'))
    with open(DECF, 'a', encoding='utf-8') as fh: fh.write('# rules.py ' + f'{datetime.date.today()}' + '\n' + '\n'.join(out) + '\n')
    print('appended to', os.path.relpath(DECF, ROOT))
