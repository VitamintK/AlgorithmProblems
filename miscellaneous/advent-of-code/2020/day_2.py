from collections import defaultdict, deque, Counter
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

ds = [(0,1), (1,0), (-1,0), (0,-1)]

if True:
    ans = 0

    while True:
        try:
            a,b,c = input().split()
            x,y = a.split('-')
            l = b[0]
            # part 1:
            # if int(x)<=c.count(l) <=int(y):
            #     ans+=1

            # part 2:
            x = int(x)-1
            y = int(y)-1
            if (c[x]==l) != (c[y]==l):
                ans+=1
        except EOFError:
            break
    
    print(ans)
else:
    pass