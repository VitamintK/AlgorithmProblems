T = int(input())

from functools import lru_cache

@lru_cache(maxsize=None)
def allc(n,x):
    if x == 0:
        return 1
    return allc(n,x-1) * (n-x+1)

@lru_cache(maxsize=None)
def bad(n,x):
    # hmmmmmmmmmmmmmmmmmmmm
    pass

@lru_cache(maxsize=None)
def good(n, x):
    return allc(n, x) - bad(n, x)

@lru_cache(maxsize=None)
def invalid(n, x):
    return (invalid(x-1) + endsat(x-1)) * (n-x+1)

@lru_cache(maxsize=None)
def endsat(n, x):
    return bad(n,x) - invalid(n,x)

for t in range(T):
    n, k = map(int, input().split())
    