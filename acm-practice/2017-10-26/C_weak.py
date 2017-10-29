n = int(input())
while n != -1:
    am = []
    for i in range(n):
        am.append([int(x) for x in input().split()])
    ans = []
    for i in range(n):
        part = False
        for j in range(n):
            for k in range(n):
                if am[i][j] and am[i][k] and am[j][k]:
                    part = True
        if not part:
            ans.append(i)
    print(' '.join(map(str,ans)))
    n = int(input())
