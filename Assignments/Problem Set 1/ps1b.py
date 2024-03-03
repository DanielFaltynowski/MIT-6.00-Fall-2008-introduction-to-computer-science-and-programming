# Problem Set 1
# Name: Daniel Faltynowski
# Collaborators: ---
# Time: 0:10
#


from math import *


def isPrime(n):
    for i in range(2, n):
        if n % i == 0: return False
    return True


def sumOfPrimeLogs(n):
    ans = 0
    for i in range(2, n):
        if isPrime(i):
            ans = ans + log(i)
    return ans


n = input('Enter a number: ')
n = int(n)

if n < 2: print('Invalid input!')
else:
    ans = sumOfPrimeLogs(n)
    print(ans , n, ans / n)