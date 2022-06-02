from collections import Counter, defaultdict


T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    c = Counter(xs)
    if any(c[k]==1 for k in c):
        print(-1)
        continue
    d = defaultdict(list)
    for i, x in enumerate(xs):
        d[x].append(i)
    ans = [None for i in range(n)]
    for k in d:
        for i in range(len(d[k])):
            ans[d[k][i]] = d[k][i-1]
    print(*[x+1 for x in ans])