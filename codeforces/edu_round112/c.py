T = int(input())
for t in range(T):
    m = int(input())
    ms = []
    ms.append([int(x) for x in input().split()])
    ms.append([int(x) for x in input().split()])
    ans = 112345678901
    pres = []
    for row in ms:
        # pre[i] = prefix sum up to and including i
        pre = []
        cur = 0
        for x in row:
            cur += x
            pre.append(cur)
        pres.append(pre)
    for i in range(m):
        if i ==0:
            left = 0
        else:
            left = pres[1][i-1]
        if i == m-1:
            right = 0
        else:
            right = pres[0][-1] - pres[0][i]
        ans = min(ans, max(right, left))
    print(ans)
