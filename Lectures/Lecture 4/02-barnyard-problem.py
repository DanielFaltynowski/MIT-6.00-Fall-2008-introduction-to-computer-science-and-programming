def barnYard(numHeads, numLegs):
    for numChickens in range(1, numHeads + 1):
        numPigs = numHeads - numChickens
        guessLegs = 4 * numPigs + 2 * numChickens
        if guessLegs == numLegs:
            return [numPigs, numChickens]
    return [None, None]


heads = input('Enter number of heads: ')
legs = input('Enter number of legs: ')

ans = barnYard(int(heads), int(legs))

pigs = ans[0]
chickens = ans[1]

if pigs == None or chickens == None:
    print('There is no solution')
else:
    print('There are', pigs, 'pigs')
    print('There are', chickens, 'chickens')