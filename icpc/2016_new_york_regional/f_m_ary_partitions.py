T = int(input())
for t in range(T):
    _, m, n = map(int, input().split())
    multiplier = 1
    DP = [0] * (n+1)
    DP[0] = 1
    mm = 1
    ans = 1
    while mm <= n:
        for i in range(n+1):
            #if i%mm == 0:
            if i >= mm:
                DP[i] += DP[i-mm]
        mm*=m    
    print(t+1, DP[-1])
