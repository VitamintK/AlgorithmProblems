import math
def cosh(x):
    return (math.exp(x) + math.exp(-x))/2
def sinh(x):
    return (math.exp(x) - math.exp(-x))/2

eps = 1e-12

d, s = map(int, input().split())
R = 1e13
L = 0
for i in range(123456):
    mid = (L+R)/2

    num = mid * (cosh(d/(2*mid))) - mid

    if num > s:
        L = mid
    else:
        R = mid

a = (L+R)/2
print(2 * a * sinh(d/(2*a)))
