'''
Titulo: Try Except Test

Objetivo: Ilustrar el uso de try y except.
'''

age = input('Please enter your age: ')
try: # Intenamos convertir a integer
    age = int(age)
except ValueError: # Si nos da error
    print('Sorry, that was not a valid number')
