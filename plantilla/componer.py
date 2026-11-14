# Uso: componer.py plano.png fondo.png salida.png [escala]
import sys
from PIL import Image, ImageChops, ImageFilter, ImageDraw
plano,fondo,salida=sys.argv[1:4]; esc=float(sys.argv[4]) if len(sys.argv)>4 else 0.82
W=H=1200
im=Image.open(plano).convert("RGB")
bgc=Image.new("RGB",im.size,(14,16,20))
diff=ImageChops.difference(im,bgc).convert("L").point(lambda v:255 if v>12 else 0)
x0,y0,x1,y1=diff.getbbox()
card=im.crop((x0,y0,x1,y1))
cw,ch=int(card.width*esc),int(card.height*esc)
card=card.resize((cw,ch),Image.LANCZOS)
# rounded mask
m=Image.new("L",(cw,ch),0); ImageDraw.Draw(m).rounded_rectangle([0,0,cw-1,ch-1],radius=int(28*esc),fill=255)
bg=Image.open(fondo).convert("RGB").resize((W,H),Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.5))
px,py=(W-cw)//2,(H-ch)//2
sh=Image.new("L",(W,H),0); ImageDraw.Draw(sh).rounded_rectangle([px,py+16,px+cw,py+ch+16],radius=30,fill=180)
sh=sh.filter(ImageFilter.GaussianBlur(24))
bg.paste(Image.new("RGB",(W,H),"black"),(0,0),sh)
bg.paste(card,(px,py),m)
bg.save(salida); print(salida)
