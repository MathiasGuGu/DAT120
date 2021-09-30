sorted_email=[]
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

