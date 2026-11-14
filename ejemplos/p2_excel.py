import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__file__),'..','plantilla'))
from pantalla import *
c=Canvas()
c.card(60,90,1140,1110)
# title bar
c.d.ellipse([R(100),R(122),R(118),R(140)],fill="#ff5f57"); c.d.ellipse([R(128),R(122),R(146),R(140)],fill="#febc2e"); c.d.ellipse([R(156),R(122),R(174),R(140)],fill="#28c840")
c.text((600,131),"informe_definitivo_v7_BUENO.xlsx","sb",26,TXT,"mm")
c.line(60,165,1140,165)
# formula bar
c.rect(100,185,1100,235,"#14171c",r=10,outline=LINE,width=2)
c.text((120,210),"fx","b",22,MUT,"lm")
c.text((170,210),"=SI(ESERROR(BUSCARV(B7;'Datos (2)'!A:Z;14;0));Hoja37!C4*1,21;0)","r",22,SUB,"lm")
# grid
cols=["","A","B","C","D","E"]; xs=[100,160,330,560,760,930,1100]
gy0=255; rh=58
rows=[["1","Cliente","Mes","Importe","Ajuste","Total"],
      ["2","Cliente 01","Octubre","12.480","-310","12.170"],
      ["3","Cliente 02","Octubre","8.920","0","8.920"],
      ["4","Cliente 03","Octubre","15.300","#¡REF!","#¡REF!"],
      ["5","Cliente 04","Octubre","4.110","+95 (?)","4.205"],
      ["6","Cliente 05","Octubre","9.760","—","9.760"],
      ["7","TOTAL","","","","#¡REF!"]]
# header row letters
for i in range(6):
    c.rect(xs[i],gy0,xs[i+1],gy0+44,"#22262e")
    c.text(((xs[i]+xs[i+1])/2,gy0+22),cols[i],"sb",20,MUT,"mm")
y=gy0+44
for r,row in enumerate(rows):
    for i in range(6):
        fill="#22262e" if i==0 else ("#1f2329" if r==0 else CARD)
        c.rect(xs[i],y,xs[i+1],y+rh,fill)
        t=row[i]; col=TXT
        w="sb" if r==0 or row[1]=="TOTAL" else "r"
        if "#¡REF!" in t: col=RED; w="sb"
        if "(?)" in t: col=AMB
        if i==0: col=MUT
        c.text(((xs[i]+xs[i+1])/2 if i==0 else xs[i]+16, y+rh/2),t,w,22,col,"mm" if i==0 else "lm")
    y+=rh
for x in xs: c.line(x,gy0,x,y,LINE,1)
for k in range(len(rows)+2): 
    yy=gy0+44+k*rh if k>0 else gy0
    c.line(xs[0],min(yy,y),xs[-1],min(yy,y),LINE,1)
# sticky comment
c.rect(590,745,1100,880,"#3a3220",r=10,outline=AMB,width=2)
c.text((614,765),"Comentario","sb",20,AMB)
for i,l in enumerate(["NO TOCAR. La fórmula de la columna E","la entiende solo quien la hizo."]):
    c.text((614,800+i*32),l,"r",22,"#f3e3c3")
# tabs
ty=1030
c.line(60,ty-20,1140,ty-20)
tabs=["Datos","Datos (2)","Datos OK","NO TOCAR","Hoja37","Copia de Copia"]
x=100
for i,t in enumerate(tabs):
    w=c.tw(t,"m",21)+36
    active=(i==1)
    c.rect(x,ty,x+w,ty+46,"#262a32" if active else "#14171c",r=8,outline=LINE,width=1)
    c.text((x+w/2,ty+23),t,"m",21,TXT if active else SUB,"mm")
    x+=w+10
c.text((x+14,ty+23),"+","b",28,MUT,"lm")
c.save(sys.argv[1])
