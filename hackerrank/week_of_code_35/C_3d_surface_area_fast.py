#!/bin/python3

import sys

def surfaceArea(A):
    # Complete this function
    #this code is not that smart.  It's hacky and thus short, since I tried coding as fast as possible to get on the leaderboard.
    ans = 0
    #print(A)
    for i in range(len(A)):
        for j in range(len(A[0])):
            for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
                nx = j + dx
                ny = i + dy
                if 0 <= nx < len(A[0]) and 0<= ny < len(A):
                    if nx >= j and ny >= i:
                        #print(ny, nx)
                        ans += abs(A[i][j] - A[ny][nx])
                else:
                    ans += A[i][j]
                    
    return ans

if __name__ == "__main__":
    H, W = input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = []
    for A_i in range(H):
        A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
        A.append(A_t)
    result = surfaceArea(A)
    print(result + H*W + H*W)
