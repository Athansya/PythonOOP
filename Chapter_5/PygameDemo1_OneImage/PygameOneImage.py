'''
Titulo: Pygame One Image

Objetivo: Utilizar pygame para dibujar una imagen.
'''

# Import packages
import pygame
from pygame.locals import *
import sys
from pathlib import Path

# Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BASE_PATH = str(Path(__file__).resolve().parent)

# Initialize world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets
ballImage = pygame.image.load(BASE_PATH + '/images/ball.png')

# Initialize variables

# Loop forever
while True:

    # Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Do any "per frame" actions

    # Clear the window
    window.fill(BLACK)

    # Draw all window elements
    # draw ball at position 100 across (x) and 200 down (y)
    window.blit(ballImage, (100,200))

    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
