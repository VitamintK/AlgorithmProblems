from functools import lru_cache


@lru_cache(maxsize=None)
def dfs(n, left):
    # print(n,left)
    if left == 0:
        return 1
    ans = 0
    if left < n:
        return ans
    for x in range(2*n,left+1,n):
        if (left-x)%x == 0:
            subans = dfs(x, left-x)
            if subans is not None:
                ans = max(ans, subans)
    if ans == 0:
        return None
    else:
        ans += 1
        return ans

def get_ans(n):
    ans = 1
    for i in range(3,n//2 +1):
        if (n-i)%i == 0:
            subans = dfs(i, n-i)
            if subans is not None:
                ans = max(ans, subans)
    return ans

T = int(input())
for t in range(T):
    n = int(input())
    print(f'Case #{t+1}: {get_ans(n)}')