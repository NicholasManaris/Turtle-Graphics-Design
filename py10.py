import turtle
bob=turtle.Turtle()
turtle.colormode(255)
turtle.bgcolor("black")
bob.pensize(2)
bob.speed(0)

for times in range(256):
    bob.color(times,times,0)
    bob.circle(times)
    bob.right(90)
     
bob.left(45)

for times in range(256):
    bob.color(times,0,times)
    bob.circle(times)
    bob.right(90)

bob.left(45)

for times in range(256):
    bob.color(0,times,times)
    bob.circle(times)
    bob.right(90)

bob.left(45)

for times in range(256):
    bob.color(times,times,times)
    bob.circle(times)
    bob.right(90)

bob.left(45)

for times in range(256):
    bob.color(times,0,times)
    bob.circle(times)
    bob.right(90)
