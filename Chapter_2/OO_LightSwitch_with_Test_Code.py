'''
Titulo: OO LightSwitch with Test Code

Objetivo: Ilustrar los metodos de una clase.
'''

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def show(self):
        print(self.switchIsOn)
# Main code
oLightSwitch = LightSwitch() # Crea un objeto de la clase LightSwitch

# Llama a su metodo
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()
oLightSwitch.turnOff()
oLightSwitch.show()
