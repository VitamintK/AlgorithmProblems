T = int(input())

for t in range(T):
    p, q = map(int, input().split())
    horiz = []
    vertic = []
    xs = set()
    ys = set()
    for i in range(p):
        x, y, d = input().split()
        x, y = int(x), int(y)
        if d in "NS":
            vertic.append((x,y,d))
        else:
            horiz.append((x,y,d))
        xs.add(x)
        ys.add(y)
    intersections = dict()
    for x in xs:
        for y in ys:
            intersections[(x,y)] = 0
            intersections[(x,0)] = 0
            intersections[(0,y)] = 0
    for x,y,d in horiz+vertic:
        for (xi, yi) in intersections:
            if d=='N':
                if xi == x and yi <= y:
                    intersections[(xi,yi)] += 1
            elif d == 'S':
                if xi == x and yi >= y:
                    intersections[(xi,yi)] += 1
            elif d == 'E':
                if yi == y and xi >= x:
                    intersections[(xi,yi)] += 1
            else:
                if yi == y and xi <= x:
                    intersections[(xi,yi)] += 1
    ans = (0,-100,-100)
    for xi, yi in intersections:
        ans = max(ans, (intersections[(xi,yi)], -xi, -yi))
    print("Case #{}: {} {}".format(t+1, -ans[1], -ans[2]))