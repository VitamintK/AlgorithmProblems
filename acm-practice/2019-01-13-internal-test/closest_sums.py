T = 0
while True:
    T += 1
    try:
        n = int(input())
    except EOFError:
        break
    print("Case {}:".format(T))
    xs = []
    for i in range(n):
        xs.append(int(input()))
    xs.sort()
    m = int(input())
    for i in range(m):
        p = int(input())
        ans = None
        best = 100000000000000
        l = 0
        r = n-1
        while r - l > 0:
            sm = xs[l]+xs[r]
            diff = p - sm
            if abs(diff) < best:
                best = abs(diff)
                ans = sm
            if diff == 0:
                break
            elif diff > 0:
                l += 1
            else:
                r -= 1

            
        print("Closest sum to {} is {}.".format(p, ans))