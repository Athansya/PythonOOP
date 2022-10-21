'''
Titulo: Object Oriented LigthSwitch

Objetivo: Ilustrar un switch como clase en Python.
'''

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

'''
Para crear un objeto nuevo o instancia
de nuestra nueva clase Lightswitch hay
que asignarlo.
'''
oLightSwitch = LightSwitch() # El prefijo 'o' indica que es un objeto
