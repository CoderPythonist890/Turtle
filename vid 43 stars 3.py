from turtle import *
from colorsys import *

ht()
speed(0)
bgcolor('black')
delay(0)
width(2)

h = 0.5

for i in range(300):
	c = hsv_to_rgb(h, 1, 1)
	color(c)
	h += 0.005
	rt(20)

	for j in range(5):
		fd(i)
		rt(20 * 5)
		rt(40)
	rt(120)

done()
