'''
UID: 202203071305
Autor: Alfonso Toriz V.

Objetivo: Ilustrar la abstraccion con una clase stack.
'''

class Stack():
    # La clase stack implementa el algoritmo LIFO Last In First Out
    def __init__(self, startingStackAsList=None):
        if startingStackAsList is None:
            self.dataList = []
        else:
            self.dataList = startingStackAsList[:] # Crea una copia

    def push(self, item):
        self.dataList.append(item)

    def pop(self, item):
        if len(self.dataList) == 0:
            raise IndexError
        element = self.dataList.pop()
        return element

    def peek(self):
        # Regresa el elemento de arriba, sin removerlo
        item = self.dataList[-1]
        return item

    def getSize(self):
        nElements = len(self.dataList)
        return nElements

    def show(self):
        # Muestra el stack en una orientacion vertical
        print('El Stack es: ')
        for value in reversed(self.dataList):
            print(f' {value}')

''' Las operaciones que realiza la clases parecen ser muy simples para el usuario porque
se utilizo abstraccion para simplificar el proceso'''
