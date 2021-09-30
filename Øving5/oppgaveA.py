def sjekk_alder():
    try:
        høyde = float(input("Hvor høy er du i meter?: "))
    except:
        print("Ikke ett lovlig flyttall")

    try:
        if høyde >= 1.20 or høyde > 0:
            print("Du kan ta karusellen")
        else:
            print("Du kan ikke ta karusellen")
    except:
        print("Kan ikke sjekke høyde")

sjekk_alder()