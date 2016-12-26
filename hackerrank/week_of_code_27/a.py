#!/bin/python3

import sys


n = int(input().strip())
p = int(input().strip())
# your code goes here
from_back = n//2 - p//2
from_front = p//2
print(min(from_back, from_front))