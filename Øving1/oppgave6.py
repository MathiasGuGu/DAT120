#OPPGAVE 6
while True:
    fall = float(input("Hvor mange sekunder skal objektet falle?: "))
    fart_etter_sek = fall * 9.81
    distanse_etter_tid = 0.5*fart_etter_sek*fall
    print(f'Fart: {fart_etter_sek} m/s') 
    print(f'Distanse: {distanse_etter_tid} m')