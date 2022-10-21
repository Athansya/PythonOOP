'''
Titulo: Bank

Objetivo: Crear un objeto organizador de objetos.
'''

from Account import *

class Bank():

    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumber = 0

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        # Increment to prepare for next account to be created
        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber

    def openAccount(self):
        print('** Open Account **')
        userName = input('What is the name for the new user account?: ')
        userStartingAmount = int(input('What is the starting balance for this account?: '))
        userPassword = input('What is the password you want to use for this account?: ')

        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print(f'Your new account number is: {userAccountNumber}')
        print()

    def closeAccount(self):
        print('** Close Account **')
        userAccountNumber = int(input('What is your account number?: '))
        userPassword = input('What is your password?: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)
        if theBalance is not None:
            print(f'You had {theBalance} in your account, which is being returned to you.')
            # Remove user's account from the dictionary of accounts
            del self.accountsDict[userAccountNumber]
            print('Your account is now closed.')

    def balance(self):
        print('** Get Balance **')
        userAccountNumber = int(input('Enter your account number: '))
        userAccountPassword = input('Enter your password: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print(f'Your balance is: {theBalance}')

    def deposit(self):
        userAccountNumber = int(input('Enter your account number: '))
        userDepositAmount = int(input('Enter your deposit amount: '))
        userAccountPassword = input('Enter your password: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.deposit(userDepositAmount, userAccountPassword)
        if theBalance is not None:
            print(f'Your new balance is: {theBalance}')

    def show(self):
        print('** Show ** ')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print(f'\tAccount: {userAccountNumber}')
            oAccount.show()

    def withdraw(self):
        print('** Withdraw **')
        userAccountNumber = int(input('Enter your account number: '))
        userWithdrawAmount = int(input('Enter your withdraw amount: '))
        userAccountPassword = input('Enter your password: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userWithdrawAmount, userAccountPassword)
        if theBalance is not None:
            print(f'You withdrew: {userWithdrawAmount}')
            print(f'Your new balance is: {theBalance}')


