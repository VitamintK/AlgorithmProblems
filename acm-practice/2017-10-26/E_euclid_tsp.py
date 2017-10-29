inp = input().split()
n = int(inp[0])
p = float(inp[1])
s = float(inp[2])
v = float(inp[3])
import math
l = 0.0000000001
r = 30

def f(c):
    top = n/(p*1000000000) * pow(math.log(n,2), c * math.sqrt(2)) + (s*(1+(1/c))/v)
    return top

eps = 0.000001
for i in range(123456):
    m = (l+r)/2
    if f(m) - f(m+eps) > 0:
        l = m
    else:
        r = m

print(f(l), l)
