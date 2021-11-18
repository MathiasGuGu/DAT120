from øvingaaa import SpørreOppgave
import unittest

class Test(unittest.TestCase):
    def test_korrekt_svar(self):
        self.assertEqual(svar.korrekt_svar_tekst(), "C")


    def test_sjekk_svar(self):
        self.assertEqual(svar.sjekk_svar(1), False)
        self.assertEqual(svar.sjekk_svar(2), False)
        self.assertEqual(svar.sjekk_svar(3), True)



if __name__ == '__main__':
    svar = SpørreOppgave([], ["A","B","C"], 3, 0)
    unittest.main()