#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER t
#  3. INTEGER r
#  4. INTEGER_ARRAY a
#

#on LEFT, ~~only need to keep track of the rightmost blocker.~~
#nvm not true...nonblockers can strike through the side of the pyramid and become blockers.
#we know the precise interval at which they will be blockers... maintaining a stack of nonoverlapping intervals
#  is ezpz, but is there not an even simpler way? whatever...
#every time we tick, we subtract a constant amount from deficit

#~~on RIGHT, keep a deque of blockers in NONINCREASING order.  Left blocker = biggest blocker.~~
#on RIGHT, just keep a value "ticks_until_unblocked".  When adding a new guy into right, 
#the new guy's ticks_until_unblocked is the ticks until it's unblocked, or ticks until it's gone.  Max the value with that.
#

#I now see that an alternate approach, where I preprocess blocked intervals, by maintaining an array
#blocked_until, with n indices, where blocked_until[i] means how many ticks after i you are blocked, would be much easier
#from collections import deque
from collections import defaultdict

def solve(l, t, r, a):
    # Write your code here
    size_of_wall = (t-r+1) + (t-l+1)
    l_blocker = None
    r_blocker = None
    wall_deficit = 0
    ticks_until_unblocked = 0
    ans = None
    #blocked_intervals = deque()
    left_blockers = defaultdict(int)
    
    for i in range(len(a)):
        print(i, ticks_until_unblocked)
        #print(left_blockers)
        #process left_blockers
        ticks_until_unblocked = max(ticks_until_unblocked, left_blockers[i])
        #process a[i]
        wall_deficit += (r-a[i])
        if a[i] > r:
            ticks_until_unblocked = max(ticks_until_unblocked, min(a[i] - r, t-r+1))
        #process a[i-(t-r+2)] (this is the left middle peak)
        lmp = i-(t-r+1)
        if lmp >= 0 and a[lmp] > l:
            
            ##blockers have variable start, but all end at i+(size_of_wall).  end is exclusive.
            ##interval = (i + (t-a[i-(t-l+1)]), i + (size_of_wall))
            #for j in reversed(range(len(blocked_intervals))):
            #    if  blocked_intervals[j][1] >= interval[0]:
            #        ll = min(blocked_intervals[j][0], interval[0])
            print("blocker at", lmp, ": ", a[lmp])
            print("{} -> {}".format(i+(t-a[lmp])+1, a[lmp]-l))
            left_blockers[i+(t-a[lmp])+1] = max(left_blockers[i+(t-a[lmp])], a[lmp]-l)
        #update ans if unblocked
        if ticks_until_unblocked <= 0 and i >= size_of_wall-1:
            if ans is not None:
                ans = min(ans, wall_deficit)
                print(i, "!!!", wall_deficit)
            else:
                print(i, "!!!", wall_deficit)
                ans = wall_deficit
        #tick. process wall_deficit delta for left and wall_deficit delta for right
        wall_deficit -= min(t-l, max(0, i-(t-r)))
        wall_deficit += min(t-r, i+1)
        if i-size_of_wall+1 >= 0:
            wall_deficit -= (l-a[i-size_of_wall+1])
        ticks_until_unblocked-=1
        #-t+l+t-r+r-r
    if ans is None:
        return -1
    else:
        return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    l = int(first_multiple_input[1])

    t = int(first_multiple_input[2])

    r = int(first_multiple_input[3])

    a = list(map(int, input().rstrip().split()))

    result = solve(l, t, r, a)

    fptr.write(str(result) + '\n')

    fptr.close()
