MOD = 1000000007
T = int(input())
for t in range(T):
    n,k = map(int, input().split())
    DP = [[0 for i in range(n+1)] for j in range(k+1)]
    for i in range(k+1):
        DP[i][0] = 1
    for i in range(n+1):
        DP[0][i] = 0
    for i in range(1,k+1):
        for j in range(1,n+1):
            DP[i][j] = (DP[i][j-1] + DP[i-1][n-j])%MOD
    print(DP[-1][-1])