T = int(input())
import math
from decimal import *
def fn(a,b,k):
    return (k-1) + (a+k-1)//k + (b+k-1)//k
for t in range(T):
    a, b = map(int, input().split())
    k = int(Decimal(a+b).sqrt())
    ans = a+b
    for i in range(-100,100):
        kk = k+i
        if kk < 1 or kk > a+b:
            continue
        ans = min(ans, fn(a,b,kk))
    # x,y,z = fn(a,b,k), fn(a,b,k-2), fn(a,b,k+2)
    # assert x<=y and x<=z, (x,y,z)
    print(ans)