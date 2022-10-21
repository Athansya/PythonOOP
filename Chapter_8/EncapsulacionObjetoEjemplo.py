'''
UID: 202205031136
Autor: Alfonso Toriz V.

Resumen: En OOP, los datos dentro de un objeto pertenecen al
objeto. Al código cliente sólo debe importarle con la interface
de la clase y no la implementación de sus métodos.
'''

class Person():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

oPerson1 = Person('Joe Schmoe', 9000)
oPerson2 = Person('Jane Smith', 9900)
# Cada objeto Person es dueño de su propia set de instance variables
