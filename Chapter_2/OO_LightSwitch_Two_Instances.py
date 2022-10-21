'''
Titulo: OO LightSwitch Two Instances

Objetivo: Ilustrar diferentes instancias de objetos.
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
oLightSwitch1 = LightSwitch()
oLightSwitch2 = LightSwitch()

# Test code
oLightSwitch1.show()
oLightSwitch2.show()

oLightSwitch1.turnOn()
oLigthSwitch2.turnOff()

oLightSwitch1.show()
oLightSwitch2.show()
