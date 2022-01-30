from turtle import *
from colorsys import *

speed(0)
hue = 0.9
bgcolor("black")
hideturtle()

for i in range(182):
	col = hsv_to_rgb(hue, 1, 1)
	hue += 0.005
	color(col, col)
	begin_fill()
	circle(190 - i, 100)
	lt(90)
	circle(190 - i, 100)
	end_fill()

done()
