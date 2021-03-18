T = int(input())
for t in range(T):
    H, M = map(int, input().split())
    h, m = map(int, input().split(':'))
    def increment(h,m):
        m = (m + 1)%M
        if m == 0:
            h = (h + 1)%H
        return h,m
    rmap = {
        '0':'0',
        '1':'1',
        '2':'5',
        '5':'2',
        '8':'8'
    }
    def check(h,m):
        def flip(tstr):
            t = ''
            for digit in reversed(tstr):
                if digit not in rmap:
                    return None
                t += rmap[digit]
            return int(t)
        hs, ms = '{:02}'.format(h), '{:02}'.format(m)
        fm, fh = flip(hs), flip(ms)
        return fh is not None and fm is not None and fh < H and fm < M
    while True:
        if check(h,m):
            print('{:02}:{:02}'.format(h,m))
            break
        h,m = increment(h,m)
