'''
UID: 202203051657
Autor: Alfonso Toriz V.

Objetivo: Mostar como funciona el decorador @property y @setter
'''

class Example():
    def __initi__(self, startingValue):
        self._x = startingValue

    @property
    def x(self): # decorador metodo setter
        return self._x

    @x.setter
    def x(self, value): # decorador metodo setter
        self._x = value

oExample = Example(10)
print(oExample.x)
oExample.x = 20
