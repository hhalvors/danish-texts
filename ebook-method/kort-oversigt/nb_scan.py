#!/usr/bin/env python3
"""ebook-method/kort-oversigt/nb_scan.py (copied 2026-10-14 from ebook-method/etik/; the notes command also drops
this book's signature line "Oplevelse og Tydning. N") -- a scan from the National Library of Norway (nb.no) as a PDF with NB's own OCR
as its text layer, so that draft.py (pdftotext) and collate/check.py can read it like a Google scan.

    python3 ebook-method/etik/nb_scan.py fetch ID WORK      page images (full resolution) and ALTO files, by IIIF
    python3 ebook-method/etik/nb_scan.py italics WORK OUT.tsv the words NB set in italics (for collate/check.py --italics)
    python3 ebook-method/etik/nb_scan.py spaced WORK OUT.tsv  the letterspaced words (for draft.py --post: \\emph)
    python3 ebook-method/etik/nb_scan.py notes WORK OUT.tsv  where each page's notes begin (for draft.py)
    python3 ebook-method/etik/nb_scan.py build WORK OUT.pdf  bind the images (no re-encoding) at --dpi and lay the
                                                             ALTO words over them as invisible text; NB's superscripts
                                                             (note marks) as superscript digits ¹ ² ³,
                                                             and the line-end hyphen (ALTO <HYP>) on its word

ID is the item's id in nb.no's catalog (the last part of https://www.nb.no/items/ID); WORK a folder for img/ and
alto/ (kept outside the repo: ~400 MB for 600 pages).  fetch skips what it already has and stops after --budget
seconds (default 160): rerun until it says "done".  --dpi (default 400) is the scan resolution: NB's ALTO is in
tenths of a millimetre, and the page then has its real size (check: ALTO <Page WIDTH> = image width / dpi * 254).
Needs curl, img2pdf, qpdf, python3 with reportlab and pikepdf, the DejaVu Sans font.  Self-contained; no Claude.

For Høffding, Etik, 4th ed. (1913): ID 07731ad5577885d75315de373989dc06 (URN:NBN:no-nb_digibok_2012092108074),
public domain, open everywhere.  Fetched 2026-10-04."""
import os, sys, json, re, time, subprocess, glob
import xml.etree.ElementTree as ET
a = sys.argv[1:]
if len(a) < 3: sys.exit(__doc__)
opt = lambda k, d: a[a.index(k) + 1] if k in a else d
cmd = a[0]; DPI = int(opt('--dpi', 400)); BUDGET = float(opt('--budget', 160))
def curl(url, out):
    r = subprocess.run(['curl', '-sS', '--retry', '3', '--max-time', '90', '-o', out + '.tmp', url])
    if r.returncode == 0 and os.path.getsize(out + '.tmp') > 0: os.replace(out + '.tmp', out); return True
    return False

if cmd == 'fetch':
    ID, WORK = a[1], a[2]
    for d in ('img', 'alto'): os.makedirs(os.path.join(WORK, d), exist_ok=True)
    mf = os.path.join(WORK, 'manifest.json')
    if not os.path.exists(mf): curl(f'https://api.nb.no/catalog/v1/iiif/{ID}/manifest', mf)
    cv = json.load(open(mf))['sequences'][0]['canvases']; t0 = time.time()
    for i, c in enumerate(cv, 1):
        img, alto = os.path.join(WORK, 'img', f'{i:04d}.jpg'), os.path.join(WORK, 'alto', f'{i:04d}.xml')
        if os.path.exists(img) and os.path.exists(alto): continue
        if time.time() - t0 > BUDGET: print(f'{len(cv) - i + 1} canvases still to fetch; run again'); sys.exit(0)
        if not os.path.exists(img): curl(c['images'][0]['resource']['@id'], img)
        if os.path.exists(img) and open(img, 'rb').read(2) != b'\xff\xd8':   # kort-oversigt (2026-10-17): NB sent a 403 page
            os.replace(img, img + '.bad'); print('not a JPEG, fetch again:', img)   # (99 bytes of HTML) as image 0040; img2pdf failed
        see = c.get('@seeAlso') or c.get('seeAlso')
        if see and not os.path.exists(alto): curl(see['@id'], alto)
    print(f'done: {len(cv)} canvases in {WORK}')

elif cmd == 'build':
    WORK, OUT = a[1], os.path.abspath(a[2])
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    font = subprocess.run(['fc-match', '-f', '%{file}', 'DejaVu Sans'], capture_output=True, text=True).stdout
    pdfmetrics.registerFont(TTFont('DV', font))
    imgs = sorted(glob.glob(os.path.join(WORK, 'img', '*.jpg')))
    tmp = os.path.join(WORK, 'tmp'); os.makedirs(tmp, exist_ok=True)
    subprocess.run(['img2pdf', '--imgsize', f'{DPI}dpi', *imgs, '-o', f'{tmp}/images.pdf'], check=True)
    import pikepdf
    SUP = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')
    src = pikepdf.open(f'{tmp}/images.pdf'); K = 72 / 254          # points per tenth of a millimetre
    c = canvas.Canvas(f'{tmp}/text.pdf')
    for k, img in enumerate(imgs):
        mb = src.pages[k].mediabox; W, H = float(mb[2]), float(mb[3]); c.setPageSize((W, H))
        alto = img.replace(os.sep + 'img' + os.sep, os.sep + 'alto' + os.sep)[:-4] + '.xml'
        if os.path.exists(alto):
            root = ET.parse(alto).getroot()
            unit = (root.findtext('.//{*}MeasurementUnit') or 'mm10').strip()
            s = K if unit == 'mm10' else 72 / DPI                     # 'pixel'
            t = c.beginText(); t.setTextRenderMode(3)                   # invisible
            # each word on its ALTO line's baseline (the line's bottom), at the size of the line's typical word: the
            # words of one line then share one height, so that the line is not torn apart when draft.py and check.py
            # rebuild lines from the word boxes (a tilted scan otherwise splits a small-type line in two)
            for ln in root.iter():
                if not ln.tag.endswith('TextLine'): continue
                ws = [e for e in ln if e.tag.endswith('String') and (e.get('CONTENT') or '').strip()]
                if not ws: continue
                hs = sorted(float(e.get('HEIGHT')) * s for e in ws if not 'superscript' in (e.get('STYLE') or ''))
                fs = max(1.0, hs[len(hs) // 2] if hs else float(ws[0].get('HEIGHT')) * s)
                # oplevelse: the MEDIAN word bottom, not the lowest: a chapter's two-line initial („D“ of „Det“, 74 units high
                # against the line's ~25) put the whole first line on the second line's baseline, and draft.py merged the two
                bots = sorted((float(e.get('VPOS')) + float(e.get('HEIGHT'))) * s for e in ws if not 'superscript' in (e.get('STYLE') or ''))
                base = bots[len(bots) // 2] if hs else (float(ln.get('VPOS')) + float(ln.get('HEIGHT'))) * s
                for k, e in enumerate(ws):
                    w = e.get('CONTENT')
                    if 'superscript' in (e.get('STYLE') or ''):       # a note mark (or a note's number): keep it
                        w = w.translate(SUP)                             # recognisable, as superscript digits
                        nxt = ws[k + 1].get('CONTENT') if k + 1 < len(ws) else ''
                        if re.fullmatch(r'[^\W\d_]', w) and nxt.startswith(')'): w = '¹'   # 1 read as x, J, l: a mark (a quote mark read as I has no ")")
                    if k == len(ws) - 1 and (e.get('SUBS_TYPE') == 'HypPart1' or any(x.tag.endswith('HYP') for x in ln)) \
                            and not w.endswith('-'):
                        w += '-'                                         # NB keeps the line-end hyphen apart (<HYP>): put it back
                    x, ww = float(e.get('HPOS')) * s, float(e.get('WIDTH')) * s
                    nat = pdfmetrics.stringWidth(w, 'DV', fs) or 1
                    t.setFont('DV', fs); t.setHorizScale(100 * ww / nat)
                    t.setTextOrigin(x, H - base + 0.2 * fs); t.textOut(w)
            c.drawText(t)
        c.showPage()
    c.save()
    subprocess.run(['qpdf', f'{tmp}/images.pdf', '--overlay', f'{tmp}/text.pdf', '--', OUT], check=True)
    print('done:', OUT, f'({len(imgs)} pages, {DPI} dpi)')
elif cmd == 'notes':
    # where the notes begin on each page, from the ALTO lines: below a gap, the lines from which the pitch stays
    # small (the notes' smaller type), or a single line that starts with a note number or is set smaller.
    # NB's layer keeps no trace of its blocks, so draft.py cannot see this itself; it reads OUT (page<TAB>pt from
    # the top), written here once and kept in the repo beside pagemap.py.
    import statistics as S
    MARK=re.compile(r"^(\S{0,2}\)|[¹²³⁴⁵⁶⁷⁸⁹1-9*'’])$")
    def classify(f):
        r=ET.parse(f).getroot()
        unit=(r.findtext('.//{*}MeasurementUnit') or 'mm10').strip()
        B=[]
        for b in r.iter():
            if not b.tag.endswith('TextBlock'): continue
            L=[]
            for l in b:
                if not l.tag.endswith('TextLine'): continue
                ws=[s for s in l if s.tag.endswith('String') and (s.get('CONTENT') or '').strip()]
                if not ws: continue
                bot=S.median(float(s.get('VPOS'))+float(s.get('HEIGHT')) for s in ws)
                hs=[float(s.get('HEIGHT')) for s in ws if len(s.get('CONTENT'))>2 and 'super' not in (s.get('STYLE') or '')]
                L.append(dict(bot=bot,top=float(l.get('VPOS')),x=float(ws[0].get('HPOS')),h=S.median(hs) if hs else None,
                              t=' '.join(s.get('CONTENT') for s in ws), sup='super' in (ws[0].get('STYLE') or '')))
            if L: B.append(dict(v=float(b.get('VPOS')),L=L))
        B.sort(key=lambda b:b['v'])
        AL=[l for b in B for l in b['L']]
        AL.sort(key=lambda l:l['bot'])
        if len(AL)<6: return None,unit,AL
        d=[b['bot']-a['bot'] for a,b in zip(AL,AL[1:])]
        top=[x for x in d[:12] if x>0]
        pitch=S.median(top)                     # the body's pitch: the top of the page is always text
        pitch=S.median([x for x in top if 0.85*pitch<x<1.15*pitch] or [pitch])
        hmed=S.median([l['h'] for l in AL if l['h']])
        # from the bottom: drop signature/sheet-number lines
        n=len(AL)
        while n>0 and (re.search(r'H\S{0,2}\s*H\S{3,7}\W*Etik|H\S{3,9}\W*Kort\W*Oversigt\W.{0,15}$',AL[n-1]['t']) or len(re.findall(r'[A-Za-zæøå]',AL[n-1]['t']))<=2): n-=1
        # walk down: the notes start at the first line i (in lower part) after a gap > 1.12 pitch, from which on the pitch stays < 0.92 pitch
        for i in range(3,n):
            gap=AL[i]['bot']-AL[i-1]['bot']
            after=[AL[j+1]['bot']-AL[j]['bot'] for j in range(i,n-1)]
            tok=AL[i]['t'].split()[0]
            markish=AL[i]['sup'] or bool(MARK.match(tok)) or (len(AL[i]['t'].split())>1 and len(tok)<=2 and AL[i]['t'].split()[1].startswith(')'))
            aft=sorted(after); small_after=bool(aft) and aft[int(0.8*(len(aft)-1))]<0.94*pitch
            hs=[l['h'] for l in AL[i:n] if l['h']]
            small_h=bool(hs) and S.median(hs)<0.93*hmed
            first=AL[i]['t']; letters=len(re.findall(r'[A-Za-zæøåÆØÅ]',' '.join(l['t'] for l in AL[i:n])))
            if not markish or letters<8: continue   # no rule found: only a line that starts with a note's number
            if gap>1.12*pitch and (small_after or (not after and (markish or small_h))) and (markish or small_h or small_after and len(after)>=2):
                return AL[i]['top'],unit,AL[i:n]
        return None,unit,[]
    # first and best: the short rule printed above the notes, found in the page image (a dark stroke from the
    # text's left edge, a tenth to a third of the line, white above and below; the scan's tilt is allowed for)
    import numpy as np
    from PIL import Image
    def find_rule(path, dpi=400):
        a=np.asarray(Image.open(path).convert('L'),dtype=np.int16); h,w=a.shape
        off=int(w*0.06); a=a[:, off:int(w*0.94)]
        dark=a<np.median(a)-30
        inked=np.where((a<np.median(a)-60).sum(0)>h*0.03)[0]
        if len(inked)<10: return None
        left=inked[0]; tw=inked[-1]-left
        st=6; win=12; n=(h-win)//st
        P=np.stack([dark[j*st:j*st+win].any(0) for j in range(n)])
        C=P.sum(1)
        for j in range(int(n*0.12),int(n*0.93)):
            c=C[j]
            if not (0.1*tw<=c<=0.35*tw): continue
            xs=np.where(P[j])[0]; br=np.where(np.diff(xs)>8)[0]           # runs, allowing small breaks in the stroke
            st_=np.r_[0,br+1]; en_=np.r_[br,len(xs)-1]; r_=int(np.argmax(xs[en_]-xs[st_]))
            x0_,x1_=xs[st_[r_]],xs[en_[r_]]; inrun=en_[r_]-st_[r_]+1; span=x1_-x0_+1
            if not (0.1*tw<=span<=0.35*tw) or abs(x0_-left)>0.06*tw or inrun<0.85*span or inrun<0.8*c: continue   # one stroke from the left edge
            if C[j-2]>0.04*tw or C[j+2]>0.08*tw: continue              # white above and below
            return (j*st+win/2)*72/dpi
        return None
    WORK, OUT = a[1], a[2]; rows = []
    for f in sorted(glob.glob(os.path.join(WORK, 'alto', '*.xml'))):
        k = int(os.path.basename(f)[:-4])                              # the PDF page (1-based)
        r_ = find_rule(os.path.join(WORK, 'img', f'{k:04d}.jpg'), DPI)
        if r_ is not None: rows.append(f'{k}\t{r_ + 2:.1f}\trule'); continue
        top, unit, NL = classify(f)
        if top is None: continue
        s_ = 72 / 254 if unit == 'mm10' else 72 / DPI
        rows.append(f'{k}\t{top * s_:.1f}\talto: {NL[0]["t"][:50]}')
    open(OUT, 'w', encoding='utf-8').write('# pdfpage\tnotes_top_pt\tfirst words (nb_scan.py notes; generated)\n' + '\n'.join(rows) + '\n')
    print(len(rows), 'pages with notes ->', OUT)
elif cmd == 'italics':
    # the words NB's OCR set in italics (STYLE or TextStyle FONTSTYLE "italics"), as boxes in points from the top
    # left of the PDF page: collate/check.py --italics reads them (pagemap.italic_boxes) beside its own slant test
    WORK, OUT = a[1], a[2]; rows = []
    for f in sorted(glob.glob(os.path.join(WORK, 'alto', '*.xml'))):
        k = int(os.path.basename(f)[:-4]); root = ET.parse(f).getroot()
        unit = (root.findtext('.//{*}MeasurementUnit') or 'mm10').strip(); s_ = 72 / 254 if unit == 'mm10' else 72 / DPI
        st = {e.get('ID'): (e.get('FONTSTYLE') or '') for e in root.iter() if e.tag.endswith('TextStyle')}
        for b in root.iter():
            if not b.tag.endswith('TextBlock'): continue
            bst = ' '.join(st.get(x, '') for x in (b.get('STYLEREFS') or '').split())
            for e in b.iter():
                if not e.tag.endswith('String'): continue
                own = ' '.join(st.get(x, '') for x in (e.get('STYLEREFS') or '').split()) if e.get('STYLEREFS') else bst
                if 'italic' in own or 'italic' in (e.get('STYLE') or ''):
                    x, y, w, h = (float(e.get(q)) * s_ for q in ('HPOS', 'VPOS', 'WIDTH', 'HEIGHT'))
                    rows.append(f'{k}\t{x:.1f}\t{y:.1f}\t{x + w:.1f}\t{y + h:.1f}\t{e.get("CONTENT")}')
    open(OUT, 'w', encoding='utf-8').write('# pdfpage\tx0\ty0\tx1\ty1\tword (pt; nb_scan.py italics; generated)\n' + '\n'.join(rows) + '\n')
    print(len(rows), 'italic words ->', OUT)
elif cmd == 'spaced':
    # the words the print letterspaces (names, in the notes above all): a word whose box is at least 15% wider than
    # its letters need in Times (reportlab's metrics), against the median of its line; draft.py --post sets them \emph
    import statistics as S
    from reportlab.pdfbase.pdfmetrics import stringWidth
    WORK, OUT = a[1], a[2]; rows = []
    for f in sorted(glob.glob(os.path.join(WORK, 'alto', '*.xml'))):
        k = int(os.path.basename(f)[:-4]); root = ET.parse(f).getroot()
        for ln in root.iter():
            if not ln.tag.endswith('TextLine'): continue
            ws = [e for e in ln if e.tag.endswith('String') and len(re.sub(r'\W', '', e.get('CONTENT') or '')) >= 3]
            if len(ws) < 4: continue
            cw = [float(e.get('WIDTH')) / stringWidth(e.get('CONTENT'), 'Times-Roman', 10) for e in ws]
            m = S.median(cw)
            for e, c in zip(ws, cw):
                if c / m >= 1.15 and len(re.sub(r'\W', '', e.get('CONTENT'))) >= 4: rows.append(f'{k}\t{e.get("CONTENT")}\t{c / m:.2f}')
    open(OUT, 'w', encoding='utf-8').write('# pdfpage\tword\twidth ratio (nb_scan.py spaced; generated)\n' + '\n'.join(rows) + '\n')
    print(len(rows), 'letterspaced words ->', OUT)
else: sys.exit(__doc__)
