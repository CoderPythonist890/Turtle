from turtle import *


def curve():
	for i in range(200):
		right(1)
		forward(1)


# color
coefficient = (255 - 97) / 255
r, g, b = 255, 0, 97
colors = '#%02x%02x%02x' % (r, g, b)

delay(0)  # turtle speed [1(slow)-->10(fast)] 0(fastest)
speed(0)
bgcolor("black")
pensize(3)
color("#C90055", colors)
increment = 8

left(140)
heartsnumber = 100
for i in range(heartsnumber):
	g += increment
	b = int(round((b + increment * coefficient)))
	print(g, " ", b)
	if (b > 255) or (g > 255):
		b, g = 97, 0
	colors = '#%02x%02x%02x' % (r, g, b)
	color("#C90055", colors)
	begin_fill()
	forward(111.65)
	curve()
	left(120)
	curve()
	forward(111.65)
	end_fill()
	hideturtle()
	right(90)
done()
