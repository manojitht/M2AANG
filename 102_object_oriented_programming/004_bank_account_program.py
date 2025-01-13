# **Problem:**
# Create a class called `BankAccount` that represents a bank account. The class should have the following attributes:
# - `account_number`: The account number (a unique identifier for the account).
# - `account_holder`: The name of the account holder.
# - `balance`: The current balance of the account.
#
# The class should have the following methods:
# 1. A `__init__` method to initialize the account's attributes.
# 2. A method called `deposit` that allows depositing money into the account (add to the balance).
# 3. A method called `withdraw` that allows withdrawing money from the account (subtract from the balance). If there are insufficient funds, it should display a message saying so.
# 4. A method called `display_balance` that shows the current balance of the account.
#
# Once you've created the class, test it by creating an account, depositing money, withdrawing money, and displaying the balance.

# My Code:
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"The entered amount is {amount}, was deposited successfully!")
        else:
            print(f"The entered amount is {amount}, it should greater than 0")

    def withdraw(self, amount):
        if self.balance < amount != 0:
            print(f"Insufficient ammount in your account, can't withdraw {amount}. Try Again!")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawal of {amount} is successful!")

    def display_balance(self):
        print(f"Dear {self.account_holder}, your current balance is {self.balance}.")


## AI Code:
# class BankAccount:
#     def __init__(self, account_number, account_holder, balance=0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"The amount {amount} was deposited successfully!")
#         else:
#             print("Deposit amount must be greater than 0. Please try again.")
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdrawal amount must be greater than 0. Please try again.")
#         elif self.balance < amount:
#             print(f"Insufficient funds! Cannot withdraw {amount}.")
#         else:
#             self.balance -= amount
#             print(f"Withdrawal of {amount} was successful!")
#
#     def display_balance(self):
#         print(f"Dear {self.account_holder}, your current balance is {self.balance}.")
#
#     def __str__(self):
#         return f"Bank Account [Account Holder: {self.account_holder}, Account Number: {self.account_number}, Balance: {self.balance}]"
#
#
# # Test the class
# account = BankAccount("123456789", "John Doe", 500)
# account.deposit(200)
# account.withdraw(800)  # Insufficient funds
# account.withdraw(100)
# account.display_balance()
# print(account)  # Displays account details
