from turtle import *
from math import *

bgcolor("black")
speed(5)
ht()

colors = ["#FF4858", "#72F2EB", "#747F7F"]
x, y, r = 0, -40, 400
direction = 90
c = 0

while r > 20:
	color(colors[c % len(colors)])
	pu()
	goto(x, y)
	seth(direction)
	fd(r)
	right(162)
	pd()
	length = r * sin(pi * 2 / 5) / (1 + sin(pi / 10))
	begin_fill()
	for _ in range(5):
		fd(length)
		left(72)
		fd(length)
		right(144)
	end_fill()
	direction += 180
	r = r * sin(pi / 10) / cos(pi / 5)
	c += 1

done()
