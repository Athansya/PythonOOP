'''
UID: 202203161704
Autor: Alfonso Toriz V.

Objetivo: Utilizar el metodo magico __del__ para informar
a un objeto que va a desaparecer.
'''

# Student class


class Student():
    def __init__(self, name):
        self.name = name
        print(f'Creating Student object {self.name}')

    def __del__(self):
        print(f'In the __del__ method for student: {self.name}')


class Teacher():
    def __init__(self):
        print('Creating the Teacher object')
        self.oStudent1 = Student('Joe')
        self.oStudent2 = Student('Sue')
        self.oStudent3 = Student('Chris')

    def __del__(self):
        print('In the __del__ method for Teacher')


# Instantiate the Teacher object (that creates Student objects)
oTeacher = Teacher()

# Delete the Teacher object
del oTeacher
