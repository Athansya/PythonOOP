'''
Titulo: BankOOP1 Individual Variables/Main Bank Version1

Objetivo: Agregar codigo de prueba para nuestra clase Account
'''

# Test program using accounts
# Version 1, using explicit variables for each Account object

# Import statement
from Account import *

# Creamos 2 cuentas
oJoesAccount = Account('Joe', 100, 'JoesPassword')
print('Created an account for Joe')

oMarysAccount = Account('Marys', 12345, 'MarysPassword')
print('Created an account for Mary')

oJoesAccount.show()
oMarysAccount.show()
print()

# Call some methods on the different accounts
print('Callind methods of the two accounts ...')

oJoesAccount.deposit(50, 'JoesPassword')
oMarysAccount.withdraw(345, 'MarysPassword')
oMarysAccount.deposit(100, 'MarysPassword')

# Show the accounts
oJoesAccount.show()
oMarysAccount.show()

# Create another account with information from the user
userName = input('What is your name?: ')
userBalance = int(input('What is user starting balance for this account?: '))
userPassword = input('What will be your password?: ')
oNewAccount = Account(userName, userBalance, userPassword)

# Show the newly created user account
oNewAccount.show()

# Let's deposit 100 into the new account
oNewAccount.deposit(100, userPassword)
userBalance = oNewAccount.getBalance(userPassword)
print()
print(f"After depositing 100, the user's balance is: {userBalance}")

# Show the new account
oNewAccount.show()
