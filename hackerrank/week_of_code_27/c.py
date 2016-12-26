#!/bin/python3

import sys


n,q = input().strip().split(' ')
n,q = [int(n),int(q)]
def hack(num):
    return [1,0,1,0,0,1,1][(num-1)%7]
m = []
m.append([[hack((i+1)*(i+1)*(j+1)*(j+1)) for i in range(n)] for j in range(n)])
diffs = [0]
for i in range(3):
    m.append([[m[-1][n-1-col][row] for col in range(n)] for row in range(n)])
    diffs.append(sum(sum(i!=j for i,j in zip(row1, row2)) for row1, row2 in zip(m[-1], m[0])))
#print(m)
#print(diffs)
for a0 in range(q):
    angle = int(input().strip())
    # your code goes here
    angle = (angle//90)%4
    print(diffs[angle])
    