from turtle import *

#choose colors :
colors = ["deeppink", "gold", "cyan", "orange"]
bgcolor("black")

r=[350,350]
s=1,4
turtles = [Turtle(), Turtle()]

for index,i in enumerate(turtles):
	i.speed(0)
	i.color("white")
	i.shape("circle")
	i.shapesize(0.3)
	i.width(3)
	i.pu()
	i.seth(90)
	i.fd(r[index])
	i.seth(180)
	i.pd()

turtles[0].pu()
tracer(30)
speed(0)
ht()

for i in colors:
	color(i)
	for i in range(360//min(s)):
		for i in range(s[0]):
			turtles[0].fd(1.75*r[0]/100)
			turtles[0].lt(1)
			pu()
			goto(turtles[0].pos())
			pd()
		for i in range(s[1]):
			turtles[1].fd(1.75*r[1]/100)
			turtles[1].lt(1)
		goto(turtles[1].pos())

done()
