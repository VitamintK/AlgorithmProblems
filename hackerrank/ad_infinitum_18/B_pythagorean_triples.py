#finding a pythagorean triple that A belongs to.
#very fun problem: https://www.hackerrank.com/contests/infinitum18/challenges/pythagorean-triple
a = int(input())

if a%2 == 1:
    print(a, (pow(a,2)-1)//2, (pow(a,2)-1)//2 + 1)
else:
    x = a//2
    import math
    for i in range(1,int(math.sqrt(x)+1)):
        if x%i == 0:
            j = x//i
            m = max(i,j)
            n = min(i,j)
            print(a, pow(m,2) - pow(n,2), pow(m,2) + pow(n,2))
            break