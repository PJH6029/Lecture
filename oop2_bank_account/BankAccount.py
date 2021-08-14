from abc import *


class BankAccount(ABC):
    account_num = 0
    bal = 0.0

    def __init__(self, num, bal):
        self.account_num = num
        self.bal = bal

    def deposit(self, amount):
        self.bal += amount

    @abstractmethod
    def withdraw(self, amount):
        if self.bal - amount >= 0:
            self.bal -= amount
        return 0

    def get_account_num(self):
        return self.account_num

    def get_balance(self):
        return self.bal

    @abstractmethod
    def print_account(self):
        pass