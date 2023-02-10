class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= amount
            print("Withdrawal Accepted")

# Instantiate the class
acct1 = BankAccount('John Doe', 100)

# Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)

# Test to make sure the account can't be overdrawn
acct1.withdraw(500)


nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
