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

def rotate(tile):
    return None

def get_h(tile):
    ans = []
    ans.append(tile[0])
    ans.append([tile[x][-1] for x in range(len(tile))])
    ans.append(list(reversed(tile[-1])))
    ans.append(list(reversed([tile[x][0] for x in range(len(tile))])))
    ans = [get_h_seq(x) for x in ans]
    return ans

def normalize(h):
    return min(''.join(h), ''.join(reversed(h)))

def orderless_match(a,b):
    a = normalize(a)
    b = normalize(b)
    return a== b

def get_h_seq(seq):
    # a, b = ''.join(seq), ''.join(reversed(seq))
    # return min(a,b)
    return ''.join(seq)

def opp(rot):
    return {1:3,3:1,2:0,0:2}[rot%4]

def find_match(inputtile, edgenum, vert=False):
    t, rot, flipped, flippedvert = inputtile
    tomatch = list(get_h(tiles[t]))[(edgenum-rot)%4]
    for tile in tiles:
        if tile == t:
            continue
        for i,h in enumerate(get_h(tiles[tile])):
            if orderless_match(h, tomatch):
                flip = False
                flipvert = False
                if vert:
                    flipvert = h == tomatch
                    flipvert = (flippedvert|flipped)^flipvert
                else:
                    flip = h == tomatch
                    flip = flip^(flippedvert|flipped)
                # print('lets flip', flip, flipped)
                # print('the match is',h,tomatch,sep='\n')
                return (tile, (-i)%4, flip, flipvert)

def rotate_once(tile):
    ntile = []
    for c in range(len(tile[0])):
        ntile.append([])
        for r in reversed(range(len(tile))):
            ntile[-1].append(tile[r][c])
    return ntile
def rotate(tile, rot, flip, flipvert):
    print(flipvert)
    # print('test')
    for i in range(rot):
        tile = rotate_once(tile)
    #     print_tile(tile)
    #     print()
    # print('end test')
    if flip:
        tile = [list(reversed(r)) for r in tile]
    if flipvert:
        tile = list(reversed(tile))
    return tile
def print_tile(tile):
    for r in tile:
        print(''.join(r))

WIDTH = 12 # 3 for the sample
if True:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    tiles = defaultdict(list)
    iid = None
    for inp in inps:
        if inp.count(':') > 0:
            iid = get_ints(inp)[0]
            continue
        if inp.strip() == '':
            continue
        tiles[iid].append(inp)
    print(len(tiles))
    visited = defaultdict(int)
    for tile in tiles:
        for h in get_h(tiles[tile]):
            # print(h)
            # print(visited[h])
            h = normalize(h)
            visited[h] +=1 
    cnts = Counter(visited.values())
    print(cnts)
    ans = 1
    for tile in tiles:
        cnt = 0
        rots = []
        for i,h in enumerate(get_h(tiles[tile])):
            h = normalize(h)
            if visited[h] == 1:
                cnt +=1
            else:
                rots.append(i)
        if cnt == 2:
            print('asdf')
            ans *= tile
            rot = rots[-1]
            if rots == [0,3]:
                rot = 0
            print(rots)
            corner = (tile, (2-rot)%4, False, False)
    print(ans)
    #pt 2
    grid = []
    print(corner)
    # print_tile(tiles[corner[0]])
    grid.append([corner])
    print_tile(rotate(tiles[corner[0]],corner[1],corner[2], 0))
    print()
    for r in range(1,WIDTH):
        # print(grid)
        tile, rots, flip,_ = find_match(grid[r-1][0], 2)
        # print(r, tile)
        print_tile(rotate(tiles[tile], rots, flip, 0))
        print()
        grid.append([(tile,(rots)%4, flip,0)])
    for r in range(WIDTH):
        print(r)
        for c in range(1,WIDTH):
            edgenum = 3 if grid[r][-1][2] else 1
            tile, rots, flip,flipvert = find_match(grid[r][-1], edgenum,True)
            grid[r].append((tile,(rots-1)%4,0,flipvert))
            print_tile(rotate(tiles[tile], (rots-1)%4, 0,flipvert))
            print()

    # for r in grid:
    #     for c in r:
    #         tile, rot, flip = c
    #         print_tile(rotate(tiles[tile], rot, flip))
    #         print()
    pictures = []
    for r in range(WIDTH):
        pictures.append([])
        for c in range(WIDTH):
            tile, rot, flip, flipvert = grid[r][c]
            toappend = rotate(tiles[tile], rot, flip, flipvert)
            toappend = toappend[1:-1]
            toappend = [x[1:-1] for x in toappend]
            pictures[r].append(toappend)
    # pictures = pictures[1:-1]
    # pictures = [x[1:-1] for x in pictures]
    biggrid = [[] for i in range(WIDTH*len(pictures[0][0]))]
    for bigr, r in enumerate(pictures):
        for c in r:
            for rn, row in enumerate(c):
                for char in row:
                    biggrid[bigr*len(pictures[0][0])+rn].append(char)
    print(len(biggrid), len(biggrid[0]))
    for row in biggrid:
        print(''.join(row))
    cmonster = [
'                  # ',
'#    ##    ##    ###',
' #  #  #  #  #  #   ']
    ccoords = []
    # cmonster = [' ####  ##   #']
    for r in range(len(cmonster)):
        for c in range(len(cmonster[0])):
            if cmonster[r][c] == '#':
                ccoords.append((r,c))
    print(ccoords)
    for i in range(2):
        for j in range(5):
            ispartof = [[0 for c in r] for r in biggrid]
            if i == 1 and j == 0:
                print('flippin')
                biggrid = rotate(biggrid, 0, True, False)
            biggrid = rotate_once(biggrid)
            for row in biggrid:
                print(''.join(row))
            for startr in range(len(biggrid)):
                for startc in range(len(biggrid)):
                    iscmonster = True
                    for dr,dc in ccoords:
                        nr, nc = startr+dr, startc+dc
                        if not is_grid_valid(len(biggrid),len(biggrid),nr,nc):
                            iscmonster = False
                            break
                        if biggrid[nr][nc] != '#':
                            iscmonster = False
                            break
                    if iscmonster:
                        print('found 1')
                        for dr, dc in ccoords:
                            nr, nc = startr+dr, startc+dc
                            ispartof[nr][nc] = 1
            ans = 0
            for r in range(len(biggrid)):
                for c in range(len(biggrid)):
                    if biggrid[r][c] == '#' and not ispartof[r][c]:
                        ans += 1
            print(ans)
else:
    pass