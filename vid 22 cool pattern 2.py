from turtle import *
from colorsys import *

bgcolor("black")
x = 1
hue = 0
tracer(5)
width(2)
ht()

for i in range(360):
	color(hsv_to_rgb(hue, 1, 1))
	pd()
	rt(x)
	fd(200)
	rt(30)
	fd(120)
	rt(30)
	fd(60)
	pu()
	home()
	hue += 0.0027
	x += 1

done()
