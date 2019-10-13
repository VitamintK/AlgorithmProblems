n = int(input())
#i dunno why this works but it does
import math
if n == 1:
    print(1)
else:
    print(int(math.log2(n-1))+2)