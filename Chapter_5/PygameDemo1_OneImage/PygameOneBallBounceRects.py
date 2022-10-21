'''
Titulo: Pygame Once Ball Bounce Rects

Objetivo: Hacer rebotar una pelota contra los bordes
utilizando un objecto rectangular.
'''

# Import packages
import pygame
from pygame.locals import *
import sys
import random
from pathlib import Path

# Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BASE_PATH = str(Path(__file__).resolve().parent)
N_PIXELS_PER_FRAME = 3

# Initialize world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()

# Load assets
ballImage = pygame.image.load(BASE_PATH + '/images/ball.png')

# Initialize variables
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

# Loop
while True:
    # Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Do any per frame actions
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed

    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed

    # Update de ball's rectangle using the speed in two directions
    ballRect.left += xSpeed
    ballRect.top += ySpeed

    # Clear the window before drawing it again
    window.fill(BLACK)

    # Draw the window elements
    window.blit(ballImage, ballRect)

    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
y
