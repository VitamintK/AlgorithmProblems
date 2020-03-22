T = int(input())
for t in range(T):
    n, k, p = map(int, input().split())
    stacks = []
    for i in range(n):
        stack = [int(x) for x in input().split()]
        suff = [0]
        # a = 0
        for j in stack:
            suff.append(suff[-1] + j)
        stacks.append(suff)
    # DP[stack][used] = max(DP[stack-1][used-X] + stacks[X])
    DP = [0 for i in range(p+1)]
    new_DP = [0 for i in range(p+1)]
    for i in range(n):
        for j in range(min(p+1, (i+1)*(k+1))):
            for l in range(min(j+1, k+1)):
                new_DP[j] = max(new_DP[j], DP[j-l] + stacks[i][l])
        DP, new_DP = new_DP, DP
        # print(DP)
    print("Case #{}: {}".format(t+1, DP[p]))