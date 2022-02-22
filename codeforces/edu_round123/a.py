from collections import defaultdict
n = int(input())
for i in range(n):
    s = input()
    keys = defaultdict(bool)
    for x in s:
        if x==x.lower():
            keys[x] = True
        else:
            if not keys[x.lower()]:
                print("NO")
                break
    else:
        print("YES")
