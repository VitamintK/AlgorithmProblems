#### ?????
import math
T = int(input())
def is_square(n):
    return n//math.sqrt(n) == math.sqrt(n)

for t in range(T):
    n = int(input())
    if(n%2 == 1):
        print("NO")
        continue
    while(n%2==0):
        n//=2
    if is_square(n):
        print("YES")
    else:
        print("NO")