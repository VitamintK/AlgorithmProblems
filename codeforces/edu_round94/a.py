T =int(input())
for t in range(T):
    n = int(input())
    s = input()
    g = s[n-1]
    print(''.join(g*n))