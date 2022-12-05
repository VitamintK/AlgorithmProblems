# based on the code of https://codeforces.com/profile/pajenegod and https://codeforces.com/profile/conqueror_of_tourist
# for printing: they use print('\n'.join(map(str, out))) instead of for ...: print(ans)
# use pypy 3-64
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    s = input()
    totals = {'0': 0, '1': 0}
    prev = None
    cum = 0
    best = 0
    for i in range(n):
        x = s[i]
        if x == prev:
            cum +=1
        else:
            best = max(best, cum)
            cum = 1
        prev = x
        totals[x] += 1
    best = max(best, cum)
    ans = totals['0'] * totals['1']
    ans = max(ans, best*best)
    print(ans)