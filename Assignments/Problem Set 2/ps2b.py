###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###

bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (5, 7, 9)   # variable that contains package sizes

for n in range(1, 150):   # only search for solutions up to size 150
    ## complete code here to find largest size that cannot be bought
    ## when done, your answer should be bound to bestSoFar
    ans = None
    for i in range(0, n // packages[0] + 1):
        for j in range(0, n // packages[1] + 1):
            for k in range(0, n // packages[2] + 1):
                result = packages[0] * i + packages[1] * j + packages[2] * k
                if result == n: 
                    ans = [i, j, k]
    if ans is None: bestSoFar = n

print('Packages', packages, '|', 'Best So Far', bestSoFar)
