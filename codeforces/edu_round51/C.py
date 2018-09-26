n = int(input())

xs = [int(x) for x in input().split()]

from collections import Counter

c = Counter(xs)

nice = []
pair = []
other = []
for i in c:
    if c[i] == 1:
        nice.append(i)
    elif c[i] == 2:
        pair.append(i)
    else:
        other.append(i)


bs = set()
for i in range(len(nice)):
    if i%2==1:
        bs.add(nice[i])
if len(nice)%2 != 0:
    if len(other) == 0:
        print("NO")
        exit()
    else:
        bs.add(other[0])

print("YES")
l = []
for i in xs:
    if i in bs:
        l.append("B")
        bs.remove(i)
    else:
        l.append("A")
print(''.join(l))
