T = int(input())
for t in range(T):
    l,r = map(int, input().split())
    lmin = (r+2)//2
    l = max(lmin, l)
    print(r-l)