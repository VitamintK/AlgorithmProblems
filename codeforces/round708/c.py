###
### doesn't work.  I should have tried to solve c small first ;_;
###
T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    if k == n:
        ans = [1 for i in range(k)]
    elif k-1 >= (n+1)//2:
        ans = [n-k+1]
        ans.extend([1 for i in range(k-1)])
    elif n==6 and k==3:
        ans = [2,2,2]
    else:
        if k == 3 and n%4==0:
            ans = [n//2, n//4, n//4]
        else:
            kk = k-2
            m = (n-kk)//2
            if m+m+kk < n:
                ans = [m,m,2] + [1 for i in range(kk-1)]
            else:
                ans = [m,m] + [1 for i in range(kk)]
    assert sum(ans) == n, f'{ans} -- {n,k}'
    # assert lcm(*ans) <= n/2
    print(*ans)
    