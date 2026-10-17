#!/usr/bin/env python3
"""alto.py (2026-10-14, from for-idee-1870-73) -- NB's ALTO for Oplevelse og Tydning (fetched by nbalto.py), one volume.
    python3 alto.py text K [K2]     the ALTO lines of PDF page(s) K..K2 (hyphen parts marked at line ends)
"""
import os, sys, re, xml.etree.ElementTree as ET
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt', '.parts', 'alto')
def alto_lines(k):
    """[(line words [(content, hpos, vpos, width, height, style)], hyphenated)], page (width, height) in mm10"""
    f = os.path.join(D, f'{k:04d}.xml')
    r = ET.parse(f).getroot(); pg = next(e for e in r.iter() if e.tag.endswith('Page'))
    st = {e.get('ID'): (e.get('FONTSTYLE') or '') for e in r.iter() if e.tag.endswith('TextStyle')}
    out = []
    for b_ in r.iter():
        if not b_.tag.endswith('TextBlock'): continue
        bst = ' '.join(st.get(x, '') for x in (b_.get('STYLEREFS') or '').split())
        for ln in b_:
            if not ln.tag.endswith('TextLine'): continue
            ws = []
            for e in ln:
                if e.tag.endswith('String') and (e.get('CONTENT') or '').strip():
                    own = ' '.join(st.get(x, '') for x in (e.get('STYLEREFS') or '').split()) if e.get('STYLEREFS') else bst
                    ws.append((e.get('CONTENT'), *(float(e.get(q)) for q in ('HPOS', 'VPOS', 'WIDTH', 'HEIGHT')),
                               ' '.join(x for x in (own, e.get('STYLE') or '', e.get('SUBS_TYPE') or '') if x)))
            hyp = any(x.tag.endswith('HYP') for x in ln)
            if ws: out.append((ws, hyp))
    return out, (float(pg.get('WIDTH')), float(pg.get('HEIGHT')))
def text(k):
    L, _ = alto_lines(k)
    return [' '.join(w[0] for w in ws) + ('-' if hyp and not ws[-1][0].endswith('-') else '') for ws, hyp in L]
if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'text':
        k = int(a[1]); k2 = int(a[2]) if len(a) > 2 else k
        for q in range(k, k2 + 1):
            print(f'--- PDF {q}'); print('\n'.join(text(q)))
