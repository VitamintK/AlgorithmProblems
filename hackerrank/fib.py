b, a, n = [int(x) for x in input().split()]
for i in range(n-2):
    new = a*a + b
    b = a
    a = new
print(a)
