'''
UID: 202203091231
Autor: Alfonso Toriz V.

Objetivo: utilizar la clase Vector y sus metodos magicos.
'''

from Vector import *

v1 = Vector(3, 4)
v2 = Vector(2, 2)
v3 = Vector(3, 4)

# Thse lines print Boolean or numeri values
print(v1 == v2)
print(v1 == v3)
print(v1 < v2)
print(v1 > v2)
print(abs(v1))
print(abs(v2))
print()

# These lines print Vectors (calls the __str__() method)
print(f'Vector 1: {v1}')
print(f'Vector 2: {v2}')
print(f'Vector 1 + Vector 2: {v1 + v2}')
print(f'Vector 1 - Vector 2: {v1 - v2}')
print(f'Vector 1 times Vector 2: {v1 * v2}')
print(f'Vector 2 times 5: {v1 * 5}')
