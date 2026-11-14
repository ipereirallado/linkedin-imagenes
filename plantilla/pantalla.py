"""Ayudas de dibujo para las pantallas de los posts de LinkedIn de Iker (estilo 14/11/2026).
Se dibuja a 1200x1200 sobre fondo liso BG; luego componer.py pone la pantalla sobre el fondo de arboles."""
import math, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
# Fuentes: Inter. Si no está en esta ruta, se busca en el sistema con fc-list.
F=os.environ.get("INTER_DIR","/usr/share/fonts/opentype/inter/")
W=H=1200; S=2
BG="#0e1014"; CARD="#1a1d23"; LINE="#2a2e36"; TXT="#eceef2"; SUB="#9aa1ad"; MUT="#6b7280"
RED="#e5484d"; AMB="#f5a524"; GRN="#3dd68c"; BLU="#3b82f6"
def font(w,s): return ImageFont.truetype(F+{"b":"Inter-Bold.otf","sb":"Inter-SemiBold.otf","m":"Inter-Medium.otf","r":"Inter-Regular.otf"}[w],int(s*S))
def R(v): return int(v*S)
class Canvas:
    def __init__(s):
        s.img=Image.new("RGB",(W*S,H*S),BG)
        s.d=ImageDraw.Draw(s.img)
    def card(s,x0,y0,x1,y1,fill=CARD,r=28,outline=LINE):
        s.d.rounded_rectangle([R(x0),R(y0),R(x1),R(y1)],radius=R(r),fill=fill,outline=outline,width=R(2))
    def text(s,xy,t,w="r",size=26,fill=TXT,anchor="la"):
        s.d.text((R(xy[0]),R(xy[1])),t,font=font(w,size),fill=fill,anchor=anchor)
    def tw(s,t,w,size): return s.d.textlength(t,font=font(w,size))/S
    def rect(s,x0,y0,x1,y1,fill,r=0,outline=None,width=0):
        s.d.rounded_rectangle([R(x0),R(y0),R(x1),R(y1)],radius=R(r),fill=fill,outline=outline,width=R(width) if width else 0)
    def line(s,x0,y0,x1,y1,fill=LINE,width=2):
        s.d.line([R(x0),R(y0),R(x1),R(y1)],fill=fill,width=R(width))
    def wrap(s,t,w,size,maxw):
        words=t.split(); lines=[]; cur=""
        for wd in words:
            test=(cur+" "+wd).strip()
            if s.tw(test,w,size)<=maxw: cur=test
            else: lines.append(cur); cur=wd
        if cur: lines.append(cur)
        return lines
    def save(s,path):
        s.img.resize((W,H),Image.LANCZOS).save(path); print(path)
