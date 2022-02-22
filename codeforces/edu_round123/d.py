# a little similar to (and simpler than) advent of code 2021 day 22
MOD = 998244353
T = int(input())
for t in range(T):
    n,m,k,q = map(int, input().split())
    qs = []
    for i in range(q):
        x,y = map(int, input().split())
        qs.append((x,y))
    qs = reversed(qs)
    xs = set()
    ys = set()
    ans = 1

    for x,y in qs:
        if x in xs and y in ys:
            continue
        if len(xs)==n or len(ys)==m:
            break
        xs.add(x)
        ys.add(y)
        ans *= k
        ans %= MOD
    print(ans)