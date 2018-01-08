#the mod inverse thing for modular "division" is unnecessary.  Since each combination would be less than
#10^9, and would be an integer, I could have just divided to get (p C q) and then mod multiplied.

MOD = 1000000007

s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
prefix = [{i: 0 for i in alphabet}]
for i in s:
    d = prefix[-1]
    p = {k:d[k] for k in d}
    p[i] += 1
    prefix.append(p)

def ee(a, b, x, y):
    xx = 0
    y = 0
    yy = 1
    x = 1
    while b:
        q = a//b
        t = b
        b = a%b
        a = t
        t = xx
        xx = x - q*xx
        x = t
        t = yy
        yy = y - q*yy
        y = t
    return a, x

def mod(a, b):
    return ((a%b) + b)%b

memo = dict()
def mod_inv(a, n):
    if a in memo:
        return memo[a]
    g, x = ee(a, n, 0, 0)
    if g > 1:
        return -1
    memo[a] = mod(x, n)
    return mod(x, n)

facts = [1]
for i in range(len(s)+1):
    facts.append((facts[-1]*(i+1))%MOD)

n = int(input())
for i in range(n):
    l, r = map(int, input().split())
    nums = [prefix[r][k] - prefix[l-1][k] for k in alphabet]
    nums.sort(reverse=True)
    #print(nums)
    middles = 0
    ans = 1
    m = 0
    for i in nums:
        m += i//2
        middles += i%2
    #print('m', m)
    for i in nums:
        if i <= 1:
            break
        #print(mod_inv(facts[0], MOD))
        #print(facts[1])
        #print(mod_inv(1, MOD))
        ans *= facts[m] * mod_inv(facts[i//2], MOD) * mod_inv(facts[m - i//2], MOD)
        ans %= MOD
        m -= i//2
    if middles > 0:
        ans *= middles
    ans %= MOD
    print(ans)