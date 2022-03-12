from turtle import *
from random import randint, uniform
from time import sleep
from colorsys import *

# Change these numbers and send me your best picture  :) :
#############################################

delay_between_images = 0.5  # second
number_of_images = 20

min_number_of_turtles = 2  # >=2
max_number_of_turtles = 10  # <=15

min_radius = 10
max_radius = 350

min_pen_size = 1
max_pen_size = 3

min_turtle_speed = 1  # >=1
max_turtle_speed = 10  # <=359

min_color_changer = 0.001  # >=0.001
max_color_changer = 0.001  # <=0.999

#############################################
tracer(0)
bgcolor("black")
allturtles = [Turtle() for _ in range(max_number_of_turtles)]

for x in range(number_of_images):
	reset()
	for i in allturtles:
		i.ht()
	ht()
	n = randint(min_number_of_turtles, max_number_of_turtles)
	w = []
	r = []
	s = []
	for _ in range(n):
		r.append(randint(min_radius, max_radius))
		s.append(randint(min_turtle_speed, max_turtle_speed))
		w.append(randint(min_pen_size, max_pen_size))
	turtles = [allturtles[i] for i in range(n)]
	# c = [(uniform(0, 1), uniform(0, 1), uniform(0, 1)) for _ in range(n - 1)]
	for index, i in enumerate(turtles):
		i.pu()
		i.seth(90)
		i.fd(r[index])
		i.seth(180)
	hue = uniform(0, 1)
	k = uniform(min_color_changer, max_color_changer)
	for i in range(360):
		for index, j in enumerate(turtles):
			for _ in range(s[index]):
				j.fd(1.75 * r[index] / 100)
				j.lt(1)
		pu()
		goto(turtles[0].pos())
		pd()
		for j in range(1, n):
			width(w[j - 1])
			# color(c[j - 1])
			color(hsv_to_rgb(hue, 1, 1))
			goto(turtles[j].pos())
			hue += k
	update()
	sleep(delay_between_images)
	for i in turtles:
		i.reset()

done()
