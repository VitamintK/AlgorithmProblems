import sys
input = sys.stdin.readline
import math
from decimal import *
getcontext().prec = 100
T = int(input())
for t in range(T):
    n = int(input())
    # print(math.sqrt(n))
    d = math.ceil(Decimal(n).sqrt()) - 1
    print(d)