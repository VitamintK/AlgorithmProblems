T = int(input())
for t in range(T):
    price = int(input())
    n = int(input())
    coins = []
    for i in range(n):
        coins.append(int(input()))
    coins.sort(reverse=True)
    dp = dict()
    ndp = dict()
    cap = price+10001
    dp[0] = 0
    for coin in coins:
        for j in dp:
            if j in ndp:
                ndp[j] = min(ndp[j], dp[j])
            else:
                ndp[j] = dp[j]
            if j+coin > cap:
                continue
            if j+coin >= price:
                cap = j+coin
            if j+coin in ndp:
                ndp[j+coin] = min(ndp[j+coin], dp[j]+1)
            else:
                ndp[j+coin] = dp[j]+1
        # if price in ndp:
        #     break
        dp, ndp = ndp, dp
    for j in range(price, cap+1):
        if j in dp:
            print(j, dp[j])
            break