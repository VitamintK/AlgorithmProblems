# based on the code of https://codeforces.com/profile/pajenegod and https://codeforces.com/profile/conqueror_of_tourist
# for printing: they use print('\n'.join(map(str, out))) instead of for ...: print(ans)
# use pypy 3-64
import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        counter = defaultdict(int)
        maxicount = 0
        for j in range(100):
            if i+j >= n:
                break
            x = s[i+j]
            counter[x] += 1
            maxicount = max(maxicount, counter[x])
            if maxicount <= len(counter):
                ans += 1
            if maxicount > 10:
                break
    print(ans)
    