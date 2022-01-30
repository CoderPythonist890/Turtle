from turtle import *

color("red", "yellow")
bgcolor("black")
speed(0)

for i in range(200):
	begin_fill()
	forward(300 - i)
	left(170)
	forward(300 - i)
	end_fill()

done()
