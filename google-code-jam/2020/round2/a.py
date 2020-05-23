T = int(input())

DEBUG = 0
def debug(*args):
    if DEBUG:
        print(*args)

def can(l, r, mid):
    # with mid customers, will the bigger stack surpass the smaller?
    big = max(l,r)
    sml = min(l, r)
    amt = (mid * (mid+1))//2
    # invert result cause im bad at binary search (fn is actually cant)
    return big - amt >= sml

def can2(l, r, mid, surpass):
    # after both stacks have approx evened (after surpass customers)
    # can we serve mid customers?
    nl, nr = get2(l,r,mid,surpass)
    debug(mid, nl, nr)
    return nl >=0 and nr>=0

def get2(l,r,mid,surpass):
    already = (surpass * (surpass+1))//2
    if max(l,r) == l:
        l -= already
    else:
        r -= already
    if max(l,r) == l:
        big = 'l'
    else:
        big = 'r'

    if (big=='l') ^ (surpass%2 == 1):
        # print(mid, surpass)
        l -= ((mid+1)//2) * ((mid+1)//2) - ((surpass+1)//2)*((surpass+1)//2)
        r -= (mid//2)+(mid//2)*(mid//2)  - ((surpass//2)+(surpass//2)*(surpass//2))
    else:
        # print('bp')
        r -= ((mid+1)//2) * ((mid+1)//2) - ((surpass+1)//2)*((surpass+1)//2)
        l -= (mid//2)+(mid//2)*(mid//2)  - ((surpass//2)+(surpass//2)*(surpass//2))
    return l, r

# dmap = {'W': (-1,0), 'E': (1,0), 'N': (0,1), 'S':(0,-1)}
for t in range(T):
    l, r = map(int, input().split())
    lo, hi = 0, 12345678901234567890
    while hi - lo > 1:
        mid = (lo+hi)//2
        if can(l, r, mid):
            lo = mid
        else:
            hi = mid
    surpass = lo
    debug(surpass)  
    lo, hi = surpass, 12345678901234567890
    while hi - lo > 1:
        mid = (lo + hi)//2
        if can2(l, r, mid, surpass):
            lo = mid
        else:
            hi = mid
    ans = lo
    ansl, ansr = get2(l,r,ans,surpass)

    print("Case #{}: {} {} {}".format(t+1, ans, ansl, ansr))