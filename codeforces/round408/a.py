n, m, k = [int(x) for x in input().split()]
costs = [int(x) for x in input().split()]
ans = 10000000000
m = m-1
for index, cost in enumerate(costs):
    if cost != 0 and cost <= k:
        ans = min(ans, abs(m-index))
print(ans*10)
