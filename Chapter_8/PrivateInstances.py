'''
UID: 202203051621
Autor: Alfonso Toriz V.

Objetivo: Mostrar las diferentes formas de hacer privadas
las variables de instancias.

Privadas Implícitas
- Se utiliza un guion bajo al inicio de la instancia variable

self._name
self._socialSecurityNumber
social._dontTouchThis

De igual manera funciona para métodos:

def _internalMethod(self):

def _dontCallMeFromClientSoftware(self):


Privadas Explícitas
- Se utilizan 2 guiones bajos

# PrivatePerson calss

class PrivatePerson():

    def __init__(self, name, privateData):
        self.name = name
        self.__privateData = privateData

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

Si intentamos accesar a la variable:

usersPrivateData = oPrivatePerson.__privateData

Nos generará un error. De igual manera podemos utilizarlo para 
métodos. No garantiza la privacidad completamente, en especial si
alguien que conoce el funcionamiento interno de Python intenta
accesar utilizando la forma: 
    <object>._<className>_<name>

'''

