T = int(input())
from bisect import bisect_left
def binary_search(l, v):
    return bisect_left(l, v)
    
types = "BG BR BY GR GY RY".split()
for t in range(T):
    n, q = map(int, input().split())
    xs = input().split()
    d = {k: [] for k in types}
    for i in range(n):
        d[xs[i]].append(i)
    for i in range(q):
        x, y = map(int, input().split())
        x, y = x-1, y-1
        if x > y:
            x, y = y, x
        if len(set(xs[x]) & set(xs[y])) > 0:
            print(abs(y - x))
        else:
            best = 999999999
            for k in types:
                if k == xs[x] or k == xs[y]:
                    continue
                if len(d[k]) == 0:
                    continue
                m = binary_search(d[k], x+1)
                if m == len(d[k]):
                    m -= 1
                best = min(best, abs(d[k][m] - y) + abs(d[k][m] - x))
                if m + 1 < len(d[k]):
                    best = min(best, abs(d[k][m+1] - y) + abs(d[k][m+1] - x))
                if m - 1 >= 0:
                    best = min(best, abs(d[k][m-1] - y) + abs(d[k][m-1] - x))
            if best == 999999999:
                print(-1)
            else:
                print(best)