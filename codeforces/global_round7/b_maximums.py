# https://codeforces.com/contest/1326/problem/B

n = int(input())
xs = [int(x) for x in input().split()]

ans = []
pmax = 0
for x in xs:
    ans.append(x + pmax)
    pmax = max(ans[-1], pmax)
print(' '.join(str(x) for x in ans))