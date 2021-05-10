# holy fuck i'm an idiot... i spent 30 minutes trying to figure out how to minimize k without realizing you don't ned to!!!!!!
from math import gcd
T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    ops = []
    for i in range(1,n):
        if(gcd(xs[i], xs[i-1]) != 1):

            prev = xs[i-2]
            nex = min(xs[i-1], xs[i])
            newval = nex+1
            while gcd(newval,prev)!=1 or gcd(newval,nex)!=1:
                    newval+=1
            ops.append((i,i+1, newval, min(xs[i-1],xs[i])))
            xs[i] = min(xs[i-1],xs[i])
            xs[i-1] = newval
    print(len(ops))
    for op in ops:
        print(*op)