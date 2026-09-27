from investment import Investment
from transaction import Transaction
from savings_pot import SavingsPot

class Wallet:
    def __init__(self):
        self.transactions = []
        self.pots = {}

    def add_transaction(self, transactions):
        self.transactions.append(transactions)

    def add_pot(self,pot):
        self.pots[pot.name]=pot


my_wallet = Wallet()

my_transaction = Transaction("Groceries", 200,"expense")
my_savings = SavingsPot("Forex", 2000, 200)

my_wallet.add_transaction(my_transaction)
my_wallet.add_pot(my_savings)

print(my_wallet.transactions)
print(my_wallet.pots)