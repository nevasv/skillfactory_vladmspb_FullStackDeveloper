from abc import ABC


class Wallet(ABC):
    def __init__(self, name: str, type: str = "General"):
        self.balance: int = 0
        self.name: str = name
        self.type: str = type

    def get_balance(self):
        return self.balance

    def change_balance(self, value: int):
        if self.balance + value < 0:
            print(f"Not enough balance {self.balance}")
        else:
            self.balance += value


class Card(Wallet):
    def __init__(self, name):
        super().__init__(name)


class ProCard(Wallet):
    def __init__(self, name, type="PRO"):
        super().__init__(name, type)

    def change_balance(self, value: int):
        if self.balance + value * 0.95 < 0:
            print(f"Not enough balance {self.balance}")
        self.balance += value * 0.95 if self.balance * value * 0.95 < self.balance else value


class CreditCard(Wallet):
    def __init__(self, name, limit: int = -1000):
        self.limit = limit
        super().__init__(name)

    def change_balance(self, value: int):
        if self.balance + value < self.limit:
            print(f"Not enough balance {self.balance}")
        else:
            self.balance = value


# card = ProCard("Sam")
# card = Card("Sam")
card = CreditCard("Sam")
print(card.get_balance())
card.change_balance(1000)
print(card.get_balance())
card.change_balance(-800)
print(card.get_balance())
card.change_balance(-210)
print(card.get_balance())
