# unfinished

n,m = map(int, input().split())
#dp = [...0, ...01, ...11]
dp = [[0,0,0] for i in range(n+1)]
dp[0][0] = 1 
for i in range(n):
    newdp = [[0,0,0] for i in range(n+1)]
    for j in range(n+1):
        newdp[j][0] = dp[j][1]+dp[j][2]
        if j > 0:
            newdp[j][1] = (dp[j-1][0]*j)%m
            newdp[j][2] = (dp[j-1][1]*j + dp[j-1][2]*j/2)%m
    dp = newdp
    print(dp)
print(dp)
ans = 0
for i in range(n+1):
    ans = (ans+dp[i][1]+dp[i][2])%m
print(ans)