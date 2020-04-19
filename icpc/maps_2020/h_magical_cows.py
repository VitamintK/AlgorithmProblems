c, n, m = map(int, input().split())
cows = []
import math
for i in range(n):
    cow = int(input())
    cows.append(math.ceil(math.log(c/(cow-0.00001), 2)))
# print(cows)
for j in range(m):
    d = int(input())
    ans = 0
    for i in cows:
        if d < i:
            ans += 1
        else:
            ans += pow(2, d-i+1)
    print(ans)