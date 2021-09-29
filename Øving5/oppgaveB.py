
Emails = input("Velg filer med Email: ")
Output = input("Velg fila som skrives til: ")
email = []
sorted_email = []

def FindEmail(Emails, Output):
    try:
        with open(f"/Users/mathiasgumpen/Desktop/Dat120/Øving5/{Emails}.txt", "r") as reader:
            for line in reader:
                for part in line.splitlines():
                    if "From:" in part:
                        if "<" in part:
                            mail = part
                            index1 = mail.find("<") 
                            index2 = mail.find(">") - 1   
                            if (True):
                                for i in range(index2-index1):
                                    index1 += 1 
                                    email.append(mail[index1])
                                    if index1 == index2:
                                        email.append("\n")        
                                        continue

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