#
# Hva er det jeg MÅ gjøre... Først må jeg finne ut av hvor mange 
# diamanter jeeg skal tegne.
# Jeg trenger også noen variabler som bestemmer størrelsen på
# diamantene. 
# def draw():
#   finn ut hvor mange diamanter:
#       Start med å tegne den første diamanten
#           tegn første strek... roter 90deg. repeter x 4
#       når den er ferdig stopper du å tegne og flytter turtle
#       en level ut. repeter per diamant.
#           Turtle pen opp... flytt posisjon til startpunkt på ny dia
#           tegne første strek... roter 90deg. repeter x 4
#
#

import turtle as t
t.speed(5)
deg = 45

def sekskant():
    lengde = 10
    avstand = 10
    sider = 1
    startx, starty = 0, 0
    antall_diamanter = int(input("hvor mange diamanter vil du tegen?: "))
    for i in range(antall_diamanter):
        lengde += avstand * 1.4
        for j in range(4):
            sider += 1
            t.left(deg)
            t.forward(lengde)
            t.left(deg)
            if sider == 5:
                sider = 1
                starty -= avstand
                t.pu()
                t.setpos(startx, starty)
                t.pd()
    t.done()
        
sekskant()