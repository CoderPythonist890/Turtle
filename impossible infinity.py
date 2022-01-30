from turtle import *


def l(x,y=120):
	lt(y)
	fd(x*cm)

def r(x,y=120,c=0):
	rt(y)
	fd(x*cm-c)

c=["blue","yellow"]
cm=50

ht()
width(2)
pu()
bk(3*cm)
pd()

fillcolor(c[0])
begin_fill()
l(2,90)
p4=pos()
r(8)
p1=pos()
l(5)
l(1,60)
l(4)
p2=pos()
y1=xcor()
r(8)
l(4)
l(1)
end_fill()

fillcolor(c[1])
begin_fill()
l(1,60)
r(7)
goto(p1[0],p1[1])
goto(p4)
end_fill()

pu()
goto(p2)
pd()
seth(90)

fillcolor(c[1])
begin_fill()
fd(4*cm)
l(8)
r(4)
l(1)
l(5,60)
p3=pos()
l(8)
p5=pos()
r(2)
end_fill()

fillcolor(c[0])
begin_fill()
bk(cm)
r(7,60)
goto(p3)
goto(p5)
end_fill()

done()