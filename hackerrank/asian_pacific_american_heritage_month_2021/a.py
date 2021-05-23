#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'canBeEqualized' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY firstStrings
#  2. STRING_ARRAY secondStrings
#

def canBeEqualized(firstStrings, secondStrings):
    # Write your code here
    anss = []
    for firstString, secondString in zip(firstStrings, secondStrings):
        ans = False
        for i in 'abcdefghijklmnopqrstuvwxyz':
            for j in 'abcdefghijklmnopqrstuvwxyz':
                if firstString.replace(i, j) == secondString:
                    ans = True
                if secondString.replace(i, j) == firstString:
                    ans = True
        anss.append("YES" if ans else "NO")
    return anss

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    firstStrings_count = int(input().strip())

    firstStrings = []

    for _ in range(firstStrings_count):
        firstStrings_item = input()
        firstStrings.append(firstStrings_item)

    secondStrings_count = int(input().strip())

    secondStrings = []

    for _ in range(secondStrings_count):
        secondStrings_item = input()
        secondStrings.append(secondStrings_item)

    result = canBeEqualized(firstStrings, secondStrings)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
