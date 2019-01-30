from collections import defaultdict
d = defaultdict(int)
n = int(input())
for i in range(n):
    w = input()
    k = ""
    print(d[w])
    for letter in w:
        k+=letter
        d[k]+=1
