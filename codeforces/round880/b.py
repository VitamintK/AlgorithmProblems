# based on the code of https://codeforces.com/profile/pajenegod and https://codeforces.com/profile/conqueror_of_tourist
# for printing: they use print('\n'.join(map(str, out))) instead of for ...: print(ans)
# use pypy 3-64
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n,k,g = map(int, input().split())
    best_payout = (g-1)//2
    if best_payout * n >= k*g:
        print(g*k)
        continue
    x = g*k
    x_used = (n-1) * best_payout
    x -= x_used
    ans = (n-1) * (best_payout)
    remainder = x%g
    if remainder <= best_payout:
        ans += remainder
    else:
        ans -= g-remainder
    print(ans)
