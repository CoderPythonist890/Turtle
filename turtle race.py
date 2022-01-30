from turtle import *
from random import randint
from time import sleep

bgcolor("black")
color("white", "white")
hideturtle()
penup()
goto(-250, 300)
begin_fill()
pendown()
fd(500)
rt(90)
fd(50)
rt(90)
fd(500)
end_fill()
goto(0, 260)
color("black", "black")
write('Finish Line', align='center', font=('Arial', 18, 'bold'))

colors = ["cyan", "lime", "yellow", "red"]
turtles = [Turtle() for i in range(4)]

for index, t in enumerate(turtles):
	t.shape("turtle")
	t.setheading(90)
	t.penup()
	t.color("black", colors[index])
	t.goto(-150 + 100 * index, -150)
	t.speed(0)

delay(0)
# sleep(5)
breaker = False

while breaker == False:
	for index, t in enumerate(turtles):
		t.fd(randint(0, 1))
		if t.ycor() >= 250:
			breaker = True
			color(colors[index])
			winner = colors[index]
			break
	sleep(0.01)

m = (f'{winner} Won').title()
penup()
goto(0,0)
write(m, align='center', font=('Arial', 35, 'bold'))
done()
