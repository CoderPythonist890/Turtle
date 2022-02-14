from turtle import *

x, y = 262, 162
t = [(x, -y), (x, y), (-x, y), (-x, -y)]
bgcolor("black")
width(3)
ht()

goto(-x, -y)
color("#e70013")
begin_fill()
for i in range(4):
	goto(t[i])
end_fill()

home()
fd(92)
color("white")
seth(90)
begin_fill()
circle(92)
end_fill()

goto(66, 0)
color("#e70013")
begin_fill()
circle(66)
end_fill()

color("white")
begin_fill()
goto(81, 0)
circle(59)
end_fill()

goto(-6, -20)
seth(48)
color("#e70013")
begin_fill()
for i in range(5):
	fd(75)
	rt(144)
end_fill()

done()
