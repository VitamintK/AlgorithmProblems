from collections import defaultdict, deque, Counter
# d = deque()
# d.append(5)
# x = d.popleft()
import re
# m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist") 
# # or re.search
# >>> m.group(0)       # The entire match
# 'Isaac Newton'
# >>> m.group(1)       # The first parenthesized subgroup.
# 'Isaac'
# >>> m.group(2)       # The second parenthesized subgroup.
# 'Newton'
# >>> m.group(1, 2)    # Multiple arguments give us a tuple.
# ('Isaac', 'Newton')
from heapq import heappush, heappop
# >>> heap = []
# >>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# >>> for item in data:
# ...     heappush(heap, item)
# heap[0] is the smallest item
import string
# string.ascii_lowercase == 'abcde...'
# string.ascii_uppercase == 'ABCDE...'

import sys

sys.setrecursionlimit(100000)

def get_ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))  # copied from mcpower from mserrano on betaveros' recommendation
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)


# Extended Euclid
def extended_euclid(a: int, b: int) -> Tuple[int, int]:
    """
    >>> extended_euclid(10, 6)
    (-1, 2)
    >>> extended_euclid(7, 5)
    (-2, 3)
    """
    if b == 0:
        return (1, 0)
    (x, y) = extended_euclid(b, a % b)
    k = a // b
    return (y, x - k * y)

    # This function find the inverses of a i.e., a^(-1)
def invert_modulo(a: int, n: int) -> int:
    # print('finding', a, n)
    """
    >>> invert_modulo(2, 5)
    3
    >>> invert_modulo(8,7)
    1
    """
    (b, x) = extended_euclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    # print('ans:', b)
    return b

if True:
    ans = 0
    inps = []
    # while True:
    #     try:
    #         inps.append(input())
    #     except EOFError:
    #         break
    t0 = int(input())
    xs = input().split(',')
    xs = [int(i) if i!='x' else None for i in xs]
    # for j in range(1000000):

    #     t = j*521+19

    #     satisfied = True
    #     for dt, y in enumerate(xs):
    #         if y is None:
    #             continue
    #         if (x+j+dt)%y!=0:
    #             satisfied = False
    #             break
    #      if satisfied:
    M = 1
    for i in xs:
        if i is not None:
            M *= i
    ans = 0
    print(M)
    print(list(enumerate(xs)))
    for a, m in list(x for x in enumerate(xs) if x[1] is not None):
        a = m-a
        b = (M//m)
        bp = invert_modulo(b%m,m)
        print(a,m, ':', b, bp)
        ans += b*bp*a
    ans %= M
    print(ans)
    # print(t0, t0 - (t0%M) + ans)
    # for i, j in list(x for x in enumerate(xs) if x[1] is not None):
    #     print('x = {} mod {},'.format(i,j), end=' ')
    # print(ans)
else:
    pass