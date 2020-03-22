T = int(input())
for t in range(T):
    n, b = map(int, input().split())
    xs = [int(x) for x in input().split()]
    xs.sort()
    ans = 0
    for i in xs:
        if b >= i:
            ans += 1
            b -= i
    print("Case #{}: {}".format(t+1, ans))