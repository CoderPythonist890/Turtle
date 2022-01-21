from turtle import *

def r(angle, length=1):
	right(angle)
	forward(length * cm)

def l(angle, length=1):
	left(angle)
	forward(length * cm)

cm = 50
pensize(3)
getscreen().bgcolor("#339EFF")

penup()
l(180)
pendown()

color("black", 'red')
begin_fill()
forward(cm)
r(120, 5)
r(120, 7)
r(120)
r(60, 5)
l(120, 3)
l(120, 2)
end_fill()

color("black", 'lime')
begin_fill()
r(60, 1)
r(120, 5)
l(120, 1)
l(60, 6)
l(120, 5)
l(120, 1)
l(60, 3)
end_fill()

color("black", 'blue')
begin_fill()
r(120, 5)
r(120, 6)
r(60)
r(120, 5)
l(120, 3)
end_fill()
done()
