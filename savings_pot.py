from datetime import datetime

class SavingsPot:

    def __init__(self, name, goal_amount):
        self.name = name
        self.goal_amount = goal_amount
        self.saved_amount =  0
        self.created_at = datetime.now()

    def deposit(self, amount):
        self.saved_amount +=amount


New_pc_pot = SavingsPot("New PC",3450)
New_pc_pot.deposit(2000)
print(New_pc_pot.name)
print(New_pc_pot.goal_amount)
print(New_pc_pot.saved_amount)
print(New_pc_pot.created_at)


