høyde = (input("Hvor høy er du?: "))

def sjekk_høyde(høyde):
    try:
        type(høyde) == float
        if høyde >= 120:
            print("Du kan ta karusellen")
        else:
            print("du kan ikke ta karusellen")
    except:
        print("Du kan ikke ta karusellen")
sjekk_høyde(høyde)

        