n = int(input())
l = [int(x) for x in input().split()]
from collections import Counter
a = Counter(l)
ans = 0
ans += min(a[2], a[1])
a[1] -= ans
ans += a[1]//3
print(ans)