from turtle import *

def r(length, angle=120):
	right(angle)
	forward(length * cm)

def l(length, angle=120):
	left(angle)
	forward(length * cm)

cm = 50

ht()
pensize(3)
bgcolor("#339EFF")

penup()
l(1, 180)
pendown()

fillcolor('red')
begin_fill()
forward(cm)
r(5)
r(7)
r(1)
r(5, 60)
l(3)
l(2)
end_fill()

fillcolor('lime')
begin_fill()
r(1, 60)
r(5)
l(1)
l(6, 60)
l(5)
l(1)
l(3, 60)
end_fill()

fillcolor('blue')
begin_fill()
r(5)
r(6)
r(1, 60)
r(5)
l(3)
end_fill()
done()
