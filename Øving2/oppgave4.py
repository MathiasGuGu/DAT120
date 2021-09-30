sum = 0
forsøk = 0

while True:
    tall = int(input("Skriv inn ett tall: "))
    if(tall >= 0):
        sum += tall
        forsøk += 1
    else:
        print(f"gjennomsnittet av tallene er {sum/forsøk}")
        break