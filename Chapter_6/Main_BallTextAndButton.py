'''
Titulo: Main Ball Text And Button

Objetivo: Utilizar las clases que hemos creado
'''
# Import packages
import pygame
from pygame.locals import *
import sys
import random
from ball import *
from SimpleText import *
from SimpleButton import *

# Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 30

# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets

# Initialize variables
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oFrameCountLabel = SimpleText(window, (60, 20), 'Program has run through this many loops: ', WHITE)
oFrameCountDisplay = SimpleText(window, (500, 20), '', WHITE)
oRestartButton = SimpleButton(window, (280, 60), '/images/buttonUp.png', '/images/buttonDown.png')
frameCounter = 0

# Loop forever
while True:
    # Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oRestartButton.handleEvent(event):
            frameCounter = 0 # Clicked button, reset counter

    # Do any per frame actions
    oBall.update() # tell the ball to update itself
    frameCounter += 1 # increment each frame
    oFrameCountDisplay.setValue(str(frameCounter))

    # Clear the window before drawing it again
    window.fill(BLACK)

    # Draw the window elements
    oBall.draw() # tell the ball to draw itself
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()

    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FPS)
