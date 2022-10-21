'''
UID: 202203091220
Autor: Alfonso Toriz V.

Objetivo: Utilizar metodos magicos en una clase vector.
'''

import math

class Vector():
    '''The Vector class represents two values as a vector,
    allow for many math calculations'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, oOther): # called for + operator
        return Vector(self.x +oOther.x, self.y + oOther.y)

    def __sub__(self, oOther): # called for - operator
        return Vector(self.x - oOther.x, self.y - oOther.y)

    def __mul__(self, oOther): # called for * operator
        # Special code to allow for multiplying by a vector or a scalar
        if isinstance(oOther, Vector): # multiply two vectors
            return Vector((self.x * oOther.x), (self.y  * oOther.y))
        elif isinstance(oOther, (int, float)): # multipy by a scalar
            return Vector((self.x * oOther), (self.y * oOther))
        else:
            raise TypeError('Second value muest be a vector or scalar')

    def __abs__(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def __eq__(self, oOther): # called for == operator
        return (self.x == oOther.x) and (self.y == oOther.y)

    def __ne__(self, oOther): # called for !=
        return (self == oOther) # calls __eq__ method

    def __lt__(self, oOther): # called for < operator
        if abs(self) < abs(oOther): # calls __abs__ method
            return True
        else:
            return False

    def __gt__(self, oOther): # called for > operator
        if abs(self) > abs(oOther): # calls __abs__ method
            return True
        else:
            return False
    
    def __str__(self):
        return f'This vector has the value ({str(self.x)}, {str(self.y)})'

