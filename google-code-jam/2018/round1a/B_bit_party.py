#could this just be a binary search problem?
#seems easy for a codejam rnd1b...
#but i don't see anything wrong with this approach
import math
class Cashier:
    def __init__(self, m, s, p):
        self.m = m
        self.s = s
        self.p = p

cashiers = []

def is_possible(time):
    #print(time)
    bits = []
    for cashier in cashiers:
        bits.append(max(0, min((time-cashier.p)//cashier.s, cashier.m)))
    bits.sort(reverse=True)
    tot = sum(bits[:R])
    return tot >= B

T = int(input())
for t in range(T):
    R, B, C = map(int, input().split())
    cashiers = []
    for c in range(C):
        cashiers.append(Cashier(*[int(x) for x in input().split()]))
    maxint = 1000000001
    hi = 1000*maxint + 1000*maxint*maxint + 1001 #for good measure
    lo = 0
    while(hi>lo):
        #print(lo, hi)
        mid = (hi+lo)//2
        if is_possible(mid):
            #print(mid, "worked")
            hi = mid
        else:
            #print(mid, "didn't work")
            lo = mid+1
    print("Case #{}: {}".format(t+1, hi))
        
