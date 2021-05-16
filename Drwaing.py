import turtle

colors = ["red", "yellow", "green", "purple", "orange"]
t=turtle.Turtle()
turtle.bgcolor("black")
for x in range(360):
    t.pencolor(colors[x%5])
    t.width(x/100+1)
    t.forward(x)
    t.left(47)
turtle.done()

#his