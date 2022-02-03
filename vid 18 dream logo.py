from turtle import *

def l(y,x):
	lt(y)
	fd(x)

def r(y,x):
	rt(y)
	fd(x)

def gt(x,y):
	pu()
	goto(x,y)
	pd()


bgcolor("lime")
color("black","white")
shape("circle")
ht()
speed(1)
width(15)


gt(-365,-380)
begin_fill()
seth(90)
fd(20)
r(5,20)
r(4,60)
r(5,100)
r(5,120)
l(85,50)
r(10,25)
r(15,10)
r(15,40)
r(15,50)
r(10,90)
r(20,50)
r(20,25)
r(10,75)
r(30,20)
r(10,10)
l(30,50)
r(15,10)
r(10,20)
r(10,80)
r(10,40)
for _ in range(7):
	r(10,30)
r(10,80)
r(20,35)
l(30,150)
for _ in range(3):
	r(5,150)
end_fill()

gt(-290,-70)
l(90,30)
l(10,120)
l(15,60)
l(10,30)
l(5,40)
l(10,40)



gt(-320,50)
r(70,30)
l(10,30)
l(15,30)
l(5,60)
l(5,60)
l(15,40)
r(10,20)
l(20,35)

color("black")
gt(-50,170)
stamp()
gt(-340,135)
stamp()

gt(40,-115)
write("dream", font = ('Arial', 85, 'italic','bold'))

done()