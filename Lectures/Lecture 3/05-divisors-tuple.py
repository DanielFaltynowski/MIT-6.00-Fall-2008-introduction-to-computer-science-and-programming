x = 10
divisors = ()
for i in range(1, x):
    if x % i == 0:
        divisors = divisors + (i, )

print(divisors)