import math

primes = []
sieve = set()
M = 100000
for i in range(2,M):
    if i in sieve:
        continue
    primes.append(i)
    for j in range(i*2, M, i):
        sieve.add(j)

def is_prime(x):
    for p in primes:
        if x%p==0:
            return False
        if p > math.sqrt(x)+2:
            break
    return True

def dfs(x, available_digits):
    if x >= 1000000000:
        return -1
    ans = -1
    if is_prime(x):
        s = str(x)
        if all(str(i) in str(x) for i in range(1,len(str(x))+1)):
            ans = max(ans, x)
    for i in list(available_digits):
        available_digits.remove(i)
        ans = max(ans, dfs(x*10+i, available_digits))
        available_digits.add(i)
    return ans

print(dfs(0, {1,2,3,4,5,6,7,8,9}))
