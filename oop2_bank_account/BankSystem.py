class BankSystem:
    def transaction(self, account_from, account_to, amount):
        withdraw_success = account_from.withdraw(amount + 10)
        if withdraw_success:
            account_to.deposit(amount)

    def deposit(self, account, amount):
        account.deposit(amount)

    def withdraw(self, account, amount):
        account.withdraw(amount)
