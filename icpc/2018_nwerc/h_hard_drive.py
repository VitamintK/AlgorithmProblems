n, c, b = map(int, input().split())

broken = set(int(x)-1 for x in input().split())

dp = [0,0]

ans = [0 for i in range(n)]

cnt = 0

flag = c%2
for i in range(n):
    if cnt == c:
        break
    if i in broken:
        flag = 1
    else:
        ans[i] = flag
        flag = 1 - flag
    if i > 0 and ans[i] != ans[i-1]:
        cnt +=1
print(''.join(str(x) for x in ans))