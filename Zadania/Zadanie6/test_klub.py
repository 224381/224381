import unittest
import klub

class TestKlub(unittest.TestCase):
    def setUp(self):
        self.ManchesterCity = klub.Klub('Manchester City')
        self.Bayern = klub.Klub('Bayern')
        self.Bayern.nadaj_trenera()

    def test_klub(self):
        self.assertEqual(self.ManchesterCity.sprawdz(), 'Klub Manchester City nie posiada trenera')
        self.assertEqual(self.Bayern.sprawdz(), 'Klub Bayern posiada trenera')

if __name__ == '__main__':

    unittest.main()
