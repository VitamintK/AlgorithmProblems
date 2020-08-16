import bisect

DEBUG = 0
def debug(*args):
    if DEBUG:
        print(*args)

MOD = 1000000007
T = int(input())
for t in range(T):
    N, K, W = map(int, input().split())
    ls = [int(x) for x in input().split()]
    al,bl,cl,dl = map(int, input().split())
    hs = [int(x) for x in input().split()]
    ah, bh, ch, dh = map(int, input().split())
    for i in range(K, N):
        l = ((al*ls[-2]+bl*ls[-1]+cl)%dl)+1
        h = ((ah*hs[-2]+bh*hs[-1]+ch)%dh)+1
        ls.append(l)
        hs.append(h)

    events = []
    # event tuple:
    # (position, type, i)
    # type 0 = start, 1 = end
    # it's good that start will come before end so flush edges don't get counted 
    for i in range(N):
        events.append((ls[i], 0, i))
        events.append((ls[i]+W, 1, i))
    events.sort()
    tot_perim = 0
    ans = 1
    active = [] #contains a non-decreasing (or strictly increasing? not sure whats more elegant) list of current horizontal lines
    # (height, i)
    # width is only up to 20 in this problem, so we don't need a sorted data structure (hopefully)
    last_zero = None
    for event in events:
        pos, typ, i = event
        h = hs[i]
        if typ == 0:
            # new room starting
            if last_zero is None:
                last_zero = pos
            if len(active) == 0:
                last_height = 0
            else:
                last_height = active[-1][0]
            if h > last_height:
                tot_perim += h - last_height
            bisect.insort(active, (h, i))
            temp = tot_perim + active[-1][0] + (pos+W-last_zero)*2
            debug(temp)
            ans *= temp
            ans %= MOD
        else:
            # room ending
            active.remove((h, i))
            if len(active) == 0:
                tot_perim += (pos - last_zero)*2
                last_zero = None
                new_height = 0
            else:
                new_height = active[-1][0]
            if h > new_height:
                tot_perim += h - new_height
    ans %= MOD
    print("Case #{}: {}".format(t+1, ans))
            