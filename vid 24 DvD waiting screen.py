from turtle import *

def sc(x, y):
	t.speed(0)
	t.ht()
	t.color("red")
	t.pensize(3)
	t.pu()
	t.fd(x)
	t.lt(90)
	t.fd(y)
	t.lt(90)
	t.pd()
	t.fd(2 * x)
	t.lt(90)
	t.fd(2 * y)
	t.lt(90)
	t.fd(2 * x)
	t.lt(90)
	t.fd(2 * y)


MAX_X = 300
MAX_Y = 200
t = Turtle()

sc(MAX_X + 78, MAX_Y + 50)
# register_shape('dvd1.gif')
# shape('dvd1.gif')
bgcolor("black")
speed(0)
pu()
left(12)

while True:
	x = xcor()
	y = ycor()
	if abs(x) >= MAX_X:
		h = heading()
		setheading(180 - h)
	if abs(y) >= MAX_Y:
		h = heading()
		setheading(-h)
	fd(10)
