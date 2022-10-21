'''
Titulo: Bank 4 N Accounts

Objetivo: Agregar un numero N de cuentas de banco
con la funcionalidad existente.
'''

# Variables
accountNamesList = []
accountBalancesList = []
accountPasswordsList = []

# Funciones
def newAccount(name, balance, password):
    global accountNamesList, accountBalancesList, accountPasswordsList

    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)

def show(accountNumber):
    global accountNamesList, accountBalancesList, accountPasswordsList
    print(f'Account: {accountNumber}')
    print(f'\tName: {accountNamesList[accountNumber]}')
    print(f'\tBalance: {accountBalancesList[accountNumber]}')
    print(f'\tPassword: {accountPasswordsList[accountNumber]}')

def getBalance(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    return accountBalancesList[accountNumber]

# Crea dos cuentas de ejemplo
print(f"Joe's account is account number: {len(accountNamesList)}") # Muestra numero de cuenta
newAccount('Joe', 100, 'soup')

print(f"Mary's account is account number: {len(accountNamesList)}")
newAccount('Mary', 12345, 'nuts')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show alla counts')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower() # forzar minuscula
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

print('Done')
