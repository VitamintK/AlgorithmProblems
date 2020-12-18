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

# def process(s):
#     tokens = tokenize(s)
#     return get_ans(tokens)
    


# def get_ans(tokens):
#     parendepth = 0
#     buff = []
#     lastparen = None
#     ntokens = []
#     for token in tokens:
#         if token == '(':
#             parendepth += 1
#             lastparen = '('
#         elif token == ')':
#             parendepth -= 1
#             if lastparen == '(':
#                 ntokens.append(get_ans(buff))
#             lastparen = ')'

class NewNum:
    def __init__(self, n):
        self.n = n
    def __add__(self, r):
        return NewNum(self.n * r.n)
    def __mul__(self,r):
        return NewNum(self.n + r.n)

if True:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    for inp in inps:
        # ans += process(inp)
        inp = inp.translate(str.maketrans('+*', '*+'))
        r = re.compile('(\d+)')
        inp = r.sub(r'NewNum(\1)', inp)
        inp = 'x = ' + inp
        print(inp)
        exec(inp)
        ans += x.n
        
    print(ans)
else:
    pass