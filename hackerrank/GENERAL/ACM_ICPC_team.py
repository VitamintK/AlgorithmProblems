n, m = map(int, input().split())
l = []
best = 0
amt = 0
for c in range(n):
    s = input()
    for i in l:
        cnt = 0
        for j in range(m):
            if i[j]=='1' or s[j]=='1':
                cnt+=1
        if cnt == best:
            amt+=1
        elif cnt > best:
            best = cnt
            amt = 1
    l.append(s)
print(best)
print(amt)