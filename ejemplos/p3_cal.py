import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__file__),'..','plantilla'))
from pantalla import *
c=Canvas()
c.card(60,80,1140,1125)
c.text((100,125),"Calendario","b",40)
c.text((100,180),"Semana del 16 al 20 de noviembre","r",24,SUB)
days=["Lun 16","Mar 17","Mié 18","Jue 19","Vie 20"]
x0=170; x1=1100; cw=(x1-x0)/5
top=280; hour_h=76; hours=list(range(9,19))
for i,dname in enumerate(days):
    c.text((x0+cw*i+cw/2,245),dname,"sb",24,TXT,"mm")
for k,h in enumerate(hours):
    y=top+k*hour_h
    c.text((150,y),f"{h}:00","r",19,MUT,"ra")
    c.line(x0,y,x1,y,LINE,1)
for i in range(6): c.line(x0+cw*i,top,x0+cw*i,top+hour_h*len(hours),LINE,1)
def ev(day,start,dur,title,kind="n"):
    xa=x0+cw*day+6; xb=x0+cw*(day+1)-6
    ya=top+(start-9)*hour_h+4; yb=ya+dur*hour_h-8
    if kind=="z": fill="#3a3220"; out=AMB; tc="#f3e3c3"
    else: fill="#23324d"; out=None; tc="#cfe0ff"
    c.rect(xa,ya,xb,yb,fill,r=10,outline=out,width=2 if out else 0)
    lines=c.wrap(title,"m",19,xb-xa-20)
    for j,l in enumerate(lines[:3]):
        c.text((xa+10,ya+10+j*25),l,"m",19,tc)
evs=[(0,9,1,"Comité semanal"),(0,10.5,1,"Revisión de KPIs"),(0,12,1.5,"Seguimiento proyecto Alfa","z"),(0,15,1,"1:1 equipo"),(0,16.5,1,"Sincro ventas"),
     (1,9,1.5,"Planificación Q1"),(1,11,1,"Daily operaciones"),(1,13,1,"Comida con cliente"),(1,15.5,1.5,"Taller procesos"),
     (2,9,1,"Daily operaciones"),(2,10,1,"Revisión presupuesto"),(2,12,1.5,"Seguimiento proyecto Alfa","z"),(2,15,2,"Reunión para preparar la reunión"),
     (3,9,1,"Daily operaciones"),(3,10.5,1.5,"Comité de dirección"),(3,13,1,"Proveedor TI"),(3,16,1,"Formación"),
     (4,9,1,"Daily operaciones"),(4,10.5,1,"Cierre semanal"),(4,12,1.5,"Seguimiento proyecto Alfa","z"),(4,16,1,"Afterwork")]
for e in evs: ev(*e)
# note
c.rect(100,1052,1100,1100,"#3a3220",r=12,outline=AMB,width=2)
c.text((600,1076),"\"Seguimiento proyecto Alfa\": el proyecto acabó en junio","m",22,"#f3e3c3","mm")
c.save(sys.argv[1])
