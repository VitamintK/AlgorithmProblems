THRESH = 50000000
sievelen = 8000
sieve = [0 for i in range(sievelen)]
primos = []
for i in range(2,sievelen):
    if sieve[i] == 0:
        primos.append(i)
        for j in range(i*2, sievelen, i):
            sieve[j] = i

### naive
# print(len(primos))
# s = set()
# for i in primos:
#     for j in primos:
#         for k in primos:
#             n = i*i + j*j*j + k*k*k*k
#             if n < THRESH:
#                 s.add(n)
# print(len(s))
#############

### dp, top-down
# cache = dict()
# def solve(n, power = 4):
#     if (n, power) in cache:
#         return cache[(n, power)]
#     if power < 2 :
#         return n == 0
#     if n < 0:
#         return False
#     if power == 4 and n%1000 == 0:
#         print(n)
#     for i in primos:
#         if solve(n - pow(i, power), power-1):
#             cache[(n, power)] = True
#             return True
#             # can short circuit here, but saving to cache is slightly nicer if we don't
#     cache[(n, power)] = False
#     return False
# ans = sum(solve(n) for n in range(1,THRESH))
# print(ans)
#############

# dp, sparse, bottom-up
ans = set()
seen = set()
frontier = [(0,2)]
cnt = 0 #debug
while len(frontier) > 0:
    n, power = frontier.pop()
    if (n, power) in seen:
        continue
    cnt+=1 #debug
    if cnt%10000 == 0: #debug
        print(n, power) #debug
    seen.add((n, power))
    if n > THRESH:
        continue
    if power == 5:
        ans.add(n)
        continue
    for i in primos:
        nex = n + pow(i, power)
        if nex < THRESH:
            frontier.append((n + pow(i, power), power+1))
print(len(ans))
