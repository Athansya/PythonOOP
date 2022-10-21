'''
Titulo: Account

Objetivo: Ilustrar el funcionamiento de las clases.
'''

# Clase Account
class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        if amountToDeposit < 0:
            print('You cannot deposit a negative amount')
            return None
        self.balance += amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        if amountToWithdraw < 0:
            print('You cannot withdraw negative amounts')
            return None
        if amountToWithdraw > self.balance:
            print('Insufficiente funds')
            return None

        self.balance -= amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print('Incorrect password')
            return None
        return self.balance

    # Added for debugging
    def show(self):
        print(f'\tName: {self.name}')
        print(f'\tBalance: {self.balance}')
        print(f'\tPassword: {self.password}')
        print()
