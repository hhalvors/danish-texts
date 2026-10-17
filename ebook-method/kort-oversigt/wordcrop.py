#!/usr/bin/env python3
"""ebook-method/kort-oversigt/wordcrop.py OUT.png PAGE:WORD [PAGE:WORD ...] -- one small sheet of line crops, each
the printed line round the first layer word on that page that starts with WORD (600 dpi, boxed), for reading a few
doubtful words at the image."""
import os, re, sys, html, subprocess
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import pagemap as C
out = sys.argv[1]; crops = []; WC = f'/tmp/wc-{os.getpid()}'   # own name: a stale /tmp/wc.png of another user blocks pdftoppm
for arg in sys.argv[2:]:
    p, w = arg.split(':', 1); p = int(p); q = C.pdfpage(p); nth = int(w.split('#')[1]) if '#' in w else 1; w = w.split('#')[0]   # WORD#2 = the second occurrence
    x = subprocess.run(['pdftotext', '-bbox', '-f', str(q), '-l', str(q), C.scan_path(), '-'], capture_output=True, text=True).stdout
    ws = [(html.unescape(t[4]), tuple(map(float, t[:4]))) for t in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', x)]
    hits = [b for t, b in ws if t.startswith(w)]; hit = hits[nth - 1] if len(hits) >= nth else None
    if not hit: print('not found', arg); continue
    d = 600; s = d / 72
    subprocess.run(['pdftoppm', '-r', str(d), '-gray', '-png', '-singlefile', '-f', str(q), '-l', str(q), '-x', '0', '-y', str(int((hit[1] - 14) * s)), '-W', str(int(380 * s)), '-H', str(int(38 * s)), C.scan_path(), WC], check=True)
    im = Image.open(WC + '.png').convert('RGB'); dr = ImageDraw.Draw(im)
    dr.rectangle((int(hit[0] * s) - 4, int(14 * s) - 4, int(hit[2] * s) + 4, int((14 + hit[3] - hit[1]) * s) + 4), outline=(220, 0, 0), width=3)
    dr.text((10, 5), arg, fill=(0, 0, 255)); crops.append(im.resize((im.width // 2, im.height // 2)))
sh = Image.new('RGB', (max(c.width for c in crops), sum(c.height + 6 for c in crops)), (160, 160, 160)); y = 0
for c in crops: sh.paste(c, (0, y)); y += c.height + 6
sh.save(out); print('wrote', out, len(crops))
