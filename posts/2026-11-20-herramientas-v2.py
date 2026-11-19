import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__file__),'..','plantilla'))
from pantalla import *
# Post del 20/11/2026: "Haz la prueba con las herramientas que pagas". v2: importes en rojo y en negativo, total más grande.
c=Canvas()
c.card(60,95,1140,1078)
c.text((100,135),"Suscripciones del área","b",40)
c.text((100,190),"Se renuevan solas el día 1 de cada mes","r",24,SUB)
hdr_y=250
c.text((100,hdr_y),"HERRAMIENTA","sb",19,MUT); c.text((650,hdr_y),"ÚLTIMO USO","sb",19,MUT); c.text((1100,hdr_y),"€/MES","sb",19,MUT,"ra")
# nombre, detalle, color del detalle, uso, color del uso, precio, resaltada
rows=[("Firma electrónica","Contratos y pedidos",SUB,"Ayer",GRN,"85",False),
      ("Gestor de proyectos Pro","Para el proyecto de la web, ya cerrado",SUB,"Hace 8 meses",AMB,"120",False),
      ("Licencia de diseño","Usuario: dado de baja en marzo",SUB,"Hace 7 meses",AMB,"32",False),
      ("Plataforma de sinergias","Pedida por: —",AMB,"Nunca",RED,"19",True),
      ("Videollamadas","Todo el equipo",SUB,"Hoy",GRN,"60",False)]
y=290; rh=118
for name,sub,subcol,use,col,price,hl in rows:
    if hl:
        c.rect(84,y+6,1116,y+rh-6,"#2a2418",r=14,outline=AMB,width=2)
    else:
        c.line(100,y,1100,y)
    c.d.ellipse([R(100),R(y+37),R(144),R(y+81)],fill="#2b3040")
    c.text((122,y+59),name[0],"sb",22,"#aab1bd","mm")
    c.text((165,y+30),name,"sb",27,TXT)
    c.text((165,y+70),sub,"r",22,subcol)
    c.d.ellipse([R(650),R(y+52),R(664),R(y+66)],fill=col)
    c.text((676,y+59),use,"m",24,TXT,"lm")
    c.text((1100,y+59),"−"+price+" €","sb",28,RED,"rm")
    y+=rh
c.line(100,y,1100,y)
c.rect(100,y+25,1100,y+125,"#14171c",r=14,outline=LINE,width=2)
c.text((130,y+75),"Total al mes","sb",30,TXT,"lm")
c.text((1070,y+75),"−316 €","b",54,RED,"rm")
c.text((600,y+165),"En uso de verdad: 2 de 5","m",24,AMB,"mm")
c.save(sys.argv[1])
