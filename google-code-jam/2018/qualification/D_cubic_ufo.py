#this is only for small testcases
#i finished this solution after the contest ended.  there's no upsolving yet,
#so i don't know if this would have passed the testcases for small.

import math
def find_ans(angle):
    """angle in degrees"""
    ang1 = (math.pi * angle)/180
    ang2 = (math.pi * (90-angle))/180
    return math.cos(ang1) + math.cos(ang2)
T = int(input())
for t in range(T):
    a = float(input())
    hi = 45
    lo = 0
    while(hi - lo > 0.0000001):
        mid = (hi+lo)/2
        x = find_ans(mid)
        if x < a:
            lo = mid
        else:
            hi = mid
    #print(x)
    print("Case #{}:".format(t+1))
    #print(mid)
    ang1 = (math.pi * (90-mid))/180
    ang2 = (math.pi*mid)/180
    print(0, 0, 0.5)
    print(math.cos(ang1)/2, math.sin(ang1)/2, 0)
    print(-math.cos(ang2)/2, math.sin(ang2)/2, 0)

