from functools import lru_cache
import sys
sys.setrecursionlimit(100000000)

MOD = 1000000007
def dfs(root, children):
    ans = 1
    size = 1
    subsizes = []
    assert len(children[root]) <= 2, 'uh oh'
    for c in children[root]:
        if c == root:
            continue
        subans, subsize = dfs(c, children)
        size += subsize
        subsizes.append(subsize)
        ans *= subans
        ans %= MOD
    if len(subsizes) > 1:
        ans *= choose(sum(subsizes), subsizes[0])
        ans %= MOD
    return ans, size

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

@lru_cache(maxsize=None)
def fac(n):
    if n <= 1:
        return 1
    return (n * fac(n-1))%MOD

@lru_cache(maxsize=None)
def choose(n,m):
    num = fac(n) * modinv(fac(n-m), MOD)
    denom = fac(m)
    return num * modinv(denom, MOD)

T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    children = [set() for i in range(n)]
    parent = [-1 for i in range(n)]
    stack = []
    flagged = False
    for i,x in enumerate(xs):
        if x == len(stack)+1:
            if len(stack) == 0:
                parent[i] = i
            else:
                parent[i] = stack[-1]
                children[stack[-1]].add(i)
            stack.append(i)
        elif x <= len(stack):
            # assert(parent[stack[x-1]] == stack[x-2]), (i,x, parent[stack[x-1]], stack[x-2])
            children[parent[stack[x-1]]].discard(stack[x-1])
            if x == 1:
                parent[i] = i
            else:
                children[parent[stack[x-1]]].add(i)
                parent[i] = parent[stack[x-1]]
            children[i].add(stack[x-1])
            parent[stack[x-1]] = i
            for j in range(len(stack)+1-x):
                squashed = stack.pop()
            stack.append(i)
        else:
            flagged = True
            break
        # print(i,x, children, stack, parent)
    if flagged:
        print(f'Case #{t+1}: 0')
        continue
    root = 0
    while root != parent[root]:
        root = parent[root]
    ans = dfs(root, children)
    print(f'Case #{t+1}: {ans[0]}')
