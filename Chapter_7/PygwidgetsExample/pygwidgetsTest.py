'''
Titulo: Test Pygwidgets

Objetivo: Ilustrar el funcionamiento de pygwidgets.
'''

# Importar
from pathlib import Path
import pygame
from pygame.locals import *
import pygwidgets

# Definir constantes
BLACK = (0, 0, 0)
BLACKISH = (10, 10, 10)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
BASE_PATH = str(Path(__file__).resolve().parent)

# Funciones y clase para callback

def myFunction(theNickname):
    if theNickname is None:
        print('In myFunction, a button was clicked')
    else:
        print(f'In myFunction, the button named {theNickname} was clicked')

class Test():
    def myMethod(self, theNickname):
        if theNickname is None:
            print('In myMethod, a button was clicked')
        else:
            print(f'In myMethod, the button named {theNickname} was clicked')

# Initialize world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()
oTest = Test()

# Load assets
oBackgroundImage = pygwidgets.Image(window, (0, 0), BASE_PATH + '/images/background.jpg')
oDisplayTextTitle = pygwidgets.DisplayText(window, (0, 20), 'pygwidgets example by Irv Kalb', fontSize=36, width=640, textColor=BLACK, justified='center')

oInputTextA = pygwidgets.InputText(window, (20, 100), 'Default input text', textColor=WHITE, backgroundColor=BLACK, fontSize=24, width=250)

oInputTextB = pygwidgets.InputText(window, (20, 200), initialFocus=True, textColor=(0, 0, 255), fontSize=28)

oDisplayTextA = pygwidgets.DisplayText(window, (20, 300), 'Here is some display text', fontSize=24, textColor=WHITE, justified='center')

oDisplayTextB = pygwidgets.DisplayText(window, (20, 400), 'Here is some display text', fontSize=24, textColor=BLACK, backgroundColor=WHITE)

oRestartButton = pygwidgets.CustomButton(window, (100, 430), BASE_PATH + '/images/restartButtonUp.png', down=BASE_PATH + '/images/restartButtonDown.png', over=BASE_PATH + '/images/restartButtonOver.png', disabled=BASE_PATH + '/images/restartButtonDisabled.png', soundOnClick=BASE_PATH + '/sounds/blip.wav', nickname='restartButton', callBack=myFunction)

# oCheckBoxA controls the availability the custom radio buttons
# oCheckBoxB controls the availability of the text radio buttons
oCheckBoxA = pywidgets.CustomCheckBox(window, (450, 110), value=True, on=BASE_PATH + '/images/checkBoxOn.png', off=BASE_PATH + '/images/checkBoxOff.png', onDown=BASE_PATH + '/images/checkBoxOnDown.png', offDown=BASE_PATH + '/images/checkBoxOffDown.png', onDisable=BASE_PATH + '/images/checkBoxOnDisabled.png')

oRadioCustom1 = pygwidgets.CustomRadioButton(window, (500, 150), 'Custom Group', on=, off=, onDown=, offDown=, onDisabled=, offDisabled=, value=True, nickname='Low')
