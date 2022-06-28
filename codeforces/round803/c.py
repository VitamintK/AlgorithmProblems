import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    pos = 0
    neg = 0
    zeroes = 0
    for x in xs:
        if x == 0:
            zeroes += 1
        elif x < 0 :
            neg += 1
        else:
            pos += 1
    if pos > 2:
        print("NO")
        continue
    if neg > 2:
        print("NO")
        continue
    if (zeroes > 0 and neg >= 2) or (zeroes > 0 and pos >= 2):
        print("NO")
        continue
    smaller = []
    for x in xs:
        if x != 0:
            smaller.append(x)
    for i in range(min(2, zeroes)):
        smaller.append(0)
    success = True
    for i in range(len(smaller)):
        for j in range(i+1, len(smaller)):
            for k in range(j+1, len(smaller)):
                l = smaller[i]+smaller[j]+smaller[k]
                if l not in smaller:
                    success = False
    if success:
        print("YES")
    else:
        print("NO")