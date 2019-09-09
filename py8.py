import turtle
bob=turtle.Turtle()
turtle.colormode(255)
bob.pensize(2)
bob.speed(0)
bob.hideturtle()

from myFunctions import* #to import from myFunction

coolSquared2(bob,100,(0,255,0),(255,0,0))

bob.left(90)

coolSquared2(bob,100,(0,255,0),(255,0,0))

bob.right(180)

coolSquared2(bob,100,(0,255,0),(255,0,0))

bob.right(90)

coolSquared2(bob,100,(0,255,0),(255,0,0))

moveTo(bob,0,0)

bob.left(90)

bob.penup()
bob.forward(200)
bob.pendown()

bob.left(90)

bob.begin_fill()
bob.color(58,95,205)
bob.circle(200)
bob.end_fill()

moveTo(bob,0,0)

bob.left(90)

bob.penup()
bob.forward(100)
bob.pendown()

bob.left(90)

bob.begin_fill()
bob.color(255,255,255)
bob.circle(100)
bob.end_fill()

moveTo(bob,0,0)

bob.left(90)

bob.penup()
bob.forward(50)
bob.pendown()

bob.left(90)

bob.begin_fill()
bob.color(152,245,255)
bob.circle(55)
bob.end_fill()

moveTo(bob,0,-35)

bob.begin_fill()
bob.color(0,0,0)
bob.circle(40)
bob.end_fill()

turtle.done()
