def squareRoot(x, epsilon=0.001):
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
            return guess
        return None

print(squareRoot(4))
print(squareRoot(9))
