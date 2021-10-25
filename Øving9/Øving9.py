
spiller1_poeng = 0
spiller2_poeng = 0

class SpørreOppgave:
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
        self.samlet_poengsum()
        print("\n")
    
    def korrekt_svar_tekst(self):
        return print("Korrekt svar var: " + f"{self.riktigsvar}")

    def sjekk_svar(self):
        global spiller1_poeng
        global spiller2_poeng
        spiller1_svar = input("velg ett svaralternativ for spiller 1: ")
        spiller2_svar = input("velg ett svaralternativ for spiller 2: ")
        print("\n")
        self.korrekt_svar_tekst()
        print("\n")

        if spiller1_svar != self.riktigsvar:
            print("Spiller 1: Feil")
        if spiller1_svar == self.riktigsvar:
            print("Spiller 1: Korrekt")
            spiller1_poeng += 1
        if spiller2_svar != self.riktigsvar:
            print("Spiller 2: Feil")
        if spiller2_svar == self.riktigsvar:
            print("Spiller 2: Korrekt")
            spiller2_poeng += 1


    def samlet_poengsum(self):
        global spiller1_poeng
        global spiller2_poeng
        return(print(f"Spiller 1 poengsum: {spiller1_poeng}" + "\n" + f"Spiller 2 poengsum: {spiller2_poeng}"))
    
    def finn_vinner(self):
        global spiller1_poeng
        global spiller2_poeng
        if spiller1_poeng > spiller2_poeng:
            print("spiller 1 vant!")

        if spiller1_poeng < spiller2_poeng:
            print("spiller 2 vant!")

        else:
            print("Uavgjort!")

fil = "/Users/mathiasgumpen/Desktop/Dat120/Øving9/sporsmaalsfil.txt"

def les_spm():
    with open(fil, "r") as reader:
        for linjenr, linje in enumerate(reader):
            linje.split()
            x2 = linje.strip().split(":")
            x1 = linje.replace(" ", "")
            x = x1.split(":")
            svar_liste = x[2].replace("\n", " ").replace("]", " ").strip().replace("[", " ").split(",")
            spm = SpørreOppgave(x2[0], svar_liste, x[1], linjenr)
            spm.__str__()
            spm.sjekk_svar()
        

            

if __name__ == "__main__":
    les_spm()
    #S
    