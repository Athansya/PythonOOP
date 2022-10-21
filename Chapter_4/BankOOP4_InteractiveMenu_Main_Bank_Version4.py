'''
Titulo: Bank OOP 4 Interactive Menu 
Bank Version 4

Objetivo: Agregar un menu interactivo 
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

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press o to open a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()

    action = input('What do you want to do?: ')
    action = action.lower() # lowcase
    action = action[0] # First letter
    print()

    if action == 'b':
        print('**Balance**')
        userAccountNumber = int(input('Enter your account number: '))
        userAccountPassword = input('Enter your password: ')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print(f'Your balance is: {theBalance}')

    elif action == 'd':
        print('**Deposit**')
        userAccountNumber = int(input('Enter your account number: '))
        userAccountPassword = input('Enter your password: ')
        userDepositAmount = int(input('Enter deposit: '))

        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.deposit(userDepositAmount, userAccountPassword)
        if theBalance is not None:
            print(f'Your new balance is: {theBalance}')

    elif action == 'o':
        print('**Open Account**')
        userName = input('Enter your name: ')
        userBalance = int(input('Enter your initial balance: '))
        userPassword = input('Enter your password: ')
        
        oAccount = Account(userName, userBalance, userPassword)
        accountsDict[nextAccountNumber] = oAccount
        print(f'Your account number is: {nextAccountNumber}')
        nextAccountNumber += 1
        print()

    elif action == 's':
        print('**Show**')
        for userAccountNumber in accountsDict:
            oAccount = accountsDict[userAccountNumber]
            print(f'Account number: {userAccountNumber}')
            oAccount.show()

    elif action == 'q':
        break

    elif action == 'w':
        print('**Withdrawal**')
        userAccountNumber = int(input('Enter your account number: '))
        userAccountPassword = input('Enter your password: ')
        userWithdrawalAmount = int(input('Enter withdrawal amount: '))

        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userWithdrawalAmount, userAccountPassword)
        if theBalance is not None:
            print(f'You withdrew: {userWithdrawalAmount}')
            print(f'Your new balance is: {theBalance}')

        else:
            print('Sorry, invalid action. Try again')

    print('Done')
