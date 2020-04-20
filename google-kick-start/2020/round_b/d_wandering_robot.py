# wow, google code jam just had a pascal triangle problem xD

# update after contest: ok fuck this problem... 
# i think my solution is correct but the numbers get 
# too outrageously big/small so the fix is to 
# store everything as logs.
# it was a good learning experience tho

T = int(input())
# fact_cache = [1]
# for i in range(1,200005):
#     if i%10000 == 0:
#         print(i)
#     fact_cache.append(fact_cache[-1] * i)
# def fact(x):
#     return fact_cache[x]
prob_cache = dict()
def prob(r, c):
    print('calc', r, c)
    if (r-1, c) in prob_cache:
        ans = prob_cache[(r-1, c)] * (r+c) / (r*2)
        prob_cache[(r,c)] = ans
        return ans
    if (r, c-1) in prob_cache:
        ans = prob_cache[(r, c-1)] * (r+c) / (c*2)
        prob_cache[(r,c)] = ans
        return ans
    # 0-indexed
    base = r + c
    # base choose r (or c)
    # b!/(b-r)! / r!
    # r = min(r, c)
    # combos = (fact(base)/fact(base-r))/fact(r)
    combos = 1
    ASDF = 1
    QWERT = 0
    for i in range(base - r + 1, base+1):
        combos *= i
        combos /= ASDF
        # combos /= 2
        ASDF += 1
        # QWERT += 1
    # for i in range(1, r+1):
    #     combos//= i
    # for i in range(QWERT, base):
        # combos /= 2
    ans = combos
    prob_cache[(r,c)] = ans
    return ans

for t in range(T):
    w, h, l, u, r, d = map(int, input().split())
    l -= 1
    r -= 1
    u -= 1
    d -= 1
    ans = 0
    for i in range(l, r+1):
        if u == 0:
            break
        p = prob(u-1, i)
        if i == w-1:
            for j in range(0, u-1):
                p0 = prob(j, i)/2
                #print('-', j, i, p0)
                p += p0
        else:
            p /= 2
        print(u, i, p)
        ans += p
    for i in range(u, d+1):
        if l == 0:
            break
        p = prob(i, l-1)
        if i == h-1:
            for j in range(0, l-1):
                p += prob(i, j)/2
        else:
            p /= 2
        ans += p
    print("Case #{}: {}".format(t+1, 1- ans))
