import math
T = int(input())
for t in range(T):
    n = int(input())
    while math.gcd(n, sum(int(x) for x in str(n))) == 1:
        n += 1
    print(n)