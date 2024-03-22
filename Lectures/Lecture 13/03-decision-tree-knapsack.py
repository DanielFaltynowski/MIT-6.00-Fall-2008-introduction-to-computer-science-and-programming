def zeroOneKnapsack(weights, values, index, actualWeight):
    global numCalls
    numCalls = numCalls + 1
    if index == 0:
        if weights[index] <= actualWeight:
            return values[index]
        else:
            return 0
    without_i = zeroOneKnapsack(weights, values, index - 1, actualWeight)
    if weights[index] > actualWeight:
        return without_i
    else:
        with_i = values[index] + zeroOneKnapsack(weights, values, index - 1, actualWeight - weights[index])
    return max(with_i, without_i)


numCalls = 0
weights = [5, 3, 2]
values = [9, 7, 8]
print(zeroOneKnapsack(weights, values, len(values) - 1, 5), numCalls)
weights = [1, 1, 5, 5, 3, 3, 4, 4]
values = [15, 15, 10, 10, 9, 9, 5, 5]
print(zeroOneKnapsack(weights, values, len(values) - 1, 8), numCalls)