import turtle
bob = turtle.Turtle()
turtle.colormode(255)
bob.pensize(2)
bob.speed(0)

from myFunctions import*

bob.right(90)

bob.penup()
bob.forward(200)
bob.pendown()

bob.left(90)

bob.begin_fill()
bob.color(238,154,73)
bob.circle(200)
bob.end_fill()

bob.color(0,0,0)

moveTo(bob,-100,100)

bob.right(90)

bob.begin_fill()
bob.color(255,255,255)
bob.circle(35)
bob.end_fill()

bob.begin_fill()
bob.color(0,0,0)
bob.circle(15)
bob.end_fill()

moveTo(bob,100,100)

bob.left(180)

bob.begin_fill()
bob.color(255,255,255)
bob.circle(35)
bob.end_fill()

bob.begin_fill()
bob.color(0,0,0)
bob.circle(15)
bob.end_fill()

moveTo(bob,0,0)

bob.right(180)

bob.penup()
bob.forward(100)
bob.pendown()

moveTo(bob,-100,-100)

bob.begin_fill()
bob.color(205,38,38)
bob.circle(100)
bob.end_fill()

moveTo(bob,0,-200)

bob.left(90)

bob.begin_fill()
bob.color(139,0,0)
bob.circle(50)
bob.end_fill()

turtle.done()
