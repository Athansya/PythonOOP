'''
Titulo: Bank OOP 3 Dictionary of Account Objects
Main Bank Version 3

Objetivo: Utilizar un diccionario para almacenar
las cuentas de los usuarios.
'''

# Import
from Account import *

accountsDict = {}
nextAccountNumber = 0

# Creamos dos cuentas
oAccount = Account('Joe', 100, 'JoesPassword')
joesAccountNumber = nextAccountNumber

accountsDict[joesAccountNumber] = oAccount
print(f'Account number for Joe is: {joesAccountNumber}')
nextAccountNumber += 1

oAccount = Account('Mary', 12345, 'MarysPassword')
marysAccountNumber = nextAccountNumber

accountsDict[marysAccountNumber] = oAccount
print(f'Account number for Mary is: {marysAccountNumber}')
nextAccountNumber += 1

accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()
print()

# Utilizamos algunos metodos
print('Calling methods of the two accounts...')
accountsDict[joesAccountNumber].deposit(50, 'JoesPassword')
accountsDict[marysAccountNumber].withdraw(345, 'MarysPassword')
accountsDict[marysAccountNumber].deposit(100, 'MarysPassword')

# Mostramos las cuentas
accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()

# Creamos una cuenta para el usuario
print()
userName = input('What is your name?: ')
userBalance = int(input('What is your initial balance?: '))
userPassword = input('What is your password?: ')

oAccount = Account(userName, userBalance, userPassword)
newAccountNumber = nextAccountNumber
accountsDict[newAccountNumber] = oAccount
print(f'User account number is: {newAccountNumber}')
nextAccountNumber += 1

# Mostramos la cuenta
accountsDict[newAccountNumber].show()
accountsDict[newAccountNumber].deposit(100, userPassword)
usersBalance = accountsDict[newAccountNumber].getBalance(userPassword)
print()
print(f'After deposit 100, your balance is: {usersBalance}')

# Mostramos la cuenta
accountsDict[newAccountNumber].show()
