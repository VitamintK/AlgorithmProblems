T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    ans = 1
    cur = 1
    curdiff = None
    for i, x in enumerate(xs):
        if i == 0:
            continue
        diff = x - xs[i-1]
        if diff == curdiff:
            cur +=1
        else:
            curdiff = diff
            cur = 1
        ans = max(ans, cur)
    print("Case #{}: {}".format(t+1, ans+1))