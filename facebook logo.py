from turtle import *

def l(y,x):
	lt(y)
	fd(x)

def r(y,x):
	rt(y)
	fd(x)

color("#4267b2")
width(3)
ht()
begin_fill()
circle(140,360)
end_fill()

rt(7)
bk(32)
color("white")

begin_fill()
l(97,98)
l(90,40)
r(90,40)
r(90,40)
l(90,34)
circle(-45,90)
fd(40)
r(90,40)
r(90,20)
circle(17,90)
fd(23)
l(90,40)
r(100,40)
r(80,30)
l(90,110)
r(90,50)
end_fill()

done()