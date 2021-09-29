"""
Funksjon som bestemmer om du møter på noe ( eks fiender eller belønninger osv...)
"""
from GenerateRandom import GenerateRandomNumber
from enemies import Wolf

class Encounter:
    def enemy():
        n = GenerateRandomNumber.Random()
        if n == 3:
            wolf = Wolf(False, "Wolf", n * n, 100, 100)
            print("Youve encountered a wolf!")
            print(wolf)
        else:
            print("You walk peacfully")
    def reward():
        return
