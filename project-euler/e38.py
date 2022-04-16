
from re import S


best = ""
argbest = None
for i in range(1,900000):
    s = ""
    for j in range(1,10):
        prod = j*i
        s += str(prod)
        if len(s) > 9:
            break
        if len(s) > len(set(s)):
            break
        if set(s) == set('123456789'):
            if s > best:
                best = s
                argbest = i
print(best, argbest)