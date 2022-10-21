'''
Titulo: Order Pizza with None

Objetivo: Ilustrar el uso de None en un keyword parameter.
'''
def orderPizza(size, style='regular', topping=None):
    # Do some calculations based on the size and style
    # Check if a topping was specified
    PRICE_OF_TOPPING = 1.50 # Price for any topping

    if size == 'small':
        price = 10.00
    elif size == 'medium':
        price = 14.00
    else: # large
        price = 18.00

    if style == 'deepdish':
        price += 2.00 # Charge extra for deepdish

    line = f'You have ordered a {size} {style} pizza with'

    if topping is None: # Check if no topping was passed in
        print(f'{line}no toppin')
    else:
        print(f'{line} {topping}')
        price += PRICE_OF_TOPPING

    print(f'The price is ${price}')
    print()

orderPizza('large')

orderPizza('large', style='regular')

orderPizza('medium', style='deepdish', topping='mushrooms')

orderPizza('small', topping='mushrooms')
