import unittest
from wallet import Wallet, not_enough

class WalletTest(unittest.TestCase):
    def test_default_cash(self):
        wallet = Wallet()

        self.assertEqual(wallet.get_cash(), 0)

    def test_start_cash(self):
        wallet = Wallet(50)

        self.assertEqual(wallet.get_cash(), 50)

    def test_add_cash(self):
        wallet = Wallet(50)
        wallet.add_cash(40)

        self.assertEqual(wallet.get_cash(), 90)

    def test_spend_cash(self):
        wallet = Wallet(90)
        wallet.spend_cash(40)

        self.assertEqual(wallet.get_cash(), 50)

    def test_check(self):
        wallet = Wallet(40)
        with self.assertRaises(not_enough):
            wallet.spend_cash(50)

if __name__ == '__main__':
    unittest.main()
