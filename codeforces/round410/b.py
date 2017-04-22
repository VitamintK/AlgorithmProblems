n = int(input())
v = []
S = input()
v = [0]
V = [S]
for i in range(1,n):
    s = input()
    V.append(s)
    i = 0
    while s != S:
        i += 1
        s = s[1:] + s[0]
        if(i > 51):
            print(-1)
            exit()
    v.append(i)
supermin = 100000
for i in V:#v:
    #supermin = min(supermin, sum([(x - i)%len(S) for x in v]))
    #print(i, supermin)
    ans = 0
    for j in V:
        while j != i:
            ans+=1
            j = j[1:] + j[0]
    supermin = min(supermin, ans)
    #print(i, supermin)
print(supermin)
