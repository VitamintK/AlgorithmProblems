# just brute force i suppose?

M = 112345
# M = 10000000
primes = set()
sieve = set()
for i in range(2,M):
    if i not in sieve:
        primes.add(i)
        for j in range(i*2, M, i):
            sieve.add(j)
print('primes computed')

# brute force
best = 0
argbest = None
for a in range(-999, 1000):
    for b in range(-100, 1001):
        n = 0
        while n*n+a*n+b in primes:
            n += 1
        if n*n+a*n+b > M:
            print('uh oh')
        if n > best:
            best = n
            argbest = a*b
print(best, argbest)