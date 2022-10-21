'''
Titulo: Dimmer Switch

Objetivo: Hacer un switch con mas funcionalidad.
'''

class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.SwitchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness += 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness -= 1

    def show(self):
        print(f'Switch is on?: {self.switchIsOn}')
        print(f'Brightness is: {self.brightness}')
