'''
Titulo: Bank 5 Dictionary

Objetivo: Agregar diccionarios para facilitar
y agilizar el codigo.
'''

# Variables
accountsList = []

# Funciones
def newAccount(aName, aBalance, aPassword):
    global accountsList
    newAccountDict = {'name':aName, 'balance':aBalance, 'password':aPassword}

    accountsList.append(newAccountDict)

def show(accountNumber):
    global accountsList
    print(f'Account: {accountNumber}')
    thisAccountDict = accountsList[accountNumber]
    print(f"\tName: {thisAccountDict['name']}")
    print(f"\tBalance: {thisAccountDict['balance']}")
    print(f"\tPassword: {thisAccountDict['password']}")
    print()

def getBalance(accountNumber, password):
    global accountsList

    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None
    return thisAccountDict['balance']

print(f"Joe's account is account number: {len(accountsList)}")
newAccount("Joe", 100, 'soup')

print(f"Mary's account is account number: {len(accountsList)}")
newAccount("Mary", 12345, 'nuts')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get Balance:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print(f'Your balance is: {theBalance}')

    elif action == 'd':
        print('Deposit:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter your password: ')

        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print(f'Your new balance is: {newBalance}')

    elif action == 'n':
        print('New Account:')
        userName = input('What is your name? ')
        userStartingAmount = input('What is the amount of your initial deposit? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What password would you like to use for this account? ')

        userAccountNumber = len(accountsList)
        newAccount(userName, userStartingAmount, userPassword)
        print(f'Your new account number is: {userAccountNumber}')

        print('Done')
