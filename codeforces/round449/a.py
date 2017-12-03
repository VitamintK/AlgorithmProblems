n, m = map(int, input().split())
s = list(input())
for i in range(m):
    l, r, c1, c2 = input().split()
    l, r = map(int, (l,r))
    for j in range(l-1, r):
        if s[j] == c1:
            s[j] = c2
print(''.join(s))
