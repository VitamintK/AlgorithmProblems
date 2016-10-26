#transcribed from my c++ code because the resulting numbers can be
#too big to be stored in c++ long longs :(
fact = [1]
for i in range(1,200):
    fact.append(fact[-1]*i)
p = int(input())
for i in range(p):
    n, s = map(int, input().split())
    ans = 0
    for twos in range(0, s+1, 4):
        if s-twos <= twos/2:
            ones = s-twos
            res = fact[twos//4 + ones//2]//(fact[twos//4]*fact[ones//2])
            ans+= res*res
    print(n, ans)
