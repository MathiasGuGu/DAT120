Emails = input("Velg filer med Email: ")
Output = input("Velg fila som skrives til: ")
email = []
sorted_email = []

def FindEmail(Emails, Output):
    try:
        with open(f"/Users/mathiasgumpen/Desktop/Dat120/Øving5/{Emails}.txt", "r") as reader:
            for line in reader:
                if "From:" in line:
                    if "<" in line:
                        x1 = line.find("<")
                        x2 = line.find(">") - 1
                    elif "[" in line:
                        x1 = line.find("[") 
                        x2 = line.find("]") - 1

                    for i in range(x2 - x1): 
                        x1 += 1
                        email.append(line[x1])

                        if (x1 == x2):
                            email.append("\n")                     
    except:
        print("Kunne ikke åpne fila") 

    try:
        with open(f"/Users/mathiasgumpen/Desktop/Dat120/Øving5/{Output}.txt", "w") as writer:
            for item in email:
                writer.write(item)
    except:
        print("kunne ikke skrive til fila")

FindEmail(Emails, Output)
