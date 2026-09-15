
class Investment:

    def __init__ (self, starting_amount, monthly_contribution,  interest_rate):
        self.starting_amount = starting_amount
        self.monthly_contribution = monthly_contribution
        self.interest_rate = interest_rate


    def project(self, years):
        current_balance = self.starting_amount
        total_months = years *12

        for months in range(total_months):
            growth = current_balance * self.interest_rate
            current_balance += growth
            current_balance +=self.monthly_contribution
        return round(current_balance, 2 )

my_investment =Investment(500,500, 0.1)
print(my_investment.project(5))



