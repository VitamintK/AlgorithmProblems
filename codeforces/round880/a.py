# based on the code of https://codeforces.com/profile/pajenegod and https://codeforces.com/profile/conqueror_of_tourist
# for printing: they use print('\n'.join(map(str, out))) instead of for ...: print(ans)
# use pypy 3-64
import sys
input = sys.stdin.readline

from collections import Counter

T = int(input())
for t in range(T):
    n = int(input())
    ls = list(map(int, input().split()))
    m = max(ls)
    c = Counter(ls)
    last = None
    ans = True
    for key in range(0,m+1):
        # print(key, c[key])
        if last is not None and c[key] > last:
            ans = False
            break
        last = c[key]
    print("YES" if ans else "NO")