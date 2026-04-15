import turtle
turtle.Screen().bgcolor("red")
turtle.Screen()

pen = turtle.Turtle()
sides = 4
angle = 90
leanth = 100

for i in range(sides):
    pen.forward(leanth)
    pen.right(angle)
turtle.done()