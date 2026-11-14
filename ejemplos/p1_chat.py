import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__file__),'..','plantilla'))
from pantalla import *
c=Canvas()
c.card(60,60,1140,1140)
# header
c.d.ellipse([R(105),R(100),R(161),R(156)],fill="#2b3040")
# sparkle
cx,cy=133,128
pts=[]
for i in range(8):
    a=math.radians(i*45-90); r=18 if i%2==0 else 6
    pts.append((R(cx+r*math.cos(a)),R(cy+r*math.sin(a))))
c.d.polygon(pts,fill="#c9ced6")
c.text((180,103),"Asistente de IA","b",32)
c.text((180,143),"En línea","r",22,GRN)
c.line(60,190,1140,190)
msgs=[("u","¿Este proyecto sale rentable?"),
      ("a","Con estos datos, no. Los costes superan al ahorro durante el primer año."),
      ("u","Revísalo. Yo creo que sí sale."),
      ("a","Lo he revisado y sigue sin salir: el ahorro no cubre la inversión hasta el segundo año."),
      ("u","Que sí, que sale. Revísalo otra vez."),
      ("a","Tienes razón, disculpa el error. El proyecto es rentable.")]
y=225; maxw=600
for who,t in msgs:
    lines=c.wrap(t,"r",27,maxw)
    h=len(lines)*38+34
    wbox=max(c.tw(l,"r",27) for l in lines)+44
    if who=="u":
        x1=1100; x0=x1-wbox; fill=BLU; col="#ffffff"
    else:
        x0=100; x1=x0+wbox; fill="#262a32"; col=TXT
    last = (who=="a" and t.startswith("Tienes razón"))
    c.rect(x0,y,x1,y+h,fill,r=24,outline=AMB if last else None,width=3 if last else 0)
    for i,l in enumerate(lines):
        c.text((x0+22,y+17+i*38),l,"r",27,col)
    y+=h+22
# input
c.rect(100,1040,1100,1100,"#14171c",r=30,outline=LINE,width=2)
c.text((130,1058),"Escribe un mensaje…","r",24,MUT)
c.save(sys.argv[1])
