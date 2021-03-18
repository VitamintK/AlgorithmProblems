# it's the right solution, but it barely TLEs on the huge testcase.
# the fix is either to use C++ or to get all factors by doing a dfs on prime factors instead of checking each possible divisor up t sqrt(x)

import math
T = int(input())
sieve = [i for i in range(20000005)]
sieve[0] = -1
sieve[1] = 1
upbound = int(math.sqrt(len(sieve))+2)
for i in range(2, upbound):
    if sieve[i] == i:
        for j in range(i, len(sieve), i):
            sieve[j] = i

cache = dict()
def get_factors(n):
    if n in cache:
        return cache[n]
    factors = []
    for i in range(1,int(math.sqrt(n)+1)):
        if n%i == 0:
            factors.append(i)
            if i*i != n:
                factors.append(n//i)
    cache[n] = factors
    return factors

powmap = [1,2,4,8,16,32,64,128,256,512,1024]
for t in range(T):
    c, d, x = map(int, input().split())
    factors = get_factors(x)
    ans = 0
    # print(x, factors)
    for factor in factors:
        if (x//factor + d)%c != 0:
            continue
        E = (x//factor+d)//c
        if E == 0:
            continue
        primes = set()
        p = E
        while p != 1:
            primes.add(sieve[p])
            p //= sieve[p]
        # print(E, primes)
        ans += powmap[len(primes)]
    print(ans)