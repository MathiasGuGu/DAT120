def pris(alder):
        if(alder < 18 or alder >= 67):
            print("biletten koster 20kr")
        elif(alder >= 18 or alder < 67):
            print("biletten koster 40kr")

alder = float(input("hvor gammel er du? "))
pris(alder)