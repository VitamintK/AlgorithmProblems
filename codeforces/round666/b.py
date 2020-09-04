n = int(input())
xs = [int(x) for x in input().split()]
if n > 100:
    # c can only be 1
    print(sum(x-1 for x in xs))
elif n == 2:
    print(xs[0]-1)
else:
    # c must be under 20
    xs.sort()
    ans = 123456123467819234
    i = 0
    while True:
        i += 1
        cur = 0
        for j in range(len(xs)):
            d = pow(i,j)
            cur += abs(d-xs[j])
            if cur >= ans:
                break
        else:
            ans = min(ans, cur)
            # print(i, cur)
            continue
        break
    print(ans)
