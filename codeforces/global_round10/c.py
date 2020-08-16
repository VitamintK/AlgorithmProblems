T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    ans = 0
    for i in reversed(range(1, n)):
        if xs[i-1]> xs[i]:
            ans += xs[i-1]-xs[i]
    print(ans)