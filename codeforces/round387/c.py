n, q = [int(x) for x in input().strip().split()]
asdf = []
for i in range(q):
    t, k, d = [int(x) for x in input().strip().split()]
    asdf.append((t,k,d))
servers = [0]*n
for t,k,d in asdf:
    for ind, i in enumerate(servers):
        if i < t:
            servers[ind] = 0
    if len([x for x in servers if x==0]) >= k:
        countr = k
        used=[]
        for ind, i in enumerate(servers):
            if countr == 0:
                break
            if i == 0:
                servers[ind] = t + d - 1
                used.append(ind+1)
                countr-=1
        print(sum(used))
    else:
        print(-1)
#dammit times out in python :((((
