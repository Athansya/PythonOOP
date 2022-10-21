'''
Titulo: Bank 2 One Account With Functions

Objetivo: Utilizar funciones para simplificar el codigo
de Bank 1.

Non-OOP
Bank 2
Single account
'''

accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword # global permite acceder a variables fuera del scope
    accountName = name
    accountBalance = balance
    accountPassword = password

def show():
    global accountName, accountBalance, accountPassword
    print(f'\tNombre: {accountName}')
    print(f'\tBalance: {accountBalance}')
    print(f'\tContrasena: {accountPassword}')
    print()

def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Contrasena incorrecta')
        return None
    return accountBalance

def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('No puedes depositar cantidades negativas!')
        return None

    if password != accountPassword:
        print('Contrasena incorrecta')
        return None

    accountBalance += amountToDeposit
    return accountBalance

def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print('No puedes depositar cantidades negativas!')
        return None

    if password != accountPassword:
        print('Contrasena incorrecta')
        return None

    if amountToWithdraw > accountBalance:
        print('Cantidad insuficiente en la cuenta')
        return None

    accountBalance -= amountToWithdraw
    return accountBalance

newAccount('Joe', 100, 'soup') # Crea una cuenta

while True:
    print()
    print('Presione b para obtener el balance')
    print('Presione d para hacer un deposito')
    print('Presione w para hacer un retiro')
    print('Presione s para mostrar la cuenta')
    print('Presione q para salir')
    print()

    action = input('Que desea hacer?: ')
    action = action.lower() # Forzar minuscula
    action = action[0] # usar la primera letra
    print()

    if action == 'b':
        print('Obtener balance:')
        userPassword = input('Ingresar password: ')
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print(f'Su saldo es: {theBalance}')

    elif action == 'd':
        print('Deposito: ')
        userDepositAmount = input('Ingresa la cantidad a depositar: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Ingresa la contrasena: ')

        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print(f'Su nuevo saldo es {newBalance}')

    elif action == 'w':
        print('Retiro: ')
        userWithdrawAmount = input('Ingresa la cantidad a retirar: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Ingresa la contrasena: ')

        newBalance = withdraw(userWithdrawAmount, userPassword)
        if newBalance is not None:
            print(f'Su nuevo saldo es {newBalance}')

    elif action == 's':
        print('Cuenta:')
        show() 

    elif action == 'q':
        break

    print('Done')
