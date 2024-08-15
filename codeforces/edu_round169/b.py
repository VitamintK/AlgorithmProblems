T = int(input())
for t in range(T):
    l, r = map(int, input().split())
    L, R = map(int, input().split())
    if L < l:
        l, r, L, R = L, R, l, r
    if l == L and r == R:
        print(R - L)
    elif r < L:
        print(1)
    else:
        i = min(r, R) - max(l, L)
        if r == R or l == L:
            print(i + 1)
        else:
            print(i + 2)
