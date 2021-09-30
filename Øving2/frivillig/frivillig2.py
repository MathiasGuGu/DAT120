import turtle

HEIGHT = 1
WIDTH = 2


turtle.screensize(WIDTH, HEIGHT)


#er det mulig for turtle å stoppe og bevege seg ned x antall pixler etter 6 runder
#konklusjon -- funker fett!

fig = int(input("hvor mange figurer vil du tegne? "))
def draw():
    posx, posy = 0, 0
    turtle.pu()
    turtle.setx, turtle.sety = -10, -10
    turtle.pd()
    for i in range(fig):
        turns = 0
        for i in range(6):
            turns+=1
            turtle.forward(15)
            turtle.left(-60)
            if turns == 6:
                turtle.pu()
                posy -= 25
                turtle.setpos(posx, posy)
                turtle.pd()
                turns = 0
    turtle.done()     




            


draw()
