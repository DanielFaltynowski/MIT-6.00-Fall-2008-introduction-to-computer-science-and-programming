def fastFibonacci(n, memory):
    global numOfCalls
    numOfCalls = numOfCalls + 1
    if not n in memory:
        memory[n] = fastFibonacci(n - 1, memory) + fastFibonacci(n - 2, memory)
        print(memory)
    return memory[n]


def fibonacci(n):
    memory = {0:1, 1:1}
    return fastFibonacci(n, memory)


numOfCalls = 0
print(fibonacci(6), numOfCalls)

dicti = {0: "a", 1: "b"}
print("a" in dicti)