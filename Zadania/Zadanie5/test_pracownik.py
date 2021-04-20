import unittest
import pracownik

class TestPracownik(unittest.TestCase):
    def setUp(self):
        pracownik_1 = pracownik.Pracownik("Jan", "Kowalski", 2000)
        pracownik_2 = pracownik.Pracownik("Bartosz", "Skorupa", 3400)
        pracownik_3 = pracownik.Pracownik("Joanna", "Nowak", 2800)
        print('setUp')

    def pracownik_test(self):
        self.assertEqual(pracownik.Pracownik("Jan", "Kowalski", 2000)).email()
        self.assertEqual(pracownik.Pracownik("Bartosz", "Skorupa", 3400)).pelna_nazwa()
        self.assertEqual(pracownik.Pracownik("Joanna", "Nowak", 2800)).podwyzka()

    def tearDown(self):
        print('tearDown')

if __name__ == '__main__':
    unittest.main()
        
