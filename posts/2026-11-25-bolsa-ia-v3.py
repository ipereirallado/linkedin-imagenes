import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__file__),'..','plantilla'))
from pantalla import *
from PIL import Image as _I, ImageDraw as _D
# Post del 25/11/2026 (v3, mezcla de v1 y v2): ficha del proyecto de IA con el ánimo del mercado de la semana.
# Todo en verde menos para qué sirve; el mercado, en rojo toda la semana y rebote el lunes.
c=Canvas()
c.card(60,60,1140,1108)
# cabecera
c.rect(105,95,161,151,"#2b3040",r=14)
for i in range(3):
    c.rect(119,111+i*13,147,117+i*13,"#c9ced6",r=3)
c.text((182,93),"Proyectos","b",32)
c.text((182,135),"Ficha del proyecto","r",22,SUB)
c.line(60,180,1140,180)
# título
c.text((105,205),"Asistente de IA para todo","b",40)
c.rect(105,265,255,305,"#16352a",r=20)
c.text((180,285),"En curso","sb",22,GRN,"mm")
c.text((275,285),"Lanzamiento: enero","m",22,SUB,"lm")

# panel del mercado
bx0,by0,bx1,by1=105,325,1095,620
c.rect(bx0,by0,bx1,by1,"#1e2128",r=16,outline=LINE,width=1)
c.text((bx0+30,by0+24),"Ánimo del mercado con la IA","sb",25,TXT)
c.rect(bx1-220,by0+20,bx1-30,by0+58,"#3a1d20",r=19)
c.text((bx1-125,by0+39),"▼ Esta semana","sb",21,RED,"mm")
gx0,gx1,gy0,gy1=bx0+60,bx1-60,by0+80,by1-50
days=["Lun","Mar","Mié","Jue","Vie","Lun"]
vals=[0.0,0.12,0.22,0.48,1.0,0.5]
step=(gx1-gx0)/5
pts=[(gx0+i*step, gy0+v*(gy1-gy0)) for i,v in enumerate(vals)]
over=_I.new("RGBA",c.img.size,(0,0,0,0)); od=_D.Draw(over)
od.polygon([(R(x),R(y)) for x,y in pts[:5]]+[(R(pts[4][0]),R(gy1+8)),(R(pts[0][0]),R(gy1+8))],fill=(229,72,77,45))
od.polygon([(R(pts[4][0]),R(pts[4][1])),(R(pts[5][0]),R(pts[5][1])),(R(pts[5][0]),R(gy1+8)),(R(pts[4][0]),R(gy1+8))],fill=(61,214,140,40))
c.img.paste(over,(0,0),over); c.d=ImageDraw.Draw(c.img)
for i in range(4): c.line(pts[i][0],pts[i][1],pts[i+1][0],pts[i+1][1],RED,5)
c.line(pts[4][0],pts[4][1],pts[5][0],pts[5][1],GRN,5)
for x,y in pts[:5]: c.d.ellipse([R(x-7),R(y-7),R(x+7),R(y+7)],fill=RED)
x,y=pts[5]; c.d.ellipse([R(x-9),R(y-9),R(x+9),R(y+9)],fill=GRN)
for i,d in enumerate(days):
    c.text((gx0+i*step,by1-22),d,"m",20,GRN if i==5 else SUB,"mm")

# filas
rows=[("Presupuesto","Aprobado",GRN),
      ("Proveedor","Elegido",GRN),
      ("Modelo de IA","El más nuevo",GRN),
      ("Presentación","42 diapositivas",GRN),
      ("Problema que resuelve","Pendiente de definir",AMB)]
y=640
for lab,val,col in rows:
    hl=(col==AMB)
    c.rect(105,y,1095,y+76,"#232730" if hl else "#1e2128",r=16,outline=AMB if hl else LINE,width=3 if hl else 1)
    c.text((140,y+38),lab,"sb" if hl else "m",28,TXT if hl else SUB,"lm")
    if hl:
        c.text((1060,y+38),val,"sb",28,AMB,"rm")
    else:
        tw=c.tw(val,"sb",28)
        c.text((1060,y+38),val,"sb",28,TXT,"rm")
        cx=1060-tw-34; cy=y+38
        c.d.ellipse([R(cx-14),R(cy-14),R(cx+14),R(cy+14)],fill="#16352a")
        c.line(cx-7,cy+1,cx-2,cy+6,GRN,4); c.line(cx-2,cy+6,cx+8,cy-6,GRN,4)
    y+=88
c.save(sys.argv[1])
