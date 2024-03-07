import math


base = None
inputBase = False
while not inputBase:
    base = input('Enter a base (float): ')
    base = float(base)
    if type(base) == type(1.0): inputBase = True
    else: print('Invalid input!')

height = None
inputHeight = False
while not inputHeight:
    height = input('Enter a height (float): ')
    height = float(height)
    if type(height) == type(1.0): inputHeight = True
    else: print('Invalid input!')

hypotenuse = math.sqrt(base ** 2 + height ** 2)

print('Base:', base, 'Height:', height, 'Hypotenuse:', hypotenuse)