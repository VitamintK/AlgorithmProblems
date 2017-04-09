#this version's logic is correct, but since the testcases were wrong,
#this will not pass all the testcases.
n, m, s, x, y, z = map(int, input().split())
cost = x + y + z
import math
comps = math.ceil(s/n)
if comps * cost <= m:
    print(m - comps*cost))
else :
    print(m%cost)
