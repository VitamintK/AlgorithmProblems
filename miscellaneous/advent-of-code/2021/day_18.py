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
from functools import lru_cache
# @lru_cache(maxsize=None)

import sys

sys.setrecursionlimit(100000)

def get_ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))  # copied from mcpower from mserrano on betaveros' recommendation
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)

class Num:
    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent
    def get_ans(self):
        return self.val
    def __repr__(self):
        return f'{self.val}'

class Snailfish:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent
    def __add__(self, r):
        ans = Snailfish(self, r, self.parent)
        ans.x.parent = ans
        ans.y.parent = ans
        ans.reduce()
        return ans
    def __repr__(self):
        return f'[{self.x.__repr__()},{self.y.__repr__()}]'
    def reduce(self):
        while True:
            print(self)
            stack = [(self, 0)]
            exploded = False
            while len(stack) > 0:
                ex, depth = stack.pop()
                if not isinstance(ex, Snailfish):
                    continue
                if depth >= 4:
                    ex.explode()
                    exploded = True
                    break
                stack.append((ex.y, depth+1))
                stack.append((ex.x, depth+1))
            if exploded:
                continue
            stack = [(self)]
            split = False
            while len(stack) > 0:
                ex = stack.pop()
                if isinstance(ex, Snailfish):
                    stack.append(ex.y)
                    stack.append(ex.x)
                else:
                    if ex.val >= 10:
                        print('split')
                        if isinstance(ex.parent.x, Num) and ex.parent.x.val >= 10:
                            ex.parent.x = Snailfish(None, None, ex.parent)
                            ex.parent.x.x = Num(ex.val//2, ex.parent.x)
                            ex.parent.x.y = Num((ex.val+1)//2, ex.parent.x)
                        else:
                            tf = Snailfish(None, None, ex.parent)
                            tf.x = Num(ex.val//2, tf)
                            tf.y = Num((ex.val+1)//2, tf)
                            ex.parent.y = tf
                        split = True
                        break
            if split == True:
                continue
            break
                
    def explode(self):
        print('boom')
        me = self
        while me.parent is not None and me is me.parent.x:
            me = me.parent
        if me.parent is not None:
            if not isinstance(me.parent.x, Snailfish):
                me.parent.x.val += self.x.val
            else:
                me = me.parent.x
                while isinstance(me.y, Snailfish):
                    me = me.y
                me.y.val += self.x.val
        
        me = self
        while me.parent is not None and me is me.parent.y:
            me = me.parent
            # print(f'{me=}')
        if me.parent is not None:
            # print('tru')
            if not isinstance(me.parent.y, Snailfish):
                me.parent.y.val += self.y.val
            else:
                me = me.parent.y
                while isinstance(me.x, Snailfish):
                    me = me.x
                # print('doing it')
                me.x.val += self.y.val
        if self.parent.x is self:
            self.parent.x = Num(0, self.parent)
        else:
            self.parent.y = Num(0, self.parent)
    def get_ans(self):
        return self.x.get_ans() * 3 + self.y.get_ans() * 2
            


def change(l, p=None):
    if isinstance(l, list):
        ans = Snailfish(None, None, p)
        ans.x = change(l[0], ans)
        ans.y = change(l[1], ans)
        return ans
    else:
        return Num(l, p)

if True:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(eval(input()))
            # inps.append(change(eval(input())))
        except EOFError:
            break
    # x = inps[0]
    # for i in inps[1:]:
    #     x = x + i
    #     print(x)
    # print(x.get_ans())
    for i in range(len(inps)):
        for j in range(i+1, len(inps)):
            t = change(inps[i]) + change(inps[j])
            ans = max(ans, t.get_ans())
            t = change(inps[j]) + change(inps[i])
            ans = max(ans, t.get_ans())
    print(ans)

else:
    pass