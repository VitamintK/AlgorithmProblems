T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    xor = 0
    candidates = []
    for x in xs[:-1]:
        xor ^= x
        candidates.append(xor)
    ok = False
    for candidate in candidates:
        xor = 0
        cands_found = 0
        for x in xs:
            xor ^= x
            if xor == candidate:
                xor = 0
                cands_found += 1
        if xor == 0 and cands_found > 1:
            ok = True
            break
    if ok:
        print("YES")
    else:
        print("NO")
            
        