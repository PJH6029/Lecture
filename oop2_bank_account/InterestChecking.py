from Checking import Checking

class InterestingChecking(Checking):
    int_rate = 0.0
    minint = 0.0
    mon_charge = 0.0

    def __init__(self, num=0, bal=0, cmin=1000, imin=2500, chg=2, rate=2.5, mon_chg=10):
        super().__init__(num, bal, cmin, chg)
        self.minint = imin
        self.int_rate = rate
        self.mon_charge = mon_chg

    def interest(self):
        if self.bal < self.minint:
            self.bal -= self.mon_charge
        else:
            month_interest = self.bal * self.int_rate / (12 * 100)
            self.bal += month_interest

    def print_account(self):
        print("Interest Checking Account:", self.account_num)
        print("\tBalance", self.bal)
        print("\tMinimum to Avoid Charges:", self.minimum)
        print("\tCharge per Check:", self.charge)
        print("\tMinimum balance for getting interest and NO Monthly Fee:", self.minint)
        print(f"\tInterest: {self.int_rate}%")
        print("\tMonthly Fee:", self.mon_charge)
        print()

