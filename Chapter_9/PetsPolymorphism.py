'''
UID: 202203071314
Autor: Alfonso Toriz V.

Objetivo: Ilustrar el concepto de poliformismo en OOP con diferentes
clases de mascotas.
'''

class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} says bark, bark, bark!')

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} says meooooooow!')

class Bird():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} says tweet')

oDog1 = Dog('Rover')
oDog2 = Dog('Firulais')
oCat1 = Cat('Garfield')
oCat2 = Cat('Fluffy')
oBird = Bird('Pika')

petsList = [oDog1, oDog2, oCat1, oCat2, oBird]

for oPet in petsList:
    oPet.speak() # Llamamos al mismo metodo en diferentes clases
