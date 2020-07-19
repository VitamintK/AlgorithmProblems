T = int(input())
for t in range(T):
    n = int(input())
    ps = [int(x) for x in input().split()]
    ans = 0
    record = 0
    for i in range(n):
        if i == 0:
            if n == 1:
                ans += 1
            elif ps[i] > ps[i+1]:
                ans += 1
        elif ps[i] <= record:
            continue
        elif i == n-1 or ps[i] > ps[i+1]:
            ans += 1
        record = max(record, ps[i])
    print("Case #{}: {}".format(t+1, ans))