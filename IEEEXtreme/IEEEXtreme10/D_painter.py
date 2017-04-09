t = int(input())
for _ in range(t):
    n = int(input())
    k = list(map(int, input().split()))
    #print(k)
    dp = [[[100000 for _ in range(21)] for i in range(21)] for j in range(500)]
    dp[0][0][k[0]] = 1
    dp[0][k[0]][0] = 1
    for time in range(1,n):
        for i in range(21):
            for j in range(21):
                if(dp[time-1][i][j] != 100000):
                    x = k[time]
                    if(x == i or x== j):
                        dp[time][i][j] = min(dp[time][i][j], dp[time-1][i][j])
                        if(i == 1 or j==1):
                            pass#print(time, i, j, 0)
                            #print(": ", time-1, i, j, dp[time-1][i][j])
                    else:
                        dp[time][i][x] = min(dp[time][i][x], dp[time-1][i][j] + 1)
                        dp[time][x][j] = min(dp[time][x][j], dp[time-1][i][j] + 1)
                        if(i == 1 or j == 1 or x ==1):
                            pass#print(time, i , j, 1)
                            #print(": ", time-1, i, j, dp[time-1][i][j])

    y = 1000000
    for i in range(0,21):
        #print("--", i)
        for j in range(0,21):
            #print("---", j)
            #print(i, j, dp[n-1][i][j])
            y = min(y,dp[n-1][i][j])
    print(y)
