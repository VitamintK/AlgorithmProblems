d, s = map(int, input().split())
l = 0
r = 123456789
eps = 0.000001
import math
for i in range(123456):
    a = (r+l)/2
    term = (d/(2*a))
    sag = 0.5*a*(math.exp(term) + math.exp(-term)) - a
    if sag < s:
        r = a
    else:
        l = a
term = d/(2*l)
print(l * (math.exp(term) - math.exp(-term)))
