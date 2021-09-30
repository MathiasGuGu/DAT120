alder = int(input("Hvor gammel er kunden? "))

if(alder < 18 or alder >= 67):
    print("biletten koster 20kr")
else:
    print("biletten koster 40kr")