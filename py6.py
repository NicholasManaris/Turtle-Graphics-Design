import turtle
bob=turtle.Turtle()
#to import the fades of the colors 
turtle.colormode(255)
bob.speed(0)
#bg color
turtle.bgcolor(0,0,0)

#the circle prgrams
for times in range(256):
    bob.circle(255-times)
    bob.color(times,255-times,255)

bob.right(180)

for times in range(256):
    bob.circle(255-times)
    bob.color(255,times,255-times)

bob.right(90)

for times in range(256):
    bob.circle(255-times)
    bob.color(255-times,255-times,255)

bob.right(180)

for times in range(256):
    bob.circle(255-times)
    bob.color(times,255,255-times)

#box function (the white box)
bob.color(255,255,255)
bob.penup()
bob.forward(50)
bob.pendown()
bob.right(90)
bob.forward(50)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(50)
