T = int(input())
for t in range(T):
    n, a, b, c = map(int, input().split())
    ans = [1 for i in range(n)]
    if a + b - c > n:
        print("Case #{}: IMPOSSIBLE".format(t+1))
        continue
    if n == 1:
        # if a == 1 and b == 1 and c == 1:
        print("Case #{}: 1".format(t+1))
        continue
    # if n == 2:
    #     if a == c == b:
    #         for i in range(c):
    #             ans[i] = 2
    # if a== 1
    # else:
    if a == c == b == 1:
        print("Case #{}: IMPOSSIBLE".format(t+1))
        continue
    if (a == c == b) and c != n:
        for i in range(c-1):
            ans[i] = n
        ans[-1] = n
    elif b == c:
        for i in range(a-c):
            ans[i] = n-1
        for i in range(n-b, n-(b-c)):
            ans[i] = n
        for i in range(n-(b-c), n):
            ans[i] = n-1
    else:
        for i in range(a-c):
            ans[i] = n-1
        for i in range(a-c, a):
            ans[i] = n
        for i in range(n-(b-c), n):
            ans[i] = n-1
    print("Case #{}: {}".format(t+1, ' '.join(str(x) for x in ans)))