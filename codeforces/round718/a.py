N = 2050
T = int(input())
for t in range(T):
    n = int(input())
    if n%N != 0:
        print(-1)
        continue
    ans = 0
    m = 20500000000000000000000
    while m > n:
        m//=10
        if m == 0:
            break
        ans += n//m
        n = n-m*(n//m)
    if n != 0:
        print(-1)
    else:
        print(ans)