def fibonacci(n):
    global numOfIters
    numOfIters = numOfIters + 1
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


numOfIters = 0
print(fibonacci(25), numOfIters)