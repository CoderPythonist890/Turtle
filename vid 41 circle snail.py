from turtle import *
from colorsys import *

x = 0
bgcolor("black")

# width(2)
speed(0)
hideturtle()
for i in range(100):
	color(hsv_to_rgb(0.6, x, 1))
	circle(i * 2)
	lt(5)
	x += 0.01

done()
