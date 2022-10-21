'''
UID: 202203161654
Autor: Alfonso Toriz V.

Objetivo: Utilizar una clase para mostrar el funcionamiento de
reference count (tracking de variables que hacen referencia a
un objeto).
'''

# Reference count example
import sys


class Square():
    def __init__(self, width, color):
        self.width = width
        self.color = color


# Instantiate an object
oSquare1 = Square(5, 'red')
print(f'Reference count is {sys.getrefcount(oSquare1)}')
print(oSquare1)
# Reference count of the Square object is 1

oSquare2 = oSquare1
print(f'Reference count is {sys.getrefcount(oSquare1)}')
print(oSquare2)
# Reference count of the Square object is 2
print(oSquare1 == oSquare2)  # Mismo objeto
