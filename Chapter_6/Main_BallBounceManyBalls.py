'''
Titulo: Main Ball Bounce Many Balls

Objetivo: Utilizar la clase Ball para hacer rebotar varias pelotas.
'''

# Import packages
import pygame
from pygame.locals import *
import sys
import random
from ball import *

# Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 3

# Init world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets

# Initialize variables
ballList = []
for oBall in range(0, N_BALLS):
    # Each time through the loop, create a Ball object
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall) # append the new Ball to the list of Balls

# Loop forever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Do any per frame actions
    for oBall in ballList:
        oBall.update()

    # Clear the window before drawing it again
    window.fill(BLACK)

    # Draw the window elements
    for oBall in ballList:
        oBall.draw()

    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
