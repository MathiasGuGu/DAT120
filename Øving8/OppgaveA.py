

def les():
    dict = {}
    linje = 0
    with open("/Users/mathiasgumpen/Downloads/oving_8_rein_tekst.txt", "r") as reader:
        for linjenr, linje in enumerate(reader):
            ordene = linje.split()
            for ordet in ordene:
                ordet.lower()
                ordet.split()
                if ordet in dict:
                    continue
                else:
                    dict[ordet] = linjenr
                    print(f"Ordet {ordet}, kommer på linje {linjenr}")
    
                
        
les()