from collections import defaultdict
T = int(input())
for t in range(T):
    n = int(input())
    c = defaultdict(int)
    for i in range(n):
        s = input()
        for x in s:
            c[x] +=1
    for l in c:
        if c[l]%n != 0:
            print("NO")
            break
    else:
        print("YES")