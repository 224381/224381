class not_enough(Exception):
    pass

class Wallet:
    def __init__(self, cash = 0):
        self.cash = cash

    def add_cash(self, account):
        if account <= 0:
            return

        self.cash += account

    def spend_cash(self, account):
        if account <= 0:
            return
        if account > self.cash:
            raise not_enough
        else:
            self.cash -= account

    def get_cash(self):
        return self.cash
