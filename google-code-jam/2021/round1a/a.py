T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    ans = 0
    prev = 0
    # ys = []
    for x in xs:
        if x > prev:
            prev = x
            continue
        if str(prev).startswith(str(x)):
            if str(prev+1).startswith(str(x)):
                prev = prev+1
                ans += len(str(prev)) - len(str(x))
                continue
        while x <= prev:
            x *= 10
            ans += 1
        prev = x
    print(f'Case #{t+1}: {ans}')