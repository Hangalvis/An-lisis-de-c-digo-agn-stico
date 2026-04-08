class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Monto inválido")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Monto inválido")
        if amount > self.balance:
            raise ValueError("Saldo insuficiente")
        self.balance -= amount
        return self.balance