from collections import defaultdict
import math
T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    good = False
    for i in range(len(xs)):
        for j in range(i):
            m = xs[i]*xs[j]
            rt = int(math.sqrt(m))
            if rt*rt != m:
                good = True
                break
    for i in range(len(xs)):
        rt = int(math.sqrt(xs[i]))
        if rt*rt != xs[i]:
            good = True
    if good:
        print("YES")
    else:
        print("NO")