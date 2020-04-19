T = int(input())
dmap = {'W': (0,-1), 'E': (0,1), 'N': (-1,0), 'S':(1,0)}
def delta(ltr):
    return dmap[ltr]

MOD = 1000000000

for t in range(T):
    cmd = input()
    multiplier = 1
    multstack = []
    r, c = 0, 0
    for ltr in cmd:
        if ltr == '(':
            continue
        elif ltr == ')':
            multiplier//= multstack.pop()
        elif ltr in dmap:
            dr, dc = delta(ltr)
            r += multiplier * dr
            c += multiplier * dc
            r %= MOD
            c %= MOD
        else:
            m = int(ltr)
            multiplier *= m
            multstack.append(m)
    print("Case #{}: {} {}".format(t+1, c+1, r+1))
    