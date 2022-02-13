from turtle import *
from time import sleep

# tracer(20)
bgcolor("black")
delay(0)

turtles = [Turtle() for _ in range(3)]
colors = ['red', 'orange', 'yellow']
ratio = [720, 60, 1]
r = 300
c=0

fd(r)
seth(90)
color("white")
width(3)
ht()

for i in range(60):
	lt(90)
	if i % 5 == 0:
		fd(r/14)
		bk(r/14)
	else:
		fd(r/28)
		bk(r/28)
	rt(90)
	for i in range(6):
		lt(1)
		fd(1.75 * (r / 100))

for index, t in enumerate(turtles):
	t.color(colors[index])
	t.pensize(8 -2*index)
	t.shape("arrow")
	t.shapesize(0.5, 1.5 - index * 0.5, 2)
	t.seth(90)
	t.lt(1)

while True:
	c+=1
	for index, t in enumerate(turtles):
		t.undo()
		t.rt((6 / ratio[index]))
		t.fd((index + 1) * (r/4))
	sleep(1)

done()
