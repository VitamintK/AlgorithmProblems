T = int(input())
for t in range(T):
    a0, a1, a2 = map(int, input().split())
    b0, b1, b2 = map(int, input().split())
    #best is to match 2 with 1
    # match 0 with 2
    # and match 1 with 1
    # b a 0 1 2
    # 0   0 0 0
    # 1   0 0 2
    # 2   0 -2 0
    ans = 0
    goods = min(a2, b1)
    ans += goods*2
    # b = b0 + b1-ans
    # a = a0 + a2-ans
    n = a0+a1+a2 - goods
    if a1 + b2 > n:
        ans -= (b2 + a1 - n) * 2
    print(ans)

