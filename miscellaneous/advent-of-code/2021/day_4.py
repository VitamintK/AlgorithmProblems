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

def check(mark):
    for row in mark:
        if all(row):
            return True
    for col in range(len(mark[0])):
        c = [mark[i][col] for i in range(len(mark))]
        if all(c):
            return True
    return False

def get_unmarked_sum(mark, board):
    ans = 0
    for r in range(len(mark)):
        for c in range(len(mark[0])):
            if mark[r][c] == 0:
                ans += board[r][c]
    return ans


# Oops I forgot about AOC for the first time ever, got distracted by the warriors-suns & lakers-clippers games OwO
# started solving at 10:24ish PM PT and finished at 10:36:55 PM PT
if True:
    ans = 0
    seq = get_ints(input())
    input()
    boards = []
    board = []
    while True:
        try:
            inp = input()
            if inp.strip() == '':
                boards.append(board)
                board = []
            else:
                board.append(get_ints(inp))
        except EOFError:
            break
    print(seq)
    print(boards)
    marks = [[[0 for x in row] for row in board] for board in boards]

    already_won = set()
    for num in seq:
        for bid, board in enumerate(boards):
            for r, row in enumerate(board):
                for c, col in enumerate(row):
                    if col == num:
                        marks[bid][r][c] = 1
                        win = check(marks[bid])
                        if win and bid not in already_won:
                            unmarked_sum = get_unmarked_sum(marks[bid], board)
                            print(unmarked_sum * num)
                            already_won.add(bid)
                            # exit() <--- part 1
else:
    pass