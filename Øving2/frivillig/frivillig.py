import turtle

HEIGHT = 1
WIDTH = 2

turtle.screensize(WIDTH, HEIGHT)


sider = int(input("Hvor mange sider skal mangekanten ha? "))
grader = 360 / sider
lengde = 100 / (sider / 9)


def draw():
    turtle.pu()
    turtle.setpos(10,10)
    turtle.pd()

    for i in range(sider):
        turtle.forward(lengde)
        turtle.left(grader)
    turtle.done()
draw()
