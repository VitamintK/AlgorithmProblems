import math
import os
import random
import re
import sys

#
# Complete the 'performOperations' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER_ARRAY op
#

# def performOperations(N, op):
#     # Write your code here
#     m = {x for x in range(1, N+1)}
#     r = [x for x in range(1, N+1)]
#     ans = []
#     s = sum(r)
#     for o in op:
#         if o in m:
#             r[0], r[-1] = r[-1], r[0]
#             ans.append(s)
#         else:
#             m.remove(r[-1])
#             s -= r[-1]
#             r.pop()
#             r.append(o)
#             m.add(o)
#             s += o
#             ans.append(s)
#     return ans
            

if __name__ == '__main__':
    N = int(input())
    M = int(input())

    op = [int(x) for x in input().split()]
    m = {x for x in range(1, N+1)}
    r = [x for x in range(1, N+1)]
    ans = []
    s = sum(r)
    for o in op:
        # op.append(int(input()))
        # o = int(input())
        if o in m:
            r[0], r[-1] = r[-1], r[0]
            print(s)
        else:
            m.remove(r[-1])
            s -= r[-1]
            r.pop()
            r.append(o)
            m.add(o)
            s += o
            print(s)
    
