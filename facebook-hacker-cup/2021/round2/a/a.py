T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    # print(n,m)
    freebie = [1 for i in range(m)]
    ans = 0
    ps = [int(x) for x in input().split()]
    ps.sort()
    for i in range(n):
        # print(freebie)
        newps = [int(x) for x in input().split()]
        newps.sort()
        newfreebie = [-1 for i in range(m)]
        needschange = []
        oldfreebs = 0
        l = 0
        for j in range(m):
            while l != m and ps[l] < newps[j]:
                if freebie[l]:
                    oldfreebs += 1
                l += 1
            if l!=m and ps[l] == newps[j]:
                newfreebie[j] = freebie[l]
                l += 1
            else:
                newfreebie[j] = 0
                needschange.append(j)
        for j in range(l, m):
            oldfreebs += freebie[j]
        # print(oldfreebs, needschange)
        for x in needschange:
            if oldfreebs > 0:
                oldfreebs -= 1
            else:
                ans += 1
        # print(f'{ans=}')
        ps, freebie = zip(*sorted(zip(newps, newfreebie), key=lambda x: (x[0], x[1])))
    print(f'Case #{t+1}: {ans}')