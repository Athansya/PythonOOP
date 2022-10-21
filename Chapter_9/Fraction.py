'''
UID: 202203091237
Autor: Alfonso Toriz V.

Objetivo: Crear una clase Fraction que permita manipular numerados y denominadores
utilizando metodos magicos.
'''

import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

class Fraction():
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError(f'Numerator {numerator} must be an integer')
        if not isinstance(denominator, int):
            raise TypeError(f'Denominator {denominator} must be an integer')
        self.numerator = numerator
        self.denominator = denominator

        # Use the math package to find the greates common divisor
        greatestCommonDivisor = math.gcd(self.numerator, self.denominator)
        if greatestCommonDivisor > 1:
            self.numerator //= greatestCommonDivisor
            self.denominator //= greatestCommonDivisor
        self.value = self.numerator / self.denominator

        # Normalize the sign of the numerator and denominator
        self.numerator = int(math.copysign(1.0, self.value)) * abs(self.numerator)
        self.denominator = abs(self.denominator)

    def getValue(self):
        return self.value

    def __str__(self):
        # Create a string representation of the fraction
        output = f'Fraction: {str(self.numerator)} / {str(self.denominator)} \n Value: {str(self.value)}'
        return output

    def __add__(self, oOtherFraction):
        # Add two Fraction objects
        if not isinstance(oOtherFraction, Fraction):
            raise TypeError('Second value in attempt to add is not a Fraction')
        # use the math package to find the least common multiple
        newDenominator = lcm(self.denominator, oOtherFraction.denominator)

        multiplicationFactor = newDenominator // self.denominator
        equivalentNumerator = self.numerator * multiplicationFactor

        otherMultiplicationFactor = newDenominator // oOtherFraction.denominator
        oOtherFractionEquivalentNumerator = oOtherFraction.numerator * otherMultiplicationFactor

        newNumerator = equivalentNumerator + oOtherFractionEquivalentNumerator

        oAddedFraction = Fraction(newNumerator, newDenominator)
        return oAddedFraction

    def __eq__(self, oOtherFraction):
        # Test for equality
        if not isinstance(oOtherFraction, Fraction):
            return False # not comparing to a fraction
        if (self.numerator == oOtherFraction.numerator) and (self.denominator == oOtherFraction.denominator):
            return True
        else:
            return False

# Test code
oFraction1 = Fraction(1, 3)
oFraction2 = Fraction(2, 5)
print(f'Fraction1: {oFraction1}')
print(f'Fraction2: {oFraction2}')

oSumFraction = oFraction1 + oFraction2
print(f'Sum is {oSumFraction}')

print(f'Are fractions 1 and 2 equal? {oFraction1 == oFraction2}')
print()

oFraction3 = Fraction(-20, 80)
oFraction4 = Fraction(4, -16)
print(f'Fraction3: {oFraction3}')
print(f'Fraction4: {oFraction4}')
print(f'Are fractions 3 and 4 equal? {oFraction3 == oFraction4}')
print()

oFraction5 = Fraction(5, 2)
oFraction6 = Fraction(500, 200)
print(f'Sum of 5/2 and 500/2 is {oFraction5 + oFraction6}')

