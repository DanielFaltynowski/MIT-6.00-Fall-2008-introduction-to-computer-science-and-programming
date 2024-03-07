def hanoi(size, fromStack, toStack, spareStack):
    if size == 1:
        print('Move disc from', fromStack, 'to', toStack)
    else:
        hanoi(size - 1, fromStack, spareStack, toStack)
        hanoi(1, fromStack, toStack, spareStack)
        hanoi(size - 1, spareStack, toStack, fromStack)

n = input('Enter a number of levels: ')
n = int(n)
if n <= 0:
    print('Invalid input!')
else:
    hanoi(n, 'A', 'B', 'C')