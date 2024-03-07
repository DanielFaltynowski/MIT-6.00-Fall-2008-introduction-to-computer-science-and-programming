def squareRoot(x, epsilon):
    if not x > 0 or not epsilon > 0: 
        print('Invalid input!')
        return None
    else:
        guess = x / 2.0
        iterations = 0
        while abs(guess * guess - x) >= epsilon and iterations < 100:
            guess = guess - ((guess * guess - x) / (2 * guess))
            iterations = iterations + 1
        if iterations >= 100: 
            print('Not found!')
            return None
        else: return guess

x = input('Enter a number: ')
x = float(x)
print(squareRoot(x, 0.001))