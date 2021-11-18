
spiller1_poeng = 0
spiller2_poeng = 0

class SpørreOppgave:
    def __init__(self, Spørsmål: str, Svar: list, RiktigSvar: str, spmnr: int):
        self.spørsmål = Spørsmål   
        self.svar = Svar
        self.riktigsvar = RiktigSvar
        self.spmnr = spmnr
        
    def __str__(self):
        print("\n" + f"Spørsmål {self.spmnr + 1}) {self.spørsmål}" + "\n\n" + "Velg ett av alternativene: " + "\n")
        for i in range(len(self.svar)):
            print(f"{i}) {self.svar[i]}")
    
    def korrekt_svar_tekst(self):
        return self.svar[self.riktigsvar - 1] 

    def sjekk_svar(self, bruker_svar):
        if bruker_svar == self.riktigsvar:
            return True
        else: return False

    def samlet_poengsum(self):
        print(f"Spiller 1 poengsum: {spiller1_poeng}" + "\n" + f"Spiller 2 poengsum: {spiller2_poeng}")
    
    def finn_vinner(self):
        if spiller1_poeng > spiller2_poeng:
            print("spiller 1 vant!")

        if spiller1_poeng < spiller2_poeng:
            print("spiller 2 vant!")

        else:
            print("Uavgjort!")

fil = "/Users/mathiasgumpen/Desktop/Dat120/Øving9/sporsmaalsfil.txt"

        
if __name__ == "__main__":
    with open(fil, "r") as reader:
        for linjenr, linje in enumerate(reader):
            linje.split()
            x2 = linje.strip().split(":")
            x1 = linje.replace(" ", "")
            x = x1.split(":")
            svar_liste = x[2].replace("\n", " ").replace("]", " ").strip().replace("[", " ").split(",")
            spm = SpørreOppgave(x2[0], svar_liste, x[1], linjenr)
            spm.__str__()

            spiller1 = input("Spiller1: velg alternativ: ")
            spiller2 = input("Spiller2: velg alternativ: ")


            if spm.sjekk_svar(spiller1):
                print("spiller1 hadde rett!")
            if spm.sjekk_svar(spiller2):
                        print("spiller1 hadde rett!")

            else: print("Det ble uavgjort!")

                
    #S