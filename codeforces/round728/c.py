T = int(input())
for t in range(T):
    n = int(input())
    ds = [int(x) for x in input().split()]
    ds.sort()
    ans = max(ds)
    run = 0
    for i in range(1,n):
        run += i * (ds[i]-ds[i-1])
        ans -= run
    print(ans)