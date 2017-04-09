n,k = [int(x) for x in input().split()]
balls = [int(x) for x in input().split()]

from collections import defaultdict
d = defaultdict(int)
for b in balls:
    d[b] += 1
correct_num = n/k
paint_needed = 0
for color, amount in d.items():
    if amount > correct_num:
        paint_needed += amount - correct_num

print(int(paint_needed))
