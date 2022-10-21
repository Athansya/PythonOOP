'''
UID: 202203051144
Autor: Alfonso Toriz V.

Objetivo: Ilustrar cómo Python permite accesar directamente
variables instanciadas.
'''

from Person import *

oPerson1 = Person('Joe Schmoe', 9000)
oPerson2 = Person('Jane Smith', 9900)

# Obtenemos los valores del salario directamente
print(oPerson1.salary)
print(oPerson2.salary)

# Cambiamos la variable salario directamente
oPerson1.salary = 10000
oPerson2.salary = 11111

# Imprimimos los valores nuevos
print(oPerson1.salary)
print(oPerson2.salary)

'''
¿Por qué es problemático?

1. Permite cambiar nombres de variables instanciadas y puede
romper el código existente.
e.g. self.<originalName> = self.<newName>

2. Puede afectar el flujo de funcionamiento y arrojar resultados
erróneos.

3. Puede insertar valores erróneos si no se utiliza la función inicializadora del objeto.
'''


