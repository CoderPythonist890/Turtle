from turtle import *
from random import uniform


def draw_square(x, y, size, tilt_angle, c):
	pu()
	goto(x, y)
	pd()
	seth(tilt_angle)
	fillcolor(c)
	begin_fill()
	for i in range(4):
		fd(size)
		lt(90)
	end_fill()

bgcolor("black")
tracer(10)
ht()
angle = 0
size = 280

while size > 0:
	draw_square(0, 0, size, angle, (uniform(0, 1), uniform(0, 1), uniform(0, 1)))
	size -= 0.1
	angle += 3

done()
