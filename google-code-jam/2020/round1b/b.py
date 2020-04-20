LOWER = -1000000000 #inclusive
UPPER = 1000000001 #exclusive
STEP = (UPPER-LOWER)//3

def process_test(t):
    # find dartboard
    xt, yt = None, None
    for x in range(LOWER,UPPER,STEP):
        for y in range(LOWER,UPPER,STEP):
            print(x,y)
            resp = input()
            if resp == 'CENTER':
                return
            elif resp == 'HIT':
                xt, yt = x, y
                break
            elif resp == 'MISS':
                continue
            else:
                raise ValueError('Server response not accounted for: {}'.format(resp))
        else:
            continue
        break
    # find edges
    top = find_edge(1, xt, yt, UPPER, 1)
    if top == 'CENTER':
        return
    bottom = find_edge(1, xt, LOWER, yt, 0)
    if bottom == 'CENTER':
        return
    right = find_edge(0, yt, xt, UPPER, 1)
    if right == 'CENTER':
        return
    left = find_edge(0, yt, LOWER, xt, 0)
    if left == 'CENTER':
        return
    # find potential middle
    x0 = (left + right)//2
    y0 = (top+bottom)//2 
    # search for center
    for dx in [0,-1,1,2,-2,3,-3,4,-4,5,-5,6,-6,7,-7]:
        for dy in [0,-1,1,2,-2,3,-3,4,-4,5,-5,6,-6,7,-7]:
            x, y = x0+dx, y0+dy
            print(x, y)
            resp = input()
            if resp == 'CENTER':
                return
            elif resp == 'HIT':
                continue
            elif resp == 'MISS':
                raise ValueError('wtf')
            else:
                raise ValueError('Server response not accounted for: {}'.format(resp))


def make_point(axis, other_value, mid):
    if axis == 0:
        return (mid, other_value)
    else:
        return (other_value, mid)

def find_edge(axis, other_value, lo, hi, up_or_right):
    # axis 0 = x, axis 1 = y
    while hi-lo > 1:
        mid = (hi+lo)//2
        x,y = make_point(axis, other_value, mid)
        print(x, y)
        resp = input()
        if resp == 'CENTER':
            return 'CENTER'
        elif resp == 'HIT':
            if up_or_right:
                lo = mid
            else:
                hi = mid
        elif resp == 'MISS':
            if up_or_right:
                hi = mid
            else:
                lo = mid
    return lo

T, A, B = map(int, input().split())
for t in range(T):
    process_test(t)