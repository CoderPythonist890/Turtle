from turtle import *

turtles = [Turtle() for i in range(3)]
x = 180
bgcolor("#1E0394")
color("#FF5F1F")
pensize(6)
ht()
pu()
fd(x)
seth(90)
pd()
circle(x, 360)
c = ["#FF7A1F", "#FF9C1F"]

for index, t in enumerate(turtles):
	t.ht()
	t.pensize(5)
	t.pu()
	t.fd(x)
	t.seth(90)
	t.circle(x, 120 * index)
	t.pd()
	t.color(c[0])
	t.circle((x * 2 / 3), 120)
	t.color(c[1])
	t.pensize(4)
	t.circle((x * 2 / 6) + 20, 126)

done()
