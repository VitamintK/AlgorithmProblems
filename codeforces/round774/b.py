T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    xs.sort()
    ans = False
    l = 1
    r = n-1
    blu = xs[0]
    red = 0
    while l < r:
        blu += xs[l]
        l += 1
        if l <= r:
            red += xs[r]
            r -= 1
        if blu < red:
            ans = True
            break
    print("YES" if ans else "NO")