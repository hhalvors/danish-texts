#!/usr/bin/env python3
"""(copied 2026-10-12 from ebook-method/udvalgte-stykker/) ebook-method/kort-oversigt/reads.py (2026-10-11, from om-aandsdannelse/reads.py) -- turn the BLIND readings of the
crop sheets into decisions.  Reader files (READER-BRIEF.md): .parts/reads/r-<tag>.tsv, one per reader and tag, lines
    id <TAB> BOX <TAB> LINE <TAB> NOTE        b-sheets (word checks)     markup: <sc>..</sc> small caps, *..* italics
    id <TAB> LINE <TAB> NOTE                  i-sheets (italics)  l-sheets (<sp>..</sp> letterspacing)  m-sheets (answer)
paired with sheets-<tag>.tsv (sheet, id, page, check key) and controls-<tag>.tsv written by the sheet scripts.
  b: the draft's reading (e) and tesseract's (w), set in their context, are looked for in the reader's LINE/BOX (markup
     and whitespace ignored, quote kinds and dashes kept); exactly one fits -> T / W; a case-only check whose word the
     reader wrote in <sc> -> SC; a reader NOTE with doubt/misprint/PRINTED -> by hand.  Everything else is listed.
  i: the run's words all inside *..* -> italic, all outside -> roman; the decision is W when that is what the slant
     claimed, T otherwise (check.py's italics keys: E<page>|words>italic|roman).
  l: every <sp>span</sp> the draft does not already have in \\emph is proposed for spaced.tsv (page, two words before,
     span, id); every draft \\emph on a line read with no <sp> is listed (a POST patch must remove it).
  m: listed for the main session (patches by hand) -- except `par` (round 3): a yes/no whose quoted line begins with the
     boxed words is written to pars.tsv and APPLIED by draft.py --post; the rest are listed.
  controls: b -- the known word must stand in the reader's BOX; i -- no italics on a known roman line.  Scored per tag.
    python3 ebook-method/kort-oversigt/reads.py            dry run
    python3 ebook-method/kort-oversigt/reads.py --tags b2,i2,l2,m2 [--write]   round 1: only these tags' reader files
  (round 1, 2026-10-11) controls are scored for every kind: b known word in BOX; i no italics on a roman line; l 'roman'
  = no <sp> in the line, 'sp:word' = the word inside <sp>..</sp>; m 'yes'/'no' = the answer begins so.
    python3 ebook-method/kort-oversigt/reads.py --write    append b/i decisions to decisions.tsv ("image, blind read")
                                                              and l proposals to spaced.tsv (backups in .parts/)"""
import os, re, sys, glob, shutil, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE); import pagemap as C
BOOK = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt'); DECF = os.path.join(HERE, 'decisions.tsv'); SPF = os.path.join(HERE, 'spaced.tsv')
RD = os.path.join(BOOK, '.parts', 'reads')
L = 'A-Za-zÀ-ÖØ-öø-ÿ0-9'; letters = lambda s: re.sub('[^' + L + ']', '', s)
unmark = lambda s: re.sub(r'</?sc>|</?sp>|\*', '', s)
def q(s):
    s = re.sub(r'\(?\*{1,4}\)', '', s)                   # oplevelse: a note mark *) **) (the draft has \footnote there), «(*) too
    s = unmark(s).replace('^', '').replace('---', '—')   # moderne-filosoffer: a raised figure ^1.replace('--', '–').replace('∅', '').replace('\\dots{}', '...')
    s = re.sub(r'\\opage\{\d+\}|\\footnote(mark)?\[\d\]\{?|\\[a-zA-Z]+\{|[{}]', '', s)
    return s.replace('"', '“')
nz = lambda s: re.sub(r'\s+', '', q(s)); sp = lambda s: re.sub(r'\s+', ' ', q(s)).strip()
def load(tag):
    idx = {}
    f = os.path.join(RD, f'sheets-{tag}.tsv')
    if os.path.exists(f):
        for l in open(f, encoding='utf-8'):
            x = l.rstrip('\n').split('\t')
            if len(x) >= 3: idx[x[1]] = (int(x[2]), x[3] if len(x) > 3 else ''); BOXW[x[1]] = x[4] if len(x) > 4 else ''
    ctl = {}
    f = os.path.join(RD, f'controls-{tag}.tsv')
    if os.path.exists(f):
        for l in open(f, encoding='utf-8'):
            x = l.rstrip('\n').split('\t')
            if len(x) >= 4: ctl[x[1]] = (int(x[2]), x[3])
    return idx, ctl
BOXW = {}                                           # round 3: the boxed words of each m item (sheets-<tag>.tsv col. 5)
done = set()
if os.path.exists(DECF): done = {l.split('\t')[0] for l in open(DECF, encoding='utf-8') if '\t' in l and not l.startswith('#')}
CH = {}
f = os.path.join(BOOK, '.parts', 'collate', 'checks.tsv')
if os.path.exists(f):
    for l in open(f, encoding='utf-8'): x = l.rstrip('\n').split('\t'); CH[x[1]] = x
def decide(e, w, pre, post, box, line):
    if letters(e) == letters(w) and sp(e).replace(' ', '') == sp(w).replace(' ', ''):        # word division / spacing
        b = ' ' + sp(box) + ' '
        te, tw = (' ' + sp(e) + ' ') in b, (' ' + sp(w) + ' ') in b
        return ('T' if te else 'W') if te != tw else None
    hay = [nz(line), nz(box)]
    for a, z in ((6, 4), (0, 4), (6, 0), (0, 0)):
        if (a and len(pre) < a) or (z and len(post) < z): continue
        if not (a and z) and (not nz(e) or not nz(w)): continue
        if not a and not z and (len(nz(e)) < 4 or len(nz(w)) < 4): continue
        ce = any((pre[-a:] if a else '') + nz(e) + post[:z] in h for h in hay)
        cw = any((pre[-a:] if a else '') + nz(w) + post[:z] in h for h in hay)
        if ce != cw: return 'T' if ce else 'W'
        if ce and cw: return None
    return None
out, hand, ctlres, spaced, spacedhand = [], [], [], [], []
pars, parchg = [], []
parkey = lambda t: re.sub(r'[^a-zà-ÿ0-9]', '', re.sub(r'\\opage\{\d+\}|\\(emph|textsc|textit)\{|\\begin\{intro\}|[{}]', '', t).lower().replace('---', '—')).replace('ö', 'o')
def parline(p, rline):                              # round 3: the build line the reader quoted -> (index, its first words, is it a paragraph start?)
    LL = TEX.split('\n')
    try: a_ = LL.index(f'% --- p. {p} ---')
    except ValueError: return None
    b_ = next((k for k in range(a_ + 1, len(LL)) if LL[k].startswith('% --- ')), len(LL))
    want = parkey(unmark(rline))[:24]
    hit = [k for k in range(a_ + 1, b_) if want and not LL[k].startswith('%') and want in parkey(LL[k])[:len(want) + 3]]   # +3: an item mark the reader wrote differently (α. / a.)
    if len(hit) != 1: return None
    i_ = hit[0]; j_ = i_ - 1
    while j_ >= 0 and (LL[j_].startswith('% --- p.') or LL[j_].startswith('\\setcounter{footnote}')): j_ -= 1
    is_par = LL[j_].strip() == '' or bool(re.match(r'\\(anthsection|excerpthead|sectionrule|begin|end)', LL[j_].strip())) or LL[i_].lstrip().startswith('\\begin{')
    words = re.sub(r'\\opage\{\d+\}|\\(emph|textsc|textit)\{|\\begin\{intro\}|[{}]', '', LL[i_]).split()[:5]
    return i_, ' '.join(words), is_par
DOUBT = re.compile(r'doubt|unclear|misprint|PRINTED|as printed|illegible|\?\?', re.I)
TEX = open(os.path.join(BOOK, C.TEXFILE), encoding='utf-8').read()
PAGES_TXT = dict(re.findall(r'% --- p\. (\d+) ---(.*?)(?=% --- p\. \d+ ---|% --- INDHOLD|\\end\{document\})', TEX, re.S))
TAGS = set(sys.argv[sys.argv.index('--tags') + 1].split(',')) if '--tags' in sys.argv else None
for fn in sorted(glob.glob(os.path.join(RD, 'r-*.tsv'))):
    tag = re.match(r'r-([a-z]\d+)', os.path.basename(fn)).group(1); kind = tag[0]
    if TAGS and tag not in TAGS: continue
    idx, ctl = load(tag)
    for l in open(fn, encoding='utf-8'):
        x = l.rstrip('\n').split('\t')
        if not x or not x[0].strip() or x[0].startswith('#'): continue
        cid = x[0].strip()
        if cid in ctl:
            p, known = ctl[cid]; txt = ' '.join(x[1:])
            f1 = x[1] if len(x) > 1 else ''
            if kind == 'b': ok = known in unmark(txt)
            elif kind == 'i': ok = '*' not in f1
            elif kind == 'l': ok = ('<sp>' not in f1) if known == 'roman' else any(letters(known[3:]).lower() in letters(z).lower() for z in re.findall(r'<sp>(.*?)</sp>', f1))
            else: ok = f1.strip().lower().startswith(known)
            ctlres.append((tag, cid, ok, known, txt[:80])); continue
        if cid not in idx: hand.append(f'{fn[-12:]} {cid}: unknown id'); continue
        p, key = idx[cid]
        if kind == 'b':
            box, line, note = (x + ['', '', ''])[1:4]
            if key in done: continue
            if key.startswith('X'): hand.append(f'{tag}:{cid} p.{p} EXTRA {key}  BOX[{box}] LINE[{line}] {note}'); continue   # round 2: third-witness spots (sheets.py --extra), decided by hand
            e, w = key.split('|', 1)[1].split('>', 1); w = re.sub(r'#\d+$', '', w)
            c = CH.get(key); pre, post = (nz(re.sub(r'\[[^\[\]]*\]$', '', c[2])), nz(c[3])) if c else ('', '')
            scs = re.findall(r'<sc>(.*?)</sc>', box + ' ' + line)
            if e.lower() == w.lower() and e != w and any(letters(s_).lower() == letters(e).lower() or letters(e).lower() in [letters(t_).lower() for t_ in s_.split()] for s_ in scs): d = 'SC'   # round 1: a word inside a longer <sc> span (round 2: the ': d = SC' had slipped into this comment, a SyntaxError)
            else: d = decide(e, w, pre, post, box, line)
            if d and not DOUBT.search(note): out.append(f'{key}\t{d}\timage, blind read {tag}:{cid}' + (f' ({note})' if note else ''))
            else: hand.append(f'{tag}:{cid} p.{p} {key}  BOX[{box}] LINE[{line}] {note}')
        elif kind == 'i':
            line, note = (x + ['', ''])[1:3]
            if key in done: continue
            line = re.sub(r'(^|\s)\*{1,3}\)', r'\1', line)   # round 4: a footnote mark „*)“ at a line start or after a space is no italic span (round 3: i4-03-02/04 misparsed); „*natura naturans*)“ keeps its asterisk
            words = key.split('|', 1)[1].rsplit('>', 1)[0].split(); claim = key.rsplit('>', 1)[1]
            spans = ' '.join(re.findall(r'\*(.*?)\*', line)); rest = re.sub(r'\*.*?\*', ' ', line)
            ins = [letters(w_) in letters(spans) for w_ in words]; outs = [letters(w_) in letters(rest) for w_ in words]
            if all(ins) and not any(outs): st = 'italic'
            elif all(outs) and not any(ins): st = 'roman'
            else: st = None
            if st and not DOUBT.search(note): out.append(f"{key}\t{'W' if st == claim else 'T'}\timage, blind read {tag}:{cid} ({st})")
            else: hand.append(f'{tag}:{cid} p.{p} {key}  LINE[{line}] {note}')
        elif kind == 'l':
            line, note = (x + ['', ''])[1:3]
            ptxt = PAGES_TXT.get(str(p), ''); have = [letters(s_) for s_ in re.findall(r'\\emph\{([^}]*)\}', ptxt)]
            for m in re.finditer(r'<sp>(.*?)</sp>', line):
                span = m.group(1).strip(); before = ' '.join(unmark(line[:m.start()]).split()[-2:])
                if letters(span) in have: continue
                spaced.append(f'{p}\t{before}\t{span}\t{tag}:{cid}')
            if '<sp>' not in line:
                for h_ in have:
                    if h_ and h_ in letters(line): spacedhand.append(f'{tag}:{cid} p.{p}: draft has \\emph "{h_}", reader saw no spacing: {line}')
            if note: hand.append(f'{tag}:{cid} p.{p} NOTE: {note}')
        elif key == 'par':                          # round 3: paragraph starts are APPLIED (pars.tsv -> draft.py --post)
            ans = x[1].split('//')[0].strip().lower() if len(x) > 1 else ''; rline = x[1].split('//', 1)[1] if '//' in x[1] else ''
            note = x[2] if len(x) > 2 else ''
            bw = BOXW.get(cid, ''); r_ = parline(p, rline)
            # the guard (round 3 audit): the reader's quoted line must BEGIN with the boxed words -- in rounds 0-2 eleven page-top
            # crops had the box on another line (miscsheets.find skipped the page's first line with the running head), and the
            # readers answered 'no' for that other line; applied blindly those would have removed eleven right paragraphs
            if ans not in ('yes', 'no') or DOUBT.search(note) or r_ is None or not any(parkey(bw)[i:i + 5] and parkey(bw)[i:i + 5] in parkey(unmark(rline))[:10] for i in range(3)):   # an item mark read differently (α./a.) may lead the box
                hand.append(f'{tag}:{cid} p.{p} [par] box „{bw}“ NOT APPLIED (answer/line do not fit the box, or doubt): ' + ' | '.join(x[1:])); continue
            i_, phrase, is_par = r_
            pars.append(f'{p}\t{phrase}\t{ans}\t{tag}:{cid}')
            if (ans == 'yes') != is_par: parchg.append(f'{tag}:{cid} p.{p} „{phrase}“: reader {ans}, build {"para" if is_par else "cont"} -> pars.tsv changes it')
        else:
            hand.append(f'{tag}:{cid} p.{p} [{key}] ' + ' | '.join(x[1:]))
print(f'{len(out)} decisions found; {len(hand)} for a decision by hand; {len(spaced)} letterspaced spans proposed')
bad = [c for c in ctlres if not c[2]]
print(f'controls: {len(ctlres) - len(bad)} of {len(ctlres)} right' + (''.join(f'\n  MISSED {t}:{c} known „{k}“ read: {r}' for t, c, ok, k, r in bad)))
for h in hand + spacedhand: print('  ' + h)
print(f'paragraph starts: {len(pars)} answers applicable (pars.tsv), {len(parchg)} change the build')
for h in parchg: print('  PAR ' + h)
if '--write' in sys.argv:
    stamp = f'{datetime.datetime.now():%Y%m%d-%H%M%S}'
    if out:
        if os.path.exists(DECF): shutil.copy2(DECF, os.path.join(BOOK, '.parts', f'decisions.tsv.bak.{stamp}'))
        with open(DECF, 'a', encoding='utf-8') as fh: fh.write(f'# reads.py {datetime.date.today()}\n' + '\n'.join(out) + '\n')
    if spaced:
        if os.path.exists(SPF): shutil.copy2(SPF, os.path.join(BOOK, '.parts', f'spaced.tsv.bak.{stamp}'))
        with open(SPF, 'a', encoding='utf-8') as fh: fh.write(f'# reads.py {datetime.date.today()}\n' + '\n'.join(spaced) + '\n')
    PARF = os.path.join(HERE, 'pars.tsv'); have_ = set()
    if os.path.exists(PARF): have_ = {l.split('\t')[3].strip() for l in open(PARF, encoding='utf-8') if l.count('\t') >= 3 and not l.startswith('#')}
    newp = [l_ for l_ in pars if l_.split('\t')[3] not in have_]
    if newp:
        with open(PARF, 'a', encoding='utf-8') as fh: fh.write(f'# reads.py {datetime.date.today()}\n' + '\n'.join(newp) + '\n')
    print('written:', len(out), 'decisions,', len(spaced), 'spaced spans,', len(newp), 'paragraph answers (pars.tsv; applied by draft.py --post)')
