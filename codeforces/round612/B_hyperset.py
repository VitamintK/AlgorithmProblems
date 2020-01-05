n, k = map(int, input().split())
cards = set()
clist = []
for i in range(n):
    s = input()
    cards.add(s)
    clist.append(s)

def ex(a,b):
    for i in 'SET':
        if i not in (a,b):
            return i

ans = 0
for a in range(len(clist)):
    for b in range(a+1, len(clist)):
        c1, c2 = clist[a], clist[b]
        complement = []
        for i in range(k):
            if c1[i]==c2[i]:
                complement.append(c1[i])
            else:
                complement.append(ex(c1[i], c2[i]))
        if ''.join(complement) in cards:
            ans += 1
print(ans//3)