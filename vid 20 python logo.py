from turtle import *


def gt(x, y):
	penup()
	goto(x, y)
	pendown()


def c3():
	for i in range(90):
		right(1)
		forward(1)


def c1():
	circle(58, 90)


def c2(x=80):
	c1()
	forward(x)
	c1()


def h():
	begin_fill()
	forward(50)
	c1()
	forward(90)
	c2()
	forward(40)
	left(90)
	forward(80)
	right(90)
	forward(10)
	right(90)
	forward(120)
	c2(90)
	forward(30)
	left(90)
	forward(50)
	c3()
	forward(40)
	seth(180)
	end_fill()


def dots(x, y):
	pu()
	goto(x, y)
	dot(35)


color("#306998")
h()
gt(19.79, -11.21)
color("#FFD43B")
h()
color("white")
dots(-50, 150)
dots(70, -160)
done()
