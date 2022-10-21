'''
UID: 202203051224
Autor: Alfonso Toriz V.

Objetivo: Agregar funciones Setter y Getter a la clase Person
'''

class Person():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Getter
    def getSalary(self):
        return self.salary

    # Setter
    def setSalary(self, salary):
        self.salary = salary

oPerson1 = Person('Michi Dubhe', 10000)
oPerson2 = Person('Alfonso Toriz', 10000)

# Obtenemos el salario con Getter
print(oPerson1.getSalary())
print(oPerson2.getSalary())

# Asignamos un nuevo salario
oPerson1.setSalary(20000)
oPerson2.setSalary(400000)

# Volvemos a imprimir los salarios
print(oPerson1.getSalary())
print(oPerson2.getSalary())
