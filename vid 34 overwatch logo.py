from turtle import *


def rcircle(r, a):
	for _ in range(a):
		fd(r / 100 * 1.75)
		rt(1)


def r(a, d):
	rt(a)
	fd(d)


def l(a, d):
	lt(a)
	fd(d)



bgcolor("black")

goto(-238, 257)
color("#43484c")
begin_fill()
lt(223)
circle(350, 274.5)
l(92, 102)
rt(272)
rcircle(239, 79)
r(103, 185)
r(20, 160)
l(154.5, 220)
l(46, 188)
rt(97)
rcircle(238, 78)

r(97, 191)
seth(90)
fd(220)
l(154.5, 160)
r(20.5, 188)
rt(103)
rcircle(237, 80)
goto(-238, 257)
end_fill()
pu()
fd(26)
p = pos()
rt(3)
pd()
color("#f99e1a")
begin_fill()
rcircle(350, 77)
r(90, 102)
rt(89)
circle(250, 76)
goto(p)
end_fill()

ht()
done()
