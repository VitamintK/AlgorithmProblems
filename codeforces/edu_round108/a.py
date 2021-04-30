T = int(input())
for t in range(T):
    r, b, d = map(int, input().split())
    x, y = min(r,b), max(r,b)
    if y > (x*(d+1)):
        print("NO")
    else:
        print("YES")