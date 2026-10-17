#!/usr/bin/env python3
"""ocr.py (2026-10-14; from for-idee-1870-73 and moderne-filosoffer) -- the WITNESS for collate/check.py --witness ocr:
tesseract `dan` (tessdata_best in the repo's .tessdata/) on each page, cached as
texts/hoeffding/kort-oversigt/.parts/collate/ocr/pN.tsv.  The page renders check.py looks for
(.render/kort-oversigt-pN-300.png and -200.png) are made from the page's own 400-dpi JPEG (pagemap.page_image,
nb_scan.py fetch -> /tmp/kort/img; else extracted from the scan by pdfimages), turned grey and scaled -- not pdftoppm,
which takes ~10 s a page on an image-only PDF of this size.  Rerunnable: only pages not yet cached; 4 workers; starts no
new page after LIMIT seconds (default 140), so one run fits one device call.  Run until it prints "done".
    python3 ebook-method/kort-oversigt/ocr.py"""
import os, sys, time, subprocess, tempfile, glob, concurrent.futures as cf
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE); import pagemap as C
from PIL import Image
O = os.path.join(C.BOOKDIR, '.parts', 'collate', 'ocr'); R = os.path.join(C.BOOKDIR, '.render')
os.makedirs(O, exist_ok=True); os.makedirs(R, exist_ok=True)
env = dict(os.environ, TESSDATA_PREFIX=os.path.join(ROOT, '.tessdata'), OMP_THREAD_LIMIT='1')
LIMIT = float(os.environ.get('LIMIT', 140)); T0 = time.time()
def source(p):
    f = os.path.join(C.IMGDIR, f'{C.pdfpage(p):04d}.jpg')
    if os.path.exists(f): return Image.open(f), None
    d = tempfile.mkdtemp(dir='/tmp'); k = C.pdfpage(p)
    subprocess.run(['pdfimages', '-j', '-f', str(k), '-l', str(k), C.scan_path(), os.path.join(d, 'i')], check=True)
    j = sorted(glob.glob(os.path.join(d, 'i-*')))
    if len(j) != 1: raise SystemExit(f'p. {p}: {len(j)} images on the page')
    return Image.open(j[0]), d
def render(p):
    fs = {dpi: os.path.join(R, f'kort-oversigt-p{p}-{dpi}.png') for dpi in (300, 200)}
    if not all(os.path.exists(f) for f in fs.values()):
        im, d = source(p); g = im.convert('L')
        for dpi, f in fs.items():
            g.resize((round(g.width * dpi / 400), round(g.height * dpi / 400)), Image.LANCZOS).save(f + '.tmp.png'); os.replace(f + '.tmp.png', f)
        if d:
            for x in glob.glob(os.path.join(d, '*')): os.remove(x)
            os.rmdir(d)
    return fs[300]
def one(p):
    if time.time() - T0 > LIMIT: return 0
    img = render(p)
    r = subprocess.run(['tesseract', img, 'stdout', '-l', 'dan', '--dpi', '300', '-c', 'tessedit_create_tsv=1'], capture_output=True, text=True, env=env)
    if r.returncode or not r.stdout.startswith('level'): print('page', p, 'failed', r.stderr[-200:]); return 0
    t = os.path.join(O, f'p{p}.tsv')
    open(t + '.tmp', 'w', encoding='utf-8').write(r.stdout); os.replace(t + '.tmp', t)
    return 1
todo = [p for p in C.PAGES if not os.path.exists(os.path.join(O, f'p{p}.tsv'))]
with cf.ThreadPoolExecutor(int(os.environ.get("WORKERS", 4))) as ex: n = sum(ex.map(one, todo))
left = len([p for p in C.PAGES if not os.path.exists(os.path.join(O, f'p{p}.tsv'))])
print(f'OCR {n} pages in {time.time() - T0:.0f} s; {left} left' + ('' if left else '; done'))
