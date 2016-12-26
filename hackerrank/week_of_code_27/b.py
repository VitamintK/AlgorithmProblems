#!/bin/python3

import sys


n,p = input().strip().split(' ')
n,p = [int(n),int(p)]
a = [(int(a_temp)+p-1)//p for a_temp in input().strip().split(' ')]
# your code goes here
a.sort()
for ind, i in enumerate(a):
    if ind > 0 and a[ind-1] >= a[ind]:
        a[ind] = a[ind-1]+1
print(sum(a))