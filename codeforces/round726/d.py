import sys
sys.setrecursionlimit(11234567)
import math
T = int(input())
from functools import lru_cache
@lru_cache(maxsize = 11234567)
def wins(n):
    # print(n)
    if n in [1,2]:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0 and not wins(n-i):
            return True
    return False

for t in range(T):
    n = int(input())
    print("Alice" if wins(n) else "Bob")
# alices = []
# for i in range(1,69):
#     if wins(i):
#         alices.append(i)
#     # print(i, wins(i))
# print(alices)