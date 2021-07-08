T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    s = sum(xs)
    a = s//n
    x = n * (a+1) - s
    ans = x * (n-x)
    print(ans)