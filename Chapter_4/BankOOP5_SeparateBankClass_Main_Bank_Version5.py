'''
Titulo: Bank OOP 5 Separate Bank Class
Main Bank Version 5

Objetivo: Utilizar la clase Bank
'''

# Importar
from Bank import *

# Creamos un objeto nuevo
oBank = Bank()

# Main
# Creamos dos cuentas
joesAccountNumber = oBank.createAccount('Joe', 100, 'JoesPassword')
print(f"Joe's account number is: {joesAccountNumber}")

marysAccountNumber = oBank.createAccount('Mary', 12345, 'MarysPasword')
print(f"Mary's account number is: {marysAccountNumber}")

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all acounts, press s')
    print('To make a withdrawal, press w')
    print()

    action = input('What do you want to do?: ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        oBank.balance()

    elif action == 'c':
        oBank.closeAccount()

    elif action == 'd':
        oBank.deposit()

    elif action == 'o':
        oBank.openAccount()

    elif action == 's':
        oBank.show()

    elif action == 'q':
        break

    elif action == 'w':
        oBank.withdraw()

    else:
        print('Sorry, that was not a valid action. Please try again.')

    print('Done')
