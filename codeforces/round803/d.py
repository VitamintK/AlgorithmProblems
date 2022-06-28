import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    l = 0
    r = n
    while r-l > 1:
        mid = l + (r-l)//2
        print('?', l+1, mid+1-1)
        sys.stdout.flush()
        xs = input()
        if xs == '-1':
            exit()
        xs = [int(x) for x in xs.split()]
        correct = 0
        for x in xs:
            if l+1 <= x <= mid+1-1:
                correct += 1
        if correct%2==1:
            r = mid
        else:
            l = mid
    print('!', l+1)
    sys.stdout.flush()