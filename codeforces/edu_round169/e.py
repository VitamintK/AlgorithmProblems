import sys
input = sys.stdin.readline

T = int(input())
sieve = [-1 for x in range(10000001)]
sieve[1] = 1
for i in range(2, len(sieve)):
    if sieve[i] == -1:
        if i == 2:
            primes = 0
        else:
            primes += 1
        sieve[i] = primes
        for j in range(i*2, len(sieve), i):
            if sieve[j] == -1:
                sieve[j] = primes
        if i == 2:
            primes = 1
        
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        ans ^= sieve[xs[i]]
    if ans == 0:
        print("Bob")
    else:
        print("Alice")