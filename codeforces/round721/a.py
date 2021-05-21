T = int(input())
for t in range(T):
    n = int(input())
    m = 1
    while m*2 <= n:
        m *=2
    print(m - 1)