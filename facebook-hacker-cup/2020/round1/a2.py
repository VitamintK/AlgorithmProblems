# I read the problem description incorrectly and thought it said non-decreasing 
# instead of non-increasing, which is actually the description for a3, so I solved a3 first.
import bisect
from sortedcontainers import SortedList

DEBUG = 0
def debug(*args):
    if DEBUG:
        print(*args)

MOD = 1000000007
T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    ls = [int(x) for x in input().split()]
    al,bl,cl,dl = map(int, input().split())
    ws = [int(x) for x in input().split()]
    aw, bw, cw, dw = map(int, input().split())
    hs = [int(x) for x in input().split()]
    ah, bh, ch, dh = map(int, input().split())
    for i in range(K, N):
        l = ((al*ls[-2]+bl*ls[-1]+cl)%dl)+1
        h = ((ah*hs[-2]+bh*hs[-1]+ch)%dh)+1
        w = ((aw*ws[-2]+bw*ws[-1]+cw)%dw)+1
        ls.append(l)
        hs.append(h)
        ws.append(w)
    debug(ls, hs, ws)
    # ok I actually have no idea how to solve this without a 
    # self balancing BST so I think I'm going to switch to C++...
    # nvm there's a sorted container library for python and I guess the good thing about
    # facebook hacker cup is that you can use imported 3rd party libraries
    sl = SortedList()
    ans = 1
    tot_perim = 0
    # here's the algorithm:
    # use this sorted datastructure (BST) to maintain all relevant start/end events of rectangles
    # relevant means that the event is not entirely hidden underneath another rectangle.
    # upon inserting a new rectangle, delete all events between start and end (inclusive)
    #   (we can do this indiscriminately bc each new height is non-decreasing)
    # and subtract all deleted events' vertical edge contributions to tot_perim
    # then add the new vertical edge contributions and any new horizontal edge contributions
    #
    # we can store the height of events as the height of the segment to their left?
    # (so we also implicitly/explicitly? store the height of +inf as 0)
    # (position, left_segment_height)
    sl.add((123456789123456789, 0))
    for i in range(N):
        l, h, w = ls[i], hs[i], ws[i]
        posl = l
        posr = l+w
        left = sl.bisect_left((posl,0))
        right = sl.bisect_right((posr,1234567890123456))
        previously_covered = 0
        # debug(sl)
        r_is_zero = sl[right][1] == 0
        l_is_zero = sl[left][1] == 0
        for i in range(left, right+1):
            pos, left_height = sl[i]
            if left_height != 0:
                p = min(pos, posr)
                previously_covered += min(p-posl, p-sl[i-1][0])
            else:
                if posl <= pos <= posr:
                    # i guess this is only false when i == right
                    tot_perim -= h
                    # debug('removing from cur edge')
                    del sl[i]
                    sl.add((pos, h))
                if i != left:
                    tot_perim -= h
                    # debug('removing from left edge')
        new_cover = (w - previously_covered)*2
        # debug('--', new_cover)
        tot_perim += new_cover
        # left_edge = max(h - sl[left][1], 0)
        # debug('---', left_edge)
        # tot_perim += left_edge
        # right_edge = max(h - sl[right][1], 0)
        # debug('---', right_edge)
        # tot_perim += right_edge

        # FUCK we don't need to rewrite individual edges... we should just delete the entire 
        # sl[left:right]...... but I didn't realize this so I missed my submission timing window
        # fuc!K    
        if r_is_zero:
            sl.add((posr, h))
            tot_perim += h
        if l_is_zero:
            sl.add((posl, 0))
            tot_perim += h
        debug(tot_perim)
        ans *= tot_perim
        ans %= MOD
    print("Case #{}: {}".format(t+1, ans))

            

    

    