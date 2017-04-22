n = int(input())
a = map(int, input().split())
import math
def get_primes(num):
    p = num
    primes = []
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            primes.append(i)
            while(p%i == 0):
                p//=i
    if(p != 1):
        primes.append(p)
    return primes
    
print(get_primes(1))
