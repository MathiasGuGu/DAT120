from oppgaveA import pris

alder = int(input("Hvor gammel er du? "))
while alder:
        if alder <= 0:
            print("Ugyldig alder...")
            alder = int(input("Hvor gammel er du? "))
        elif alder >= 0 : 
            pris(alder)   
            break
            