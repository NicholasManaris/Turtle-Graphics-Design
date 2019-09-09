import turtle

andrew=turtle.Turtle()
andrew.color("red","black")
andrew.pensize(10)

helen=turtle.Turtle()
helen.color("pink","black")
helen.pensize(10)

greg=turtle.Turtle()
greg.color("black","yellow")
greg.pensize(10)

nico=turtle.Turtle()
nico.color("blue","yellow")
nico.pensize(10)

sides=8
angle=360/sides
distance=100

for times in range (sides):
    andrew.forward(distance)
    andrew.right(angle)

for times in range (sides):
    helen.forward(distance)
    helen.left(angle)

for times in range (sides):
    greg.left(angle)
    greg.forward(distance)

for times in range (sides):
    nico.right(angle)
    nico.forward(distance)
