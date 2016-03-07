n, m, s, x, y, z = map(int, input().split())
cost = x + y + z
import math
comps = s/n
if comps * cost <= m:
    print(int(m - comps*cost))
else :
    print( int(m%cost))
