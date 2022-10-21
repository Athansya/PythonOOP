'''
Titulo: OO Dimmer Switch Model2 Instantiation

Objetivo: Ilustrar otro modelo mendal de OOP
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

# Create three DimmerSwitch objects
oDimmer1 = DimmerSwitch('Dimmer1')
print(type(oDimmer1))
print(oDimmer1)
print()
oDimmer2 = DimmerSwitch('Dimmer2')
print(type(oDimmer2))
print(oDimmer2)
print()
oDimmer3 = DimmerSwitch('Dimmer3')
print(type(oDimmer3))
print(oDimmer3)
print()

print(f'oDimmer1 variables: {vars(oDimmer1)}')
