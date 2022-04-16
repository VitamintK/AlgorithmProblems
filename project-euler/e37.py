# another prime problem?
# damn, people in 2004 really liked primes

# not sure how to bound the answer...
cnt = 0
ans=0
M = 1000000
sieve = [-1 for i in range(M+1)]
for i in range(2,M+1):
    if sieve[i] != -1:
        continue
    for j in range(i, M+1, i):
        sieve[j] = i
for i in range(10, M+1):
    if sieve[i] != i:
        continue
    x = i
    fail = False
    digits=[]
    while x!=0:
        digits.append(x%10)
        if sieve[x]!=x:
            fail=True
            break
        x//=10
    x=0
    mult = 1
    for digit in digits:
        x+=mult*digit
        if sieve[x]!=x:
            fail=True
            break
        mult*=10
    if not fail:
        print(i)
        cnt +=1
        ans += i
print(cnt, ans)