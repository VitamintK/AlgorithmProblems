from collections import defaultdict
squares = dict()
for i in range(2000):
    squares[i*i] = i
perims = defaultdict(int)
for a in range(1,1001):
    for b in range(a+1, 1001):
        if a*a+b*b not in squares:
            continue
        c = squares[a*a+b*b]
        perims[a+b+c] += 1
for perim, v in sorted(perims.items(), key=lambda x:x[1]):
    if v >1 and perim <= 1000:
        print(perim, v)