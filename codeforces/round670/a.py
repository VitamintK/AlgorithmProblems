T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    for i in range(102):
        if xs.count(i) < 2:
            a = i
            for j in range(i, 102):
                if xs.count(j) < 1:
                    b = j
                    break
            break
    print(j+i)
            