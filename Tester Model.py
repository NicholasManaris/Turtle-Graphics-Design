import turtle
bob=turtle.Turtle()
turtle.colormode(255)
bob.pensize(1)
bob.speed(0)
turtle.bgcolor("white")

from myFunctions import*

for times in range(256):
    bob.color(times,10,times)
    bob.forward(times)
    bob.left(times)
    bob.forward(times)
