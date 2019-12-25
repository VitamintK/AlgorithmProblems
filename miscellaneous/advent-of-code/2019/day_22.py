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
cards = list(range(10007))
# l = top, r = bottom
if True:
    while True:
        try:
            i = input().split()
            if i[0] == 'cut':
                v = int(i[1])
                cards = cards[v:] + cards[:v]
            elif i[2] == 'increment':
                v = int(i[-1])
                nc = [None for x in range(10007)]
                x = 0
                for i in cards:
                    nc[x%10007] = i
                    x += v
                cards = nc
            elif i[2] == 'new':
                cards.reverse()
            print(cards.index(2019))
        except EOFError:
            break
else:
    pass
print(cards.index(2019))
# t = [cards.index(i) for i in range(10007)]
# i = 0
# for j in range(2423):
#     cards = [t[card] for card in cards]
#     if cards == sorted(cards) and i != 0:
#         break
#     i+=1
# z