import turtle as t


t.speed(0)

class GetUserInfo():
    def getAntall() -> None:
        antallInput = input("hvor mange sekskanter vil du tegne?: ")
        return int(antallInput)

    def getFill() -> None:
        fill = input("vil du fylle sekskantene? y/n: ")
        return fill

    def getFillColor() -> None:
        fillcolor = input("Hvilken farge vil du fylle inn? red/green/black: ")
        return fillcolor

    """def getUserInput(self) -> None:"""
            

class Sixtuple():
    def draw():
        amount = GetUserInfo.getAntall()
        isFill = GetUserInfo.getFill()
        if (isFill.lower() == "y"):
            fillColor = GetUserInfo.getFillColor()

        lengde = 10
        avstand = 10
        sider = 1
        startx, starty = 0, 0
        diamant = 0
        for i in range(amount):

                lengde += avstand * 1.4
                diamant += 1
                t.pu()
                
                if (isFill.lower() == "y"):
                    if (diamant % 2 == 0):
                        t.fillcolor(fillColor)
                        t.begin_fill()
                        t.pu()
                    elif not (diamant % 2 == 0):
                        t.end_fill()
                        t.pu()

                        

                for j in range(4):
                    sider += 1
                    t.pd
                    t.left(45)
                    t.forward(lengde)
                    t.left(45)
                    if sider == 5:
                        sider = 1
                        starty -= avstand
                        t.pu()
                        t.setpos(startx, starty)
                        t.pd()

                    """
                    sider += 1
                    t.left(45)
                    t.forward(lengde)
                    t.left(45)
                    if sider == 5:
                        sider = 1
                        starty -= avstand
                        t.pu()
                        t.setpos(startx, starty)
                        t.pd()
                    """
                t.end_fill()
        t.done()


if __name__ == "__main__":
    sixtuple = Sixtuple()
    Sixtuple.draw()