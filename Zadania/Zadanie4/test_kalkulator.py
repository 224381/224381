import unittest
import kalkulator

class testKalkulator(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(kalkulator.add(2,2),4)

    def testSubtract(self):
        self.assertEqual(kalkulator.subtract(2,2),0)

    def testMultiplication(self):
        self.assertEqual(kalkulator.multiplication(2,2),4)

    def testDivision(self):
        self.assertEqual(kalkulator.division(2,2),1)
        self.assertRaises(ZeroDivisionError, kalkulator.division, 2, 0)

    def testExponentiation(self):
        self.assertEqual(kalkulator.exponentiation(2),4)

    def testSquareroot(self):
        self.assertEqual(kalkulator.squareroot(4),2)

    def testPercent(self):
        self.assertEqual(kalkulator.percent(5, 4),1)
        self.assertRaises(ZeroDivisionError, kalkulator.percent, 4, 0)

if __name__ == '__main__':
    unittest.main()

    

    

    
