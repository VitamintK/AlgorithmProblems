T = int(input())

def can(secs):
    # p is man, q is freeze
    qpt = 0
    for p in ps:
        already_added_left = False
        l, r = p, p
        splosions = 0
        while qpt < M:
            q = qs[qpt]
            l = min(q, l)
            r = max(q, r)
            splosions +=1
            time_used = (r-l) + splosions*S + min((p-l),(r-p))
            # if p>=q or not already_added_left:
            #     time_used+=abs(p-q)
                
            # if q < p:
            #     already_added_left = True
            if time_used <= secs:
                qpt += 1
            else:
                break
    return qpt==M

for t in range(T):
    N, M, K, S = map(int, input().split())
    ps = [int(x) for x in input().split()]
    ap, bp, cp, dp = map(int, input().split())
    qs = [int(x) for x in input().split()]
    aq, bq, cq, dq = map(int, input().split())
    for i in range(K, N):
        p = ((ap*ps[i-2]+bp*ps[i-1]+cp)%dp)+1
        ps.append(p)
    for i in range(K, M):
        q = ((aq*qs[i-2]+bq*qs[i-1]+cq)%dq)+1
        qs.append(q)
    ps.sort()
    qs.sort()
    hi = S*M+500000000*10
    lo = -1
    # hi is inclusive, lo is exclusive
    while hi-lo > 1:
        mid = (hi+lo)//2
        if can(mid):
            hi = mid
        else:
            lo = mid
    print("Case #{}: {}".format(t+1, hi))