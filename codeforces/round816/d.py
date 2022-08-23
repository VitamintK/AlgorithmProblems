import sys
input = sys.stdin.readline

M = 30

n,q = map(int, input().split())

ans = [[None for i in range(M)] for i in range(n)]

edges = [[[] for i in range(M)] for j in range(n)]

for _ in range(q):
    i,j,x = map(int,input().split())
    i-=1
    j-=1
    for k in range(M):
        one = x & 1
        # print(i,j, x, k, one)
        x //= 2
        if j==i:
            ans[i][k] = one
            continue
        if one:
            edges[i][k].append(j)
            edges[j][k].append(i)
        else:
            ans[i][k] = 0
            ans[j][k] = 0
            for neighbor in edges[i][k]:
                ans[neighbor][k] = 1
            for neighbor in edges[j][k]:
                ans[neighbor][k] = 1

ans2 = []
for i in range(len(ans)):
    x = 0
    for k in range(M):
        if ans[i][k] == 1:
            x += (1 << k)
        elif ans[i][k] is None:
            x += 0
            for neighbor in edges[i][k]:
                ans[neighbor][k] = 1
    ans2.append(str(x))
print(' '.join(ans2))
            
