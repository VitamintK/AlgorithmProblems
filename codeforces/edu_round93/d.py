R, G, B = map(int, input().split())
rs = [int(x) for x in input().split()]
gs = [int(x) for x in input().split()]
bs = [int(x) for x in input().split()]
rs.sort()
gs.sort()
bs.sort()
sticks = [rs, gs, bs]
# ans = 0
# while sum(len(x)>0 for x in sticks)>1:
#     greed = [(sticks[x][-1], len(sticks[x]), x) if len(sticks[x])>0 else (-100000000000,0,x) for x in range(3)]
#     greed.sort()
#     ans += greed[-1][0]*greed[-2][0]
#     for i in range(1, len(greed)):
#         sticks[greed[i][2]].pop()
# print(ans)
import sys 
sys.setrecursionlimit(1000)
memo = dict()
def dfs(i,j,k):
    if (i,j,k) in memo:
        return memo[(i,j,k)]
    if sum([i==-1,j==-1,k==-1])>1:
        return 0
    a = gs[j]*bs[k] + dfs(i,j-1,k-1) if j>=0 and k>=0 else 0
    b = rs[i]*bs[k] + dfs(i-1,j,k-1) if i>=0 and k>=0 else 0
    c = rs[i]*gs[j] + dfs(i-1,j-1,k) if i>=0 and j>=0 else 0
    r = max(a,b,c)
    memo[(i,j,k)] = r
    return r
ans = dfs(R-1, G-1, B-1)
print(ans)