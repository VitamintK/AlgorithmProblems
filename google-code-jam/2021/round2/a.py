T, n = map(int, input().split())
for t in range(T):
    for i in range(1,n):
        print(f'M {i} {n}')
        m = int(input())
        if m != i:
            print(f'S {i} {m}')
            input()
    print('D')
    input()