def barnYardWithSpiders(numHeads, numLegs):
    for numSpiders in range(1, numHeads + 1):
        for numChickens in range(1, (numHeads + 1) - numSpiders):
            numPigs = numHeads - numChickens - numSpiders
            guessLegs = 4 * numPigs + 2 * numChickens + 8 * numSpiders
            if guessLegs == numLegs:
                return [numPigs, numChickens, numSpiders]
    return [None, None, None]

heads = input('Enter number of heads: ')
legs = input('Enter number of legs: ')

ans = barnYardWithSpiders(int(heads), int(legs))

pigs = ans[0]
chickens = ans[1]
spiders = ans[2]

if pigs == None or chickens == None or spiders == None:
    print('There is no solution')
else:
    print('There are', pigs, 'pigs')
    print('There are', chickens, 'chickens')
    print('There are', spiders, 'spiders')