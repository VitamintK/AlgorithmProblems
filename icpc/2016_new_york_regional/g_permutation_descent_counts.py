T = int(input())

MOD = 1001113
DP = [[0 for i in range(101)] for j in range(101)]
DP[1][0] = 1
for i in range(2,101):
    for j in range(i):
        if j == i-1:
            DP[i][j] = 1
        elif i >= 1:
            DP[i][j] = DP[i-1][j] * (j+1)
            if j >= 1:
                DP[i][j] += ((i-j) * DP[i-1][j-1])
                DP[i][j]%=MOD
            
for t in range(T):
    tt, n, v = map(int, input().split())
    print(t+1, DP[n][v])
    
