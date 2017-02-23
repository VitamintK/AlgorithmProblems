a, b = input().strip().split()
n = int(input())
for i in range(n):
    print(a, b)
    c, d = input().strip().split()
    if a == c:
        a = d
    else:
        b = d
print(a, b)
