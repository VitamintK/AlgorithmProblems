import fractions
from functools import lru_cache

# mod stuff
MOD = 1000000007

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
###########


n = int(input())
edges = [[] for i in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    u -=1
    v -=1
    edges[u].append(v)
    edges[v].append(u)

xytable = [[0 for i in range(200)] for j in range(200)]
xytable[0][0] = fractions.Fraction(1,1)
for h in range(200):
    for t in range(200):
        if h+t > 200:
            break
        if t+1 < 200:
            xytable[h][t+1] += xytable[h][t]/2
        if h+1 < 200:
            xytable[h+1][t] += xytable[h][t]/2

@lru_cache(maxsize=None)
def get_f(h1,h2):
    # probability of flipping h1 heads first, before flipping h2 tails
    # i.e. probability of marking a node at height h1 first before marking one at height h2
    ans = 0
    recent = None
    for i in range(h2):
        # print(h1, i, xytable[h1][i])
        ans += xytable[h1][i]
        if recent is not None:
            ans -= recent / 2
        recent = xytable[h1][i]
    return ans

def dfs(heights, ancmap, ancs, root):
    for v in edges[root]:
        if v in heights:
            continue
        heights[v] = heights[root]+1
        for anc in ancs:
            ancmap[v][anc] = 1
        ancs.append(v)
        dfs(heights, ancmap, ancs, v)
        ancs.pop()

def get_ans(root):
    # print('root is', root)
    ans = 0
    heights = {root: 0}
    ancmap = [[0 for i in range(n)] for j in range(n)]
    dfs(heights, ancmap, [root], root)
    # print(ancmap)
    for u in range(n):
        for v in range(u+1, n):
            if ancmap[u][v]:
                # if u is a descendant of v
                # and v is larger than u
                # print('ancestor', u, v, 1)
                ans += fractions.Fraction(1,1)
                continue
            if ancmap[v][u]:
                # if v is a descendant of u
                # and v is larger than u
                continue
            print('get_f', u,v, get_f(heights[v], heights[u]))
            ans += get_f(heights[v], heights[u])
    return ans


ans = 0
for root in range(n):
    print("ROOT IS", root)
    a = get_ans(root) / n
    print(root, a)
    ans += a
print(ans)
print((ans.numerator * modinv(ans.denominator, MOD))%MOD)
