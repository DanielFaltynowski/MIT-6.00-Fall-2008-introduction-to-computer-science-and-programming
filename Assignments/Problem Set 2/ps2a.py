n = input('Enter a number: ')
n = int(n)

def nuggets(n):
    if n < 0: print('Invalid Input!')
    else:
        for i in range(0, n // 6 + 1):
            for j in range(0, n // 9 + 1):
                for k in range(0, n // 20 + 1):
                    result = 6 * i + 9 * j + 20 * k
                    if result == n: 
                        print('You can buy', n, 'nuggets using:')
                        print('\t', i, 'packages of 6 nuggets,')
                        print('\t', j, 'packages of 9 nuggets,')
                        print('\t', k, 'packages of 20 nuggets.')
                        print('\n')
                        return [i, j, k]
        
    print("You can't buy", n, "nuggets!" )
    return None


def cannotBuy(m):
    max = 1
    for n in range(1, m + 1):
        if n < 0: print('Invalid Input!')
        else:
            ans = None
            for i in range(0, n // 6 + 1):
                for j in range(0, n // 9 + 1):
                    for k in range(0, n // 20 + 1):
                        result = 6 * i + 9 * j + 20 * k
                        if result == n: 
                            ans = [i, j, k]
            if ans is None: max = n
    print('Largest number of McNuggets that cannot be bought in exact quantity:', max)
    return max


print('\n\n\nPROBLEM 1.\n')
nuggets(n)
print('\n\n\nPROBLEM 3.\n')
cannotBuy(n)


