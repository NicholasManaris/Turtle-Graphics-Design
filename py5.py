import turtle
gg=turtle.Turtle()
turtle.colormode(255)
gg.speed(0)
gg.pensize(1)
gg.hideturtle()
turtle.bgcolor(0,0,0)

for times in range(256):
    gg.color(255,0,times)
    gg.forward(100)
    gg.left(92)
    gg.forward(100) 
    
for times in range(256):
    gg.color(times,255,0)
    gg.forward(100)
    gg.left(92)
    gg.forward(100)

for times in range(256):
    gg.color(0,times,255)
    gg.forward(100)
    gg.left(92)
    gg.forward(100)    

for times in range(256):
    gg.color(255,255,0)
    gg.forward(100)
    gg.left(92)
    gg.forward(100)    

for times in range(256):
    gg.color(255,times,255)
    gg.forward(100)
    gg.left(92)
    gg.forward(100)    


turtle.done()
