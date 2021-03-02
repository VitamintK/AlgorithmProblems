T = int(input())
for t in range(T):
    n,u,r,d,l = map(int, input().split())
    xs = [u,r,d,l]
    if any(x>n for x in xs):
        print("NO")
        continue
    ans = True
    for i, x in enumerate(xs):
        opp = xs[i-2]
        lef = xs[i-1]
        rig = xs[i-3]
        if x == n-1:
            needs = 1 + max(0,opp-(n-2))
            if lef+rig < needs:
                ans = False
        elif x == n:
            needs = 2 if opp==n else 1
            if lef < needs or rig < needs:
                ans = False
    print("YES" if ans else "NO")
