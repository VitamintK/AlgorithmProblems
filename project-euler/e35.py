M = 1000000
sieve = [-1 for i in range(M+1)]
for i in range(2,M+1):
    if sieve[i] != -1:
        continue
    for j in range(i, M+1, i):
        sieve[j] = i


def cyclic_shift(x, i):
    sx = str(x)
    return int(sx[i:] + sx[:i])

ans = 0
for i in range(2, M):
    x = i
    for j in range(len(str(i))):
        if sieve[x] != x:
            break
        x = cyclic_shift(i, j+1)
    else:
        print(i)
        ans += 1

print(ans)