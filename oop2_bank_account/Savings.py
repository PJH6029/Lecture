from BankAccount import BankAccount

class Savings(BankAccount):
    int_rate = 0.0

    def __init__(self, num=0, bal=0, rate=3.5):
        super().__init__(num, bal)
        self.int_rate = rate

    def interest(self):
        month_interest = self.bal * self.int_rate / (12 * 100)
        self.bal += month_interest

    def withdraw(self, amount):
        if self.bal <= amount:
            print(f"Cannot withdraw ${amount} on account #{self.account_num} because the balance is low")
            return 0

        self.bal -= amount
        return 1

    def print_account(self):
        print("Savings Account:", self.account_num)
        print("\tBalance:", self.bal)
        print(f"\tInterest: {self.int_rate}%")
        print()
