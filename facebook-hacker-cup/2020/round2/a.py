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
    ss = [int(x) for x in input().split()]
    al,bl,cl,dl = map(int, input().split())
    xs = [int(x) for x in input().split()]
    aw, bw, cw, dw = map(int, input().split())
    ys = [int(x) for x in input().split()]
    ah, bh, ch, dh = map(int, input().split())
    for i in range(K, N):
        l = ((al*ss[-2]+bl*ss[-1]+cl)%dl)
        w = ((aw*xs[-2]+bw*xs[-1]+cw)%dw)
        h = ((ah*ys[-2]+bh*ys[-1]+ch)%dh)
        ss.append(l)
        xs.append(w)
        ys.append(h)
    needmore = 0
    needless = 0
    slackup = 0
    slackdown = 0
    for i in range(N):
        l, r = xs[i], xs[i]+ys[i]
        if ss[i] > r:
            needless += ss[i] - r
            slackdown += ys[i]
        elif ss[i] < l:
            needmore += l - ss[i]
            slackup += ys[i]
        else:
            slackdown += ss[i] - l
            slackup += r - ss[i]
    debug(needmore, needless)
    netneed = needmore - needless
    ans = max(needmore, needless)
    if netneed < 0 and slackup < -netneed:
        ans = -1
    elif netneed > 0 and slackdown < netneed:
        ans = -1
    print("Case #{}: {}".format(t+1, ans))

            

    

    