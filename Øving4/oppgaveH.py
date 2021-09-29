from oppgaveG import avstand

while True:
    x1, y1 = int(input("punkt x1 ")), int(input("punkt y1 "))
    x2, y2 = int(input("punkt x2 ")), int(input("punkt y2 "))

    print(f"avstanden er: {avstand(x1, x2, y1, y2)}")
