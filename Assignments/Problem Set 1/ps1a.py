# Problem Set 1
# Name: Daniel Faltynowski
# Collaborators: ---
# Time: 0:15
#


def isPrime(n):
    for divisor in range(2, n):
        if n % divisor == 0: return False
    return True


def thousandthPrimeNumber():
    counter = 1
    ans = 1
    while counter != 1000:
        print('It is', counter, 'iteration and ans is equal', ans)
        ans = ans + 2
        if isPrime(ans):
            counter = counter + 1
    return ans


print('1000th prime number is:', thousandthPrimeNumber())