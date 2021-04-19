MOD = 1000000007
T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    ans = 1
    for i in range(k):
        ans *= n
        ans %= MOD
    print(ans)