def squareRootBS(x, epsilon=0.001):
    if not x > 0 or not epsilon > 0: 
        print('Invalid input!')
        return None
    else:
        left = 0
        right = x
        guess = (left + right) / 2.0
        iteration = 0
        while abs(guess * guess - x) > epsilon and iteration < 100:
            if guess * guess < x: left = guess
            else: right = guess
            guess = (left + right) / 2.0
            iteration = iteration + 1
        if iteration < 100:
            return [guess, iteration]
        return None


def squareRootNR(x, epsilon):
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
        else: return [guess, iterations]


x = input('Enter a number: ')
x = float(x)
print('Bisection method:', squareRootBS(x, 0.01))
print('Newton-Raphson method:', squareRootNR(x, 0.001))
print()
print('Bisection method:', squareRootBS(x, 0.001))
print('Newton-Raphson method:', squareRootNR(x, 0.001))
print()
print('Bisection method:', squareRootBS(x, 0.0001))
print('Newton-Raphson method:', squareRootNR(x, 0.001))