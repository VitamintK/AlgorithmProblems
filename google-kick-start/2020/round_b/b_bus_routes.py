T = int(input())
for t in range(T):
    n, d = map(int, input().split())
    xs = [int(x) for x in input().split()]
    day = d
    for x in reversed(xs):
        day = day - day%x
    print("Case #{}: {}".format(t+1, day))