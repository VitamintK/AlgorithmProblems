T = int(input())
for t in range(T):
    n = int(input())
    if n == 3:
        print('3 2 1')
        print('1 3 2')
        print('3 1 2')
    else:
        l = list(reversed(range(1,n+1)))
        for i in range(n):
            print(' '.join(str(x) for x in l))
            l = l[1:] + [l[0]]