## Encapsulation means wrapping data and the functions that work on that data into one unit (class) and protecting the data from direct access.
## In simple words: “Keep data safe and control how it is accessed

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}, New amount {self.__balance}")

    def get_balance(self):
        return self.__balance      # controlled access


account = BankAccount('12345', 5000)

account.deposit(2000)

print(account.get_balance())       # Correct