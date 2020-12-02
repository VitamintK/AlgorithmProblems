M = 112345678
N = 10001
sieve = [0 for i in range(M)]
primes = 0
for i in range(2,M):
    if sieve[i] == 0:
        for j in range(i*2, M, i):
            sieve[j] = 1
        primes += 1
        if primes == N:
            print(i)
            break