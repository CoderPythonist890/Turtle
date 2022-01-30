from turtle import *

bgcolor("black")
ht()
bk(180)
setheading(-90)
speed(0)

for i in range(180):
	color("blue")
	lt(i)
	fd(i * 3)
	color("red")
	lt(i)
	fd(i * 3)

done()
