if True:
    ans = 0
    while True:
        try:
            x = int(input())
            x = x//3 - 2
            while x > 0:
                ans += x
                x = x//3 -2
        except EOFError:
            break
    print(ans)
else:
    pass