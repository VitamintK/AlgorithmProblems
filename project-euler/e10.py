M = 2000000 + 1
N = 10001
sieve = [0 for i in range(M)]
primesum = 0
for i in range(2,M):
    if sieve[i] == 0:
        for j in range(i*2, M, i):
            sieve[j] = 1
        primesum += i
print(primesum)