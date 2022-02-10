from turtle import *
from math import cos, radians
from random import choice

bgcolor("black")
tracer(2)
width(2)
ht()
X = 300
Y = 300
angle =1

colors = ["red","yellow","blue","lime","orange","cyan","white","deeppink","pink","magenta","gold","blue4","coral","deepskyblue","brown","orangered"]
l = [(-X, -Y), (X, -Y), (X, Y), (-X, Y)]
while True:
	for i in range(4):
		pu()
		goto(l[i % 4])
		pd()
		color(choice(colors))
		rt(angle)
		for j in range(int(90 / angle)+1):
			lt(angle)
			if j < 90 / (2 * angle):
				fd(2 * X / cos(radians(j * angle)))
			else:
				fd(2 * X / cos((radians(90 - j * angle))))
			pu()
			goto(l[i % 4])
			pd()
done()
