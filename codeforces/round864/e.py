from functools import lru_cache
import math
@lru_cache
def totient(x):
    while x != 1:
        x //= sieve[x]

    # ans = 0
    # for i in range(1,x):
    #     if math.gcd(i,x) == 1:
    #         ans += 1
    # return ans

sieve = [0 for i in range(5000000)]

for i in range(2,10000):
    if sieve[i] == 0:
        for j in range(i, 5000000, i):
            sieve[j] = i

