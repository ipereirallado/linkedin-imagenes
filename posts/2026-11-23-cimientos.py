import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__file__),'..','plantilla'))
from pantalla import *
# Post del 23/11/2026: "Nadie construiría un ático de lujo encima de un garaje con goteras".
# Si le das desorden, devuelve desorden. Eso sí, muy bien redactado.
c=Canvas()
c.card(60,70,1140,1070)
# cabecera
c.d.ellipse([R(105),R(105),R(161),R(161)],fill="#2b3040")
cx,cy=133,133; pts=[]
for i in range(8):
    a=math.radians(i*45-90); r=18 if i%2==0 else 6
    pts.append((R(cx+r*math.cos(a)),R(cy+r*math.sin(a))))
c.d.polygon(pts,fill="#c9ced6")
c.text((180,108),"Asistente de IA","b",32)
c.text((180,148),"Conectado a 3 fuentes de datos","r",22,GRN)
c.line(60,195,1140,195)

def bubble(who,t,y,hl=False,size=28):
    lines=c.wrap(t,"r",size,640)
    h=len(lines)*40+36
    wbox=max(c.tw(l,"r",size) for l in lines)+48
    if who=="u": x1=1100; x0=x1-wbox; fill=BLU; col="#ffffff"
    else: x0=100; x1=x0+wbox; fill="#262a32"; col=TXT
    c.rect(x0,y,x1,y+h,fill,r=24,outline=AMB if hl else None,width=3 if hl else 0)
    for i,l in enumerate(lines): c.text((x0+24,y+18+i*40),l,"r",size,col)
    return y+h+24

y=bubble("u","¿Cuánto hemos facturado en octubre?",230)
# respuesta con las tres fuentes
x0,x1=100,920; h=330
c.rect(x0,y,x1,y+h,"#262a32",r=24)
c.text((x0+24,y+22),"He consultado las tres fuentes:","r",28,TXT)
rows=[("Pedidos","48.000 €",TXT),("Contabilidad","52.000 €",TXT),("cierre_mes_2014_DEFINITIVO.xlsx","",None)]
yy=y+82
for i,(src,val,col) in enumerate(rows):
    c.rect(x0+24,yy,x1-24,yy+68,"#1c1f25",r=12,outline=LINE,width=1)
    c.text((x0+48,yy+34),src,"m",25,SUB,"lm")
    if col: c.text((x1-48,yy+34),val,"sb",27,col,"rm")
    else: c.text((x1-48,yy+34),"#¡REF!","sb",27,RED,"rm")
    yy+=80
y=y+h+24
y=bubble("a","En resumen: ha sido un mes excelente, con una facturación de entre 48.000 € y #¡REF!.",y,hl=True)
y=bubble("a","¿Quieres que lo presente al comité con un gráfico?",y)
# caja de escribir
c.rect(100,985,1100,1045,"#14171c",r=30,outline=LINE,width=2)
c.text((130,1002),"Escribe un mensaje…","r",24,MUT)
c.save(sys.argv[1])
