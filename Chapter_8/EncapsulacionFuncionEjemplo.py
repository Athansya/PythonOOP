'''
UID: 202205031123
Autor: Alfonso Toriz V.
Titulo: Encapsulacion con una funcion ejemplo

Resumen: Una funcion es un buen ejemplo de encapsulacion
porque uno no se interesa en cómo logra hacer lo que quiere
la función. Solo te interesa qué argumento se necesita pasar
y cómo usarás el resultado obtenido.
'''

def calculateAverage(numbersList):
    total = 0.0
    for number in numbersList:
        total += number
    nElements = len(numbersList)
    average = total / nElements
    return average
