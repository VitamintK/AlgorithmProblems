# based on the code of https://codeforces.com/profile/pajenegod and https://codeforces.com/profile/conqueror_of_tourist
# for printing: they use print('\n'.join(map(str, out))) instead of for ...: print(ans)
# use pypy 3-64
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n, x = map(int, input().split())
    xss = []
    for i in range(3):
        xss.append([int(x) for x in input().split()])
    bigaccum = 0
    for bs in xss:
        accum = 0
        for b in bs:
            if b != b & x:
                break
            accum |= b
        bigaccum |= accum
    # print(bigaccum)
    if bigaccum == x:
        print("Yes")
    else:
        print("No")
        