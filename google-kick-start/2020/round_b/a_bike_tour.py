T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    ans = 0
    for i in range(len(xs)):
        if i == 0 or i == len(xs)-1:
            continue
        if xs[i] > xs[i-1] and xs[i] > xs[i+1]:
            ans += 1
    print("Case #{}: {}".format(t+1, ans))