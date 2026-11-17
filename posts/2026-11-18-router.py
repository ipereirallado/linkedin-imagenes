import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__file__),'..','plantilla'))
from pantalla import *
# Post del 18/11/2026: el rúter nuevo que saturó la red de control aéreo.
c=Canvas()
c.card(60,120,1140,1030)
c.text((100,160),"Monitor de red","b",40)
c.d.ellipse([R(100),R(224),R(114),R(238)],fill=RED)
c.text((126,231),"Red de control · en directo","r",24,SUB,"lm")
hdr_y=285
c.text((100,hdr_y),"EQUIPO","sb",19,MUT); c.text((540,hdr_y),"ACTIVIDAD","sb",19,MUT); c.text((1100,hdr_y),"ESTADO","sb",19,MUT,"ra")
AMB_T="#3a2d12"; RED_T="#3a1a1c"
rows=[("rúter-nuevo-01","Instalado hoy · fibra","1.000 llamadas cada 5 s","Muy hablador",AMB,AMB_T),
      ("rúter-norte-02","Cobre · desde 2009","Contestando al nuevo","Saturado",RED,RED_T),
      ("rúter-sur-03","Cobre · desde 2011","Contestando al nuevo","Saturado",RED,RED_T),
      ("rúter-este-04","Cobre · desde 2008","Contestando al nuevo","Saturado",RED,RED_T),
      ("rúter-oeste-05","Cobre · desde 2012","Contestando al nuevo","Saturado",RED,RED_T)]
y=320; rh=112
for i,(name,sub,act,est,col,tint) in enumerate(rows):
    if i==0:
        c.rect(84,y+6,1116,y+rh-6,"#1f1c16",r=16,outline=AMB,width=3)
    elif i>1:
        c.line(100,y,1100,y)
    # icono del equipo: caja con tres luces
    c.rect(100,y+36,150,y+76,"#2b3040",r=8)
    for k in range(3):
        cx=112+k*13
        c.d.ellipse([R(cx-4),R(y+52),R(cx+4),R(y+60)],fill=col if k==0 else "#5b6270")
    c.text((172,y+30),name,"sb",27,TXT)
    c.text((172,y+68),sub,"r",21,SUB)
    c.text((540,y+56),act,"m",23,AMB if i==0 else TXT,"lm")
    pw=c.tw(est,"sb",22)+40
    c.rect(1100-pw,y+36,1100,y+76,tint,r=20)
    c.text((1100-pw/2,y+56),est,"sb",22,col,"mm")
    y+=rh
c.line(100,y,1100,y)
c.rect(100,y+28,1100,y+108,"#14171c",r=14,outline=LINE,width=2)
c.text((130,y+68),"Despegues autorizados","sb",28,TXT,"lm")
c.text((1070,y+68),"0","b",40,RED,"rm")
c.save(sys.argv[1])
