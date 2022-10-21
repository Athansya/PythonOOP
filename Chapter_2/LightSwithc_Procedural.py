'''
Titulo: Light Switch Procedural

Objetivo: Simular el comportamiento de
un switch de luz.
'''

def turnOn():
    global switchIsOn
    # turn the light one
    switchIsOn = True

def turnOff():
    global switchIsOn
    # turn the light off
    switchIsOn = False

# Main code
switchIsOn = False # Global Variable

# Test code
print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
