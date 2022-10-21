'''
Titulo: Bank OOP 2 List of Account Objects
Main Bank Version 2

Objetivo: Utilizar una lista para almacenar las cuentas.
'''

# Importamos
from Account import *

# Creamos la lista vacia
accountsList = []

# Creamos dos cuentas
oAccount = Account('Joe', 100, 'JoesPassword')
print(f"Joe's account number is {len(accountsList)}")
accountsList.append(oAccount)

oAccount = Account('Mary', 12345, 'MarysPassword')
print(f"Marys account number is {len(accountsList)}")
accountsList.append(oAccount)

accountsList[0].show()
accountsList[1].show()
print()

# Utilizamos algunos metodos
print('Calling methods of the two accounts ...')
accountsList[0].deposit(50, 'JoesPassword')
accountsList[1].withdraw(345, 'MarysPassword')
accountsList[1].deposit(100, 'MarysPassword')

# Mostramos las cuentas
accountsList[0].show()
accountsList[1].show()

# Creamos una nueva cuenta con informacion del usuario
userName = input('What is your name?: ')
userBalance = int(input('What is user starting balance for this account?: '))
userPassword = input('What will be your password?: ')
oAccount = Account(userName, userBalance, userPassword)
print(f'Your account number is {len(accountsList)}')
accountsList.append(oAccount)

# Mostramos la nueva cuenta
accountsList[2].show()

# Depositamos 100
accountsList[2].deposit(100, userPassword)
usersBalance = accountsList[2].getBalance(userPassword)
print()
print(f'After depositing 100, your balance is {usersBalance}')

# Mostramos la cuenta
accountsList[2].show()
