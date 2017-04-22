T = int(input())
for t in range(T):
    d, n = map(int, input().split())
    slowest_time = 0
    for i in range(n):
        k, s = map(int, input().split())
        time = (d - k)/s
        slowest_time = max(time, slowest_time)
    print("Case #{}: {}".format(t+1, d/slowest_time))
