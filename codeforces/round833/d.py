# based on the code of https://codeforces.com/profile/pajenegod and https://codeforces.com/profile/conqueror_of_tourist
# for printing: they use print('\n'.join(map(str, out))) instead of for ...: print(ans)
# use pypy 3-64
import sys
input = sys.stdin.readline

T = int(input())
bigboss = pow(2,59)
for t in range(T):
    a,b,d = map(int, input().split())
    c = a|b
    deficit = (d - (c%d))%d
    bit = bigboss
    ans = c
    modpows = []
    while bit != 0:
        if bit&c == 0:
            modpows.append((bit%d, bit))
        bit //= 2
    modpows.sort(reverse=True)
    # while deficit != 0 and bit > 0:
    #     print(bit%d)
    #     if bit%d <= deficit and bit&c==0:
    #         deficit -= (bit%d)
    #         ans |= bit
    #     bit //= 2
    for modpow, bit in modpows:
        if modpow <= deficit:
            deficit -= modpow
            ans |= bit
    if deficit == 0:
        print(ans, (ans|a)%d, (ans|b)%d)
    else:
        print(-1, bin(ans))
    # ans = c
    # while ans%d != 0 and ans < bigboss:
    #     ans *= 2
    #     ans += 1
    # if ans%d==0:
    #     print(ans)
    # else:
    #     print(-1)