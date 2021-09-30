
#min høyde = 120
#max er uendelig

def sjekk_alder():
    try:
        høyde = float(input("Hvor høy er du?: "))
    except:
        print("Ikke ett lovlig flyttall")

    try:
        if høyde >= 120:
            print("Du kan ta karusellen")
        else:
            print("Du kan ikke ta karusellen")
    except:
        print("Kan ikke sjekke høyde")

sjekk_alder()