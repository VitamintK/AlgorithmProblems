T = int(input())
for t in range(T):
    n, x = map(int, input().split())
    l = [int(x) for x in input().split()]
    dp = [0 for i in range(n+1)]
    for i in range(1,n+1):
        dp[i] = max(dp[i-1]+l[i-1], 0)
    ans = [max(dp)]
    for k in range(n):
        prevdp = dp
        dp = [0]*(n+1)
        best = 0
        for i in range(1,n+1):
            dp[i] = max(
                dp[i-1]+l[i-1],
                prevdp[i-1]+l[i-1]+x,
                0
            )
            best = max(best, dp[i])
        ans.append(best)
    # ans = []
    # best = -1
    # for k in range(n+1):
    #     left = 0
    #     acc = 0
    #     # argbest = None
    #     remaining = k
    #     for i in range(n):
    #         acc += l[i]
    #         if remaining > 0:
    #             acc += x
    #             remaining -= 1
    #         if acc < 0:
    #             acc = 0
    #             left = i+1
    #             remaining = k
    #         if acc > best:
    #             best = acc
    #             # argbest = (l, i)
    #     ans.append(best)
    print(' '.join(str(a) for a in ans))