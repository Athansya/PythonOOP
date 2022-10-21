'''
Titulo: Monster example

Objetivo: Ilustrar el funcionamiento de una lista
de objetos.
'''

import random

class Monster():
    '''
    Monster class that can be used to instantiate many Monster
    '''
    def __init__(self, nRows, nCols, maxSpeed):
        self.nRows = nRows
        self.nCols = nCols
        # Choose random row and col
        self.myRow = random.randrange(self.nRows)
        self.myCol = random.randrange(self.nCols)
        # Set speed on x and y
        self.mySpeedX = random.randrange(-maxSpeed, maxSpeed + 1)
        self.mySpeedY = random.randrange(-maxSpeed, maxSpeed + 1)
        # Set other instance variables like health, power, etc.

    def move(self):
        self.myRow = (self.myRow + self.mySpeedX) % self.nRows
        self.myCol = (self.myCol + self.mySpeedY) % self.nCols

# We create a list of Monster objects
N_MONSTER = 20
N_ROWS = 100
N_COLS = 200
MAX_SPEED = 4
monsterList = []
for i in range(N_MONSTERS):
    # Create object
    oMonster = Monster(N_ROWS, N_COLS, MAX_SPEED)
    # Append object
    monsterList.append(oMonster)

'''
Later on, we could make all monsters do one action: 
    e.g.
    for oMonster in monsterList:
    oMonster.move()
'''

