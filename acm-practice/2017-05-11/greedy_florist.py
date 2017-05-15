#https://www.hackerrank.com/challenges/greedy-florist
n, k = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()
prices = prices[:n]
f = 0
ans = 0
for i in reversed(prices):
    ans += i * ((k+f)//k)
    f += 1
print(ans)