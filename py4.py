import turtle
bob=turtle.Turtle()
bob.color("green","yellow")
bob.pensize(5)


sides=7
angle=360/sides
distance=100

for times in range (sides):
    bob.forward(distance)
    bob.left(angle)

bob.color("blue","yellow")
bob.pensize(5)


sides=7
angle=360/sides
distance=100

for times in range (sides):
    bob.forward(distance)
    bob.right(angle)

bob.color("yellow","green")
bob.pensize(5)

bob.penup()
bob.forward(100)
bob.pendown()

sides=7
angle=360/sides
distance=100

for times in range (sides):
    bob.forward(distance)
    bob.right(angle)

bob.color("black","yellow")
bob.pensize(5)

sides=7
angle=360/sides
distance=100

for times in range (sides):
    bob.forward(distance)
    bob.left(angle)

bob.color("pink","black")
bob.pensize(5)


bob.right(180)
bob.penup()
bob.forward(100)
bob.pendown()

sides=7
angle=360/sides
distance=100

for times in range (sides):
    bob.forward(distance)
    bob.right(angle)

bob.color("teal","green")
bob.pensize(5)

sides=7
angle=360/sides
distance=100

for times in range (sides):
    bob.forward(distance)
    bob.left(angle)

bob.color("purple","pink")
bob.pensize(5)

bob.penup()
bob.forward(100)
bob.pendown()

sides=7
angle=360/sides
distance=100

for times in range (sides):
    bob.forward(distance)
    bob.right(angle)

bob.color("red","white")
bob.pensize(5)

sides=7
angle=360/sides
distance=100

for times in range (sides):
    bob.forward(distance)
    bob.left(angle)
