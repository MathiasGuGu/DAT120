Emails = input("Velg filer med Email: ")
Output = input("Velg fila som skrives til: ")
email = []
sorted_email = []

def FindEmail(Emails, Output):
    try:
        with open(f"/Users/mathiasgumpen/Desktop/Dat120/Øving5/{Emails}.txt", "r") as reader:
            for line in reader:
                if "From:" in line:
                    #print(line)
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
            print(email)
                     
    except:
        print("Kunne ikke åpne fila") 

    try:
        with open(f"/Users/mathiasgumpen/Desktop/Dat120/Øving5/{Output}.txt", "w") as writer:
            for item in email:
                writer.write(item)
    except:
        print("kunne ikke skrive til fila")

def sort_emails(Output):

    #Lager en ny fil som er sortert

    try:
        items = []
        with open(f"/Users/mathiasgumpen/Desktop/Dat120/Øving5/{Output}.txt", "r") as reader:
            for line in reader:
                items.append(line)

        for i in items:
            if i not in sorted_email:
                sorted_email.append(i)

        with open(f"/Users/mathiasgumpen/Desktop/Dat120/Øving5/Sorted.txt", "w") as writer:
            for item in sorted_email:
                writer.write(item)
                
    except:
        print("Could not sort")



FindEmail(Emails, Output)
sort_emails(Output)