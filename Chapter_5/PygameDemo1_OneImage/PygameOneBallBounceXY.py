'''
Titulo: Pygame One Ball Bounce X Y

Objetivo: Hacer una pelota que rebote contra los bordes de la pantalla
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
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3

# Initialize world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets
ballImage = pygame.image.load(BASE_PATH + '/images/ball.png')

# Initialize variables
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

# Loop
while True:
    # Check for and handle events
    for event in pygame.event.get():
        # Close button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if (ballX < 0) or (ballX >= MAX_WIDTH):
        xSpeed = -xSpeed
    if (ballY < 0) or (ballY >= MAX_HEIGHT):
        ySpeed = -ySpeed

    # Update the balls location, using the speed in two directions
    ballX += xSpeed
    ballY += ySpeed

    # Clear the window before drawing it again
    window.fill(BLACK)

    # Draw the ball
    window.blit(ballImage, (ballX, ballY))

    # Update the window
    pygame.display.update()

    # Slow down things a bit
    clock.tick(FRAMES_PER_SECOND)
