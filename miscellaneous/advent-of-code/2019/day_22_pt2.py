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
l = 119315717514047
#l = 10007
# cards = list(range(10007))
# l = top, r = bottom
instr = []
if True:
    while True:
        try:
            i = input().split()
            instr.append(i)
        except EOFError:
            break
else:
    pass

instr.reverse()
def get_position_before_process(final_pos):
    pos = final_pos
    for i in instr:
        if i[0] == 'cut':
            v = int(i[1])
            v = v%l
            if pos < l-v:
                pos = v + pos
            else:
                pos = pos - (l-v)
        elif i[2] == 'increment':
            v = int(i[-1])
            offset = pos%v
            coffset = 0
            dealt = 0
            while coffset != offset:
                # print(coffset, offset, pos, l, dealt)
                dealt += (l-coffset)//v + 1
                coffset = v - ((l-coffset)%v)
            dealt += (pos-offset)//v
            pos = dealt
        elif i[2] == 'new':
            pos = l-pos-1
        # print(i, pos)
    # print(pos)
    return pos

its = 0
pos = 2020
while pos != 2020 or its == 0:
    if its%1000 == 0:
        print(its, pos)
    pos = get_position_before_process(pos)
    its += 1
    break
print(its, pos)
# >>> 1, 46590577671461
# mod inverse of 2020 is 108506422313517
# 
# tr = (46590577671461 * 108506422313517)%119315717514047
# times = 101741582076661
# ans = 2020
# while times:
#     #print((2020 * pow(tr, 101741582076661, 119315717514047))%119315717514047)
#     if times%2:
#         ans *= 
#         #wtf
#     else: 
# 94017790677205 is too low
# 110324280691490 is too high
# 119315717514047 cards in the deck

# repeats = [None for i in range(49)]
# for i in range(49):

# t = [cards.index(i) for i in range(10007)]
# i = 0
# for j in range(2423):
#     cards = [t[card] for card in cards]
#     if cards == sorted(cards) and i != 0:
#         break
#     i+=1
# print(cards.index(2020))
# print(i)