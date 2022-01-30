from turtle import *

#choose colors:
c=("blue4","cyan3","deeppink")
bgcolor("black")

width(3)
delay(0)
speed(0)
ht()

for i in range(1000):
    color(c[i%len(c)])
    lt(150)
    fd(i)
    
done()