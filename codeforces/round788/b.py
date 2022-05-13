T = int(input())
for t in range(T):
    n = int(input())
    s = input()
    ks = input().split()
    k = ks[0]
    ks = {ki for ki in ks[1:]}
    ans = 0
    cnt = 0
    for i in range(n):
        if s[i] in ks:
            ans = max(ans, cnt)
            cnt = 1
        else:
            cnt += 1
    print(ans)