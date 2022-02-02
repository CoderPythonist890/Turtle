from turtle import *

t = [Turtle(), Turtle()]
c = [1, 3]

colors = ["darkorange1", "gold", "cyan", "mediumorchid"]
bgcolor("black")
tracer(10)
ht()

for index, i in enumerate(t):
	i.ht()
	i.width(3)
	i.pu()
	i.seth(90)
	i.bk(120* (c[index]))
	i.seth(0)
	i.pd()

for i in colors:
	t[0].color(i)
	t[1].color(i)
	color(i)
	for i in range(361):
		for i in range(6):
			t[0].fd(2)
			t[0].lt(1)
		pu()
		goto(t[0].pos())
		t[1].fd(c[1] * 2)
		t[1].lt(1)
		pd()
		goto(t[1].pos())

done()
