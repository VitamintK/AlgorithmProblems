n = int(input())

# hi = n
# lo = 0
# #binary search for how many printers we want to print?
# #binary search with exclusive hi and inclusive lo why is this still hard to code even after 5 years??
# while hi-1 > lo:
#     mid = (hi+lo)//2
#     if works(mid):
#         lo = mid
#     else:
#         hi = mid

# def works(mid):
#     statues = 0
#     printers = 1
#     while printers < mid:
import math
if n == 1:
    print(1)
else:
    print(int(math.log2(n-1))+2)