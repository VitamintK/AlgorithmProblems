# diverse groupings math contest
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numberOfPartitions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
MOD = 1000000007
def numberOfPartitions(arr):
    data = [[0,0],[0,0]]
    # row 1: total is even, row 2: total is odd
    # col 1: ends in even, col2 : ends in odd
    cur_parity = 0
    for i in range(len(arr)):
        cur_parity = (cur_parity + arr[i])%2
        evens, odds = 0,0
        if cur_parity == 1:
            odds += 1
            odds += data[0][0]
            evens += data[1][1]
        else:
            evens += 1
            odds += data[1][0]
            evens += data[0][1]
        data[cur_parity][1] = (data[cur_parity][1]+odds)%MOD
        data[cur_parity][0] = (data[cur_parity][0]+evens)%MOD
        #print(i, evens, odds)
    return (evens + odds)%MOD
            
    # Write your code here
if __name__ == '__main__':