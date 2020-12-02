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

if True:
    ans = 0
    xs = []
    while True:
        try:
            a = int(input())
            # xs = [int(x) for x in input().split()]
            xs.append(a)
            for j in xs:
                if 2020-a-j in xs:
                    print(a,j)
                    print((2020-a-j) * a * j)
        except EOFError:
            break
    print(ans)
else:
    pass