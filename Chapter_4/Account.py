'''
Titulo: Account

Objetivo: Crear una clase sencilla para una
cuenta de banco con operaciones simples.
'''

# Definimos la clase
class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Incorrect password')
            return None
        
        if amountToDeposit < 0:
            print('You cannot deposit negative cuantities')
            return None

        self.balance += amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Incorrect password')
            return None

        if amountToWithdraw < 0:
            print('You cannot withdraw negative cuantities')
            return None
        
        if amountToWithdraw > self.balance:
            print('You do not have enough funds')
            return None

        self.balance -= amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print('Incorrect password')
            return None

        return self.balance

    def show(self):
        print(f'\tName: {self.name}')
        print(f'\tBalance: {self.balance}')
        print(f'\tPassword: {self.password}')
        print()
'''
# Creamos una cuenta y la mostramos
oAccount1 = Account('John', 1000, 'nuts')
oAccount1.show()
# Depositamos y mostramos
oAccount1.deposit(500, 'nuts')
oAccount1.show()
# Retiramos y mostramos
oAccount1.withdraw(1000, 'nuts')
oAccount1.show()
# Obtenemos el balance e imprimimos
currentBalance = oAccount1.getBalance('nuts')
print(f'Current Balance: {currentBalance}')
'''
