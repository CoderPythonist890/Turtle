from turtle import *

#choose colors :
colors=("blue", "gold", "deeppink", "red", "lime")
bgcolor("black")

width(3)
delay(0)
speed(0)
ht()

for i in range(1000):
    color(colors[i % len(colors)])
    lt(130)
    fd(i)

done()