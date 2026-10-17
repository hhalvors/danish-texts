#!/usr/bin/env python3
"""ebook-method/den-store-humor/notecrops.py -- reading sheets of the footnote areas, for reading every note at the
image (TRANSCRIPTION-PLAYBOOK §00, Den store Humor lessons).  For each page: find the footnote rule (a solid run of
300-1000 px with blank rows above and below, below 30% of the page), crop from it to the last text line of the
tesseract witness (+EXTRA px), scale to 1500 px wide, and stack the crops ~2400 px per sheet, each labelled PAGE N.

    python3 ebook-method/den-store-humor/notecrops.py 9,10,13 a [EXTRA]
        -> texts/hoeffding/den-store-humor/.render/nc-a00.png, nc-a01.png, ...   (.render is gitignored)
Needs the 300 dpi renders (.render/den-store-humor-pN-300.png) and the witness (.parts/collate/ocr/pN.tsv);
numpy and Pillow.  "norule N": no rule found (a note-less page, or a page whose text runs to the foot); the crop
then starts at 60% of the page.
"""
import csv,sys,re,os
import numpy as np
from PIL import Image,ImageDraw
HERE=os.path.dirname(os.path.abspath(__file__)); D=os.path.join(os.path.dirname(os.path.dirname(HERE)),'texts','hoeffding','den-store-humor')+'/'
pages=[int(x) for x in sys.argv[1].split(',')]
out=[]
def runs(row):
    best=cur=0
    for v in row:
        cur=cur+1 if v else 0; best=max(best,cur)
    return best
for p in pages:
    L={}
    for r in csv.DictReader(open(D+f'.parts/collate/ocr/p{p}.tsv'),delimiter='\t',quoting=csv.QUOTE_NONE):
        if r['level']!='5' or not r['text'].strip(): continue
        k=(r['block_num'],r['par_num'],r['line_num'])
        L.setdefault(k,[]).append((int(r['left']),int(r['top']),int(r['width']),int(r['height']),r['text']))
    lines=[]
    for k,w in L.items():
        t=' '.join(x[4] for x in w)
        if len(w)<2 or re.search(r'Den store Humor|HUMOR|HØFFDING|FFDING',t): continue
        lines.append((min(x[1] for x in w),max(x[1]+x[3] for x in w),min(x[0] for x in w),max(x[0]+x[2] for x in w)))
    x0=int(np.median([l[2] for l in lines]))-60; x1=int(np.median([l[3] for l in lines]))+60
    im=Image.open(D+f'.render/den-store-humor-p{p}-300.png').convert('L')
    a=np.array(im)[:,x0:x1]<128
    H=a.shape[0]; rule=None
    cnt=a.sum(1)
    for y in range(int(H*0.3),H-50):
        if 300<=cnt[y]<1000 and cnt[y-14]<80 and cnt[y+14]<80:
            r=a[y].astype(int); d=np.diff(np.concatenate([[0],r,[0]])); st_=np.where(d==1)[0]; en=np.where(d==-1)[0]; m=(en-st_).max()
            if m>=300 and cnt[y]-m<60: rule=y; break
    if rule is None: print('norule',p); rule=int(H*0.6)
    below=[l for l in lines if l[0]>rule]
    bot=max([l[1] for l in below],default=rule+600)+int(sys.argv[3]) if len(sys.argv)>3 else max([l[1] for l in below],default=rule+600)
    c=im.crop((x0,rule-20,x1,bot+25))
    s=1500/c.width; c=c.resize((1500,int(c.height*s)))
    out.append((p,c))
grp=[];h=0;n=0
def flush():
    global grp,h,n
    if not grp: return
    M=Image.new('L',(1500,sum(c.height+40 for _,c in grp)),255);y=0;d=ImageDraw.Draw(M)
    for p,c in grp:
        d.rectangle((0,y,1500,y+38),fill=200);d.text((10,y+10),f'PAGE {p}',fill=0);y+=40;M.paste(c,(0,y));y+=c.height
    M.save(D+f'.render/nc-{sys.argv[2]}{n:02d}.png');n+=1;grp=[];h=0
for p,c in out:
    if h+c.height>2400: flush()
    grp.append((p,c));h+=c.height+40
flush()
