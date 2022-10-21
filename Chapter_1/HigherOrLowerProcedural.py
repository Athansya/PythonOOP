''''
Título: HigherOrLowerProcedural

Objetivo: Crear un juego de cartas donde el usuario
debe adivinar si la carta siguiente a la mostrada es
mayor o menor. Con esta mecánica se otorgarán o quitarán
puntos al jugador.
'''

# Bibliotecas
import random

# Cartas Constantes
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8',
              '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

# Ingresa un deck y regresa una carta al azar
def getCard(deckListIn):
    thisCard = deckListIn.pop() # pop one off the top

    return thisCard

# Ingresa un deck y regresa el deck revuelto
def shuffle(deckListIn):
    deckListOut = deckListIn.copy() # Copia el deck inicial
    random.shuffle(deckListOut)
    return deckListOut

# Main
print('Bienvenido a Mayor o Menor.')
print('''Tienes que elegir si la siguiente carta por ser mostrada
        será mayor o menor a la carta en pantalla.''')
print('''Obtener el resultado correcto te dara 20 puntos; tenerlo
        incorrecto te restara 15.''')
print('Tienes 50 puntos para empezar.')

startingDeckList = []

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE): # enumerate da los indexes
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True: # Multiples juegos
    print()
    gameDeckList = shuffle(startingDeckList)

    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print(f'La carta inicial es: {currentCardRank} de {currentCardSuit}')
    print()

    for cardNumber in range(0, NCARDS): # Juega un juego de tantas cartas
        answer = input(f'''La siguiente carta sera mayor o menor a {currentCardRank}
        de {currentCardSuit}? (ingresa h o l): ''')
        answer = answer.casefold() # forzar minuscula

        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']

        print(f'La siguiente carta es: {nextCardRank} de {nextCardSuit}')

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('Bien hecho!, es mayor')
                score += 20
            else:
                print('Fallaste, no es mayor')
                score -= 15

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                print('Bien hecho!, es menor')
                score += 20
            else:
                print('Fallaste, no es menor')
                score -= 15

        print(f'Tu score es {score}')
        print()
        currentCardrank = nextCardRank
        currentCardValue = nextCardValue

    goAgain = input('Para jugar de nuevo, presione ENTER, o q para salir: ')
    if goAgain == 'q':
        break

    print('OK bye')


