from turtle import *

bgcolor("black")
def rcircle(x,y):
	for i in range(y):
		fd(1.75*x/100)
		rt(1)
def gt(x,y):
	pu()
	goto(x,y)
	pd()

goto(240,60)
seth(90)
color("#622DF7")
begin_fill()
circle(95,90)
fd(58)
rcircle(10,98)
fd(41)
circle(13,122)
fd(138)
rcircle(100,24)
fd(42)
circle(96,90)
fd(184)
circle(96,90)
fd(288)
circle(96,90)
goto(240,60)
end_fill()

color("#FFD700")
gt(-0.6,-8)
begin_fill()
seth(150)
for i in range(3):
	circle(22,120)
	fd(75)

end_fill()

color("white")
gt(79,-8)
begin_fill()
seth(330)
circle(12,180)
fd(15)
rt(115)
fd(15)
circle(12,180)
fd(33)
circle(10,105)
goto(79,-8)
end_fill()


gt(-74 ,21)
dot(51)

done()