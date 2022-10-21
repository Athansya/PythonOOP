'''
Titulo: Account Class with Exceptions

Objetivo: Agregar exceptions a la clase Account.
'''

# Errores indicados por "raise"

# Custom exceptions
class AbortTransaction(Exception):
    # Raise exception to abort bank transaction
    pass

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = self.validateAmount(balance)
        self.password = password

    def validateAmount(self, amount):
        try amount = int(amount)
        except ValueError:
            raise AbortTransaction('Amount must be an integer')
        if amount <= 0:
            raise AbortTransaction('Amount must be positive')
        return amount

    def checkPasswordMatch(self, password):
        if password != self.password:
            raise AbortTransaction('Incorrect password')

    def deposit(self, amountToDeposit):
        amountToDeposit = self.validateAmount(amountToDeposit)
        self.balance += amountToDeposit
        return self.balance

    def getBalance(self):
        return self.balance

    def withdraw(self, amountToWithdraw):
        amountToWithdraw = self.validateAmount(amountToWithdraw)
        if amountToWithdraw > self.balance:
            raise AbortTransaction('Not enough funds in your account')
        self.balance -= amountToWithdraw
        return self.balance

    # Added for debugging
    def show(self):
        print(f'\tName: {self.name}')
        print(f'\tBalance: {self.balance}')
        print(f'\tPassword: {self.password}')
