# based on the code of https://codeforces.com/profile/pajenegod and https://codeforces.com/profile/conqueror_of_tourist
# for printing: they use print('\n'.join(map(str, out))) instead of for ...: print(ans)
# use pypy 3-64
import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    n,m = map(int, input().split())
    print("? 1 1", flush=True)
    d1 = int(input())
    print('?', n, 1, flush=True)
    d2 = int(input())
    if d1 == n-1-d2:
        # we know the vertical line it lies on
        print("?", d1+1, 1, flush=True)
        y = int(input())
        print("!", d1+1, y+1, flush=True)
        continue
    if d1 == d2:
        # we know the horizontal line it lies on
        print("?", 1, d1+1, flush=True)
        x = int(input())
        print("!", x+1, d1+1, flush=True)
        continue
    if d1 > d2:
        print("!", d1+1, d2+1, flush=True)
    else:
        # d1 < d2
        print("!", n-d2, d1+1, flush=True)
