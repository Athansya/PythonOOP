'''
Titulo: OO Dimmer Switch Model1

Objetivo: Ilustrar un modelo mental de OOP
'''

class DimmerSwitch():
    def __init__(self, label):
        self.switchIsOn = False
        self.brightness = 0
        self.label = label

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
        print(f'Label: {self.label}')
        print(f'Switch is on?: {self.switchIsOn}')
        print(f'Brightness is: {self.brightness}')

# Create first DimmerSwitch, turn it on, and raise the level twice
oDimmer1 = DimmerSwitch('Dimmer1')
oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()

# Create second DimmerSwitch, turn it on, and raise the level 3 times
oDimmer2 = DimmerSwitch('Dimmer2')
oDimmer2.turnOn()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()

# Create a thrid DimmerSwitch, using the default settings
oDimmer3 = DimmerSwitch('Dimmer3')

# Ask each switch to show itself
oDimmer1.show()
oDimmer2.show()
oDimmer3.show()



