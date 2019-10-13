T = int(input())

for t in range(T):
    n = int(input())
    mols = []
    for i in range(n):
        c, j = map(int, input().split())
        mols.append((c,j))
    SMALL_NUM = 1/5123456789
    slopes = [1+SMALL_NUM, 1-SMALL_NUM]
    for i in range(n):
        for j in range(i):
            a = mols[i]
            b = mols[j]
            if a[0] == b[0]:
                slopes.append(5123456789)
                continue
            slope = -((a[1]-b[1])/(a[0]-b[0]))
            if slope < 0:
                continue
            slopes.append(slope+SMALL_NUM)
            if slope != 0:
                slopes.append(slope-SMALL_NUM)
    orders = set()
    for slope in slopes:
        weights = [(mol[0]*slope + mol[1], i) for i, mol in enumerate(mols)]
        weights.sort()
        # print(slope, tuple(weight[1] for weight in weights), weights)
        orders.add(tuple(weight[1] for weight in weights))
    ans = len(orders)
    #print(orders)
    print("Case #{}: {}".format(t+1, ans))

