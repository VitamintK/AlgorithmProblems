n = int(input().strip())
s = input().strip()
from collections import Counter
c = Counter(s)
if n%4 != 0:
    print("===")
    exit()
correct = n//4
inputs = ['A']*(correct-c['A']) + ['G']*(correct-c['G']) + ['C']*(correct-c['C']) + ['T']*(correct-c['T'])
s = list(s)
for ind, i in enumerate(s):
    if i == '?':
        s[ind] = inputs.pop()
if(len(inputs) >  0):
    print("===")
else:
    print(''.join(s))
