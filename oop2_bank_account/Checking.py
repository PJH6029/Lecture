from BankAccount import BankAccount


class Checking(BankAccount):
    minimum = 0.0
    charge = 0.0

    def __init__(self, num=0, bal=0.0, minimum=1000, chg=2):
        super().__init__(num, bal)
        self.minimum = minimum
        self.charge = chg

    def withdraw(self, amount):
        if self.bal <= amount:
            print(f"Cannot withdraw ${amount} on account #{self.account_num} because the balance is low")
            return 0

        if self.bal < self.minimum:
            self.bal -= amount + self.charge
        else:
            self.bal -= amount
        return 1

    def print_account(self):
        print("Checking Account:", self.account_num)
        print("\tBalance:", self.bal)
        print("\tMinimum to Avoid Charges:", self.minimum)
        print("\tCharge per Check:", self.charge)
        print()
