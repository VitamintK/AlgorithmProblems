T = int(input())
for t in range(T):
    n = int(input())
    cs = [int(x) for x in input().split()]
    bests = [cs[0], cs[1]]
    totals = [cs[0],cs[1]]
    ans = 12345677890123409875678
    for i in range(2, n+1):
        firsts = i - i//2 - 1
        seconds = i//2 - 1
        cost = bests[0]*(n-firsts) + (totals[0]-bests[0]) + bests[1]*(n-seconds) + (totals[1]-bests[1])
        ans = min(ans, cost)
        # print(i, cost, bests)
        if i < n:
            index = i%2
            bests[index] = min(bests[index], cs[i])
            totals[index] += cs[i]
    print(ans)