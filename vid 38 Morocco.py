from turtle import *

x, y = 400, 262
t = [(x, -y), (x, y), (-x, y), (-x, -y)]
bgcolor("black")
ht()

goto(-x, -y)
color("#c1272d")
begin_fill()
for i in range(4):
	goto(t[i])
end_fill()

goto(-75,20)
width(14)
color("#006233")
for i in range(5):
	fd(150)
	rt(144)

done()