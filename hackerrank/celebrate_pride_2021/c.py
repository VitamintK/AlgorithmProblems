#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximumIslandSize' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY matrix as parameter.
#
import sys
# sys.setrecursionlimit(100000)
def dfs(matrix, islandID, r, c):
    stack = [(r,c)]
    matrix[r][c] = islandID
    sz = 1
    while len(stack) > 0:
        r,c = stack.pop()
        for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)]:
            nr = r + dr
            nc = c + dc
            if nr >= 0 and nr < len(matrix) and nc >= 0 and nc < len(matrix[r]) and matrix[nr][nc] == 1:
                matrix[nr][nc] = islandID
                sz += 1
                stack.append((nr,nc))
    return sz
            

def maximumIslandSize(matrix):
    matrix = [[int(x) for x in r] for r in matrix]
    # Write your code here
    islandSize = dict()
    islandID = 2
    # print(matrix)
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 1:
                sz = dfs(matrix, islandID, r, c)
                islandSize[islandID] = sz
                islandID += 1
    # print(islandSize)
    if len(islandSize.values()) == 0:
        return 1
    ans = max(islandSize.values())
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] != 0:
                continue
            a = 1
            islands = set()
            for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)]:
                nr = r + dr
                nc = c + dc
                if nr >= 0 and nr < len(matrix) and nc >= 0 and nc < len(matrix[r]):
                    if matrix[nr][nc] != 0:
                        islands.add(matrix[nr][nc])
                # print(islands)
            for isl in islands:
                a += islandSize[isl]
                # print(a)
            ans = max(ans, a)
    return ans
                
if __name__ == '__main__':