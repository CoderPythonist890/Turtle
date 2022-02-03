from turtle import *
from colorsys import *

hue = 0.8

bgcolor("black")
speed(0)

for i in range(264):
	col = hsv_to_rgb(hue, 1, 1)
	hue += 0.0005
	color(col, col)
	begin_fill()
	circle(270 - i, 90)
	lt(90)
	circle(270 - i, 90)
	lt(10)
	end_fill()

done()
