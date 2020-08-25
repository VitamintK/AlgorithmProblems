T = int(input())
for t in range(T):
    p, f = map(int, input().split())
    cs, cw = map(int, input().split())
    s, w = map(int, input().split())
    ans = 0
    if w < s:
        cs, cw = cw, cs
        s, w = w, s
    # now s will be the min of the two
    ans = 0
    for i in range(cs+1):
        pp, ff, ccs, ccw = p, f, cs, cw
        iuses = min(pp//s, i)
        pp -= iuses*s
        ccs -= iuses
        uuses = min(ff//s, ccs)
        ff -= uuses*s
        ccs -= uuses
        #
        iusew = min(pp//w, ccw)
        ccw -= iusew
        uusew = min(ff//w, ccw)
        ff -= uusew*w
        ccw -= uusew
        # print(uusew, uuses, iusew, iuses)
        ans = max(ans, uusew+uuses+iusew+iuses)
    print(ans)