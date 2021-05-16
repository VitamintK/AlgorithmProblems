from functools import lru_cache

@lru_cache(maxsize=None)
def get_ans(n, d=-1):
    # print(n, d)
    if n == 1 or n==2:
        return None
    ans = 0
    for polygon in range((n+1)//2, n+1):
        if polygon == n:
            if (d==-1 or d%polygon==0) and polygon!=d:
                ans = max(1,ans)
        elif d==-1 or d%polygon==0:
            subans = get_ans(n-polygon, polygon)
            if subans is not None:
                ans = max(ans, subans)
    if ans == 0:
        return None
    else:
        # print(n,d, ans+1)
        return ans+1
T = int(input())
for t in range(T):
    n = int(input())
    print(f'Case #{t+1}: {get_ans(n)-1}')