from turtle import *
from random import uniform

bgcolor("black")
tracer(100)

n = 6
width = 30
step = 0.5  # round(width / 60,1)
j = sl = 1
ht()

while True:
	if j >= (n - 1) * step + sl:
		k = True
	if round(j, 2) == float(sl):
		k = False
	goto(0, -350)
	begin_fill()
	seth(139)
	for i in range(623):
		color((uniform(0, 1), uniform(0, 1), uniform(0, 1)))
		if i == 312:
			lt(120)
		if i >= 112 and i <= 511:
			rt(1)
		fd(j)
		dot(width)
	if k:
		j -= step
	else:
		j += step

	end_fill()
done()
