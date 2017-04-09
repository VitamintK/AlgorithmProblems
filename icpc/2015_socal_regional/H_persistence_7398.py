from functools import reduce
import operator
while(True):
    try:
        n = int(input())
        og = n
    except:
        break
    ans = 0
    while(n > 9):
        n = reduce(operator.mul, (int(x) for x in str(n)))
        ans+=1
    print(og, ans)
