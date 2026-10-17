#!/usr/bin/env python3
"""nbalto.py (2026-10-14) -- fetch Nasjonalbiblioteket's own OCR (ALTO) for every page of Oplevelse og Tydning
(NB item 363c131e7e2e2c6e3b0602f49dae5268, 247 canvases) into texts/hoeffding/kort-oversigt/.parts/alto/NNNN.xml
(NNNN = PDF page of the working scan = NB canvas).  Rerunnable (skips pages it has); stops starting new pages after LIMIT s.
    python3 ebook-method/kort-oversigt/nbalto.py"""
import os, sys, json, time, urllib.request, concurrent.futures as cf
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
ITEM = '363c131e7e2e2c6e3b0602f49dae5268'
D = os.path.join(ROOT, 'texts', 'hoeffding', 'kort-oversigt', '.parts', 'alto'); os.makedirs(D, exist_ok=True)
LIMIT = float(os.environ.get('LIMIT', 150)); T0 = time.time()
f = os.path.join(D, 'manifest.json')
if not os.path.exists(f): urllib.request.urlretrieve(f'https://api.nb.no/catalog/v1/iiif/{ITEM}/manifest', f)
cv = json.load(open(f))['sequences'][0]['canvases']
def one(k):
    out = os.path.join(D, f'{k:04d}.xml'); see = cv[k - 1].get('@seeAlso') or cv[k - 1].get('seeAlso')
    if os.path.exists(out) or not see or time.time() - T0 > LIMIT: return 0
    for _ in range(3):
        try: urllib.request.urlretrieve(see['@id'], out + '.tmp'); os.replace(out + '.tmp', out); return 1
        except Exception: time.sleep(2)
    print('failed', k); return 0
with cf.ThreadPoolExecutor(6) as ex: n = sum(ex.map(one, range(1, len(cv) + 1)))
left = [k for k in range(1, len(cv) + 1) if not os.path.exists(os.path.join(D, f'{k:04d}.xml'))]
print(f'ALTO: {n} fetched in {time.time() - T0:.0f} s; {len(left)} left {left[:12]}')
