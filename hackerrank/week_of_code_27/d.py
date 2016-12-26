#!/bin/python3

import sys


g = int(input().strip())
for a0 in range(g):
    n = int(input().strip())
    p = [int(p_temp) for p_temp in input().strip().split(' ')]
    # your code goes here
    p = [x+2*(x%2)-1 for x in p]
    from functools import reduce
    print("L" if reduce(lambda a,b: a^b, p, 0)==0 else "W")
    
