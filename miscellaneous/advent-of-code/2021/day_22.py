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

def get_intersection_area_1(cube1, cube2):
    # print(f'{cube1=} {cube2=}')
    x,xx,y,yy,z,zz = cube1
    X,XX, Y,YY, Z, ZZ = cube2
    xf = max(x,X)
    xxf = min(xx, XX)
    yf = max(y,Y)
    yyf = min(yy,YY)
    zf = max(z,Z)
    zzf = min(zz,ZZ)
    if xf > xxf or yf > yyf or zf > zzf:
        return None, 0
    # print(f'{(xxf-xf+1) * (zzf-zf+1) * (yyf-yf+1)=}')
    return (xf,xxf,yf,yyf,zf,zzf), (xxf-xf+1) * (zzf-zf+1) * (yyf-yf+1) 

def get_intersection_area(cube, cubes):
    print(cube, cubes)
    ans = 0
    all_time_intersections_considered = set()
    for i in range(len(cubes)):
        intersection, intersection_area = get_intersection_area_1(cube, cubes[i])
        if intersection_area > 0:
            ans += intersection_area
            intersect_dict = {(i,):intersection}
            parity = -1
            while len(intersect_dict) > 0:
                # print(intersect_dict)
                new_intersect_dict = dict()
                for j in range(i):
                    for k,v in intersect_dict.items():
                        if j in k:
                            continue
                        new_k = tuple(sorted(k + (j,)))
                        if new_k in all_time_intersections_considered:
                            continue
                        all_time_intersections_considered.add(new_k)
                        # print(new_k)
                        intersection, intersection_area = get_intersection_area_1(v, cubes[j])
                        if intersection_area > 0:
                            new_intersect_dict[new_k] = intersection
                            ans += parity * intersection_area
                parity *= -1
                intersect_dict = new_intersect_dict
    
    return ans
    





if True:
    ans = 0
    inps = []
    while True:
        try:
            s = input()
            command = s.split()[0]
            inps.append((command, get_ints(s)))
        except EOFError:
            break
    
    # grid = defaultdict(bool)
    # for inp in inps:
    #     command = inp[0]
    #     x,xx,y,yy,z,zz = inp[1]
    #     x = max(-50,x)
    #     xx = min(51,xx)
    #     y = max(-50,y)
    #     yy = min(51,yy)
    #     z = max(-50,z)
    #     zz = min(51,zz)
    #     for i in range(x,xx+1):
    #         for j in range(y,yy+1):
    #             for k in range(z,zz+1):
    #                 if command=='on':
    #                     grid[(i,j,k)] = True
    #                 else:
    #                     grid[(i,j,k)] = False
    # for i in range(-50,51):
    #     for j in range(-50,51):
    #         for k in range(-50,51):
    #             if grid[(i,j,k)]:
    #                 ans +=1
    inps.reverse()
    added = []
    for inp in inps:
        cmd, cube = inp
        print(f'{inp=}')
        if cmd == 'on':
            _, area = get_intersection_area_1(cube, cube)
            print(f'command was on: {area}')
            ans += area
            intersection_area = get_intersection_area(cube, added)
            print(f'intersection area: {intersection_area}')
            ans -= intersection_area
        added.append(cube)
        print(f'-----{ans=}')
    print(ans)
else:
    pass