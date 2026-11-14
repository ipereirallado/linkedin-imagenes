import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__file__),'..','plantilla'))
from pantalla import *
c=Canvas()
c.card(60,110,1140,1090)
c.text((100,150),"Suscripciones del área","b",40)
c.text((100,205),"Se renuevan automáticamente cada mes","r",24,SUB)
hdr_y=265
c.text((100,hdr_y),"HERRAMIENTA","sb",19,MUT); c.text((640,hdr_y),"USO","sb",19,MUT); c.text((1100,hdr_y),"€/MES","sb",19,MUT,"ra")
rows=[("Encuestas online","Proyecto de 2024","Último uso: hace 214 días",AMB,"49"),
      ("Gestor de proyectos","30 licencias","4 usuarios activos",AMB,"360"),
      ("Pizarra colaborativa","La pidió alguien que ya no está","Último uso: nunca",RED,"12"),
      ("Firma electrónica","Contratos y pedidos","Último uso: ayer",GRN,"85"),
      ("Editor de vídeo","Para un evento","Último uso: hace 1 año",AMB,"29"),
      ("Herramienta de informes","Nadie recuerda pedirla","Último uso: nunca",RED,"64")]
y=305; rh=110
for name,sub,use,col,price in rows:
    c.line(100,y,1100,y)
    c.d.ellipse([R(100),R(y+33),R(144),R(y+77)],fill="#2b3040")
    c.text((122,y+55),name[0],"sb",22,"#aab1bd","mm")
    c.text((165,y+28),name,"sb",27,TXT)
    c.text((165,y+66),sub,"r",22,SUB)
    c.d.ellipse([R(640),R(y+48),R(654),R(y+62)],fill=col)
    c.text((666,y+55),use,"m",23,TXT,"lm")
    c.text((1100,y+55),price+" €","sb",27,TXT,"rm")
    y+=rh
c.line(100,y,1100,y)
c.rect(100,y+25,1100,y+95,"#14171c",r=14,outline=LINE,width=2)
c.text((130,y+60),"Total al mes","sb",27,TXT,"lm")
c.text((1070,y+60),"599 €","b",30,TXT,"rm")
c.save(sys.argv[1])
