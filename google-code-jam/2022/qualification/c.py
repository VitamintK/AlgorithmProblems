T = int(input())
for t in range(T):
    n = int(input())
    ss = [int(x) for x in input().split()]
    ss.sort()
    ans = 0
    for x in ss:
        if x >= ans+1:
            ans += 1
    print(f"Case #{t+1}: {ans}")
            