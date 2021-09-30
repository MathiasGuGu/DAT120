sum = 0

while True:
    tall = int(input("Skriv inn ett tall: "))
    if(tall >= 0):
        sum += tall
    else:
        print(f"summen av tallene er {sum}")
        break
        