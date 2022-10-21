'''
Titulo: Main Simple Button Callback

Objetivo: Crear un callback que se ejecute al picar el boton.
'''
# Import packages
import pygame
from pygame.locals import *
from SimpleButton import *
import sys

# Define constants
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FPS = 30

# Define a function to be used as a "callback"
def myCallBackFunction():
    print('User pressed the button B, called myCallBackFunction')

# Define a class with a method to be used as a "callback"
class CallBackTest():
    # Snipped any other methods in this class
    def myMethod(self):
        print('User Pressed button C, called myMethod of the CallBackTest object')

# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets

# Initialize variables
oCallBackTest = CallBackTest()
# Create instances of SimpleButton
# No call back
oButtonA = SimpleButton(window, (25, 30), '/images/buttonAUp.png', '/images/buttonADown.png')
# Specifying a function to call back
oButtonB = SimpleButton(window, (150, 30), '/images/buttonBUp.png', '/images/buttonBDown.png', callBack = myCallBackFunction)

oButtonC = SimpleButton(window, (275, 30), '/images/buttonCUp.png', '/images/buttonCDown.png', callBack = oCallBackTest.myMethod)
counter = 0

# Loop forever
while True:
    # Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pass the event to the button, see if it has been clicked on
        if oButtonA.handleEvent(event):
            print('User pressed button A, handled in the main loop')

        # oButton B and oButton C have callbacks,
        # no need to check result of these calls
        oButtonB.handleEvent(event)
        oButtonC.handleEvent(event)

    # Do any per frame actions
    counter += 1

    # Clear the window
    window.fill(GRAY)

    # Draw all window elements
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FPS)
