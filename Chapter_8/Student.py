'''
UID: 202203051707
Autor: Alfonso Toriz V.

Objetivo: Ilustrar los decoradores @property y @<nombre>.setter
'''

class Student():

    def __init__(self, name, startingGrade=0):
        self.__name = name
        self.grade = startingGrade

    @property
    def grade(self):
        return self.__grade # Lo vuelve privado

    @grade.setter
    def grade(self, newGrade):
        try:
            newGrade = int(newGrade)
        except (TypeError, ValueError) as e:
            raise type(e) (f'New grade: {str(newGrade)} is an invalid type.')
        if (newGrade < 0) or (newGrade > 100):
            raise ValueError(f'New grade: {str(newGrade)} must be between 0 and 100.')
        self.__grade = newGrade

# Student example
oStudent1 = Student('Michelle')
oStudent2 = Student('Alfonso', 90)

print(oStudent1.grade)
print(oStudent2.grade)

oStudent1.grade = 94
oStudent2.grade = 92

print(oStudent1.grade)
print(oStudent2.grade)

