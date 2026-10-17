#!/usr/bin/env python3
"""ebook-method/kort-oversigt/efix.py -- turn the decided e-book differences (qresolve.py's qdecisions.tsv, with the
decisions made by hand in OVERRIDE below, each from the blind reading named) into efix.tsv: (page, regex, replacement,
note), each regex matching the collated transcription exactly once.  draft.py --post applies efix.tsv after
patches.POST.  Re-run after any rebuild of the collated text: the regexes are made from the words around each place.
    python3 ebook-method/kort-oversigt/efix.py          -> ebook-method/kort-oversigt/efix.tsv (+ report of what failed)"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
BOOK = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt'); RD = os.path.join(BOOK, '.parts', 'reads')
TEX = open(os.path.join(BOOK, 'transcription.tex'), encoding='utf-8').read()
Q = [l.rstrip('\n').split('\t') for l in open(os.path.join(RD, 'qdecisions.tsv'), encoding='utf-8') if l.strip()]
CTX = {l.split('\t')[0]: l.rstrip('\n').split('\t')[5] for l in open(os.path.join(RD, 'qsheets.tsv'), encoding='utf-8') if l.strip()}
RULES_AFTER = {'Q002', 'Q039', 'Q041', 'Q043', 'Q051', 'Q059', 'Q060', 'Q064', 'Q068', 'Q074', 'Q082', 'Q086', 'Q091', 'Q098',
               'Q103', 'Q106', 'Q113', 'Q114', 'Q116', 'Q128', 'Q129', 'Q130', 'Q131', 'Q139', 'Q142', 'Q147', 'Q149', 'Q157',
               'Q159', 'Q163', 'Q165', 'Q172', 'Q173', 'Q201', 'Q205', 'Q206'}   # read at the image: a short rule there
WHITE = {'Q198'}                                                                  # an extra blank line, no rule
# decisions by hand (2026-10-07), each from the blind reading of the crop: value = the print's reading, or 'T'
OVERRIDE = {'Q003': 'T', 'Q009': '', 'Q018': 'T', 'Q023': 'havde', 'Q026': 'T', 'Q036': 'Falstaffscenerne.', 'Q038': 'T',
            'Q040': '', 'Q048': '', 'Q061': '', 'Q071': '', 'Q118': '', 'Q141': '', 'Q049': 'Forskelligheder',
            'Q052': '70’erne,', 'Q055': '70’erne.', 'Q054': 'videnskabelige', 'Q057': 'T', 'Q062': 'T', 'Q066': 'denne Egn.',
            'Q070': 'ser .....', 'Q078': 'T', 'Q080': 'T', 'Q085': 'T', 'Q095': 'T', 'Q134': 'T', 'Q135': 'T', 'Q138': 'T',
            'Q160': 'T', 'Q168': 'T', 'Q195': 'T', 'Q088': 'T', 'Q115': 'T', 'Q119': 'østerrigsk-ungarsk-slaviske',
            'Q120': 'Harvarduniversitetet,', 'Q121': 'T', 'Q132': 'T', 'Q137': 'Genève’s', 'Q150': 'T', 'Q153': 'T',
            'Q156': '', 'Q166': 'Arbejde.', 'Q167': 'T', 'Q175': 'T', 'Q183': 'T', 'Q184': 'T', 'Q185': 'T', 'Q203': 'T',
            'Q105': 'T', 'Q081': 'her.“', 'Q033': 'T', 'Q102': 'ud .....', 'Q196': 'forbi .....', 'Q021': 'T',
            'Q182': 'Nationalitetspricipet % PRINTED AS IS: pricipet (for principet)'}
LEAVE = {'Q020', 'Q021', 'Q028', 'Q044', 'Q053', 'Q154', 'Q155', 'Q181', 'Q193',   # page pass / the 23 Sep reading
         'Q040', 'Q048', 'Q054', 'Q061', 'Q071', 'Q118', 'Q141'}   # sheet signatures and a folio: since removed by draft.py
SEP = r'(?:\s|%[^\n]*\n|\\opage\{\d+\}|\\setcounter\{footnote\}\{0\}|\\textit\{|\}|\\whiteline)*'
def rx(tokens):
    return SEP.join(re.escape(t.replace('—', '---')) for t in tokens)
out, bad = [], []
for qid, p, kind, t, e, d, *_ in Q:
    if qid in LEAVE: continue
    ctx = CTX.get(qid, '')
    pre = ctx.split('[')[0].split()[-3:]; post = ctx.split(']', 1)[1].split()[:2] if ']' in ctx else []
    if kind == 'rule':
        if qid in RULES_AFTER or qid in WHITE:
            ins = '\n\n\\secrule\n\n' if qid in RULES_AFTER else '\n\n\\whiteline\n\n'
            pat = '(' + rx(pre) + ')' + r'(?:\s|\\whiteline)*' + '(?=' + rx(post) + ')'   # a white line found by its gap gives way to the rule
            out.append((p, qid, pat, '\\g<1>' + ins.replace('\\', '\\\\'), 'section ' + ('rule' if qid in RULES_AFTER else 'white line') + ', read at the image'))
        continue
    v = OVERRIDE.get(qid, {'E': e, 'E?': e}.get(d, 'T'))
    if v == 'T': continue
    tt = t.split()
    pat = '(' + rx(pre) + SEP + ')' + rx(tt) + '(?=' + SEP + rx(post) + ')' if tt else '(' + rx(pre) + ')' + '(?=' + SEP + rx(post) + ')'
    v2 = v.replace('—', '---')
    if '% PRINTED' in v2: v2 = v2.split(' %')[0] + '%\n' + '%' + v2.split(' %', 1)[1] + '\n'
    out.append((p, qid, pat, '\\g<1>' + (' ' if not tt and v2 else '') + v2.replace('\\', '\\\\'), f'e-book difference read at the image ({qid})'))
MANUAL = [   # where the words around the place did not make a unique pattern (a ']' in the context, a name twice)
    ('254', 'Q148', r'(Professor Axel\s+)Her lin', r'\g<1>Herlin', 'e-book difference read at the image (Q148)'),
    ('308', 'Q201', r'(\[Brevet maa være skrevet omkring 1900\]\.)(?:\s|\\whiteline)*(?=Personlighedsfilosofi)', r'\g<1>\n\n\\secrule\n\n', 'section rule, read at the image (Q201)'),
]
out = [o for o in out if o[1] not in ('Q148', 'Q201')] + MANUAL
good = []
for p, qid, pat, rep, note in out:
    n = len(re.findall(pat, TEX))
    if n == 1: good.append((p, qid, pat, rep, note))
    else: bad.append((qid, p, n, pat[:120]))
with open(os.path.join(HERE, 'efix.tsv'), 'w', encoding='utf-8') as f:
    f.write('# efix.py output: page, id, regex, replacement, note -- applied by draft.py --post after patches.POST\n')
    for r in good: f.write('\t'.join(str(x).replace('\n', '\\n') for x in r) + '\n')   # a newline in a replacement is written \\n (re.sub reads it back)
print(len(good), 'fixes written;', len(bad), 'failed to match exactly once:')
for b in bad: print('  ', b)
