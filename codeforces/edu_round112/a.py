T = int(input())
for t in range(T):
    n = int(input())
    if n%2==1:
        n += 1
    if n < 6:
        n = 6
    print(n * 2 + n//2)
    