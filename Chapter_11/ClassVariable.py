'''
UID: 202203161714
Autor: Alfonso Toriz V.

Objetivo: Mostrar un uso de class variables.
'''

# Sample class


class Sample():
    nObjects = 0  # this is a class variable of the Sample class

    def __init__(self, name):
        self.name = name
        Sample.nObjects = Sample.nObjects + 1

    def howManyObjects(self):
        print(f'There are {Sample.nObjects} Sample objects')

    def __del__(self):
        Sample.nObjects = Sample.nObjects - 1


# Instantiate 4 objects
oSample1 = Sample('A')
oSample2 = Sample('B')
oSample3 = Sample('C')
oSample4 = Sample('D')

# Delete 1 object
del oSample3

# See how many we have
oSample1.howManyObjects()
