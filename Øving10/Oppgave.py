import unittest

spillere = []
spiller_poengsum = {}



class SpørreOppgave():
    def __init__(self, Spørsmål: str, Svar: list, RiktigSvar: int, spmnr: int):
        self.spørsmål = Spørsmål   
        self.svar = Svar
        self.riktigsvar = RiktigSvar
        self.spmnr = spmnr
        


    def __str__(self):
        print("\n" + f"Spørsmål {self.spmnr + 1}) {self.spørsmål}" + "\n\n" + "Velg ett av alternativene: " + "\n")
        for i in range(len(self.svar)):
            print(f"{i}) {self.svar[i]}")        
        print("\n")


        
        
    def korrekt_svar_tekst(self):
        print("Korrekt svar var: " + f"{self.riktigsvar}")
        return self.riktigsvar



    def sjekk_svar(self):
        svar = []
        for spiller in spillere:
            ans = input(f"{spiller}: Velg det alternativet du tror er korrekt: ")
            print("\n")
            if ans == self.riktigsvar:
                spiller_poengsum[spiller] += 1
                svar.append(f"{spiller}: Korrekt!")
            else:
                spiller_poengsum[spiller] == spiller_poengsum[spiller]
                svar.append(f"{spiller}: Feil!")
        for sv in svar:
            print(sv)

        return ans


    def samlet_poengsum(self):
        global spillere
        global spiller_poengsum

        for spiller in spillere:
            return(f"{spiller} poengsum: {spiller_poengsum[spiller]}")
    


    def finn_vinner(self):
        global spillere
        global spiller_poengsum
        poeng = []
        for x in spillere:
            poeng.append(spiller_poengsum[x])

        x = max(poeng)
        for spiller in spillere:
            if spiller_poengsum[spiller] == x:
                print(f"Vinneren var {spiller} med {spiller_poengsum[spiller]} poeng! ")



class Spiller:
    def __init__(self, navn, poengsum = 0):
        self.navn = navn
        self.poengsum = poengsum

    def __str__(self):
        return self.navn

    def poeng(self):
        return self.poengsum


fil = "/Users/mathiasgumpen/Desktop/Dat120/Øving9/sporsmaalsfil.txt"


def lag_spillere():
    global spillere
    global spiller_poengsum
    antall = int(input("Hvor mange spillere?: "))
    for _ in range(antall):
        navn = str(input("Hva heter du?: "))
        spiller = Spiller(navn)
        spillere.append(spiller)

    for x in spillere:
        spiller_poengsum[x] = spiller.poeng()
    

def still_spørsmål():
    Mellomrom = "-------------------------------------------"
    with open(fil, "r") as reader:
        for linjenr, linje in enumerate(reader):

            linje.split()
            x = linje.strip().split(":")
            riktig_svar = x[1].replace(" ", "")
            svar_liste = x[2].replace("\n", " ").replace("]", " ").strip().replace("[", " ").split(",")

            spm = SpørreOppgave(x[0], svar_liste, riktig_svar, linjenr)
            print(Mellomrom)
            spm.__str__()
            spm.sjekk_svar()
            spm.korrekt_svar_tekst()
            """
            check = Test(spm)
            check.run()
            """
    print(Mellomrom)
    spm.finn_vinner()



if __name__ == "__main__":
    lag_spillere()
    still_spørsmål()
    
