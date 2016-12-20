n = int(input().strip())
import math
import sys
factor = 1
each_row_min = [10000000000]*n
for i in range(int(math.log(n, 2))+1):
    if factor >= n:
        break
    mask = []
    comp_mask = []
    for j in range(n):
        if (j//factor)%2 == 0:
            mask.append(j)
        else:
            comp_mask.append(j)
    print(len(mask))
    print(' '.join([str(x+1) for x in mask]))
    sys.stdout.flush()
    results = [int(x) for x in input().split()]
    for row, rowmin in enumerate(results):
        if row not in mask:
            each_row_min[row] = min(each_row_min[row], rowmin)
    #comp
    mask = comp_mask
    print(len(mask))
    print(' '.join([str(x+1) for x in mask]))
    sys.stdout.flush()
    results = [int(x) for x in input().split()]
    for row, rowmin in enumerate(results):
        if row not in mask:
            each_row_min[row] = min(each_row_min[row], rowmin)
    factor*=2
print(-1)
print(' '.join(str(x) for x in each_row_min))
sys.stdout.flush
