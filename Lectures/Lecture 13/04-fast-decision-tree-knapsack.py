def fastZeroOneKnapsack(weights, values, index, actualWeight, memory):
    global numCalls
    numCalls = numCalls + 1
    try:
        return memory[(index, actualWeight)]
    except KeyError:
        if index == 0:
            if weights[index] <= actualWeight:
                memory[(index, actualWeight)] = values[index]
                return values[index]
            else:
                memory[(index, actualWeight)] = 0
                return 0
        without_i = fastZeroOneKnapsack(weights, values, index - 1, actualWeight, memory)
        if weights[index] > actualWeight:
            memory[(index, actualWeight)] = without_i
            return without_i
        else:
            with_i = values[index] + fastZeroOneKnapsack(weights, values, index - 1, actualWeight - weights[index], memory)
        response = max(with_i, without_i)
        memory[(index, actualWeight)] = response
        return response


def zeroOneKnapsack(weights, values, index, actualWeight):
    memory = {}
    return fastZeroOneKnapsack(weights, values, index, actualWeight, memory)


numCalls = 0
weights = [5, 3, 2]
values = [9, 7, 8]
print(zeroOneKnapsack(weights, values, len(values) - 1, 5), numCalls)
weights = [1, 1, 5, 5, 3, 3, 4, 4]
values = [15, 15, 10, 10, 9, 9, 5, 5]
print(zeroOneKnapsack(weights, values, len(values) - 1, 8), numCalls)