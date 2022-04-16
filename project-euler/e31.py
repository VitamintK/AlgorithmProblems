coins = [1,2,5,10,20,50,100,200]

dp = [0 for i in range(201)]
dp[0] = 1
for i in range(len(coins)):
    coin = coins[i]
    for j in range(201):
        if j>=coin:
            dp[j] += dp[j-coin]
print(dp[200])