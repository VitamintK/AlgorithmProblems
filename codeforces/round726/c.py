T = int(input())
for t in range(T):
    n = int(input())
    hs = [int(x) for x in input().split()]
    hs.sort()
    mindiff = 112345678901
    argmindiff = None
    for i in range(1,len(hs)):
        if hs[i] - hs[i-1] < mindiff:
            mindiff = hs[i] - hs[i-1]
            argmindiff = i-1
    if hs[1] - hs[0] == mindiff:
        print(*([hs[0]] + hs[2:] + [hs[1]]))
    else:
        print(*(hs[argmindiff+1:] + hs[:argmindiff+1]))