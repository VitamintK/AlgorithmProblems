T = int(input())
for t in range(T):
    n, m, r, c = map(int, input().split())
    r, c = r-1, c-1
    h = max(n-r-1, r)
    v = max(m-c-1, c)
    print(h+v)