'''
Titulo: Bank 3 Two Accounts

Objetivo: El mismo que Bank 2, pero
agrega la abilidad de tener 2 cuentas.
'''

account0Name = ''
account0Balance = 0
account0Password = ''
account1Name = ''
account1Balance = 0
account1Password = ''

def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password
    if accountNumber == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password

def show():
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if account0Name = != '':
        print('Account 0')
        print(f'\t Name: {account0Name}')
        print(f'\t Balance: {account0Balance}')
        print(f'\t Password: {account0Password}')
        print()
    if account0Name = != '':
        print('Account 1')
        print(f'\t Name: {account1Name}')
        print(f'\t Balance: {account1Balance}')
        print(f'\t Password: {account1Password}')
        print()

def getBalance(accountNumber, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if password != account0Password:
            print('Incorrect password')
            return None
        return account0Balance

    if accountNumber == 1:
        if password != account1Password:
            print('Incorrect password')
            return None
        return account1Balance

    print('Done')
