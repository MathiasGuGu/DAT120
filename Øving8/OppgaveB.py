
class SpørreOppgave:
    def __init__(self, Spørsmål: str, Svar: list, RiktigSvar: int):
        self.spørsmål = Spørsmål   
        self.svar = Svar
        self.riktigsvar = RiktigSvar
        

    def __str__(self):
        return(print(f"{self.spørsmål}" + "\n" + "Velg ett av alternativene: indeks: " f"{self.svar}"))
    
    def SjekkSvar(self):
        svar = int(input("Ditt valg: "))
        if svar == self.riktigsvar:
            print("Riktig svar! ")
        else:
            print("Feil svar! ")

if __name__ == "__main__":
    spm1 = SpørreOppgave("Hva er 2 + 2?", ["1", "4" ,"3", "7", "8"], 1)
    spm2 = SpørreOppgave("Hvor mange sivile/krigsfanger i kina ble kokt, brent, hengt, skutt og kjørt over av tanks i nanjingmassakeren? ", ["1000", "25000", "300000", "560000"], 2)
    spm1.__str__()
    spm1.SjekkSvar()
    spm2.__str__()
    spm2.SjekkSvar()