from datetime import datetime

class Transaction:
    purchase_categories = ("Groceries", "Utilities", "Entertainment", "Transportation", "Housing", "Healthcare", "Education", "Investments", "Loans and Mortgages", "Traveel", "Personal Care", "Other")

    def __init__(self, category, amount, transaction_type):
        self.category = category
        self.amount = amount
        self.transaction_type = transaction_type
        self.purchase_time = datetime.now()


item = Transaction("Groceries",4.50 , "expense")
print(item.category)
print(item.amount)
print(item.purchase_time)