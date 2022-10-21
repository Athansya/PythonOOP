'''
Nombre: Bank1 One Account

Objetivo: Implementar un programa que se asemeje a un banco
y permita realizar diferentes operaciones con una cuenta.

Non-OOP
Version 1
'''

# Variables
accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

while True:
    print()
    print('Presione b para obtener el balance')
    print('Presione d para hacer un deposito')
    print('Presione w para hacer un retiro')
    print('Presione s para mostrar la cuenta')
    print('Presione q para salir')
    print()

    action = input('Que desea realizar?: ')
    action = action.lower() # Forzar minuscula
    action = action[0] # solo usar la primera letra
    print()

    if action == 'b':
        print('Obtener balance:')
        userPassword = input('Por favor ingrese su contrasena: ')
        if userPassword != accountPassword:
            print('Contrasena incorrecta')
        else:
            print(f'Su balance es: {accountBalance}')

    elif action == 'd':
        print('Deposito:')
        userDepositAmount = input('Ingrese la cantidad a depositar: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Por favor ingrese su contrasena: ')

        if userDepositAmount < 0:
            print('No puede depositar una cantidad negativa!')

        elif userPassword != accountPassword:
            print('Contrasena incorrecta')

        else: # OK
            accountBalance += userDepositAmount
            print(f'Su nuevo balance es: {accountBalance}')

    elif action == 's': # mostrar
        print('Mostrar:')
        print(f'\tNombre: {accountName}')
        print(f'\tBalance: {accountBalance}')
        print(f'\tContrasena: {accountPassword}')
        print()

    elif action == 'q':
        break

    elif action == 'w':
        print('Retiro:')

        userWithdrawAmount = input('Ingrese la cantidad a retirar: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Ingrese su contrasena: ')

        if userWithdrawAmount < 0:
            print('No puede retirar cantidades negativas!')

        elif userPassword != accountPassword:
            print('Contrasena incorrecta!')

        elif userWithdrawAmount > accountBalance:
            print('Fondos insuficientes')

        else: # OK
            accountBalance -= userWithdrawAmount
            print(f'Su nuevo balance es: {accountBalance}')

        print('Done')
