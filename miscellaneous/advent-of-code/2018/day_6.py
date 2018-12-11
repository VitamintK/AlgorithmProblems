if False:
    coords = []
    while True:
        try:
            x, y = map(int, input().split(','))
            coords.append((x,y))
        except EOFError:
            break
    cnt = [0 for i in coords]
    print(coords)
    for i in range(0,1000):
        for j in range(0,1000):
            l = [abs(x-i)+abs(y-j) for x,y in coords]
            if l.count(min(l)) > 1:
                continue
            else:
                cnt[l.index(min(l))]+=1
    print(cnt)
    disq = set()
    for i in range(-100,1000):
        l = [abs(x-i)+abs(y+100) for x,y in coords]
        if l.count(min(l)) > 1:
            continue
        else:
            disq.add(l.index(min(l)))
    for i in range(-100,1000):
        l = [abs(x-i)+abs(y-1000) for x,y in coords]
        if l.count(min(l)) > 1:
            continue
        else:
            disq.add(l.index(min(l)))
    for i in range(-100,1000):
        l = [abs(x+1000)+abs(y-i) for x,y in coords]
        if l.count(min(l)) > 1:
            continue
        else:
            disq.add(l.index(min(l)))
    for i in range(-100,1000):
        l = [abs(x-1000)+abs(y-i) for x,y in coords]
        if l.count(min(l)) > 1:
            continue
        else:
            disq.add(l.index(min(l)))
    print(disq)
    print(cnt)
    ans = 0
    for i, c in enumerate(cnt):
        if i in disq:
            continue
        ans = max(ans, c)
    print(ans)


else:
    coords = []
    while True:
        try:
            x, y = map(int, input().split(','))
            coords.append((x,y))
        except EOFError:
            break
    ans = 0
    print(coords)
    for i in range(20,800):
        for j in range(20,800):
            l = [abs(x-i)+abs(y-j) for x,y in coords]
            if sum(l) < 10000:
                ans+=1
    print(ans)