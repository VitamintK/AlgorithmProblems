n = int(input())
inps = []
ans = 0
for i in range(n):
    a,c = map(int, input().split())
    ans += c
    inps.append((a,c))
inps.sort()
# ans += inps[-1][0] - inps[0][0]
topcover = inps[0][0]
for i in range(len(inps)):
    if inps[i][0] > topcover:
        ans += inps[i][0] - topcover
        # print(ans)
    topcover = max(topcover, inps[i][0]+inps[i][1])
print(ans)