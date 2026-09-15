from datetime import datetime

class SavingsPot:

    def __init__(self, name, goal_amount, saved_amount):
        self.name = name
        self.goal_amount = goal_amount
        self.saved_amount =  200
        self.created_at = datetime.now()

    def deposit(self, amount):
        self.saved_amount +=amount

    def withdraw(self, amount):
        if amount <= self.saved_amount:
            self.saved_amount -= amount
            return "Withdrawal successful"

        else:
            return "not enough money"

    def progress_bar(self):
        progress_bar = round(self.saved_amount / self.goal_amount * 100, 1 )
        progress_message = f"You are " + str(progress_bar) + "% of the way to your goal"
        return progress_message

    def balance(self):
        return self.saved_amount




New_pc_pot = SavingsPot("New PC",3450, 200)
New_pc_pot.deposit(2000)
print(New_pc_pot.name)
print(New_pc_pot.goal_amount)
print(New_pc_pot.saved_amount)
print(New_pc_pot.created_at)

New_pc_pot.withdraw(500)
print(New_pc_pot.balance())
New_pc_pot.balance()
print(New_pc_pot.progress_bar())
