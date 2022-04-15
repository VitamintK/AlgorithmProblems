# ok so you could do this in python by just actually doing it
# but I think that's clearly not the point here.
# I'm not actually sure how to do it without using bignums.
# I guess prime factorizing?
# yeah... that sounds right.
from collections import defaultdict
M = 100
sieve = [-1 for i in range(M+1)]
for i in range(2,M+1):
    if sieve[i] != -1:
        continue
    for j in range(i, M+1, i):
        sieve[j] = i

ans_set = set()
for a in range(2,101):
    prime_factors = defaultdict(int)
    n = a
    while n != 1:
        prime_factors[sieve[n]] += 1
        n //= sieve[n]
    for b in range(2, 101):
        key = [(k, v*b) for k,v in prime_factors.items()]
        ans_set.add(tuple(sorted(key)))
print(len(ans_set))

# it worked! I think there could also be a simpler answer, maybe O(1)-ish?