import sys
from pantalla import *
c=Canvas()
c.card(60,110,1140,1090)
c.d.ellipse([R(100),R(142),R(118),R(160)],fill="#ff5f57"); c.d.ellipse([R(128),R(142),R(146),R(160)],fill="#febc2e"); c.d.ellipse([R(156),R(142),R(174),R(160)],fill="#28c840")
c.text((600,151),"Proyectos · Operaciones","sb",26,TXT,"mm")
c.line(60,185,1140,185)
c.text((100,222),"Plan para el pico de diciembre","b",44,TXT)
c.text((100,290),"Volumen previsto: el triple (se sabe desde enero)","m",27,SUB)
c.line(60,345,1140,345)
c.text((100,375),"Tarea","sb",22,MUT)
c.text((1100,375),"Estado","sb",22,MUT,"ra")
rows=[("Reforzar el equipo esas semanas","Sin definir","n"),
      ("Ver qué proceso no aguanta el triple","Pendiente","n"),
      ("Plan B si falla \"el Excel de los pedidos\"","Pendiente","n"),
      ("Quedarnos hasta las 22:00","Confirmado","z")]
y=420; rh=118
for t,st,k in rows:
    if k=="z":
        c.rect(84,y+8,1116,y+rh-8,"#3a3220",r=14,outline=AMB,width=2)
        tc="#f3e3c3"; pf="#1f3a2c"; pc=GRN; po=GRN
    else:
        tc=TXT; pf="#262a32"; pc=SUB; po=LINE
    c.text((110,y+rh/2),t,"sb" if k=="z" else "m",29,tc,"lm")
    pw=c.tw(st,"sb",24)+40
    c.rect(1090-pw,y+rh/2-25,1090,y+rh/2+25,pf,r=25,outline=po,width=2)
    c.text((1090-pw/2,y+rh/2),st,"sb",24,pc,"mm")
    if k!="z": c.line(84,y+rh,1116,y+rh,LINE,1)
    y+=rh
c.text((100,y+50),"Avance del plan","m",24,SUB)
c.rect(100,y+90,1100,y+112,"#262a32",r=11)
c.rect(100,y+90,350,y+112,AMB,r=11)
c.text((1100,y+50),"1 de 4","sb",24,SUB,"ra")
c.save(sys.argv[1])
