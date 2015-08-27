inp = input()
from collections import defaultdict
d = defaultdict(int)
for i in inp:
    d[i]+=1
for i in sorted(d.items(), key=lambda x: x[1], reverse = True)[:3]:
    print("{} {}".format(i[0], i[1]))