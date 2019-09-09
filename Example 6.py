import turtle
turtle=turtle.Turtle()
turtle.speed(11)
import colorsys
#turtle setup stuff goes here
for i in range(1000):
    color = colorsys.hsv_to_rgb(i/4545, 1.0, 1.0)
    #compatibility quirk: on 2.7 and below, use i/1000.0
    turtle.color(color)
    turtle.forward(i)
    turtle.right(98)
