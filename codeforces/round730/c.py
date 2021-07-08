import sys
import decimal
import functools

sys.setrecursionlimit(30)

eps = 1e-8
def dfs(c,m,p,v, x):
    # print(c,m,p,v,x)
    # assert abs(c+m+p-1)<1e-10, f'{c,m,p}, {c+m+p}' 
    # ans = prob * p * x
    ans = p * x
    if c > eps:
        if c > v:
            d = v
        else:
            d = c
        if m > eps:
            ans += c * dfs(c-d, m+d/2, p+d/2, v, x+1)
        else:
            ans += c * dfs(c-d, m, p+d, v, x+1)
    if m > eps:
        if m > v:
            d = v
        else:
            d = m
        if c > eps:
            ans += m * dfs(c+d/2, m-d, p+d/2, v, x+1)
        else:
            ans += m * dfs(c, m-d, p+d, v, x+1)
    return ans
    # if c < eps:
    #     pass
    # elif c > v:
    #     if m > 0:
    #         ans += dfs(c-v, m+v/2, p+v/2, v, x+1, prob * c)
    #     else:
    #         ans += dfs(c-v, m, p+v, v, x+1, prob*c)
    # else:
    #     if m > 0:
    #         ans += dfs(0, m+c/2, p+c/2, v, x+1, prob*c)
    #     else:
    #         ans += dfs(0, m, p+c, v, x+1, prob*c)
    
    # if m < eps:
    #     pass
    # elif m > v:
    #     if c > 0:
    #         ans += dfs(c+v/2, m-v, p+v/2, v, x+1, prob*m)
    #     else:
    #         ans += dfs(c, m-v, p+v, v, x+1, prob*m)
    # else:
    #     if c > 0:
    #         ans += dfs(c+m/2, 0, p+m/2, v, x+1, prob*m)
    #     else:
    #         ans += dfs(c, 0, p+m, v, x+1, prob*m)
    # print(c,m,p,v,x, prob, f'{ans=}')
    # return ans

decimal.getcontext().prec = 7
T = int(input())
for t in range(T):
    c,m,p,v = map(float, input().split())
    # c *= 100
    # m *= 100
    # p *= 100
    # v *= 100
    ans = dfs(c,m,p,v,1)
    print(ans)