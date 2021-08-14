from BankAccount import BankAccount
from BankSystem import BankSystem
from Checking import Checking
from InterestChecking import InterestingChecking
from Savings import Savings

if __name__ == '__main__':
    bank1 = BankSystem()

    James = Checking(1103458181, 950)
    Thompson = InterestingChecking(1203217789, 2800)
    Mathew = Savings(1308563516, 4000)
    Amy = Checking(1401945501, 670)

    accounts = [James, Thompson, Mathew, Amy]

    # all operations
    bank1.transaction(James, Thompson, 200)
    bank1.withdraw(James, 100)
    bank1.withdraw(Mathew, 1000)
    bank1.transaction(Thompson, Amy, 600)
    bank1.withdraw(Amy, 1300)
    bank1.withdraw(Thompson, 200)
    bank1.transaction(Mathew, James, 540)
    bank1.transaction(James, Amy, 1200)
    bank1.deposit(James, 300)

    Thompson.interest()
    Mathew.interest()

    print("\n\n\t\tAccount Balances\n")
    print(f"Name: James     Account Number: #{James.get_account_num()}", end='')
    print(f"     Balance: ${James.get_balance()}")
    print(f"Name: Thompson     Account Number: #{Thompson.get_account_num()}", end='')
    print(f"     Balance: ${Thompson.get_balance()}")
    print(f"Name: Mathew     Account Number: #{Mathew.get_account_num()}", end='')
    print(f"     Balance: ${Mathew.get_balance()}")
    print(f"Name: Amy     Account Number: #{Amy.get_account_num()}", end='')
    print(f"     Balance: ${Amy.get_balance()}")
    print()

    for i in range(4):
        accounts[i].print_account()
