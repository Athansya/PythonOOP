'''
UID: 202203101225
Autor: Alfonso Toriz V.

Objetivo: Ilustar inheritance de Python con una clase base y subclase.
'''

# Employye Manager inheritance

# Define the Employee class, which we will use as a base class

class Employee():
    def __init__(self, name, title, ratePerHour=None):
        self.name = name
        self.title = title
        if ratePerHour is not None:
            ratePerHour = float(ratePerHour)
        self.ratePerHour = ratePerHour

    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def payPerYear(self):
        # 52 weeks * 5 days a week * 8 hours per day
        pay = 52 * 5 * 8 * self.ratePerHour
        return pay

class Manager(Employee): # La base class va entre el parentesis y le hereda sus metodos
    def __init__(self, name, title, salary, reportsList=None): # Inicializamos las variables que no tiene Employee()
        self.salary = float(salary)
        if reportsList is None:
            reportsList = []
        self.reportsList = reportsList
        super().__init__(name, title) # Llama al init de la super class / base class Employee() para inicializar

    def getReports(self):
        return self.reportsList

    def payPerYear(self, giveBonus=False):
        pay = self.salary
        if giveBonus:
            pay = pay + (.10 * self.salary) # add a bonus of 10%
            print(f'{self.name} gets a bonus for good work')
        return pay

# Ambas clases tienen un metodo payPerYear que se ejecutara dependiendo el objeto con el que se llame (Overriding)
# Overriding:
# 1. Puede cambiar por completo el funcionamiento
# 2. Puede agregar funcionamiento

# Test
# Creamos objetos
oEmployee1 = Employee('Joe Schmoe', 'Pizza Maker', 16)
oEmployee2 = Employee('Chris Smith', 'Cashier', 14)
oManager = Manager('Sue Jones', 'Pizza Restaurant Manager', 55000, [oEmployee1, oEmployee2])

# Call methods of the Employee objects
print(f'Employee name: {oEmployee1.getName()}')
print(f'Employee salary: {oEmployee1.payPerYear():,.2f}')
print(f'Employee name: {oEmployee2.getName()}')
print(f'Employee salary: {oEmployee2.payPerYear():,.2f}')

# Call methods of the Manager object
managerName = oManager.getName()
print(f'Manager name: {managerName}')

# Give the manager a bonus
print(f'Manager salary: {oManager.payPerYear(True):,.2f}')
print(f'{managerName} {oManager.getTitle()} direct reports:')
reportsList = oManager.getReports()
for oEmployee in reportsList:
    print(f'    {oEmployee.getName()} ({oEmployee.getTitle()})')
