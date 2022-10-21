'''
Titulo: Bank Class with exceptions

Objetivo: Agregar exceptions a la clase Bank.
'''

from AccountExceptions import *

class Bank():
    def __init__(self, hours, address, phone):
        self.accountsDict = {}
        self.nextAccountNumber = 0
        self.hours = hours
        self.address = address
        self phone = phone

    def askForValidAccountNumber(self):
        accountNumber = input('What is your account number?: ')
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AbortTransaction('The account number must be an integer')

        if accountNumber not in self.accountsDict:
            raise AbortTransaction(f'There is not account {accountNumber}')

        return accountNumber

    def getUsersAccount(self):
        accountNumber = self.askForValidAccountNumber()
        oAccount = self.accountsDict[accountNumber]
        self.askForValidPassword(oAccount)
        return oAccount

    # snipped additional methods

    def deposit(self):
        print('** Deposit **')
        oAccount = self.getUsersAccount()
        depositAmount = input('Pleas enter amount to deposit: ')
        theBalance = oAccount.deposit(depositAmount)
        print(f'Deposited: {depositAmount}')
        print(f'Your new balance is: {theBalance}')

    def withdraw(self):
        print('** Withdraw **')
        oAccount = self.getUsersAccount()
        userAmount = input('Please enter the amount to wihtdraw: ')
        theBalance = oAccount.withdraw(userAmount)
        print(f'Withdrew: {userAmount}')
        print(f'Your new balacne is: {theBalance}')

    def getInfo(self):
        print(f'Hours: {self.hours}')
        print(f'Address: {self.address}')
        print(f'Phone: {self.phone}')
        print(f'We currently have {len(self.accountsDict)} account(s) open.')

    # Special method for Bank Administrator only
    def show(self):
        print('** Show **')
        print('(This would typically require an admin password)')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print(f'Account: {userAccountNumber}')
            oAccount.show()
            print()

