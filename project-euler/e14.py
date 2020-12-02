from functools import lru_cache
n = 1000000

@lru_cache
def collatz(i):
    if i == 1:
        return 1
    if i%2 == 0:
        return 1 + collatz(i//2)
    else:
        return 1 + collatz(3*i+1)

argmax = None
maxval = 0
for i in range(1,n+1):
    val = collatz(i)
    if val > maxval:
        maxval = val
        argmax = i
print(argmax)