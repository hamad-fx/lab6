class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def transfer(self, other_account, amount):
        self.withdraw(amount)
        other_account.deposit(amount)

        return True
