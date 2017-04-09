dp = dict()
def f(n,k):
    if (n,k) in dp:
        return dp[(n,k)]
    if k == 1:
        return ((n)//2, (n-1)//2)
    a1, b1 = f((n-1)//2, k//2)
    a2, b2 = f(n//2, (k+1)//2)
    if b2 > b1:
        aans = a2
        bans = b2
    elif a2 > a1:
        aans = a2
        bans = b2
    else:
        aans = a1
        bans = b1
    dp[(n,k)] = (aans, bans)
    return (aans, bans)

T = int(input().strip())
for t in range(T):
    n, k = input().split()
    n, k = int(n), int(k)
    maxlr, minlr = f(n,k)
    print("Case #{}: {} {}".format(t+1, maxlr, minlr))
